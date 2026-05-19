"""v01 — zero-shot baseline on the upstream Qwen weights, no finetune."""

VERSION_NUM = 1
STRATEGY_TAG = "zeroshot"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Zero-shot inference with a strict-format physics prompt. No few-shot, "
    "no RAG, no fine-tuning. Used as the floor that all later versions must beat."
)
