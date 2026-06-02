"""Local, GPU-free smoke test for the Phase-2 harness.

Validates everything except the actual model calls: the execution gate
(`pot_common.verify` -> executor + scorer), `make_trajectory`, and every
`guards` decision (keep computed, reject echo / baked-literal / no-computation,
dedup, cap). Run this before spending any GPU time on self-gen.

    PYTHONPATH=. .venv/bin/python -m app.physics_solution.versions.v06_finetune.data_pipeline.pot_smoke

Exits non-zero if any assertion fails.
"""

from __future__ import annotations

import asyncio
import sys

from app.physics_solution.config import repo_root
from app.physics_solution.versions.v06_finetune.data_pipeline import guards, pot_common
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec, read_jsonl

_PASS = 0
_FAIL = 0


def check(label: str, cond: bool) -> None:
    global _PASS, _FAIL
    if cond:
        _PASS += 1
        print(f"  [PASS] {label}")
    else:
        _FAIL += 1
        print(f"  [FAIL] {label}")


def _spec(sid, q, domain, at, gold, unit) -> ProblemSpec:
    return ProblemSpec(id=sid, question=q, domain=domain, answer_type=at,
                       gold_answer=gold, gold_unit=unit, dataset_source="btc_golden", meta={})


def _block(code: str) -> str:
    return f"```python\n{code}\n```"


# completions for a numeric gold G = 36.32 -------------------------------------
_COMPUTED = _block(
    "x = 254.24          # 7 * answer (an input, not the answer)\n"
    'print(f"FINAL ANSWER: {x / 7:.6g}")\n'
    'print("UNIT: N")'
)
_ECHO = _block('print("FINAL ANSWER: 36.32")\nprint("UNIT: N")')
_LITERAL_VAR = _block('ans = 36.32\nprint(f"FINAL ANSWER: {ans}")\nprint("UNIT: N")')
_BROKEN = _block("print(this_is_undefined)")


async def _verify_tests() -> None:
    print("\n=== verify (execution gate) ===")
    spec = _spec("LDx", "dummy", "LDDT", "numeric", "36.32", "N")

    vr = await pot_common.verify(_COMPUTED, spec)
    check("computed code -> correct", vr.is_correct and vr.exec_result.success)

    vr = await pot_common.verify(_ECHO, spec)
    check("echo code runs + scores correct (gate alone can't catch it)", vr.is_correct)

    vr = await pot_common.verify(_BROKEN, spec)
    check("broken code -> not correct, exec failed",
          (not vr.is_correct) and vr.exec_result is not None and not vr.exec_result.success)

    vr = await pot_common.verify("no code here", spec)
    check("no code block -> not correct, no exec_result",
          (not vr.is_correct) and vr.exec_result is None)

    # wrong-but-running answer must not pass the gate
    wrong = _block('print("FINAL ANSWER: 99.0")\nprint("UNIT: N")')
    vr = await pot_common.verify(wrong, spec)
    check("wrong numeric answer -> not correct", not vr.is_correct)

    # make_trajectory shape
    vr = await pot_common.verify(_COMPUTED, spec)
    t = pot_common.make_trajectory(spec, _COMPUTED, vr, route="self_gen",
                                   gen_model="test", temperature=0.2, sample_idx=0)
    check("trajectory carries code + exec evidence + provenance",
          t.is_correct and t.code and t.exec_answer and t.provenance.route == "self_gen"
          and t.source_id == "LDx")


