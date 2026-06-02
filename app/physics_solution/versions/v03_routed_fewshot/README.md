---
license: apache-2.0
tags:
- physics
- exact-2026
- type2
- electrical-circuits
- electrostatics
base_model: Qwen/Qwen3.5-4B
language:
- en
---
# physics-v03-routed_fewshot-qwen3.5-4b
EXACT 2026 — Task Type 2 (Physics Problems).
Team: **Laplace's Red Devils**.
## TL;DR
| | |
|---|---|
| Strategy | `routed_fewshot` |
| Base | `qwen3.5-4b` (Qwen/Qwen3.5-4B) |
| Accuracy | **0.5414** (732 / 1352 correct, mean latency 0.6252 s) |
| Built | 2026-05-23 13:28 UTC |

## Strategy

Strategy `routed_fewshot` applied on top of Qwen/Qwen3.5-4B. See app/physics_solution/versions/v03_*/ for code.
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
| `LD` | 397 | 0.242 |
| `CH` | 290 | 0.614 |
| `NL` | 190 | 0.711 |
| `TD` | 177 | 0.735 |
| `DDT` | 130 | 0.685 |
| `THCB` | 80 | 0.850 |
| `DT` | 68 | 0.294 |
| `CHLT` | 20 | 0.800 |
### Per-answer-type accuracy
| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 971 | 0.644 |
| `sci_notation` | 241 | 0.162 |
| `text_only` | 59 | 0.119 |
| `mixed` | 35 | 0.686 |
| `multi_value` | 25 | 0.800 |
| `yes_no` | 21 | 0.809 |
## Error analysis
| Fail mode | Count | % of wrong |
|---|---:|---:|
| `magnitude_wrong` | 187 | 30.2% |
| `off_by_power10` | 120 | 19.4% |
| `numeric_far` | 71 | 11.5% |
| `formula_off` | 65 | 10.5% |
| `sci_scale_wrong` | 57 | 9.2% |
| `lexically_wrong` | 56 | 9.0% |
| `wrong_subquestion` | 17 | 2.7% |
| `unit_mismatch` | 14 | 2.3% |
| `format_no_final` | 13 | 2.1% |
| `format_bad_number` | 10 | 1.6% |
| `wrong_choice` | 4 | 0.6% |
| `count_wrong` | 3 | 0.5% |
| `partial_match` | 2 | 0.3% |
| `wrong_sign` | 1 | 0.2% |
## Golden data evaluation
Evaluated on **golden data** (`app/physics_solution/versions/v03_routed_fewshot/output/results_golden.json`) — CoT rewritten by DeepSeek-v4-pro.
| | |
|---|---|
| Accuracy | **0.5473** (740 / 1352 correct) |
### Per-domain accuracy (golden)
| Domain | n | Accuracy |
|---|---|---|
| `LD` | 397 | 0.247 |
| `CH` | 290 | 0.617 |
| `NL` | 190 | 0.721 |
| `TD` | 177 | 0.735 |
| `DDT` | 130 | 0.685 |
| `THCB` | 80 | 0.863 |
| `DT` | 68 | 0.324 |
| `CHLT` | 20 | 0.800 |
### Per-answer-type accuracy (golden)
| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 985 | 0.650 |
| `sci_notation` | 239 | 0.172 |
| `text_only` | 56 | 0.125 |
| `multi_value` | 26 | 0.808 |
| `mixed` | 25 | 0.560 |
| `yes_no` | 21 | 0.809 |
### Error analysis (golden)
| Fail mode | Count | % of wrong |
|---|---:|---:|
| `magnitude_wrong` | 189 | 30.9% |
| `off_by_power10` | 118 | 19.3% |
| `numeric_far` | 70 | 11.4% |
| `formula_off` | 60 | 9.8% |
| `sci_scale_wrong` | 60 | 9.8% |
| `lexically_wrong` | 53 | 8.7% |
| `wrong_subquestion` | 16 | 2.6% |
| `unit_mismatch` | 14 | 2.3% |
| `format_no_final` | 14 | 2.3% |
| `format_bad_number` | 7 | 1.1% |
| `wrong_choice` | 4 | 0.7% |
| `partial_match` | 3 | 0.5% |
| `wrong_sign` | 2 | 0.3% |
| `count_wrong` | 2 | 0.3% |
## How to reproduce
```bash
# 1. Pull this repo
git clone https://github.com/Laplaces-Red-Devils/Exact_2026_Laplace-s_Red_Devils
cd Exact_2026_Laplace-s_Red_Devils
# 2. Rebuild the exact test sample
python -m app.physics_solution.cli.prepare_sample \
    --n 1352 --seed 42
# 3. Run inference (config.py provides the defaults shown above)
python -m app.physics_solution.cli.inference --version v03_routed_fewshot
# 4. Or use this exact upload as the model:
python -m app.physics_solution.cli.inference \
    --version v03_routed_fewshot \
    --model-id Laplaces-Red-Devils/physics-v03-routed_fewshot-qwen3.5-4b
```
## Notes
(none)