FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY prompts.py .
COPY download_models.py .
COPY prompt_types/ ./prompt_types/

# Set environment variable for Ollama host
# This can be overridden at runtime
ENV OLLAMA_HOST=http://host.docker.internal:11434

# Default command
CMD ["python3", "prompts.py"]
