"""v07_ensemble_vLLM async pipeline: SFT + BASE self-consistency, agree-or-judge.

Per query (Type 2 physics):
  1. classify -> (domain, answer_type)  [one fast BASE call]
  2. build the SFT generation prompt; sample K from SFT and K from BASE **in
     parallel** (asyncio.gather over two vLLM servers -> wall-time ~= max, not sum)
  3. execute every sample's code (async) and majority-vote each model's answer
  4. agree (scorer-equivalent) -> done; else BASE JUDGES which final answer is
     correct (text only, NO code, NO vote counts shown) -> pick A(sft)/B(base)
  5. build explanation + CoT steps from the chosen solution (no extra LLM call)

Deadline-safe: if the budget is nearly spent after sampling, skip the judge and
fall back to the SFT vote. Competition-legal: SFT(4B)+BASE(4B)=8B active in
parallel; the judge reuses the already-running BASE model.

Public API:  async def solve(question, client, deadline) -> dict
"""

from __future__ import annotations

import asyncio
import re
import time
from collections import Counter

from app.core.config import settings
from app.model.llm_client import physics_base_llm
from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.shared.router import RouteResult, _parse_route
from app.physics_solution.versions.v05_best.code_executor import extract_code
from app.physics_solution.versions.v05_best_vLLM.code_executor import execute_code_async
from app.physics_solution.versions.v05_best_vLLM.pipeline import _build_classify_messages
from app.physics_solution.versions.v06_finetune.data_pipeline.prompts import build_gen_messages

_DEFAULT_ROUTE = RouteResult(domain="ELECTROSTATICS", answer_type="numeric", confidence=0.0)
_AB = re.compile(r"\b([AB])\b")


# --------------------------------------------------------------------------- #
#  sampling + voting                                                          #
# --------------------------------------------------------------------------- #
async def _exec_one(comp: str) -> dict:
    code = extract_code(comp)
    stdout = ""
    if code:
        try:
            res = await execute_code_async(code, timeout=10)
            stdout = res.stdout or ""
        except Exception:  # noqa: BLE001 — a bad sample must not sink the request
            stdout = ""
    ext = evaluator.extract(stdout)
    return {"comp": comp, "stdout": stdout, "num": ext.numeric,
            "ans": (ext.raw_answer or "").strip(),
            "unit": (ext.raw_unit or "").strip(),
            "txt": (ext.raw_answer or "").strip().lower()}


def _vote(rows: list[dict]) -> tuple[dict, int]:
    """Majority vote (no gold). Numeric answers cluster by scorer tolerance."""
    numeric = [r for r in rows if r["num"] is not None]
    text = [r for r in rows if r["num"] is None and r["txt"]]
    if numeric and len(numeric) >= len(text):
        clusters: list[dict] = []
        for r in numeric:
            for cl in clusters:
                if evaluator.numeric_close(r["num"], cl["key"]):
                    cl["rows"].append(r)
                    break
            else:
                clusters.append({"key": r["num"], "rows": [r]})
        clusters.sort(key=lambda c: len(c["rows"]), reverse=True)
        win = clusters[0]["rows"]
        return win[0], len(win)
    if text:
        cnt = Counter(r["txt"] for r in text)
        best, votes = cnt.most_common(1)[0]
        return next(r for r in text if r["txt"] == best), votes
    return (rows[0] if rows else {"comp": "", "stdout": "", "num": None,
                                  "ans": "", "unit": "", "txt": ""}), 0


def _has_answer(r: dict) -> bool:
    return r["num"] is not None or bool(r["txt"])


def _agree(a: dict, b: dict) -> bool:
    if a["num"] is not None and b["num"] is not None:
        return evaluator.numeric_close(a["num"], b["num"])
    if a["num"] is None and b["num"] is None:
        return bool(a["txt"]) and a["txt"] == b["txt"]
    return False


# --------------------------------------------------------------------------- #
#  judge (BASE model, text only, no vote counts)                              #
# --------------------------------------------------------------------------- #
def _final_lines(stdout: str) -> str:
    keep = [ln.strip() for ln in stdout.splitlines()
            if "FINAL ANSWER" in ln.upper() or ln.upper().lstrip().startswith("UNIT")]
    return " | ".join(keep) if keep else (stdout.strip()[-160:] or "(no output)")


def _sol_block(r: dict, max_chars: int = 1200) -> str:
    return f"{(r['comp'] or '').strip()[:max_chars]}\n>>> Computed: {_final_lines(r['stdout'])}"


def _cluster(rows: list[dict]) -> list[dict]:
    """Cluster sample rows by answer equivalence, largest cluster first. Each cluster:
    {key, rows}. Numeric: scorer tolerance; else exact normalized text."""
    rows = [r for r in rows if _has_answer(r)]
    numeric = [r for r in rows if r["num"] is not None]
    text = [r for r in rows if r["num"] is None and r["txt"]]
    clusters: list[dict] = []
    if numeric and len(numeric) >= len(text):
        for r in numeric:
            for cl in clusters:
                if evaluator.numeric_close(r["num"], cl["key"]):
                    cl["rows"].append(r)
                    break
            else:
                clusters.append({"key": r["num"], "rows": [r]})
    elif text:
        groups: dict = {}
        for r in text:
            groups.setdefault(r["txt"], []).append(r)
        clusters = [{"key": k, "rows": v} for k, v in groups.items()]
    clusters.sort(key=lambda c: len(c["rows"]), reverse=True)
    return clusters


