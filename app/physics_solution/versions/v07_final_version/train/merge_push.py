"""Merge LoRA -> full weights and push BOTH the adapter and the merged model to
the Hub, each with a model card recording everything needed to reload exactly.

- adapter repo : LoRA adapter + tokenizer (small; load on top of the base).
- merged  repo : full fp16/bf16 weights (vLLM serves this directly).

Merge is done with plain PEFT on CPU (deterministic, framework-agnostic) so the
result reloads with vanilla transformers — no Unsloth needed at serve time.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import torch
from huggingface_hub import HfApi
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def _hf_token() -> str:
    for k in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "HUGGINGFACE_HUB_TOKEN"):
        v = (os.environ.get(k) or "").strip()
        if v:
            return v
    raise RuntimeError("No HF token in env (HF_TOKEN / HUGGING_FACE_HUB_TOKEN).")


def _model_card(cfg: dict, repo: str, metrics: dict, kind: str) -> str:
    m, lo, t = cfg["model"], cfg["lora"], cfg["training"]
    acc = metrics.get("accuracy", {})
    acc_lines = "\n".join(f"- **{k}**: {v}" for k, v in acc.items()) or "- (run `eval.py` to fill)"
    return f"""---
license: apache-2.0
base_model: {m['name']}
library_name: {'peft' if kind == 'adapter' else 'transformers'}
tags:
  - exact-2026
  - physics
  - program-of-thoughts
  - qlora
---

# {repo.split('/')[-1]}

v07 SFT of **{m['name']}** for EXACT-2026 Task-2 physics: emit a short (5-10 line)
reasoning preamble then ONE Python code block that computes `FINAL ANSWER:` / `UNIT:`.
{'LoRA adapter (+ tokenizer). Load on top of the base.' if kind == 'adapter' else 'Merged full model — serve directly with vLLM.'}

## Training
- Method: {'QLoRA (NF4)' if m.get('load_in_4bit') else '16-bit LoRA'}, train-on-completion (loss on the assistant turn only).
- LoRA: r={lo['r']}, alpha={lo['alpha']}, dropout={lo['dropout']}, targets={lo['target_modules']}.
- Epochs={t['num_train_epochs']}, lr={t['learning_rate']}, eff_batch={int(t['per_device_train_batch_size'])*int(t['gradient_accumulation_steps'])}, max_seq_len={m['max_seq_length']}.
- Data: {metrics.get('n_train')} train / {metrics.get('n_val')} val trajectories (golden_60 held out).
- Chat template: Qwen `<|im_start|>`/`<|im_end|>`; eos `<|im_end|>`, pad `<|endoftext|>`.

## Metrics
- train_loss: {metrics.get('train_loss')}
- best_eval_loss: {metrics.get('best_eval_loss')}
{acc_lines}

External hint/teacher data used during data-gen is declared in the Data Disclosure Document.
"""


def _push_folder(api: HfApi, repo: str, folder: str, token: str, private: bool) -> None:
    api.create_repo(repo, private=private, exist_ok=True, token=token)
    api.upload_folder(repo_id=repo, folder_path=folder, token=token)


def merge_and_push(cfg: dict, adapter_dir: str, metrics: dict) -> dict:
    token = _hf_token()
    org = cfg["hub"]["org"]
    private = bool(cfg["hub"].get("private", True))
    adapter_repo = f"{org}/{cfg['hub']['adapter_repo']}"
    merged_repo = f"{org}/{cfg['hub']['merged_repo']}"
    api = HfApi(token=token)

    # --- adapter repo ---
    (Path(adapter_dir) / "README.md").write_text(_model_card(cfg, adapter_repo, metrics, "adapter"))
    _push_folder(api, adapter_repo, adapter_dir, token, private)

    # --- merge on CPU ---
    base = AutoModelForCausalLM.from_pretrained(
        cfg["model"]["name"], torch_dtype="auto",
        trust_remote_code=bool(cfg["model"].get("trust_remote_code", True)), device_map="cpu",
    )
    merged = PeftModel.from_pretrained(base, adapter_dir).merge_and_unload()
    merged_dir = Path(cfg["paths"]["merged_dir"])
    merged_dir.mkdir(parents=True, exist_ok=True)
    merged.save_pretrained(str(merged_dir))

    tok = AutoTokenizer.from_pretrained(adapter_dir, trust_remote_code=True)
    tok.save_pretrained(str(merged_dir))
    (merged_dir / "README.md").write_text(_model_card(cfg, merged_repo, metrics, "merged"))
    _push_folder(api, merged_repo, str(merged_dir), token, private)

    del base, merged
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return {"adapter": f"https://huggingface.co/{adapter_repo}",
            "merged": f"https://huggingface.co/{merged_repo}"}
