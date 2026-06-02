---
base_model: Qwen/Qwen2.5-3B-Instruct
library_name: peft
pipeline_tag: text-generation
license: apache-2.0
language:
- en
tags:
- base_model:adapter:Qwen/Qwen2.5-3B-Instruct
- lora
- sft
- transformers
- trl
- logic
- qa
- chain-of-thought
- education
datasets:
- Logic_Based_Educational_Queries
---

# QA Stage 2 — COT Reasoning (NL + FOL → Answer + Explanation)

LoRA adapter for **Qwen/Qwen2.5-3B-Instruct**, fine-tuned on the Logic-Based Educational Queries dataset. Given natural-language premises, their FOL translations, and a question, the model reasons step-by-step and outputs a JSON answer with explanation.

## Pipeline

```
NL premises + FOL premises + Question
        |
  QA COT Model (this adapter)
        |
  {"answer": "B", "explanation": "Premise 1 states..."}
```

This model is **Stage 2** in a two-stage ensemble:
1. **Stage 1 (FOL Model)**: NL → FOL ([fol-v05-cot-augmented](https://huggingface.co/Laplaces-Red-Devils/fol-v05-cot-augmented-fol-pretrain-malls-qwen2.5-3))
2. **Stage 2 (This Model)**: NL + FOL + Question → Answer + Explanation

## Accuracy (Dev set, 40 samples)

| Epoch | Raw Accuracy | Avg Latency |
|-------|-------------|-------------|
| 1 | 20.0% | 20.6s |
| 5 | 52.5% | 13.2s |
| 10 | 47.5% | 17.0s |
| 15 | 50.0% | 11.3s |
| 19 | 55.0% | 10.3s |
| 20 | 55.0% | 10.3s |
| 25 | 55.0% | 11.4s |
| **29** | **57.5%** | **11.2s** |
| 30 | 52.5% | 11.7s |

**Best raw accuracy: 57.5% (23/40) at epoch 29**

### Adjusted Accuracy (corrected gold labels)

5 samples in the dev set have **gold label errors** — the gold explanation contradicts the gold answer label. After manual verification, the model predicted correctly on all 5.

| Sample | Gold (wrong) | Corrected | Pred | Evidence |
|--------|-------------|-----------|------|----------|
| 4 | Unknown | A | A | Explanation: "Option A is most effective because..." |
| 20 | No | Yes | Yes | Explanation: "So such a programmer exists" |
| 25 | No | Yes | Yes | Explanation: "Therefore, JavaScript supports..." |
| 28 | No | Yes | Yes | Explanation: "Thus, all committee members approve" |
| 29 | No | Yes | Yes | Explanation: "Thus, all faculty members think..." |

**Adjusted accuracy: 70.0% (28/40)**

## Training Details

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Base model | `Qwen/Qwen2.5-3B-Instruct` |
| Method | LoRA (PEFT) |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj |
| Trainable params | 3,686,400 (0.12%) |
| Epochs | 30 (early stop patience=7) |
| Batch size | 1 (gradient accumulation=8, effective=8) |
| Learning rate | 2e-5 |
| Warmup ratio | 0.05 |
| Weight decay | 0.01 |
| Precision | INT8 (bitsandbytes) |
| Max seq length | 3500 |
| Seed | 42 |

### Training Loss Curve

| Epoch | Train Loss | Eval Loss | Token Accuracy |
|-------|-----------|-----------|----------------|
| 1 | 1.487 | 1.468 | 69.8% |
| 3 | 0.854 | 0.420 | 89.9% |
| 5 | 0.370 | 0.380 | 90.4% |
| 10 | 0.345 | 0.347 | 91.1% |
| 15 | 0.333 | 0.328 | 91.5% |
| 20 | 0.328 | 0.319 | 91.7% |
| 24 | 0.321 | **0.316** | 91.8% |
| 25 | 0.315 | 0.316 | 91.9% |

**Best eval_loss: 0.3155 at step 1944 (epoch 24)**

### Dataset

- **Task**: Logic-Based Educational Queries (MCQ + Yes/No)
- **Train**: 647 QA samples (328 records)
- **Dev**: 79 QA samples (41 records)
- **Test**: 81 QA samples (41 records)
- **Input**: NL premises + FOL premises + Question
- **Output**: JSON `{"answer": "<label>", "explanation": "<reasoning>"}`

### Training Infrastructure

- **Hardware**: NVIDIA L4 (24GB VRAM)
- **Platform**: Modal Cloud
- **Training time**: ~6 hours (30 epochs)

## Usage

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct", device_map="auto")
model = PeftModel.from_pretrained(base_model, "Laplaces-Red-Devils/qa-v01-cot-Qwen2.5-3B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")

messages = [
    {"role": "system", "content": "You are a logic-based educational QA system..."},
    {"role": "user", "content": "Premises (NL):\n1. If a student attends lectures...\n\nPremises (FOL):\n1. ∀x (AttendsLectures(x) → UnderstandsMaterial(x))\n\nQuestion:\nWhich conclusion is best supported?\nA. ...\nB. ..."},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=200, do_sample=False)
print(tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
# {"answer": "B", "explanation": "Premise 1 states..."}
```

## Framework Versions

- PEFT: 0.19.1
- Transformers: 4.52.4
- TRL: 0.18.1
- PyTorch: 2.10.0+cu128
- BitsAndBytes: 0.46.0

## Team

**Laplace's Red Devils** — EXACT 2026 Competition
