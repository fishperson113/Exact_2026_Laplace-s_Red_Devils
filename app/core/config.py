from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # vLLM — template uses internal port 18000
    vllm_model: str = "Qwen/Qwen3.5-4B"
    vllm_base_url: str = "http://localhost:18000/v1"
    vllm_api_key: str = "dummy"

    # Pipeline routing — set PIPELINE_VERSION env var to switch versions
    pipeline_version: str = "v05_best_vLLM"
    question_timeout_s: float = 60.0


settings = Settings()
