"""Vietjack worked-solutions -> normalized ProblemSpec JSONL (6 competition domains).

Vietjack is Vietnamese, grade-skewed, and full of off-domain physics (mechanics,
thermo, waves, nuclear, optics) plus OCR noise ("I = 3 2 A", "10 - 5 T") and even
some figure-referencing questions. So this branch is heavy:

  parse lop-10/11/12 markdown -> (question, solution) blocks            [offline]
  -> keyword pre-filter: drop obvious off-domain to save API calls      [offline, optional]
  -> ONE DeepSeek-flash call per problem: classify domain + solvability,
     translate the question to English (BTC style), extract answer + unit
  -> drop out-of-domain / unsolvable; keep the rest as ProblemSpec
  -> write input/vietjack_normalized.jsonl (kept)
     + output/vietjack_dropped.jsonl (DROPPED + reason -- audit trail)

Vietjack has no labeled answer/unit, so the extracted gold is UNVERIFIED here; the
Phase-2 execution gate (code answer must match this gold) is what catches bad
extractions, so no wrong data is injected into SFT.

Run (from repo root; needs DEEPSEEK_API_KEY):
    python -m ...vietjack_normalize                       # all grades 10-12
    python -m ...vietjack_normalize --grades 12 --limit 30
    python -m ...vietjack_normalize --parse-only          # offline: parse + prefilter stats
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re

from app.physics_solution.config import COMMERCIAL_MODEL_FLASH, repo_root
from app.physics_solution.shared.router import _ANSWER_TYPE_ALIASES
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import (
    ProblemSpec,
    read_jsonl,
    write_jsonl,
)
from app.physics_solution.versions.v06_finetune.data_pipeline.taxonomy import (
    VALID_DOMAINS,
    canonicalize_domain,
)

SRC_TEMPLATE = "data/pretrain_processed/lop-{grade}_high_quality.md"
OUT_KEPT = "app/physics_solution/versions/v06_finetune/input/vietjack_normalized.jsonl"
OUT_DROPPED = "app/physics_solution/versions/v06_finetune/output/vietjack_dropped.jsonl"
_PREFILTER_REASON = "prefilter: off-domain keyword"


def _load(path) -> list[dict]:
    return list(read_jsonl(path)) if path.exists() else []

# ------------------------------------------------------------------ md parsing

_PROBLEM_RE = re.compile(
    r"^##\s*Problem:.*?\n"          # the "## Problem: <title>" line
    r"\*\*Question:\*\*\s*\n(?P<q>.*?)"
    r"\n###\s*Solution\s*\n(?P<s>.*?)"
    r"(?=\n---|\n##\s*Problem:|\Z)", # until ---, next problem, or EOF
    re.DOTALL | re.MULTILINE,
)


def parse_markdown(text: str, grade: int) -> list[dict]:
    """Split a Vietjack grade file into {id, question, solution} problems."""
    out: list[dict] = []
    for i, m in enumerate(_PROBLEM_RE.finditer(text)):
        q = m.group("q").strip()
        s = m.group("s").strip()
        if not q:
            continue
        out.append({"id": f"vj_l{grade}_{i:04d}", "question": q, "solution": s})
    return out


# ------------------------------------------------------------------ keyword prefilter

# In-domain signals (Vietnamese) for the 6 competition domains. If a problem has
# NO in-domain signal AND a strong off-domain signal, drop it before the API call.
_IN_DOMAIN_KW = (
    "điện tích", "điện trường", "cường độ điện trường", "coulomb", "cu-lông",
    "tụ điện", "điện dung", "điện môi", "tụ",
    "rlc", "xoay chiều", "cảm kháng", "dung kháng", "tổng trở", "cộng hưởng",
    "hiệu điện thế", "công suất", "hệ số công suất", "mạch điện", "cuộn cảm",
    "dao động điện từ", "mạch lc", "năng lượng điện trường", "năng lượng từ trường",
    "cảm ứng điện từ", "suất điện động", "từ thông", "ống dây", "tự cảm", "độ tự cảm",
    "faraday", "fa-ra-đây", "sai số", "điện trở trong", "vôn kế", "ampe kế", "đo",
)
_OFF_DOMAIN_KW = (
    "vận tốc", "gia tốc", "quãng đường", "ném", "rơi tự do", "ma sát", "động lượng",
    "con lắc", "lò xo", "dao động điều hòa", "biên độ", "li độ", "chu kì dao động",
    "sóng âm", "sóng cơ", "bước sóng", "giao thoa",
    "hạt nhân", "phóng xạ", "phản ứng hạt nhân", "nơtron", "prôtôn",
    "thấu kính", "quang phổ", "photon", "phôtôn", "lượng tử", "quang điện",
    "nhiệt độ", "áp suất", "khí lý tưởng", "pit-tông", "pít-tông", "mol", "nhiệt lượng",
)


def _has_any(text: str, kws) -> bool:
    low = text.lower()
    return any(k in low for k in kws)


def prefilter_off_domain(problem: dict) -> bool:
    """True if the problem looks clearly off-domain (safe to drop pre-API)."""
    blob = problem["question"] + " " + problem.get("solution", "")
    return _has_any(blob, _OFF_DOMAIN_KW) and not _has_any(blob, _IN_DOMAIN_KW)


# ------------------------------------------------------------------ DeepSeek translate+extract

NORMALIZE_SYSTEM = """\
You convert a Vietnamese physics worked-example into one English training sample
for a code-solving model. The dataset covers ONLY these 6 domains:
- LDDT: electrostatics (Coulomb force, electric field E, potential V, work by field)
- CH:   AC/RLC circuits (impedance, resonance, rms current/voltage, power, phase; incl. yes/no)
- NL:   energy & LC oscillations (energy stored, LC charge/current/period)
- TD:   capacitors (capacitance, charge, dielectric, series/parallel)
- DDT:  electromagnetic induction & solenoids (Faraday, flux, induced EMF, inductance)
- THCB: measurement error & basic DC circuits (absolute/relative error, internal resistance)

