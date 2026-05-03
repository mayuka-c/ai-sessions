# LangChain Fundamentals

Hands-on guide to learning LangChain basics through 8 practical examples.

## Quick Start

```bash
# Prerequisites
ollama pull granite3.3:8b

# Run interactive mode
python langchain_basics/langchain_fundamentals.py
```

## What's Covered

1. Basic LLM Setup
2. Prompt Templates
3. LLM Chains
4. Few-Shot Prompting
5. Chat Templates
6. Output Parsers
7. Batch Processing
8. Streaming

## Usage

**Interactive Menu:**
- Choose examples 1-8 individually
- Option 9 runs all examples
- Option 0 exits

**Run All at Once:**
Edit the file and change last line to `run_all_examples()`

## Troubleshooting

```bash
# Ollama not running
ollama serve

# Model not found
ollama pull granite3.3:8b

# Dependencies
pip install -r ../requirements.txt
