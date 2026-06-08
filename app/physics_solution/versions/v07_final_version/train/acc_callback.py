"""Best-checkpoint selection by EXECUTION ACCURACY (not eval_loss).

For code-gen, eval_loss is a poor proxy — many different token sequences map to a
correct program, so lowest loss != highest accuracy. Mirrors FOL's
`FolDevRMForBestModelCallback`: each epoch, generate on the val problems, run the
code, score the executed answer, and inject `metrics["eval_accuracy"]` so the
Trainer (metric_for_best_model=eval_accuracy) and EarlyStopping select on what we
actually care about.

Generation matches inference exactly: enable_thinking=False, left padding.
"""

from __future__ import annotations

import gc
import importlib
import json
import os

import torch
from transformers import TrainerCallback

# Generating inside the training loop competes with optimizer/grad memory; reduce
# fragmentation so the KV cache fits in the headroom on a 40 GB A100.
os.environ.setdefault("PYTORCH_ALLOC_CONF", "expandable_segments:True")

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.versions.v05_best.code_executor import execute_code, extract_code
from app.physics_solution.versions.v06_finetune.data_pipeline.prompts import build_gen_messages


def _inner_tok(obj):
    """Unsloth may return a multimodal *processor* wrapping the real text tokenizer.
    Calling processor(text) routes text to the image path -> PIL error. Unwrap it for
    encode/decode; apply_chat_template stays on the processor (it holds the template)."""
    t = getattr(obj, "tokenizer", None)
    if t is not None and hasattr(t, "convert_ids_to_tokens"):
        return t
    return obj


def _disable_flex_attention() -> None:
    for name in ("transformers.modeling_utils", "transformers.utils", "transformers"):
        try:
            mod = importlib.import_module(name)
            if hasattr(mod, "is_torch_flex_attn_available"):
                mod.is_torch_flex_attn_available = lambda: False  # type: ignore[assignment]
        except Exception:
            pass


class ExecAccuracyCallback(TrainerCallback):
    def __init__(self, tokenizer, val_problems_jsonl: str, max_samples: int | None = 56,
                 max_new_tokens: int = 1024, batch_size: int = 16):
        self.proc = tokenizer            # processor (has chat_template)
        self.tok = _inner_tok(tokenizer)  # real text tokenizer (encode/decode)
        rows = [json.loads(l) for l in open(val_problems_jsonl) if l.strip()]
        self.problems = rows[:max_samples] if max_samples else rows
        self.max_new_tokens = max_new_tokens
        self.batch_size = batch_size
        self.history: list[tuple[float, float]] = []  # (epoch, accuracy)
        _disable_flex_attention()

    def _prompt(self, p: dict) -> str:
        msgs = build_gen_messages(p["question"], p["domain"], p["answer_type"])
        try:
            return self.proc.apply_chat_template(
                msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        except TypeError:
            return self.proc.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

    @torch.no_grad()
    def on_evaluate(self, args, state, control, metrics=None, model=None, **kwargs):
        if metrics is None or model is None:
            return
        tok = self.tok
        model.eval()
        gc.collect()
        torch.cuda.empty_cache()  # free training fragmentation before generation
        prev_pad = tok.padding_side
        tok.padding_side = "left"
        prev_cache = getattr(model.config, "use_cache", None)
        try:
            model.config.use_cache = True
        except Exception:
            pass
        # Unsloth: switch LoRA to inference mode so generate() doesn't keep training-mode
        # buffers (otherwise the KV/activation memory isn't released and the resumed
        # backward pass OOMs on a 40 GB A100).
        FLM = None
        try:
            from unsloth import FastLanguageModel as FLM
            FLM.for_inference(model)
        except Exception:
            FLM = None

        n_ok = 0
        probs = self.problems
        try:
            for s in range(0, len(probs), self.batch_size):
                batch = probs[s:s + self.batch_size]
                enc = tok([self._prompt(p) for p in batch], return_tensors="pt",
                          padding=True, truncation=True, max_length=2048).to(model.device)
                out = model.generate(
                    **enc, max_new_tokens=self.max_new_tokens, do_sample=False,
                    pad_token_id=tok.pad_token_id or tok.eos_token_id,
                    eos_token_id=tok.eos_token_id)
                texts = tok.batch_decode(out[:, enc["input_ids"].shape[1]:],
                                         skip_special_tokens=True)
                for p, t in zip(batch, texts):
                    code = extract_code(t)
                    stdout = execute_code(code).stdout or "" if code else ""
                    if evaluator.score(stdout, p["gold_answer"], p["gold_unit"]).is_correct:
                        n_ok += 1
                del enc, out, texts          # free this batch's KV/activations now
                torch.cuda.empty_cache()
        finally:
            if FLM is not None:
                try:
                    FLM.for_training(model)  # restore trainable LoRA before training resumes
                except Exception:
                    pass
            tok.padding_side = prev_pad
            try:
                model.config.use_cache = prev_cache
            except Exception:
                pass
            gc.collect()
            torch.cuda.empty_cache()  # release KV cache before training resumes

        acc = n_ok / len(probs) if probs else 0.0
        metrics["eval_accuracy"] = acc
        self.history.append((float(state.epoch or 0), acc))
        print(f"[acc-callback] epoch={float(state.epoch or 0):.2f} "
              f"eval_accuracy={acc:.4f} ({n_ok}/{len(probs)})", flush=True)
