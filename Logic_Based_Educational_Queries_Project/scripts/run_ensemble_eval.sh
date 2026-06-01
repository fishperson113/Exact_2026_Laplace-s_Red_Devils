#!/usr/bin/env bash
# ==============================================================================
# Ensemble Evaluate: FOL Model + QA Model → test accuracy
# ==============================================================================
# Usage:
#   bash scripts/run_ensemble_eval.sh
# ==============================================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="${PROJECT_DIR}/logic_env"
CONFIG="${PROJECT_DIR}/configs/ensemble_model.yaml"

echo "=============================================="
echo "  Ensemble Model Evaluate"
echo "=============================================="

# Activate venv (đã cài đủ dependencies từ training)
if [ -d "${VENV_DIR}" ]; then
    source "${VENV_DIR}/bin/activate"
    echo "  Venv: ${VENV_DIR}"
else
    echo "  Venv not found. Installing dependencies..."
    pip install -q peft transformers datasets torch pandas pyyaml
fi

echo "  Python: $(python --version)"
echo "  Config: ${CONFIG}"
echo ""

cd "${PROJECT_DIR}/src"
PYTHONPATH=. python -m models.Ensemble_Model.inference --config "${CONFIG}" --mode evaluate

echo ""
echo "=============================================="
echo "  Ensemble Evaluate DONE"
echo "=============================================="
