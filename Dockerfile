# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
