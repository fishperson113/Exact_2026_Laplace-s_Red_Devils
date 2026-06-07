"""Phase-2 Route-1: self-gen execution-verified PoT trajectories from Qwen.

RUNS ON THE GPU BOX (Vast AI) -- it samples Qwen 3.5 4B via the local vLLM
endpoint and executes the generated Python on the same machine (no cross-box
round trips). On-policy data is the highest-value SFT signal: it converges best
and forgets least, so this is the PRIMARY route. Whatever Qwen cannot solve here
falls through to the DeepSeek teacher (`teacher.py`).

Per problem:
  for temp in --temps:  request `n` completions  (total ~ --k)
      verify each (extract -> execute -> score vs gold)
      on EXECUTION ERROR: retry once with the stderr fed back (the v05 shape)
      keep every correct, distinct-code sample  (dedup by normalized-code hash)
  >= --min-keep correct -> append Trajectories to trajectories_selfgen.jsonl
  too few correct       -> ALSO append the ProblemSpec to selfgen_residual.jsonl, carrying
                           meta.qwen_attempt (a failed try) + meta.hint_code (the QC verified
                           solve) for the hinted route (`hinted.py`) to re-derive on-policy.

Qwen NEVER sees the gold answer -- that would defeat the on-policy / verification
point. Gold is used only by the scorer to gate. (The hinted route shows a reference
SOLUTION, not the gold value, and the gate still verifies Qwen's own output.)

Auto-saves every --save-every problems and resumes by skipping ids already in
either output file (re-run without --fresh). Interrupt-safe.

Run (on Vast, vLLM up on :18000):
    PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.selfgen
    PYTHONPATH=. python -m ...selfgen --limit 20 --concurrency 32     # smoke
Local (no GPU) orchestration test:
    PYTHONPATH=. .venv/bin/python -m ...selfgen --stub --limit 30
"""

from __future__ import annotations

import argparse
import asyncio

from app.physics_solution.config import LANGSMITH_PROJECT, repo_root
from app.physics_solution.shared.runtime.tracing import setup_tracing
from app.physics_solution.versions.v06_finetune.data_pipeline import pot_common, vllm_client
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec

# THE canonical clean dataset (1584 problems, each with an optional `hint_code`): the single
# source of truth for train+val. Do not reference any other dataset file. See v07 README.
INPUT = "app/physics_solution/versions/v06_finetune/input/self_gen_dataset.jsonl"
OUT_TRAJ = "app/physics_solution/versions/v06_finetune/output/trajectories_selfgen.jsonl"
OUT_RESIDUAL = "app/physics_solution/versions/v06_finetune/output/selfgen_residual.jsonl"

DEFAULT_TEMPS = [0.2, 0.5, 0.8, 1.0]


# --------------------------------------------------------------------------- stub

def _stub_completion(spec: ProblemSpec, broken: bool) -> str:
    """Canned completion for GPU-free local testing of the orchestration.

    `broken` -> code that errors (exercises the retry + residual path); otherwise
    code that prints the gold string verbatim (verify passes -> exercises the keep
    path). The echo has no arithmetic, so it would be rejected later by guards --
    which is fine: --stub only tests selfgen's loop/checkpoint/resume, not data quality.
    """
    if broken:
        return "```python\nprint(this_is_undefined)\n```"
    ans = spec.gold_answer.replace('"', "'")
    unit = (spec.gold_unit or "-").replace('"', "'")
    return f'```python\nprint("FINAL ANSWER: {ans}")\nprint("UNIT: {unit}")\n```'


# --------------------------------------------------------------------------- per-problem

async def _sample(client, messages, *, args, temperature, n):
    """vLLM sample, or canned stub completions. Returns list[str] (never raises)."""
    if args.stub:
        return []  # handled directly in _process_problem for stub mode
    try:
        return await vllm_client.sample(
            client, messages, model=args.model, temperature=temperature,
            n=n, max_tokens=args.max_tokens, timeout=args.req_timeout,
        )
    except Exception as e:  # transport / API error -> no samples this temp
        print(f"  [warn] sample failed (T={temperature}): {e}")
        return []


