"""Reformat Logic_Based_Educational_Queries_clean.json -> per-question training rows.

Two phases:
  Phase 1 (deterministic, NO API):
    - flatten record -> 1 row per question (giu record_id + q_idx de split tranh leak)
    - premises_used: doi idx 1-based -> 0-based
    - gom used_fol = [premises-FOL[i] for i in premises_used]
    -> *_reformatted.json

  Phase 2 (Claude API):
    - voi moi row, synthesize reasoning.steps theo taxonomy:
        "Rule:" / "Fact:" / "Derive:" / "Conclusion:"
      Rule/Fact lay TU used_fol; Conclusion phai khop answer.
    - validate: prefix hop le, co Conclusion cuoi, predicate truy ve used_fol
    -> *_with_reasoning.json   (resume duoc: bo qua row da co reasoning hop le)

Chay:
  python build_reasoning_dataset.py --phase 1
  set ANTHROPIC_API_KEY=...   &&  python build_reasoning_dataset.py --phase 2 --limit 5
  python build_reasoning_dataset.py --phase 2            # full 776, resume tu cache
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ------------------------------------------------------------------ paths
HERE = Path(__file__).resolve()
PROJECT = HERE.parents[2]  # .../Logic_Based_Educational_Queries_Project
DEFAULT_IN = PROJECT / "data" / "raw" / "Logic_Based_Educational_Queries_clean.json"
DEFAULT_REFORMATTED = PROJECT / "data" / "processed" / "lbeq_reformatted.json"
DEFAULT_FINAL = PROJECT / "data" / "processed" / "lbeq_with_reasoning.json"

STEP_PREFIXES = ("Rule:", "Fact:", "Derive:", "Conclusion:")
DEFAULT_MODEL = "claude-sonnet-4-6"   # bulk 776 calls; doi --model claude-opus-4-8 neu can chat hon

# ------------------------------------------------------------------ Phase 1


def flatten(records: list[dict]) -> list[dict]:
    """1 record (premise set) -> N rows (1/question). premises_used: 1-based -> 0-based."""
    rows: list[dict] = []
    for rid, rec in enumerate(records):
        premises_fol = rec["premises-FOL"]
        premises_nl = rec["premises-NL"]
        n_prem = len(premises_fol)
        questions = rec["questions"]
        answers = rec["answers"]
        explanations = rec.get("explanation", [""] * len(questions))
        idx_lists = rec["idx"]

        for qi, question in enumerate(questions):
            raw_idx = idx_lists[qi] if qi < len(idx_lists) else []
            # 1-based -> 0-based, loc index ngoai pham vi (du lieu ban)
            used = sorted({i - 1 for i in raw_idx if 1 <= i <= n_prem})
            rows.append({
                "record_id": rid,
                "q_idx": qi,
                "premises_nl": premises_nl,
                "premises_fol": premises_fol,
                "query": question,
                "answer": answers[qi] if qi < len(answers) else "",
                "premises_used": used,                       # 0-based
                "used_fol": [premises_fol[i] for i in used],  # tien cho Phase 2 + validate
                "explanation": explanations[qi] if qi < len(explanations) else "",
                "reasoning": None,                            # Phase 2 dien vao
            })
    return rows


def run_phase1(in_path: Path, out_path: Path) -> list[dict]:
    records = json.loads(in_path.read_text(encoding="utf-8"))
    rows = flatten(records)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    # sanity report
    empty_used = sum(1 for r in rows if not r["premises_used"])
    bad_shift = sum(1 for r in rows if any(i < 0 for i in r["premises_used"]))
    print(f"[Phase 1] records={len(records)} -> rows={len(rows)}")
    print(f"[Phase 1] rows voi premises_used rong: {empty_used}")
    print(f"[Phase 1] rows co index am (loi shift): {bad_shift}")
    print(f"[Phase 1] da ghi: {out_path}")
    return rows


# ------------------------------------------------------------------ Phase 2: prompt

SYSTEM_PROMPT = """You are an expert in first-order logic (FOL) and formal proof.

