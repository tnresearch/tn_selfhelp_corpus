# Topic classification

Zero-shot topic classification of the **original-language** documents (the published version had used the
English machine translations). Each document is assigned the category — among ten predefined categories —
whose prompt embedding has the highest cosine similarity to the document, using multilingual-e5-large.

The category prompts are applied in each document's **own language**: an English template
(`category_descriptions.csv`, `english` column) was translated into Finnish, Danish, Norwegian and Swedish
and verified by a native speaker of each language. This native-prompt classification is the **primary**
result — it produces Figure 2, the per-language Table A1, and the per-document label written into the
dataset. The category-defining terms (router, SIM, SMS, MMS, modem, TV, eSIM, PIN, …) are technical terms
used as-is across the Nordic languages.

The same run also classifies the original text and its English machine translation with the English
prompt and reports the agreement (`topic_agreement.csv`) — a check of how much machine translation affects
the analysis. Text is Markdown-stripped and truncated to the first `max_words` words (fair across
languages) before embedding.

## Run (Docker)
```bash
cd analysis/topicclass
docker compose up --build
```
Outputs to `output/tables/`: `topic_per_doc.csv`, `topic_agreement.csv`,
`appendix_category_frequencies_originals.tex`; and `output/figures/figure2_content_categories_originals.pdf`.
The container log prints the per-language category counts and the translation-agreement numbers.

To write the derived label (`metadata.topic_classification`) into the dataset JSONs, run from the repo root
(`data/` is mounted read-only in Docker, so this step runs on the host):
```bash
python analysis/topicclass/write_topic_labels.py
```
