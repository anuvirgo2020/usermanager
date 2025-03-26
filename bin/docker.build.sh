#!/bin/bash

IMAGE_NAME="usermanager"

# Build the docker image
docker build -t $IMAGE_NAME .

# Run the Docker container with DB IP and port arguments
docker run -d -p 9000:9000 $IMAGE_NAME --db_host=localhost --db_port=5432

