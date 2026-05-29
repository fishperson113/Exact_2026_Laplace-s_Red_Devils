#!/usr/bin/env bash
# ==============================================================================
# FOL_Z3 Pipeline — Setup & Inference
# ==============================================================================
# Cai moi truong + chay pipeline FOL_Z3 tren test set:
#   FOL Model → Z3 Solver → QA Model → JSON {answer, explanation}
#
# Cach dung:
#   chmod +x scripts/run_fol_z3_inference.sh
#   bash scripts/run_fol_z3_inference.sh
#
# Tuy chon:
#   USE_FOL=false bash scripts/run_fol_z3_inference.sh   # baseline (khong FOL/Z3)
#   CONFIG=configs/fol_z3.yaml bash scripts/run_fol_z3_inference.sh
#
# Trong tmux:
#   tmux new -s infer
#   bash scripts/run_fol_z3_inference.sh
# ==============================================================================

set -euo pipefail

# --- Config ---
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${PROJECT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${PROJECT_DIR}/requirements.txt"
CONFIG="${CONFIG:-configs/fol_z3.yaml}"

echo "=============================================="
echo "  FOL_Z3 Pipeline — Setup & Inference"
echo "=============================================="
echo "Project dir : ${PROJECT_DIR}"
echo "Config      : ${CONFIG}"
echo "USE_FOL     : ${USE_FOL:-true}"
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
# Step 2: Tao / reuse venv
# ==============================================================================
echo ""
echo "[2/5] Virtual environment: ${VENV_NAME}..."
if [ -d "${VENV_DIR}" ]; then
    echo "  ${VENV_NAME} da ton tai. Dung lai."
else
    uv venv "${VENV_DIR}" --python "${PYTHON_VERSION}"
    echo "  Da tao ${VENV_NAME}."
fi

source "${VENV_DIR}/bin/activate"
echo "  Python: $(python --version) — $(which python)"

# ==============================================================================
# Step 3: Cai dependencies
# ==============================================================================
echo ""
echo "[3/5] Cai dependencies..."
uv pip install -r "${REQUIREMENTS}"
uv pip install -e "${PROJECT_DIR}"
echo "  Dependencies da cai xong."

# ==============================================================================
# Step 4: Kiem tra imports
# ==============================================================================
echo ""
echo "[4/5] Kiem tra imports..."

python -c "
import torch
import transformers
import z3

print(f'  PyTorch     : {torch.__version__}')
print(f'  CUDA        : {torch.cuda.is_available()}', end='')
if torch.cuda.is_available():
    print(f' — {torch.cuda.get_device_name(0)}')
else:
    print(' — CPU mode')
print(f'  Transformers: {transformers.__version__}')
print(f'  Z3          : {z3.get_version_string()}')
print('  Imports OK.')
"

# ==============================================================================
# Step 5: Chay FOL_Z3 pipeline inference
# ==============================================================================
echo ""
echo "=============================================="
echo "[5/5] Chay FOL_Z3 inference..."
echo "=============================================="
echo ""

cd "${PROJECT_DIR}/src"

# Truyen USE_FOL qua env neu co
if [ -n "${USE_FOL:-}" ]; then
    export FOL_Z3_USE_FOL="${USE_FOL}"
fi

PYTHONPATH=. python -m models.FOL_Z3.run_inference --config "${PROJECT_DIR}/${CONFIG}"
