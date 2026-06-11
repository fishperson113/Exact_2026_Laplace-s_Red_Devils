"""
utils/io.py
-----------
Load input JSON (format BTC) và save output JSON.

Input BTC — mỗi sample đủ 5 trường:
  {"query_id": "T1_0001", "type": "type1", "query": "...",
   "premises": ["...", "..."], "options": ["...", ...]}

Fallback tên cũ (nội bộ): "question" ↔ "query", "premises-NL"/"premises_nl" ↔ "premises".
Output LUÔN là JSON list — kể cả khi chỉ có 1 query (quy định BTC).
"""
from __future__ import annotations

import json
from pathlib import Path


def load_input(path: str | Path) -> list[dict]:
    """
    Load danh sách samples từ JSON file (format BTC, 5 trường).

    Trả về list[dict] đã chuẩn hoá:
      - "query_id"  (str)  — nếu input thiếu, tự sinh "T1_0001", "T1_0002", ...
      - "type"      (str)  — passthrough (pipeline logic không dùng)
      - "query"     (str)  — câu hỏi
      - "premises"  (list[str])
      - "options"   (list[str]) — rỗng = free-form (number/text)
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if isinstance(raw, dict):
        raw = [raw]     # Hỗ trợ single-sample input → vẫn xử lý như list

    samples = []
    for i, item in enumerate(raw):
        query = str(item.get("query") or item.get("question") or "").strip()
        if not query:
            raise ValueError(f"Sample [{i}]: thiếu field 'query' (hoặc 'question').")

        premises = (
            item.get("premises")
            or item.get("premises-NL")
            or item.get("premises_nl")
            or item.get("premises_NL")
            or []
        )
        options = item.get("options") or []

        samples.append({
            "query_id": str(item.get("query_id") or f"T1_{i + 1:04d}"),
            "type":     str(item.get("type") or "type1"),
            "query":    query,
            "premises": premises if isinstance(premises, list) else [premises],
            "options":  options if isinstance(options, list) else [options],
        })

    return samples


def save_output(results: list[dict], path: str | Path) -> None:
    """Lưu results ra JSON file (UTF-8). LUÔN là JSON list — kể cả 1 phần tử."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(list(results), f, ensure_ascii=False, indent=2)
    print(f"[IO] Saved {len(results)} results → {path}")
