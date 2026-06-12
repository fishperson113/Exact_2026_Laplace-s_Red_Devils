"""Phase-2 Step-4 guards: turn verified candidates into the clean SFT set.

RUNS ANYWHERE (pure CPU). Input = the verified trajectories from both routes
(`trajectories_selfgen.jsonl` + `trajectories_teacher.jsonl`). Even though every
input already passed the execution gate, "the printed number equals gold" is not
enough -- a script can *echo* the gold instead of *computing* it (especially for
yes_no / low-entropy numerics). This stage enforces that the code actually does
the work, then trims redundancy:

  1. spurious-correct reject -- the answer must be computed, not hardcoded/echoed,
  2. dedup        -- drop identical (normalized) code per problem,
  3. cap          -- keep at most --cap diverse trajectories per problem,
                     preferring on-policy (self_gen) > low temperature > few retries.

Domain oversampling is deferred to the Phase-3 stratified split (build_sft.py);
here we only report the distribution so that split can balance it.

Run:
    PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.guards
    PYTHONPATH=. python -m ...guards --cap 4
"""

from __future__ import annotations

import argparse
import difflib
import re
from collections import Counter, defaultdict

from app.physics_solution.config import repo_root
from app.physics_solution.shared.eval.scorer import _parse_sci_notation, _safe_float
from app.physics_solution.versions.v06_finetune.data_pipeline import pot_common
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import write_jsonl

IN_SELFGEN = "app/physics_solution/versions/v06_finetune/output/trajectories_selfgen.jsonl"
IN_HINTED = "app/physics_solution/versions/v06_finetune/output/trajectories_hinted.jsonl"
IN_TEACHER = "app/physics_solution/versions/v06_finetune/output/trajectories_teacher.jsonl"  # legacy (deprecated)
OUT_SFT = "app/physics_solution/versions/v06_finetune/output/trajectories_sft.jsonl"
OUT_REJECTED = "app/physics_solution/versions/v06_finetune/output/guards_rejected.jsonl"

# A computation marker -> at least one of these must appear (comments stripped).
_ARITH_RE = re.compile(r"\*\*|//|[*/]|math\.|np\.|numpy\.|sympy|\bsqrt\b|\bsum\(")
_COMPARE_RE = re.compile(r"[<>]=?|==|!=|isclose|\babs\(")
# the FINAL ANSWER value baked directly into a string literal after the colon
_FINAL_LIT_RE = re.compile(r"""["']FINAL\s*ANSWER\s*:\s*([^"']*)["']""", re.IGNORECASE)
# interpolation mechanisms -> the value is computed, not baked (checked per line)
_FSTRING_RE = re.compile(r"""[fF][rR]?["']|[rR][fF]["']""")
_FORMAT_CALL_RE = re.compile(r"\.\s*format\s*\(")
_PERCENT_FMT_RE = re.compile(r"%[-+0-9.* ]*[sdifgeExX]")
# numeric literals in code, not part of an identifier / attribute
_NUM_LIT_RE = re.compile(r"(?<![\w.])[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?")


def _gold_floats(gold_answer: str, answer_type: str) -> list[float]:
    """Parse gold into comparable floats (for the hardcoded-literal check)."""
    parts = gold_answer.split(";") if answer_type == "multi_value" else [gold_answer]
    out: list[float] = []
    for p in parts:
        p = p.strip()
        v = _parse_sci_notation(p)
        if v is None:
            v = _safe_float(p)
        if v is not None:
            out.append(v)
    return out


def _final_answer_hardcoded(code: str) -> bool:
    """True if a FINAL ANSWER is emitted as a baked string literal (not interpolated).

    `print("FINAL ANSWER: 36.32")` / `print("FINAL ANSWER: 3.29 * 10^{6}")` /
    `print("FINAL ANSWER: Yes")` -> True (literal braces are NOT interpolation).
    `print(f"FINAL ANSWER: {ans:.4g}")`, `"...{}".format(x)`, `"...%.2f" % x`,
    `print("FINAL ANSWER:", ans)` -> False (value is computed / supplied separately).
    """
    for line in code.splitlines():
        if "final" not in line.lower():
            continue
        m = _FINAL_LIT_RE.search(line)
        if not m or not m.group(1).strip():
            continue  # no baked content after the colon (value comes from a var/arg)
        # computed if this line interpolates via f-string / .format() / %-format
        if (_FSTRING_RE.search(line) or _FORMAT_CALL_RE.search(line)
                or _PERCENT_FMT_RE.search(line)):
            continue
        return True
    return False


