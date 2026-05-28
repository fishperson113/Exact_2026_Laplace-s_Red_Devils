"""v05_best_vLLM — v05_best pipeline served via vLLM API (async, concurrent-ready)."""

VERSION_NUM = 5
STRATEGY_TAG = "best_vLLM"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "v05_best pipeline over vLLM API. Fully async: classify → codegen → "
    "execute_code_async → retry. Supports concurrent requests via event loop."
)