You are given a Vietnamese QUESTION and its Vietnamese SOLUTION.

1. in_domain: true only if it clearly belongs to one of the 6 domains above.
   (Mechanics, thermodynamics, mechanical waves, nuclear, optics, quantum -> false.)
2. solvable: true only if it is solvable from text alone — no reference to a figure
   /diagram/graph the text doesn't describe, fully specified, and has a numeric /
   yes-no / multi-value answer (not a pure theory/definition question).
3. If in_domain AND solvable: translate the QUESTION into clean, self-contained
   English in the organizer's style (fix OCR artifacts like "I = 3 2 A" -> "I = 1.5 A",
   "10 - 5 T" -> "1e-5 T"; keep all given numbers and what is asked). Then extract the
   FINAL ANSWER value and UNIT from the SOLUTION.

ANSWER format: plain decimal if |exp|<4, else "a x 10^n". Multi-value -> "v1; v2".
Yes/No -> "Yes"/"No". UNIT "N/A" if dimensionless/none. answer_type in
{numeric, yes_no, multi_value, text}.

Output ONLY one compact JSON object, no prose:
{"in_domain": <bool>, "domain": "<XX or OTHER>", "solvable": <bool>, "reason": "<short>",
 "question_en": "<english question or empty>", "answer": "<value or empty>",
 "unit": "<unit or empty>", "answer_type": "<type or empty>"}
