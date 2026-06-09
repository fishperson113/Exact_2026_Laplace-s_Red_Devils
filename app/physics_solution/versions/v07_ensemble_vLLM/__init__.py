"""v07_ensemble_vLLM — physics ensemble served via vLLM (async).

Two 4B models served in parallel (BTC allows 2x4B = 8B active):
  * SFT  (v07c)         — the primary physics solver
  * BASE (Qwen3.5-4B)   — second voter AND the judge

Per query: each model self-consistency-samples K, votes its own answer; if the
two voted answers agree -> done; else the BASE model judges which is correct
(text only, no code). Explanation + CoT steps are built from the chosen solution.
"""

VERSION_NUM = 7
STRATEGY_TAG = "ensemble_vLLM"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Ensemble of SFT + BASE Qwen3.5-4B over vLLM. Each self-consistency-votes "
    "K samples in parallel; agree-or-judge (BASE judges); deadline-safe."
)
