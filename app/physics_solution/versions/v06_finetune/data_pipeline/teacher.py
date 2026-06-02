"""Phase-2 Route-2/3: DeepSeek-pro teacher for the self-gen residual.

RUNS WHERE DEEPSEEK_API_KEY LIVES (the user copies app/physics_solution/.env to
Vast, so it runs on Vast next to self-gen; it also runs local). It executes the
generated Python locally in-process -- no GPU needed.

Only the residual that Qwen could NOT solve (`selfgen_residual.jsonl`) reaches
here. Keeping the teacher confined to the residual is deliberate: distilling a
much larger model (DeepSeek >> 4B) risks distribution shift / forgetting, so
on-policy self-gen stays primary and the teacher only backfills.

Uses the STRONG `deepseek-v4-pro` (config.COMMERCIAL_MODEL), NOT the flash model
used for Phase-1 filter/translate. The teacher is given the gold answer as a
verification target plus any solution sketch (BTC cot / Vietjack vn_solution) and
Qwen's failed attempt -- but it is told to COMPUTE, not hardcode; `guards.py`
rejects echoes regardless. v1 "rewrite" shortcut: a full fresh trajectory rather
than fiddly prefix-splicing (route = teacher_rewrite).

Same execution gate as self-gen (`pot_common.verify`); retry up to --max-retries
with the error fed back. Auto-saves every 50 and resumes.

Run (needs DEEPSEEK_API_KEY in app/physics_solution/.env):
    PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.teacher
    PYTHONPATH=. python -m ...teacher --limit 20 --concurrency 8
"""

from __future__ import annotations

import argparse
import asyncio

from app.physics_solution.config import COMMERCIAL_MODEL, LANGSMITH_PROJECT, repo_root
from app.physics_solution.shared.runtime.tracing import setup_tracing
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client, pot_common
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec

IN_RESIDUAL = "app/physics_solution/versions/v06_finetune/output/selfgen_residual.jsonl"
OUT_TRAJ = "app/physics_solution/versions/v06_finetune/output/trajectories_teacher.jsonl"
OUT_FAILED = "app/physics_solution/versions/v06_finetune/output/teacher_failed.jsonl"


TEACHER_SYSTEM = """\
You are an expert physics solver. Write a self-contained Python script that solves
the problem and COMPUTES the answer from the given quantities.

RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- Define all given values at the top with SI unit conversions.
- Write the key formula as a comment before each computation.
- The script MUST print exactly two lines at the end:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute the relevant quantity, compare, and print "Yes" or "No".
- For multi_value: print values separated by semicolons.
- NEVER use e-notation in output. Write 2.97 * 10^6, not 2.97e6.
- Round numeric answers to 2-4 significant figures unless the problem specifies otherwise.

You are given the EXPECTED ANSWER only so you can self-check. Your code MUST derive
it from the physics -- do NOT hardcode or print the expected answer directly; a
script that just prints the number will be rejected."""


def _hint_block(spec: ProblemSpec) -> str:
    """Optional context for the teacher: prior solution sketch + Qwen's miss."""
    meta = spec.meta or {}
    parts: list[str] = []
    sketch = meta.get("cot") or meta.get("vn_solution")
    if sketch:
        parts.append(f"SOLUTION SKETCH (may contain the method; verify it):\n{str(sketch).strip()}")
    attempt = meta.get("qwen_attempt")
    if attempt:
        parts.append(f"A PREVIOUS ATTEMPT THAT FAILED (do not repeat its mistake):\n{str(attempt).strip()}")
    return ("\n\n".join(parts) + "\n\n") if parts else ""


def build_teacher_messages(spec: ProblemSpec) -> list[dict]:
    from app.physics_solution.versions.v05_best.formula_kb import get_formula_hints

    user = (
        f"DOMAIN: {spec.domain}\n"
        f"ANSWER TYPE: {spec.answer_type}\n\n"
        f"REFERENCE:\n{get_formula_hints(spec.domain)}\n\n"
        f"PROBLEM:\n{spec.question}\n\n"
        f"EXPECTED ANSWER (for self-check only): {spec.gold_answer} {spec.gold_unit}\n\n"
        f"{_hint_block(spec)}"
        f"Write a Python script that COMPUTES this answer and prints FINAL ANSWER / UNIT."
    )
    return [
        {"role": "system", "content": TEACHER_SYSTEM},
        {"role": "user", "content": user},
    ]