You are given:
- A list of FOL premises that ARE USED to answer a question (numbered).
- The question (may contain multiple-choice options A./B./C./D.).
- The correct answer.
- A prose explanation of why that answer is correct.

Produce a step-by-step FOL derivation that justifies the correct answer, as a JSON
list of strings. EVERY step MUST start with exactly one of these prefixes:

  "Rule:"        a conditional / quantified law (uses ->, forall, exists, <->).
                 MUST come from one of the given USED premises.
  "Fact:"        a ground fact / concrete assignment.
                 MUST come from one of the given USED premises.
  "Derive:"      an intermediate inference: contrapositive, modus ponens,
                 a numeric comparison (e.g. 118 < 120), or combining earlier steps.
  "Conclusion:"  the final result. There MUST be exactly one, and it MUST be the
                 LAST step, and it MUST logically correspond to the correct answer
                 (for Yes/No: state the entailed proposition; for MCQ: end with the
                 chosen option, e.g. "... => Option A").

Rules:
- Use FOL symbols where natural: ->, <->, not, forall, exists, and, or, <, >, =, >=, <=.
- Rule/Fact steps must paraphrase the GIVEN used premises only (do not invent predicates).
- Keep steps short and formal; NO long prose sentences.
- For contrapositive questions, include an explicit "Derive: contrapositive ..." step.

Output ONLY a JSON object: {"steps": ["...", "..."]}  and nothing else."""

USER_TEMPLATE = """USED PREMISES (FOL):
{used_block}

QUESTION:
{question}

CORRECT ANSWER:
{answer}

EXPLANATION:
{explanation}

