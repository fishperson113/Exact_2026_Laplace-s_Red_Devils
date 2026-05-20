"""Model + tokenizer loading and a tiny generate() helper.

Supported dtypes (passed via --dtype):
- fp32 / fp16 / bf16: standard torch dtypes, work on CPU and GPU.
- int8:  CPU-friendly 8-bit *weight* quantisation via
         `torch.quantization.quantize_dynamic` on Linear layers. This is
         the closest pure-torch analogue to FP8 that runs on CPU without
         extra dependencies (true FP8 needs Hopper GPU + vLLM).
- fp8:   Loads in bf16 and applies FP8 weight quantisation if running on
         a CUDA device that supports it (Hopper / Ada). On CPU we transparently
         fall back to int8 and emit a warning.

vLLM is the right serving path for FP8/AWQ/GPTQ on GPU; this loader stays
HF-Transformers-based so the same code runs locally on CPU and on Colab GPU.
"""

from __future__ import annotations

import os
import time
import warnings
from dataclasses import dataclass

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

DTYPE_MAP = {
    "fp32": torch.float32,
    "fp16": torch.float16,
    "bf16": torch.bfloat16,
}

VALID_DTYPES = ("fp32", "fp16", "bf16", "int8", "fp8")


@dataclass
class LoadedModel:
    tokenizer: object
    model: object
    model_id: str
    dtype: str
    effective_dtype: str
    device: str


def _quantize_int8_dynamic(model: torch.nn.Module) -> torch.nn.Module:
    """Dynamic INT8 weight quantisation on Linear layers. CPU-only.

    Halves the memory footprint of the Linear weight matrices vs fp16 and
    typically gives a moderate speed-up on CPUs with AVX512_VNNI.
    """
    return torch.quantization.quantize_dynamic(
        model, {torch.nn.Linear}, dtype=torch.qint8
    )


def load_model(
    model_id: str,
    dtype: str = "fp16",
    device: str = "cpu",
    trust_remote_code: bool = True,
) -> LoadedModel:
    if dtype not in VALID_DTYPES:
        warnings.warn(f"Unknown dtype={dtype!r}; falling back to fp16")
        dtype = "fp16"

    # Decide the load-time torch dtype + whether to post-quantise.
    if dtype == "int8":
        load_dtype = torch.float32  # quantize_dynamic expects fp32 source
        post_quantise = "int8"
    elif dtype == "fp8":
        if device.startswith("cuda") and torch.cuda.is_available():
            load_dtype = torch.bfloat16
            post_quantise = "fp8"
        else:
            warnings.warn(
                "fp8 requested but no CUDA device available — falling back to int8 on CPU."
            )
            load_dtype = torch.float32
            post_quantise = "int8"
    else:
        load_dtype = DTYPE_MAP[dtype]
        post_quantise = None

    tokenizer = AutoTokenizer.from_pretrained(
        model_id, trust_remote_code=trust_remote_code
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=load_dtype,
        trust_remote_code=trust_remote_code,
        low_cpu_mem_usage=True,
    )
    model.to(device)

    effective_dtype = dtype
    if post_quantise == "int8":
        if device != "cpu":
            warnings.warn(
                "int8 dynamic quantisation runs on CPU; moving model to CPU before quantising."
            )
            model = model.to("cpu")
            device = "cpu"
        model = _quantize_int8_dynamic(model)
        effective_dtype = "int8"
    elif post_quantise == "fp8":
        # Hopper / Ada path. Use torchao if available; otherwise leave bf16.
        try:
            from torchao.quantization import quantize_, Float8DynamicActivationFloat8WeightConfig

            quantize_(model, Float8DynamicActivationFloat8WeightConfig())
            effective_dtype = "fp8"
        except Exception as e:
            warnings.warn(
                f"fp8 quantisation via torchao failed ({e}); staying at bf16."
            )
            effective_dtype = "bf16"

    model.eval()

    return LoadedModel(
        tokenizer=tokenizer,
        model=model,
        model_id=model_id,
        dtype=dtype,
        effective_dtype=effective_dtype,
        device=device,
    )


