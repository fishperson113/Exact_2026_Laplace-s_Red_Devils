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
    # Fallback: pull a label out of free text
    for label in ("A", "B", "C", "D", "Yes", "No", "Unknown"):
        if label in text:
            return {"answer": label, "explanation": text}
    return {"answer": "Unknown", "explanation": text}
