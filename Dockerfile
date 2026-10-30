# Step 8 & 9: Lightweight Python Docker Image
FROM python:3.11-alpine

# Metadata
LABEL maintainer="Abhi Trambadiya <dev.abhitrambadiya@gmail.com>"
LABEL purpose="MLOps Lab Internal POE - UAT Dry Run"

# Set working directory inside container
WORKDIR /app

# Install pytest for automated container testing
RUN pip install --no-cache-dir pytest

# Step 10: Add hello.py and application code into docker container
COPY hello.py .
COPY tests/ ./tests/

# Default entrypoint runs the Hello application
CMD ["python", "hello.py"]
