"""QC prompts + parser + apply logic for the execution-grounded QC (pure helpers).

Kept free of heavy deps (only json/re) so the parse/apply logic is offline-testable
(qc_smoke.py). The orchestration — DeepSeek calls + the execution gate — lives in
run_qc.py.

Two model roles:
  SOLVE_SYSTEM    a strong solver that writes code to solve the problem AS WRITTEN
                  (gold-free). run_qc executes it and scores vs gold: match -> CLEAN.
  DIAGNOSE_SYSTEM on a mismatch, with the gold + failed attempt shown, decides FIX/DROP
                  and (for FIX) returns the corrected statement.

Diagnose verdict contract (JSON):
    {"verdict": "FIX|DROP",
     "error_type": "ocr|missing_symbol|garbled_value|missing_data|missing_options|"
                   "ambiguous|answer_wrong|other",
     "fixed_question": "<full corrected statement, or null>",
     "reason": "<short>"}
"""

from __future__ import annotations

import json
import re

# --------------------------------------------------------------- solve (stage 1 & 3)

SOLVE_SYSTEM = """\
You are an expert physics solver. Write a self-contained Python script that solves the
problem EXACTLY AS STATED and COMPUTES the answer from the given quantities.

RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- HARDCODE standard constants rather than importing them (they are more reliable):
  k = 9e9, epsilon_0 = 8.854e-12, mu_0 = 4*math.pi*1e-7, e = 1.602e-19, g = 9.8.
- Define every given value at the top with SI unit conversions.
- Write the key formula as a comment before each computation.
- COMPUTE everything in code — never hardcode an intermediate result or the final number.
  (Symbolic computation with sympy is fine when the problem gives no numeric values.)
- The script MUST print exactly two lines at the end:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute the quantity and compare with TOLERANCE (~1%, or round to the
  precision implied by the question) — textbooks round (e.g. 79.57 -> 80), so do not fail a
  near-match; print "Yes" or "No".
- For multi_value print values separated by ";".
- NEVER use e-notation in output. Write 2.97 * 10^6, not 2.97e6.

Solve the problem strictly as written. Do NOT assume the statement is wrong and do NOT
"correct" it — if the text leads to a particular number, compute that number.
"""


def build_solve_messages(spec: dict) -> list[dict]:
    """Gold-free solve prompt for one ProblemSpec dict (stage 1 and the FIX re-check)."""
    user = (
        f"DOMAIN: {spec.get('domain', '')}\n"
        f"ANSWER TYPE: {spec.get('answer_type', '')}\n\n"
        f"PROBLEM:\n{spec.get('question', '')}\n\n"
        f"Write a Python script that solves this exactly as stated."
    )
    return [
        {"role": "system", "content": SOLVE_SYSTEM},
        {"role": "user", "content": user},
    ]


# --------------------------------------------------------------- diagnose (stage 2)

DIAGNOSE_SYSTEM = """\
You are a meticulous physics data-quality reviewer. A strong solver tried to solve the
problem EXACTLY AS WRITTEN and its executed answer did NOT match the known correct answer.
Diagnose WHY. Use the correct answer ONLY to locate the defect — NEVER copy it into the
statement and NEVER invent numbers to force a match.

Give exactly ONE verdict:

- CLEAN: the STATEMENT is actually fine — the mismatch is NOT a text defect. Use this when
  the solver simply made a mistake (wrong constant, arithmetic/setup slip), OR the two
  answers differ only by rounding / significant figures / an acceptable approximation (the
  given answer is a rounded form of the solver's result). Keep the problem unchanged.

- FIX: a single, mechanically-plausible corruption of a NUMBER, MATH SYMBOL, or UNIT in the
  statement explains the gap — an OCR misread (e.g. "3√2" vs "√3/2", "10^-4" lost as
  "10-4", l<->1, O<->0), a dropped symbol (a missing π, √, exponent, "×10^n", or unit), or
  a garbled digit. Return `fixed_question` = the FULL statement with ONLY that token
  corrected, preserving every other word, number, and the original formatting. You are
  reconstructing what was clearly intended, NOT authoring a new problem.

- DROP: not safely repairable, e.g.:
    * required data/options/figure are missing or the statement is truncated;
    * reconciling would require changing a physics-MEANING word (parallel<->perpendicular,
      series<->parallel, increases<->decreases) or the described setup — that is guessing
      the author's intent, not repairing an OCR/typo of a number;
    * the solver's attempt looks physically correct but the GIVEN ANSWER is genuinely wrong
      (NOT merely a rounded form of the solver's result — that case is CLEAN). Such a
      problem can't yield a verified solution, so drop it.

Rules: only ever FIX corrupted numbers, math symbols, or units. Prefer CLEAN when the text
is fine; if torn between FIX and DROP, choose DROP.

Output ONLY a compact JSON object, no prose:
{"verdict":"CLEAN","error_type":"none","fixed_question":null,"reason":"<short>"}
"""

