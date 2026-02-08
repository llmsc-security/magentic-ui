#!/bin/bash
# Entrypoint script for Microsoft Magentic-UI Docker container

set -e

# Run the FastAPI application
# magentic-ui CLI command starts the FastAPI server on port 8081
exec python3 -m magentic_ui.backend.cli --host 0.0.0.0 --port 8081
