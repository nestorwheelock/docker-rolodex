#!/bin/bash

# Step 1: Build the Docker image
echo "Building the Docker image 'rolodex-app'..."
docker build -t rolodex-app .

# Check if the image was built successfully
if [ $? -eq 0 ]; then
    echo "Docker image 'rolodex-app' built successfully."
else
    echo "Failed to build Docker image 'rolodex-app'. Exiting..."
    exit 1
fi

# Step 2: Run the Docker container
echo "Running the Docker container from 'rolodex-app' image..."
docker run -d -p 5000:5000 rolodex-app

# Check if the container started successfully
if [ $? -eq 0 ]; then
    echo "Docker container is running on port 5000."
else
    echo "Failed to run the Docker container. Exiting..."
    exit 1
fi

# Step 3: Verify the container is running
echo "Verifying if the container is running..."
docker ps | grep rolodex-app

if [ $? -eq 0 ]; then
    echo "Container is running successfully!"
else
    echo "The container is not running."
fi
