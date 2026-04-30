from fastapi import FastAPI
from app.api.routes.ask import router as ask_router
from app.api.routes.health import router as health_router
from app.api.routes.dev import router as dev_router

app = FastAPI(title="Exact 2026 QA API", version="0.1.0")


@app.get("/")
async def root() -> dict:
    return {"message": "Exact 2026 QA backend is running."}


app.include_router(ask_router)
app.include_router(health_router)
app.include_router(dev_router)
