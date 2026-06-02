from fastapi import APIRouter
from app.model.llm_client import llm

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    vllm_ok = await llm.is_alive()
    return {
        "status": "ok" if vllm_ok else "vllm_down",
        "vllm": "up" if vllm_ok else "down",
    }
