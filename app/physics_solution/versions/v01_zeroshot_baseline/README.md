# physics-v01-zeroshot-qwen3.5-4b

EXACT 2026 — Task Type 2 (Physics Problems).
Team: **Laplace's Red Devils**.

## TL;DR

| | |
|---|---|
| Strategy | `zeroshot` |
| Base | `qwen3.5-4b` (Qwen/Qwen3.5-4B) |
| Accuracy | **0.3787** (512 / 1352 correct, mean latency 0.4093 s) |
| Built | 2026-05-23 05:25 UTC |

## Strategy

Strategy `zeroshot` applied on top of Qwen/Qwen3.5-4B. See app/physics_solution/versions/v01_*/ for code.

## Inference configuration

| Knob | Value |
|---|---|
| `dtype` | bf16 (effective: bf16) |
| `batch_size` | 100 |
| `max_new_tokens` | 640 |
| `temperature` | 0 |
| `assistant_prefix` | `` |
| `n_examples` (few-shot) | — |

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
| Few-shot pool size | 14 |

### Per-domain accuracy

| Domain | n | Accuracy |
|---|---|---|
| `LD` | 397 | 0.151 |
| `CH` | 290 | 0.469 |
| `NL` | 190 | 0.647 |
| `TD` | 177 | 0.294 |
| `DDT` | 130 | 0.600 |
| `THCB` | 80 | 0.550 |
| `DT` | 68 | 0.176 |
| `CHLT` | 20 | 0.350 |

### Per-answer-type accuracy

| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 971 | 0.471 |
| `sci_notation` | 241 | 0.104 |
| `text_only` | 59 | 0.000 |
| `mixed` | 35 | 0.657 |
| `multi_value` | 25 | 0.000 |
| `yes_no` | 21 | 0.333 |

## Error analysis

| Fail mode | Count | % of wrong |
|---|---:|---:|
| `off_by_power10` | 176 | 21.0% |
| `numeric_far` | 173 | 20.6% |
| `magnitude_wrong` | 167 | 19.9% |
| `formula_off` | 149 | 17.7% |
| `lexically_wrong` | 62 | 7.4% |
| `wrong_subquestion` | 25 | 3.0% |
| `count_wrong` | 25 | 3.0% |
| `sci_scale_wrong` | 20 | 2.4% |
| `format_no_final` | 14 | 1.7% |
| `wrong_choice` | 14 | 1.7% |
| `format_bad_number` | 8 | 1.0% |
| `unit_mismatch` | 5 | 0.6% |
| `wrong_sign` | 2 | 0.2% |

## Golden data evaluation

Evaluated on **golden data** (`app/physics_solution/versions/v01_zeroshot_baseline/output/results_golden.json`) — CoT rewritten by DeepSeek-v4-pro.

| | |
|---|---|
| Accuracy | **0.3817** (516 / 1352 correct) |

### Per-domain accuracy (golden)

| Domain | n | Accuracy |
|---|---|---|
| `LD` | 397 | 0.151 |
| `CH` | 290 | 0.469 |
| `NL` | 190 | 0.658 |
| `TD` | 177 | 0.299 |
| `DDT` | 130 | 0.600 |
| `THCB` | 80 | 0.562 |
| `DT` | 68 | 0.176 |
| `CHLT` | 20 | 0.350 |

### Per-answer-type accuracy (golden)

| Answer type | n | Accuracy |
|---|---|---|
| `pure_numeric` | 985 | 0.478 |
| `sci_notation` | 239 | 0.109 |
| `text_only` | 56 | 0.000 |
| `multi_value` | 26 | 0.038 |
| `mixed` | 25 | 0.440 |
| `yes_no` | 21 | 0.333 |

### Error analysis (golden)

| Fail mode | Count | % of wrong |
|---|---:|---:|
| `off_by_power10` | 176 | 21.1% |
| `magnitude_wrong` | 171 | 20.5% |
| `numeric_far` | 171 | 20.5% |
| `formula_off` | 148 | 17.7% |
| `lexically_wrong` | 59 | 7.1% |
| `count_wrong` | 25 | 3.0% |
| `wrong_subquestion` | 24 | 2.9% |
| `sci_scale_wrong` | 21 | 2.5% |
| `format_no_final` | 14 | 1.7% |
| `wrong_choice` | 14 | 1.7% |
| `unit_mismatch` | 6 | 0.7% |
| `format_bad_number` | 5 | 0.6% |
| `wrong_sign` | 2 | 0.2% |


## How to reproduce

```bash
# 1. Pull this repo
git clone https://github.com/Laplaces-Red-Devils/Exact_2026_Laplace-s_Red_Devils
cd Exact_2026_Laplace-s_Red_Devils

# 2. Rebuild the exact test sample
python -m app.physics_solution.cli.prepare_sample \
    --n 1352 --seed 42

# 3. Run inference (config.py provides the defaults shown above)
python -m app.physics_solution.cli.inference --version v01_zeroshot

# 4. Or use this exact upload as the model:
python -m app.physics_solution.cli.inference \
    --version v01_zeroshot \
    --model-id Laplaces-Red-Devils/physics-v01-zeroshot-qwen3.5-4b
```

## Notes

(none)
