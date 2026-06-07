"""Offline test of the QC pure logic (no API, no execution, no heavy deps).

Run: PYTHONPATH=. python3 -m app.physics_solution.QC_data.qc_smoke
(or run_qc.py --selftest). Covers parse_diagnose fallbacks, the gold-leak guard, and
apply_verdict's CLEAN/FIX/DROP handling. The 3-stage orchestration + execution gate are
exercised live by run_qc (see README); this only pins the deterministic helpers.
"""

from __future__ import annotations

import json

from app.physics_solution.QC_data import qc_filter


def _spec(**kw) -> dict:
    base = {
        "id": "X1", "question": "Q text", "domain": "CH", "answer_type": "numeric",
        "gold_answer": "12.34", "gold_unit": "V", "dataset_source": "vietjack", "meta": {},
    }
    base.update(kw)
    return base


def _diag(verdict, fixed=None, err="other", reason="r") -> str:
    return json.dumps({"verdict": verdict, "error_type": err,
                       "fixed_question": fixed, "reason": reason})


def run() -> None:
    P = qc_filter.parse_diagnose
    A = qc_filter.apply_verdict
    ok = 0

    def check(cond, msg):
        nonlocal ok
        assert cond, "FAIL: " + msg
        ok += 1

    # ---- parse_diagnose ----------------------------------------------------
    check(P(_diag("FIX", fixed="z"))["verdict"] == "FIX", "parse FIX")
    check(P("noise " + _diag("DROP"))["verdict"] == "DROP", "parse DROP w/ surrounding noise")
    check(P("not json")["verdict"] == "DROP", "parse failure -> DROP (conservative)")
    check(P("not json")["error_type"] == "diagnose_parse_failure", "parse failure tagged")
    check(P(_diag("CLEAN"))["verdict"] == "CLEAN", "parse CLEAN (solver-slip/rounding escape)")
    check(P(_diag("weird"))["verdict"] == "DROP", "unknown verdict -> DROP")

    # ---- apply CLEAN -------------------------------------------------------
    k, d = A(_spec(question="orig"), {"verdict": "CLEAN", "error_type": "none",
                                      "fixed_question": None, "reason": "ok"})
    check(d is None and k["question"] == "orig", "CLEAN keeps question")
    check(k["meta"]["qc_verdict"] == "CLEAN", "CLEAN tags meta")

    # ---- apply FIX swaps corrected question, stashes original --------------
    k, d = A(_spec(question="I = 3 sqrt(2) A", gold_answer="60", gold_unit="deg"),
             {"verdict": "FIX", "error_type": "ocr", "fixed_question": "I = sqrt(3)/2 A", "reason": "ocr"})
    check(d is None and k["question"] == "I = sqrt(3)/2 A", "FIX applies corrected question")
    check(k["meta"]["qc_original_question"] == "I = 3 sqrt(2) A", "FIX stashes original")
    check(k["meta"]["qc_verdict"] == "FIX" and k["meta"]["qc_error_type"] == "ocr", "FIX meta")

    # ---- apply DROP -> audit only -----------------------------------------
    k, d = A(_spec(question="see figure"),
             {"verdict": "DROP", "error_type": "missing_figure", "fixed_question": None, "reason": "needs fig"})
    check(k is None and d is not None, "DROP -> audit only")
    check(d["qc_error_type"] == "missing_figure" and d["question"] == "see figure", "DROP record fields")

    # ---- gold-leak guard (used by run_qc before confirming a FIX) ---------
    check(qc_filter.gold_leaked("12.34", "U equals 12.34 V", "find U"), "leak detected")
    check(not qc_filter.gold_leaked("50", "R = 50 ohm fixed", "R = 50 ohm given"), "gold in original is not a leak")
    check(not qc_filter.gold_leaked("Yes", "answer is Yes", "q"), "yes/no never a leak")

    print(f"qc_smoke: all {ok} checks passed.")


if __name__ == "__main__":
    run()
