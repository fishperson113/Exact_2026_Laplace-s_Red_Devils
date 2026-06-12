"""FINAL ensemble decision experiment — SFT-only vs BASE-only vs ENSEMBLE.

For each run we sample K from SFT and K from BASE **once per problem** (identical
samples feed all three configs), so the configs differ ONLY by which votes are
counted — the cleanest way to isolate "does adding BASE to SFT help?":

  config 1  SFT-only      : majority vote over the SFT K samples
  config 2  BASE-only     : majority vote over the BASE K samples
  config 3  ENSEMBLE      : pooled majority vote over all SFT+BASE 2K samples

(Explanation/CoT is the SAME downstream BASE step in all three, so it does not
change the answer or the decision — skipped here for speed.)

Runs each config 3x on BOTH sets (val_56, golden_60). Logs per problem: per-side
votes, which side(s) actually produced the correct answer, domain. Then aggregates
accuracy (mean±range over runs), the ensemble correct-source distribution, and a
per-domain SFT-vs-BASE breakdown to reveal domain specialization (for weighting).

    PYTHONPATH=. VLLM_MODEL=sft JUDGE_MODEL=base \
      /venv/main/bin/python -m app.physics_solution.versions.v07_ensemble_vLLM.final_experiment

Writes:  versions/v07_ensemble_vLLM/output/final_experiment_raw.jsonl  (per problem)
         versions/v07_ensemble_vLLM/output/FINAL_EXPERIMENT.md          (the report)
"""
from __future__ import annotations

import asyncio, csv, json, time, statistics as st
from collections import defaultdict
from pathlib import Path

from app.model.llm_client import physics_llm, physics_base_llm
from app.core.config import settings
from app.physics_solution.shared.eval import scorer as ev
from app.physics_solution.shared.router import RouteResult, _parse_route
from app.physics_solution.versions.v05_best_vLLM.pipeline import _build_classify_messages
from app.physics_solution.versions.v06_finetune.data_pipeline.prompts import build_gen_messages
from app.physics_solution.versions.v07_ensemble_vLLM.pipeline import (
    _exec_one, _vote, _cluster, _has_answer, _DEFAULT_ROUTE,
)

K = settings.ensemble_k
RUNS = 3
HERE = Path("app/physics_solution/versions/v07_ensemble_vLLM")
OUT = HERE / "output"; OUT.mkdir(parents=True, exist_ok=True)
VAL = Path("app/physics_solution/versions/v07_final_version/val_56.jsonl")
GOLD = Path("app/physics_solution/data/golden/golden_60.csv")


def load(set_name):
    if set_name == "val":
        return [{"id": r["id"], "q": r["question"], "ans": r["gold_answer"],
                 "unit": r.get("gold_unit", ""), "domain": r.get("domain", "?")}
                for r in (json.loads(l) for l in open(VAL) if l.strip())]
    return [{"id": r["id"], "q": r["question"], "ans": r["answer"],
             "unit": r.get("unit", ""), "domain": r.get("domain", "?")}
            for r in csv.DictReader(open(GOLD))]


def ok(ans, unit, gold, gunit):
    return ev.score(f"FINAL ANSWER: {ans}\nUNIT: {unit}", gold, gunit).is_correct


async def solve_one(p):
    """Sample SFT K + BASE K once; return both row sets (tagged) + classify route."""
    try:
        raw = await physics_base_llm.chat(_build_classify_messages(p["q"]), max_tokens=50, temperature=0.0)
        route = _parse_route(raw)
    except Exception:
        route = _DEFAULT_ROUTE
    msgs = build_gen_messages(p["q"], route.domain, route.answer_type)
    sft_c, base_c = await asyncio.gather(
        physics_llm.chat_n(msgs, n=K, temperature=settings.ensemble_temperature,
                           top_p=settings.ensemble_top_p, max_tokens=settings.ensemble_max_tokens),
        physics_base_llm.chat_n(msgs, n=K, temperature=settings.ensemble_temperature,
                                top_p=settings.ensemble_top_p, max_tokens=settings.ensemble_max_tokens),
    )
    sft_rows = list(await asyncio.gather(*[_exec_one(c) for c in sft_c]))
    base_rows = list(await asyncio.gather(*[_exec_one(c) for c in base_c]))
    for r in sft_rows: r["side"] = "sft"
    for r in base_rows: r["side"] = "base"
    return sft_rows, base_rows


