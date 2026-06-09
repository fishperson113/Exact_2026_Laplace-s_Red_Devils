"""Investigate: single-SFT vs single-BASE vs ENSEMBLE on the SAME run.

Calls solve() directly (not via /predict) so we see each model's own voted answer
plus the ensemble's chosen answer, and score all three against gold. Also breaks down
agree/judge and where the judge helped or hurt.

    PYTHONPATH=. /venv/main/bin/python -m \
      app.physics_solution.versions.v07_ensemble_vLLM.investigate_ensemble [val|golden] [LIMIT]
"""
import asyncio, csv, json, sys, time
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
    n_sft = n_base = n_ens = 0
    n_agree = n_judge = judge_ok = 0
    ens_vs_sft = []     # problems where ensemble != sft-only outcome
    for r in rows:
        res = await solve(r["question"], physics_llm, time.time() + 58)
        sp, bp = res["sft_pred"], res["base_pred"]
        s_ok = ok(sp["answer"], sp["unit"], r["answer"], r["unit"])
        b_ok = ok(bp["answer"], bp["unit"], r["answer"], r["unit"])
        e_ok = ok(res["answer"], res["unit"], r["answer"], r["unit"])
        n_sft += s_ok; n_base += b_ok; n_ens += e_ok
        agree = res["solve_method"] == "ensemble_agree"
        judged = res["solve_method"].startswith("ensemble_judge")
        n_agree += agree; n_judge += judged; judge_ok += (judged and e_ok)
        if e_ok != s_ok:
            ens_vs_sft.append((r["id"], "ens+sft-" if e_ok else "ens-sft+", res["solve_method"]))
        tag = "".join(["S" if s_ok else ".", "B" if b_ok else ".", "E" if e_ok else "."])
        print(f"[{tag}] {r['id']:8} {res['solve_method']:20} "
              f"sft={sp['answer']!r:>14} base={bp['answer']!r:>14} ens={res['answer']!r:>14} "
              f"gold={r['answer']!r}", flush=True)
    n = len(rows)
    print(f"\n===== {SET} (n={n}) =====")
    print(f"single SFT : {n_sft}/{n} = {n_sft/n:.3f}")
    print(f"single BASE: {n_base}/{n} = {n_base/n:.3f}")
    print(f"ENSEMBLE   : {n_ens}/{n} = {n_ens/n:.3f}")
    print(f"agree={n_agree}  judged={n_judge} (judge correct {judge_ok}/{n_judge})")
    print(f"ensemble differs from single-SFT on: {ens_vs_sft}")


asyncio.run(main())
