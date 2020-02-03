#!/bin/sh

# This script will:
# 1. Start Docker engine
# 2. Create image and container
# 3. Run app

# 1. Start Docker engine
echo Starting docker engine...
sudo systemctl start docker

# 2. Create image and container
echo Building Docker image...
sudo docker build -t team1/poet .
sudo docker images

# 3. Run app
echo Creating docker container...
sudo docker run team1/poet
echo container created, app started!
