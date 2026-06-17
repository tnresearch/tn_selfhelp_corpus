FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ \
    && rm -rf /var/lib/apt/lists/*

# CPU-only torch (smaller image, no CUDA)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the embedding model at build time so runs are offline/reproducible (~2 GB)
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/multilingual-e5-large')"

COPY topic_classify.py settings.json category_descriptions.csv ./

ENV PYTHONUNBUFFERED=1
CMD ["python", "topic_classify.py"]
