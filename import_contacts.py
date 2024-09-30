# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to the root of the project
WORKDIR /rolodex-app

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Copy the current directory contents into the container at /rolodex-app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Initialize SQLite
