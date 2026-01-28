# Transformers Practice

Interactive Python application demonstrating text generation and tokenization using Hugging Face Transformers.

## Features

1. Text Generation (DistilGPT2)
2. Tokenization Demo (Encode & Decode)

## How to Run

### Option 1: Run Locally

```bash
# Creating a new virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python transformers_pract.py
```

### Option 2: Run with Podman

```bash
# Build the image
podman build -t ai-session-transformers .

# Run the container
podman run -it --rm --name ai-session-transformer-pract \
  ai-session-transformers python3 /app/transformers_pract.py
```
