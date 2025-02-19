# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the script
COPY receiver.py .

# Install dependencies
RUN pip install requests

# Command to run the application
CMD ["python", "receiver.py"]


