"""Phase-2 hinted self-gen — the residual route, NO API at generation time.

Replaces the old DeepSeek teacher. For problems plain self-gen (`selfgen.py`) could NOT
solve (or solved too few times), we now show **Qwen** a verified REFERENCE SOLUTION (the QC
`hint_code`, carried in `selfgen_residual.jsonl` meta) and let Qwen re-derive ITS OWN
reasoning + code. The execution gate still verifies the output, so what lands in the SFT set
is Qwen's on-policy work — just guided. This is the "truly teach" idea: the model learns to
produce the right result itself, so the SFT data stays on-distribution (less forgetting /
domain shift than distilling a much larger model's code directly).

Runs on the GPU box (Qwen via the local vLLM endpoint), same as selfgen — NOT DeepSeek.
The shown hint is external-model data (DeepSeek/Claude): provenance.route="self_gen_hinted"
and provenance.hint_source flag it for the Data Disclosure Document. The gold value is never
shown (only a solution method); guards still reject echoes/hardcoding.

Run (on Vast, vLLM up on :18000, after selfgen.py produced the residual):
    PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.hinted
    PYTHONPATH=. python -m ...hinted --concurrency 32
"""

from __future__ import annotations

import argparse
import asyncio

from app.physics_solution.config import LANGSMITH_PROJECT, repo_root
from app.physics_solution.shared.runtime.tracing import setup_tracing
from app.physics_solution.versions.v06_finetune.data_pipeline import pot_common, vllm_client
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import ProblemSpec

IN_RESIDUAL = "app/physics_solution/versions/v06_finetune/output/selfgen_residual.jsonl"
OUT_TRAJ = "app/physics_solution/versions/v06_finetune/output/trajectories_hinted.jsonl"
OUT_FAILED = "app/physics_solution/versions/v06_finetune/output/hinted_failed.jsonl"

DEFAULT_TEMPS = [0.5, 0.8, 1.0]  # a bit hotter than plain self-gen — diversify around the hint


async def _sample(client, messages, *, args, temperature, n):
    try:
        return await vllm_client.sample(
            client, messages, model=args.model, temperature=temperature,
            n=n, max_tokens=args.max_tokens, timeout=args.req_timeout)
    except Exception as e:
        print(f"  [warn] sample failed (T={temperature}): {e}")
        return []


