#!/usr/bin/env python3
"""
Topic classification of the corpus.

PRIMARY analysis: each original-language document is classified with category prompts
written in its OWN language. The category prompts are the full "name: key terms" phrases
in `category_descriptions.csv`; an English template was translated into Finnish, Danish,
Norwegian and Swedish and verified by a native speaker of each language. Prompt and document
therefore share a language. This produces the reported distribution (Figure 2, Table A1) and
the per-document label written into the released data by write_topic_labels.py.

As a secondary check (cat_orig_en vs cat_trans), the original text and its English machine
translation are both classified with the full English prompt; the agreement between them
(topic_agreement.csv) measures how much machine translation affects the analysis.

Method: cosine similarity between each document embedding ("passage: ...") and the category
prompt embeddings ("query: ..."); argmax = predicted category. Text is Markdown-stripped and
truncated to the first N words (fair across languages) before embedding.

Outputs to <output_dir>:
  - topic_per_doc.csv          per-doc: native (primary) + English-prompt + translation categories/scores
  - topic_agreement.csv        translation check (orig vs translation, full English prompt), overall + per language
  - appendix_category_frequencies_originals.tex   category x language (native-prompt classification)
and a Figure 2 (native-prompt) PDF to <figures_dir>. Agreement and the prompt-language side-note
are printed to the log.
"""
import argparse
import csv
import json
import logging
import os
from glob import glob

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("topicclass")

DOMAIN_LANG = {"www.dna.fi": "Finnish", "www.telenor.dk": "Danish",
               "www.telenor.no": "Norwegian", "www.telenor.se": "Swedish"}
LANG_ORDER = ["Finnish", "Danish", "Norwegian", "Swedish"]
LANG_COL = {"Finnish": "finnish", "Danish": "danish", "Norwegian": "norwegian", "Swedish": "swedish"}
LANG_COLORS = {"Finnish": "#001845", "Danish": "#5B9BD5", "Norwegian": "#70CEC8", "Swedish": "#78C850"}
CATEGORY_COLORS = ["#001845", "#3B6CB4", "#5B9BD5", "#8DB4E2", "#70CEC8",
                   "#78C850", "#B8CCE8", "#8B7BBC", "#D4A0B8", "#B0B0B0"]

PROMPTS_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "category_descriptions.csv")

try:
    import markdown as _md
    from bs4 import BeautifulSoup

    def strip_md(t):
        import re
        html = _md.markdown(t or "", extensions=["tables", "fenced_code"])
        return re.sub(r"\s+", " ", BeautifulSoup(html, "html.parser").get_text(" ")).strip()
