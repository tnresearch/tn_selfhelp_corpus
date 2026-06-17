"""
Generate all paper tables as LaTeX (.tex) files.

Tables produced:
  - table1_filtering_summary.tex  (Table 1: filtering pipeline results)
  - table3_annotation_agreement.tex  (Table 3: LLM vs human agreement)
  - structure_summary.csv  (per-language Markdown structure: headings, list items)

Usage:
  pip install -r analysis/requirements.txt
  python analysis/generate_tables.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import load_corpus, parse_markdown_structure, LANG_ORDER, DOMAIN_LANG, DATA_DIR, TABLES_DIR


def count_accepted_per_domain() -> dict[str, int]:
    """Count JSON files per domain in data/."""
    counts = {}
    for domain in DOMAIN_LANG:
        domain_dir = os.path.join(DATA_DIR, domain)
        if os.path.isdir(domain_dir):
            counts[domain] = len([f for f in os.listdir(domain_dir) if f.endswith(".json")])
        else:
            counts[domain] = 0
    return counts


def fmt(n: int) -> str:
    """Format integer with LaTeX thousands separator."""
    if n >= 1000:
        return f"{n:,}".replace(",", "{,}")
    return str(n)


def generate_table1():
    """Table 1: Filtering summary."""
    pipeline = {
        "www.dna.fi":      {"initial": 382, "pii": 1, "not_cs": 12, "not_sh": 2, "dup": 4, "empty": 1},
        "www.telenor.dk":  {"initial": 234, "pii": 0, "not_cs": 25, "not_sh": 0, "dup": 30, "empty": 0},
        "www.telenor.no":  {"initial": 187, "pii": 0, "not_cs": 1,  "not_sh": 2, "dup": 8,  "empty": 0},
        "www.telenor.se":  {"initial": 449, "pii": 0, "not_cs": 17, "not_sh": 24, "dup": 3, "empty": 0},
    }
    expected_accepted = {
        "www.dna.fi": 362, "www.telenor.dk": 179,
        "www.telenor.no": 176, "www.telenor.se": 405,
    }

    actual_accepted = count_accepted_per_domain()
    for domain, expected in expected_accepted.items():
        actual = actual_accepted.get(domain, 0)
        if actual != expected:
            print(f"WARNING: {domain} has {actual} accepted files, expected {expected}")

    domains = ["www.dna.fi", "www.telenor.dk", "www.telenor.no", "www.telenor.se"]

    steps = [
        ("Initial documents",              "initial"),
        ("Excluded: Contains PII",         "pii"),
        ("Excluded: Not customer service", "not_cs"),
        ("Excluded: Not self help",        "not_sh"),
        ("Excluded: Duplicates",           "dup"),
        ("Excluded: Empty content",        "empty"),
    ]

    lines = []
    lines.append(r"\begin{table*}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Number of documents remaining after filtering steps for each website.}")
    lines.append(r"\begin{tabular}{lrrrrr}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Filtering Step} & \textbf{DNA FI} & \textbf{Telenor DK} & \textbf{Telenor NO} & \textbf{Telenor SE} & \textbf{Total} \\")
    lines.append(r"\midrule")

    for label, key in steps:
        vals = [pipeline[d][key] for d in domains]
        total = sum(vals)
        lines.append(f"{label} & {fmt(vals[0])} & {fmt(vals[1])} & {fmt(vals[2])} & {fmt(vals[3])} & {fmt(total)} \\\\")

    # Total excluded
    excluded = []
    for d in domains:
        p = pipeline[d]
        excluded.append(p["pii"] + p["not_cs"] + p["not_sh"] + p["dup"] + p["empty"])
    lines.append(r"\midrule")
    lines.append(f"Total excluded & {fmt(excluded[0])} & {fmt(excluded[1])} & {fmt(excluded[2])} & {fmt(excluded[3])} & {fmt(sum(excluded))} \\\\")

    # Accepted (from actual data)
    acc = [actual_accepted.get(d, 0) for d in domains]
    lines.append(r"\textbf{Total accepted} & \textbf{" + r"} & \textbf{".join(fmt(v) for v in acc) + r"} & \textbf{" + fmt(sum(acc)) + r"} \\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\label{tab:filtering_summary}")
    lines.append(r"\end{table*}")

    output = "\n".join(lines) + "\n"
    path = os.path.join(TABLES_DIR, "table1_filtering_summary.tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Saved: {path}")


def generate_table3():
    """Table 3: Annotation agreement (LLM vs human).

    These values are from the annotation pipeline comparison and cannot be
    recomputed from the shipped dataset alone.
    """
    rows = [
        ("Customer service related", 1195, 1251),
        ("Self-help resource",       1170, 1251),
        ("Contains PII",             1248, 1251),
    ]
    span_rows = [
        ("Span extraction success",   937, 1251),
        ("Exact span match",           64,  937),
    ]

    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Agreement between LLM (Gemma-3-27b-it) pre-annotation and human review across 1{,}251 matched document pairs.}")
    lines.append(r"\label{tab:agreement}")
    lines.append(r"\begin{tabular}{lrrr}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Field} & \textbf{Agreed} & \textbf{Total} & \textbf{Agreement} \\")
    lines.append(r"\midrule")

    for label, agreed, total in rows:
        pct = f"{agreed/total*100:.1f}\\%"
        lines.append(f"{label} & {fmt(agreed)} & {fmt(total)} & {pct} \\\\")

    lines.append(r"\midrule")

    for label, agreed, total in span_rows:
        pct = f"{agreed/total*100:.1f}\\%"
        lines.append(f"{label} & {fmt(agreed)} & {fmt(total)} & {pct} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    output = "\n".join(lines) + "\n"
    path = os.path.join(TABLES_DIR, "table3_annotation_agreement.tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Saved: {path}")


def generate_structure_stats():
    """Per-language Markdown structure averages (headings, list items, links, ...).

    Reproduces the structural-density figures cited in Section 3 (e.g. Norwegian
    documents average 6.1 headings and 13.1 list items per document). Reuses
    common.parse_markdown_structure on the original Markdown of each document.
    """
    import csv
    from collections import defaultdict

    docs = load_corpus()
    agg = defaultdict(list)
    for d in docs:
        agg[d["language"]].append(parse_markdown_structure(d["text"]))

    fields = ["headings", "list_items", "links", "table_rows", "bold_spans"]
    path = os.path.join(TABLES_DIR, "structure_summary.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["language", "docs"] + [f"{x}_avg" for x in fields])
        for lang in LANG_ORDER:
            rows = agg.get(lang, [])
            if not rows:
                continue
            avgs = [round(sum(r[x] for r in rows) / len(rows), 1) for x in fields]
            w.writerow([lang, len(rows)] + avgs)
    print(f"Saved: {path}")


if __name__ == "__main__":
    print("=" * 60)
    print("Generating paper tables (LaTeX)")
    print("=" * 60)

    generate_table1()
    print()
    generate_table3()
    print()
    generate_structure_stats()

    print("\nAll tables saved to:", TABLES_DIR)
