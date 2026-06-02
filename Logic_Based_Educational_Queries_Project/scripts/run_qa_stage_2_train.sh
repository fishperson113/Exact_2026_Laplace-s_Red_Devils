#!/usr/bin/env bash
# ==============================================================================
# QA Stage 2 Training Pipeline — Setup & Run
# ==============================================================================
# Train → Merge → Push best model lên HF Hub.
#
# Cách dùng:
#   chmod +x scripts/run_qa_stage_2_train.sh
#   bash scripts/run_qa_stage_2_train.sh
#
# Debug nhanh (không push):
#   bash scripts/run_qa_stage_2_train.sh --debug 10
#
# Trong tmux:
#   tmux new -s qa_train
#   cd Logic_Based_Educational_Queries_Project/
#   bash scripts/run_qa_stage_2_train.sh
# ==============================================================================

set -euo pipefail

# --- Config ---
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${PROJECT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${PROJECT_DIR}/requirements.txt"
QA_CONFIG="${PROJECT_DIR}/configs/qa_model.yaml"

# Parse args
DEBUG_SAMPLES=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --debug)
            DEBUG_SAMPLES="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

echo "=============================================="
echo "  QA Stage 2 (COT) Training Pipeline"
echo "=============================================="
echo "Project dir : ${PROJECT_DIR}"
echo "Config      : ${QA_CONFIG}"
if [ -n "${DEBUG_SAMPLES}" ]; then
    echo "Mode        : DEBUG (${DEBUG_SAMPLES} samples, no push)"
else
    echo "Mode        : FULL (train → merge → push)"
fi
echo ""

# ==============================================================================
# Step 1: Kiểm tra uv
# ==============================================================================
echo "[1/7] Kiểm tra uv..."
if ! command -v uv &> /dev/null; then
    echo "  uv chưa cài. Đang cài uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    echo "  uv đã cài xong."
else
    echo "  uv đã có: $(uv --version)"
fi

# ==============================================================================
# Step 2: Tạo venv
# ==============================================================================
echo ""
echo "[2/7] Virtual environment: ${VENV_NAME}..."
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
echo "[3/7] Cài dependencies..."
uv pip install -r "${REQUIREMENTS}"
echo "  Done."

# ==============================================================================
# Step 4: Cài project editable
# ==============================================================================
echo ""
echo "[4/7] Cài project (editable)..."
uv pip install -e "${PROJECT_DIR}"
echo "  Done."

# ==============================================================================
# Step 5: Kiểm tra imports
# ==============================================================================
echo ""
echo "[5/7] Kiểm tra imports..."
python -c "
import torch, transformers, trl, peft, datasets
print(f'  PyTorch      : {torch.__version__}')
print(f'  CUDA         : {torch.cuda.is_available()} — {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')
print(f'  Transformers : {transformers.__version__}')
print(f'  TRL          : {trl.__version__}')
print(f'  PEFT         : {peft.__version__}')
"

# ==============================================================================
# Step 6: Prepare data
# ==============================================================================
echo ""
echo "[6/7] Preparing QA COT dataset..."
cd "${PROJECT_DIR}/src"
PYTHONPATH=. python -m models.QA_model.prepare_data --config "${QA_CONFIG}"

# ==============================================================================
# Step 7: Train + Merge + Push
# ==============================================================================
echo ""
echo "=============================================="
echo "[7/7] Training QA Stage 2..."
echo "=============================================="

if [ -n "${DEBUG_SAMPLES}" ]; then
    # Debug: train only, no merge, no push
    PYTHONPATH=. python -m models.QA_model.train --config "${QA_CONFIG}" --debug-samples "${DEBUG_SAMPLES}"
else
    # Full: train → merge → push
    PYTHONPATH=. python -m models.QA_model.train --config "${QA_CONFIG}" --merge
fi

echo ""
echo "=============================================="
echo "  QA Stage 2 DONE"
echo "=============================================="