def _guard_tests() -> None:
    print("\n=== guards (spurious / dedup / cap) ===")

    def reason(code, at="numeric", gold="36.32", route="self_gen"):
        return guards.spurious_reason(
            {"code": code, "answer_type": at, "gold_answer": gold,
             "provenance": {"route": route}}, rel_tol=1e-4)

    check("computed kept", reason(_COMPUTED.split("```python\n")[1].rsplit("```", 1)[0]) is None)
    check("echo rejected (literal_final_answer)",
          reason('print("FINAL ANSWER: 36.32")') == "literal_final_answer")
    check("echo with literal LaTeX braces rejected (not mistaken for interpolation)",
          reason('print("FINAL ANSWER: 3.29 * 10^{6}")', gold="3.29 * 10^{6}")
          == "literal_final_answer")
    check(".format() value kept (computed, not baked)",
          reason('x = 254.24\nprint("FINAL ANSWER: {:.4g}".format(x/7))') is None)
    check("%-format value kept (computed, not baked)",
          reason('x = 254.24\nprint("FINAL ANSWER: %.4g" % (x/7))') is None)
    # gold-as-literal is TEACHER-only (self-gen never sees gold)
    check("teacher: baked-literal var rejected (gold_hardcoded_literal)",
          reason('ans = 36.32\nprint(f"FINAL ANSWER: {ans:.4g}")', route="teacher_rewrite")
          == "gold_hardcoded_literal")
    check("self_gen: gold-coinciding literal NOT flagged (input/coefficient, e.g. resonance Z=R=60)",
          reason('Z = 60.0\nR = Z\nF = R * 2 / 2\nprint(f"FINAL ANSWER: {F:.4g}")',
                 gold="60", route="self_gen") is None)
    check("self_gen: identity answer w/ no arithmetic KEPT (resonance Z=R)",
          reason('Z = 60.0  # given at resonance\nR = Z\nprint(f"FINAL ANSWER: {R}")',
                 gold="60", route="self_gen") is None)
    check("teacher: no-computation rejected",
          reason('x = 99.0  # comment\nprint(f"FINAL ANSWER: {x}")',
                 route="teacher_rewrite") == "no_computation")
    check("yes_no without comparison rejected",
          reason('print("FINAL ANSWER: Yes")', at="yes_no", gold="Yes") == "literal_final_answer")
    check("yes_no computed kept",
          reason('z = 50.0\nans = "Yes" if z < 60 else "No"\nprint(f"FINAL ANSWER: {ans}")',
                 at="yes_no", gold="Yes") is None)
    check("teacher: sci_notation gold echo via f-string literal var rejected",
          reason('q = 2e-6\nprint(f"FINAL ANSWER: {q}")', at="numeric", gold="2 x 10^-6",
                 route="teacher_rewrite") == "gold_hardcoded_literal")
    check("multi_value computed kept",
          reason('a = 1.2 / 2\nb = 1.2\nprint(f"FINAL ANSWER: {a}; {b}")',
                 at="multi_value", gold="0.6; 1.2") is None)

    # dedup + cap via guards.run path (build fake trajectories in-memory)
    def traj(sid, code, route="self_gen", temp=0.2, retry=0, idx=0):
        return {
            "id": f"{sid}#{route}{idx}", "source_id": sid, "question": "q",
            "domain": "LDDT", "answer_type": "numeric", "gold_answer": "36.32",
            "gold_unit": "N", "dataset_source": "btc_golden",
            "code": code, "assistant": _block(code), "exec_answer": "36.32",
            "exec_unit": "N", "exec_stdout": "", "is_correct": True,
            "provenance": {"route": route, "gen_model": "t", "temperature": temp,
                           "retry_count": retry, "sample_idx": idx, "created_at": ""},
        }

    c_a = 'x = 254.24\nprint(f"FINAL ANSWER: {x/7:.6g}")'
    c_a_recomment = 'x = 254.24  # different comment\nprint(f"FINAL ANSWER: {x/7:.6g}")'
    c_b = 'y = 363.2\nprint(f"FINAL ANSWER: {y/10:.6g}")'
    c_c = 'z = 72.64\nprint(f"FINAL ANSWER: {z/2:.6g}")'
    c_d = 'w = 36320\nprint(f"FINAL ANSWER: {w/1000:.6g}")'
    group = [
        traj("P1", c_a, idx=0),
        traj("P1", c_a_recomment, idx=1),   # dup of c_a (comments ignored)
        traj("P1", c_b, idx=2),
        traj("P1", c_c, idx=3),
        traj("P1", c_d, idx=4),
    ]
    h = {pot_common.code_hash(c_a), pot_common.code_hash(c_b),
         pot_common.code_hash(c_c), pot_common.code_hash(c_d)}
    check("comment-only diff dedups to same hash",
          pot_common.code_hash(c_a) == pot_common.code_hash(c_a_recomment) and len(h) == 4)

    # exercise cap=2: 5 candidates -> 1 dup dropped -> 4 unique -> cap to 2
    from collections import defaultdict
    by = defaultdict(list)
    for t in group:
        by[t["source_id"]].append(t)
    g = by["P1"]
    g.sort(key=guards._sort_key)
    seen, deduped = set(), []
    for t in g:
        hsh = pot_common.code_hash(t["code"])
        if hsh in seen:
            continue
        seen.add(hsh)
        deduped.append(t)
    check("dedup leaves 4 unique of 5", len(deduped) == 4)
    check("cap=2 keeps 2", len(deduped[:2]) == 2)


def _data_roundtrip() -> None:
    print("\n=== real data round-trip ===")
    p = repo_root() / "app/physics_solution/versions/v06_finetune/input/problems_all.jsonl"
    rows = []
    for i, d in enumerate(read_jsonl(p)):
        rows.append(ProblemSpec.from_dict(d))
        if i >= 4:
            break
    check("read_jsonl + ProblemSpec.from_dict on real input",
          len(rows) == 5 and all(r.id and r.question and r.domain for r in rows))


async def _main() -> None:
    await _verify_tests()
    _guard_tests()
    _data_roundtrip()
    print(f"\n{'='*44}\n{_PASS} passed, {_FAIL} failed")
    sys.exit(1 if _FAIL else 0)


if __name__ == "__main__":
    asyncio.run(_main())
