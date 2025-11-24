# Dockerfile - Flask app with Prometheus metrics
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps for optional things
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and templates
COPY . .

EXPOSE 5000

# Use gunicorn for production-like run
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

