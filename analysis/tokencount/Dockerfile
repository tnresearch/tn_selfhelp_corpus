FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY token_counter.py .
COPY settings.json .

# Create data directory for volume mounting
RUN mkdir -p /data

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "token_counter.py"] 