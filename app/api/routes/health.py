from fastapi import APIRouter
from app.model.llm_client import llm
from app.memory.redis_client import memory

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    vllm_ok = await llm.is_alive()
    redis_ok = await memory.is_alive()
    return {
        "status": "ok" if (vllm_ok and redis_ok) else "degraded",
        "vllm": "up" if vllm_ok else "down",
        "redis": "up" if redis_ok else "down",
    }
