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
    vllm_model: str = "Laplaces-Red-Devils/physics-v04-optimized_routing-qwen3.5-4b"
    vllm_base_url: str = "http://localhost:18000/v1"
    vllm_api_key: str = "dummy"

    # ---- Logic (Task Type 1) — two vLLM servers, FOL then QA ----
    fol_model: str = "Laplaces-Red-Devils/fol-v05-cot-augmented-fol-pretrain-malls-qwen2.5-3"
    fol_base_url: str = "http://localhost:18001/v1"
    fol_max_tokens: int = 400

    # qa_model is the LoRA module name registered in vLLM (--lora-modules qa=<adapter>),
    # NOT a HF repo id. The base (Qwen/Qwen2.5-3B-Instruct) is loaded by the qa server.
    qa_model: str = "qa"
    qa_base_url: str = "http://localhost:18002/v1"
    qa_max_tokens: int = 400

    # ---- Pipeline routing ----
    pipeline_version: str = "v05_best_vLLM"   # physics batch/serving version
    question_timeout_s: float = 60.0


settings = Settings()
