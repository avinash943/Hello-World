# Use official Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy local files to the container
COPY fibonacci.py .

# Run the Fibonacci script when container starts
CMD ["python", "fibonacci.py"]
