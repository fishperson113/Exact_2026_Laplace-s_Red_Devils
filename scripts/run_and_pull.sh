#!/usr/bin/env bash
# run_and_pull.sh — Run inference on GPU server and pull results back.
#
# Usage:
#   bash scripts/run_and_pull.sh <HOST> <PORT> [LIMIT]
#
# Examples:
#   bash scripts/run_and_pull.sh 77.48.24.239 43789 10    # smoke test
#   bash scripts/run_and_pull.sh 77.48.24.239 43789        # full golden run
set -euo pipefail

HOST="${1:?Usage: $0 <HOST> <PORT> [LIMIT]}"
PORT="${2:?Usage: $0 <HOST> <PORT> [LIMIT]}"
LIMIT="${3:-0}"

SSH_TARGET="root@${HOST}"
REMOTE_PROJECT="/root/project"
TEST_FILE="app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv"
OUT="app/physics_solution/versions/v05_code_execution/output/results_golden.json"

INFER_CMD="cd ${REMOTE_PROJECT} && source ${REMOTE_PROJECT}/.venv/bin/activate && python -m app.physics_solution.cli.inference --version v05_code_execution --test-file ${TEST_FILE} --out ${OUT}"
if [ "$LIMIT" -gt 0 ] 2>/dev/null; then
    INFER_CMD="${INFER_CMD} --limit ${LIMIT}"
fi

echo ""
echo "=== Running inference on ${SSH_TARGET} (port ${PORT}) ==="
echo "Command: ${INFER_CMD}"
echo ""

ssh -p "${PORT}" -o StrictHostKeyChecking=no "${SSH_TARGET}" "${INFER_CMD}"

echo ""
echo "=== Inference complete. Pulling results... ==="

LOCAL_OUT_DIR="app/physics_solution/versions/v05_code_execution/output"
mkdir -p "${LOCAL_OUT_DIR}"

REMOTE_BASE="${REMOTE_PROJECT}/${OUT%.json}"
scp -P "${PORT}" -o StrictHostKeyChecking=no "${SSH_TARGET}:${REMOTE_BASE}.json" "${LOCAL_OUT_DIR}/"
scp -P "${PORT}" -o StrictHostKeyChecking=no "${SSH_TARGET}:${REMOTE_BASE}.csv" "${LOCAL_OUT_DIR}/"

echo ""
echo "=== Results pulled to ${LOCAL_OUT_DIR} ==="
ls -lh "${LOCAL_OUT_DIR}/"
