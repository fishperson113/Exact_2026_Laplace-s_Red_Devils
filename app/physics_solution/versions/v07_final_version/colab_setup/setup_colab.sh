#!/usr/bin/env bash
# ==============================================================================
# v07 SFT — Colab environment setup (SSH into the Colab box, cd /content first)
# ==============================================================================
# Reproduces the PROVEN Qwen3.5-4B Unsloth stack (same pins the FOL model trained
# with: torch 2.10 + transformers 5.5 + unsloth 2026.5.6). We install into an
# isolated uv venv so we never clobber Colab's system jupyter/kernel; training is
# then invoked with $VENV/bin/python (works fine from a notebook via `!`).
#
# fla / causal-conv1d are NOT in the pinned set — the FOL model trained without
# them (Unsloth/tf5 uses a torch fallback). We install them best-effort only for
# speed; failure is harmless.
#
# Usage (from /content, after the LD_LIBRARY_PATH lines below):
#   bash colab_setup/setup_colab.sh
# ==============================================================================
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-/content/Exact_2026_Laplace-s_Red_Devils}"
VENV_DIR="${VENV_DIR:-/content/v07_env}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQ="${HERE}/requirements.txt"

echo "=============================================="
echo "  v07 SFT — Colab setup"
echo "  repo : ${REPO_ROOT}"
echo "  venv : ${VENV_DIR}"
echo "=============================================="

# --- 0. CUDA libs on PATH (Colab needs this for nvidia-smi / torch CUDA) -------
# These also belong in ~/.bashrc (run once); harmless to re-export here.
export LD_LIBRARY_PATH=/usr/lib64-nvidia:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH:-}
export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
echo "[0/4] nvidia-smi:"; nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv || true

# --- 1. uv ---------------------------------------------------------------------
echo "[1/4] uv ..."
if ! command -v uv &>/dev/null; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
echo "  uv: $(uv --version)"

# --- 2. venv + pinned deps -----------------------------------------------------
echo "[2/4] venv + pinned requirements (this is the long step) ..."
if [ ! -d "${VENV_DIR}" ]; then
  uv venv "${VENV_DIR}" --python 3.12
fi
# hf_transfer speeds up the ~8GB base-model download.
VENV_PY="${VENV_DIR}/bin/python"
uv pip install --python "${VENV_PY}" -r "${REQ}"
echo "  ✅ pinned deps installed."

# --- 3. fast kernels (OPTIONAL — speed only; torch fallback works without) -----
echo "[3/4] flash-linear-attention + causal-conv1d (best-effort) ..."
uv pip install --python "${VENV_PY}" flash-linear-attention 2>/dev/null \
  && echo "  fla: OK" || echo "  fla: skipped (torch fallback)"
# causal-conv1d: pre-built wheel matched to torch2.10 / cu12 / cp312 if one exists.
CC_OK=0
for V in 1.5.2 1.5.0.post8; do for ABI in FALSE TRUE; do
  URL="https://github.com/Dao-AILab/causal-conv1d/releases/download/v${V}/causal_conv1d-${V}+cu12torch2.10cxx11abi${ABI}-cp312-cp312-linux_x86_64.whl"
  if uv pip install --python "${VENV_PY}" "${URL}" 2>/dev/null; then
    echo "  causal-conv1d: OK (v${V} abi=${ABI})"; CC_OK=1; break; fi
done; [ $CC_OK -eq 1 ] && break; done
[ $CC_OK -eq 0 ] && echo "  causal-conv1d: no matching wheel (torch fallback — fine)."

# --- 4. import sanity ----------------------------------------------------------
echo "[4/4] import sanity ..."
"${VENV_PY}" - <<'PY'
import unsloth  # import FIRST (patches trl/transformers) — must precede trl
import torch, transformers, trl, peft, accelerate, bitsandbytes, datasets
print("  torch       :", torch.__version__, "cuda", torch.cuda.is_available())
print("  transformers:", transformers.__version__)
print("  trl/peft    :", trl.__version__, "/", peft.__version__)
print("  unsloth     :", unsloth.__version__)
from transformers.models.auto.configuration_auto import CONFIG_MAPPING_NAMES as C
print("  qwen3_5 supported:", "qwen3_5" in C)
PY
echo "✅ setup_colab.sh done. Train with: ${VENV_PY} -m ..."