async def _process_problem(spec: ProblemSpec, client, args):
    """Return (kept: list[Trajectory], failed_dict | None). Needs a hint to run."""
    meta = spec.meta or {}
    hint, hint_source = meta.get("hint_code"), meta.get("hint_source", "")
    if not hint:
        return [], spec.to_dict()  # no reference solve -> can't hint this one

    messages = pot_common.build_hinted_messages(spec)
    kept, seen = [], set()
    idx = s_no = 0
    n_per = max(1, args.k // max(1, len(args.temps)))

    for temp in args.temps:
        for comp in await _sample(client, messages, args=args, temperature=temp, n=n_per):
            vr = await pot_common.verify(comp, spec)
            used_comp, used_vr, retry = comp, vr, 0
            if (not vr.is_correct and vr.exec_result is not None
                    and not vr.exec_result.success):
                retry_comps = await _sample(
                    client,
                    messages + [{"role": "assistant", "content": comp},
                                {"role": "user", "content": pot_common.error_feedback(vr.exec_result)}],
                    args=args, temperature=temp, n=1)
                if retry_comps:
                    rv = await pot_common.verify(retry_comps[0], spec)
                    if rv.is_correct:
                        used_comp, used_vr, retry = retry_comps[0], rv, 1

            pot_common.trace_sample(
                spec, messages, temperature=temp, sample_idx=s_no, route="self_gen_hinted",
                retry_count=retry, raw_completion=used_comp, vr=used_vr)
            s_no += 1

            if used_vr.is_correct:
                h = pot_common.code_hash(used_vr.code or "")
                if h not in seen:
                    seen.add(h)
                    kept.append(pot_common.make_trajectory(
                        spec, used_comp, used_vr, route="self_gen_hinted", gen_model=args.model,
                        temperature=temp, retry_count=retry, sample_idx=idx, hint_source=hint_source))
                    idx += 1

    if kept:
        return kept, None
    return [], spec.to_dict()


async def _run(args) -> None:
    root = repo_root()
    setup_tracing(LANGSMITH_PROJECT, version="v06_hinted")
    in_path = root / IN_RESIDUAL
    traj_path, failed_path = root / OUT_TRAJ, root / OUT_FAILED
    if not in_path.exists():
        raise SystemExit(f"No residual at {IN_RESIDUAL}. Run selfgen.py first.")

    specs = [ProblemSpec.from_dict(d) for d in pot_common.read_jsonl(in_path)]
    if args.limit:
        specs = specs[: args.limit]

    existing_traj = [] if args.fresh else pot_common.load_jsonl_if_exists(traj_path)
    existing_failed = [] if args.fresh else pot_common.load_jsonl_if_exists(failed_path)
    done = {t["source_id"] for t in existing_traj} | {r["id"] for r in existing_failed}
    todo = [s for s in specs if s.id not in done]
    n_hint = sum(1 for s in todo if (s.meta or {}).get("hint_code"))
    print(f"Residual {len(specs)} | done {len(done)} | to do {len(todo)} ({n_hint} have a hint)")
    if not todo:
        print("Nothing to do (use --fresh to redo).")
        return

    client = vllm_client.make_client(args.base_url)
    if not await vllm_client.is_alive(client):
        raise SystemExit(f"vLLM not reachable at {args.base_url or vllm_client.default_base_url()}.")

    sem = asyncio.Semaphore(args.concurrency)
    lock = asyncio.Lock()
    new_traj: list[dict] = []
    new_failed: list[dict] = []
    n_done = 0

    async def worker(spec: ProblemSpec) -> None:
        nonlocal n_done
        async with sem:
            kept, failed = await _process_problem(spec, client, args)
        async with lock:
            for t in kept:
                new_traj.append(t.to_dict())
            if failed is not None:
                new_failed.append(failed)
            n_done += 1
            if n_done % args.save_every == 0:
                pot_common.save_checkpoint(
                    traj_path, failed_path, existing_traj + new_traj, existing_failed + new_failed)
                print(f"  [checkpoint] {n_done}/{len(todo)} | "
                      f"{len(new_traj)} hinted trajectories | failed {len(new_failed)}")

    await asyncio.gather(*(worker(s) for s in todo))
    pot_common.save_checkpoint(
        traj_path, failed_path, existing_traj + new_traj, existing_failed + new_failed)
    print(f"\nDone. Hinted route added {len(new_traj)} trajectories; {len(new_failed)} still unsolved.")
    print(f"Totals -> {len(existing_traj)+len(new_traj)} ({OUT_TRAJ}); "
          f"{len(existing_failed)+len(new_failed)} unsolved ({OUT_FAILED}).")


def main() -> None:
    p = argparse.ArgumentParser(description="Phase-2 hinted self-gen (Qwen via vLLM, no API)")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=32)
    p.add_argument("--k", type=int, default=6, help="total samples per problem (spread over temps)")
    p.add_argument("--temps", type=float, nargs="+", default=DEFAULT_TEMPS)
    p.add_argument("--base-url", default=None, help="vLLM base url (default env VLLM_BASE_URL / :18000)")
    p.add_argument("--model", default=None, help="served model id (default env VLLM_MODEL)")
    p.add_argument("--max-tokens", type=int, default=2000)
    p.add_argument("--req-timeout", type=float, default=120.0)
    p.add_argument("--save-every", type=int, default=50)
    p.add_argument("--fresh", action="store_true")
    args = p.parse_args()
    if args.model is None:
        args.model = vllm_client.default_model()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
