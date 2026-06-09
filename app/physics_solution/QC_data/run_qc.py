"""Driver: execution-grounded content-QC of the v06 SFT input (BTC + Vietjack).

Unlike a judgment-only pass, every verdict is backed by CODE THAT RAN. Per problem:

  Stage 1  DeepSeek solves the problem AS WRITTEN (gold-free prompt) -> we execute the
           code (pot_common.verify, the same local sandbox + scorer as Phase-2) and
           compare to gold.  match -> CLEAN  (+ a verified solve kept as bonus teacher data)
  Stage 2  on a mismatch, DeepSeek is shown the gold + the failed attempt and diagnoses
           FIX (repair a corrupted number/symbol/unit, return the corrected statement) or
           DROP (unrepairable / would require guessing intent / gold itself looks wrong)
  Stage 3  a proposed FIX is CONFIRMED by re-solving the corrected statement gold-free;
           it is accepted only if it now computes to gold, else DROP (fix_unconfirmed)

The solver never sees gold, so a CLEAN/FIX is genuine (the text really computes gold).
DeepSeek runs are thinking-ON by default (solving + diagnosing need reasoning).

Outputs (in --out-dir, default gold/):
  qc_verdicts.jsonl  full per-problem record incl. the verified solve code (resume cache)
  problems_qc.jsonl  cleaned set = CLEAN + FIX (FIX carries the corrected `question`)
  qc_dropped.jsonl   DROP audit
  qc_report.md       counts (verdict x source x domain x error_type)

Run (lean venv with `openai`; DEEPSEEK_API_KEY in app/physics_solution/.env):
    PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --source vietjack --concurrency 12
    PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --concurrency 16      # full
    PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --selftest            # offline
Resumable: re-run skips ids already in qc_verdicts.jsonl; errored ids are not cached.
"""

from __future__ import annotations

import argparse
import asyncio
from collections import Counter
from pathlib import Path

from app.physics_solution.config import COMMERCIAL_MODEL, repo_root
from app.physics_solution.QC_data import qc_filter
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client, pot_common
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import (
    ProblemSpec,
    read_jsonl,
    write_jsonl,
)

INPUT = "app/physics_solution/versions/v06_finetune/input/problems_all.jsonl"
OUT_DIR = "app/physics_solution/QC_data/gold"
_SOURCE_MAP = {"btc": "btc_golden", "vietjack": "vietjack"}

# Stage-1 / stage-3 sample temps: a clean problem the solver fumbles at T=0 may still
# solve at a higher temp, so any match -> CLEAN (short-circuits on first success).
SOLVE_TEMPS = (0.0, 0.5)


def _load(path: Path) -> list[dict]:
    return list(read_jsonl(path)) if path.exists() else []


# --------------------------------------------------------------------------- model calls

async def _complete(client, messages, args, *, temperature: float = 0.0, max_retries: int = 2) -> str:
    """ds_client.complete with a small backoff retry on transient API errors."""
    last = None
    for attempt in range(max_retries + 1):
        try:
            return await ds_client.complete(
                client, messages, model=args.model,
                temperature=temperature, thinking_off=args.no_thinking,
                timeout=args.req_timeout)
        except Exception as e:  # rate-limit / network
            last = e
            if attempt < max_retries:
                await asyncio.sleep(2 ** attempt)
    raise last  # type: ignore[misc]


async def _solve_k(spec_dict: dict, client, args, *, temps=SOLVE_TEMPS):
    """Up to len(temps) gold-free solve attempts; short-circuit on the first that hits gold.

    Returns the best (VerifyResult, completion), ranked correct > runs-but-wrong > errored,
    so a one-off solver slip (wrong constant, a code bug) doesn't masquerade as a broken
    statement — only a problem NO attempt can solve falls through to diagnosis.
    """
    spec = ProblemSpec.from_dict(spec_dict)
    msgs = qc_filter.build_solve_messages(spec_dict)
    best = None  # (rank, vr, comp)
    for t in temps:
        comp = await _complete(client, msgs, args, temperature=t)
        vr = await pot_common.verify(comp, spec)
        rank = 2 if vr.is_correct else (1 if (vr.exec_result is not None and vr.exec_result.success) else 0)
        if best is None or rank > best[0]:
            best = (rank, vr, comp)
        if vr.is_correct:
            break
    return best[1], best[2]


