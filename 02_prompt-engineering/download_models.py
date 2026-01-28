from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODELS = [
    "google/flan-t5-small",
    "google/flan-t5-large",
]

print("Downloading models into Hugging Face cache...")
for name in MODELS:
    AutoTokenizer.from_pretrained(name)
    AutoModelForSeq2SeqLM.from_pretrained(name)
print("Model predownload complete.")
