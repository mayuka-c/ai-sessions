FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
	git \
	&& rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Configure Hugging Face cache and pre-download models
ENV TRANSFORMERS_CACHE=/root/.cache/huggingface
ENV MODEL_NAME=google/flan-t5-large
COPY download_models.py ./
RUN python download_models.py

# Copy application code
COPY prompts.py .
COPY prompt_types/ prompt_types/

# Default command (can be overridden)
CMD ["python", "-c", "print('container ready')"]
