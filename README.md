# Telenor Nordics Customer Service Self-help Corpus

A multilingual customer service self-help corpus comprising **1,122 manually validated documents** in Finnish, Danish, Norwegian, and Swedish, totaling over **one million tokens**.

The documents have been sourced from the public self-help pages of four Nordic telecommunications operators and filtered for person-identifiable information, relevance, and duplicates through a combined LLM and human annotation pipeline.

**Paper:** _placeholder here until paper is published_

## Dataset overview

| Language | Operator | Docs | Total tokens | Avg tokens/doc | Median tokens/doc |
|----------|----------|------|-------------|----------------|-------------------|
| Finnish | DNA Finland | 362 | 467,052 | 1,290 | 956 |
| Danish | Telenor Denmark | 179 | 123,374 | 689 | 509 |
| Norwegian | Telenor Norway | 176 | 214,736 | 1,220 | 986 |
| Swedish | Telenor Sweden | 405 | 236,450 | 584 | 362 |
| **Total** | | **1,122** | **1,041,612** | **928** | **600** |

Token counts use the GPT-2 tokenizer.

## Repository structure

```
data/
  www.dna.fi/             Finnish documents (362 JSON + 362 Markdown files)
  www.telenor.dk/         Danish documents (179 JSON + 179 Markdown files)
  www.telenor.no/         Norwegian documents (176 JSON + 176 Markdown files)
  www.telenor.se/         Swedish documents (405 JSON + 405 Markdown files)
  translations/           English translations for topic analysis
analysis/
  common.py               Shared utilities
  generate_tables.py      Reproduce paper tables (LaTeX output)
  generate_figures.py     Reproduce paper figures (PDF output)
  requirements.txt        Dependencies (tables + figure 1)
  requirements-embeddings.txt  Additional deps for figure 2
  tokencount/             Token counting utility (Docker)
```

## Data format

Each JSON file contains the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| `source_file_relative_path` | Source file path (domain/...) | `tuki/-alykellot_apple-watch.html` |
| `annotations.content_selection.selected_span.text` | Document text (Markdown) | ... |
| `annotations.content_selection.selected_span.heading` | Document heading | `Apple Watch` |
| `annotations.filtering.customer_service_related` | Relevance flag | `true` |
| `annotations.filtering.self_help_resource` | Self-help flag | `true` |
| `annotations.pii_detection.contains_pii` | PII flag | `false` |
| `metadata.llm_annotator_id` | LLM used for pre-annotation | `google/gemma-3-27b-it` |

Each document is available in two formats:
- **JSON** (`*.html.json`): Full annotation data including metadata, filtering flags, and content spans
- **Markdown** (`*.md`): Plain document text, ready to use

To read a markdown file directly:

```python
with open("data/www.dna.fi/example.md") as f:
    text = f.read()
```

Or extract text from the JSON:

```python
import json

with open("data/www.dna.fi/example.html.json") as f:
    doc = json.load(f)

text = doc["annotations"]["content_selection"]["selected_span"]["text"]
```

## Reproducing the analysis

### Tables (lightweight, no GPU needed)

```bash
pip install -r analysis/requirements.txt
python analysis/generate_tables.py
```

Outputs to `output/tables/`:
- `table1_filtering_summary.tex` - Filtering pipeline results
- `table3_annotation_agreement.tex` - LLM vs human annotation agreement
- `table4_token_stats.tex` - Token statistics per language

### Figures

```bash
# Figure 1 only (no ML model needed):
python analysis/generate_figures.py

# Figure 1 + Figure 2 (downloads ~2GB embedding model):
pip install -r analysis/requirements-embeddings.txt
python analysis/generate_figures.py
```

Outputs to `output/figures/`:
- `figure1_doc_length_histogram.pdf` - Document length distribution
- `figure2_content_categories_normalized.pdf` - Topic category distribution

Also produces `output/tables/appendix4_category_frequencies.tex`.

## Citation

```bibtex
**placeholder**

```

## License

This dataset is released under [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Contact

Mike Riess - mike.riess@telenor.com
Research and Innovation, Telenor Group, Oslo, Norway
