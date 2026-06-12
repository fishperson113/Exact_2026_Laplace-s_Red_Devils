"""Compare the internal scorer's verdicts with the BTC-faithful strict scorer.

Re-scores the 348 recorded ensemble answers (output/final_experiment_raw.jsonl: 56 val +
60 golden questions x 3 runs) with shared/eval/scorer_btc.py — answer AND unit must both
match, NO SI-prefix rescue, no text containment — and reports where the internal
(optimistic) scorer and the strict scorer disagree, broken down by cause.

Run:  python -m app.physics_solution.versions.v07_ensemble_vLLM.compare_btc_scoring
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from app.physics_solution.shared.eval.normalizer import NO_UNIT, normalize_unit
from app.physics_solution.shared.eval.scorer import _parse_sci_notation
from app.physics_solution.shared.eval.scorer_btc import score_btc

_HERE = Path(__file__).parent
_RAW = _HERE / "output" / "final_experiment_raw.jsonl"
_VAL = _HERE.parent / "v07_final_version" / "val_56.jsonl"
_GOLDEN = _HERE.parent.parent / "data" / "golden" / "golden_60.csv"

_VOTE_RE = re.compile(r"\((?:\d+/\d+|sft\d+\+base\d+)\)\s*$")


_NUMLIKE_RE = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def _is_numeric_chunk(s: str) -> bool:
    """Every ';'-separated piece IS a bare number ('0.6;1.2', '3.57143%') — fullmatch,
    so '2.03e+06 V/m' is NOT numeric (model preds never use the x10^ spelling)."""
    s = s.strip().rstrip(";")
    if not s:
        return False
    for part in s.split(";"):
        part = part.strip().rstrip("%")
        if not _NUMLIKE_RE.fullmatch(part):
            return False
    return True


def split_pred(s: str) -> tuple[str, str]:
    """Recorded '0.0;0.0 C;J(3/5)' -> ('0.0;0.0', 'C;J'). Longest numeric prefix wins."""
    s = _VOTE_RE.sub("", s).strip()
    tokens = s.split(" ")
    if _is_numeric_chunk(tokens[0]):
        i = 1
        while i < len(tokens) and _is_numeric_chunk(" ".join(tokens[: i + 1])):
            i += 1
        value, unit = " ".join(tokens[:i]), " ".join(tokens[i:])
    elif tokens[0].rstrip(".,").lower() in ("yes", "no", "false", "true"):
        value, unit = tokens[0], " ".join(tokens[1:])
    elif len(tokens) > 1:                      # symbolic / text answer: last token = unit
        value, unit = " ".join(tokens[:-1]), tokens[-1]
    else:
        value, unit = s, ""
    if value.endswith("%") and not unit:       # extract() left '%' glued to the value
        value, unit = value[:-1], "%"
    return value.strip(), unit.strip()


def load_gold() -> dict[str, tuple[str, str]]:
    gold: dict[str, tuple[str, str]] = {}
    with open(_VAL) as f:
        for line in f:
            r = json.loads(line)
            gold[r["id"]] = (r["gold_answer"], r["gold_unit"])
    with open(_GOLDEN) as f:
        for r in csv.DictReader(f):
            gold[r["id"]] = (r["answer"], r["unit"])
    return gold


def main() -> None:
    gold = load_gold()
    recs = [json.loads(line) for line in open(_RAW)]

    diag = Counter()
    diffs: list[str] = []
    summary: dict[str, Counter] = {m: Counter() for m in ("sft", "base", "ens")}

    for rec in recs:
        g_ans, g_unit = gold[rec["id"]]
        for model in ("sft", "base", "ens"):
            internal_ok = rec[f"{model}_ok"]
            p_ans, p_unit = split_pred(rec[f"{model}_ans"])
            strict = score_btc(p_ans, p_unit, g_ans, g_unit)

            c = summary[model]
            c["n"] += 1
            c["internal"] += internal_ok
            c["strict"] += strict.correct
            if internal_ok == strict.correct:
                continue
            c["internal_only"] += internal_ok
            c["strict_only"] += not internal_ok

            # cause taxonomy for internal-pass/strict-fail
            if internal_ok:
                if strict.value_ok and not strict.unit_ok:
                    pu, gu = normalize_unit(p_unit), normalize_unit(g_unit)
                    cause = ("unit-missing" if pu == NO_UNIT or gu == NO_UNIT
                             else "unit-mismatch")
                elif not strict.value_ok and not strict.unit_ok:
                    cause = "prefix-scale (rescued internally)"
                else:
                    cause = "value-only (text containment / tolerance)"
            else:
                cause = "STRICT-PASS-ONLY (internal was pessimistic)"
            diag[f"{model}:{cause}"] += 1
            if model == "ens":
                diffs.append(
                    f"  [{rec['set']}/r{rec['run']}] {rec['id']:7} {cause:40} "
                    f"pred=({p_ans!r}, {p_unit!r})  gold=({g_ans!r}, {g_unit!r})"
                )

    print(f"{'model':6} {'n':>4} {'internal':>9} {'strict':>7} {'gap':>6}  (per-348 verdicts)")
    for model, c in summary.items():
        gap = c["internal"] - c["strict"]
        print(f"{model:6} {c['n']:4} {c['internal']:6} ({c['internal']/c['n']:.1%})"
              f" {c['strict']:4} ({c['strict']/c['n']:.1%}) {gap:+4}")

    print("\nDisagreement causes:")
    for k, v in sorted(diag.items()):
        print(f"  {k}: {v}")

    print(f"\nENSEMBLE diffs ({len(diffs)}):")
    for d in diffs:
        print(d)


if __name__ == "__main__":
    main()