_VALID_DIAG = {"CLEAN", "FIX", "DROP"}
_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def build_diagnose_messages(spec: dict, attempt_code: str | None,
                            attempt_answer: str | None, attempt_error: str | None) -> list[dict]:
    """Diagnose prompt: original statement + gold + the failed solve attempt."""
    if attempt_code:
        attempt = f"SOLVER ATTEMPT (code, solved as written):\n{attempt_code}\n"
        if attempt_answer is not None:
            attempt += f"-> it computed: {attempt_answer}\n"
        elif attempt_error:
            attempt += f"-> it errored: {attempt_error[:400]}\n"
    else:
        attempt = "SOLVER ATTEMPT: no runnable code could be produced for the text as written.\n"

    user = (
        f"DOMAIN: {spec.get('domain', '')}\n"
        f"ANSWER TYPE: {spec.get('answer_type', '')}\n\n"
        f"PROBLEM (as written):\n{spec.get('question', '')}\n\n"
        f"CORRECT ANSWER (for diagnosis only): "
        f"{spec.get('gold_answer', '')} {spec.get('gold_unit', '')}\n\n"
        f"{attempt}\n"
        f"Diagnose: FIX (repair a corrupted number/symbol/unit) or DROP?"
    )
    return [
        {"role": "system", "content": DIAGNOSE_SYSTEM},
        {"role": "user", "content": user},
    ]


def parse_diagnose(text: str) -> dict:
    """Parse the {verdict, error_type, fixed_question, reason} JSON.

    On parse failure -> DROP (conservative: stage-2 only runs after a real solve mismatch,
    so an undiagnosable problem is treated as broken; it is logged for audit/re-run).
    """
    m = _JSON_RE.search(text or "")
    if not m:
        return {"verdict": "DROP", "error_type": "diagnose_parse_failure",
                "fixed_question": None, "reason": "could not parse diagnosis"}
    try:
        obj = json.loads(m.group(0))
    except (json.JSONDecodeError, ValueError):
        return {"verdict": "DROP", "error_type": "diagnose_parse_failure",
                "fixed_question": None, "reason": "could not parse diagnosis"}
    verdict = str(obj.get("verdict", "DROP")).strip().upper()
    if verdict not in _VALID_DIAG:
        verdict = "DROP"
    fixed = obj.get("fixed_question")
    return {
        "verdict": verdict,
        "error_type": str(obj.get("error_type", "other")).strip() or "other",
        "fixed_question": fixed if isinstance(fixed, str) else None,
        "reason": str(obj.get("reason", "")).strip(),
    }


# --------------------------------------------------------------- apply

def gold_leaked(gold_answer: str, fixed_q: str, original_q: str) -> bool:
    """True if a FIX injected the gold value into the statement (a leak we must reject).

    Conservative: only fires when the full gold string (>=2 chars, not a yes/no/bool token)
    newly appears in the fixed text but was absent from the original.
    """
    g = str(gold_answer or "").strip().lower()
    if len(g) < 2 or g in {"yes", "no", "true", "false", "n/a"}:
        return False
    return g in (fixed_q or "").lower() and g not in (original_q or "").lower()


def apply_verdict(spec: dict, verdict: dict) -> tuple[dict | None, dict | None]:
    """Turn a (spec, verdict) into (kept_spec | None, dropped_record | None).

    `verdict["verdict"]` is CLEAN / FIX / DROP (run_qc maps the 3 stages onto these).
    - DROP  -> (None, audit dict).
    - CLEAN -> (spec + qc meta, None).
    - FIX   -> (spec with corrected `question` + original stashed in meta, None).
    """
    v = verdict.get("verdict", "CLEAN")
    if v == "DROP":
        dropped = {
            "id": spec.get("id", ""),
            "domain": spec.get("domain", ""),
            "answer_type": spec.get("answer_type", ""),
            "dataset_source": spec.get("dataset_source", ""),
            "qc_error_type": verdict.get("error_type", ""),
            "qc_reason": verdict.get("reason", ""),
            "gold_answer": spec.get("gold_answer", ""),
            "gold_unit": spec.get("gold_unit", ""),
            "question": spec.get("question", ""),
        }
        return None, dropped

    kept = dict(spec)
    meta = dict(spec.get("meta") or {})
    meta["qc_verdict"] = v
    meta["qc_reason"] = verdict.get("reason", "")
    if v == "FIX":
        meta["qc_original_question"] = spec.get("question", "")
        meta["qc_error_type"] = verdict.get("error_type", "")
        kept["question"] = (verdict.get("fixed_question") or "").strip() or spec.get("question", "")
    kept["meta"] = meta
    return kept, None
