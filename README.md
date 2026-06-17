# Telenor Nordics Customer Service Self-help Corpus

A multilingual customer service self-help corpus comprising **1,122 manually validated documents** in Finnish, Danish, Norwegian, and Swedish, totaling **274,599 words** (over 1.8 million characters).

The documents have been sourced from the public self-help pages of four Nordic telecommunications operators and filtered for person-identifiable information, relevance, and duplicates through a combined LLM and human annotation pipeline.

**Paper:** _placeholder here until paper is published_

## Dataset overview

| Language | Operator | Docs | Words | Avg words/doc | Median words/doc | Characters |
|----------|----------|------|-------|---------------|------------------|------------|
| Finnish | DNA Finland | 362 | 87,306 | 241 | 164 | 749,435 |
| Danish | Telenor Denmark | 179 | 44,744 | 250 | 196 | 268,032 |
| Norwegian | Telenor Norway | 176 | 72,749 | 413 | 320 | 445,850 |
| Swedish | Telenor Sweden | 405 | 69,800 | 172 | 99 | 421,516 |
| **Total** | | **1,122** | **274,599** | **245** | **151** | **1,884,833** |

Word counts use spaCy; character counts are also reported.

## Repository structure

```
data/
  www.dna.fi/             Finnish documents (362 JSON + 362 Markdown files)
  www.telenor.dk/         Danish documents (179 JSON + 179 Markdown files)
  www.telenor.no/         Norwegian documents (176 JSON + 176 Markdown files)
  www.telenor.se/         Swedish documents (405 JSON + 405 Markdown files)
  translations/           English translations for topic analysis
analysis/
  common.py               Shared utilities (corpus loading, Markdown structure)
  generate_tables.py      Reproduce filtering + agreement tables + structure stats
  lingcount/              Corpus size/length: spaCy words + characters (Docker)
  topicclass/             Topic classification + category figure: multilingual-e5 (Docker)
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
| `metadata.topic_classification.category` | Derived topic label (zero-shot; see note) | `Routers, modems & network hardware` |

> **Note — `metadata.topic_classification` is a _derived_ field, not a human-reviewed annotation.**
> Each document's original-language text is classified zero-shot by cosine similarity to ten category
> prompts written in the document's own language, using `intfloat/multilingual-e5-large`. The object
> contains `category`, `score` (the cosine similarity, usable as a confidence filter), `model`,
> `text_source`, and `prompt_language`. It is fully reproducible from `analysis/topicclass/`.

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

### Tables (pure Python, no dependencies)

```bash
python analysis/generate_tables.py
```

Outputs to `output/tables/`:
- `table1_filtering_summary.tex` - Filtering pipeline results
- `table3_annotation_agreement.tex` - LLM vs human annotation agreement
- `structure_summary.csv` - per-language Markdown structure (headings, list items)

The corpus size/length table (words + characters) is produced by the Dockerised `analysis/lingcount/` tool (`docker compose up --build`).

### Figures

The document-length histogram (Figure 1, in words) is produced by `analysis/lingcount/plot_length_histogram.py`.

The topic-category figure (Figure 2) and the per-language category table are produced by the Dockerised `analysis/topicclass/` tool (`docker compose up --build`), which writes `output/figures/figure2_content_categories_originals.pdf` and `output/tables/appendix_category_frequencies_originals.tex`.

## Citation

```bibtex
**placeholder**

```

## License

This dataset is released under [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Contact

Mike Riess - mike.riess@telenor.com
Research and Innovation, Telenor Group, Oslo, Norway
