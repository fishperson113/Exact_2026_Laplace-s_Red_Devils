#!/bin/bash
# =============================================================================
# serve_all.sh — bring up the EXACT-2026 serving stack on ONE GPU box.
#
# For a Vast "NVIDIA CUDA Development Environment" box with a CUDA-13 driver
# (>=580), serving the Qwen3.5-4B (GDN-hybrid) family via vLLM. vLLM has its OWN
# GDN/causal-conv1d kernels — serving needs NO fla/causal-conv1d/transformers
# spells (those are only for the HF/Unsloth finetune path).
#
# ONE FastAPI gateway (:9000, POST /ask, BTC hits this) routes by request shape:
#   premises-NL present -> Type 1 (logic, FOL->QA);  question only -> Type 2 (physics).
#
# SERVE_MODE:
#   shared (DEFAULT) — ONE vLLM (:18000) serves all 3 roles. Used while the two
#         finetuned Qwen3.5-4B logic models aren't uploaded (physics-v04 stands in).
#   triple — 3 DISTINCT Qwen3.5-4B (fol :18001, qa :18002, physics :18000). They
#         exceed 24GB co-resident, so each runs with --enable-sleep-mode and the
#         gateway wakes the needed group and sleeps the rest per request
#         (logic group = {fol,qa}; physics group = {physics}). Set the 3 repos via
#         FOL_REPO/QA_REPO/PHYSICS_REPO (default: all = SERVE_MODEL placeholder).
#
# Usage:  bash scripts/serve_all.sh start | stop | status
# Key env: SERVE_MODE, SERVE_MODEL, FOL_REPO/QA_REPO/PHYSICS_REPO, GPU_UTIL,
#          FOL_GPU/QA_GPU/PHYSICS_GPU, MAX_MODEL_LEN, HF_TOKEN, SKIP_TUNNEL.
# =============================================================================
set -uo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/workspace/project}"
VENV="${VENV:-/venv/main}"
PY="$VENV/bin/python"
VLLM_BIN="$VENV/bin/vllm"

SERVE_MODE="${SERVE_MODE:-shared}"
SERVE_MODEL="${SERVE_MODEL:-Laplaces-Red-Devils/physics-v04-optimized_routing-qwen3.5-4b}"
SERVED_NAME="${SERVED_NAME:-physics}"

# triple-mode repos (default to the placeholder so the swap is testable now)
FOL_REPO="${FOL_REPO:-$SERVE_MODEL}"
QA_REPO="${QA_REPO:-$SERVE_MODEL}"
PHYSICS_REPO="${PHYSICS_REPO:-$SERVE_MODEL}"

VLLM_PORT="${VLLM_PORT:-18000}"
FOL_PORT="${FOL_PORT:-18001}"
QA_PORT="${QA_PORT:-18002}"
PHYSICS_PORT="${PHYSICS_PORT:-18000}"
API_PORT="${API_PORT:-9000}"

GPU_UTIL="${GPU_UTIL:-0.85}"                 # shared mode (1 model alone)
PHYSICS_GPU="${PHYSICS_GPU:-0.85}"           # triple: physics awake alone
FOL_GPU="${FOL_GPU:-0.45}"                   # triple: fol+qa awake together (~0.9)
QA_GPU="${QA_GPU:-0.45}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-8192}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-16}"
# ENFORCE_EAGER=1 (default) keeps vLLM in eager mode (lower VRAM, safe for serving).
# Set ENFORCE_EAGER=0 to enable CUDA graphs (faster decode) — useful for high-throughput
# data-gen where the KV cache has headroom. Pair with a larger MAX_NUM_SEQS.
ENFORCE_EAGER="${ENFORCE_EAGER:-1}"

export HF_HOME="${HF_HOME:-/dev/shm/hf}"
export HF_HUB_ENABLE_HF_TRANSFER="${HF_HUB_ENABLE_HF_TRANSFER:-1}"
export TOKENIZERS_PARALLELISM=false
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
    for name in gateway vllm vllm_fol vllm_qa vllm_physics tunnel; do
        pidf="$RUN_DIR/$name.pid"; [ -f "$pidf" ] || continue
        pid="$(cat "$pidf" 2>/dev/null)"
        [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && { kill "$pid" 2>/dev/null && log "  killed $name ($pid)"; }
        rm -f "$pidf"
    done
    # vLLM spawns EngineCore GPU workers that are NOT the port listener; fuser
    # alone leaves them holding VRAM. Kill GPU compute procs directly (dedicated box).
    for p in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader 2>/dev/null); do kill "$p" 2>/dev/null; done
    sleep 2
    for p in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader 2>/dev/null); do kill -9 "$p" 2>/dev/null; done
    for p in "$VLLM_PORT" "$FOL_PORT" "$QA_PORT" "$API_PORT"; do fuser -k "${p}/tcp" 2>/dev/null || true; done
}

