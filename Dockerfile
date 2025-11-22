FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

COPY app.py .
COPY test_app.py .

# Add this line to run Flask when the container starts
CMD ["python", "app.py"]
	
