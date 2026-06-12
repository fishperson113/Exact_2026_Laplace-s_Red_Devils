"""Torch-free parsers for the logic pipeline (in-process HOẶC vLLM HTTP).

ĐỒNG BỘ 1:1 với src/models/QA_model/train.py::_parse_full_output (QA v3):
output model = <reasoning steps Rule:/Fact:/Derive:/Conclusion:> + JSON cuối
{"premises_used": [...], "explanation": "...", "answer": "..."} (answer ĐỨNG CUỐI).
Không import torch/transformers để FastAPI gateway (vLLM over HTTP) dùng chung.
"""
from __future__ import annotations

import json
import re

QA_STEP_PREFIXES = ("Rule:", "Fact:", "Derive:", "Conclusion:")


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


def extract_reasoning_steps(text: str) -> list[str]:
    """Gom NGUYÊN VĂN các dòng reasoning (Rule:/Fact:/Derive:/Conclusion:) model sinh.
    Không cắt câu, không chế biến — đúng yêu cầu BTC reasoning.steps."""
    return [ln.strip() for ln in text.split("\n") if ln.strip().startswith(QA_STEP_PREFIXES)]


def parse_qa_output(text: str) -> dict:
    """Parse output QA v3: <reasoning steps> + JSON cuối {premises_used, explanation, answer}.

    Trả: {"answer", "explanation", "premises_used", "reasoning_steps"}.
    Robust với JSON cụt/lỗi (3 tầng fallback, khớp train.py + Ensemble inference).
    """
    reasoning_steps = extract_reasoning_steps(text)

    def _premises(parsed) -> list[int]:
        pu = parsed.get("premises_used", [])
        out = []
        if isinstance(pu, list):
            for v in pu:
                try:
                    out.append(int(v))
                except (ValueError, TypeError):
                    pass
        return out

    # 1. JSON CUỐI cùng có "answer"
    for m in reversed(list(re.finditer(r"\{.*?\}", text, re.DOTALL))):
        try:
            parsed = json.loads(m.group())
        except json.JSONDecodeError:
            continue
        if "answer" in parsed:
            return {
                "answer": str(parsed["answer"]).strip(),
                "explanation": str(parsed.get("explanation", "")).strip(),
                "premises_used": _premises(parsed),
                "reasoning_steps": reasoning_steps,
            }

    # 2. JSON cụt/lỗi: moi từng trường (explanation NON-GREEDY → hết rác)
    m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
    if m:
        em = re.search(r'"explanation"\s*:\s*"(.*?)"\s*[,}]', text, re.DOTALL)
        pm = re.search(r'"premises_used"\s*:\s*\[([^\]]*)\]', text)
        return {
            "answer": m.group(1).strip(),
            "explanation": em.group(1).strip() if em else "",
            "premises_used": [int(x) for x in re.findall(r"\d+", pm.group(1))] if pm else [],
            "reasoning_steps": reasoning_steps,
        }

    # 3. Last-resort: Conclusion hoặc cue, KHÔNG đoán bừa A/B/C/D trong văn xuôi
    concl = next((s for s in reversed(reasoning_steps) if s.startswith("Conclusion:")), "")
    m2 = re.search(r"\b(Yes|No|Unknown|Uncertain|[ABCD])\b\s*$", concl)
    if not m2:
        m2 = re.search(
            r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|Uncertain|[ABCD])\b",
            text, re.I,
        )
    if m2:
        return {"answer": m2.group(1), "explanation": "",
                "premises_used": [], "reasoning_steps": reasoning_steps}
    for label in ("Uncertain", "Unknown", "Yes", "No"):
        if re.search(rf"\b{label}\b", text):
            return {"answer": label, "explanation": "",
                    "premises_used": [], "reasoning_steps": reasoning_steps}
    return {"answer": "Uncertain", "explanation": "",
            "premises_used": [], "reasoning_steps": reasoning_steps}
