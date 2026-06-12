#!/bin/bash
# =============================================================================
# setup_env.sh — ONE-SHOT bootstrap for the EXACT-2026 serving stack on a fresh
# Vast.ai "NVIDIA CUDA Development Environment" instance (CUDA-13 driver, >=580).
#
# Designed to be called from Vast's **On-start Script** via a raw GitHub URL:
#
#     curl -fsSL -o setup_env.sh \
#       https://raw.githubusercontent.com/fishperson113/Exact_2026_Laplace-s_Red_Devils/Nguyen/Final/setup_env.sh
#     chmod +x setup_env.sh && bash setup_env.sh
#
# What it does (idempotent — safe to re-run):
#   1. install vLLM (latest, CUDA-13) + gateway/code-exec deps into /venv/main
#      (via `uv` — resilient on flaky links; falls back to pip)
#   2. git clone/pull this repo to /workspace/project
#   3. launch the FULL competition stack (SERVE_MODE=combined): physics base+LoRA
#      (:18000) + logic fol/qa grafted-composite (:18001/:18002), FastAPI gateway
#      (:9000, POST /predict), one cloudflared tunnel per service + urls.txt (BTC §3)
#
# vLLM has its OWN GDN / causal-conv1d kernels, so serving Qwen3.5-4B needs NO
# `fla` / `causal-conv1d` / transformers spells (those are only for finetuning).
#
# REQUIRED env (set these in the Vast template's "Environment Variables"):
#   HF_TOKEN=hf_xxx        # to download the gated Qwen3.5-4B repo
# Optional env (sensible defaults):
#   REPO_URL, REPO_BRANCH, PROJECT_DIR, VENV, SERVE_MODEL, SKIP_TUNNEL=0
# =============================================================================
set -uo pipefail

REPO_URL="${REPO_URL:-https://github.com/fishperson113/Exact_2026_Laplace-s_Red_Devils.git}"
REPO_BRANCH="${REPO_BRANCH:-Nguyen/Final}"
PROJECT_DIR="${PROJECT_DIR:-/workspace/project}"
VENV="${VENV:-/venv/main}"
PY="$VENV/bin/python"

log() { echo -e "\033[0;36m[setup_env]\033[0m $*"; }
err() { echo -e "\033[0;31m[setup_env] ERROR:\033[0m $*" >&2; }

export TMPDIR="${TMPDIR:-/workspace/tmp}"; mkdir -p "$TMPDIR"

# --- HF token: prefer env (Vast var); else an already-staged secret.env ---
if [ -z "${HF_TOKEN:-}" ] && [ -f /workspace/secret.env ]; then
    HF_TOKEN="$(grep -E '^HF_TOKEN_CC=' /workspace/secret.env | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')"
fi
export HF_TOKEN="${HF_TOKEN:-}" HUGGING_FACE_HUB_TOKEN="${HF_TOKEN:-}"
[ -n "$HF_TOKEN" ] && log "HF token present." || err "HF_TOKEN not set — gated model download will 401. Set it in Vast env vars."

# ---------------------------------------------------------------------------
# 1. Python deps into the template venv (idempotent)
# ---------------------------------------------------------------------------
PKGS=(vllm hf_transfer fastapi "uvicorn[standard]" "openai>=1.0" \
      pydantic pydantic-settings httpx numpy scipy sympy pandas)

if "$PY" -c "import vllm, fastapi, scipy" 2>/dev/null; then
    log "vLLM + deps already installed — skipping."
else
    log "Installing vLLM (CUDA-13) + gateway/code-exec deps ..."
    export UV_HTTP_TIMEOUT=300 UV_CACHE_DIR=/workspace/uv-cache
    mkdir -p "$UV_CACHE_DIR"
    ok=0
    if command -v uv >/dev/null 2>&1; then
        for attempt in 1 2 3; do
            log "  uv attempt $attempt ..."
            uv pip install --python "$PY" "${PKGS[@]}" && { ok=1; break; }
            sleep 5
        done
    fi
    if [ "$ok" != "1" ]; then
        log "  falling back to pip (retries) ..."
        "$VENV/bin/pip" install --no-cache-dir --retries 10 --timeout 300 "${PKGS[@]}" && ok=1
    fi
    [ "$ok" = "1" ] || { err "dependency install failed (network?). Re-run setup_env.sh."; exit 1; }
fi

# Sanity: torch must see the GPU on this driver (CUDA-13 needs driver >=580).
if ! "$PY" -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
    err "torch installed but CUDA unavailable — the box driver is too old for this vLLM (need CUDA 13 / driver >=580)."
    "$PY" -c "import torch;print('torch',torch.__version__)" 2>/dev/null || true
    exit 1
fi
log "torch <-> CUDA OK: $("$PY" -c 'import torch;print(torch.__version__, torch.cuda.get_device_name(0))' 2>/dev/null)"

# ---------------------------------------------------------------------------
# 2. Get the code
# ---------------------------------------------------------------------------
if [ -d "$PROJECT_DIR/.git" ]; then
    log "Updating repo at $PROJECT_DIR ($REPO_BRANCH) ..."
    git -C "$PROJECT_DIR" fetch --depth 1 origin "$REPO_BRANCH" \
        && git -C "$PROJECT_DIR" checkout -f "$REPO_BRANCH" 2>/dev/null \
        && git -C "$PROJECT_DIR" reset --hard "origin/$REPO_BRANCH" \
        || err "git update failed; using existing checkout."
else
    log "Cloning $REPO_URL ($REPO_BRANCH) -> $PROJECT_DIR ..."
    git clone --depth 1 --branch "$REPO_BRANCH" "$REPO_URL" "$PROJECT_DIR" \
        || { err "git clone failed (repo public? branch exists?)."; exit 1; }
fi

# ---------------------------------------------------------------------------
# 3. Install cloudflared (for the public BTC URL) if missing, then serve.
# ---------------------------------------------------------------------------
if ! command -v cloudflared >/dev/null 2>&1; then
    log "Installing cloudflared ..."
    curl -fsSL -o /usr/local/bin/cloudflared \
        https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 \
        && chmod +x /usr/local/bin/cloudflared || err "cloudflared install failed (tunnel optional)."
fi

log "Launching the serving stack (SERVE_MODE=${SERVE_MODE:-combined}) ..."
PROJECT_ROOT="$PROJECT_DIR" VENV="$VENV" SKIP_TUNNEL="${SKIP_TUNNEL:-0}" \
    SERVE_MODE="${SERVE_MODE:-combined}" HF_TOKEN="${HF_TOKEN:-}" \
    bash "$PROJECT_DIR/scripts/serve_all.sh" start

log "Done. Logs in /workspace/logs/. Public /ask URL printed above (if tunnel started)."
