#!/bin/bash

# Check if the Docker group exists, and create it if it doesn't
if getent group docker > /dev/null 2>&1; then
  echo "Docker group already exists."
else
  echo "Creating Docker group..."
  sudo groupadd docker
fi

# Add the current user to the Docker group
if groups $USER | grep &>/dev/null "\bdocker\b"; then
  echo "User $USER is already in the Docker group."
else
  echo "Adding $USER to the Docker group..."
  sudo usermod -aG docker $USER
fi

# Restart the Docker service
echo "Restarting Docker service..."
sudo systemctl restart docker

echo "Setup complete. You need to log out and log back in for the group changes to take effect."
