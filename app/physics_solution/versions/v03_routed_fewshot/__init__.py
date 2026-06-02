"""v03 — routed few-shot: classify (domain, answer_type) then solve with specialised prompts."""

VERSION_NUM = 3
STRATEGY_TAG = "routed_fewshot"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Two-pass pipeline on the same model: Pass 1 classifies (domain, answer_type) "
    "from question text alone; Pass 2 solves with a domain-specific system prompt "
    "and answer-type-matched few-shot examples."
)
