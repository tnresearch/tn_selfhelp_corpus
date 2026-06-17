#!/usr/bin/env python3
"""Write derived topic-classification labels into each document JSON.

Reads the original-language classification (topic_per_doc.csv) and adds, under
`metadata`, a clearly-derived `topic_classification` object. It is placed under
metadata (not annotations) to signal that it is machine-derived and NOT
human-reviewed, unlike the filtering/PII/content_selection annotations.

Idempotent (re-running overwrites the field). Matches the existing JSON formatting
(indent=4, non-ASCII preserved, no trailing newline) so diffs show only the added field.
"""
import argparse
import json
import logging
import os

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("write-labels")
MODEL = "intfloat/multilingual-e5-large"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="output/tables/topic_per_doc.csv")
    ap.add_argument("--data-dir", default="data")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    n = 0
    for _, r in df.iterrows():
        path = os.path.join(args.data_dir, r["domain"], r["file"])
        if not os.path.exists(path):
            log.warning("missing %s", path)
            continue
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        had_nl = raw.endswith("\n")
        d = json.loads(raw)
        d.setdefault("metadata", {})
        d["metadata"]["topic_classification"] = {
            "category": r["cat_orig"],
            "score": round(float(r["score_orig"]), 4),
            "model": MODEL,
            "text_source": "original_language",
            "prompt_language": "document_language",
        }
        out = json.dumps(d, indent=4, ensure_ascii=False)
        if had_nl:
            out += "\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        n += 1
    log.info("updated %d JSON files with metadata.topic_classification", n)


if __name__ == "__main__":
    main()
