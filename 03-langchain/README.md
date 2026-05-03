# Prompt Engineering with LangChain

Interactive demonstration of various prompt engineering techniques using LangChain with Granite 3.3:8b model via Ollama.

## Features

- Zero-Shot Prompt
- Few-Shot Prompt
- Chain-of-Thought Prompt
- Instructional Prompt
- Role-Based Prompt
- Comparative Demo

## Prerequisites

- Python 3.11+
- Ollama installed and running
- Granite 3.3:8b model pulled in Ollama

## Local Setup

### Install Ollama

If you haven't installed Ollama yet, visit [https://ollama.ai](https://ollama.ai) and follow the installation instructions for your platform.

### Pull the Granite Model

```bash
ollama pull granite3.3:8b
```

### Setup Python Environment

```bash
# Create a new virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
# Run with default model (granite3.3:8b)
python prompts.py

# Or specify a different Ollama model
python prompts.py --model granite3.3:8b

# Or use environment variable
MODEL_NAME=granite3.3:8b python prompts.py
```

## Container Setup (Podman/Docker)

### Build the image

```bash
# With Podman
podman build -t ai-session-langchain-prompts .

# With Docker
docker build -t ai-session-langchain-prompts .
```

This will:
- Install all dependencies
- Set up the application environment
- Note: The Granite model needs to be available in your Ollama instance

### Run the container

```bash
# Podman (connects to host Ollama)
podman run -it --rm --name ai-session-langchain \
  --network host \
  ai-session-langchain-prompts python3 /app/prompts.py

# Docker (connects to host Ollama on macOS/Windows)
docker run -it --rm --name ai-session-langchain \
  -e OLLAMA_HOST=host.docker.internal:11434 \
  ai-session-langchain-prompts python3 /app/prompts.py

# Docker on Linux (connects to host Ollama)
docker run -it --rm --name ai-session-langchain \
  --network host \
  ai-session-langchain-prompts python3 /app/prompts.py
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
- langchain>=0.1.0
- langchain-community>=0.0.20
- ollama>=0.1.0

## Differences from Original Implementation

The original implementation (`02_prompt-engineering`) used:
- Direct transformers library with FLAN-T5 models
- Custom generator function wrapper
- Local model loading

This LangChain implementation uses:
- LangChain abstractions for prompt management
- Ollama backend for model inference
- Granite 3.3:8b model (more powerful than FLAN-T5)
- Structured prompt templates for better maintainability

## Usage Tips

1. Make sure Ollama is running before starting the application
2. The first request may take a moment as the model loads
3. Use Ctrl-D to finish multi-line inputs
4. Try the same prompt with different techniques to see how they affect responses
5. Experiment with different models by changing the `--model` parameter
