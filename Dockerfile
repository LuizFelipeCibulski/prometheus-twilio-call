# Use a Python image base
FROM python:3.9-slim

# Copy the code files to the container
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask twilio python-dotenv
RUN apt-get update && apt-get upgrade && apt-get install curl -y

# Expose port 5000 outside the container
EXPOSE 5000

# Set the default command to start the Flask server
CMD ["python3", "app.py"]
