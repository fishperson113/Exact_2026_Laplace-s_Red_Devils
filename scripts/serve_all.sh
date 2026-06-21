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

# combined = full competition stack (both task types). shared/triple kept for testing.
SERVE_MODE="${SERVE_MODE:-combined}"
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
# ENFORCE_EAGER=1 keeps vLLM eager (lower VRAM). 0 = CUDA graphs (faster decode).
# physics_ensemble runs ONE small model with a huge KV cache, so CUDA graphs are a big
# win there (golden_60: median 8.9s vs ~15s eager, max 22s vs ~60s) -> default 0 for it,
# 1 elsewhere. User override always wins.
_EAGER_DEFAULT=1; [ "$SERVE_MODE" = "physics_ensemble" ] && _EAGER_DEFAULT=0
ENFORCE_EAGER="${ENFORCE_EAGER:-$_EAGER_DEFAULT}"

# Model storage: these Vast boxes often have a TINY disk (e.g. 32GB overlay, mostly
# eaten by the vLLM install) but a big /dev/shm (RAM). The box may also preset HF_HOME
# to a small-disk path. So put the HF cache on /dev/shm unless the chosen path has
# >=45GB free. Models in RAM also load faster. Override with HF_HOME to force a path.
_fs_free_g() { df -BG --output=avail "$1" 2>/dev/null | tail -1 | tr -dc '0-9'; }
_HF_CAND="${HF_HOME:-/dev/shm/hf}"; mkdir -p "$_HF_CAND" 2>/dev/null
_HF_FREE="$(_fs_free_g "$_HF_CAND")"
if [ -z "$_HF_FREE" ] || [ "$_HF_FREE" -lt 45 ]; then
    [ "$_HF_CAND" != "/dev/shm/hf" ] && echo "[serve_all] HF_HOME '$_HF_CAND' has only ${_HF_FREE:-?}GB free -> using /dev/shm/hf (RAM)."
    _HF_CAND="/dev/shm/hf"
fi
export HF_HOME="$_HF_CAND"
# xet is the ONLY fast HF download path now (hf_transfer is deprecated/ignored). It
# stages chunks to HF_HOME/xet — which is on /dev/shm above, so it's fast AND fits.
# (Disabling xet fell back to plain HTTP = painfully slow / looks hung.) Keep it ON.
export HF_HUB_DISABLE_XET="${HF_HUB_DISABLE_XET:-0}"
export HF_XET_HIGH_PERFORMANCE="${HF_XET_HIGH_PERFORMANCE:-1}"
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
    log "Stopping gateway + vLLM + tunnels..."
    for name in gateway vllm vllm_fol vllm_qa vllm_physics vllm_base \
                tunnel cf_gateway cf_vllm0 cf_vllm1 cf_vllm2; do
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
    if [ "$SERVE_MODE" = "combined" ]; then
        local pairs="base(sft+qa):$VLLM_PORT fol:$FOL_PORT gateway:$API_PORT"
    elif [ "$SERVE_MODE" = "triple" ]; then
        local pairs="physics(base+sft):$VLLM_PORT fol:$FOL_PORT qa:$QA_PORT gateway:$API_PORT"
    elif [ "$SERVE_MODE" = "physics_ensemble" ]; then
        local pairs="vllm(base+sft):$VLLM_PORT gateway:$API_PORT"
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
if [ "$SERVE_MODE" = "physics_ensemble" ]; then
    # ONE vLLM serves the BASE Qwen3.5-4B (vLLM-supported arch Qwen3_5ForConditionalGeneration)
    # AND the SFT as a LoRA adapter (the adapter's keys match the composite base's
    # language_model.*). It exposes BOTH model ids on /v1/models: "base" (voter #2 + judge)
    # and "sft" (primary solver). Total params ~4B (one base + tiny adapter) << 8B.
    # NOTE: the text-only MERGED checkpoint (arch Qwen3_5ForCausalLM, model_type qwen3_5_text)
    # is NOT servable by vLLM 0.22.1 — LoRA serving is the working path (and uses less VRAM,
    # so a single base gives a huge KV cache → both base+sft requests batch on one engine).
    BASE_REPO="${BASE_REPO:-Qwen/Qwen3.5-4B}"
    SFT_ADAPTER="${SFT_ADAPTER:-Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b}"
    MAX_LORA_RANK="${MAX_LORA_RANK:-16}"
    log "SERVE_MODE=physics_ensemble (LoRA) — BASE($BASE_REPO) + adapter sft=$SFT_ADAPTER on :$VLLM_PORT"
    if ! health_ok "$VLLM_PORT"; then
        extra=""; [ "$ENFORCE_EAGER" = "1" ] && extra="--enforce-eager"
        OMP_NUM_THREADS=8 nohup "$VLLM_BIN" serve "$BASE_REPO" --served-model-name base \
            --host 0.0.0.0 --port "$VLLM_PORT" --dtype bfloat16 \
            --gpu-memory-utilization "$GPU_UTIL" --max-model-len "$MAX_MODEL_LEN" \
            --max-num-seqs "$MAX_NUM_SEQS" --enable-lora --max-lora-rank "$MAX_LORA_RANK" \
            --lora-modules "sft=$SFT_ADAPTER" $extra \
            </dev/null >"$LOG_DIR/vllm_physics.log" 2>&1 &
        echo $! > "$RUN_DIR/vllm_physics.pid"; disown 2>/dev/null || true
        wait_health vllm_physics "$VLLM_PORT" || { err "vLLM (base+LoRA) failed."; exit 1; }
    fi
    log "Serving base+sft on :$VLLM_PORT. /v1/models lists both (BTC verify): curl :$VLLM_PORT/v1/models"
    GW_ENV=(PIPELINE_VERSION=v07_ensemble_vLLM
            VLLM_MODEL=sft   VLLM_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            JUDGE_MODEL=base JUDGE_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            FOL_MODEL=base   FOL_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            QA_MODEL=base    QA_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            SLEEP_SWAP_ENABLED=0)
