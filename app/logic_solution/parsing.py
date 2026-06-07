"""Torch-free parsers for the logic vLLM pipeline.

Mirrors ``FOLModel._parse_fol`` and ``QAModel._parse_output`` from
``pipeline/`` but WITHOUT importing torch/transformers, so the FastAPI
gateway (which talks to vLLM over HTTP) can reuse the exact parse logic.
Keep these in sync with the staticmethods in pipeline/{fol,qa}_model.py.
"""
from __future__ import annotations

import json
import re


def parse_fol(text: str) -> list[str]:
    """Parse ``{"premises_fol": [...]}`` or fall back to line-by-line."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            parsed = json.loads(match.group())
            if "premises_fol" in parsed and isinstance(parsed["premises_fol"], list):
                return [str(f).strip() for f in parsed["premises_fol"]]
        except json.JSONDecodeError:
            pass
    # Fallback: keep lines that carry logic symbols / predicate calls
    lines = []
    for line in text.split("\n"):
        line = line.strip().lstrip("0123456789.)-  ")
        if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
            lines.append(line)
    return lines


def parse_qa_output(text: str) -> dict[str, str]:
    """Parse ``{"answer": ..., "explanation": ...}`` with a label fallback."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            parsed = json.loads(match.group())
            if "answer" in parsed:
                return {
                    "answer": str(parsed["answer"]).strip(),
                    "explanation": str(parsed.get("explanation", "")).strip(),
                }
        except json.JSONDecodeError:
            pass
    # JSON cụt/lỗi: vẫn moi được "answer": "..." (và explanation nếu có)
    m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
    if m:
        ans = m.group(1).strip()
        em = re.search(r'"explanation"\s*:\s*"(.*)', text, re.DOTALL)
        explanation = em.group(1).strip().rstrip('"}').strip() if em else ""
        return {"answer": ans, "explanation": explanation}
    # Last-resort: word-boundary + cue, KHÔNG đoán bừa chữ "A" trong văn xuôi
    m2 = re.search(
        r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|[ABCD])\b",
        text, re.I,
    )
    if m2:
        return {"answer": m2.group(1), "explanation": ""}
    for label in ("Unknown", "Yes", "No"):
        if re.search(rf"\b{label}\b", text):
            return {"answer": label, "explanation": ""}
    return {"answer": "Unknown", "explanation": ""}
