# Prompt Engineering

Interactive demonstration of various prompt engineering techniques using Google FLAN-T5 models.

## Features

- Zero-Shot Prompt
- Few-Shot Prompt
- Chain-of-Thought Prompt
- Instructional Prompt
- Role-Based Prompt
- Comparative Demo

## Local Setup

```bash
# Creating a new virtual env
python3 -m venv .venv
source .venv/bin/activate
```

```bash
# Install dependencies
pip install -r requirements.txt

# Run (defaults to large)
python prompts.py

# Prefer CLI to choose model
python prompts.py --model large
python prompts.py --model small

# Optional: choose via env var instead
MODEL_NAME=google/flan-t5-large python prompts.py
MODEL_NAME=google/flan-t5-small python prompts.py
```

## Container Setup (Podman)

### Build the image
```bash
# With Podman
podman build -t ai-session-prompt-engineering .
```

This will:
- Install all dependencies
- Pre-download both models into cache:
	- google/flan-t5-large (~1.2GB)
	- google/flan-t5-small (~300MB)
- Set up the application environment

### Run the container
```bash
# Podman (explicit model via CLI)
podman run -it --rm --name ai-session-prompts \
  ai-session-prompt-engineering python3 /app/prompts.py --model large

# Docker (use the smaller model via CLI)
docker run -it --rm --name ai-session-prompts \
  ai-session-prompt-engineering python3 /app/prompts.py --model small

# Optional: use env var if preferred
podman run -it --rm --name ai-session-prompts \
  -e MODEL_NAME=google/flan-t5-small \
  ai-session-prompt-engineering python3 /app/prompts.py
```

## Model Information

- **Default model**: google/flan-t5-large (~1.2GB)
- **Alternative**: google/flan-t5-small (~300MB)
- **Selection**: use `--model large|small` (preferred) or `MODEL_NAME` env var
- **Downloaded during**: container image build
- **Cache location**: /root/.cache/huggingface

## Requirements

- Python 3.11+
- transformers>=4.30.0
- torch>=2.0.0
- sentencepiece>=0.1.99