elif [ "$SERVE_MODE" = "combined" ]; then
    # FULL competition stack on ONE GPU, both task types. Model layout matches the
    # authoritative logic config (app/logic_solution/config.yaml):
    #   :18000 base Qwen3.5-4B + LoRA(sft=physics) + LoRA(qa=qa-v05-cot)   ids: base, sft, qa
    #          (qa default tracks app/logic_solution/config.yaml; override via $QA_ADAPTER)
    #          Serves physics (sft) AND logic stage-2 QA (qa adapter).
    #   :18001 fol = fol-v06-cot-augmented (full finetune, grafted)        id: fol  (logic stage 1)
    #
    # Peak GPU residency is ~8B EITHER WAY (base 4B + fol 4B; sft/qa are tiny LoRA deltas),
    # which already satisfies the ≤8B rule. So RESIDENT_ALL=1 (DEFAULT): keep BOTH engines
    # awake on the 32GB GPU — no sleep/wake, no per-type swap cost, fewer failure modes.
    # RESIDENT_ALL=0 falls back to sleep-swap (fol slept during type2 -> base alone 4B) for
    # tighter GPUs. The qa LoRA shares :18000 with physics, so swap only ever toggles fol.
    #
    # FOL ships as text-only Qwen3_5ForCausalLM (NOT vLLM-servable) -> graft onto the
    # composite base first (idempotent). QA ships as a LoRA adapter -> served on the base
    # engine exactly like the physics sft adapter (no graft).
    BASE_REPO="${BASE_REPO:-Qwen/Qwen3.5-4B}"
    SFT_ADAPTER="${SFT_ADAPTER:-Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b}"
    QA_ADAPTER="${QA_ADAPTER:-Laplaces-Red-Devils/qa-v05-cot-Qwen3.5-4B}"
    MAX_LORA_RANK="${MAX_LORA_RANK:-32}"     # must cover BOTH adapters (sft + qa)
    MAX_LORAS="${MAX_LORAS:-2}"              # 2 registered adapters on one base engine
    FOL_FT="${FOL_FT:-Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4}"
    MODELS_DIR="${MODELS_DIR:-/dev/shm/models}"
    PHYSICS_EAGER="${PHYSICS_EAGER:-0}"      # base: CUDA graphs ON (big decode win for ensemble)
    RESIDENT_ALL="${RESIDENT_ALL:-1}"

    if [ "$RESIDENT_ALL" = "1" ]; then
        # Both engines AWAKE together. Co-resident utils must leave room for BOTH on 32GB:
        # fol ~0.40 (eager, weights 8GB + small KV) + base ~0.48 -> ~28GB, ~4GB headroom.
        FOL_UTIL="${FOL_GPU_RESIDENT:-0.40}"; BASE_UTIL="${GPU_UTIL_RESIDENT:-0.48}"
        SLEEPMODE=0; SWAP=0
    else
        # Sleep-swap fol by type; base keeps the big KV (fol asleep frees VRAM).
        FOL_UTIL="$FOL_GPU"; BASE_UTIL="$GPU_UTIL"
        SLEEPMODE=1; SWAP=1
    fi

    log "SERVE_MODE=combined (resident_all=$RESIDENT_ALL) — grafting FOL -> composite (idempotent)..."
    HF_HOME="$HF_HOME" HF_TOKEN="${HF_TOKEN:-}" HUGGING_FACE_HUB_TOKEN="${HF_TOKEN:-}" \
    "$PY" "$PROJECT_ROOT/scripts/graft_text_to_composite.py" \
        --base "$BASE_REPO" --finetune "$FOL_FT" --out "$MODELS_DIR/fol-composite" --rm-finetune \
        >>"$LOG_DIR/graft.log" 2>&1 \
      || { err "graft of fol failed — see $LOG_DIR/graft.log"; exit 1; }
    log "  fol -> $MODELS_DIR/fol-composite ready"

    # Re-key the LoRA adapters to the COMPOSITE namespace (idempotent). A LoRA trained on the
    # text-only Qwen3.5-4B exports keys without `language_model`, which vLLM silently binds to
    # nothing on the composite base = a NO-OP (serving id == base output). A text-only-trained
    # QA adapter (e.g. qa-v05-cot / v04-QA-CoT) needs this; physics-v07c-sft is already
    # composite-namespace (0 keys re-keyed; re-key is idempotent either way). Serve local dirs.
    for spec in "sft:$SFT_ADAPTER" "qa:$QA_ADAPTER"; do
        nm="${spec%%:*}"; rp="${spec#*:}"
        HF_HOME="$HF_HOME" HF_TOKEN="${HF_TOKEN:-}" HUGGING_FACE_HUB_TOKEN="${HF_TOKEN:-}" \
        "$PY" "$PROJECT_ROOT/scripts/rekey_lora_to_composite.py" \
            --adapter "$rp" --out "$MODELS_DIR/$nm-lora" >>"$LOG_DIR/graft.log" 2>&1 \
          || { err "re-key of $nm adapter failed — see $LOG_DIR/graft.log"; exit 1; }
        log "  $nm adapter -> $MODELS_DIR/$nm-lora ready"
    done
    SFT_LORA="$MODELS_DIR/sft-lora"; QA_LORA="$MODELS_DIR/qa-lora"

    # FOL server. resident: stays awake. swap: sleep it after load so base sees free VRAM.
    start_vllm vllm_fol "$MODELS_DIR/fol-composite" "$FOL_PORT" "$FOL_UTIL" "$SLEEPMODE" fol || { err "fol failed"; exit 1; }
    [ "$SWAP" = "1" ] && sleep_server "$FOL_PORT"

    # base + 2 LoRA adapters (sft=physics, qa=logic) on :18000.
    if ! health_ok "$VLLM_PORT"; then
        extra="--enable-lora --max-lora-rank $MAX_LORA_RANK --max-loras $MAX_LORAS --lora-modules sft=$SFT_LORA qa=$QA_LORA"
        [ "$SWAP" = "1" ] && { export VLLM_SERVER_DEV_MODE=1; extra="--enable-sleep-mode $extra"; }
        [ "$PHYSICS_EAGER" = "1" ] && extra="$extra --enforce-eager"
        log "Starting base+LoRA ($BASE_REPO + sft=$SFT_ADAPTER + qa=$QA_ADAPTER) :$VLLM_PORT util=$BASE_UTIL swap=$SWAP eager=$PHYSICS_EAGER"
        OMP_NUM_THREADS=8 nohup "$VLLM_BIN" serve "$BASE_REPO" --served-model-name base \
            --host 0.0.0.0 --port "$VLLM_PORT" --dtype bfloat16 \
            --gpu-memory-utilization "$BASE_UTIL" --max-model-len "$MAX_MODEL_LEN" \
            --max-num-seqs "$MAX_NUM_SEQS" $extra \
            </dev/null >"$LOG_DIR/vllm_physics.log" 2>&1 &
        echo $! > "$RUN_DIR/vllm_physics.pid"; disown 2>/dev/null || true
        wait_health vllm_physics "$VLLM_PORT" || { err "base+LoRA failed."; exit 1; }
    fi
    if [ "$SWAP" = "1" ]; then
        log "Combined stack (swap): base(sft+qa):$VLLM_PORT awake; fol:$FOL_PORT asleep. Gateway wakes fol on type1."
    else
        log "Combined stack (resident): base(sft+qa):$VLLM_PORT + fol:$FOL_PORT both awake (~8B peak). No swap."
    fi
    GW_ENV=(PIPELINE_VERSION=v07_ensemble_vLLM
            VLLM_MODEL=sft   VLLM_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            JUDGE_MODEL=base JUDGE_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            FOL_MODEL=fol    FOL_BASE_URL="http://127.0.0.1:$FOL_PORT/v1"
            QA_MODEL=qa      QA_BASE_URL="http://127.0.0.1:$VLLM_PORT/v1"
            SLEEP_SWAP_ENABLED=$SWAP)