async def _process_problem(spec: ProblemSpec, client, args):
    """Return (kept: list[Trajectory], residual_dict | None)."""
    # ---- stub mode: deterministic, no network --------------------------------
    if args.stub:
        broken = (hash(spec.id) % 5 == 0)
        comp = _stub_completion(spec, broken)
        vr = await pot_common.verify(comp, spec)
        if vr.is_correct:
            t = pot_common.make_trajectory(
                spec, comp, vr, route="self_gen", gen_model="stub",
                temperature=0.0, retry_count=0, sample_idx=0)
            return [t], None
        return [], _residual(spec, comp)

    # ---- real self-gen -------------------------------------------------------
    messages = pot_common.build_gen_messages(spec)
    kept = []
    seen = set()
    best_failed = None
    idx = 0
    s_no = 0  # per-sample counter for the trace (counts every sample, kept or not)
    n_per = max(1, args.k // max(1, len(args.temps)))

    for temp in args.temps:
        completions = await _sample(client, messages, args=args, temperature=temp, n=n_per)
        for comp in completions:
            vr = await pot_common.verify(comp, spec)
            used_comp, used_vr, retry = comp, vr, 0

            # retry ONCE on execution error (not on a wrong-but-running answer)
            if (not vr.is_correct and vr.exec_result is not None
                    and not vr.exec_result.success):
                retry_msgs = messages + [
                    {"role": "assistant", "content": comp},
                    {"role": "user", "content": pot_common.error_feedback(vr.exec_result)},
                ]
                retry_comps = await _sample(client, retry_msgs, args=args, temperature=temp, n=1)
                if retry_comps:
                    rv = await pot_common.verify(retry_comps[0], spec)
                    if rv.is_correct:
                        used_comp, used_vr, retry = retry_comps[0], rv, 1

            pot_common.trace_sample(
                spec, messages, temperature=temp, sample_idx=s_no, route="self_gen",
                retry_count=retry, raw_completion=used_comp, vr=used_vr)
            s_no += 1

            if used_vr.is_correct:
                h = pot_common.code_hash(used_vr.code or "")
                if h not in seen:
                    seen.add(h)
                    kept.append(pot_common.make_trajectory(
                        spec, used_comp, used_vr, route="self_gen", gen_model=args.model,
                        temperature=temp, retry_count=retry, sample_idx=idx))
                    idx += 1
            elif best_failed is None and comp.strip():
                best_failed = comp

    # Route to the hinted residual when Qwen found TOO FEW correct samples (default <1, i.e.
    # only on 0 correct; raise --min-keep to also top up problems with very few). The kept
    # samples are still emitted; the hinted route adds more (guards then caps per problem).
    if len(kept) >= args.min_keep:
        return kept, None
    return kept, _residual(spec, best_failed)


def _residual(spec: ProblemSpec, qwen_attempt: str | None) -> dict:
    """ProblemSpec dict + one failed Qwen attempt, for the teacher route."""
    d = spec.to_dict()
    d["meta"] = dict(spec.meta or {}, qwen_attempt=qwen_attempt or "")
    return d


# --------------------------------------------------------------------------- driver

async def _run(args) -> None:
    root = repo_root()
    if not args.stub:
        setup_tracing(LANGSMITH_PROJECT, version="v06_selfgen")
    in_path = root / args.input
    traj_path, res_path = root / OUT_TRAJ, root / OUT_RESIDUAL

    specs = []
    for d in pot_common.read_jsonl(in_path):
        s = ProblemSpec.from_dict(d)
        if d.get("hint_code"):  # carry the QC hint into meta for the hinted residual route
            s.meta = dict(s.meta or {}, hint_code=d["hint_code"], hint_source=d.get("hint_source"))
        specs.append(s)
    if args.limit:
        specs = specs[: args.limit]

    existing_traj = [] if args.fresh else pot_common.load_jsonl_if_exists(traj_path)
    existing_res = [] if args.fresh else pot_common.load_jsonl_if_exists(res_path)
    done = {t["source_id"] for t in existing_traj} | {r["id"] for r in existing_res}
    todo = [s for s in specs if s.id not in done]
    print(f"Loaded {len(specs)} problems | already done {len(done)} | to do {len(todo)}")
    print(f"K={args.k} temps={args.temps} concurrency={args.concurrency} "
          f"model={'STUB' if args.stub else args.model}")
    if not todo:
        print("Nothing to do (use --fresh to redo).")
        return

    client = None if args.stub else vllm_client.make_client(args.base_url)
    if client is not None and not await vllm_client.is_alive(client):
        raise SystemExit(
            f"vLLM endpoint not reachable at {args.base_url or vllm_client.default_base_url()}. "
            "Is the template up? (curl :18000/v1/models)")

    sem = asyncio.Semaphore(args.concurrency)
    lock = asyncio.Lock()
    new_traj: list[dict] = []
    new_res: list[dict] = []
    n_done = 0
    n_solved = 0

    async def worker(spec: ProblemSpec) -> None:
        nonlocal n_done, n_solved
        async with sem:
            kept, residual = await _process_problem(spec, client, args)
        async with lock:
            for t in kept:
                new_traj.append(t.to_dict())
            if residual is not None:
                new_res.append(residual)
            else:
                n_solved += 1
            n_done += 1
            if n_done % args.save_every == 0:
                pot_common.save_checkpoint(
                    traj_path, res_path, existing_traj + new_traj, existing_res + new_res)
                print(f"  [checkpoint] {n_done}/{len(todo)} problems | "
                      f"solved {n_solved} | {len(new_traj)} trajectories | "
                      f"residual {len(new_res)}")

    await asyncio.gather(*(worker(s) for s in todo))
    pot_common.save_checkpoint(
        traj_path, res_path, existing_traj + new_traj, existing_res + new_res)

    total_traj = len(existing_traj) + len(new_traj)
    total_res = len(existing_res) + len(new_res)
    print(f"\nDone. This run: {n_solved}/{len(todo)} problems solved by self-gen, "
          f"{len(new_traj)} new trajectories.")
    print(f"Totals -> {total_traj} trajectories ({OUT_TRAJ}); "
          f"{total_res} residual ({OUT_RESIDUAL}).")


def main() -> None:
    p = argparse.ArgumentParser(description="Route-1 self-gen PoT trajectories (Qwen via vLLM)")
    p.add_argument("--input", default=INPUT, help="ProblemSpec JSONL to read (default: problems_all)")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=32)
    p.add_argument("--k", type=int, default=8, help="total samples per problem (spread over temps)")
    p.add_argument("--min-keep", type=int, default=1,
                   help="route to the hinted residual when fewer than this many correct "
                        "samples were kept (default 1 = only on 0 correct)")
    p.add_argument("--temps", type=float, nargs="+", default=DEFAULT_TEMPS)
    p.add_argument("--base-url", default=None, help="vLLM base url (default env VLLM_BASE_URL / :18000)")
    p.add_argument("--model", default=None, help="served model id (default env VLLM_MODEL)")
    p.add_argument("--max-tokens", type=int, default=2000)
    p.add_argument("--req-timeout", type=float, default=120.0, help="per-request timeout (s)")
    p.add_argument("--save-every", type=int, default=50)
    p.add_argument("--fresh", action="store_true", help="ignore existing output and redo")
    p.add_argument("--stub", action="store_true", help="no GPU; canned completions (orchestration test)")
    args = p.parse_args()
    if args.model is None and not args.stub:
        args.model = vllm_client.default_model()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
