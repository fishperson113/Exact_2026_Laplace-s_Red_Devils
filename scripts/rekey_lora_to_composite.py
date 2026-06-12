#!/usr/bin/env python3
"""Re-key a LoRA adapter so vLLM actually applies it on the COMPOSITE Qwen3.5-4B base.

Why: vLLM 0.22.1 can only serve the composite ``Qwen3_5ForConditionalGeneration`` (its LM
lives under ``model.language_model.*``). A LoRA trained on the text-only ``Qwen/Qwen3.5-4B``
exports keys like ``base_model.model.model.layers.N...`` (no ``language_model``). vLLM loads
such an adapter WITHOUT error but binds it to modules that don't exist on the composite, so it
is a silent **no-op** — serving the adapter id returns byte-identical output to the base. This
script inserts the ``language_model`` segment so the keys match the composite's module paths.

Idempotent: an adapter already in the composite namespace (e.g. physics-v07c-sft, whose keys
already contain ``language_model``) is copied through unchanged (0 keys re-keyed).

Usage:
    python scripts/rekey_lora_to_composite.py --adapter <hf_repo_or_local_dir> --out <dir>
"""
from __future__ import annotations

import argparse
import os
import shutil

from safetensors.torch import load_file, save_file

OLD = "base_model.model.model.layers."
NEW = "base_model.model.model.language_model.layers."


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--adapter", required=True, help="HF repo id or local adapter dir")
    ap.add_argument("--out", required=True, help="output dir for the (re-keyed) adapter")
    args = ap.parse_args()

    src = args.adapter
    if not os.path.isdir(src):
        from huggingface_hub import snapshot_download
        src = snapshot_download(args.adapter)

    weights = os.path.join(src, "adapter_model.safetensors")
    if not os.path.isfile(weights):
        raise SystemExit(f"[rekey] no adapter_model.safetensors in {src}")

    os.makedirs(args.out, exist_ok=True)
    sd = load_file(weights)
    out, n = {}, 0
    for k, v in sd.items():
        if k.startswith(OLD):
            k = NEW + k[len(OLD):]
            n += 1
        out[k] = v
    save_file(out, os.path.join(args.out, "adapter_model.safetensors"))
    for f in os.listdir(src):                       # adapter_config.json + any other json
        if f.endswith(".json"):
            shutil.copy(os.path.join(src, f), os.path.join(args.out, f))
    print(f"[rekey] {args.adapter}: {len(sd)} tensors, re-keyed {n} -> {args.out}"
          + ("  (already composite-namespace)" if n == 0 else ""))


if __name__ == "__main__":
    main()
