from fastapi import APIRouter

from app.model.llm_client import fol_llm, physics_llm, qa_llm

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    """Report liveness of all three backing vLLM servers."""
    physics_ok = await physics_llm.is_alive()
    fol_ok = await fol_llm.is_alive()
    qa_ok = await qa_llm.is_alive()
    all_ok = physics_ok and fol_ok and qa_ok
    return {
        "status": "ok" if all_ok else "degraded",
        "physics_vllm": "up" if physics_ok else "down",
        "fol_vllm": "up" if fol_ok else "down",
        "qa_vllm": "up" if qa_ok else "down",
    }
