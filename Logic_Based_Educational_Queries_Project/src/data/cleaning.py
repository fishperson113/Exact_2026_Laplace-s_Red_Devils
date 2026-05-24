"""Làm sạch dữ liệu (outlier, missing, noise) — mở rộng theo nhu cầu.

Với bộ Logic hiện tại, bước làm sạch chính là chuẩn hoá nhãn và flatten ở `splitting.py`
(gọi `require_answer_label` trong `evaluation.metrics`). Hàm dưới giữ chỗ cho logic bổ sung.
"""
from __future__ import annotations

from typing import Any


def noop_clean_record(rec: dict[str, Any]) -> dict[str, Any]:
    """Trả về record không đổi; thay bằng filter/transform khi cần."""
    return rec
