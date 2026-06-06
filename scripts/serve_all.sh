#!/bin/bash
# =============================================================================
# serve_all.sh — bring up the EXACT-2026 serving stack on ONE GPU box.
#
# Tuned for a Vast.ai "NVIDIA CUDA Development Environment" instance with a
# CUDA-13 driver (>=580), serving the Qwen3.5-4B (GDN-hybrid) family via vLLM.
# vLLM has its OWN GDN / causal-conv1d kernels — no `fla` / `causal-conv1d` /
# transformers wheels needed for SERVING (those are only for the HF/Unsloth
# finetune path).
#
# Architecture (single competition endpoint):
#     vLLM    -> :18000   one Qwen3.5-4B model
#     gateway -> :9000    POST /ask  (routes by request shape; BTC hits this)
#
# MODE (env SERVE_MODE):
#   shared  (DEFAULT, current) — ONE vLLM serves all 3 roles (physics + the two
#           logic stages). Used now because the two finetuned Qwen3.5-4B logic
#           models aren't uploaded yet; everything points at the physics model.
#   triple  (future) — 3 DISTINCT Qwen3.5-4B. They don't co-reside on 24GB
#           (3x ~9.3GB > 24GB), so that mode needs vLLM sleep-mode swap
#           (--enable-sleep-mode + VLLM_SERVER_DEV_MODE=1, gateway wakes the
#           target server and sleeps the others). Stubbed below; not wired yet.
#
# Usage (on the server, from the project root):
#     bash scripts/serve_all.sh start | stop | status
#
# Env overrides (all optional):
#   PROJECT_ROOT=/workspace/project   VENV=/venv/main
#   SERVE_MODEL=Laplaces-Red-Devils/physics-v04-optimized_routing-qwen3.5-4b
#   SERVED_NAME=physics   VLLM_PORT=18000   API_PORT=9000
#   GPU_UTIL=0.85   MAX_MODEL_LEN=8192
#   HF_HOME=/dev/shm/hf                 # model cache (RAM-backed; fits 1 model)
#   HF_TOKEN=hf_...                     # gated repo; else read secret.env/.env
#   SKIP_TUNNEL=1                       # 0 => start cloudflared quick tunnel
# =============================================================================
set -uo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/workspace/project}"
VENV="${VENV:-/venv/main}"
PY="$VENV/bin/python"
VLLM_BIN="$VENV/bin/vllm"

SERVE_MODE="${SERVE_MODE:-shared}"
SERVE_MODEL="${SERVE_MODEL:-Laplaces-Red-Devils/physics-v04-optimized_routing-qwen3.5-4b}"
SERVED_NAME="${SERVED_NAME:-physics}"
VLLM_PORT="${VLLM_PORT:-18000}"
API_PORT="${API_PORT:-9000}"
GPU_UTIL="${GPU_UTIL:-0.85}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-8192}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-16}"

export HF_HOME="${HF_HOME:-/dev/shm/hf}"
export HF_HUB_ENABLE_HF_TRANSFER="${HF_HUB_ENABLE_HF_TRANSFER:-1}"
export TOKENIZERS_PARALLELISM=false
# flashinfer sampler has crashed on some stacks; vLLM's default sampler is fine.
export VLLM_USE_FLASHINFER_SAMPLER="${VLLM_USE_FLASHINFER_SAMPLER:-0}"

RUN_DIR="$PROJECT_ROOT/.run"
LOG_DIR="${LOG_DIR:-/workspace/logs}"
WAIT_TIMEOUT="${WAIT_TIMEOUT:-1800}"

mkdir -p "$RUN_DIR" "$LOG_DIR" "$HF_HOME"
cd "$PROJECT_ROOT" 2>/dev/null || true

log() { echo -e "\033[0;36m[serve_all]\033[0m $*"; }
err() { echo -e "\033[0;31m[serve_all] ERROR:\033[0m $*" >&2; }
health_ok() { curl -sf -m 3 "http://127.0.0.1:$1/health" >/dev/null 2>&1; }

stop_all() {
    log "Stopping gateway + vLLM + tunnel..."
    for name in gateway vllm tunnel; do
        pidf="$RUN_DIR/$name.pid"
        if [ -f "$pidf" ]; then
            pid="$(cat "$pidf" 2>/dev/null)"
            [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && { kill "$pid" 2>/dev/null && log "  killed $name (pid $pid)"; }
            rm -f "$pidf"
        fi
    done
    # free any leftover on our ports (fuser, NOT a vllm/cloudflared pkill string
    # — that would match this ssh command and self-kill the shell)
    for p in "$VLLM_PORT" "$API_PORT"; do fuser -k "${p}/tcp" 2>/dev/null || true; done
}

status_all() {
    for pair in "vllm:$VLLM_PORT" "gateway:$API_PORT"; do
        n="${pair%%:*}"; p="${pair##*:}"
        if health_ok "$p"; then echo "  $n (:$p) -> UP"; else echo "  $n (:$p) -> down"; fi
    done
}

load_hf_token() {
    [ -n "${HF_TOKEN:-}" ] && return 0
    HF_TOKEN="${HF_TOKEN_CC:-}"
    for f in /workspace/secret.env "$PROJECT_ROOT/app/physics_solution/.env"; do
        [ -n "${HF_TOKEN:-}" ] && break
        [ -f "$f" ] && HF_TOKEN="$(grep -E '^HF_TOKEN_CC=' "$f" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')"
    done
    export HF_TOKEN HUGGING_FACE_HUB_TOKEN="${HF_TOKEN:-}"
}

wait_health() {  # name port
    local name="$1" port="$2" pidf="$RUN_DIR/$1.pid" waited=0
    local pid; pid="$(cat "$pidf" 2>/dev/null)"
    log "Waiting for '$name' (:$port) ready (download+load can take minutes)..."
    until health_ok "$port"; do
        sleep 4; waited=$((waited+4))
        if [ -n "$pid" ] && ! kill -0 "$pid" 2>/dev/null; then
            err "'$name' died. Last log:"; tail -30 "$LOG_DIR/$name.log" >&2; return 1
        fi
        [ "$waited" -ge "$WAIT_TIMEOUT" ] && { err "'$name' not ready in ${WAIT_TIMEOUT}s"; return 1; }
    done
    log "'$name' READY on :$port (${waited}s)"
}

case "${1:-start}" in
    stop)   stop_all; exit 0 ;;
    status) log "Health:"; status_all; exit 0 ;;
    start)  ;;
    *) err "unknown subcommand '$1' (use: start | stop | status)"; exit 2 ;;
