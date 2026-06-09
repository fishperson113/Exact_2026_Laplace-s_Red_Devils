"""Measure /predict ensemble accuracy + latency (competition conditions: one request
at a time). Synthesizes the scorer's stdout from answer+unit and scores.

    PYTHONPATH=. /venv/main/bin/python -m \
      app.physics_solution.versions.v07_ensemble_vLLM.measure_predict \
      [SET=val|golden] [URL] [LIMIT]
"""
import csv, json, sys, time, urllib.request, statistics as st
from pathlib import Path
from app.physics_solution.shared.eval import scorer as ev

SET = sys.argv[1] if len(sys.argv) > 1 else "val"
URL = sys.argv[2] if len(sys.argv) > 2 else "http://127.0.0.1:9000/predict"
LIMIT = int(sys.argv[3]) if len(sys.argv) > 3 else None
HERE = Path("app/physics_solution/versions/v07_final_version")

if SET == "golden":
    rows = list(csv.DictReader(open(HERE.parent.parent / "data" / "golden" / "golden_60.csv")))
    rows = [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "unit": r.get("unit", "")} for r in rows]
else:
    rows = [json.loads(l) for l in open(HERE / "val_56.jsonl") if l.strip()]
    rows = [{"id": r["id"], "question": r["question"], "answer": r["gold_answer"],
             "unit": r.get("gold_unit", "")} for r in rows]
rows = rows[:LIMIT]
n_ok, lat = 0, []
for r in rows:
    body = json.dumps({"query_id": r["id"], "type": "type2", "query": r["question"],
                       "premises": [], "options": []}).encode()
    t0 = time.time()
    try:
        req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
        resp = json.load(urllib.request.urlopen(req, timeout=70))[0]
    except Exception as e:  # noqa: BLE001
        resp = {"answer": "", "unit": "", "explanation": f"req error {e}"}
    dt = time.time() - t0
    lat.append(dt)
    synth = f"FINAL ANSWER: {resp.get('answer','')}\nUNIT: {resp.get('unit','')}"
    sc = ev.score(synth, r["answer"], r.get("unit", ""))
    n_ok += int(sc.is_correct)
    print(f"{'OK' if sc.is_correct else 'XX'} {r['id']:8} {dt:5.1f}s "
          f"pred={resp.get('answer','')!r} {resp.get('unit','')!r} "
          f"gold={r['answer']!r} {r.get('unit','')!r}", flush=True)

print(f"\nACC: {n_ok}/{len(rows)} = {n_ok/len(rows):.3f}" if rows else "no rows")
if lat:
    sl = sorted(lat)
    print(f"LATENCY mean={st.mean(lat):.1f}s median={st.median(lat):.1f}s "
          f"p90={sl[int(len(sl)*0.9)]:.1f}s max={max(lat):.1f}s "
          f"(over correct: {st.mean([l for l,r2 in zip(lat,rows)]) :.1f}s)")
