# Use Python 3.13 slim image
FROM python:3.13-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the model during build (optional but recommended)
RUN python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; \
    model_name='distilgpt2'; \
    AutoTokenizer.from_pretrained(model_name); \
    AutoModelForCausalLM.from_pretrained(model_name)"

# Final stage
FROM python:3.13-slim

WORKDIR /app

# Copy installed packages and cached models from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /root/.cache/huggingface /root/.cache/huggingface

# Copy application code
COPY transformers_pract.py .

# Set environment variables
ENV TRANSFORMERS_CACHE=/root/.cache/huggingface
ENV HF_HOME=/root/.cache/huggingface

# Keep container running indefinitely
CMD ["tail", "-f", "/dev/null"]
