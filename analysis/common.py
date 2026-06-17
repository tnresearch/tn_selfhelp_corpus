"""
Shared utilities for dataset analysis: paths, language mapping, corpus loading,
and Markdown structure parsing.
"""

import json
import os
import re

# ── Paths (relative to repo root) ────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "data")
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")
TABLES_DIR = os.path.join(OUTPUT_DIR, "tables")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")

os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# ── Domain → Language mapping ────────────────────────────────────────────────
DOMAIN_LANG = {
    "www.dna.fi": "Finnish",
    "www.telenor.dk": "Danish",
    "www.telenor.no": "Norwegian",
    "www.telenor.se": "Swedish",
}

LANG_ORDER = ["Finnish", "Danish", "Norwegian", "Swedish"]


# ── Data loading ─────────────────────────────────────────────────────────────
def load_corpus() -> list[dict]:
    """
    Load all accepted documents from data/{domain}/.
    Returns a list of dicts with keys:
        domain, language, text, heading, path, filename, source_path
    """
    docs = []
    for domain, language in DOMAIN_LANG.items():
        domain_dir = os.path.join(DATA_DIR, domain)
        if not os.path.isdir(domain_dir):
            print(f"Warning: {domain_dir} not found")
            continue
        for fname in sorted(os.listdir(domain_dir)):
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(domain_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            span = (data.get("annotations", {})
                    .get("content_selection", {})
                    .get("selected_span", {}))
            text = span.get("text", "")
            if not text:
                continue
            docs.append({
                "domain": domain,
                "language": language,
                "text": text,
                "heading": span.get("heading", ""),
                "path": fpath,
                "filename": fname,
                "source_path": data.get("source_file_relative_path", ""),
            })
    return docs


# ── Markdown structure parsing ───────────────────────────────────────────────
def parse_markdown_structure(text: str) -> dict:
    """Count structural elements in a Markdown document."""
    lines = text.split("\n")
    return {
        "headings": sum(1 for l in lines if re.match(r"^#{1,6}\s", l)),
        "list_items": sum(1 for l in lines if re.match(r"^\s*[-*+]\s", l) or re.match(r"^\s*\d+\.\s", l)),
        "links": len(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)),
        "table_rows": sum(1 for l in lines if "|" in l and not re.match(r"^\s*\|[-:|\s]+\|\s*$", l)),
        "bold_spans": len(re.findall(r"\*\*[^*]+\*\*", text)),
        "lines": len(lines),
    }
