"""Hậu xử lý answer/explanation — torch-free, dùng chung cho QA + Ensemble inference.

ĐỒNG BỘ 1:1 với app/logic_solution/utils/postprocess.py (bản đã fix hiện tượng
model trả LETTER A/B/C/D hoặc text lệch khi options lồng vào query):
  - snap_answer_to_options: ép answer của choice-question về VERBATIM một option
    (BTC chấm exact match) — exact-norm → letter→index → Unknown↔Uncertain → fuzzy.
  - clean_explanation: gỡ explanation bị model bọc JSON.
"""
from __future__ import annotations

import difflib
import json
import re

_OPT_LETTERS = "ABCDEFGHIJ"


def _snap_norm(s: str) -> str:
    """lowercase + gộp khoảng trắng + bỏ dấu câu cuối (khớp _na khi eval)."""
    s = re.sub(r"\s+", " ", str(s).strip().lower())
    return s.rstrip(" .;:!?")


def snap_answer_to_options(answer: str, options: list[str]) -> str:
    """Ép answer về VERBATIM một option. Thứ tự ưu tiên:
      1. options rỗng (free-form) → giữ nguyên.
      2. Khớp option sau normalize → trả NGUYÊN VĂN option.
      3. Answer là 1 letter A-J → map options[index].
      4. Unknown ↔ Uncertain → map option tương ứng.
      5. Fuzzy (difflib ≥ 0.75) → option giống nhất.
      6. Không khớp → giữ nguyên (không đoán bừa).
    """
    ans = str(answer).strip()
    if not options:
        return ans
    for opt in options:
        if _snap_norm(opt) == _snap_norm(ans):
            return opt
    if len(ans) == 1 and ans.upper() in _OPT_LETTERS:
        idx = _OPT_LETTERS.index(ans.upper())
        if idx < len(options):
            return options[idx]
    if _snap_norm(ans) in ("unknown", "uncertain"):
        for opt in options:
            if _snap_norm(opt) in ("unknown", "uncertain"):
                return opt
    matches = difflib.get_close_matches(
        _snap_norm(ans), [_snap_norm(o) for o in options], n=1, cutoff=0.75
    )
    if matches:
        for opt in options:
            if _snap_norm(opt) == matches[0]:
                return opt
    return ans


def clean_explanation(explanation: str) -> str:
    """Gỡ explanation bị model bọc JSON ('{"answer": "A", "explanation": "text...')."""
    if not isinstance(explanation, str):
        return str(explanation)
    stripped = explanation.strip()
    if not stripped.startswith('{"'):
        return explanation
    try:
        inner = json.loads(stripped)
        if isinstance(inner, dict) and "explanation" in inner:
            return str(inner["explanation"]).strip()
    except (json.JSONDecodeError, ValueError):
        pass
    match = re.search(r'"explanation"\s*:\s*"(.*)', stripped, re.DOTALL)
    if match:
        raw = match.group(1)
        raw = re.sub(r'["}]+$', "", raw)
        return raw.replace('\\"', '"').replace("\\n", "\n").strip()
    return explanation
