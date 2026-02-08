#!/bin/bash
# Build and run script for Microsoft Magentic-UI Docker container

set -e

IMAGE_NAME="magentic-ui"
IMAGE_VERSION="0.0.1"
REGISTRY=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --push)
            PUSH_FLAG="--push"
            shift
            ;;
        *)
            IMAGE_NAME="$1"
            shift
            ;;
    esac
done

# Default image name if not provided
if [ -z "$IMAGE_NAME" ]; then
    IMAGE_NAME="magentic-ui"
fi

echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_VERSION}"

# Build the Docker image
docker buildx build \
    --platform linux/amd64 \
    -t "${REGISTRY}${IMAGE_NAME}:${IMAGE_VERSION}" \
    -t "${REGISTRY}${IMAGE_NAME}:latest" \
    ${PUSH_FLAG:-} \
    .

echo "Running Docker container..."

# Run the Docker container with port mapping
docker run --rm -it \
    --name magentic-ui-container \
    -p 11240:11240 \
    -v "${PWD}/src:/workspace/src:ro" \
    -v "${PWD}/docker-magentic-ui/config.yaml:/workspace/config.yaml:ro" \
    "${REGISTRY}${IMAGE_NAME}:latest"
