"""
Shared utilities for dataset analysis.
Provides data loading, color palette, and plot styling.
"""

import json
import os
import re
import tiktoken
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

# ── Paths (relative to repo root) ────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "data")
TRANSLATIONS_DIR = os.path.join(REPO_ROOT, "data", "translations")
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")
TABLES_DIR = os.path.join(OUTPUT_DIR, "tables")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")

# Create output directories
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

# ── Color palette (consistent across all figures) ────────────────────────────
LANG_COLORS = {
    "Finnish": "#001845",
    "Danish": "#5B9BD5",
    "Norwegian": "#70CEC8",
    "Swedish": "#78C850",
}

CATEGORY_COLORS = [
    "#001845", "#3B6CB4", "#5B9BD5", "#8DB4E2", "#70CEC8",
    "#78C850", "#B8CCE8", "#8B7BBC", "#D4A0B8", "#B0B0B0",
]

# ── Plot styling ─────────────────────────────────────────────────────────────
def setup_plot_style():
    """Set publication-quality matplotlib defaults."""
    sns.set_context("paper", font_scale=1.2)
    sns.set_style("whitegrid")
    plt.rcParams.update({
        "font.family": "serif",
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.1,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

# ── GPT-2 Tokenizer ─────────────────────────────────────────────────────────
_tokenizer = None

def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = tiktoken.get_encoding("gpt2")
    return _tokenizer

def count_tokens(text: str) -> int:
    return len(get_tokenizer().encode(text))

# ── Data loading ─────────────────────────────────────────────────────────────
def load_corpus() -> list[dict]:
    """
    Load all accepted documents from data/{domain}/.
    Returns list of dicts with keys:
        domain, language, text, heading, path, filename, source_path, token_count
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
            text = (data.get("annotations", {})
                    .get("content_selection", {})
                    .get("selected_span", {})
                    .get("text", ""))
            heading = (data.get("annotations", {})
                       .get("content_selection", {})
                       .get("selected_span", {})
                       .get("heading", ""))
            source_path = data.get("source_file_relative_path", "")
            if not text:
                continue
            docs.append({
                "domain": domain,
                "language": language,
                "text": text,
                "heading": heading,
                "path": fpath,
                "filename": fname,
                "source_path": source_path,
                "token_count": count_tokens(text),
            })
    return docs


def load_translations(docs: list[dict]) -> dict[tuple[str, str], str]:
    """
    Load English translations for accepted documents.
    Returns dict mapping (domain, filename) -> translated text.
    Translation files are *_ENG.md files in data/translations/{domain}/.
    """
    translations = {}
    missing = 0
    for doc in docs:
        domain = doc["domain"]
        fname = doc["filename"]  # e.g. "name.html.json"
        base = fname.replace(".html.json", "")
        trans_path = os.path.join(TRANSLATIONS_DIR, domain, base + "_ENG.md")
        if os.path.exists(trans_path):
            with open(trans_path, "r", encoding="utf-8") as f:
                translations[(domain, fname)] = f.read()
        else:
            missing += 1
    if missing:
        print(f"Warning: {missing} documents missing translations")
    return translations


# ── Markdown structure parsing ───────────────────────────────────────────────
def parse_markdown_structure(text: str) -> dict:
    """Count structural elements in a markdown document."""
    lines = text.split("\n")
    return {
        "headings": sum(1 for l in lines if re.match(r"^#{1,6}\s", l)),
        "list_items": sum(1 for l in lines if re.match(r"^\s*[-*+]\s", l) or re.match(r"^\s*\d+\.\s", l)),
        "links": len(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)),
        "table_rows": sum(1 for l in lines if "|" in l and not re.match(r"^\s*\|[-:|\s]+\|\s*$", l)),
        "bold_spans": len(re.findall(r"\*\*[^*]+\*\*", text)),
        "lines": len(lines),
    }


def get_color_list():
    """Return colors in LANG_ORDER for consistent plotting."""
    return [LANG_COLORS[lang] for lang in LANG_ORDER]
