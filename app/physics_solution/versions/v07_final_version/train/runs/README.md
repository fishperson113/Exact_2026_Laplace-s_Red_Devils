# `train/runs/` — eval/SC output dumps (naming guide)

This dir holds (a) training checkpoints `sft_v07/` (v07b, 4-bit) & `sft_v07c/` (v07c, 16-bit)
and (b) **eval result JSONs**. The JSON names are confusing because they accreted across a day
of investigation — this file decodes them. Authoritative numbers live in
[`../../README.md` → Results & Error Analysis](../../README.md).

## Filename grammar

```
{prefix}_{model}[_{modifier}]_{set}.json
```

| field | values | meaning |
|---|---|---|
| **prefix** | `eval` | greedy single-pass (`eval.py`, `do_sample=False`) |
| | `sc` | self-consistency K=5 majority vote (`self_consistency.py`) |
| **model** | `base` | plain `Qwen/Qwen3.5-4B` |
| | `v07b` | 4-bit QLoRA run, **merged** model |
| | `adp` / `adapter` | v07b as **4-bit base + LoRA adapter** (un-merged = training condition) |
| | `v07c` | 16-bit LoRA run, **merged** model — **the deploy model** |
| | _(none)_ | scratch: the LAST `eval.py` run overwrote it; model is whatever ran last — **don't trust** |
| **modifier** | `fixed` | **NEW** scorer (SI-unit rescue + bidir text) **+ NEW** prompt (full precision, no `X*10^N`/rounding rules). Absence ⇒ OLD scorer+prompt |
| | `1024` | `max_new_tokens=1024` (default elsewhere is 2048) |
| **set** | `val56` / `val_56` | the 56-problem validation set |
| | `golden60` / `golden_60` | the 60 held-out golden (true OOD test) |
| | `results` | summary only (accuracy + buckets, **no per-problem rows**) |

All eval is **think-OFF, greedy** (unless `sc`), `max_new_tokens=2048` (unless `1024`).
Per-problem files carry `rows[]` with `{id, correct, bucket, gold, pred, exec_stdout,
completion, ...}` — use these for error analysis.

## Canonical files (git-tracked — trust these)

| file | model · condition | val_56 | golden_60 |
|---|---|---|---|
| `eval_base_fixed_*` | base · new scorer+prompt, greedy | 0.821 | 0.683 |
| `eval_v07c_fixed_*` | **v07c · new scorer+prompt, greedy** | **0.857** | **0.717** |
| `sc_v07c_*` | **v07c · new scorer+prompt, SC K=5** | **0.875** | **0.817** |

> `sc_base_*` (base under SC = 0.875 / 0.783) was **never pulled** — the Colab box died first;
> only the cumulative-acc log survived at `../../colab_logs/sc_base.log`. Re-run to regenerate.

## Scratch / local-only files (NOT committed — intermediate investigation, OLD scorer+prompt)

These are the pre-fix greedy runs that established the QLoRA-merge finding. Kept locally for the
record; superseded by the `*_fixed` files for any current claim.

| file | what | val_56 | golden_60 |
|---|---|---|---|
| `eval_base_*` (no `fixed`) | base, OLD scorer+prompt, @2048 | 0.679 | 0.650 |
| `eval_v07b_*` | v07b **merged**, OLD, @2048 | 0.696 | 0.600 |
| `eval_v07b_1024_*` | v07b merged, OLD, @**1024** | 0.696 | 0.567 |
| `eval_adp_*` / `eval_adapter_results` | v07b **4-bit base+adapter** (train cond.), OLD | 0.732 | 0.650 |
| `eval_v07c_*` (no `fixed`) | v07c merged, OLD scorer+prompt, @2048 | 0.750 | 0.633 |
| `eval_results.json`, `eval_val_56.json`, `eval_golden_60.json` | **scratch** — last eval.py run's generic output (currently = v07c_fixed) | — | — |
| `eval_*_BASE.json`, `eval_*_FT.json` | **legacy** earliest base-vs-FT run (pre-naming-convention; conditions uncertain — ignore) | — | — |

## Regenerate (fresh GPU)

```bash
cd /content/Exact_2026_Laplace-s_Red_Devils
export LD_LIBRARY_PATH=/usr/lib64-nvidia:$LD_LIBRARY_PATH PYTORCH_ALLOC_CONF=expandable_segments:True PYTHONPATH=.
PY=/content/v07_env/bin/python   # see ../../colab_setup/
M=app.physics_solution.versions.v07_final_version
# greedy (writes generic eval_*.json; cp to a tagged name after):
$PY -m $M.eval --model <merged_dir|Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged> \
   --sets both --max-new-tokens 2048 --batch-size 32
# self-consistency (writes sc_{val_56,golden_60}.json):
$PY -m $M.self_consistency --model <...> --sets both --k 5 --temperature 0.7 --prob-batch 6
```
Deploy model on the Hub: `Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged` (think-OFF,
2048 tokens; best = + SC K=5).
