from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    ollama_model: str = "qwen2.5:7b"
    ollama_base_url: str = "http://localhost:11434"

    redis_url: str = "redis://localhost:6379"
    session_ttl: int = 3600
    max_history_turns: int = 5

    pinecone_api_key: Optional[str] = None
    pinecone_index: Optional[str] = None
    embed_model: str = "nomic-embed-text"


settings = Settings()
