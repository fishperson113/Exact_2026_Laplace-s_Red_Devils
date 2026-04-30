from fastapi import APIRouter
from app.memory.redis_client import memory
from app.core.pipeline import SESSION_ID

router = APIRouter(prefix="/dev", tags=["dev"])


@router.post("/reset")
async def reset_session() -> dict:
    """Clear conversation history. Dev-only — reset before a new demo run."""
    await memory.clear(SESSION_ID)
    return {"status": "ok", "message": "Session cleared."}
