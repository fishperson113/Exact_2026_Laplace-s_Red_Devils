from fastapi import FastAPI

from app.api.routes.ask import router as ask_router
from app.api.routes.health import router as health_router

app = FastAPI(title="EXACT 2026 API", version="1.0.0")


@app.get("/")
async def root() -> dict:
    return {
        "message": "EXACT 2026 API is running.",
        "endpoint": "POST /ask  (single endpoint, routes by request shape)",
        "routing": {
            "type1_logic": "body has 'premises-NL' -> FOL+QA pipeline",
            "type2_physics": "body has only 'question' -> code-exec pipeline",
        },
    }


# Single competition endpoint (handles both task types) + health.
app.include_router(ask_router)
app.include_router(health_router)
