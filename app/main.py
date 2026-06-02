from fastapi import FastAPI

from app.api.routes.ask import router as ask_router
from app.api.routes.health import router as health_router
from app.api.routes.logic import router as logic_router

app = FastAPI(title="EXACT 2026 API", version="0.3.0")


@app.get("/")
async def root() -> dict:
    return {
        "message": "EXACT 2026 API is running.",
        "tracks": {
            "physics": "/ask  (Task Type 2)",
            "logic": "/logic/ask  (Task Type 1 — mock)",
        },
    }


# Task Type 2: Physics
app.include_router(ask_router)
app.include_router(health_router)

# Task Type 1: Education Logic (mock — adapt later)
app.include_router(logic_router)
