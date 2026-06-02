# physics-v02-fewshot-qwen3.5-4b

EXACT 2026 — Task Type 2 (Physics Problems).
Team: **Laplace's Red Devils**.

## TL;DR

| | |
|---|---|
| Strategy | `fewshot` |
| Base | `qwen3.5-4b` (Qwen/Qwen3.5-4B) |
| Accuracy | **0.5178** (700 / 1352 correct, mean latency 0.6246 s) |
| Built | 2026-05-23 12:39 UTC |

## Strategy

Strategy `fewshot` applied on top of Qwen/Qwen3.5-4B. See app/physics_solution/versions/v02_*/ for code.
## Inference configuration
| Knob | Value |
|---|---|
| `dtype` | bf16 (effective: bf16) |
| `batch_size` | 80 |
| `max_new_tokens` | 640 |
| `temperature` | 0 |
| `assistant_prefix` | `` |
| `n_examples` (few-shot) | 3 |
## Hardware
| | |
|---|---|
| Device | cuda |
| GPU | NVIDIA A100-SXM4-40GB (39.49 GB) |
| CUDA | 12.6 |
| Python | 3.12.12 |
| `torch` | 2.8.0+cu126 |
| `transformers` | 5.9.0 |
## Test set
| | |
|---|---|
| File | `app/physics_solution/data/test/full_test.csv` |
| Data variant | Original |
| Size | 1352 questions |
| Seed | 42 |
| Few-shot pool size | 24 |
### Per-domain accuracy
| Domain | n | Accuracy |
|---|---|---|
| `LD` | 397 | 0.285 |
| `CH` | 290 | 0.583 |
| `NL` | 190 | 0.705 |
| `TD` | 177 | 0.503 |
| `DDT` | 130 | 0.677 |
| `THCB` | 80 | 0.850 |
| `DT` | 68 | 0.294 |
| `CHLT` | 20 | 0.950 |
### Per-answer-type accuracy
| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 971 | 0.596 |
| `sci_notation` | 241 | 0.224 |
| `text_only` | 59 | 0.068 |
| `mixed` | 35 | 0.657 |
| `multi_value` | 25 | 0.800 |
| `yes_no` | 21 | 0.952 |
## Error analysis
| Fail mode | Count | % of wrong |
|---|---:|---:|
| `magnitude_wrong` | 203 | 31.1% |
| `off_by_power10` | 171 | 26.2% |
| `numeric_far` | 79 | 12.1% |
| `lexically_wrong` | 59 | 9.0% |
| `formula_off` | 51 | 7.8% |
| `sci_scale_wrong` | 39 | 6.0% |
| `unit_mismatch` | 17 | 2.6% |
| `wrong_subquestion` | 16 | 2.5% |
| `format_no_final` | 5 | 0.8% |
| `format_bad_number` | 4 | 0.6% |
| `count_wrong` | 4 | 0.6% |
| `wrong_sign` | 2 | 0.3% |
| `partial_match` | 1 | 0.2% |
| `wrong_choice` | 1 | 0.2% |
## Golden data evaluation
Evaluated on **golden data** (`app/physics_solution/versions/v02_fewshot/output/results_golden.json`) — CoT rewritten by DeepSeek-v4-pro.
| | |
|---|---|
| Accuracy | **0.5229** (707 / 1352 correct) |
### Per-domain accuracy (golden)
| Domain | n | Accuracy |
|---|---|---|
| `LD` | 397 | 0.287 |
| `CH` | 290 | 0.593 |
| `NL` | 190 | 0.716 |
| `TD` | 177 | 0.503 |
| `DDT` | 130 | 0.677 |
| `THCB` | 80 | 0.863 |
| `DT` | 68 | 0.294 |
| `CHLT` | 20 | 0.950 |
### Per-answer-type accuracy (golden)
| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 985 | 0.603 |
| `sci_notation` | 239 | 0.230 |
| `text_only` | 56 | 0.071 |
| `multi_value` | 26 | 0.808 |
| `mixed` | 25 | 0.520 |
| `yes_no` | 21 | 0.952 |
### Error analysis (golden)
| Fail mode | Count | % of wrong |
|---|---:|---:|
| `magnitude_wrong` | 201 | 31.2% |
| `off_by_power10` | 172 | 26.7% |
| `numeric_far` | 77 | 11.9% |
| `lexically_wrong` | 56 | 8.7% |
| `formula_off` | 49 | 7.6% |
| `sci_scale_wrong` | 42 | 6.5% |
| `unit_mismatch` | 18 | 2.8% |
| `wrong_subquestion` | 16 | 2.5% |
| `format_no_final` | 5 | 0.8% |
| `count_wrong` | 4 | 0.6% |
| `wrong_sign` | 2 | 0.3% |
| `format_bad_number` | 1 | 0.2% |
| `partial_match` | 1 | 0.2% |
| `wrong_choice` | 1 | 0.2% |
## How to reproduce
```bash
# 1. Pull this repo
git clone https://github.com/Laplaces-Red-Devils/Exact_2026_Laplace-s_Red_Devils
cd Exact_2026_Laplace-s_Red_Devils
# 2. Rebuild the exact test sample
python -m app.physics_solution.cli.prepare_sample \
    --n 1352 --seed 42
# 3. Run inference (config.py provides the defaults shown above)
python -m app.physics_solution.cli.inference --version v02_fewshot
# 4. Or use this exact upload as the model:
python -m app.physics_solution.cli.inference \
    --version v02_fewshot \
    --model-id Laplaces-Red-Devils/physics-v02-fewshot-qwen3.5-4b
```
## Notes
(none)
