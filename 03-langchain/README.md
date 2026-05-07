# LangChain with Prompt Engineering

Interactive demonstration of LangChain fundamentals and various prompt engineering techniques using Granite 3.3:8b model via Ollama.

## Features

### LangChain Fundamentals (`langchain_basics/langchain_fundamentals.py`)
- Basic LLM Setup
- Prompt Templates
- LLM Chains (LCEL)
- Chat Templates
- Output Parsers
- Batch Processing
- Streaming

### Prompt Engineering (`prompts.py`)
- Zero-Shot Prompt
- Few-Shot Prompt
- Chain-of-Thought Prompt
- Instructional Prompt
- Role-Based Prompt
- Comparative Demo

## Prerequisites

- Python 3.11+
- Ollama installed and running
- Granite 3.3:8b model already deployed in Ollama

## Setup

### 1. Install Ollama

If you haven't installed Ollama yet, visit [https://ollama.ai](https://ollama.ai) and follow the installation instructions for your platform.

### 2. Verify Granite Model

Ensure the Granite 3.3:8b model is already pulled and available:

```bash
ollama list
```

If not available, pull it:

```bash
ollama pull granite3.3:8b
```

### 3. Create Virtual Environment

```bash
# Create a new virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Applications

```bash
# Run LangChain fundamentals (interactive teaching module)
python langchain_basics/langchain_fundamentals.py

# Run prompt engineering demo with default model (granite3.3:8b)
python prompts.py

# Or specify a different Ollama model
python prompts.py --model granite3.3:8b

# Or use environment variable
MODEL_NAME=granite3.3:8b python prompts.py
```

### 6. Deactivate Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## Model Information

- **Default model**: granite3.3:8b
- **Backend**: Ollama
- **Selection**: use `--model <model-name>` or `MODEL_NAME` env var
- **Requirements**: Ollama must be running with the model pulled

## LangChain Integration

This implementation uses:
- `langchain-community` for Ollama integration
- `PromptTemplate` for structured prompts
- `FewShotPromptTemplate` for few-shot learning examples
- Direct LLM invocation for flexible prompt handling

## Requirements

- Python 3.11+
- langchain>=0.3.13
- langchain-community>=0.3.13
- langchain-core>=0.3.28
- langchain-ollama>=0.3.0
- ollama>=0.4.4

