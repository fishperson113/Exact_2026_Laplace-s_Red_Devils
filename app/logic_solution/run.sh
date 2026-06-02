#!/usr/bin/env bash
# ==============================================================================
# logic_solution/run.sh
# Ensemble inference: Type 1 input → answer + explanation + fol
# ==============================================================================
# Usage:
#   bash run.sh --input data/sample_input.json
#   bash run.sh --input data/sample_input.json --output outputs/results.json
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${SCRIPT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${SCRIPT_DIR}/requirements.txt"

# ── Parse args để forward sang run.py ─────────────────────────────────────────
INPUT_ARG=""
OUTPUT_ARG=""
CONFIG_ARG=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --input)  INPUT_ARG="--input $2";  shift 2 ;;
        --output) OUTPUT_ARG="--output $2"; shift 2 ;;
        --config) CONFIG_ARG="--config $2"; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "${INPUT_ARG}" ]]; then
    echo "Usage: bash run.sh --input <path_to_input.json> [--output <path>] [--config <path>]"
    exit 1
fi

echo "=============================================="
echo "  Logic Solution — Ensemble Inference"
echo "=============================================="
echo "Script dir : ${SCRIPT_DIR}"
echo ""

# ==============================================================================
# Step 1: Kiểm tra uv
# ==============================================================================
echo "[1/4] Kiểm tra uv..."
if ! command -v uv &> /dev/null; then
    echo "  uv chưa cài. Đang cài..."
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
echo "[2/4] Virtual environment: ${VENV_NAME}..."
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
echo "[3/4] Cài dependencies từ requirements.txt..."
uv pip install -r "${REQUIREMENTS}"
echo "  Done."

# ==============================================================================
# Step 4: Kiểm tra GPU + chạy inference
# ==============================================================================
echo ""
echo "[4/4] Kiểm tra môi trường..."
python -c "
import torch, transformers, peft, bitsandbytes
print(f'  PyTorch      : {torch.__version__}')
print(f'  CUDA         : {torch.cuda.is_available()} — {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')
print(f'  Transformers : {transformers.__version__}')
print(f'  PEFT         : {peft.__version__}')
print(f'  BnB          : {bitsandbytes.__version__}')
"

echo ""
echo "=============================================="
echo "  Running inference..."
echo "=============================================="
echo ""

cd "${SCRIPT_DIR}"
python run.py ${INPUT_ARG} ${OUTPUT_ARG} ${CONFIG_ARG}

echo ""
echo "=============================================="
echo "  DONE"
echo "=============================================="
