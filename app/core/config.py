from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Serving-side config. One gateway fronts TWO vLLM engines (one GPU):

        :18000   base Qwen3.5-4B + LoRA(sft=physics) + LoRA(qa=logic stage 2)
                   -> ids: base, sft, qa  (Task Type 2 + Task Type 1 stage 2)
        :18001   fol (full finetune, grafted)  -> Task Type 1, stage 1 (NL -> FOL)

    The qa LoRA shares :18000 with physics, so the gateway only sleep-swaps fol
    (:18001) by type; :18000 stays awake. Model set matches app/logic_solution/
    config.yaml (fol=fol-v06-cot-augmented, qa=v04-QA-CoT adapter).

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

    # ---- Logic (Task Type 1) — two-stage FOL -> QA ----
    # FOL (stage 1, NL->FOL) is a FULL finetune (fol-v06-cot-augmented) grafted onto
    # the composite base and served standalone on :18001 (text-only Qwen3_5ForCausalLM
    # isn't vLLM-servable; the graft makes it composite). QA (stage 2) is a LoRA adapter
    # (v04-QA-CoT) served on the SAME :18000 engine as physics — so qa_base_url == the
    # physics endpoint and only fol gets sleep-swapped. Values are vLLM served-model
    # NAMES ("fol"/"qa"), not repo ids. max_tokens match app/logic_solution/config.yaml.
    fol_model: str = "fol"
    fol_base_url: str = "http://localhost:18001/v1"
    fol_max_tokens: int = 768

    qa_model: str = "qa"
    qa_base_url: str = "http://localhost:18000/v1"
    qa_max_tokens: int = 1000

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