def cluster_sides(rows):
    """Pooled clusters with per-side vote counts; largest first."""
    out = []
    for cl in _cluster(rows):
        s = sum(1 for r in cl["rows"] if r["side"] == "sft")
        b = sum(1 for r in cl["rows"] if r["side"] == "base")
        rep = cl["rows"][0]
        out.append({"ans": rep["ans"], "unit": rep["unit"] or "-", "sft": s, "base": b, "n": s + b})
    return out


async def main():
    raw_fh = open(OUT / "final_experiment_raw.jsonl", "w")
    records = []
    for set_name in ("val", "golden"):
        rows = load(set_name)
        for run in range(1, RUNS + 1):
            print(f"\n########## SET={set_name}  RUN={run}  (n={len(rows)}) ##########", flush=True)
            for p in rows:
                t0 = time.time()
                sft_rows, base_rows = await solve_one(p)
                lat = time.time() - t0
                sft_rep, sft_v = _vote(sft_rows)
                base_rep, base_v = _vote(base_rows)
                clusters = cluster_sides(sft_rows + base_rows)
                ens = clusters[0] if clusters else {"ans": "", "unit": "-", "sft": 0, "base": 0, "n": 0}

                sft_ok = ok(sft_rep["ans"], sft_rep["unit"], p["ans"], p["unit"])
                base_ok = ok(base_rep["ans"], base_rep["unit"], p["ans"], p["unit"])
                ens_ok = ok(ens["ans"], ens["unit"], p["ans"], p["unit"])
                # which side(s) produced ANY correct sample (oracle per side)
                sft_any = any(ok(r["ans"], r["unit"], p["ans"], p["unit"]) for r in sft_rows)
                base_any = any(ok(r["ans"], r["unit"], p["ans"], p["unit"]) for r in base_rows)
                source = ("both" if sft_any and base_any else "sft_only" if sft_any
                          else "base_only" if base_any else "none")

                rec = {"set": set_name, "run": run, "id": p["id"], "domain": p["domain"],
                       "gold": f"{p['ans']} {p['unit']}",
                       "sft_ok": sft_ok, "base_ok": base_ok, "ens_ok": ens_ok,
                       "sft_ans": f"{sft_rep['ans']} {sft_rep['unit']}({sft_v}/{K})",
                       "base_ans": f"{base_rep['ans']} {base_rep['unit']}({base_v}/{K})",
                       "ens_ans": f"{ens['ans']} {ens['unit']}(sft{ens['sft']}+base{ens['base']})",
                       "correct_source": source, "lat": round(lat, 1),
                       "pool": [f"{c['ans']}(s{c['sft']}b{c['base']})" for c in clusters]}
                records.append(rec)
                raw_fh.write(json.dumps(rec) + "\n"); raw_fh.flush()
                flag = "".join(["S" if sft_ok else ".", "B" if base_ok else ".", "E" if ens_ok else "."])
                print(f"[{flag}] {set_name[:3]} r{run} {p['id']:8} {p['domain']:5} {lat:5.1f}s "
                      f"src={source:9} sft={rec['sft_ans']:22} base={rec['base_ans']:22} "
                      f"ens={rec['ens_ans']:26} gold={rec['gold']!r}", flush=True)
    raw_fh.close()
    report(records)


def _acc_runs(recs, key):
    by_run = defaultdict(lambda: [0, 0])
    for r in recs:
        by_run[r["run"]][1] += 1
        by_run[r["run"]][0] += int(r[key])
    accs = [c / n for c, n in by_run.values()]
    return accs


