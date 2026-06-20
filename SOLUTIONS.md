# EXACT 2026 — Solution Description · Team **Laplace's Red Devils**

**One** endpoint `POST /predict`, routed by the `type` field: `type1` → Logic pipeline (FOL + QA), `type2` → Physics pipeline (compute + CoT). Returns a JSON **list** of `{query_id, answer, unit, explanation, premises_used, reasoning}`. Every LLM is **Qwen3.5-4B**, served via **vLLM** (each server exposes `/v1/models` for committee verification).

---

## 1. Datasets used

| Scenario | Dataset | Source / Origin | Samples used | Role |
|---|---|---|---|---|
| **Type 1** | EXACT 2026 official (logic) | Organizer — `train/dev/test.csv` | **~630** records (filtered `len(premises_nl)==len(premises_fol)>0`) | Stage 2 target (gold FOL + answer) |
| **Type 1** | MALLS-v0.1 (NL→FOL) | External — HuggingFace (LogicLLaMA, ACL'24, arXiv:2305.15541) | 28,284 normalized → **random 5,000** (seed 3407) | Stage 1 pretrain (FOL syntax warmup) |
| **Type 1** | Reasoning CoT (augmented) | **Synthetic — Claude Sonnet 4.6** | `Rule/Fact/Derive/Conclusion` chain per train/dev/test question | Stage 2 QA target (validated, no invented predicates) |
| **Type 2** | EXACT 2026 official (physics) | Organizer (1318) + **Vietjack** crawl (353) → QC | 1671 → **1584** clean (CLEAN+FIX, execution-grounded) | Source for trajectory generation |
| **Type 2** | SFT trajectories (PoT) | **Synthetic self-gen** (Qwen3.5-4B, on-policy) | **2,846 traj / 1,505 problems** (cap 2 diverse/problem) | SFT target (5–10 line reasoning + ONE code block) |
| **Type 2** | `hint_code` (method hint) | **External** — DeepSeek / Claude (**only shown to the model on problems it solved INCORRECTLY itself**; never used at inference) | 1550/1584 | Hinted route (residual) + QC verify |
| **Type 2** | `val_56` / `golden_60` | Organizer | 56 / 60 (held-out) — **these are the two test sets** | Evaluation, **never** trained on (leak-guarded) |

> *Type 1 input sample:* `{premises:["A student with ≥120 credits is eligible.","Student A has 118 credits."], query:"Is Student A eligible?", options:["Yes","No","Uncertain"]}`. *Type 2 sample:* `{query:"A 2 µF capacitor charged to 12 V stores how much energy?"}` → `answer:"1.44e-4", unit:"J"`.

---

## 2. Approach & Method

### Type 1 — Logic (two fine-tuned models in series)
- **Model 1 — FOL Translator** (`fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4`, full finetune): NL premises → `premises_fol`. Trained with a **two-stage curriculum**: *Stage 1* pretrain on MALLS 5K (learn general FOL syntax) → *Stage 2* fine-tune on the official set. Best model is selected by **RM = 0.6·LE + 0.4·BLEU** (LE = logical equivalence checked with **Z3**; BLEU = n-gram overlap on FOL) instead of exact-match.
- **Model 2 — QA CoT Reasoner** (`v04-QA-CoT`, LoRA): takes NL + FOL + question → emits `Rule/Fact/Derive/Conclusion` steps, then a final **JSON `{premises_used, explanation, answer}` last** (reason first, commit the answer last). Reasoning steps augmented with **Claude Sonnet 4.6**.
- **Core principle:** both models are trained INDEPENDENTLY on **GOLD FOL** (teacher forcing); they are **chained only at inference** (Model 1 emits FOL → Model 2 consumes it). `premises_used` (0-based) comes from Model 2's output (50% of the Type 1 score).

### Type 2 — Physics (SFT Program-of-Thought + self-consistency / ensemble)
- **Solver — `physics-v07c-sft-qwen3.5-4b`** (16-bit LoRA, r8 q/k/v/o; lossless merge): emits **short reasoning (5–10 lines) + EXACTLY one Python block** → executed in a sandbox (scipy/sympy, no GPU) → parse `FINAL ANSWER:` / `UNIT:`. Physical constants are hardcoded; computed values are **never** hardcoded.
- **Serving pipeline (`v07_ensemble_vLLM`):** classify (domain, answer_type) → **BASE & SFT each sample K=5 concurrently** (one vLLM engine batches all 10 sequences) → execute all → **pooled vote over 10 answers, majority cluster wins** (predictions only, never the gold) → **BASE writes the `explanation` + `cot`** for the chosen answer (does not change it). Deadline-safe < 60 s.
- **Results (RTX 5090):** v07c + SC K=5 = **val 0.875 / golden 0.817**; pooled ensemble = **0.869 / 0.789** (kept because it is nearly free and raises the floor). Latency median ~6.5–9 s ≪ 60 s. Remaining bottleneck: electrostatics vector-superposition (a data lever, not a serving issue).

---

## 3. Model size calculation (≤ 8B)

Serving mode `combined` — **two vLLM servers on one GPU**, every model is **Qwen3.5-4B**:

| vLLM server | Model / adapter | Params | Role |
|---|---|---|---|
| `:18000` | base **Qwen3.5-4B** + LoRA `sft` (physics-v07c) + LoRA `qa` (v04-QA-CoT) | ~**4B** (+ tiny PEFT adapters, not counted) | Type 2 solver/judge · Type 1 QA stage-2 |
| `:18001` | `fol` = `fol-v06-cot-augmented…` (full finetune, grafted composite) | ~**4B** | Type 1 stage-1 NL→FOL |

**Peak concurrent = base 4B + fol 4B = ~8B** (LoRA adapters are small deltas, not added) → **within the 8B-class limit** (Guide §6.3: "two 4B models in parallel" is allowed). Measured VRAM ~26.7/32 GB. Non-LLM tools (Z3 solver, code-execution sandbox) do not count toward the limit. The FastAPI gateway `:9000` exposes `/predict`; each vLLM server exposes its own `/v1/models` (`:18000` → base, sft, qa · `:18001` → fol) for committee verification.
