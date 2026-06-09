"""Measure the POOLED-vote ensemble (5 sft + 5 base -> one vote, majority wins).

Calls solve() directly so we see the pooled clusters. Per problem logs: latency,
agreement (sft-vote == base-vote), winner vote count /10, whether the MAJORITY answer
is correct, and — if the majority is wrong — whether a MINORITY cluster held the correct
answer (i.e. majority voting cost us a point). Aggregates the same.

    PYTHONPATH=. /venv/main/bin/python -m \
      app.physics_solution.versions.v07_ensemble_vLLM.measure_pool [val|golden] [LIMIT]
"""
import asyncio, csv, json, sys, time, statistics as st
from pathlib import Path
from app.physics_solution.shared.eval import scorer as ev
from app.physics_solution.versions.v07_ensemble_vLLM.pipeline import solve
from app.model.llm_client import physics_llm

SET = sys.argv[1] if len(sys.argv) > 1 else "golden"
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else None
HERE = Path("app/physics_solution/versions/v07_final_version")

if SET == "golden":
    rows = [{"id": r["id"], "question": r["question"], "answer": r["answer"], "unit": r.get("unit", "")}
            for r in csv.DictReader(open(HERE.parent.parent / "data" / "golden" / "golden_60.csv"))]
else:
    rows = [{"id": r["id"], "question": r["question"], "answer": r["gold_answer"], "unit": r.get("gold_unit", "")}
            for r in (json.loads(l) for l in open(HERE / "val_56.jsonl") if l.strip())]
rows = rows[:LIMIT]


def ok(ans, unit, gold, gunit):
    return ev.score(f"FINAL ANSWER: {ans}\nUNIT: {unit}", gold, gunit).is_correct


async def main():
    n = len(rows)
    n_ok = n_agree = 0
    minority_lost = 0     # majority wrong BUT a minority cluster had the right answer
    recoverable = 0       # any cluster (oracle) had the right answer
    lat, wvotes = [], []
    for r in rows:
        res = await solve(r["question"], physics_llm, time.time() + 58)
        lat.append(res["elapsed_s"])
        pool = res.get("pool", [])
        win = pool[0] if pool else {"answer": res["answer"], "unit": res["unit"], "votes": 0}
        wvotes.append(win["votes"])
        maj_ok = ok(res["answer"], res["unit"], r["answer"], r["unit"])
        n_ok += maj_ok
        n_agree += bool(res.get("agree"))
        any_ok = any(ok(c["answer"], c["unit"], r["answer"], r["unit"]) for c in pool) if pool else maj_ok
        recoverable += any_ok
        if (not maj_ok) and any_ok:
            minority_lost += 1
        pool_s = " ".join(f"{c['answer']}({c['votes']})" for c in pool)
        print(f"[{'OK' if maj_ok else 'XX'}] {r['id']:8} {res['elapsed_s']:5.1f}s "
              f"agree={int(bool(res.get('agree')))} win={win['votes']}/10 "
              f"{'MINORITY-HAD-IT' if (not maj_ok and any_ok) else ''} "
              f"| pool=[{pool_s}] gold={r['answer']!r}", flush=True)
    sl = sorted(lat)
    print(f"\n===== POOLED ENSEMBLE — {SET} (n={n}) =====")
    print(f"ACCURACY (majority): {n_ok}/{n} = {n_ok/n:.3f}")
    print(f"agreement (sft==base): {n_agree}/{n} = {n_agree/n:.3f}")
    print(f"ORACLE (any cluster right): {recoverable}/{n} = {recoverable/n:.3f}")
    print(f"minority-lost (majority wrong, a minority was right): {minority_lost}")
    print(f"winner votes/10: mean={st.mean(wvotes):.1f} median={st.median(wvotes):.0f} min={min(wvotes)}")
    print(f"LATENCY mean={st.mean(lat):.1f}s median={st.median(lat):.1f}s "
          f"p90={sl[int(len(sl)*0.9)]:.1f}s max={max(lat):.1f}s")


asyncio.run(main())
