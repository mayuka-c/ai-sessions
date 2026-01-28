# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download models during build to avoid runtime downloads
RUN python - << 'PY'
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

models = [
    'google/flan-t5-small',
    'google/flan-t5-base',
]
print('Downloading models into HF cache...')
for name in models:
    AutoTokenizer.from_pretrained(name)
    AutoModelForSeq2SeqLM.from_pretrained(name)
print('All requested models downloaded successfully!')
PY

# Copy application code
COPY prompts.py .
COPY prompt_types/ prompt_types/

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/root/.cache/huggingface
ENV MODEL_NAME=google/flan-t5-base

# Keep container running indefinitely
CMD ["tail", "-f", "/dev/null"]
