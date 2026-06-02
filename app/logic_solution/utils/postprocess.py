"""
utils/postprocess.py
--------------------
Đảm bảo output đúng format BTC trước khi lưu:
  - Thứ tự field: answer → explanation → fol
  - Fix nested JSON trong explanation (lỗi model sinh ra)
  - Không thêm field nào ngoài 3 field trên
"""
from __future__ import annotations

import re


def clean_explanation(explanation: str) -> str:
    """
    Fix trường hợp model sinh explanation dạng nested JSON:
      '{"answer": "A", "explanation": "actual text here...'
    → trả về chỉ "actual text here..."
    """
    if not isinstance(explanation, str):
        return str(explanation)

    stripped = explanation.strip()

    # Không bị lỗi → trả nguyên
    if not stripped.startswith('{"answer"'):
        return explanation

    # Thử parse JSON đầy đủ
    import json
    try:
        inner = json.loads(stripped)
        if isinstance(inner, dict) and "explanation" in inner:
            return str(inner["explanation"]).strip()
    except (json.JSONDecodeError, ValueError):
        pass

    # Fallback cho truncated JSON: lấy mọi thứ sau "explanation": "
    match = re.search(r'"explanation"\s*:\s*"(.*)', stripped, re.DOTALL)
    if match:
        raw = match.group(1)
        raw = re.sub(r'["}]+$', '', raw)   # bỏ ký tự đóng JSON cuối nếu có
        return raw.replace('\\"', '"').replace('\\n', '\n').strip()

    return explanation


def format_submission(answer: str, explanation: str, fol: str) -> dict:
    """
    Trả về dict đúng thứ tự field BTC:
      answer → explanation → fol
    """
    return {
        "answer":      str(answer).strip(),
        "explanation": clean_explanation(explanation),
        "fol":         str(fol).strip(),
    }
