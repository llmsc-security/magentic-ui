#!/bin/bash
# Entrypoint script for Microsoft Magentic-UI Docker container

set -e

# Run the FastAPI application with --run-without-docker flag
# since we're inside a container and don't have access to Docker daemon
exec python3 -m magentic_ui.backend.cli --host 0.0.0.0 --port 8081 --run-without-docker
