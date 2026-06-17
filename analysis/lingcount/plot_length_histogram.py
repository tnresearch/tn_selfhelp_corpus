#!/usr/bin/env python3
"""Figure 1: document-length distribution by language, in WORDS (spaCy word tokens).
Reads the per-document CSV produced by linguistic_count.py and renders a four-panel
stacked histogram (one per language).

Usage:
  python plot_length_histogram.py --csv output/tables/linguistic_counts_per_doc.csv \
                                  --out  task1_doc_length_histogram.pdf
"""
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LANG_ORDER = ["Finnish", "Danish", "Norwegian", "Swedish"]
LANG_COLORS = {"Finnish": "#001845", "Danish": "#5B9BD5",
               "Norwegian": "#70CEC8", "Swedish": "#78C850"}
WORD_COL = "spacy_trained_words"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bin", type=int, default=50)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    plt.rcParams.update({"font.family": "serif", "savefig.dpi": 300,
                         "savefig.bbox": "tight", "pdf.fonttype": 42, "ps.fonttype": 42})
    maxw = df[WORD_COL].max()
    bins = np.arange(0, maxw + args.bin, args.bin)

    fig, axes = plt.subplots(4, 1, figsize=(8, 8), sharex=True)
    for lang, ax in zip(LANG_ORDER, axes):
        sub = df[df["language"] == lang][WORD_COL]
        med = int(sub.median())
        ax.hist(sub, bins=bins, color=LANG_COLORS[lang], edgecolor="white", linewidth=0.5, alpha=0.9)
        ax.set_ylabel("Count")
        ax.text(0.97, 0.85, f"{lang}  (median = {med})", transform=ax.transAxes,
                ha="right", va="top", fontsize=10, fontweight="bold")
        ax.yaxis.grid(True, alpha=0.3)
        ax.set_axisbelow(True)
    axes[-1].set_xlabel("Word count (spaCy)")
    fig.suptitle("Document Length Distribution by Language", y=1.01, fontsize=12)
    fig.tight_layout()
    fig.savefig(args.out)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