Return JSON: {{"steps": [...]}}"""


def build_user_msg(row: dict) -> str:
    used_block = "\n".join(f"{i}. {f}" for i, f in enumerate(row["used_fol"])) or "(none)"
    return USER_TEMPLATE.format(
        used_block=used_block,
        question=row["query"],
        answer=row["answer"],
        explanation=row["explanation"],
    )


# ------------------------------------------------------------------ Phase 2: validate

_WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def _predicates(text: str) -> set[str]:
    """Lay ten predicate/identifier (bo qua tu khoa logic) de truy nguon."""
    skip = {"forall", "exists", "not", "and", "or", "ForAll", "Exists",
            "Rule", "Fact", "Derive", "Conclusion", "Option", "Premise",
            "contrapositive", "modus", "ponens", "premise", "satisfied"}
    return {w for w in _WORD.findall(text) if w not in skip and len(w) > 1}


def validate_steps(steps, row: dict) -> tuple[bool, str]:
    """Tra (ok, reason). Kiem tra cau truc + truy nguon predicate."""
    if not isinstance(steps, list) or not steps:
        return False, "steps rong/khong phai list"
    if not all(isinstance(s, str) and s.strip() for s in steps):
        return False, "co step rong/khong phai string"
    if not all(s.lstrip().startswith(STEP_PREFIXES) for s in steps):
        return False, "co step thieu prefix hop le"
    if not steps[-1].lstrip().startswith("Conclusion:"):
        return False, "step cuoi khong phai Conclusion"
    if sum(s.lstrip().startswith("Conclusion:") for s in steps) != 1:
        return False, "phai co dung 1 Conclusion"
    if not any(s.lstrip().startswith(("Rule:", "Fact:")) for s in steps):
        return False, "thieu Rule/Fact"

    # truy nguon: predicate trong Rule/Fact phai xuat hien trong used_fol
    src = _predicates(" ".join(row["used_fol"]))
    if src:  # neu used_fol rong thi bo qua check nay
        for s in steps:
            if s.lstrip().startswith(("Rule:", "Fact:")):
                preds = _predicates(s)
                if preds and preds.isdisjoint(src):
                    return False, f"Rule/Fact khong truy ve used_fol: {s[:60]}"
    return True, "ok"


# ------------------------------------------------------------------ Phase 2: run

def synthesize_one(client, model: str, row: dict, max_retries: int = 3):
    """Goi Claude -> steps hop le, hoac None neu that bai sau retry."""
    user_msg = build_user_msg(row)
    last_err = ""
    for attempt in range(max_retries):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            text = resp.content[0].text.strip()
            m = re.search(r"\{.*\}", text, re.DOTALL)
            if not m:
                last_err = "khong tim thay JSON"
                continue
            steps = json.loads(m.group()).get("steps")
            ok, reason = validate_steps(steps, row)
            if ok:
                return steps
            last_err = reason
        except Exception as e:  # noqa: BLE001
            last_err = f"{type(e).__name__}: {e}"
    return None, last_err  # type: ignore[return-value]


def run_phase2(reformatted_path: Path, out_path: Path, model: str,
               limit: int | None, workers: int) -> None:
    try:
        import anthropic
    except ImportError:
        sys.exit("Chua cai anthropic SDK:  pip install anthropic")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Chua set ANTHROPIC_API_KEY")

    rows = json.loads(reformatted_path.read_text(encoding="utf-8"))

    # resume: nap reasoning da co tu out_path (theo record_id|q_idx)
    done: dict[tuple[int, int], dict] = {}
    if out_path.exists():
        for r in json.loads(out_path.read_text(encoding="utf-8")):
            if r.get("reasoning"):
                done[(r["record_id"], r["q_idx"])] = r["reasoning"]
        print(f"[Phase 2] resume: {len(done)} row da co reasoning")

    todo = [r for r in rows if (r["record_id"], r["q_idx"]) not in done]
    if limit:
        todo = todo[:limit]
    print(f"[Phase 2] can synthesize: {len(todo)} (model={model}, workers={workers})")

    client = anthropic.Anthropic()
    failures: list[tuple[int, int, str]] = []
    done_count = 0

    def work(row):
        res = synthesize_one(client, model, row)
        if isinstance(res, tuple):  # (None, reason)
            return row, None, res[1]
        return row, res, ""

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(work, r) for r in todo]
        for fut in as_completed(futs):
            row, steps, err = fut.result()
            key = (row["record_id"], row["q_idx"])
            if steps:
                done[key] = {"type": "fol", "steps": steps}
                done_count += 1
            else:
                failures.append((key[0], key[1], err))
            n = done_count + len(failures)
            if n % 20 == 0:
                print(f"  ... {n}/{len(todo)}  (ok={done_count}, fail={len(failures)})")

    # ghi ket qua (giu thu tu goc, dien reasoning)
    for r in rows:
        key = (r["record_id"], r["q_idx"])
        if key in done:
            r["reasoning"] = done[key]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[Phase 2] OK={done_count}  FAIL={len(failures)}")
    if failures:
        print("[Phase 2] mau fail (record_id, q_idx, ly do):")
        for rid, qi, err in failures[:15]:
            print(f"    ({rid},{qi}) {err}")
    print(f"[Phase 2] da ghi: {out_path}")


# ------------------------------------------------------------------ main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["1", "2"], required=True)
    ap.add_argument("--in", dest="in_path", type=Path, default=DEFAULT_IN)
    ap.add_argument("--reformatted", type=Path, default=DEFAULT_REFORMATTED)
    ap.add_argument("--out", type=Path, default=DEFAULT_FINAL)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    if args.phase == "1":
        run_phase1(args.in_path, args.reformatted)
    else:
        if not args.reformatted.exists():
            print("[Phase 2] chua co file reformatted, chay Phase 1 truoc...")
            run_phase1(args.in_path, args.reformatted)
        run_phase2(args.reformatted, args.out, args.model, args.limit, args.workers)


if __name__ == "__main__":
    main()