def _gold_as_literal(code: str, golds: list[float], rel_tol: float) -> bool:
    """True if EVERY gold value sits in the code as a near-exact numeric literal.

    Requiring *all* components (not just one) keeps false positives low: a real
    computed solution rarely has all of its answers pre-written as input literals,
    whereas a single multi_value component coinciding with a given input is common.
    """
    if not golds:
        return False
    body = pot_common.normalize_code(code)  # comments stripped
    lits: list[float] = []
    for tok in _NUM_LIT_RE.findall(body):
        try:
            lits.append(float(tok))
        except ValueError:
            pass

    def _present(g: float) -> bool:
        for lit in lits:
            if g == 0:
                if abs(lit) < 1e-12:
                    return True
            elif abs(lit - g) <= rel_tol * abs(g):
                return True
        return False

    return all(_present(g) for g in golds)


# routes whose model SAW the gold answer (and could therefore hardcode it)
_TEACHER_ROUTES = {"teacher_residual", "teacher_rewrite"}


def spurious_reason(traj: dict, rel_tol: float) -> str | None:
    """Return a rejection reason, or None to keep. Pure code-quality check.

    Guard strength depends on whether the model SAW the gold answer:
      - self-gen never sees gold, so it cannot echo/hardcode it; a correct numeric
        answer is also not a lucky guess (continuous space). The only self-gen
        concern is a baked literal print and yes_no lucky 50/50 guesses.
      - the teacher sees gold, so we additionally reject gold baked as a literal
        and code with no real computation.
    """
    code = traj.get("code", "") or ""
    at = traj.get("answer_type", "")
    route = traj.get("provenance", {}).get("route", "")
    norm = pot_common.normalize_code(code)

    # (1) baked-literal FINAL ANSWER -- not reproducible computation -- all routes.
    if _final_answer_hardcoded(code):
        return "literal_final_answer"

    # (2) yes_no must show a comparison -- a correct Yes/No is otherwise a coin flip.
    if at == "yes_no":
        return None if _COMPARE_RE.search(norm) else "no_comparison"

    # (3) teacher-only (it saw gold): reject hardcoded gold + no-computation echoes.
    #     For self-gen these are false positives (e.g. resonance Z=R=60 is a valid
    #     identity with no arithmetic, and a coinciding literal is just a given).
    if route in _TEACHER_ROUTES:
        if at in ("numeric", "multi_value") and _gold_as_literal(
                code, _gold_floats(traj.get("gold_answer", ""), at), rel_tol):
            return "gold_hardcoded_literal"
        if not _ARITH_RE.search(norm):
            return "no_computation"
    return None


# preference order when capping: pure on-policy first, then hinted (still Qwen, but guided),
# then any legacy teacher; within a route, lower temperature / fewer retries is cleaner.
_ROUTE_RANK = {"self_gen": 0, "self_gen_hinted": 1, "teacher_residual": 2, "teacher_rewrite": 2}


def _sort_key(traj: dict) -> tuple:
    prov = traj.get("provenance", {})
    return (
        _ROUTE_RANK.get(prov.get("route", ""), 9),
        float(prov.get("temperature", 9.0)),
        int(prov.get("retry_count", 9)),
    )


def _select_diverse(group_sorted: list[dict], cap: int) -> tuple[list[dict], list[dict]]:
    """Keep `cap` trajectories that are as DIFFERENT as possible (method diversity).

    `group_sorted` is already sorted best-first by `_sort_key` and deduped. Anchor #1 =
    the cleanest solution (on-policy, low temp, few retries). Each further pick maximizes
    code dissimilarity to the already-chosen set (greedy max-min on normalized code), so
    for cap=2 we get the cleanest solve + the most different valid solve (often a hotter
    temp / different method). Returns (kept, dropped).
    """
    if len(group_sorted) <= cap:
        return group_sorted, []
    norms = [pot_common.normalize_code(t.get("code", "")) for t in group_sorted]
    chosen = [0]  # anchor: best by _sort_key
    while len(chosen) < cap:
        # pick the candidate whose nearest already-chosen neighbour is the FARTHEST away
        best_i, best_sim = None, 2.0
        for i in range(len(group_sorted)):
            if i in chosen:
                continue
            nearest = max(difflib.SequenceMatcher(None, norms[i], norms[j]).ratio()
                          for j in chosen)
            if nearest < best_sim:
                best_sim, best_i = nearest, i
        chosen.append(best_i)
    chosen_set = set(chosen)
    kept = [group_sorted[i] for i in chosen]
    dropped = [group_sorted[i] for i in range(len(group_sorted)) if i not in chosen_set]
    return kept, dropped


