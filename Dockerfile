# Use official Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app code
COPY app.py .

# Expose the port Flask will run on
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]