elif [ "$SERVE_MODE" = "triple" ]; then
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

# Warm-up: send one /predict so the grader's FIRST real query isn't a cold-start
# (cold first request was ~60s; warmed requests are ~10-22s). Best-effort, non-fatal.
if health_ok "$API_PORT"; then
    # Warm BOTH types so the grader's first query of EITHER type isn't a cold swap.
    # type1 first (swaps in the logic group), then type2 (swaps back) -> end physics-awake.
    if [ "$SERVE_MODE" = "combined" ] || [ "$SERVE_MODE" = "triple" ]; then
        log "Warming type1 (logic group)..."
        curl -s -m 120 "http://127.0.0.1:$API_PORT/predict" -H 'Content-Type: application/json' \
          -d '{"query_id":"warmup1","type":"type1","query":"Is a cat an animal?","premises":["All cats are animals.","Tom is a cat."],"options":["Yes","No"]}' \
          >/dev/null 2>&1 && log "  type1 warmup done." || log "  type1 warmup skipped."
    fi
    log "Warming type2 (physics group)..."
    curl -s -m 120 "http://127.0.0.1:$API_PORT/predict" -H 'Content-Type: application/json' \
      -d '{"query_id":"warmup2","type":"type2","query":"What is the energy stored in a 2 uF capacitor charged to 12 V, in joules?","premises":[],"options":[]}' \
      >/dev/null 2>&1 && log "  type2 warmup done." || log "  type2 warmup skipped."
