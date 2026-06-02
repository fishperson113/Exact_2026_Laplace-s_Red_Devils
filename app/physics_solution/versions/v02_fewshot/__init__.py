"""v02 — few-shot in-context learning on the upstream Qwen weights."""

VERSION_NUM = 2
STRATEGY_TAG = "fewshot"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Few-shot prompting: K worked examples per domain are injected as prior "
    "user/assistant turns before the real question. Examples are curated by "
    "`select_fewshot.py` from the training data (test-set IDs excluded)."
)
