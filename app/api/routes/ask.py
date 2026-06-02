from fastapi import APIRouter
from app.api.schemas import AskRequest, QAResponse
from app.core.pipeline import run_qa_pipeline

router = APIRouter()


@router.post("/ask", response_model=QAResponse)
async def ask(request: AskRequest) -> QAResponse:
    return await run_qa_pipeline(request)