def has_chat_template(tokenizer) -> bool:
    return getattr(tokenizer, "chat_template", None) is not None


def render_prompt(
    tokenizer,
    messages: list[dict],
    raw_fallback: str,
    assistant_prefix: str = "",
    enable_thinking: bool = False,
) -> str:
    """Use chat template if present, else fall back to a raw prompt string.

    `assistant_prefix` is appended after the generation prompt marker so
    the model is forced to continue from that text. Use it to prefill the
    first tokens of the assistant turn (e.g. "Step 1:") and suppress
    preambles.

    `enable_thinking=False` disables Qwen3.5's default `<think>...</think>`
    block. Silently ignored if the tokenizer's chat template doesn't
    declare the kwarg (other model families).
    """
    if has_chat_template(tokenizer):
        try:
            prompt = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=enable_thinking,
            )
        except TypeError:
            prompt = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
    else:
        prompt = raw_fallback
    if assistant_prefix:
        # Some chat templates already end with a trailing newline after the
        # assistant marker; just append without inserting another one.
        prompt = prompt + assistant_prefix
    return prompt


def _prepare_tokenizer_for_padding(tokenizer) -> None:
    """Left-padding is required for causal-LM batched generation."""
    tokenizer.padding_side = "left"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token


@torch.inference_mode()
def generate_text(
    loaded: LoadedModel,
    prompt: str,
    max_new_tokens: int = 512,
    temperature: float = 0.0,
    top_p: float = 1.0,
) -> tuple[str, float]:
    """Return (decoded_completion, elapsed_seconds). Completion excludes the prompt."""
    tokenizer = loaded.tokenizer
    model = loaded.model

    inputs = tokenizer(prompt, return_tensors="pt").to(loaded.device)
    input_len = inputs["input_ids"].shape[1]

    do_sample = temperature > 0.0
    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        pad_token_id=tokenizer.eos_token_id,
    )
    if do_sample:
        gen_kwargs["temperature"] = temperature
        gen_kwargs["top_p"] = top_p

    t0 = time.time()
    output_ids = model.generate(**inputs, **gen_kwargs)
    elapsed = time.time() - t0

    completion_ids = output_ids[0, input_len:]
    completion = tokenizer.decode(completion_ids, skip_special_tokens=True)
    return completion, elapsed


@torch.inference_mode()
def generate_batch(
    loaded: LoadedModel,
    prompts: list[str],
    max_new_tokens: int = 512,
    temperature: float = 0.0,
    top_p: float = 1.0,
) -> tuple[list[str], float]:
    """Batched generation.

    Returns (list_of_completions, total_elapsed_seconds). The per-question
    cost is `total_elapsed / len(prompts)` — we don't try to attribute
    a per-row time inside the kernel.

    Left-padding is used (causal-LM requirement), which means short
    prompts in a batch waste a bit of compute on PAD tokens. For our
    50-question evaluation that's fine; for production we'd bucket by
    length.
    """
    tokenizer = loaded.tokenizer
    model = loaded.model
    _prepare_tokenizer_for_padding(tokenizer)

    enc = tokenizer(prompts, return_tensors="pt", padding=True, truncation=False).to(
        loaded.device
    )
    input_len = enc["input_ids"].shape[1]

    do_sample = temperature > 0.0
    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        pad_token_id=tokenizer.pad_token_id,
    )
    if do_sample:
        gen_kwargs["temperature"] = temperature
        gen_kwargs["top_p"] = top_p

    t0 = time.time()
    output_ids = model.generate(**enc, **gen_kwargs)
    elapsed = time.time() - t0

    # Left-padding means every row's generated tokens start at `input_len`.
    completion_ids = output_ids[:, input_len:]
    completions = tokenizer.batch_decode(completion_ids, skip_special_tokens=True)
    return completions, elapsed