async def _solve(spec: ProblemSpec, client, args):
    """Try the teacher up to --max-retries+1 times. Return (Trajectory | None)."""
    messages = build_teacher_messages(spec)
    for attempt in range(args.max_retries + 1):
        temp = 0.0 if attempt == 0 else 0.3  # deterministic first, then diversify
        try:
            comp = await ds_client.complete(
                client, messages, model=args.model, temperature=temp,
                thinking_off=args.thinking_off,
            )
        except Exception as e:
            print(f"  [warn] teacher API failed for {spec.id} (attempt {attempt}): {e}")
            return None
        vr = await pot_common.verify(comp, spec)
        pot_common.trace_sample(
            spec, messages, temperature=temp, sample_idx=attempt, route="teacher_rewrite",
            retry_count=attempt, raw_completion=comp, vr=vr)
        if vr.is_correct:
            return pot_common.make_trajectory(
                spec, comp, vr, route="teacher_rewrite", gen_model=args.model,
                temperature=temp, retry_count=attempt, sample_idx=0)
        messages = messages + [
            {"role": "assistant", "content": comp},
            {"role": "user", "content": pot_common.error_feedback(vr.exec_result)},
        ]
    return None


async def _run(args) -> None:
    root = repo_root()
    setup_tracing(LANGSMITH_PROJECT, version="v06_teacher")
    in_path = root / IN_RESIDUAL
    traj_path, failed_path = root / OUT_TRAJ, root / OUT_FAILED

    if not in_path.exists():
        raise SystemExit(f"No residual file at {IN_RESIDUAL}. Run selfgen.py first.")
    specs = [ProblemSpec.from_dict(d) for d in pot_common.read_jsonl(in_path)]
    if args.limit:
        specs = specs[: args.limit]

    existing_traj = [] if args.fresh else pot_common.load_jsonl_if_exists(traj_path)
    existing_failed = [] if args.fresh else pot_common.load_jsonl_if_exists(failed_path)
    done = {t["source_id"] for t in existing_traj} | {r["id"] for r in existing_failed}
    todo = [s for s in specs if s.id not in done]
    print(f"Residual {len(specs)} | already done {len(done)} | to do {len(todo)} | model {args.model}")
    if not todo:
        print("Nothing to do (use --fresh to redo).")
        return

    client = ds_client.make_client()
    sem = asyncio.Semaphore(args.concurrency)
    lock = asyncio.Lock()
    new_traj: list[dict] = []
    new_failed: list[dict] = []
    n_done = 0

    async def worker(spec: ProblemSpec) -> None:
        nonlocal n_done
        async with sem:
            traj = await _solve(spec, client, args)
        async with lock:
            if traj is not None:
                new_traj.append(traj.to_dict())
            else:
                new_failed.append(spec.to_dict())
            n_done += 1
            if n_done % args.save_every == 0:
                pot_common.save_checkpoint(
                    traj_path, failed_path, existing_traj + new_traj, existing_failed + new_failed)
                print(f"  [checkpoint] {n_done}/{len(todo)} | solved {len(new_traj)} | "
                      f"failed {len(new_failed)}")

    await asyncio.gather(*(worker(s) for s in todo))
    pot_common.save_checkpoint(
        traj_path, failed_path, existing_traj + new_traj, existing_failed + new_failed)
    print(f"\nDone. Teacher solved {len(new_traj)}/{len(todo)} residual; {len(new_failed)} still failed.")
    print(f"Totals -> {len(existing_traj)+len(new_traj)} teacher trajectories; "
          f"{len(existing_failed)+len(new_failed)} unsolved ({OUT_FAILED}).")


def main() -> None:
    p = argparse.ArgumentParser(description="Route-2/3 teacher residual (deepseek-v4-pro)")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=8)
    p.add_argument("--model", default=COMMERCIAL_MODEL, help="strong teacher model (NOT flash)")
    p.add_argument("--max-retries", type=int, default=2, help="error-feedback retries")
    p.add_argument("--thinking", dest="thinking_off", action="store_false",
                   help="enable DeepSeek thinking (default: OFF — deepseek-v4-pro runs thinking-disabled)")
    p.add_argument("--fresh", action="store_true")
    p.add_argument("--save-every", type=int, default=50)
    p.set_defaults(thinking_off=True)
    args = p.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
