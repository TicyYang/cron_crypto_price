#!/bin/bash

IMAGE_NAME="crypto"
CONTAINER_NAME="crypto_ctr"

docker build -t $IMAGE_NAME .

docker run --name $CONTAINER_NAME -v ~/datasets:/app/datasets $IMAGE_NAME
