"""Question classifier: (domain, answer_type) via zero-shot LLM call.

Uses the same Qwen 3.5 4B model instance as the solver to avoid a second
load. Output is a short JSON object (~20 tokens), parsed with fallback.

The classification prompt (system message + few-shot examples) is passed
by each version's run.py, so different versions can use different prompts
while sharing the parsing / batching engine.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from app.physics_solution.shared.model.loader import LoadedModel, generate_batch
from app.physics_solution.shared.model.batched_llm import _apply_chat_template_no_think
from app.physics_solution.shared.runtime.tracing import traceable


VALID_DOMAINS = {"LD", "CH", "NL", "TD", "DDT", "THCB", "DT", "CHLT"}
VALID_ANSWER_TYPES = {
    "pure_numeric", "sci_notation", "yes_no",
    "multi_value", "text_only", "mixed",
}

DEFAULT_DOMAIN = "LD"
DEFAULT_ANSWER_TYPE = "pure_numeric"

CLASSIFY_USER = """{question}"""


@dataclass
class RouteResult:
    domain: str
    answer_type: str
    confidence: float


def _parse_route(text: str) -> RouteResult:
    """Parse model output into RouteResult with fallback."""
    text = text.strip()
    # Try to find JSON in the output
    json_match = re.search(r"\{[^}]+\}", text)
    if json_match:
        try:
            obj = json.loads(json_match.group(0))
            domain = str(obj.get("domain", DEFAULT_DOMAIN)).strip().upper()
            answer_type = str(obj.get("answer_type", DEFAULT_ANSWER_TYPE)).strip().lower()
            if domain not in VALID_DOMAINS:
                domain = DEFAULT_DOMAIN
            if answer_type not in VALID_ANSWER_TYPES:
                answer_type = DEFAULT_ANSWER_TYPE
            return RouteResult(domain=domain, answer_type=answer_type, confidence=0.9)
        except (json.JSONDecodeError, KeyError):
            pass
    return RouteResult(
        domain=DEFAULT_DOMAIN, answer_type=DEFAULT_ANSWER_TYPE, confidence=0.1,
    )


def _build_classify_prompt(
    question: str,
    tokenizer,
    system_prompt: str,
    examples: list[dict],
) -> str:
    msgs = [{"role": "system", "content": system_prompt}]
    for ex in examples:
        msgs.append({"role": "user", "content": ex["q"]})
        msgs.append({"role": "assistant", "content": ex["a"]})
    msgs.append({"role": "user", "content": CLASSIFY_USER.format(question=question)})
    return _apply_chat_template_no_think(tokenizer, msgs)


@traceable(name="classify_question", run_type="chain")
def classify_question(
    question: str,
    model: LoadedModel,
    *,
    system_prompt: str,
    examples: list[dict],
) -> RouteResult:
    """Classify a single question."""
    results = classify_batch(
        [question], model, batch_size=1,
        system_prompt=system_prompt, examples=examples,
    )
    return results[0]


def classify_batch(
    questions: list[str],
    model: LoadedModel,
    batch_size: int = 32,
    *,
    system_prompt: str,
    examples: list[dict],
) -> list[RouteResult]:
    """Batch classification for efficiency.

    Parameters
    ----------
    system_prompt : str
        The system message describing domains and answer types.
    examples : list[dict]
        Few-shot examples, each with keys "q" (question) and "a" (JSON answer).
    """
    prompts = [
        _build_classify_prompt(q, model.tokenizer, system_prompt, examples)
        for q in questions
    ]
    all_results: list[RouteResult] = []

    for i in range(0, len(prompts), batch_size):
        chunk = prompts[i : i + batch_size]
        completions, _ = generate_batch(
            model, chunk,
            max_new_tokens=50,
            temperature=0.0,
        )
        for comp in completions:
            all_results.append(_parse_route(comp))

    return all_results
