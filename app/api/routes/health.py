from fastapi import APIRouter
from app.model.llm_client import llm
from app.memory.redis_client import memory

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    ollama_ok = await llm.is_alive()
    redis_ok = await memory.is_alive()
    return {
        "status": "ok" if (ollama_ok and redis_ok) else "degraded",
        "ollama": "up" if ollama_ok else "down",
        "redis": "up" if redis_ok else "down",
    }
