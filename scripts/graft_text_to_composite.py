#!/usr/bin/env python
"""Graft a text-only Qwen3.5 finetune onto the composite base so vLLM can serve it.

WHY this exists
---------------
Our finetuned checkpoints (physics-merged, fol-pretrain, qa) are saved as the
**text-only** arch ``Qwen3_5ForCausalLM`` / model_type ``qwen3_5_text``:
only the 426 ``model.language_model.*`` tensors, tied embeddings, NO vision tower.
vLLM 0.22.1 registers ONLY the **composite** ``Qwen3_5ForConditionalGeneration``
(model_type ``qwen3_5``: language_model + visual + mtp). So the text-only
checkpoints are NOT directly servable.

The fix is pure tensor surgery: the base ``Qwen/Qwen3.5-4B`` (composite) has the
*identical* 426 ``model.language_model.*`` keys plus 297 ``model.visual.*`` + a
few ``mtp.*``. We take the base composite and OVERWRITE its ``language_model.*``
with the finetune's, keeping the base's visual+mtp and config verbatim. Result =
a valid composite checkpoint whose text path is our finetune (vision is dead
weight, never exercised by text-only chat — same as how we already serve the base
composite text-only for physics). This is the full-weight analogue of the
base+LoRA trick used for the physics SFT adapter.

Usage
-----
    HF_HOME=/dev/shm/hf python scripts/graft_text_to_composite.py \
        --finetune Laplaces-Red-Devils/fol-pretrain-malls-qwen3.5-4b \
        --out /dev/shm/models/fol-composite

Idempotent: skips if <out>/.graft_done exists. Writes a single model.safetensors
(vLLM reads it fine) + composite config from base + tokenizer/chat_template from
the finetune (same vocab, but the finetune's chat template is what it was trained
with).
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import torch
from huggingface_hub import snapshot_download
from safetensors import safe_open
from safetensors.torch import save_file

LM_PREFIX = "model.language_model."
# config goes from the COMPOSITE base; tokenizer/template from the FINETUNE.
FROM_BASE = ["config.json", "generation_config.json", "preprocessor_config.json",
             "video_preprocessor_config.json", "merges.txt", "vocab.json"]
FROM_FINETUNE = ["tokenizer.json", "tokenizer_config.json", "chat_template.jinja"]


def _snapshot(repo: str) -> Path:
    if Path(repo).exists():
        return Path(repo)
    return Path(snapshot_download(repo))


def _load_safetensors_dir(d: Path, want) -> dict[str, torch.Tensor]:
    """Load tensors whose key passes ``want(key)`` from every *.safetensors in d."""
    out: dict[str, torch.Tensor] = {}
    files = sorted(d.glob("*.safetensors")) + sorted(d.glob("*.safetensors-*"))
    seen = set()
    for f in files:
        if f.name in seen:
            continue
        seen.add(f.name)
        with safe_open(str(f), framework="pt") as s:
            for k in s.keys():
                if want(k):
                    out[k] = s.get_tensor(k).contiguous()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="Qwen/Qwen3.5-4B")
    ap.add_argument("--finetune", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    if (out / ".graft_done").exists():
        print(f"[graft] {out} already done — skip.")
        return
    out.mkdir(parents=True, exist_ok=True)

    base_dir = _snapshot(args.base)
    ft_dir = _snapshot(args.finetune)
    print(f"[graft] base={base_dir}\n[graft] finetune={ft_dir}\n[graft] out={out}")

    # finetune: the language_model tensors (the *only* thing it has)
    ft_lm = _load_safetensors_dir(ft_dir, lambda k: k.startswith(LM_PREFIX))
    # base: everything EXCEPT language_model (visual tower + mtp head + any extras)
    base_rest = _load_safetensors_dir(base_dir, lambda k: not k.startswith(LM_PREFIX))
    base_lm_keys = set(_load_safetensors_dir(base_dir, lambda k: k.startswith(LM_PREFIX)).keys())

    missing = base_lm_keys - set(ft_lm)
    extra = set(ft_lm) - base_lm_keys
    if missing or extra:
        raise SystemExit(f"[graft] language_model key mismatch!\n  missing in finetune: "
                         f"{sorted(missing)[:5]}...\n  extra in finetune: {sorted(extra)[:5]}...")
    print(f"[graft] lm tensors={len(ft_lm)}  base-rest(visual+mtp)={len(base_rest)}  (keys match ✓)")

    merged = {**base_rest, **ft_lm}          # base visual+mtp + finetuned language_model
    save_file(merged, str(out / "model.safetensors"), metadata={"format": "pt"})
    print(f"[graft] wrote model.safetensors ({len(merged)} tensors)")

    for fn in FROM_BASE:
        src = base_dir / fn
        if src.exists():
            shutil.copy2(src, out / fn)
    for fn in FROM_FINETUNE:
        src = ft_dir / fn
        if src.exists():
            shutil.copy2(src, out / fn)

    # sanity: config must be the composite arch vLLM serves
    cfg = json.loads((out / "config.json").read_text())
    assert cfg.get("architectures") == ["Qwen3_5ForConditionalGeneration"], cfg.get("architectures")

    (out / ".graft_done").write_text("ok\n")
    print(f"[graft] DONE -> {out}  (arch {cfg['architectures']}, model_type {cfg['model_type']})")


if __name__ == "__main__":
    main()
