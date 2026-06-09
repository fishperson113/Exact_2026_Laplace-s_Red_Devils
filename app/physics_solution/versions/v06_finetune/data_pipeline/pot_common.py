"""Shared, GPU-free core for Phase-2 trajectory generation (both routes).

This is the part that turns a raw model completion into a verified SFT sample:

    completion --extract_code--> code --execute_code--> printed answer
                                              |
                                              v
                              scorer.score(printed, gold)  == the execution gate

Only completions whose code runs AND whose printed answer matches gold become
`Trajectory` records. `selfgen.py` (Qwen via vLLM) and `teacher.py` (DeepSeek)
both call `verify()` + `make_trajectory()` here, so the gate is identical for
both routes. Nothing in this module needs a GPU or a network model -- it runs
anywhere (local or Vast), which is also why the heavy v05 prompt/formula imports
are lazy (they pull PyYAML; the verifier itself does not).

Code normalization (`code_hash`) is shared so self-gen dedup and guards dedup
agree on what "the same solution" means.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from app.physics_solution.shared.eval import scorer
from app.physics_solution.shared.runtime.tracing import traceable
from app.physics_solution.versions.v05_best.code_executor import (
    ExecutionResult,
    extract_code,
)
from app.physics_solution.versions.v05_best_vLLM.code_executor import execute_code_async
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import (
    ProblemSpec,
    Provenance,
    Trajectory,
    read_jsonl,
    write_jsonl,
)

EXEC_TIMEOUT = 10  # seconds; same sandbox budget as v05_best


# ------------------------------------------------------------------ prompts

def build_gen_messages(spec: ProblemSpec) -> list[dict]:
    """The v06 PoT generation prompt: short reasoning THEN one code block (see prompts.py).

    Lazy import: pulls prompts -> formula_kb -> PyYAML, which the GPU boxes have but the
    lean verifier-only path should not require.
    """
    from app.physics_solution.versions.v06_finetune.data_pipeline import prompts

    return prompts.build_gen_messages(spec.question, spec.domain, spec.answer_type)


def build_hinted_messages(spec: ProblemSpec) -> list[dict]:
    """Hinted self-gen prompt: shows `spec.meta['hint_code']` as a method reference so Qwen
    can re-derive ITS OWN reasoning + code (on-policy). Used for the residual only.
    """
    from app.physics_solution.versions.v06_finetune.data_pipeline import prompts

    hint = (spec.meta or {}).get("hint_code") or ""
    return prompts.build_hinted_messages(spec.question, spec.domain, spec.answer_type, hint)


def error_feedback(exec_result: ExecutionResult | None) -> str:
    """The retry user-turn fed back after an execution failure (v05 shape)."""
    if exec_result is None:
        return (
            "No Python code block was found in your reply. Output exactly ONE "
            "```python ... ``` block that prints FINAL ANSWER: <value> and UNIT: <unit>."
        )
    return (
        "The previous code produced an error:\n"
        f"stderr: {exec_result.stderr.strip()[:1500]}\n"
        f"stdout: {exec_result.stdout.strip()[:500]}\n\n"
        "Fix the code and try again. Output one Python code block that prints "
        "FINAL ANSWER: <value> and UNIT: <unit>."
    )


# ------------------------------------------------------------------ execution gate

@dataclass
class VerifyResult:
    """Outcome of running + scoring one completion. `is_correct` is the gate."""

    code: str | None
    exec_result: ExecutionResult | None
    is_correct: bool


async def verify(completion: str, spec: ProblemSpec) -> VerifyResult:
    """Extract -> execute -> score one completion against the problem's gold.

    `is_correct` is True only when code ran, printed a FINAL ANSWER, and the
    scorer judged it equal to gold (value-level; units are not gated -- they are
    too noisy, e.g. "N" vs "Newton" -- matching v05's scoring).
    """
    code = extract_code(completion)
    if code is None:
        return VerifyResult(None, None, False)

    res = await execute_code_async(code, timeout=EXEC_TIMEOUT)
    if not res.success or res.answer is None:
        return VerifyResult(code, res, False)

    pred = f"FINAL ANSWER: {res.answer}\nUNIT: {res.unit or ''}"
    scored = scorer.score(pred, spec.gold_answer, spec.gold_unit)
    return VerifyResult(code, res, bool(scored.is_correct))


def make_trajectory(
    spec: ProblemSpec,
    completion: str,
    vr: VerifyResult,
    *,
    route: str,
    gen_model: str,
    temperature: float,
    retry_count: int = 0,
    sample_idx: int = 0,
    hint_source: str = "",
) -> Trajectory:
    """Wrap a verified completion into the cross-stage `Trajectory` contract.

    Caller must pass a `vr` with `is_correct=True` (the execution-gate evidence
    is copied verbatim from it). `provenance` is filled for the Data Disclosure
    Document -- keep `route`/`gen_model` accurate (teacher data must be declared).
    """
    res = vr.exec_result
    prov = Provenance(
        route=route,
        gen_model=gen_model,
        temperature=temperature,
        retry_count=retry_count,
        sample_idx=sample_idx,
        created_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        hint_source=hint_source,
    )
    return Trajectory(
        id=f"{spec.id}#{route}{sample_idx}",
        source_id=spec.id,
        question=spec.question,
        domain=spec.domain,
        answer_type=spec.answer_type,
        gold_answer=spec.gold_answer,
        gold_unit=spec.gold_unit,
        dataset_source=spec.dataset_source,
        assistant=completion,
        code=vr.code or "",
        exec_answer=(res.answer or "") if res else "",
        exec_unit=(res.unit or "") if res else "",
        exec_stdout=res.stdout if res else "",
        is_correct=True,
        provenance=prov,
    )


# ------------------------------------------------------------------ structured LangSmith trace

def gold_value_in_prompt(gold_answer: str, *prompt_parts: str) -> bool:
    """Leak check: does the gold answer string appear verbatim in the prompt?

    For self-gen this must be False (gold is never sent). For the teacher it is
    True by design (gold is given as a verification target). Crude substring match
    — a short numeric gold may coincide with a given in the question, so read it
    alongside `route`.
    """
    g = str(gold_answer).strip().lower()
    if not g:
        return False
    blob = " ".join(p or "" for p in prompt_parts).lower()
    return g in blob


@traceable(run_type="chain", name="pot_sample")
def _pot_sample_run(
    *,
    qid: str,
    question: str,
    domain: str,
    answer_type: str,
    temperature: float,
    sample_idx: int,
    route: str,
    retry_count: int,
    system_prompt: str,
    user_prompt: str,
    gold_answer: str,
    gold_unit: str,
    raw_completion: str,
    extracted_code: str | None,
    exec_answer: str | None,
    exec_unit: str | None,
    exec_stdout: str,
    exec_error: str | None,
    is_correct: bool,
) -> dict:
    """One LangSmith span per (question, temperature, sample).

    Inputs (the args) capture EXACTLY what the model saw — `system_prompt` +
    `user_prompt` (formula hints + question; no gold for self-gen) — plus its
    `raw_completion` and the scraped `extracted_code`. The returned dict is the
    verdict: executed answer, correctness, and the gold-leak check.
    """
    return {
        "is_correct": is_correct,
        "exec_answer": exec_answer,
        "exec_unit": exec_unit,
        "exec_error": exec_error,
        "exec_stdout": exec_stdout,
        "gold": f"{gold_answer} {gold_unit}",
        "gold_value_in_prompt": gold_value_in_prompt(gold_answer, system_prompt, user_prompt),
    }


def trace_sample(
    spec: ProblemSpec,
    messages: list[dict],
    *,
    temperature: float,
    sample_idx: int,
    route: str,
    retry_count: int,
    raw_completion: str,
    vr: "VerifyResult",
) -> None:
    """Emit a structured LangSmith span for one generated sample (no-op if tracing off).

    Side-effect only — pulls the system/user prompt out of `messages` and the
    execution evidence out of `vr`. Safe to call unconditionally; when LangSmith
    is disabled, `traceable` is the identity decorator so this just builds a dict.
    """
    sysp = next((m["content"] for m in messages if m.get("role") == "system"), "")
    usrp = next((m["content"] for m in messages if m.get("role") == "user"), "")
    res = vr.exec_result
    _pot_sample_run(
        qid=spec.id,
        question=spec.question,
        domain=spec.domain,
        answer_type=spec.answer_type,
        temperature=temperature,
        sample_idx=sample_idx,
        route=route,
        retry_count=retry_count,
        system_prompt=sysp,
        user_prompt=usrp,
        gold_answer=spec.gold_answer,
        gold_unit=spec.gold_unit,
        raw_completion=raw_completion,
        extracted_code=vr.code,
        exec_answer=(res.answer if res else None),
        exec_unit=(res.unit if res else None),
        exec_stdout=(res.stdout if res else ""),
        exec_error=(res.error_type if res else "no_code_block"),
        is_correct=vr.is_correct,
    )


# ------------------------------------------------------------------ code normalization (shared dedup key)

_COMMENT_RE = re.compile(r"#.*$", re.MULTILINE)


def normalize_code(code: str) -> str:
    """Strip comments + blank lines + trailing whitespace -> canonical form.

    Used as the dedup key so two solutions that differ only in comments or
    spacing count as the same. Self-gen dedup and guards dedup share this.
    """
    no_comments = _COMMENT_RE.sub("", code or "")
    lines = [ln.rstrip() for ln in no_comments.splitlines()]
    lines = [ln for ln in lines if ln.strip()]
    return "\n".join(lines)


def code_hash(code: str) -> str:
    return hashlib.sha1(normalize_code(code).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ resume / checkpoint helpers

def load_jsonl_if_exists(path: str | Path) -> list[dict]:
    p = Path(path)
    return list(read_jsonl(p)) if p.exists() else []


def save_checkpoint(
    solved_path: str | Path,
    residual_path: str | Path,
    solved: list[dict],
    residual: list[dict],
) -> None:
    """Atomically-ish rewrite both output files (the Phase-1 resume pattern).

    A crash mid-run loses at most one save interval; a re-run skips done ids.
    """
    write_jsonl(solved_path, solved)
    write_jsonl(residual_path, residual)
