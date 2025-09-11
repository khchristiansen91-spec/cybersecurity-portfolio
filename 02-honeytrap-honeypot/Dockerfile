FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy and install requirements first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the honeypot port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
