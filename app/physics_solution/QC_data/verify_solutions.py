"""Verify CLAUDE's full QC of the 278 stage-2 problems — CLEAN / FIX / DROP, NO API.

Same execution-grounded contract as the DeepSeek QC (`run_qc.py`), but **Claude** (the agent
in another chat) is the solver/judge instead of the DeepSeek API, so it costs no budget.
Claude MAY look at the gold (it's the check target / the signal for diagnosing a corruption),
exactly like DeepSeek's diagnose stage.

Per problem Claude writes one line in `gold/claude_solutions.jsonl`:
    {"id","verdict":"CLEAN","code":"<python>","reason":"..."}
    {"id","verdict":"FIX","fixed_question":"<corrected statement>","code":"<python>","reason":"OCR ..."}
    {"id","verdict":"DROP","reason":"missing data / not computable"}

This harness then checks each (NO network):
  CLEAN -> code must solve the ORIGINAL statement to gold.
  FIX   -> code must solve the FIXED statement to gold; the fix must not leak the gold value.
  DROP  -> recorded as-is (no code).
  + guards.spurious_reason rejects echo / no-computation / yes_no-without-comparison
    (skipped for answer_type=text). Verified code -> hint_pool.jsonl; verdicts ->
    claude_verdicts.jsonl; failures -> verify_failed.jsonl (revise & re-run, resumable).

The FIX/DROP verdicts are applied to the dataset in Task B of STAGE2_BACKFILL_HANDOFF.md
(FIX -> corrected question; DROP -> excluded). Note: because Claude sees gold while solving,
CLEAN/FIX here are "teacher-mode" verified (the guard + gold-leak check are the backstops),
not gold-blind like DeepSeek's stage-1 — fine for a fallback hint pool.

    PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.verify_solutions
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from app.physics_solution.config import repo_root
from app.physics_solution.QC_data.qc_filter import gold_leaked
from app.physics_solution.versions.v06_finetune.data_pipeline import guards, pot_common
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec, read_jsonl

PROBLEMS = "app/physics_solution/QC_data/gold/stage2_no_code.jsonl"
SOLUTIONS = "app/physics_solution/QC_data/gold/claude_solutions.jsonl"
POOL = "app/physics_solution/QC_data/gold/hint_pool.jsonl"
VERDICTS = "app/physics_solution/QC_data/gold/claude_verdicts.jsonl"
FAILED = "app/physics_solution/QC_data/gold/verify_failed.jsonl"
_REL_TOL = 0.01


def _spurious(code: str, spec: dict) -> str | None:
    """Reject echo / no-computation / yes_no-without-comparison (skip for text answers)."""
    if spec.get("answer_type") == "text":
        return None
    traj = {"code": code, "answer_type": spec.get("answer_type", ""),
            "gold_answer": spec.get("gold_answer", ""),
            "provenance": {"route": "teacher_rewrite"}}  # Claude saw gold -> teacher-strength guard
    return guards.spurious_reason(traj, _REL_TOL)


async def verify_one(spec_dict: dict, code: str) -> "pot_common.VerifyResult":
    """Execute + score one candidate `code` against the problem's gold (no API)."""
    spec = ProblemSpec.from_dict(spec_dict)
    return await pot_common.verify(f"```python\n{code}\n```", spec)


