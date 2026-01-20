# Prompt Engineering

Interactive demonstration of various prompt engineering techniques using google/flan-t5-small model.

## Features

- Simple Prompt
- Zero-Shot Prompt
- Few-Shot Prompt
- Chain-of-Thought Prompt
- Instructional Prompt
- Role-Based Prompt
- Comparative Demo

## Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python prompts.py
```

## Podman Setup

### Build the Podman image
```bash
podman build -t prompt-engineering .
```

This will:
- Install all dependencies
- Pre-download the google/flan-t5-small model (~300MB)
- Set up the application environment

### Run the container
```bash
podman run -it prompt-engineering
```

The `-it` flags are required for interactive input.

### Optional: Run with volume mount (for development)
```bash
podman run -it -v $(pwd):/app prompt-engineering
```

## Model Information

- **Model**: google/flan-t5-small
- **Size**: ~300MB
- **Downloaded during**: Podman image build (not at runtime)
- **Cache location**: /root/.cache/huggingface

## Requirements

- Python 3.11+
- transformers>=4.30.0
- torch>=2.0.0
- sentencepiece>=0.1.99