esac

[ -x "$VLLM_BIN" ] || { err "vllm not at $VLLM_BIN — run setup_env.sh first."; exit 1; }
if ! "$PY" -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
    err "torch can't see CUDA in $VENV (driver too old for this torch build?)."; exit 1
fi
load_hf_token
[ -n "${HF_TOKEN:-}" ] && log "HF token loaded." || log "No HF token (gated model will 401)."

if [ "$SERVE_MODE" != "shared" ]; then
    err "SERVE_MODE=$SERVE_MODE not implemented yet. Only 'shared' is wired."
    err "For 3 distinct Qwen3.5-4B: they exceed 24GB co-resident -> use vLLM sleep-swap"
    err "(--enable-sleep-mode + VLLM_SERVER_DEV_MODE=1 + gateway wake/sleep)."
    exit 2
fi

# ---- ONE vLLM serving the model; all 3 gateway roles point at it ----
if health_ok "$VLLM_PORT"; then
    log "vLLM already healthy on :$VLLM_PORT — skip."
else
    log "Starting vLLM '$SERVED_NAME' ($SERVE_MODEL) on :$VLLM_PORT (gpu-util=$GPU_UTIL)"
    OMP_NUM_THREADS=8 \
    nohup "$VLLM_BIN" serve "$SERVE_MODEL" \
        --served-model-name "$SERVED_NAME" \
        --host 127.0.0.1 --port "$VLLM_PORT" \
        --dtype bfloat16 --gpu-memory-utilization "$GPU_UTIL" \
        --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
        --enforce-eager \
        </dev/null >"$LOG_DIR/vllm.log" 2>&1 &
    echo $! > "$RUN_DIR/vllm.pid"; disown 2>/dev/null || true
    wait_health vllm "$VLLM_PORT" || { err "vLLM failed to start; aborting."; exit 1; }
fi

# ---- FastAPI gateway: point physics + both logic roles at the one server ----
if health_ok "$API_PORT"; then
    log "Gateway already healthy on :$API_PORT — skip."
else
    log "Starting FastAPI gateway on :$API_PORT (all roles -> :$VLLM_PORT/$SERVED_NAME)"
    V1="http://127.0.0.1:$VLLM_PORT/v1"
    VLLM_MODEL="$SERVED_NAME" VLLM_BASE_URL="$V1" \
    FOL_MODEL="$SERVED_NAME"  FOL_BASE_URL="$V1" \
    QA_MODEL="$SERVED_NAME"   QA_BASE_URL="$V1" \
    PYTHONPATH="$PROJECT_ROOT" \
    nohup "$PY" -m uvicorn app.main:app --host 0.0.0.0 --port "$API_PORT" \
        --workers 1 --loop uvloop </dev/null >"$LOG_DIR/gateway.log" 2>&1 &
    echo $! > "$RUN_DIR/gateway.pid"; disown 2>/dev/null || true
    for _ in $(seq 1 20); do health_ok "$API_PORT" && break; sleep 2; done
fi

log "Gateway /health: $(curl -sf -m3 "http://127.0.0.1:$API_PORT/health" 2>/dev/null || echo '(not ready)')"
echo; log "=== STACK UP ==="; status_all
echo; log "Test from laptop:  ssh -p <PORT> root@<HOST> -L $API_PORT:localhost:$API_PORT  then http://localhost:$API_PORT/docs"

# ---- optional public tunnel for BTC ----
if [ "${SKIP_TUNNEL:-1}" = "1" ]; then
    log "SKIP_TUNNEL=1 (default) — no public tunnel."
    exit 0
fi
command -v cloudflared >/dev/null 2>&1 || { err "cloudflared not installed; skipping tunnel."; exit 0; }
TPID="$(cat "$RUN_DIR/tunnel.pid" 2>/dev/null || true)"
if [ -n "$TPID" ] && kill -0 "$TPID" 2>/dev/null; then
    log "cloudflared already running: $(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG_DIR/cloudflared.log" 2>/dev/null | head -1)/ask"
    exit 0
fi
: > "$LOG_DIR/cloudflared.log"
setsid cloudflared tunnel --url "http://localhost:$API_PORT" --no-autoupdate \
    >"$LOG_DIR/cloudflared.log" 2>&1 </dev/null &
echo $! > "$RUN_DIR/tunnel.pid"; disown 2>/dev/null || true
URL=""
for _ in $(seq 1 20); do
    URL="$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG_DIR/cloudflared.log" | head -1)"
    [ -n "$URL" ] && break; sleep 2
done
[ -n "$URL" ] && log "=== PUBLIC ENDPOINT (give BTC) ===  $URL/ask" \
              || err "No tunnel URL yet (shared-IP rate limit?). Fallback: reverse-SSH :$API_PORT to your VPS."
exit 0
