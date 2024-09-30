# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Copy the requirements.txt file separately into the container
COPY requirements.txt /app/requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the app directory into the container
COPY ./app /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Initialize SQLite database
RUN sqlite3 /app/rolodex.db "CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL);"

# Run the application
CMD ["python", "app.py"]