status_all() {
    if [ "$SERVE_MODE" = "triple" ]; then
        local pairs="physics:$PHYSICS_PORT fol:$FOL_PORT qa:$QA_PORT gateway:$API_PORT"
    else
        local pairs="vllm:$VLLM_PORT gateway:$API_PORT"
    fi
    for pair in $pairs; do
        n="${pair%%:*}"; p="${pair##*:}"
        if health_ok "$p"; then echo "  $n (:$p) -> UP"; else echo "  $n (:$p) -> down"; fi
    done
}

load_hf_token() {
    [ -n "${HF_TOKEN:-}" ] && { export HUGGING_FACE_HUB_TOKEN="$HF_TOKEN"; return 0; }
    HF_TOKEN="${HF_TOKEN_CC:-}"
    for f in /workspace/secret.env "$PROJECT_ROOT/app/physics_solution/.env"; do
        [ -n "${HF_TOKEN:-}" ] && break
        [ -f "$f" ] && HF_TOKEN="$(grep -E '^HF_TOKEN_CC=' "$f" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')"
    done
    export HF_TOKEN HUGGING_FACE_HUB_TOKEN="${HF_TOKEN:-}"
}

wait_health() {  # logname port
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

# start_vllm: logname repo port util sleepmode(0/1) served-name
start_vllm() {
    local logname="$1" repo="$2" port="$3" util="$4" sleepmode="${5:-0}" served="${6:-$1}"
    if health_ok "$port"; then log "$logname healthy on :$port — skip."; return 0; fi
    local extra=""
    if [ "$sleepmode" = "1" ]; then extra="--enable-sleep-mode"; export VLLM_SERVER_DEV_MODE=1; else unset VLLM_SERVER_DEV_MODE; fi
    [ "$ENFORCE_EAGER" = "1" ] && extra="$extra --enforce-eager"
    log "Starting vLLM '$logname' ($repo -> served '$served') :$port util=$util sleep=$sleepmode eager=$ENFORCE_EAGER seqs=$MAX_NUM_SEQS"
    OMP_NUM_THREADS=8 \
    nohup "$VLLM_BIN" serve "$repo" --served-model-name "$served" \
        --host 127.0.0.1 --port "$port" --dtype bfloat16 \
        --gpu-memory-utilization "$util" --max-model-len "$MAX_MODEL_LEN" \
        --max-num-seqs "$MAX_NUM_SEQS" $extra \
        </dev/null >"$LOG_DIR/$logname.log" 2>&1 &
    echo $! > "$RUN_DIR/$logname.pid"; disown 2>/dev/null || true
    wait_health "$logname" "$port"
}

sleep_server() {  # port — offload after load so the next server has free VRAM
    if curl -s -m 30 -X POST "http://127.0.0.1:$1/sleep?level=1" >/dev/null 2>&1; then
        log "  slept :$1 (VRAM freed)"
    else err "  sleep :$1 failed (need VLLM_SERVER_DEV_MODE=1)"; fi
}

case "${1:-start}" in
    stop)   stop_all; exit 0 ;;
    status) log "Health:"; status_all; exit 0 ;;
    start)  ;;
    *) err "unknown subcommand '$1' (use: start | stop | status)"; exit 2 ;;
esac

[ -x "$VLLM_BIN" ] || { err "vllm not at $VLLM_BIN — run setup_env.sh first."; exit 1; }
if ! "$PY" -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
    err "torch can't see CUDA in $VENV (driver too old for this torch build? need CUDA13/driver>=580)."; exit 1
fi
load_hf_token
[ -n "${HF_TOKEN:-}" ] && log "HF token loaded." || log "No HF token (gated model will 401)."