def run(cap: int, rel_tol: float, select: str = "diverse") -> None:
    root = repo_root()
    candidates: list[dict] = []
    for path in (IN_SELFGEN, IN_HINTED, IN_TEACHER):
        candidates.extend(pot_common.load_jsonl_if_exists(root / path))
    print(f"Loaded {len(candidates)} candidate trajectories "
          f"(self_gen + hinted [+ legacy teacher]).")
    if not candidates:
        raise SystemExit("No candidate trajectories. Run selfgen.py / teacher.py first.")

    # 1. spurious-correct reject -------------------------------------------------
    kept_after_spurious: list[dict] = []
    rejected: list[dict] = []
    reasons = Counter()
    for t in candidates:
        reason = spurious_reason(t, rel_tol)
        if reason:
            reasons[reason] += 1
            rejected.append({**t, "_reject_reason": reason})
        else:
            kept_after_spurious.append(t)

    # 2 + 3. dedup + cap per problem --------------------------------------------
    by_problem: dict[str, list[dict]] = defaultdict(list)
    for t in kept_after_spurious:
        by_problem[t["source_id"]].append(t)

    final: list[dict] = []
    n_dup = 0
    n_capped = 0
    for sid, group in by_problem.items():
        group.sort(key=_sort_key)
        seen_hashes: set[str] = set()
        deduped: list[dict] = []
        for t in group:
            h = pot_common.code_hash(t.get("code", ""))
            if h in seen_hashes:
                n_dup += 1
                rejected.append({**t, "_reject_reason": "duplicate_code"})
                continue
            seen_hashes.add(h)
            deduped.append(t)
        if len(deduped) > cap:
            if select == "diverse":
                deduped, over = _select_diverse(deduped, cap)
            else:  # "clean": keep the top-`cap` by _sort_key (on-policy, low temp)
                deduped, over = deduped[:cap], deduped[cap:]
            for t in over:
                rejected.append({**t, "_reject_reason": "over_cap"})
            n_capped += len(over)
        final.extend(deduped)

    write_jsonl(root / OUT_SFT, final)
    write_jsonl(root / OUT_REJECTED, rejected)

    _report(candidates, final, reasons, n_dup, n_capped)
    print(f"\nWrote {len(final)} SFT trajectories -> {OUT_SFT}")
    print(f"Wrote {len(rejected)} rejected (audit) -> {OUT_REJECTED}")


def _report(candidates, final, spurious_reasons, n_dup, n_capped) -> None:
    print("\n--- guards report ---")
    print(f"candidates {len(candidates)} -> kept {len(final)}")
    print(f"  spurious rejected: {dict(spurious_reasons)}")
    print(f"  duplicates dropped: {n_dup} | over-cap dropped: {n_capped}")

    problems = {t["source_id"] for t in final}
    print(f"\nproblems covered: {len(problems)}")
    for label, key in (("domain", "domain"), ("source", "dataset_source"),
                       ("answer_type", "answer_type")):
        c = Counter(t[key] for t in final)
        print(f"  by {label}: {dict(sorted(c.items()))}")
    routes = Counter(t.get("provenance", {}).get("route", "?") for t in final)
    print(f"  by route: {dict(routes)}")
    # trajectories-per-problem histogram
    per = Counter(t["source_id"] for t in final)
    hist = Counter(per.values())
    print(f"  trajectories/problem histogram: {dict(sorted(hist.items()))}")


def main() -> None:
    p = argparse.ArgumentParser(description="Phase-2 guards: spurious-reject + dedup + cap")
    p.add_argument("--cap", type=int, default=4, help="max trajectories kept per problem")
    p.add_argument("--select", choices=("diverse", "clean"), default="diverse",
                   help="when capping: 'diverse' keeps the cleanest + most code-different "
                        "solves (method diversity); 'clean' keeps the top-cap by route/temp")
    p.add_argument("--spurious-rel-tol", type=float, default=1e-4,
                   help="tolerance for flagging a gold value baked in as a literal")
    args = p.parse_args()
    run(args.cap, args.spurious_rel_tol, args.select)


if __name__ == "__main__":
    main()
