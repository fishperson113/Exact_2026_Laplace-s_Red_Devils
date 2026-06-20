---
tags:
- logic
- qa
- ensemble
- fol
- chain-of-thought
- education
language:
- en
---

# Logic-Based Educational QA — Ensemble Final Results

## Pipeline

```
NL premises + Question
        |
  Stage 1: FOL Model (NL -> FOL)
  Model: Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4
        |
  Stage 2: QA COT Model (NL + FOL + Question -> Answer + Explanation)
  Model: Laplaces-Red-Devils/qa-v05-cot-Qwen3.5-4B
        |
  {"answer": "B", "explanation": "Premise 1 states..."}
```

## Models Used

| Stage | Model | Type |
|-------|-------|------|
| FOL (Stage 1) | [Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4](https://huggingface.co/Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4) | Merged (Qwen2.5-3B) |
| QA (Stage 2) | [Laplaces-Red-Devils/qa-v05-cot-Qwen3.5-4B](https://huggingface.co/Laplaces-Red-Devils/qa-v05-cot-Qwen3.5-4B) | LoRA adapter (Qwen2.5-3B-Instruct) |

## Inference Config

| Parameter | Value |
|-----------|-------|
| FOL max_new_tokens | 768 |
| QA max_new_tokens | 1000 |
| Quantization | INT8 (bitsandbytes) |
| Decoding | Greedy (do_sample=False) |
| Slow threshold | 60s |

## Results on Test Set

| Metric | Value |
|--------|-------|
| **Accuracy** | **74/78 (94.9%)** |
| Avg total latency | 25.80s / sample |
| Avg FOL latency | 9.34s / sample |
| Avg QA latency | 16.45s / sample |
| Slow samples (>60s) | 1 samples |

## Full Evaluation Log

```
[ 1/78] OK    pred=Uncertain gold=Uncertain time=20.54s
[ 2/78] OK    pred=There exists a student likely to pass the exam. gold=There exists a student likely to pass the exam. time=20.00s
[ 3/78] OK    pred=Uncertain gold=Uncertain time=19.46s
[ 4/78] OK    pred=There exists a function that satisfies the Intermediate Value Theorem. gold=There exists a function that satisfies the Intermediate Value Theorem. time=22.69s
[ 5/78] OK    pred=Iruma’s graduation status is uncertain. gold=Iruma’s graduation status is uncertain. time=18.70s
[ 6/78] OK    pred=No       gold=No       time=17.83s
[ 7/78] WRONG pred=Yashiro passed the course. gold=It is uncertain whether Yashiro passed the course. time=26.88s
[ 8/78] OK    pred=Rillance stayed on the basketball team. gold=Rillance stayed on the basketball team. time=16.94s
[ 9/78] OK    pred=All gain knowledge. gold=All gain knowledge. time=29.89s
[10/78] OK    pred=((¬P(x) → ¬R(x)) → (U(x) → P(x))) gold=((¬P(x) → ¬R(x)) → (U(x) → P(x))) time=23.61s
[11/78] OK    pred=Philosophy failures → Advanced seminar seats. gold=Philosophy failures → Advanced seminar seats. time=22.56s
[12/78] OK    pred=Yes      gold=Yes      time=70.92s !! SLOW
[13/78] OK    pred=If there exists at least one object with property R, then every object has property P. gold=If there exists at least one object with property R, then every object has property P. time=23.85s
[14/78] OK    pred=Yes      gold=Yes      time=16.43s
[15/78] OK    pred=If participating in extracurricular activities helps students develop social skills, then understanding the material will help them perform well in exams. gold=If participating in extracurricular activities helps students develop social skills, then understanding the material will help them perform well in exams. time=20.48s
[16/78] OK    pred=Attending classes regularly, participating in extracurricular activities. gold=Attending classes regularly, participating in extracurricular activities. time=19.90s
[17/78] OK    pred=If there exists at least one student who has completed the Thesis Writing course, then all students are enrolled in Research Methods. gold=If there exists at least one student who has completed the Thesis Writing course, then all students are enrolled in Research Methods. time=25.90s
[18/78] OK    pred=Yes      gold=Yes      time=17.52s
[19/78] OK    pred=If a student completes the Thesis Writing course, then all students are enrolled in Research Methods. gold=If a student completes the Thesis Writing course, then all students are enrolled in Research Methods. time=19.43s
[20/78] OK    pred=Yes      gold=Yes      time=15.65s
[21/78] OK    pred=Uncertain. gold=Uncertain. time=17.02s
[22/78] OK    pred=If fairness leads to trustworthiness, then transparency implies auditability. gold=If fairness leads to trustworthiness, then transparency implies auditability. time=21.39s
[23/78] OK    pred=Yes      gold=Yes      time=15.14s
[24/78] OK    pred=∀x (L(x) → (C(x) ∧ P(x) ∧ G(x))) gold=∀x (L(x) → (C(x) ∧ P(x) ∧ G(x))) time=23.18s
[25/78] OK    pred=No       gold=No       time=21.47s
[26/78] OK    pred=∀x (¬A(x) → (¬R(x) ∧ ¬P(x))) gold=∀x (¬A(x) → (¬R(x) ∧ ¬P(x))) time=22.85s
[27/78] OK    pred=Yes      gold=Yes      time=17.39s
[28/78] OK    pred=∀x (P(x) → E(x)) gold=∀x (P(x) → E(x)) time=20.75s
[29/78] OK    pred=No       gold=No       time=16.89s
[30/78] OK    pred=Lan is allowed to enter the laboratory for Chemistry 101. gold=Lan is allowed to enter the laboratory for Chemistry 101. time=30.13s
[31/78] OK    pred=Yes      gold=Yes      time=27.71s
[32/78] OK    pred=Phong has an Average ranking. gold=Phong has an Average ranking. time=30.23s
[33/78] OK    pred=Yes      gold=Yes      time=29.60s
[34/78] OK    pred=If every teacher is respected, then someone must be prepared. gold=If every teacher is respected, then someone must be prepared. time=23.73s
[35/78] OK    pred=Yes      gold=Yes      time=21.52s
[36/78] OK    pred=All students have attended the Software Engineering workshop. gold=All students have attended the Software Engineering workshop. time=18.27s
[37/78] OK    pred=Yes      gold=Yes      time=27.15s
[38/78] OK    pred=Completing the prerequisite course implies eligibility for advanced courses. gold=Completing the prerequisite course implies eligibility for advanced courses. time=21.92s
[39/78] OK    pred=Yes      gold=Yes      time=23.89s
[40/78] OK    pred=Yes      gold=Yes      time=17.92s
[41/78] OK    pred=Participating in research, taking thesis course, being registered, receiving scholarship. gold=Participating in research, taking thesis course, being registered, receiving scholarship. time=20.62s
[42/78] OK    pred=Yes      gold=Yes      time=14.89s
[43/78] OK    pred=Theoretical knowledge, presentation skills, writing thesis, receiving certificate. gold=Theoretical knowledge, presentation skills, writing thesis, receiving certificate. time=21.80s
[44/78] OK    pred=Yes      gold=Yes      time=18.89s
[45/78] OK    pred=Completing training module, participating in project, giving seminar, earning certification. gold=Completing training module, participating in project, giving seminar, earning certification. time=20.90s
[46/78] WRONG pred=Uncertain gold=Yes      time=20.70s
[47/78] OK    pred=Writing a motivation letter, participating in the exchange program, having a high TOEFL score. gold=Writing a motivation letter, participating in the exchange program, having a high TOEFL score. time=22.62s
[48/78] OK    pred=If some student is allowed to enroll, then passing Classical Mechanics implies they can take Data Structures. gold=If some student is allowed to enroll, then passing Classical Mechanics implies they can take Data Structures. time=28.84s
[49/78] OK    pred=Yes      gold=Yes      time=18.31s
[50/78] OK    pred=∀x (F(x) → (W(x) ∧ R(x))) gold=∀x (F(x) → (W(x) ∧ R(x))) time=38.68s
[51/78] OK    pred=Yes      gold=Yes      time=33.51s
[52/78] OK    pred=∀x (C(x) → (U(x) ∧ W(x))) gold=∀x (C(x) → (U(x) ∧ W(x))) time=45.57s
[53/78] OK    pred=Yes      gold=Yes      time=36.10s
[54/78] OK    pred=The Amber Amulet must be displayed in a climate-controlled case gold=The Amber Amulet must be displayed in a climate-controlled case time=38.81s
[55/78] OK    pred=The River Codex is searchable online, but safe public release is not established gold=The River Codex is searchable online, but safe public release is not established time=34.46s
[56/78] OK    pred=MedKit-7 is eligible to use the aerial corridor gold=MedKit-7 is eligible to use the aerial corridor time=33.32s
[57/78] OK    pred=Mira enters the antiviral protocol and requires dose review gold=Mira enters the antiviral protocol and requires dose review time=33.44s
[58/78] OK    pred=Autonomous watering is allowed for Greenhouse Basil gold=Autonomous watering is allowed for Greenhouse Basil time=32.04s
[59/78] OK    pred=Batch Nova can be administered gold=Batch Nova can be administered time=28.74s
[60/78] OK    pred=The Atlas case is audit-ready, but formal closure is not established by the premises gold=The Atlas case is audit-ready, but formal closure is not established by the premises time=34.72s
[61/78] OK    pred=A temporary no-take zone is recommended for Azure Reef gold=A temporary no-take zone is recommended for Azure Reef time=30.79s
[62/78] OK    pred=Linh receives a blue access badge gold=Linh receives a blue access badge time=30.26s
[63/78] OK    pred=Manuscript Nova is eligible for open science recognition gold=Manuscript Nova is eligible for open science recognition time=26.53s
[64/78] OK    pred=Robot Kappa can pick inventory items gold=Robot Kappa can pick inventory items time=23.10s
[65/78] OK    pred=Satellite Vega can monitor surface temperature and capture daytime images gold=Satellite Vega can monitor surface temperature and capture daytime images time=24.38s
[66/78] OK    pred=Asha may join Study Alpha gold=Asha may join Study Alpha time=24.13s
[67/78] OK    pred=Yes      gold=Yes      time=35.08s
[68/78] OK    pred=Yes      gold=Yes      time=31.85s
[69/78] OK    pred=Yes      gold=Yes      time=29.90s
[70/78] OK    pred=Yes      gold=Yes      time=28.41s
[71/78] OK    pred=No       gold=No       time=27.00s
[72/78] OK    pred=No       gold=No       time=26.12s
[73/78] OK    pred=Uncertain gold=Uncertain time=14.52s
[74/78] OK    pred=Yes      gold=Yes      time=32.40s
[75/78] WRONG pred=No       gold=Uncertain time=34.20s
[76/78] OK    pred=No       gold=No       time=40.06s
[77/78] WRONG pred=Yes      gold=Uncertain time=46.19s
[78/78] OK    pred=Uncertain gold=Uncertain time=13.12s
```

## Files

| File | Description |
|------|-------------|
| `ensemble_eval_log.jsonl` | Full detail per sample (NL, FOL gold, FOL generated, question, gold, prediction, latency) |
| `ensemble_eval_summary.json` | Summary statistics |
| `eval_log.txt` | Plain text evaluation log |
| `README.md` | This file |

## Team

**Laplace's Red Devils** — EXACT 2026 Competition
