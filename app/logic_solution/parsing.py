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


# ── Epistemic / meta premises ("vắng mặt thông tin") ──────────────────────────
# Mệnh đề kiểu "No premise states whether X" / "It is unknown whether X" nói về
# bản thân tập tri thức (meta), KHÔNG về thế giới. FOL object-level không biểu
# diễn được → FOL model hay bám từ khoá bề mặt và sinh phủ định GIẢ (¬X), khiến
# QA suy ra No thay vì Uncertain. Ta phát hiện trên NL gốc rồi ghi đè ô FOL
# tương ứng bằng note trung lập (giữ nguyên số dòng → index không lệch).
#
# REGEX HẸP — chỉ bắt cụm meta đặc trưng, KHÔNG bắt mọi "whether" (có premise
# hợp lệ chứa "whether", vd "If a student passes whether or not they study...").
_EPISTEMIC_PATTERNS = [
    r"\bno premise\b.{0,40}\bwhether\b",
    r"\bno premise (?:states|specifies|mentions|indicates)\b",
    r"\bit is (?:un)?known whether\b",
    r"\b(?:not|isn't|is not) (?:specified|stated|known|mentioned) whether\b",
    r"\b(?:does not|doesn't|do not|don't) (?:state|specify|say) whether\b",
    r"\bno (?:information|statement|fact)\b.{0,40}\bwhether\b",
    r"\bunspecified whether\b",
]
_EPISTEMIC_RE = re.compile("|".join(_EPISTEMIC_PATTERNS), re.IGNORECASE)

# Cờ đặt TRƯỚC câu NL gốc của mệnh đề epistemic (thay cho phủ định giả ¬X).
# ĐỒNG BỘ 1:1 với src/models/QA_model/prepare_data.py::_EPISTEMIC_FOL_TAG — PHẢI khớp
# ĐÚNG chuỗi cờ trong SYSTEM_PROMPT_QA (khối "Handling premises absent/unknown").
_EPISTEMIC_FOL_TAG = "[UNCERTAIN]"


def is_epistemic_premise(nl: str) -> bool:
    """True nếu mệnh đề NL chỉ nêu sự VẮNG MẶT/không chắc chắn thông tin."""
    return bool(_EPISTEMIC_RE.search(str(nl)))


def neutralize_epistemic_fol(premises_nl: list[str], fol_list: list[str]) -> list[str]:
    """Ghi đè TẠI CHỖ ô FOL của mệnh đề epistemic bằng chính câu NL gốc (gắn cờ [UNCERTAIN]).

    - Quét premises_nl GỐC (không quét fol_list — NL đáng tin hơn FOL output).
    - GIỮ NGUYÊN số phần tử của fol_list (chỉ replace, không xoá) → index không lệch.
    - Giữ nguyên nội dung NL (còn predicate dưới dạng chữ) thay vì sentinel trống.
    - Trả về list mới (không mutate input).
    """
    out = list(fol_list)
    for i, nl in enumerate(premises_nl):
        if i < len(out) and is_epistemic_premise(nl):
            out[i] = f"{_EPISTEMIC_FOL_TAG} {str(nl).strip()}"
    return out


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

    def _from_expl(expl) -> list[int]:
        # premises_used CHUẨN = các "premise N" model tự trích trong explanation (0-based).
        # Bắt cả số nhiều ("premises"), list ("1, 2 and 3") và range ("1-3", "1–3").
        if not expl:
            return []
        out: set[int] = set()
        for m in re.finditer(r"premises?\s+((?:\d+\s*(?:[-–—]\s*\d+)?\s*[,&]?\s*(?:and\s+)?)+)", expl, re.I):
            chunk = m.group(1)
            for a, b in re.findall(r"(\d+)\s*[-–—]\s*(\d+)", chunk):
                a, b = int(a), int(b)
                if a <= b and b - a < 100:
                    out.update(range(a, b + 1))
            chunk = re.sub(r"\d+\s*[-–—]\s*\d+", " ", chunk)
            out.update(int(n) for n in re.findall(r"\d+", chunk))
        return sorted(out)

    # 1. JSON CUỐI cùng có "answer"
    for m in reversed(list(re.finditer(r"\{.*?\}", text, re.DOTALL))):
        try:
            parsed = json.loads(m.group())
        except json.JSONDecodeError:
            continue
        if "answer" in parsed:
            expl = str(parsed.get("explanation", "")).strip()
            pu_expl = _from_expl(expl)
            return {
                "answer": str(parsed["answer"]).strip(),
                "explanation": expl,
                "premises_used": pu_expl if pu_expl else _premises(parsed),
                "reasoning_steps": reasoning_steps,
            }

    # 2. JSON cụt/lỗi: moi từng trường (explanation NON-GREEDY → hết rác)
    m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
    if m:
        em = re.search(r'"explanation"\s*:\s*"(.*?)"\s*[,}]', text, re.DOTALL)
        pm = re.search(r'"premises_used"\s*:\s*\[([^\]]*)\]', text)
        expl = em.group(1).strip() if em else ""
        pu_model = [int(x) for x in re.findall(r"\d+", pm.group(1))] if pm else []
        pu_expl = _from_expl(expl)
        return {
            "answer": m.group(1).strip(),
            "explanation": expl,
            "premises_used": pu_expl if pu_expl else pu_model,
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