async def qc_one(spec_dict: dict, client, args) -> dict:
    """Run the 3-stage execution-grounded QC on one problem -> a verdict record."""
    base = {"id": spec_dict["id"]}

    # Stage 1 — solve as written (K samples) --------------------------------
    vr1, _ = await _solve_k(spec_dict, client, args)
    if vr1.is_correct:
        return {**base, "verdict": "CLEAN", "error_type": "none", "fixed_question": None,
                "reason": "solved as-written matches gold", "stage": 1,
                "solve_code": vr1.code,
                "solve_answer": vr1.exec_result.answer if vr1.exec_result else None}

    # Stage 2 — diagnose the mismatch (gold shown) --------------------------
    ran = vr1.exec_result is not None and vr1.exec_result.success
    a_code = vr1.code
    a_ans = vr1.exec_result.answer if ran else None
    a_err = (vr1.exec_result.stderr if (vr1.exec_result and not ran) else None)
    dcomp = await _complete(client, qc_filter.build_diagnose_messages(spec_dict, a_code, a_ans, a_err), args)
    diag = qc_filter.parse_diagnose(dcomp)

    if diag["verdict"] == "CLEAN":  # solver slipped, or answers differ only by rounding
        return {**base, "verdict": "CLEAN", "error_type": "none", "fixed_question": None,
                "reason": f"diagnosed clean: {diag['reason']}", "stage": 2}

    if diag["verdict"] == "FIX":
        fixed_q = (diag.get("fixed_question") or "").strip()
        if not fixed_q:
            return {**base, "verdict": "DROP", "error_type": "fix_empty", "fixed_question": None,
                    "reason": "FIX proposed without a fixed_question", "stage": 2}
        if qc_filter.gold_leaked(spec_dict.get("gold_answer", ""), fixed_q, spec_dict.get("question", "")):
            return {**base, "verdict": "DROP", "error_type": "fix_leaked_gold", "fixed_question": None,
                    "reason": "proposed fix injected the gold value into the statement", "stage": 2}
        # Stage 3 — confirm the fix by re-solving it gold-free ---------------
        vr3, _ = await _solve_k({**spec_dict, "question": fixed_q}, client, args)
        if vr3.is_correct:
            return {**base, "verdict": "FIX", "error_type": diag["error_type"], "fixed_question": fixed_q,
                    "reason": diag["reason"], "stage": 3, "fix_confirmed": True,
                    "solve_code": vr3.code,
                    "solve_answer": vr3.exec_result.answer if vr3.exec_result else None}
        return {**base, "verdict": "DROP", "error_type": "fix_unconfirmed", "fixed_question": fixed_q,
                "reason": f"fix did not compute to gold; {diag['reason']}", "stage": 3}

    return {**base, "verdict": "DROP", "error_type": diag["error_type"], "fixed_question": None,
            "reason": diag["reason"], "stage": 2}


# --------------------------------------------------------------------------- driver

