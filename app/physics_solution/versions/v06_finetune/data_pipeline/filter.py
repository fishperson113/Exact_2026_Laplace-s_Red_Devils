"""Step-0 filter: drop physics problems unsolvable from text alone.

A problem is DROPPED if it (a) refers to a figure/diagram/graph/table/image the
text doesn't fully describe, (b) is underspecified (missing data needed to
compute), or (c) is a pure theory/definition question with no computable answer.
Everything else is KEPT.

Uses the cheap `deepseek-v4-flash` (this is simple classification, not code-gen).
Returns a verdict per item; callers log dropped items + reasons (audit trail).

Library module — orchestrated by btc_normalize.py / vietjack_normalize.py.
"""

from __future__ import annotations

import json
import re
from typing import Any, Awaitable, Callable

from app.physics_solution.config import COMMERCIAL_MODEL_FLASH
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client

FILTER_SYSTEM = """\
You are a data-quality filter for a physics problem dataset. Each problem must be
solvable by writing a Python script from the TEXT ALONE. Decide whether to KEEP it.

IMPORTANT — apply standard physics BEFORE judging a problem "underspecified". A
problem is solvable if a standard relationship connects the given quantities, even
when not every symbol is stated numerically:
- Series RLC at RESONANCE: X_L = X_C, so impedance Z = R and power factor cosφ = 1.
  Hence "Z at resonance, R given" = R; "R from Z at resonance" = Z; at resonance
  I = U/R, P = U²/R, U_R = U.
- Standard formulas relate givens, e.g. f0 = 1/(2π√(LC)) gives C from L and f0;
  capacitive/inductive reactance from C/L and f; Coulomb's law; Faraday's law.
Only call something underspecified if a needed quantity is GENUINELY absent and NOT
derivable from the given data via such a standard relationship.

DROP the problem (solvable=false) if ANY of these hold:
- It refers to a figure, diagram, graph, picture, circuit drawing, or table that
  is NOT fully described in words (e.g. "as shown in the figure", "from the graph",
  "in the diagram below", segments/points only defined by an unseen drawing).
- It is genuinely underspecified: a required quantity is missing AND cannot be
  derived from the given data by a standard physics relationship.
- It is a pure theory / definition / "explain" question with no numeric or yes/no
  answer to compute.

KEEP it (solvable=true) otherwise.

Output ONLY a compact JSON object, no prose:
{"solvable": true, "reason": "<short reason>"}
"""

_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def build_filter_messages(question: str) -> list[dict]:
    return [
        {"role": "system", "content": FILTER_SYSTEM},
        {"role": "user", "content": f"PROBLEM:\n{question}\n\nKeep or drop?"},
    ]


def parse_filter(text: str) -> dict:
    """Parse the {solvable, reason} JSON. On parse failure, KEEP (conservative)."""
    m = _JSON_RE.search(text)
    if not m:
        return {"solvable": True, "reason": "parse-failure-kept"}
    try:
        obj = json.loads(m.group(0))
        return {
            "solvable": bool(obj.get("solvable", True)),
            "reason": str(obj.get("reason", "")).strip(),
        }
    except (json.JSONDecodeError, ValueError):
        return {"solvable": True, "reason": "parse-failure-kept"}


async def filter_questions(
    items: list[dict],
    *,
    id_key: str = "id",
    question_key: str = "question",
    model: str = COMMERCIAL_MODEL_FLASH,
    concurrency: int = 10,
    on_progress: Callable[[list[dict]], None] | None = None,
) -> list[dict]:
    """Classify each item's solvability.

    `items` are dicts with at least an id + question. Returns one verdict dict per
    item: {"id", "solvable", "reason"} (plus "__error__" if the API call failed).
    """

    def _build(item: dict) -> list[dict]:
        return build_filter_messages(str(item[question_key]))

    def _parse(item: dict, text: str) -> dict:
        verdict = parse_filter(text)
        verdict["id"] = item.get(id_key, "")
        return verdict

    raw = await ds_client.run_batch(
        items, _build, _parse,
        model=model, concurrency=concurrency, on_progress=on_progress,
    )
    # surface API errors as kept-with-error so nothing is silently lost
    out: list[dict] = []
    for r in raw:
        if "__error__" in r:
            item = r["__item__"]
            out.append({
                "id": item.get(id_key, ""),
                "solvable": True,
                "reason": f"api-error-kept: {r['__error__']}",
            })
        else:
            out.append(r)
    return out