except ImportError:
    import re

    def strip_md(t):
        t = re.sub(r"```.*?```", " ", t or "", flags=re.S)
        t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[#>*_~|`]", " ", t)
        return re.sub(r"\s+", " ", t).strip()


def truncate_words(text, n):
    return " ".join(text.split()[:n])


def load_prompts(path):
    """Return (cat_keys, {column: [full prompt per category]}) from category_descriptions.csv."""
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cat_keys = [r["category"] for r in rows]
    cols = ["english", "finnish", "danish", "norwegian", "swedish"]
    prompts = {c: [r[c] for r in rows] for c in cols}
    for c in cols:
        missing = sum(1 for p in prompts[c] if not str(p).strip())
        if missing:
            log.warning("%s: %d empty prompt(s)", c, missing)
    return cat_keys, prompts


def load_docs(data_dir, max_words):
    trans_dir = os.path.join(data_dir, "translations")
    docs = []
    for domain, lang in DOMAIN_LANG.items():
        for fp in sorted(glob(os.path.join(data_dir, domain, "*.html.json"))):
            with open(fp, encoding="utf-8") as f:
                d = json.load(f)
            raw = (d.get("annotations", {}).get("content_selection", {})
                   .get("selected_span", {}).get("text", "") or "")
            if not raw.strip():
                continue
            fname = os.path.basename(fp)
            base = fname.replace(".html.json", "")
            tpath = os.path.join(trans_dir, domain, base + "_ENG.md")
            trans = None
            if os.path.exists(tpath):
                with open(tpath, encoding="utf-8") as f:
                    trans = f.read()
            docs.append({
                "domain": domain, "language": lang, "file": fname,
                "orig": truncate_words(strip_md(raw), max_words),
                "trans": truncate_words(strip_md(trans), max_words) if trans else None,
            })
    log.info("loaded %d documents (%d with translations)",
             len(docs), sum(1 for d in docs if d["trans"]))
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--settings", default="settings.json")
    ap.add_argument("--prompts", default=PROMPTS_CSV)
    args = ap.parse_args()
    cfg = json.load(open(args.settings))
    data_dir, out_dir, fig_dir = cfg["data_dir"], cfg["output_dir"], cfg["figures_dir"]
    max_words = cfg.get("max_words", 400)
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(fig_dir, exist_ok=True)

    cat_keys, prompts = load_prompts(args.prompts)

    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity

    docs = load_docs(data_dir, max_words)
    df = pd.DataFrame(docs).reset_index(drop=True)

    log.info("loading multilingual-e5-large ...")
    model = SentenceTransformer("intfloat/multilingual-e5-large")

    def embed(texts, prefix):
        return model.encode([prefix + t for t in texts], batch_size=32,
                            show_progress_bar=False, normalize_embeddings=True)

    cat_emb_en = embed(prompts["english"], "query: ")
    cat_emb_lang = {lang: embed(prompts[LANG_COL[lang]], "query: ") for lang in LANG_ORDER}

    # ── embed originals once, reuse for both the native (primary) and English-prompt passes ──
    log.info("embedding originals (n=%d) ...", len(df))
    orig_emb = embed(df["orig"].tolist(), "passage: ")

    # English-full prompt on originals (the starting point) → cat_orig_en
    sims_en = cosine_similarity(orig_emb, cat_emb_en)
    df["cat_orig_en"] = [cat_keys[i] for i in sims_en.argmax(1)]
    df["score_orig_en"] = sims_en.max(1)

    # PRIMARY: native-language prompt on originals → cat_orig
    df["cat_orig"] = None
    df["score_orig"] = 0.0
    for lang in LANG_ORDER:
        mask = (df["language"] == lang).values
        if not mask.any():
            continue
        sims = cosine_similarity(orig_emb[mask], cat_emb_lang[lang])
        df.loc[mask, "cat_orig"] = [cat_keys[i] for i in sims.argmax(1)]
        df.loc[mask, "score_orig"] = sims.max(1)

    # English-full prompt on the English translations → cat_trans (translation check baseline)
    tmask = df["trans"].notna()
    log.info("embedding translations (n=%d) ...", int(tmask.sum()))
    trans_emb = embed(df.loc[tmask, "trans"].tolist(), "passage: ")
    sims_t = cosine_similarity(trans_emb, cat_emb_en)
    df.loc[tmask, "cat_trans"] = [cat_keys[i] for i in sims_t.argmax(1)]
    df.loc[tmask, "score_trans"] = sims_t.max(1)

    df.drop(columns=["orig", "trans"]).to_csv(os.path.join(out_dir, "topic_per_doc.csv"), index=False)

    # ── translation check: cat_orig_en vs cat_trans, full English prompt baseline ──
    both = df[tmask].copy()
    both["agree"] = both["cat_orig_en"] == both["cat_trans"]
    rows = [{"language": "ALL", "n": len(both), "agreement_pct": round(100 * both["agree"].mean(), 1)}]
    for lang in LANG_ORDER:
        s = both[both["language"] == lang]
        rows.append({"language": lang, "n": len(s),
                     "agreement_pct": round(100 * s["agree"].mean(), 1) if len(s) else 0})
    pd.DataFrame(rows).to_csv(os.path.join(out_dir, "topic_agreement.csv"), index=False)

    # ── crosstab (native primary) → LaTeX appendix table ──
    ct = pd.crosstab(df["cat_orig"], df["language"], margins=True).reindex(columns=[*LANG_ORDER, "All"])
    order = (ct.drop("All").drop(columns="All").sum(1).sort_values(ascending=False).index.tolist())
    if "Other" in order:
        order.remove("Other"); order.append("Other")
    lines = [r"\begin{table}[h]", r"\centering",
             r"\caption{Content category distribution by language, zero-shot classification of the "
             r"\emph{original-language} documents with multilingual-e5-large using native-language "
             r"category prompts.}",
             r"\label{tab:categories}", r"\begin{tabular}{lrrrrr}", r"\toprule",
             r"\textbf{Category} & \textbf{FI} & \textbf{DK} & \textbf{NO} & \textbf{SE} & \textbf{Total} \\",
             r"\midrule"]
    for cat in order:
        v = [int(ct.at[cat, l]) if l in ct.columns else 0 for l in LANG_ORDER]
        cat_esc = cat.replace("&", r"\&")
        tot = int(ct.at[cat, "All"])
        lines.append(f"{cat_esc} & {v[0]} & {v[1]} & {v[2]} & {v[3]} & {tot} \\\\")
    lines += [r"\midrule",
              r"\textbf{Total} & \textbf{" + r"} & \textbf{".join(str(int(ct.at['All', l])) for l in LANG_ORDER)
              + r"} & \textbf{" + str(int(ct.at['All', 'All'])) + r"} \\",
              r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    open(os.path.join(out_dir, "appendix_category_frequencies_originals.tex"), "w").write("\n".join(lines) + "\n")

    # ── Figure 2 (native primary): normalized stacked bars ──
    ctp = pd.crosstab(df["cat_orig"], df["language"], normalize="columns") * 100
    colors = {c: CATEGORY_COLORS[i % len(CATEGORY_COLORS)] for i, c in enumerate(order)}
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(LANG_ORDER)); bottom = np.zeros(len(LANG_ORDER))
    for cat in order:
        vals = np.array([ctp.at[cat, l] if (cat in ctp.index and l in ctp.columns) else 0 for l in LANG_ORDER], float)
        ax.bar(x, vals, 0.6, bottom=bottom, label=cat, color=colors[cat]); bottom += vals
    ax.set_xticks(x); ax.set_xticklabels(LANG_ORDER)
    ax.set_ylabel("Percentage of documents (%)"); ax.set_xlabel("Language")
    ax.set_title("Content Category Distribution by Language (Native-language prompts, Normalized)")
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(fig_dir, "figure2_content_categories_originals.pdf"), dpi=300, bbox_inches="tight")

    # ── log summary ──
    log.info("=" * 64)
    log.info("PRIMARY = native-language prompts on original text. Category counts:")
    for cat in order:
        log.info("   %-38s %4d", cat, int(ct.at[cat, "All"]))
    log.info("TRANSLATION CHECK cat_orig_en vs cat_trans, full English prompt:")
    for r in rows:
        log.info("   %-10s n=%4d  agreement=%5.1f%%", r["language"], int(r["n"]), r["agreement_pct"])
    log.info("=" * 64)
    log.info("done")


if __name__ == "__main__":
    main()