def _write(path: Path, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


async def _run(args) -> None:
    root = repo_root()
    specs = {s["id"]: s for s in read_jsonl(root / args.problems)}
    sols = list(read_jsonl(root / args.solutions)) if (root / args.solutions).exists() else []
    pool = list(read_jsonl(root / args.pool)) if (root / args.pool).exists() else []
    verdicts = list(read_jsonl(root / args.verdicts)) if (root / args.verdicts).exists() else []
    done = {v["id"] for v in verdicts}

    todo = [s for s in sols if s.get("id") in specs and s["id"] not in done]
    have_stage2 = {v["id"] for v in verdicts} & set(specs)
    print(f"solutions {len(sols)} | stage-2 problems {len(specs)} | "
          f"already judged {len(have_stage2)} | to check {len(todo)}")
    if not todo:
        print("Nothing to check (write into claude_solutions.jsonl, or all done).")
        return

    sem = asyncio.Semaphore(args.concurrency)
    lock = asyncio.Lock()
    new_verdicts: list[dict] = []
    new_hints: list[dict] = []
    failed: list[dict] = []

    async def worker(sol: dict) -> None:
        spec = specs[sol["id"]]
        v = str(sol.get("verdict", "")).upper()

        if v == "DROP":
            async with lock:
                new_verdicts.append({"id": sol["id"], "verdict": "DROP",
                                     "fixed_question": None, "reason": sol.get("reason", "")})
            return

        if v not in ("CLEAN", "FIX") or not sol.get("code"):
            async with lock:
                failed.append({"id": sol["id"], "reject": "bad_record (need verdict+code)", "code": sol.get("code")})
            return

        fixed_q = (sol.get("fixed_question") or "").strip() if v == "FIX" else None
        if v == "FIX":
            if not fixed_q:
                async with lock:
                    failed.append({"id": sol["id"], "reject": "fix_no_question", "code": sol.get("code")})
                return
            if gold_leaked(spec.get("gold_answer", ""), fixed_q, spec.get("question", "")):
                async with lock:
                    failed.append({"id": sol["id"], "reject": "fix_leaked_gold", "code": sol.get("code")})
                return

        check_spec = {**spec, "question": fixed_q} if v == "FIX" else spec
        async with sem:
            vr = await verify_one(check_spec, sol["code"])
        spur = _spurious(vr.code or "", spec) if vr.is_correct else None

        async with lock:
            if vr.is_correct and spur is None:
                new_verdicts.append({"id": sol["id"], "verdict": v,
                                     "fixed_question": fixed_q, "reason": sol.get("reason", "")})
                new_hints.append({"id": sol["id"], "hint_source": "claude", "verdict": v,
                                  "exec_answer": vr.exec_result.answer if vr.exec_result else None,
                                  "code": vr.code})
            else:
                res = vr.exec_result
                failed.append({"id": sol["id"], "verdict": v, "answer_type": spec.get("answer_type"),
                               "gold_answer": spec.get("gold_answer"),
                               "exec_answer": (res.answer if res else None),
                               "reject": spur or ("wrong_answer" if (res and res.success) else "exec_error"),
                               "error": (res.stderr.strip()[:400] if (res and not res.success) else None),
                               "code": sol["code"]})

    await asyncio.gather(*(worker(s) for s in todo))

    _write(root / args.verdicts, verdicts + new_verdicts)
    _write(root / args.pool, pool + new_hints)
    _write(root / args.failed, failed)

    from collections import Counter
    split = Counter(v["verdict"] for v in verdicts + new_verdicts)
    covered = len({v["id"] for v in verdicts + new_verdicts} & set(specs))
    print(f"\nAccepted this run: {len(new_verdicts)} (failed {len(failed)})")
    print(f"Verdict split so far: {dict(split)}")
    print(f"hint_pool now: {len(pool) + len(new_hints)}  |  failures -> {args.failed} (revise & re-run)")
    print(f"Coverage: {covered}/{len(specs)} stage-2 problems judged ({len(specs) - covered} left).")


def main() -> None:
    p = argparse.ArgumentParser(description="Verify Claude's CLEAN/FIX/DROP for the stage-2 problems (no API)")
    p.add_argument("--problems", default=PROBLEMS)
    p.add_argument("--solutions", default=SOLUTIONS)
    p.add_argument("--pool", default=POOL)
    p.add_argument("--verdicts", default=VERDICTS)
    p.add_argument("--failed", default=FAILED)
    p.add_argument("--concurrency", type=int, default=8)
    args = p.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
