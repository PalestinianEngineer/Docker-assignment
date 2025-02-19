# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application script into the container
COPY sender.py .

# Install required Python packages
RUN pip install flask

# Expose port 5000 so other containers can communicate with it
EXPOSE 5000 

# Command to run the application
CMD ["python", "sender.py"]






