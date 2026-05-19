"""v02 runner — few-shot via LangChain.

For each question we pick K examples whose domain prefix matches (falling
back to the head of the pool). The selected examples are injected into
the `few_shot_messages` placeholder of the ChatPromptTemplate.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from app.physics_solution.shared.lc_prompts import (
    build_fewshot_template,
    fewshot_messages_from,
)
from app.physics_solution.shared.runner import run_solver
from app.physics_solution.versions.v02_fewshot import (
    DEFAULT_BASE_MODEL_ID,
    DESCRIPTION,
    STRATEGY_TAG,
    VERSION_NUM,
)


HERE = Path(__file__).resolve().parent
EXAMPLES_PATH = HERE / "examples.json"
PREFIX_RE = re.compile(r"^([A-Z]+)")
N_EXAMPLES_DEFAULT = 2


def _load_examples() -> list[dict]:
    if not EXAMPLES_PATH.exists():
        raise FileNotFoundError(
            f"{EXAMPLES_PATH} not found. Run "
            "`python -m app.physics_solution.versions.v02_fewshot.select_fewshot --k 2` first."
        )
    return json.loads(EXAMPLES_PATH.read_text(encoding="utf-8"))


def _domain(qid: str) -> str:
    m = PREFIX_RE.match(str(qid))
    return m.group(1) if m else "UNK"


def _make_input_builder(pool: list[dict], n_examples: int):
    def build(row: dict) -> dict:
        qid = str(row.get("id", ""))
        target = _domain(qid)
        # Defensively exclude the question itself from its own few-shot
        # context — important when the test set and the example pool may
        # overlap (e.g. --n 973 full eval).
        safe_pool = [ex for ex in pool if str(ex.get("id", "")) != qid]
        same = [ex for ex in safe_pool if ex.get("prefix") == target]
        chosen = (same[:n_examples]) or safe_pool[:n_examples]
        return {
            "question": str(row["question"]),
            "few_shot_messages": fewshot_messages_from(chosen),
        }

    return build


def run(args) -> dict:
    n_examples = getattr(args, "n_examples", None) or N_EXAMPLES_DEFAULT
    pool = _load_examples()
    return run_solver(
        args,
        version_num=VERSION_NUM,
        strategy_tag=STRATEGY_TAG,
        default_model_id=DEFAULT_BASE_MODEL_ID,
        description=DESCRIPTION,
        prompt_template=build_fewshot_template(),
        build_inputs=_make_input_builder(pool, n_examples),
        extra_meta={"n_examples": n_examples},
    )
