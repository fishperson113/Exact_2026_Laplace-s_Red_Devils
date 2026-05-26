"""Central inference configuration.

Change values here, NOT in notebooks. Every CLI tool (inference.py,
upload_model.py) reads its defaults from this module, so once a setting
is edited here it picks up automatically on the next `!python -m ...`
call inside a Colab notebook — no need to re-run a config cell.

CLI flags still override these values if explicitly passed.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    _ENV_PATH = Path(__file__).resolve().parent / ".env"
    load_dotenv(_ENV_PATH)
except ImportError:
    pass


# -------------------------------------------------------------------- model
BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
BASE_TAG = "qwen3.5-4b"

# -------------------------------------------------------------------- runtime
DEVICE = "cuda"        # "cuda" on Colab GPU, "cpu" locally
DTYPE = "bf16"         # "bf16" on Ampere+ (L4 / A100), "fp16" on T4,
                       # "int8" for CPU-friendly 8-bit weight quant
BATCH_SIZE = 100       # Full-eval batch. Fits A100 40GB comfortably; on L4
                       # 22.5GB may run tight — drop to 32-64 if you see OOM.
                       # Drop to 4-8 for batch=1 latency benchmarks.

# -------------------------------------------------------------------- generation
# With Qwen3.5 thinking mode OFF (we pass enable_thinking=False to the chat
# template), a typical answer fits in 256-512 tokens. Default 640 leaves
# headroom for harder problems without paying the speed cost of 1024+.
MAX_NEW_TOKENS = 2000
TEMPERATURE = 0.0      # math QA → greedy. Raise only if you want diversity.

# -------------------------------------------------------------------- eval
LIMIT: int | None = None      # set e.g. 5 for smoke tests
TEST_FILE = "app/physics_solution/data/test/full_test.csv"  # 1352 rows, all answer types
# Legacy pure-numeric only: "app/physics_solution/data/test/sample_test.csv"
GOLDEN_TEST_FILE = "app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv"  # 1352 rows, rewritten CoT

# -------------------------------------------------------------------- org
HF_ORG = "Laplaces-Red-Devils"
PUSH_PRIVATE = True

# -------------------------------------------------------------------- tracing
LANGSMITH_PROJECT = "exact26-physics-type2"


# -------------------------------------------------------------------- commercial LLM (golden-data generation)
COMMERCIAL_PROVIDER = "deepseek"             # "deepseek" or "openai"
COMMERCIAL_MODEL = "deepseek-v4-pro"         # model name for the provider's API
COMMERCIAL_API_KEY_ENV = {
    "deepseek": "DEEPSEEK_API_KEY",
    "openai":   "OPENAI_API_KEY",
}
COMMERCIAL_BASE_URL = {
    "deepseek": "https://api.deepseek.com",
    "openai":   None,                        # uses SDK default
}


# -------------------------------------------------------------------- golden data
GOLDEN_DIR = "app/physics_solution/data/golden"
GOLDEN_SAVE_EVERY = 50


# -------------------------------------------------------------------- helpers
def repo_root() -> Path:
    """Best-effort repo root. Set REPO_ROOT env var to override."""
    env = os.environ.get("REPO_ROOT")
    if env:
        return Path(env)
    # __file__ = .../app/physics_solution/config.py -> repo is two levels up.
    return Path(__file__).resolve().parents[2]
