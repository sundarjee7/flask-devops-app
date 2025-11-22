FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for Jenkins test stage
RUN pip install pytest

# Copy application code
COPY app.py .

# Copy test folder
COPY tests/ ./tests/

# Expose port (optional)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

