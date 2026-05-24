"""Chạy từ `notebooks/*.ipynb`: `%run -i project_bootstrap.py` — thêm `src/` vào PYTHONPATH + nạp `.env`."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from services.config import load_dotenv_for_logic

_loaded = load_dotenv_for_logic()
if _loaded:
    print("Đã nạp .env:", _loaded)
else:
    print(
        "Chưa nạp .env (không thấy file hoặc chưa cài python-dotenv) — dùng biến shell / notebook."
    )

print(f"project_bootstrap: PYTHONPATH += {_SRC}")