# ---------------------------------------------------------------------------
# Launch vLLM server(s)
# ---------------------------------------------------------------------------
if [ "$SERVE_MODE" = "triple" ]; then
    log "SERVE_MODE=triple — 3 distinct models with sleep-swap."
    # Start sequentially; SLEEP each right after it loads so the next sees free VRAM.
    start_vllm vllm_fol     "$FOL_REPO"     "$FOL_PORT"     "$FOL_GPU"     1 fol     || { err "fol failed";     exit 1; }
    sleep_server "$FOL_PORT"
    start_vllm vllm_qa      "$QA_REPO"      "$QA_PORT"      "$QA_GPU"      1 qa      || { err "qa failed";      exit 1; }
    sleep_server "$QA_PORT"
    start_vllm vllm_physics "$PHYSICS_REPO" "$PHYSICS_PORT" "$PHYSICS_GPU" 1 physics || { err "physics failed"; exit 1; }
    sleep_server "$PHYSICS_PORT"
    log "All 3 servers loaded + asleep; gateway will wake the needed group per request."
    GW_ENV=(VLLM_MODEL=physics VLLM_BASE_URL="http://127.0.0.1:$PHYSICS_PORT/v1"
            FOL_MODEL=fol      FOL_BASE_URL="http://127.0.0.1:$FOL_PORT/v1"
            QA_MODEL=qa        QA_BASE_URL="http://127.0.0.1:$QA_PORT/v1"
            SLEEP_SWAP_ENABLED=1)
else
    start_vllm vllm "$SERVE_MODEL" "$VLLM_PORT" "$GPU_UTIL" 0 "$SERVED_NAME" || { err "vLLM failed."; exit 1; }
    V1="http://127.0.0.1:$VLLM_PORT/v1"
    GW_ENV=(VLLM_MODEL="$SERVED_NAME" VLLM_BASE_URL="$V1"
            FOL_MODEL="$SERVED_NAME"  FOL_BASE_URL="$V1"
            QA_MODEL="$SERVED_NAME"   QA_BASE_URL="$V1"
            SLEEP_SWAP_ENABLED=0)
fi

# ---------------------------------------------------------------------------
# FastAPI gateway
# ---------------------------------------------------------------------------
if health_ok "$API_PORT"; then
    log "Gateway already healthy on :$API_PORT — skip."
else
    log "Starting FastAPI gateway on :$API_PORT"
    env "${GW_ENV[@]}" PYTHONPATH="$PROJECT_ROOT" \
        nohup "$PY" -m uvicorn app.main:app --host 0.0.0.0 --port "$API_PORT" \
        --workers 1 --loop uvloop </dev/null >"$LOG_DIR/gateway.log" 2>&1 &
    echo $! > "$RUN_DIR/gateway.pid"; disown 2>/dev/null || true
    for _ in $(seq 1 20); do health_ok "$API_PORT" && break; sleep 2; done
fi

log "Gateway /health: $(curl -sf -m3 "http://127.0.0.1:$API_PORT/health" 2>/dev/null || echo '(not ready)')"
echo; log "=== STACK UP (mode=$SERVE_MODE) ==="; status_all
echo; log "Test from laptop:  ssh -p <PORT> root@<HOST> -L $API_PORT:localhost:$API_PORT  then http://localhost:$API_PORT/docs"

# ---------------------------------------------------------------------------
# optional public tunnel for BTC
# ---------------------------------------------------------------------------
if [ "${SKIP_TUNNEL:-1}" = "1" ]; then log "SKIP_TUNNEL=1 — no public tunnel."; exit 0; fi
command -v cloudflared >/dev/null 2>&1 || { err "cloudflared not installed; skipping tunnel."; exit 0; }
TPID="$(cat "$RUN_DIR/tunnel.pid" 2>/dev/null || true)"
if [ -n "$TPID" ] && kill -0 "$TPID" 2>/dev/null; then
    log "cloudflared running: $(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG_DIR/cloudflared.log" 2>/dev/null | head -1)/ask"; exit 0
fi
: > "$LOG_DIR/cloudflared.log"
setsid cloudflared tunnel --url "http://localhost:$API_PORT" --no-autoupdate >"$LOG_DIR/cloudflared.log" 2>&1 </dev/null &
echo $! > "$RUN_DIR/tunnel.pid"; disown 2>/dev/null || true
URL=""; for _ in $(seq 1 20); do URL="$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG_DIR/cloudflared.log" | head -1)"; [ -n "$URL" ] && break; sleep 2; done
[ -n "$URL" ] && log "=== PUBLIC ENDPOINT (give BTC) ===  $URL/ask" \
              || err "No tunnel URL yet (shared-IP rate limit?). Fallback: reverse-SSH :$API_PORT to your VPS."
exit 0
