"""v04 — optimized routing: improved classification prompt via keyword analysis + disambiguation rules."""

VERSION_NUM = 4
STRATEGY_TAG = "optimized_routing"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Two-pass pipeline with optimized classification. Pass 1 uses a refined "
    "routing prompt (domain-knowledge keywords, disambiguation rules, synthetic "
    "few-shot examples) to classify (domain, answer_type). Pass 2 solves with "
    "domain-specific system prompt and matched few-shot examples. "
    "Routing prompt designed via keyword frequency analysis + artifact filtering "
    "(see ROUTING_PROMPT_DESIGN.md)."
)
