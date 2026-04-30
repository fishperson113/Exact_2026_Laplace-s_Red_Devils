from __future__ import annotations
import json
from app.api.schemas import QAResponse


def parse_response(raw: str) -> QAResponse:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return QAResponse(answer="?", explanation=raw.strip())

    return QAResponse(
        answer=str(data.get("answer", "?")),
        explanation=str(data.get("explanation", "")),
        fol=data.get("fol") or None,
        cot=data.get("cot") or None,
        premises=data.get("premises") or None,
        confidence=_clamp(data.get("confidence")),
    )


def _clamp(val: object) -> float | None:
    if val is None:
        return None
    try:
        return max(0.0, min(1.0, float(val)))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
