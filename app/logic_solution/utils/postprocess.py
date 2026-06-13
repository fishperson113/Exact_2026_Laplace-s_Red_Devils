"""
utils/postprocess.py
--------------------
Đảm bảo output đúng Unified Output Schema BTC (§4.1) trước khi lưu:

  {"query_id", "answer", "unit", "explanation", "premises_used",
   "reasoning": {"type": "fol", "steps": [...]}}

  - Đúng 6 trường, đúng thứ tự; trường không áp dụng để rỗng ("" hoặc []).
  - "unit" là trường của Type 2 (physics) — logic luôn "".
  - reasoning.type LUÔN "fol"; reasoning.steps = NGUYÊN VĂN steps model sinh.
  - snap_answer_to_options: lưới an toàn — đảm bảo answer của choice question
    luôn là VERBATIM một option trong list (BTC chấm exact match với answer).
"""
from __future__ import annotations

import difflib
import json
import re

_OPT_LETTERS = "ABCDEFGHIJ"


def _norm(s: str) -> str:
    """lowercase + gộp khoảng trắng + bỏ dấu câu cuối (khớp _norm_answer khi train)."""
    s = re.sub(r"\s+", " ", str(s).strip().lower())
    return s.rstrip(" .;:!?")


def snap_answer_to_options(answer: str, options: list[str]) -> str:
    """Ép answer về VERBATIM một option (BTC so khớp y hệt chuỗi đáp án).

    Thứ tự ưu tiên:
      1. options rỗng (free-form) → trả answer nguyên trạng (đã strip).
      2. Khớp option sau normalize → trả NGUYÊN VĂN option đó.
      3. Answer là 1 letter A-J (tail case model trả letter) → map options[index].
      4. "Unknown" ↔ "Uncertain" (lệch nhãn) → map về option tương ứng nếu có.
      5. Fuzzy match (difflib ≥ 0.75) → option giống nhất.
      6. Không khớp gì → trả answer nguyên trạng (không đoán bừa).
    """
    ans = str(answer).strip()
    if not options:
        return ans

    # 2. Exact match sau normalize → verbatim option
    for opt in options:
        if _norm(opt) == _norm(ans):
            return opt

    # 3. Letter đơn → map theo index
    if len(ans) == 1 and ans.upper() in _OPT_LETTERS:
        idx = _OPT_LETTERS.index(ans.upper())
        if idx < len(options):
            return options[idx]

    # 4. Unknown ↔ Uncertain
    if _norm(ans) in ("unknown", "uncertain"):
        for opt in options:
            if _norm(opt) in ("unknown", "uncertain"):
                return opt

    # 5. Fuzzy match thận trọng
    matches = difflib.get_close_matches(_norm(ans), [_norm(o) for o in options], n=1, cutoff=0.75)
    if matches:
        for opt in options:
            if _norm(opt) == matches[0]:
                return opt

    # 6. Bó tay → giữ nguyên
    return ans


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
    if not stripped.startswith('{"'):
        return explanation

    # Thử parse JSON đầy đủ
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


def format_submission(
    query_id: str,
    answer: str,
    explanation: str,
    premises_used: list[int] | None = None,
    reasoning_steps: list[str] | None = None,
    options: list[str] | None = None,
    unit: str = "",
    fol_list: list[str] | None = None,
) -> dict:
    """
    Trả về dict đúng Unified Output Schema BTC — 6 trường, đúng thứ tự:
      query_id → answer → unit → explanation → premises_used → reasoning

    - answer được snap về verbatim option nếu là choice question.
    - reasoning.type LUÔN "fol"; steps giữ NGUYÊN VĂN (không chế biến).
    - reasoning.fol = bản FOL CUỐI (sau neutralize) mà QA đã đọc — tiện debug Stage 1.
      BTC bỏ qua key dư nên để thường trực.
    - unit: chỉ Type 2 dùng; logic mặc định "".
    """
    return {
        "query_id":      str(query_id),
        "answer":        snap_answer_to_options(answer, options or []),
        "unit":          str(unit or ""),
        "explanation":   clean_explanation(explanation),
        "premises_used": list(premises_used or []),
        "reasoning": {
            "type":  "fol",
            "steps": list(reasoning_steps or []),
            "fol":   list(fol_list or []),
        },
    }
