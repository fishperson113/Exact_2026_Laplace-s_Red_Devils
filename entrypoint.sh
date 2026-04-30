#!/bin/bash
set -e

ollama serve &
SERVER_PID=$!

if [ -n "$OLLAMA_MODEL" ]; then
  echo "[ollama] Waiting for server to be ready..."
  until curl -sf http://localhost:11434/api/tags > /dev/null; do
    sleep 1
  done
  echo "[ollama] Pulling model: $OLLAMA_MODEL"
  ollama pull "$OLLAMA_MODEL"
  echo "[ollama] Model ready."
fi

wait $SERVER_PID