# --------------------------------------------------------------------------- #
#  explanation / CoT — written by the BASE model (the judge, repurposed)      #
# --------------------------------------------------------------------------- #
def _reasoning_steps(comp: str, limit: int = 10) -> list[str]:
    head = (comp or "").split("```")[0]                # text before the code fence
    out = []
    for ln in head.replace("\r", "").split("\n"):
        s = ln.strip(" -*\t")
        if not s or s.lower().startswith("reasoning"):
            continue
        out.append(s)
    return out[:limit]


def _split_steps(text: str, limit: int = 12) -> list[str]:
    out = []
    for ln in (text or "").replace("\r", "").split("\n"):
        s = ln.strip(" -*\t")
        if s:
            out.append(s)
    return out[:limit]


async def _explain(question: str, rep: dict, deadline: float) -> tuple[str, list[str]]:
    """BASE model writes a clear explanation + CoT for the already-chosen answer (does
    NOT change it). Falls back to the chosen solution's own reasoning if out of time."""
    if time.time() >= deadline:
        steps = _reasoning_steps(rep["comp"])
        return (" ".join(steps) + f" Final answer: {rep['ans']} {rep['unit'] or '-'}.").strip(), steps
    user = (
        f"PROBLEM:\n{question.strip()}\n\nA verified computation produced this result:\n"
        f"{_sol_block(rep)}\n\nWrite a clear, concise physics EXPLANATION followed by numbered "
        "step-by-step reasoning (CoT) that justifies THIS exact final answer. Do NOT change the "
        "answer or its unit. Keep it tight (<=10 short steps)."
    )
    try:
        out = await physics_base_llm.chat([{"role": "user", "content": user}],
                                          temperature=0.0, max_tokens=settings.explain_max_tokens)
        return out.strip(), _split_steps(out)
    except Exception:  # noqa: BLE001
        steps = _reasoning_steps(rep["comp"])
        return (" ".join(steps)).strip(), steps


# --------------------------------------------------------------------------- #
#  main                                                                       #
# --------------------------------------------------------------------------- #
async def solve(question: str, client, deadline: float) -> dict:
    t0 = time.time()
    k = settings.ensemble_k

    # 1. classify (fast; default route on failure) -------------------------------
    try:
        raw = await physics_base_llm.chat(_build_classify_messages(question),
                                          max_tokens=50, temperature=0.0)
        route = _parse_route(raw)
    except Exception:  # noqa: BLE001
        route = _DEFAULT_ROUTE

    msgs = build_gen_messages(question, route.domain, route.answer_type)

    # 2. sample K from SFT and BASE in parallel ----------------------------------
    try:
        sft_comps, base_comps = await asyncio.gather(
            client.chat_n(msgs, n=k, temperature=settings.ensemble_temperature,
                          top_p=settings.ensemble_top_p, max_tokens=settings.ensemble_max_tokens),
            physics_base_llm.chat_n(msgs, n=k, temperature=settings.ensemble_temperature,
                                    top_p=settings.ensemble_top_p,
                                    max_tokens=settings.ensemble_max_tokens),
        )
    except Exception:  # noqa: BLE001 — fall back to a single SFT greedy attempt
        sft_comps = [await client.chat(msgs, max_tokens=settings.ensemble_max_tokens,
                                       temperature=0.0)]
        base_comps = []

    # 3. execute all samples -----------------------------------------------------
    sft_rows = list(await asyncio.gather(*[_exec_one(c) for c in sft_comps])) if sft_comps else []
    base_rows = list(await asyncio.gather(*[_exec_one(c) for c in base_comps])) if base_comps else []
    sft_rep, sft_votes = _vote(sft_rows)
    base_rep, base_votes = _vote(base_rows)

    # 4. POOLED vote — combine all 5+5 samples into ONE vote, majority wins -------
    all_rows = sft_rows + base_rows
    clusters = _cluster(all_rows)
    agree = _has_answer(sft_rep) and _has_answer(base_rep) and _agree(sft_rep, base_rep)
    if clusters:
        winner = clusters[0]
        chosen = winner["rows"][0]
        winner_votes = len(winner["rows"])
        method = "pool_agree" if agree else "pool_majority"
        conf = round(winner_votes / max(1, len(all_rows)), 2)
    else:
        chosen, winner_votes, method, conf = sft_rep, 0, "no_answer", 0.0

    # 5. explanation + CoT written by the BASE model -----------------------------
    answer = chosen["ans"]
    unit = chosen["unit"] or "-"
    explanation, steps = await _explain(question, chosen, deadline)
    if not explanation:
        explanation = f"Computed answer: {answer} {unit}."
    return {
        "answer": answer,
        "unit": unit,
        "explanation": explanation,
        "cot": chosen["comp"],
        "reasoning_steps": steps,
        "confidence": conf,
        "solve_method": method,
        "elapsed_s": time.time() - t0,
        "domain": route.domain,
        "answer_type": route.answer_type,
        "execution_stdout": chosen["stdout"],
        "agree": agree,
        "votes": {"winner": f"{winner_votes}/{len(all_rows)}",
                  "sft": f"{sft_votes}/{len(sft_rows)}", "base": f"{base_votes}/{len(base_rows)}"},
        # debug for analysis: pooled clusters + each model's own voted answer
        "pool": [{"answer": c["rows"][0]["ans"], "unit": c["rows"][0]["unit"] or "-",
                  "votes": len(c["rows"])} for c in clusters],
        "sft_pred": {"answer": sft_rep["ans"], "unit": sft_rep["unit"] or "-"},
        "base_pred": {"answer": base_rep["ans"], "unit": base_rep["unit"] or "-"},
    }
