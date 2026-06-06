#!/bin/bash
# =============================================================================
# deploy_vast.sh — (run on your LAPTOP) rsync code to a Vast.ai box and bring
# up the full serving stack via serve_all.sh.
#
# Usage:
#     bash scripts/deploy_vast.sh <HOST> <PORT> [SSH_KEY] [REMOTE_ROOT]
#
# Examples:
#     bash scripts/deploy_vast.sh 212.13.234.23 12527
#     bash scripts/deploy_vast.sh 212.13.234.23 12527 ~/.ssh/vastai_key /root/project
#
# Env:
#     SKIP_TUNNEL=1   (default) don't start cloudflared on the server
#     SYNC_ONLY=1     just rsync, don't launch serve_all.sh
# =============================================================================
set -euo pipefail

HOST="${1:?usage: deploy_vast.sh <HOST> <PORT> [SSH_KEY] [REMOTE_ROOT]}"
PORT="${2:?need PORT}"
KEY="${3:-$HOME/.ssh/vastai_key}"
REMOTE_ROOT="${4:-/workspace/project}"

SSH_OPTS=(-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
          -o ServerAliveInterval=30 -i "$KEY" -p "$PORT")
RSYNC_SSH="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i $KEY -p $PORT"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "[deploy] target root@$HOST:$PORT  ->  $REMOTE_ROOT"
ssh "${SSH_OPTS[@]}" root@"$HOST" "mkdir -p $REMOTE_ROOT"

# Ship code only — models download on the box; skip data/notebooks/caches.
EXCLUDES=(
    --exclude '__pycache__' --exclude '*.pyc' --exclude '.venv' --exclude '.git'
    --exclude 'app/physics_solution/data' --exclude 'app/physics_solution/eda'
    --exclude 'app/physics_solution/docs' --exclude 'app/notebooks'
    --exclude 'app/figures' --exclude 'app/logic_solution/outputs'
    --exclude 'app/logic_solution/data' --exclude '*/output/' --exclude '*.rar'
)

echo "[deploy] rsync app/ + scripts/ ..."
rsync -az --delete "${EXCLUDES[@]}" -e "$RSYNC_SSH" \
    app scripts root@"$HOST":"$REMOTE_ROOT"/

if [ "${SYNC_ONLY:-0}" = "1" ]; then
    echo "[deploy] SYNC_ONLY=1 — code uploaded, not launching. Done."
    exit 0
fi

echo "[deploy] launching serve_all.sh (this blocks while ~20GB of models download)..."
ssh "${SSH_OPTS[@]}" root@"$HOST" \
    "cd $REMOTE_ROOT && SKIP_TUNNEL=${SKIP_TUNNEL:-1} bash scripts/serve_all.sh start"

echo "[deploy] done. Tunnel in with:"
echo "  ssh -p $PORT root@$HOST -L 9000:localhost:9000   # then http://localhost:9000/docs"
