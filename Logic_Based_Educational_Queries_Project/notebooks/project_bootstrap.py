"""Bootstrap: thêm `src/` vào PYTHONPATH + nạp `.env`.

Trong notebook pipeline, ô đầu tiên đã gọi script này bằng **đường dẫn tuyệt đối** (tìm từ
`Path.cwd()` lên các thư mục cha), nên không phụ thuộc cwd.

Nếu bạn tự chạy tay và cwd đã là `notebooks/`, có thể dùng: ``%run -i project_bootstrap.py``
"""
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
