#!/usr/bin/env bash
# ==============================================================================
# FOL Training Pipeline — Setup & Run
# ==============================================================================
# Tạo venv logic_env (Python 3.12), cài dependencies qua uv, chạy FOL training.
#
# Cách dùng:
#   chmod +x scripts/run_fol_train.sh
#   bash scripts/run_fol_train.sh
#
# Hoặc chạy trong tmux:
#   tmux set -g mouse on
#   tmux new -s train
#   cd Logic_Based_Educational_Queries_Project/
# cd /home/
# rm -rf /home/*
# git clone https://{token}@github.com/fishperson113/Exact_2026_Laplace-s_Red_Devils.git .
# git config --global user.email "thaisoncbq@gmail.com"
# git config --global user.email "{name}"
# git checkout Son/Logic_Based_Educational_Queries
#   bash scripts/run_fol_train.sh
# ==============================================================================

set -euo pipefail

# --- Config ---
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_NAME="logic_env"
VENV_DIR="${PROJECT_DIR}/${VENV_NAME}"
PYTHON_VERSION="3.12"
REQUIREMENTS="${PROJECT_DIR}/requirements.txt"

echo "=============================================="
echo "  FOL Training Pipeline Setup"
echo "=============================================="
echo "Project dir : ${PROJECT_DIR}"
echo "Venv        : ${VENV_DIR}"
echo "Python      : ${PYTHON_VERSION}"
echo ""

# ==============================================================================
# Step 1: Kiểm tra uv
# ==============================================================================
echo "[1/6] Kiểm tra uv..."
if ! command -v uv &> /dev/null; then
    echo "  uv chưa cài. Đang cài uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    echo "  ✅ uv đã cài xong."
else
    echo "  ✅ uv đã có: $(uv --version)"
fi

# ==============================================================================
# Step 2: Tạo venv logic_env với Python 3.12
# ==============================================================================
echo ""
echo "[2/6] Tạo virtual environment: ${VENV_NAME} (Python ${PYTHON_VERSION})..."
if [ -d "${VENV_DIR}" ]; then
    echo "  ⚠️  ${VENV_NAME} đã tồn tại. Dùng lại."
else
    uv venv "${VENV_DIR}" --python "${PYTHON_VERSION}"
    echo "  ✅ Đã tạo ${VENV_NAME}."
fi

# Activate venv
source "${VENV_DIR}/bin/activate"
echo "  Python: $(python --version) — $(which python)"

# ==============================================================================
# Step 3: Cài dependencies qua uv
# ==============================================================================
echo ""
echo "[3/6] Cài dependencies từ requirements.txt (pinned versions)..."
uv pip install -r "${REQUIREMENTS}"
echo "  ✅ Dependencies đã cài xong."

# ==============================================================================
# Step 4: Cài project ở chế độ editable
# ==============================================================================
echo ""
echo "[4/6] Cài project (editable mode)..."
uv pip install -e "${PROJECT_DIR}"
echo "  ✅ Project đã cài."

# ==============================================================================
# Step 5: Kiểm tra imports quan trọng
# ==============================================================================
echo ""
echo "[5/6] Kiểm tra imports..."

python -c "
import torch
import transformers
import trl
import peft
import z3

print(f'  PyTorch     : {torch.__version__}')
print(f'  CUDA        : {torch.cuda.is_available()} — {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')
print(f'  Transformers: {transformers.__version__}')
print(f'  TRL         : {trl.__version__}')
print(f'  PEFT        : {peft.__version__}')
print(f'  Z3          : {z3.get_version_string()}')
print('  ✅ Tất cả imports OK.')
"

# Kiểm tra Unsloth (optional, có thể fail trên một số setup)
python -c "
try:
    import unsloth
    print(f'  Unsloth     : {unsloth.__version__}')
except ImportError:
    print('  ⚠️  Unsloth chưa cài được — train vẫn chạy nhưng tốn VRAM hơn.')
"

# ==============================================================================
# Step 6: Chạy FOL training
# ==============================================================================
echo ""
echo "=============================================="
echo "[6/6] Bắt đầu FOL training..."
echo "=============================================="
echo ""

cd "${PROJECT_DIR}/src"
PYTHONPATH=. python -m models.fol_model.train