def _write_report(path: Path, specs, kept, dropped, n_clean, n_fix, n_drop, n_err) -> None:
    fixes = [k for k in kept if (k.get("meta") or {}).get("qc_verdict") == "FIX"]
    by_fix_err = Counter((k.get("meta") or {}).get("qc_error_type", "?") for k in fixes)
    by_drop_err = Counter(d.get("qc_error_type", "?") for d in dropped)
    by_drop_src = Counter(d.get("dataset_source", "?") for d in dropped)
    by_drop_dom = Counter(d.get("domain", "?") for d in dropped)
    lines = [
        "# QC report (execution-grounded)", "",
        f"- input problems: **{len(specs)}**",
        f"- CLEAN **{n_clean}** | FIX **{n_fix}** | DROP **{n_drop}**"
        + (f" | error/pending {n_err}" if n_err else ""),
        f"- kept (CLEAN+FIX) -> `problems_qc.jsonl`: **{len(kept)}**",
        f"- fixed (review) -> `qc_fixed.jsonl`: **{n_fix}**",
        f"- dropped (review) -> `qc_dropped.jsonl`: **{len(dropped)}**", "",
        "## FIX by error_type", *[f"- {k}: {v}" for k, v in by_fix_err.most_common()], "",
        "## DROP by error_type", *[f"- {k}: {v}" for k, v in by_drop_err.most_common()], "",
        "## DROP by source", *[f"- {k}: {v}" for k, v in by_drop_src.most_common()], "",
        "## DROP by domain", *[f"- {k}: {v}" for k, v in by_drop_dom.most_common()], "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def _apply_verdicts(specs, vmap):
    """Map verdicts onto specs -> (kept, dropped, fixed, counts). `fixed` is the FIX audit
    (original vs corrected statement) so changes are reviewable."""
    kept, dropped, fixed = [], [], []
    n_clean = n_fix = n_drop = n_pending = 0
    for s in specs:
        v = vmap.get(s["id"])
        if v is None:  # errored / not yet processed -> keep flagged, retry on re-run
            s2 = dict(s); m = dict(s2.get("meta") or {}); m["qc_status"] = "error_pending"; s2["meta"] = m
            kept.append(s2); n_pending += 1
            continue
        k, d = qc_filter.apply_verdict(s, v)
        if d is not None:
            dropped.append(d); n_drop += 1
        elif k["meta"].get("qc_verdict") == "FIX":
            kept.append(k); n_fix += 1
            fixed.append({
                "id": s["id"], "domain": s.get("domain", ""),
                "dataset_source": s.get("dataset_source", ""),
                "qc_error_type": k["meta"].get("qc_error_type", ""),
                "qc_reason": k["meta"].get("qc_reason", ""),
                "gold_answer": s.get("gold_answer", ""), "gold_unit": s.get("gold_unit", ""),
                "original_question": k["meta"].get("qc_original_question", ""),
                "fixed_question": k["question"],
            })
        else:
            kept.append(k); n_clean += 1
    return kept, dropped, fixed, (n_clean, n_fix, n_drop, n_pending)


def _write_outputs(out_dir: Path, specs, kept, dropped, fixed, counts) -> None:
    """Write all reviewable artifacts (called at every checkpoint AND at the end)."""
    write_jsonl(out_dir / "problems_qc.jsonl", kept)
    write_jsonl(out_dir / "qc_dropped.jsonl", dropped)
    write_jsonl(out_dir / "qc_fixed.jsonl", fixed)
    _write_report(out_dir / "qc_report.md", specs, kept, dropped, *counts)


async def _run(args) -> None:
    root = repo_root()
    in_path = root / args.input
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    verdicts_path = out_dir / "qc_verdicts.jsonl"

    specs = list(read_jsonl(in_path))
    if args.source != "all":
        specs = [s for s in specs if s.get("dataset_source") == _SOURCE_MAP[args.source]]
    if args.limit:
        specs = specs[: args.limit]

    existing = {} if args.fresh else {v["id"]: v for v in _load(verdicts_path)}
    existing_list = list(existing.values())
    todo = [s for s in specs if s["id"] not in existing]
    print(f"Loaded {len(specs)} problems | cached {len(existing)} | to do {len(todo)}")
    print(f"model={args.model} thinking={'OFF' if args.no_thinking else 'ON'} "
          f"concurrency={args.concurrency} source={args.source}")

    new: list[dict] = []

    def _checkpoint() -> tuple:
        """Persist verdicts + all reviewable audit files from progress so far."""
        succ = [x for x in new if "__error__" not in x]
        write_jsonl(verdicts_path, existing_list + succ)
        vmap = {v["id"]: v for v in existing_list + succ}
        kept, dropped, fixed, counts = _apply_verdicts(specs, vmap)
        _write_outputs(out_dir, specs, kept, dropped, fixed, counts)
        return kept, dropped, fixed, counts

    if todo:
        client = ds_client.make_client()
        sem = asyncio.Semaphore(args.concurrency)
        lock = asyncio.Lock()
        n_done = 0

        async def worker(s: dict) -> None:
            nonlocal n_done
            async with sem:
                try:
                    v = await asyncio.wait_for(qc_one(s, client, args), timeout=args.problem_timeout)
                except Exception as e:  # incl. TimeoutError -> not cached, retried on re-run
                    v = {"id": s["id"], "__error__": type(e).__name__ + ": " + str(e)[:200]}
            async with lock:
                new.append(v)
                n_done += 1
                if "__error__" not in v and v.get("verdict") != "CLEAN":
                    print(f"  {v['verdict']:4s} [{s['id']}] ({v.get('error_type')}) :: {v.get('reason','')[:80]}")
                if n_done % args.save_every == 0:
                    _, _, _, c = _checkpoint()  # auto-save verdicts + audit files
                    print(f"  [checkpoint] {n_done}/{len(todo)} | CLEAN {c[0]} FIX {c[1]} DROP {c[2]}")

        await asyncio.gather(*(worker(s) for s in todo))

    kept, dropped, fixed, (n_clean, n_fix, n_drop, n_pending) = _checkpoint()
    n_err = len([v for v in new if "__error__" in v])
    print(f"\nDone. CLEAN {n_clean} | FIX {n_fix} | DROP {n_drop}"
          + (f" | error/pending {n_pending} (api errors {n_err}; re-run to retry)" if n_pending else ""))
    print(f"  kept   -> {args.out_dir}/problems_qc.jsonl ({len(kept)})")
    print(f"  fixed  -> {args.out_dir}/qc_fixed.jsonl ({len(fixed)})   [review]")
    print(f"  drop   -> {args.out_dir}/qc_dropped.jsonl ({len(dropped)})   [review]")
    print(f"  report -> {args.out_dir}/qc_report.md")


def main() -> None:
    p = argparse.ArgumentParser(description="Execution-grounded DeepSeek QC of the v06 SFT input")
    p.add_argument("--input", default=INPUT)
    p.add_argument("--out-dir", default=OUT_DIR)
    p.add_argument("--source", choices=["all", "btc", "vietjack"], default="all")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=12)
    p.add_argument("--model", default=COMMERCIAL_MODEL, help="default: deepseek-v4-pro")
    p.add_argument("--save-every", type=int, default=25)
    p.add_argument("--req-timeout", type=float, default=90.0,
                   help="per-DeepSeek-request timeout (s) — prevents a hung request blocking a worker")
    p.add_argument("--problem-timeout", type=float, default=360.0,
                   help="hard cap (s) for all stages of one problem; on timeout -> retry next run")
    p.add_argument("--no-thinking", action="store_true",
                   help="disable DeepSeek thinking (faster/cheaper, less reliable solving)")
    p.add_argument("--fresh", action="store_true", help="ignore cached verdicts and redo")
    p.add_argument("--selftest", action="store_true", help="run offline logic test and exit")
    args = p.parse_args()
    if args.selftest:
        from app.physics_solution.QC_data import qc_smoke
        qc_smoke.run()
        return
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
