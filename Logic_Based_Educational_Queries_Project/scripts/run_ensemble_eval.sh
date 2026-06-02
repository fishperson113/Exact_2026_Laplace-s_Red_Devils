#!/usr/bin/env bash
# ==============================================================================
# Ensemble Evaluate: FOL Model + QA Model → test accuracy
# ==============================================================================
# Usage:
#   bash scripts/run_ensemble_eval.sh
# ==============================================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${PROJECT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${PROJECT_DIR}/requirements.txt"
CONFIG="${PROJECT_DIR}/configs/ensemble_model.yaml"

echo "=============================================="
echo "  Ensemble Model Evaluate"
echo "=============================================="
echo "Project dir : ${PROJECT_DIR}"
echo ""

# ==============================================================================
# Step 1: Kiểm tra uv
# ==============================================================================
echo "[1/5] Kiểm tra uv..."
if ! command -v uv &> /dev/null; then
    echo "  uv chưa cài. Đang cài uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    echo "  uv đã cài xong."
else
    echo "  uv đã có: $(uv --version)"
fi

# ==============================================================================
# Step 2: Tạo / reuse venv
# ==============================================================================
echo ""
echo "[2/5] Virtual environment: ${VENV_NAME}..."
if [ -d "${VENV_DIR}" ]; then
    echo "  ${VENV_NAME} đã tồn tại. Dùng lại."
else
    uv venv "${VENV_DIR}" --python "${PYTHON_VERSION}"
    echo "  Đã tạo ${VENV_NAME}."
fi
source "${VENV_DIR}/bin/activate"
echo "  Python: $(python --version)"

# ==============================================================================
# Step 3: Cài dependencies
# ==============================================================================
echo ""
echo "[3/5] Cài dependencies..."
uv pip install -r "${REQUIREMENTS}"
echo "  Done."

# ==============================================================================
# Step 4: Cài project editable
# ==============================================================================
echo ""
echo "[4/5] Cài project (editable)..."
uv pip install -e "${PROJECT_DIR}"
echo "  Done."

# ==============================================================================
# Step 5: Kiểm tra imports + Run
# ==============================================================================
echo ""
echo "[5/5] Kiểm tra imports..."
python -c "
import torch, transformers, peft, datasets, bitsandbytes, pandas, huggingface_hub
print(f'  PyTorch      : {torch.__version__}')
print(f'  CUDA         : {torch.cuda.is_available()} — {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')
print(f'  Transformers : {transformers.__version__}')
print(f'  PEFT         : {peft.__version__}')
print(f'  BnB          : {bitsandbytes.__version__}')
"

echo ""
echo "=============================================="
echo "  Running Ensemble Evaluate..."
echo "=============================================="
echo ""

cd "${PROJECT_DIR}/src"
PYTHONPATH=. python -m models.Ensemble_Model.inference --config "${CONFIG}" --mode evaluate

echo ""
echo "=============================================="
echo "  Ensemble Evaluate DONE"
echo "=============================================="
