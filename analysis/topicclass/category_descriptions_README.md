# `category_descriptions.csv` — per-language topic-classification prompts

These ten prompts define the topic categories used to characterise the Telenor/DNA telecom
customer-service corpus. They are the "query" side of the zero-shot classifier (`topic_classify.py`):
each document is matched against the prompt **in its own language**, so prompt and document share a
language. The file has one column per language (`english`, `finnish`, `danish`, `norwegian`, `swedish`);
the `category` column is an internal English label and is not embedded.

The Finnish, Norwegian and Swedish prompts were translated and verified by native-speaker colleagues; the
Danish prompt was produced by the author. The `english` column is the template they were translated from.

## How the translations were produced
Each language column is the **whole** English prompt translated — **both the category name and the key
terms** (the parts before and after the colon) — read as one natural phrase in that language. Guidelines:

- Translate the full prompt: the category name **and** the keyword list.
- Keep widely-used **English technical terms as they actually appear** in customer-service text in that
  language — e.g. *router, modem, WiFi, SIM, eSIM, SMS, MMS, 4G/5G, TV, PIN, PUK* are usually left as-is.
  Translate the general/connecting words (subscriptions, settings, coverage, billing, account, …).
- Aim for how a real **support page** in that language would phrase the topic; a natural phrase beats a
  literal word-for-word translation.
- Keep roughly the English structure (category name, then a short list of terms).
- Do not edit the `category` column.
