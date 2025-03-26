#!/bin/bash

# Start Ollama in background if not running
if ! pgrep -f "ollama serve" > /dev/null; then
  echo "Starting Ollama server..."
  ollama serve > /dev/null 2>&1 &
else
  echo "Ollama already running"
fi

# Wait for Ollama to be ready (check /api/tags)
echo "Waiting for Ollama to respond..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 1
done

echo "Ollama is ready!"
