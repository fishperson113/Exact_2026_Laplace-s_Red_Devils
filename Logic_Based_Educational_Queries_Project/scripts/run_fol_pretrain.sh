#!/usr/bin/env bash
# ==============================================================================
# Stage 1: Pretrain FOL model tren MALLS dataset
# ==============================================================================
# Train LoRA tren MALLS (28K mau, 3 epochs), merge + push len Hub.
# Sau do chuyen sang Stage 2: bash scripts/run_fol_train.sh
#
# Cach chay:
#   chmod +x scripts/run_fol_pretrain.sh
#   bash scripts/run_fol_pretrain.sh
#
# Trong tmux:
#   tmux new -s pretrain
#   bash scripts/run_fol_pretrain.sh
# ==============================================================================

set -euo pipefail

# --- Config ---
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${PROJECT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${PROJECT_DIR}/requirements.txt"

echo "=============================================="
echo "  Stage 1: FOL Pretrain (MALLS)"
echo "=============================================="
echo "Project dir : ${PROJECT_DIR}"
echo "Venv        : ${VENV_DIR}"
echo ""

# ==============================================================================
# Step 1: Kiem tra uv
# ==============================================================================
echo "[1/5] Kiem tra uv..."
if ! command -v uv &> /dev/null; then
    echo "  uv chua cai. Dang cai uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    echo "  uv da cai xong."
else
    echo "  uv da co: $(uv --version)"
fi

# ==============================================================================
# Step 2: Tao venv
# ==============================================================================
echo ""
echo "[2/5] Tao virtual environment: ${VENV_NAME} (Python ${PYTHON_VERSION})..."
if [ -d "${VENV_DIR}" ]; then
    echo "  ${VENV_NAME} da ton tai. Dung lai."
else
    uv venv "${VENV_DIR}" --python "${PYTHON_VERSION}"
    echo "  Da tao ${VENV_NAME}."
fi

source "${VENV_DIR}/bin/activate"
echo "  Python: $(python --version) — $(which python)"

# ==============================================================================
# Step 3: Cai dependencies (skip neu da cai)
# ==============================================================================
echo ""
MARKER="${VENV_DIR}/.deps_installed"
if [ "${SKIP_INSTALL:-}" = "1" ] || [ -f "${MARKER}" ]; then
    echo "[3/5] Dependencies da cai truoc do — skip."
else
    echo "[3/5] Cai dependencies tu requirements.txt..."
    uv pip install -r "${REQUIREMENTS}"
    uv pip install -e "${PROJECT_DIR}"
    touch "${MARKER}"
    echo "  Dependencies da cai xong."
fi

# ==============================================================================
# Step 4: Kiem tra imports
# ==============================================================================
echo ""
echo "[4/5] Kiem tra imports..."
python -c "
import torch
import transformers
import trl
import peft

print(f'  PyTorch     : {torch.__version__}')
print(f'  CUDA        : {torch.cuda.is_available()} — {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')
print(f'  Transformers: {transformers.__version__}')
print(f'  TRL         : {trl.__version__}')
print(f'  PEFT        : {peft.__version__}')
print('  Imports OK.')
"

# ==============================================================================
# Step 5: Chay pretrain
# ==============================================================================
echo ""
echo "=============================================="
echo "[5/5] Bat dau Stage 1 Pretrain (MALLS)..."
echo "=============================================="
echo ""

cd "${PROJECT_DIR}/src"
PYTHONPATH=. python -m models.fol_model.pretrain

echo ""
echo "=============================================="
echo "  Stage 1 DONE"
echo "=============================================="
echo ""
echo "Buoc tiep theo:"
echo "  1. Sua configs/fol_model.yaml > model.name thanh repo pretrain (xem log ben tren)"
echo "  2. Chay Stage 2: bash scripts/run_fol_train.sh"
echo ""