def report(records):
    L = []
    L.append("# FINAL ensemble decision — SFT-only vs BASE-only vs ENSEMBLE\n")
    L.append(f"K={K} samples/side, {RUNS} runs/config, identical samples feed all 3 configs per run "
             "(so differences are purely the voting strategy). Explanation/CoT is the same downstream "
             "BASE step in all configs (skipped here; does not affect the answer).\n")
    L.append("## 1. Accuracy per config (mean over runs [min..max])\n")
    L.append("| set | SFT-only | BASE-only | ENSEMBLE |")
    L.append("|---|---|---|---|")
    for set_name in ("val", "golden"):
        sub = [r for r in records if r["set"] == set_name]
        cells = []
        for key in ("sft_ok", "base_ok", "ens_ok"):
            a = _acc_runs(sub, key)
            cells.append(f"{st.mean(a):.3f} [{min(a):.3f}..{max(a):.3f}]")
        n = len({r["id"] for r in sub})
        L.append(f"| {set_name} (n={n}) | {cells[0]} | {cells[1]} | {cells[2]} |")
    L.append("")

    L.append("## 2. Does ENSEMBLE beat the best single model?\n")
    for set_name in ("val", "golden"):
        sub = [r for r in records if r["set"] == set_name]
        s, b, e = (st.mean(_acc_runs(sub, k)) for k in ("sft_ok", "base_ok", "ens_ok"))
        best = max(s, b); delta = e - best
        verdict = "ENSEMBLE WINS" if delta > 0.005 else "TIE/NO GAIN" if abs(delta) <= 0.005 else "ENSEMBLE WORSE"
        L.append(f"- **{set_name}**: ensemble {e:.3f} vs best-single {best:.3f} "
                 f"(SFT {s:.3f} / BASE {b:.3f}) → Δ={delta:+.3f} → **{verdict}**")
    L.append("")

    L.append("## 3. Where does the correct answer come from? (ensemble runs)\n")
    L.append("Per problem-instance, which side produced ANY correct sample:\n")
    L.append("| set | both | sft_only | base_only | none |")
    L.append("|---|---|---|---|---|")
    for set_name in ("val", "golden"):
        sub = [r for r in records if r["set"] == set_name]
        c = defaultdict(int)
        for r in sub: c[r["correct_source"]] += 1
        tot = len(sub)
        L.append(f"| {set_name} | {c['both']} ({c['both']/tot:.0%}) | {c['sft_only']} ({c['sft_only']/tot:.0%}) "
                 f"| {c['base_only']} ({c['base_only']/tot:.0%}) | {c['none']} ({c['none']/tot:.0%}) |")
    L.append("\n*sft_only/base_only > 0 means that model uniquely solves problems the other misses "
             "→ a reason to ensemble. If ~all 'both', the two are redundant.*\n")

    L.append("## 4. Domain specialization — SFT vs BASE accuracy by domain\n")
    L.append("(vote accuracy averaged over all runs; Δ = SFT − BASE; +Δ = SFT stronger)\n")
    L.append("| set | domain | n | SFT | BASE | ENS | Δ(SFT−BASE) | who |")
    L.append("|---|---|---|---|---|---|---|---|")
    for set_name in ("val", "golden"):
        sub = [r for r in records if r["set"] == set_name]
        doms = sorted({r["domain"] for r in sub})
        for d in doms:
            ds = [r for r in sub if r["domain"] == d]
            n = len({r["id"] for r in ds})
            sa = st.mean([r["sft_ok"] for r in ds])
            ba = st.mean([r["base_ok"] for r in ds])
            ea = st.mean([r["ens_ok"] for r in ds])
            delta = sa - ba
            who = "SFT" if delta > 0.05 else "BASE" if delta < -0.05 else "tie"
            L.append(f"| {set_name} | {d} | {n} | {sa:.2f} | {ba:.2f} | {ea:.2f} | {delta:+.2f} | {who} |")
    L.append("")

    L.append("## 5. Latency (ensemble sampling, CUDA graphs)\n")
    lats = [r["lat"] for r in records]
    sl = sorted(lats)
    L.append(f"- mean {st.mean(lats):.1f}s · median {st.median(lats):.1f}s · "
             f"p90 {sl[int(len(sl)*0.9)]:.1f}s · max {max(lats):.1f}s (n={len(lats)} solves)\n")
    L.append("*Single-model configs sample K not 2K, so they run a bit faster; all ≪ 60s.*\n")

    (OUT / "FINAL_EXPERIMENT.md").write_text("\n".join(L))
    print("\n" + "\n".join(L))
    print(f"\n[written] {OUT/'FINAL_EXPERIMENT.md'} and final_experiment_raw.jsonl")


if __name__ == "__main__":
    asyncio.run(main())
