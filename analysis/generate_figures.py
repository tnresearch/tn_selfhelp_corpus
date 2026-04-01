"""
Generate all paper figures as .pdf files.

Figures produced:
  - figure1_doc_length_histogram.pdf  (Figure 1: document length distribution)
  - figure2_content_categories_normalized.pdf  (Figure 2: topic categories)

Side-effect:
  - appendix4_category_frequencies.txt  (Appendix 4: category cross-tabulation)

Usage:
  # Figure 1 only (lightweight):
  pip install -r analysis/requirements.txt
  python analysis/generate_figures.py

  # Figure 1 + Figure 2 (requires ~2GB model download):
  pip install -r analysis/requirements-embeddings.txt
  python analysis/generate_figures.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common import (
    load_corpus, load_translations, setup_plot_style,
    LANG_ORDER, LANG_COLORS, CATEGORY_COLORS, FIGURES_DIR, TABLES_DIR,
)


# ── Category definitions for zero-shot classification ────────────────────────
CATEGORIES = {
    "Mobile subscriptions & services": "Mobile phone subscriptions, plans, prepaid, roaming, MMS, SMS, VoLTE, VoWiFi, mobile services",
    "Broadband & fixed internet": "Broadband, fiber, DSL, fixed internet connection, internet speed, home internet",
    "Routers, modems & network hardware": "Router setup, modem configuration, WiFi settings, network equipment, dongles, repeaters",
    "TV & streaming": "Television services, streaming, TV boxes, channels, remote control, set-top box",
    "Billing & payment": "Invoice, billing, payment, pricing, charges, fees, credit, subscription cost",
    "Account & login": "My account, login, password, profile, app, self-service portal",
    "SIM & eSIM": "SIM card, eSIM, activation, SIM swap, PIN, PUK",
    "Mobile devices": "Smartphones, tablets, smartwatches, phone setup, device troubleshooting, screen, insurance",
    "Network & coverage": "Network coverage, outages, 4G, 5G, signal strength, connectivity problems",
    "Other": "General customer service information, terms and conditions, contact information, moving, address change, security",
}


def truncate_text(text: str, max_chars: int = 2000) -> str:
    return text[:max_chars] if len(text) > max_chars else text


def generate_figure1(docs):
    """Figure 1: Document length distribution (stacked histograms)."""
    setup_plot_style()
    df = pd.DataFrame(docs)

    max_tokens = df["token_count"].max()
    bin_width = 200
    bins = np.arange(0, max_tokens + bin_width, bin_width)

    fig, axes = plt.subplots(4, 1, figsize=(8, 8), sharex=True)

    for i, (lang, ax) in enumerate(zip(LANG_ORDER, axes)):
        subset = df[df["language"] == lang]["token_count"]
        median_val = int(subset.median())

        ax.hist(subset, bins=bins, color=LANG_COLORS[lang], edgecolor="white",
                linewidth=0.5, alpha=0.9)
        ax.set_ylabel("Count")
        ax.text(0.97, 0.85, f"{lang}  (median = {median_val})",
                transform=ax.transAxes, ha="right", va="top",
                fontsize=10, fontweight="bold")
        ax.set_ylim(0, None)
        ax.yaxis.grid(True, alpha=0.3)
        ax.set_axisbelow(True)

    axes[-1].set_xlabel("Token count (GPT-2)")
    fig.suptitle("Document Length Distribution by Language", y=1.01, fontsize=12)
    fig.tight_layout()

    path = os.path.join(FIGURES_DIR, "figure1_doc_length_histogram.pdf")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved: {path}")


def generate_figure2(docs):
    """Figure 2: Content categories (normalized stacked bar chart).

    Requires sentence-transformers and multilingual-e5-large model.
    Also produces appendix4_category_frequencies.txt.
    """
    try:
        from sentence_transformers import SentenceTransformer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError:
        print("\nFigure 2 requires sentence-transformers and scikit-learn.")
        print("Install with: pip install -r analysis/requirements-embeddings.txt")
        print("Skipping figure 2.\n")
        return

    setup_plot_style()

    # Load model
    print("Loading multilingual-e5-large model (first run downloads ~2GB)...")
    model = SentenceTransformer("intfloat/multilingual-e5-large")

    # Load translations
    print("Loading English translations...")
    translations = load_translations(docs)

    docs_with_trans = []
    for d in docs:
        key = (d["domain"], d["filename"])
        if key in translations:
            d["english_text"] = translations[key]
            docs_with_trans.append(d)

    n_total = len(docs)
    n_translated = len(docs_with_trans)
    print(f"Translations found: {n_translated}/{n_total} ({n_translated/n_total*100:.1f}%)")

    if not docs_with_trans:
        print("ERROR: No translations found. Cannot generate figure 2.")
        return

    # Embed English translations
    print(f"Encoding {len(docs_with_trans)} English translations...")
    texts_en = ["passage: " + truncate_text(d["english_text"]) for d in docs_with_trans]
    embeddings_en = model.encode(texts_en, show_progress_bar=True, batch_size=32)

    # Embed category descriptions
    cat_names = list(CATEGORIES.keys())
    cat_descriptions = ["query: " + desc for desc in CATEGORIES.values()]
    cat_embeddings = model.encode(cat_descriptions, show_progress_bar=False)

    # Classify by cosine similarity
    sim_matrix = cosine_similarity(embeddings_en, cat_embeddings)

    for i, d in enumerate(docs_with_trans):
        scores = sim_matrix[i]
        best_idx = np.argmax(scores)
        d["category"] = cat_names[best_idx]
        d["category_score"] = scores[best_idx]

    # Build cross-tabulation
    df = pd.DataFrame(docs_with_trans)
    ct = pd.crosstab(df["category"], df["language"], margins=True)
    ct = ct.reindex(columns=[*LANG_ORDER, "All"])
    ct = ct.sort_values("All", ascending=False)

    ct_pct = pd.crosstab(df["category"], df["language"], normalize="columns") * 100
    ct_pct = ct_pct.reindex(columns=LANG_ORDER)

    # Category ordering
    cat_order = (ct.drop("All", axis=0).drop("All", axis=1)
                 .sum(axis=1).sort_values(ascending=False).index.tolist())
    if "Other" in cat_order:
        cat_order.remove("Other")
        cat_order.append("Other")

    cat_colors = {cat: CATEGORY_COLORS[i % len(CATEGORY_COLORS)] for i, cat in enumerate(cat_order)}

    # Normalized stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(LANG_ORDER))
    width = 0.6
    bottom = np.zeros(len(LANG_ORDER))

    for cat in cat_order:
        values = []
        for lang in LANG_ORDER:
            val = ct_pct.at[cat, lang] if (cat in ct_pct.index and lang in ct_pct.columns) else 0
            values.append(val)
        values = np.array(values, dtype=float)
        ax.bar(x, values, width, bottom=bottom, label=cat, color=cat_colors[cat])
        bottom += values

    ax.set_xlabel("Language")
    ax.set_ylabel("Percentage of documents (%)")
    ax.set_title("Content Category Distribution by Language (Normalized)")
    ax.set_xticks(x)
    ax.set_xticklabels(LANG_ORDER)
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)

    fig.tight_layout()
    path = os.path.join(FIGURES_DIR, "figure2_content_categories_normalized.pdf")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved: {path}")

    # Appendix 4: Category frequencies as LaTeX table
    lines = []
    lines.append(r"\begin{table*}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Content category frequencies by language (zero-shot classification using multilingual-e5-large on English translations).}")
    lines.append(r"\label{tab:categories}")
    lines.append(r"\begin{tabular}{lrrrrr}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Category} & \textbf{Finnish} & \textbf{Danish} & \textbf{Norwegian} & \textbf{Swedish} & \textbf{Total} \\")
    lines.append(r"\midrule")

    for cat in cat_order:
        vals = []
        for lang in LANG_ORDER:
            v = ct.at[cat, lang] if cat in ct.index else 0
            vals.append(int(v))
        total = int(ct.at[cat, "All"]) if cat in ct.index else 0
        cat_escaped = cat.replace("&", r"\&")
        lines.append(f"{cat_escaped} & {vals[0]} & {vals[1]} & {vals[2]} & {vals[3]} & {total} \\\\")

    lines.append(r"\midrule")
    totals = [int(ct.at["All", lang]) for lang in LANG_ORDER]
    grand = int(ct.at["All", "All"])
    lines.append(r"\textbf{Total} & \textbf{" + r"} & \textbf{".join(str(v) for v in totals) + r"} & \textbf{" + str(grand) + r"} \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table*}")

    output = "\n".join(lines) + "\n"
    app_path = os.path.join(TABLES_DIR, "appendix4_category_frequencies.tex")
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Saved: {app_path}")


if __name__ == "__main__":
    print("=" * 60)
    print("Generating paper figures")
    print("=" * 60)

    docs = load_corpus()
    print(f"Loaded {len(docs)} documents\n")

    print("--- Figure 1: Document length histogram ---")
    generate_figure1(docs)

    print("\n--- Figure 2: Content categories ---")
    generate_figure2(docs)

    print("\nAll outputs saved to:", os.path.dirname(FIGURES_DIR))
