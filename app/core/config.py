from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Serving-side config. One gateway fronts THREE vLLM servers (one GPU):

        physics  -> :18000   Task Type 2 (code-exec pipeline)
        fol      -> :18001   Task Type 1, stage 1 (NL -> FOL)
        qa       -> :18002   Task Type 1, stage 2 (FOL+NL+Q -> answer), LoRA

    Override any field via env var (UPPER_SNAKE of the field name) or .env.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # ---- Physics (Task Type 2) — kept VLLM_* names for back-compat ----
    # Ensemble serving = ONE vLLM hosting the BASE Qwen3.5-4B + the SFT as a LoRA adapter,
    # exposing two ids on /v1/models: "sft" (primary solver) and "base" (voter #2 + judge).
    # Both share the same endpoint; total params ~4B (base + tiny adapter) << 8B.
    vllm_model: str = "sft"                          # LoRA adapter id served by vLLM
    vllm_base_url: str = "http://localhost:18000/v1"
    vllm_api_key: str = "dummy"

    # ---- Physics ensemble: BASE model + JUDGE (SAME vLLM endpoint as SFT) ----
    judge_model: str = "base"                        # base served-model-name on the same vLLM
    judge_base_url: str = "http://localhost:18000/v1"
    # ensemble sampling knobs (self-consistency K + judge)
    ensemble_k: int = 5
    ensemble_temperature: float = 0.7
    ensemble_top_p: float = 0.95
    ensemble_max_tokens: int = 2048

    # ---- Logic (Task Type 1) — two vLLM servers, FOL then QA ----
    # Both are FULL Qwen3.5-4B finetunes (fol-pretrain = continued-pretrain; qa =
    # cot-augmented SFT on top). They ship as the text-only arch Qwen3_5ForCausalLM,
    # which vLLM 0.22.1 CANNOT serve — serve_all grafts each onto the composite base
    # (scripts/graft_text_to_composite.py) and serves the local composite dir. These
    # are the vLLM served-model-NAMES ("fol"/"qa"), not repo ids.
    fol_model: str = "fol"
    fol_base_url: str = "http://localhost:18001/v1"
    fol_max_tokens: int = 400

    qa_model: str = "qa"
    qa_base_url: str = "http://localhost:18002/v1"
    qa_max_tokens: int = 400

    # ---- Pipeline routing ----
    pipeline_version: str = "v07_ensemble_vLLM"   # physics serving version
    question_timeout_s: float = 60.0

    # ---- Sleep-mode swap (SERVE_MODE=triple) ----
    # When 3 DISTINCT Qwen3.5-4B models can't co-reside on one 24GB GPU, each
    # vLLM runs with --enable-sleep-mode and the gateway wakes the server(s) a
    # request needs and sleeps the rest. OFF in shared mode (one server serves
    # all roles -> nothing to swap).
    sleep_swap_enabled: bool = False


settings = Settings()
