"""
utils/io.py
-----------
Load input JSON và save output JSON.

Input hỗ trợ 2 dạng field name (theo BTC):
  - "premises-NL"  (dấu gạch ngang — đúng chuẩn BTC Type 1)
  - "premises_nl"  (gạch dưới — dạng nội bộ)
"""
from __future__ import annotations

import json
from pathlib import Path


def load_input(path: str | Path) -> list[dict]:
    """
    Load danh sách samples từ JSON file.

    Mỗi sample phải có:
      - "premises-NL" hoặc "premises_nl"  (list[str], Type 1)
      - "question"                         (str)

    Trả về list[dict] với key chuẩn hoá thành "premises_nl".
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if isinstance(raw, dict):
        raw = [raw]     # Hỗ trợ single-sample input

    samples = []
    for i, item in enumerate(raw):
        # Chuẩn hoá field name: "premises-NL" → "premises_nl"
        premises = (
            item.get("premises-NL")
            or item.get("premises_nl")
            or item.get("premises_NL")
            or []
        )
        question = item.get("question", "")

        if not question:
            raise ValueError(f"Sample [{i}]: thiếu field 'question'.")

        samples.append({
            "premises_nl": premises if isinstance(premises, list) else [premises],
            "question":    str(question),
        })

    return samples


def save_output(results: list[dict], path: str | Path) -> None:
    """Lưu results ra JSON file (đẹp, UTF-8)."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[IO] Saved {len(results)} results → {path}")