fi

echo; log "=== STACK UP (mode=$SERVE_MODE) ==="; status_all
echo; log "Test from laptop:  ssh -p <PORT> root@<HOST> -L $API_PORT:localhost:$API_PORT  then http://localhost:$API_PORT/docs"

# ---------------------------------------------------------------------------
# optional public tunnel(s) for BTC
#   BTC §3 wants the prediction URL + EVERY vLLM /v1/models URL (one per server) in
#   urls.txt. combined/triple -> 1 gateway tunnel (/predict) + one per vLLM engine
#   (/v1/models, vLLM auto-exposes it). Else -> single gateway tunnel.
# ---------------------------------------------------------------------------
if [ "${SKIP_TUNNEL:-1}" = "1" ]; then log "SKIP_TUNNEL=1 — no public tunnel."; exit 0; fi
command -v cloudflared >/dev/null 2>&1 || { err "cloudflared not installed; skipping tunnel."; exit 0; }

# Start a quick tunnel to a local port; print its public URL (waits for it to REGISTER,
# since trycloudflare prints the hostname before the edge connection is live).
start_tunnel() {  # logname localport -> echoes URL
    # NOTE: split across two `local` statements — a single `local name=$1 lg=..$name..`
    # expands $name before it's assigned, which dies under `set -u` (empty URLs).
    local name="$1" port="$2"
    local lg="$LOG_DIR/cf_$name.log"
    local old; old="$(cat "$RUN_DIR/cf_$name.pid" 2>/dev/null || true)"
    [ -n "$old" ] && kill "$old" 2>/dev/null
    : > "$lg"
    setsid cloudflared tunnel --url "http://localhost:$port" --no-autoupdate >"$lg" 2>&1 </dev/null &
    echo $! > "$RUN_DIR/cf_$name.pid"; disown 2>/dev/null || true
    local url=""
    for _ in $(seq 1 30); do
        url="$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$lg" | head -1)"
        [ -n "$url" ] && grep -q "Registered tunnel connection" "$lg" && break
        sleep 2
    done
    echo "$url"
}

