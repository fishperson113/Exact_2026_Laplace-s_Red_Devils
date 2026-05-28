#!/bin/bash
# Start FastAPI gateway (+ optional cloudflared tunnel).
#
# If vLLM is already running (e.g. Vast AI vLLM template), skips vLLM startup.
# Otherwise starts vLLM first, waits for it, then starts gateway.
#
# Usage:
#   bash scripts/start_server.sh
#
# Env overrides (optional):
#   VLLM_MODEL="Qwen/Qwen3.5-4B"
#   VLLM_PORT=18000              # 18000 = Vast AI template internal port
#   API_PORT=8001
#   SKIP_TUNNEL=1                # skip cloudflared

set -euo pipefail

VLLM_MODEL="${VLLM_MODEL:-Qwen/Qwen3.5-4B}"
VLLM_PORT="${VLLM_PORT:-18000}"
API_PORT="${API_PORT:-8001}"
PROJECT_ROOT="${PROJECT_ROOT:-/root/project}"

cd "$PROJECT_ROOT"

# ---------------------------------------------------------------------------
# 1. Check if vLLM is already running (Vast AI template manages it)
# ---------------------------------------------------------------------------
if curl -sf "http://localhost:$VLLM_PORT/health" > /dev/null 2>&1; then
    echo "=== vLLM already running on port $VLLM_PORT (template-managed) ==="
    # Auto-detect actual model name from vLLM (template may set a different VLLM_MODEL env)
    DETECTED_MODEL=$(curl -sf "http://localhost:$VLLM_PORT/v1/models" \
        | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null)
    if [ -n "$DETECTED_MODEL" ]; then
        VLLM_MODEL="$DETECTED_MODEL"
        echo "Detected model: $VLLM_MODEL"
    fi
    VLLM_PID=""
else
    echo "=== [1/3] Starting vLLM (model=$VLLM_MODEL, port=$VLLM_PORT) ==="
    python -m vllm.entrypoints.openai.api_server \
        --model "$VLLM_MODEL" \
        --dtype bfloat16 \
        --host 0.0.0.0 \
        --port "$VLLM_PORT" \
        --max-model-len 4096 \
        --gpu-memory-utilization 0.90 \
        &
    VLLM_PID=$!

    echo "=== Waiting for vLLM ready (may take 1-2 min) ==="
    until curl -sf "http://localhost:$VLLM_PORT/health" > /dev/null 2>&1; do
        sleep 3
        if ! kill -0 "$VLLM_PID" 2>/dev/null; then
            echo "ERROR: vLLM process died. Check logs above."
            exit 1
        fi
    done
    echo "vLLM ready on port $VLLM_PORT"
fi

# ---------------------------------------------------------------------------
# 2. Start FastAPI gateway (background)
# ---------------------------------------------------------------------------
echo "=== Starting FastAPI gateway (port=$API_PORT, model=$VLLM_MODEL) ==="
VLLM_MODEL="$VLLM_MODEL" \
VLLM_BASE_URL="http://localhost:$VLLM_PORT/v1" \
uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "$API_PORT" \
    --workers 1 \
    --loop uvloop \
    &
API_PID=$!
sleep 2

if curl -sf "http://localhost:$API_PORT/health" | grep -q "ok"; then
    echo "Gateway healthy on port $API_PORT"
else
    echo "WARNING: Gateway health check returned non-ok. Check logs."
fi

# ---------------------------------------------------------------------------
# 3. Start cloudflared tunnel (foreground — URL printed here)
# ---------------------------------------------------------------------------
if [ "${SKIP_TUNNEL:-0}" = "1" ]; then
    echo "=== Tunnel skipped (SKIP_TUNNEL=1). Gateway on port $API_PORT ==="
    trap 'echo "Shutting down..."; kill "$API_PID" ${VLLM_PID:+"$VLLM_PID"} 2>/dev/null; exit 0' INT TERM
    wait "$API_PID"
else
    echo "=== Starting cloudflared tunnel -> localhost:$API_PORT ==="
    echo "The public URL will appear below (trycloudflare.com). Copy it."
    echo ""
    trap 'echo "Shutting down..."; kill "$API_PID" ${VLLM_PID:+"$VLLM_PID"} 2>/dev/null; exit 0' INT TERM
    cloudflared tunnel --url "http://localhost:$API_PORT"
fi
