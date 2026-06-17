FROM python:3.11-slim

WORKDIR /app

# Build deps for spaCy wheels
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# spaCy trained pipelines (tolerant: the script falls back to a blank tokenizer
# for any language whose model is unavailable at build time).
RUN for m in fi_core_news_sm da_core_news_sm sv_core_news_sm nb_core_news_sm; do \
        python -m spacy download $m || echo "WARN: spaCy model $m unavailable"; \
    done

COPY linguistic_count.py settings.json ./

ENV PYTHONUNBUFFERED=1
CMD ["python", "linguistic_count.py"]
