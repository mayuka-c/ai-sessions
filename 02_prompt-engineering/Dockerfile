# Use Python 3.11 slim image as base
FROM python:3.11-slim

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

# Pre-download the model during build time to avoid downloading at runtime
RUN python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; \
    model_name = 'google/flan-t5-small'; \
    print('Downloading model and tokenizer...'); \
    tokenizer = AutoTokenizer.from_pretrained(model_name); \
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name); \
    print('Model downloaded successfully!')"

# Copy application code
COPY prompts.py .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/root/.cache/huggingface

# Keep container running indefinitely
CMD ["tail", "-f", "/dev/null"]