SUB_DIR="$PROJECT_ROOT/submission"; mkdir -p "$SUB_DIR"
if [ "$SERVE_MODE" = "combined" ]; then
    # 2 vLLM engines now: :18000 (base+sft+qa) + :18001 (fol). qa is a LoRA on :18000.
    GW="$(start_tunnel gateway "$API_PORT")"
    U0="$(start_tunnel vllm0 "$VLLM_PORT")"
    U1="$(start_tunnel vllm1 "$FOL_PORT")"
    {
        echo "# EXACT 2026 — endpoint URLs (BTC §3). trycloudflare URLs change per restart."
        echo "# One GPU; sleep-swap keeps <=8B GPU-resident at any moment (type2: base 4B; type1: base+fol 8B)."
        echo "$GW/predict"
        echo "$U0/v1/models   # :$VLLM_PORT base + sft(physics) + qa(logic stage 2) LoRA adapters"
        echo "$U1/v1/models   # :$FOL_PORT fol (logic stage 1)"
    } > "$SUB_DIR/urls.txt"
    log "=== PUBLIC URLs (BTC) written to $SUB_DIR/urls.txt ==="; cat "$SUB_DIR/urls.txt"
    [ -n "$GW$U0$U1" ] || err "some tunnels empty (shared-IP rate limit) — re-run or use a named tunnel/VPS."
elif [ "$SERVE_MODE" = "triple" ]; then
    GW="$(start_tunnel gateway "$API_PORT")"
    U0="$(start_tunnel vllm0 "$VLLM_PORT")"
    U1="$(start_tunnel vllm1 "$FOL_PORT")"
    U2="$(start_tunnel vllm2 "$QA_PORT")"
    {
        echo "# EXACT 2026 — endpoint URLs (BTC §3). trycloudflare URLs change per restart."
        echo "# One GPU; sleep-swap by type keeps <=8B GPU-resident at any moment."
        echo "$GW/predict"
        echo "$U0/v1/models   # :$VLLM_PORT base+sft (physics)"
        echo "$U1/v1/models   # :$FOL_PORT fol (logic stage 1)"
        echo "$U2/v1/models   # :$QA_PORT qa (logic stage 2)"
    } > "$SUB_DIR/urls.txt"
    log "=== PUBLIC URLs (BTC) written to $SUB_DIR/urls.txt ==="; cat "$SUB_DIR/urls.txt"
    [ -n "$GW$U0$U1$U2" ] || err "some tunnels empty (shared-IP rate limit) — re-run or use a named tunnel/VPS."
else
    URL="$(start_tunnel gateway "$API_PORT")"
    { echo "$URL/predict"; echo "$URL/v1/models   # gateway proxy (aggregates engines)"; } > "$SUB_DIR/urls.txt"
    [ -n "$URL" ] && log "=== PUBLIC ENDPOINT (give BTC) ===  $URL/predict  (urls.txt written)" \
                  || err "No tunnel URL yet (shared-IP rate limit?). Fallback: reverse-SSH :$API_PORT to your VPS."
fi
exit 0
