# Handoff — Claude does the QC (CLEAN/FIX/DROP) for the 278 stage-2 problems, NO API

Paste this whole file into a fresh chat (in this repo, with Claude). **No DeepSeek / API budget
needed** — Claude is the solver/judge; a local harness executes + checks its code.

## Context (what already happened)

EXACT 2026 physics, v06 fine-tune. We ran an **execution-grounded QC** over 1671 normalized
problems (BTC + Vietjack). Per problem DeepSeek solved it as-written and we executed the code:
stage 1 = solved-as-written matches gold → CLEAN (kept code); stage 2 = mismatch → DeepSeek
*diagnoses* FIX/DROP/CLEAN (no code produced); stage 3 = a FIX confirmed by re-solving (kept code).

`app/physics_solution/QC_data/gold/`:
- `problems_qc.jsonl` — **1584 clean problems** (= Phase-2 self-gen INPUT; FIX questions baked in).
- `hint_pool.jsonl` — **1306** verified solve-codes (fallback hints for Phase-2).
- `stage2_no_code.jsonl` — the **278** stage-2-CLEAN problems with **no code** (your input).
  **215 numeric, 63 non-numeric.** DeepSeek already judged them CLEAN, but its stage-2 produced
  no code — your job is to give them code (and re-judge with full CLEAN/FIX/DROP power, in case
  any need a statement fix or a drop).
- `qc_dropped.jsonl` (66), `qc_fixed.jsonl` (38), `qc_unprocessed.jsonl` (21 removed).

## Task A — Claude QCs the 278 (CLEAN / FIX / DROP), harness verifies (NO API)

This mirrors the DeepSeek QC exactly, with **you (Claude)** as the solver/judge. You MAY look at
the gold — it's the check target and the signal for spotting a corrupted statement.

Loop (batches of ~30–40):
1. Read a batch from `gold/stage2_no_code.jsonl` (`id, question, domain, answer_type,
   gold_answer, gold_unit`).
2. For each, decide a verdict and append ONE line to `gold/claude_solutions.jsonl`:
   - **CLEAN** — statement is fine; write code that solves the ORIGINAL statement to gold:
     `{"id","verdict":"CLEAN","code":"<python>","reason":"..."}`
   - **FIX** — a corrupted NUMBER/SYMBOL/UNIT (OCR `3√2`↔`√3/2`, a dropped `π`, a garbled unit);
     give the corrected statement AND code that solves the FIXED statement to gold:
     `{"id","verdict":"FIX","fixed_question":"<corrected>","code":"<python>","reason":"OCR ..."}`
     (don't change a physics-meaning word to match gold — that's a DROP, not a FIX; don't put the
     gold value into the statement.)
   - **DROP** — not safely fixable (missing data/options, truncated, or the gold itself is wrong):
     `{"id","verdict":"DROP","reason":"..."}`
   Code rules (the harness enforces — echoes are rejected):
   - **Actually COMPUTE** from the givens; a baked `print("FINAL ANSWER: <gold>")` is rejected
     (`literal_final_answer`/`no_computation`). Sympy symbolic is OK.
   - Hardcode constants (`k=9e9`, `mu_0=4*pi*1e-7`, `eps_0=8.854e-12`, …).
   - Print `FINAL ANSWER: <value>` then `UNIT: <unit>`; no e-notation (`2.97 * 10^6`).
   - `yes_no`: compute + compare **with ~1% tolerance** (must contain a real comparison).
   - Pure-knowledge `text` answers (e.g. "doesn't depend on current") aren't computable — `DROP`
     them rather than echo (or skip the line).
3. Run the harness:
   ```bash
   PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.verify_solutions
   ```
   It executes/scoring each: CLEAN→code must solve the original to gold; FIX→code must solve the
   fixed statement to gold (and the fix must not leak the gold); DROP→recorded as-is. Verified code
   → `hint_pool.jsonl`; accepted verdicts → `claude_verdicts.jsonl`; failures (with `reject` ∈
   {literal_final_answer, no_computation, no_comparison, fix_leaked_gold, wrong_answer, exec_error})
   → `verify_failed.jsonl`. Resumable: ids already in `claude_verdicts.jsonl` are skipped.
4. Read `verify_failed.jsonl`, fix those lines in `claude_solutions.jsonl`, re-run. Repeat until
   `Coverage: X/278` is high (aim high on the 215 numeric; conceptual text → DROP is fine).

> Note: because you see the gold while solving, CLEAN/FIX here are "teacher-mode" verified (the
> echo-guard + gold-leak check are the backstops), not gold-blind like DeepSeek's stage-1 — fine
> for a fallback hint pool. Be honest: only mark CLEAN/FIX if the code *genuinely* computes it.

## Task B — apply the verdicts + assemble the final self-gen dataset

```bash
PYTHONPATH=. python3 - <<'PY'
import json
B='app/physics_solution/QC_data/gold/'
prob=[json.loads(l) for l in open(B+'problems_qc.jsonl')]
hint={json.loads(l)['id']:json.loads(l) for l in open(B+'hint_pool.jsonl')}
verd={json.loads(l)['id']:json.loads(l) for l in open(B+'claude_verdicts.jsonl')} if __import__('os').path.exists(B+'claude_verdicts.jsonl') else {}
out=[]
for p in prob:
    v=verd.get(p['id'])
    if v and v['verdict']=='DROP':                 # Claude dropped it -> exclude
        continue
    q = v['fixed_question'] if (v and v['verdict']=='FIX' and v.get('fixed_question')) else p['question']
    h=hint.get(p['id'])
    out.append({"id":p['id'],"question":q,"domain":p['domain'],"answer_type":p['answer_type'],
                "gold_answer":p['gold_answer'],"gold_unit":p['gold_unit'],
                "dataset_source":p['dataset_source'],
                "hint_code": h['code'] if h else None,
                "hint_source": h['hint_source'] if h else None})  # qc_stage1|qc_stage3|claude
with open(B+'self_gen_dataset.jsonl','w') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+"\n")
print("self_gen_dataset.jsonl:",len(out),"| with hint_code:",sum(1 for r in out if r['hint_code']))
PY
```
**`self_gen_dataset.jsonl` is the final clean file** = clean (FIX-applied, DROP-removed) problems,
each with gold + an optional `hint_code`.

## How Phase-2 self-gen will use it
- Qwen 3.5 4B: short reasoning + one code block (NO HARDCODING of computed values; sympy OK;
  yes_no tolerance), multi-temp → execute → keep correct, pick top-K.
- Code error → feed the error back; keep only the clean final reasoning+code (not the error→fix
  transcript), matching one-shot samples.
- Qwen can't solve / too few samples → use `hint_code` as a **method hint** (hint the approach,
  don't paste verbatim → stays on-policy), Qwen re-derives, execution-gate it. **Don't** hint easy
  solved problems; do use hints to balance rare domains (CHLT…).

## Acceptance
- `claude_verdicts.jsonl` covers ~all 278 (CLEAN/FIX/DROP); `hint_pool.jsonl` grew (hint_source:"claude").
- `self_gen_dataset.jsonl` exists (≈1584 minus any Claude-DROPs; most have hint_code).
- Don't re-run the full DeepSeek QC; don't touch `qc_dropped/qc_unprocessed`.
