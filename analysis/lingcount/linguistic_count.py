#!/usr/bin/env python3
"""
Linguistic corpus-size counter.

Reports corpus size/length in linguistic units (spaCy word tokens) plus characters,
computed on Markdown-stripped prose.

Methods (per document):
  - chars        : character count of the stripped prose (assumption-free anchor)
  - spacy_trained: spaCy trained pipelines (fi/da/sv/nb_core_news_sm); tokens / words
                   (non-PUNCT).
  - spacy_blank  : spacy.blank(lang), is_punct filter — lightweight, no model download;
                   validates the trained pipeline.

Reads data/<domain>/*.html.json, language inferred from the domain, text taken from
annotations.content_selection.selected_span.text (same source as analysis/common.py).

Outputs to <output_dir>:
  - linguistic_counts_per_doc.csv   (every metric, per document)
  - linguistic_counts_summary.csv   (per language + total: total/mean/median/IQR per method)
  - table4_token_stats_linguistic.tex (draft LaTeX table: spaCy words + characters)
and prints per-language word/character totals to the log.
"""

import argparse
import json
import logging
import os
import re
from glob import glob

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("lingcount")

# domain -> (paper language label, ISO code for spaCy)
DOMAIN_LANG = {
    "www.dna.fi":     ("Finnish",   "fi"),
    "www.telenor.dk": ("Danish",    "da"),
    "www.telenor.no": ("Norwegian", "nb"),  # Telenor Norway = Bokmål
    "www.telenor.se": ("Swedish",   "sv"),
}
LANG_ORDER = ["Finnish", "Danish", "Norwegian", "Swedish"]
SPACY_MODEL = {"fi": "fi_core_news_sm", "da": "da_core_news_sm",
               "sv": "sv_core_news_sm", "nb": "nb_core_news_sm"}


# ── markdown to plain prose ────────────────────────────────────────────────────
try:
    import markdown as _md
    from bs4 import BeautifulSoup

    def strip_markdown(text: str) -> str:
        """Render markdown to HTML then extract text: drops heading markup, list
        bullets, table pipes, code fences, and LINK TARGETS/URLs (keeps link text)."""
        html = _md.markdown(text or "", extensions=["tables", "fenced_code"])
        prose = BeautifulSoup(html, "html.parser").get_text(separator=" ")
        return re.sub(r"\s+", " ", prose).strip()
except ImportError:
    log.warning("markdown/bs4 unavailable — falling back to regex markdown stripping")

    def strip_markdown(text: str) -> str:
        t = text or ""
        t = re.sub(r"```.*?```", " ", t, flags=re.S)         # fenced code
        t = re.sub(r"`([^`]*)`", r"\1", t)                    # inline code
        t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)      # links/images -> text
        t = re.sub(r"[#>*_~|]", " ", t)                       # md symbols + table pipes
        t = re.sub(r"https?://\S+", " ", t)                   # bare URLs
        return re.sub(r"\s+", " ", t).strip()


# ── corpus loading ────────────────────────────────────────────────────────────
def load_docs(data_dir: str):
    docs = []
    for domain, (lang, iso) in DOMAIN_LANG.items():
        ddir = os.path.join(data_dir, domain)
        if not os.path.isdir(ddir):
            log.warning("missing domain dir: %s", ddir)
            continue
        for fp in sorted(glob(os.path.join(ddir, "*.html.json"))):
            with open(fp, encoding="utf-8") as f:
                d = json.load(f)
            raw = (d.get("annotations", {}).get("content_selection", {})
                   .get("selected_span", {}).get("text", "") or "")
            if not raw.strip():
                continue
            docs.append({"domain": domain, "language": lang, "iso": iso,
                         "file": os.path.basename(fp),
                         "prose": strip_markdown(raw)})
    log.info("loaded %d documents", len(docs))
    return docs


# ── spaCy backends ────────────────────────────────────────────────────────────
def spacy_pipe(iso: str, trained: bool):
    import spacy
    if trained:
        return spacy.load(SPACY_MODEL[iso], disable=["ner", "lemmatizer"])
    return spacy.blank(iso)


def spacy_metrics(nlp, texts):
    out = []
    for doc in nlp.pipe(texts, batch_size=64):
        tokens = sum(1 for t in doc if not t.is_space)
        words = sum(1 for t in doc if not t.is_space and not t.is_punct)
        out.append((tokens, words))
    return out


# ── aggregation + output ──────────────────────────────────────────────────────
def agg(series):
    a = np.asarray(series, dtype=float)
    if a.size == 0:
        return dict(total=0, mean=0, median=0, iqr=0)
    return dict(total=int(a.sum()), mean=round(a.mean(), 1),
                median=round(float(np.median(a)), 1),
                iqr=round(float(np.percentile(a, 75) - np.percentile(a, 25)), 1))


