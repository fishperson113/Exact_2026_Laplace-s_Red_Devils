from fastapi import FastAPI

from app.api.routes.ask import router as ask_router
from app.api.routes.health import router as health_router
from app.api.routes.models import router as models_router
from app.api.routes.predict import router as predict_router

app = FastAPI(title="EXACT 2026 API", version="2.0.0")


@app.get("/")
async def root() -> dict:
    return {
        "message": "EXACT 2026 API is running.",
        "endpoint": "POST /predict  (BTC 2026 unified schema, routes by `type`)",
        "routing": {
            "type1_logic": "type == 'type1' -> FOL+QA pipeline",
            "type2_physics": "type == 'type2' -> ensemble code-exec pipeline",
        },
    }


# BTC 2026 competition endpoint (/predict) + /v1/models proxy + legacy /ask + health.
app.include_router(predict_router)
app.include_router(models_router)
app.include_router(ask_router)
app.include_router(health_router)