"""

_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def build_normalize_messages(problem: dict) -> list[dict]:
    user = (
        f"QUESTION (Vietnamese):\n{problem['question']}\n\n"
        f"SOLUTION (Vietnamese):\n{problem.get('solution', '')}\n\n"
        f"Produce the JSON."
    )
    return [
        {"role": "system", "content": NORMALIZE_SYSTEM},
        {"role": "user", "content": user},
    ]


def parse_normalize(problem: dict, text: str) -> dict:
    """Parse the model JSON; attach source id. Returns a dict with status."""
    m = _JSON_RE.search(text)
    if not m:
        return {"id": problem["id"], "status": "drop", "reason": "parse-failure",
                "raw_question": problem["question"]}
    try:
        obj = json.loads(m.group(0))
    except (json.JSONDecodeError, ValueError):
        return {"id": problem["id"], "status": "drop", "reason": "json-error",
                "raw_question": problem["question"]}

    in_domain = bool(obj.get("in_domain", False))
    solvable = bool(obj.get("solvable", False))
    domain = canonicalize_domain(str(obj.get("domain", "")))
    reason = str(obj.get("reason", "")).strip()

    if not in_domain or domain is None:
        return {"id": problem["id"], "status": "drop",
                "reason": f"off-domain ({obj.get('domain')}): {reason}",
                "raw_question": problem["question"]}
    if not solvable:
        return {"id": problem["id"], "status": "drop",
                "reason": f"unsolvable: {reason}", "raw_question": problem["question"]}

    question_en = str(obj.get("question_en", "")).strip()
    answer = str(obj.get("answer", "")).strip()
    if not question_en or not answer:
        return {"id": problem["id"], "status": "drop",
                "reason": "missing question_en/answer", "raw_question": problem["question"]}

    answer_type = _ANSWER_TYPE_ALIASES.get(
        str(obj.get("answer_type", "numeric")).strip(), str(obj.get("answer_type", "numeric")).strip()
    ) or "numeric"
    spec = ProblemSpec(
        id=problem["id"],
        question=question_en,
        domain=domain,
        answer_type=answer_type,
        gold_answer=answer,
        gold_unit=str(obj.get("unit", "")).strip() or "N/A",
        dataset_source="vietjack",
        meta={"vn_question": problem["question"], "vn_solution": problem.get("solution", ""),
              "answer_unverified": True},
    )
    return {"id": problem["id"], "status": "keep", "spec": spec.to_dict()}


# ------------------------------------------------------------------ orchestration

async def _run(args) -> None:
    root = repo_root()

    # 1. parse
    problems: list[dict] = []
    for g in args.grades:
        path = root / SRC_TEMPLATE.format(grade=g)
        parsed = parse_markdown(path.read_text(encoding="utf-8"), g)
        problems.extend(parsed)
        print(f"lop-{g}: parsed {len(parsed)} problems")
    if args.limit:
        problems = problems[: args.limit]

    # 2. keyword pre-filter (offline, recomputed each run)
    prefilter_drops: list[dict] = []
    if args.prefilter:
        kept_pre = []
        for p in problems:
            if prefilter_off_domain(p):
                prefilter_drops.append({"id": p["id"], "reason": _PREFILTER_REASON,
                                        "raw_question": p["question"]})
            else:
                kept_pre.append(p)
        print(f"Pre-filter: {len(problems)} -> {len(kept_pre)} candidates "
              f"({len(prefilter_drops)} dropped as off-domain)")
        problems = kept_pre

    kept_path, dropped_path = root / OUT_KEPT, root / OUT_DROPPED

    if args.parse_only:
        write_jsonl(dropped_path, prefilter_drops)
        print(f"[parse-only] {len(problems)} candidates remain; "
              f"prefilter drops logged -> {OUT_DROPPED}")
        return

    # --- resume: skip ids already kept or API-dropped from a previous run ---
    existing_kept = [] if args.fresh else _load(kept_path)
    existing_dropped = [] if args.fresh else _load(dropped_path)
    existing_api_dropped = [d for d in existing_dropped if d.get("reason") != _PREFILTER_REASON]
    done_ids = {r["id"] for r in existing_kept} | {d["id"] for d in existing_api_dropped}
    todo = [p for p in problems if p["id"] not in done_ids]
    print(f"Already done (API): {len(done_ids)} | to process: {len(todo)}")

    # --- auto-save: rebuild + write the real kept/dropped files every 50 ---
    def _save(results: list[dict]) -> None:
        kept = list(existing_kept)
        api_dropped = list(existing_api_dropped)
        for r in results:
            if "__error__" in r:
                api_dropped.append({"id": r["__item__"]["id"],
                                    "reason": f"api-error: {r['__error__']}",
                                    "raw_question": r["__item__"]["question"]})
            elif r.get("status") == "keep":
                kept.append(r["spec"])
            else:
                api_dropped.append({"id": r["id"], "reason": r.get("reason", ""),
                                    "raw_question": r.get("raw_question", "")})
        write_jsonl(kept_path, kept)
        write_jsonl(dropped_path, prefilter_drops + api_dropped)

    if todo:
        await ds_client.run_batch(
            todo, build_normalize_messages, parse_normalize,
            model=args.model, concurrency=args.concurrency, on_progress=_save, save_every=50,
        )
    else:
        _save([])  # still refresh files to fold in this run's prefilter drops
        print("Nothing to process (use --fresh to redo).")

    final_kept = _load(kept_path)
    by_domain: dict[str, int] = {}
    for s in final_kept:
        by_domain[s["domain"]] = by_domain.get(s["domain"], 0) + 1
    print(f"\nKept {len(final_kept)} -> {OUT_KEPT}  | domains: {by_domain}")
    print(f"Dropped {len(_load(dropped_path))} (audit) -> {OUT_DROPPED}")


def main() -> None:
    p = argparse.ArgumentParser(description="Normalize Vietjack -> ProblemSpec JSONL")
    p.add_argument("--grades", type=int, nargs="+", default=[10, 11, 12])
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=10)
    p.add_argument("--model", default=COMMERCIAL_MODEL_FLASH)
    p.add_argument("--no-prefilter", dest="prefilter", action="store_false",
                   help="Skip the offline keyword pre-filter (send everything to the API).")
    p.add_argument("--parse-only", action="store_true",
                   help="Offline: parse + pre-filter stats only, no API.")
    p.add_argument("--fresh", action="store_true",
                   help="Ignore existing output and redo from scratch (default: resume).")
    args = p.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
