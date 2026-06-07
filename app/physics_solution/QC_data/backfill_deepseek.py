"""Backfill solve-code for the remaining stage-2 problems via DeepSeek — HARD CAP 2 ROUNDS.

The earlier QC (`run_qc.py`) used up to ~5 model calls per problem (K-sample solve + diagnose
+ confirm) — too slow/expensive. This is the lean "old flow": DeepSeek solves the problem with
the gold shown as a self-check target (teacher-style), we execute + score it, and we allow at
most **--max-rounds (default 2)** code-gen attempts (round 1 + one feedback retry). No diagnose
/ no fix stage. A problem unsolved within 2 rounds simply gets no hint (logged) — it stays CLEAN
in the dataset (these were already QC-judged CLEAN), just hint-less.

Verified code -> hint_pool.jsonl (hint_source:"deepseek"). Skips ids already in the pool (so the
41 Claude-done CH problems are NOT redone). Resumable + checkpointed; per-request + per-problem
timeouts so it can't hang. Echo/no-computation rejected via guards.spurious_reason.

    PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.backfill_deepseek --concurrency 16
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from app.physics_solution.config import COMMERCIAL_MODEL, repo_root
from app.physics_solution.QC_data.qc_filter import gold_leaked  # noqa: F401  (kept for parity/imports)
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client, guards, pot_common, teacher
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec, read_jsonl

PROBLEMS = "app/physics_solution/QC_data/gold/stage2_no_code.jsonl"
POOL = "app/physics_solution/QC_data/gold/hint_pool.jsonl"
UNSOLVED = "app/physics_solution/QC_data/gold/backfill_unsolved.jsonl"
_REL_TOL = 0.01


def _spurious(code: str, spec: dict) -> str | None:
    if spec.get("answer_type") == "text":
        return None
    traj = {"code": code, "answer_type": spec.get("answer_type", ""),
            "gold_answer": spec.get("gold_answer", ""), "provenance": {"route": "teacher_rewrite"}}
    return guards.spurious_reason(traj, _REL_TOL)


async def _complete(client, messages, args) -> str:
    last = None
    for attempt in range(3):
        try:
            return await ds_client.complete(client, messages, model=args.model,
                                            temperature=0.0, thinking_off=False, timeout=args.req_timeout)
        except Exception as e:
            last = e
            if attempt < 2:
                await asyncio.sleep(2 ** attempt)
    raise last  # type: ignore[misc]


async def _solve_capped(spec_dict: dict, client, args):
    """<= args.max_rounds gold-shown solve attempts. Returns (VerifyResult, rounds) on success,
    else (None, rounds_used). Round N>1 retries with feedback (exec error / wrong / hardcoded)."""
    spec = ProblemSpec.from_dict(spec_dict)
    msgs = teacher.build_teacher_messages(spec)
    for rnd in range(1, args.max_rounds + 1):
        comp = await _complete(client, msgs, args)
        vr = await pot_common.verify(comp, spec)
        spur = _spurious(vr.code or "", spec_dict) if vr.is_correct else None
        if vr.is_correct and spur is None:
            return vr, rnd
        if rnd < args.max_rounds:  # build feedback for the next (final) attempt
            if vr.exec_result is not None and not vr.exec_result.success:
                fb = pot_common.error_feedback(vr.exec_result)
            elif spur:
                fb = ("Your code did not actually COMPUTE the answer (it echoed/hardcoded it). "
                      "Re-derive it from the given quantities step by step, then print FINAL ANSWER / UNIT.")
            else:
                got = vr.exec_result.answer if vr.exec_result else None
                fb = (f"Your code ran and printed {got}, which does not match the expected answer. "
                      "Re-derive the physics and output one corrected Python code block.")
            msgs = msgs + [{"role": "assistant", "content": comp}, {"role": "user", "content": fb}]
    return None, args.max_rounds


async def _run(args) -> None:
    root = repo_root()
    specs = list(read_jsonl(root / args.problems))
    if args.limit:
        specs = specs[: args.limit]
    pool_path = root / args.pool
    pool = list(read_jsonl(pool_path)) if pool_path.exists() else []
    have = {r["id"] for r in pool}
    todo = [s for s in specs if s["id"] not in have]
    print(f"{len(specs)} stage-2 problems | in pool {len(have)} | to backfill {len(todo)} "
          f"| max_rounds={args.max_rounds} concurrency={args.concurrency}")
    if not todo:
        print("Nothing to do.")
        return

    client = ds_client.make_client()
    sem = asyncio.Semaphore(args.concurrency)
    lock = asyncio.Lock()
    new: list[dict] = []
    unsolved: list[dict] = []
    n_done = 0

    async def worker(s: dict) -> None:
        nonlocal n_done
        async with sem:
            try:
                vr, rounds = await asyncio.wait_for(_solve_capped(s, client, args), timeout=args.problem_timeout)
            except Exception:
                vr, rounds = None, 0
        async with lock:
            n_done += 1
            if vr is not None:
                new.append({"id": s["id"], "hint_source": "deepseek", "rounds": rounds,
                            "exec_answer": vr.exec_result.answer if vr.exec_result else None, "code": vr.code})
            else:
                unsolved.append({"id": s["id"], "answer_type": s.get("answer_type"),
                                 "gold_answer": s.get("gold_answer")})
            if n_done % args.save_every == 0:
                _write(pool_path, pool + new)
                _write(root / args.unsolved, unsolved)
                print(f"  [checkpoint] {n_done}/{len(todo)} | solved {len(new)} | unsolved {len(unsolved)}")

    await asyncio.gather(*(worker(s) for s in todo))
    _write(pool_path, pool + new)
    _write(root / args.unsolved, unsolved)
    print(f"\nDone. solved {len(new)}/{len(todo)} (unsolved {len(unsolved)} -> {args.unsolved}).")
    print(f"hint_pool now: {len(pool) + len(new)}")


def _write(path: Path, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main() -> None:
    p = argparse.ArgumentParser(description="DeepSeek backfill for stage-2 problems (hard 2-round cap)")
    p.add_argument("--problems", default=PROBLEMS)
    p.add_argument("--pool", default=POOL)
    p.add_argument("--unsolved", default=UNSOLVED)
    p.add_argument("--max-rounds", type=int, default=2, help="hard cap on code-gen attempts per problem")
    p.add_argument("--concurrency", type=int, default=16)
    p.add_argument("--model", default=COMMERCIAL_MODEL)
    p.add_argument("--req-timeout", type=float, default=90.0)
    p.add_argument("--problem-timeout", type=float, default=240.0)
    p.add_argument("--save-every", type=int, default=20)
    p.add_argument("--limit", type=int, default=None)
    args = p.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
