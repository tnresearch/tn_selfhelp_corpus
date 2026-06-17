# Linguistic Count

Reports corpus size/length in **linguistic** units (spaCy word tokens) plus characters — a cross-corpus-comparable metric. Mirrors the existing Docker pattern.

## Methods (per document)
- **chars** — character count of markdown-stripped prose (assumption-free, fully comparable).
- **spacy_trained** — spaCy `*_core_news_sm` (fi/da/sv/nb); tokens / words (non-punctuation).
- **spacy_blank** — `spacy.blank(lang)`; lightweight, no model download; validates the trained run.

All methods run on text with markdown stripped (headings, lists, tables, code, links/URLs removed; link text kept).

## Run (Docker)
```bash
cd analysis/lingcount
docker compose up --build
```
Inputs: `data/<domain>/*.html.json` (read-only). Outputs to `output/tables/`:
- `linguistic_counts_per_doc.csv` — every metric per document
- `linguistic_counts_summary.csv` — per language + total: total/mean/median/IQR per method
- `table4_token_stats_linguistic.tex` — linguistic corpus-size table

The container log prints per-language word and character totals and medians.

## Config
`settings.json`: `data_dir`, `output_dir`, and `methods` (e.g. drop `spacy_trained` for a fast blank-only run).