def build_summary(df, metric_cols):
    rows = []
    for lang in LANG_ORDER + ["TOTAL"]:
        sub = df if lang == "TOTAL" else df[df["language"] == lang]
        row = {"language": lang, "docs": len(sub)}
        for col in metric_cols:
            if col in sub:
                s = agg(sub[col])
                row[f"{col}_total"] = s["total"]
                row[f"{col}_mean"] = s["mean"]
                row[f"{col}_median"] = s["median"]
                row[f"{col}_iqr"] = s["iqr"]
        rows.append(row)
    return pd.DataFrame(rows)


def fmt(n):
    n = int(round(n))
    return f"{n:,}".replace(",", "{,}") if abs(n) >= 1000 else str(n)


def write_latex(summary, path, words_col, char_col):
    lab = {"Finnish": "DNA FI", "Danish": "Telenor DK",
           "Norwegian": "Telenor NO", "Swedish": "Telenor SE", "TOTAL": "Total"}
    L = [r"\begin{table*}[t]", r"\centering",
         r"\caption{Corpus size and document length by language "
         r"(spaCy word tokens and characters).}",
         r"\label{tab:token_stats}", r"\begin{tabular}{lrrrr}", r"\toprule",
         r"\textbf{Language} & \textbf{Docs} & \textbf{Words} & \textbf{Median words/doc} "
         r"& \textbf{Characters} \\", r"\midrule"]
    for _, r in summary.iterrows():
        line = (f"{lab.get(r['language'], r['language'])} & {int(r['docs'])} & "
                f"{fmt(r.get(words_col + '_total', 0))} & {fmt(r.get(words_col + '_median', 0))} & "
                f"{fmt(r.get(char_col + '_total', 0))} \\\\")
        if r["language"] == "TOTAL":
            L.append(r"\midrule")
            line = (r"\textbf{Total} & \textbf{" + str(int(r['docs'])) + r"} & \textbf{"
                    + fmt(r.get(words_col + '_total', 0)) + r"} & \textbf{"
                    + fmt(r.get(words_col + '_median', 0)) + r"} & \textbf{"
                    + fmt(r.get(char_col + '_total', 0)) + r"} \\")
        L.append(line)
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--settings", default="settings.json")
    args = ap.parse_args()
    with open(args.settings) as f:
        cfg = json.load(f)
    data_dir = cfg["data_dir"]
    out_dir = cfg["output_dir"]
    methods = cfg.get("methods", ["chars", "spacy_trained", "spacy_blank"])
    os.makedirs(out_dir, exist_ok=True)

    docs = load_docs(data_dir)
    df = pd.DataFrame(docs)
    df["chars"] = df["prose"].str.len()

    # spaCy word counts, grouped per language
    for lang in LANG_ORDER:
        mask = df["language"] == lang
        iso = DOMAIN_LANG[[d for d, (l, i) in DOMAIN_LANG.items() if l == lang][0]][1]
        texts = df.loc[mask, "prose"].tolist()
        for tag, trained in (("spacy_trained", True), ("spacy_blank", False)):
            if tag not in methods:
                continue
            try:
                res = spacy_metrics(spacy_pipe(iso, trained), texts)
                df.loc[mask, f"{tag}_tokens"] = [r[0] for r in res]
                df.loc[mask, f"{tag}_words"] = [r[1] for r in res]
                log.info("%s [%s] ok (%d docs)", tag, iso, len(texts))
            except Exception as e:  # missing model etc. — keep going
                log.warning("%s [%s] FAILED: %s", tag, iso, e)

    per_doc = os.path.join(out_dir, "linguistic_counts_per_doc.csv")
    df.drop(columns=["prose"]).to_csv(per_doc, index=False)
    log.info("wrote %s", per_doc)

    metric_cols = [c for c in df.columns
                   if c == "chars" or c.endswith(("_tokens", "_words"))]
    summary = build_summary(df, metric_cols)
    summ_path = os.path.join(out_dir, "linguistic_counts_summary.csv")
    summary.to_csv(summ_path, index=False)
    log.info("wrote %s", summ_path)

    if "spacy_trained_words" in df.columns:
        write_latex(summary, os.path.join(out_dir, "table4_token_stats_linguistic.tex"),
                    "spacy_trained_words", "chars")

    # ── summary log ──
    log.info("=" * 64)
    for col in ("spacy_trained_words", "spacy_blank_words", "chars"):
        if col in df:
            log.info("TOTAL %-20s = %s", col, f"{int(df[col].sum()):,}")
    if "spacy_trained_words" in df:
        log.info("median words/doc and chars/doc per language:")
        for lang in LANG_ORDER:
            sub = df[df["language"] == lang]
            log.info("   %-10s words=%6.0f  chars=%7.0f",
                     lang, np.median(sub["spacy_trained_words"]), np.median(sub["chars"]))
    log.info("=" * 64)
    log.info("done")


if __name__ == "__main__":
    main()
