"""Trajectory schema — the contract shared across all v06 data-pipeline stages.

A *trajectory* is one execution-verified PoT sample destined for SFT. Per the
locked v06 design (see ../README.md), the assistant turn is a SINGLE Python
block preceded by a short reason; the script prints `FINAL ANSWER:` / `UNIT:`.
We never put a trajectory into the SFT set unless its code was executed and the
printed answer matched gold via `shared/eval/scorer.py` (the execution gate).

`provenance` carries everything the Data Disclosure Document needs: which route
produced it (self-gen vs DeepSeek teacher), the generating model, temperature,
and how many retries it took. Keep it accurate — external/teacher data must be
declared and must never leak into inference.

Files are stored as JSONL (one Trajectory per line). Intermediate stages read
and write the same shape so they compose:

    filter/normalize  -> ProblemSpec  (no trajectory yet)
    selfgen/teacher   -> Trajectory   (candidate, execution-verified)
    guards            -> Trajectory   (deduped, spurious-correct rejected)
    build_sft         -> SFT JSONL    (Qwen chat-template messages)
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Iterator, Literal

Route = Literal["self_gen", "teacher_residual", "teacher_rewrite"]
DatasetSource = Literal["btc_golden", "vietjack"]


@dataclass
class ProblemSpec:
    """A normalized, filter-passed problem ready for trajectory generation.

    One ProblemSpec per source problem. `answer`/`unit` are the verified gold
    used by the execution gate. Produced by Phase-1 (filter + normalize).
    """

    id: str                         # source problem id, e.g. "LD343" or "vj_l12_0042"
    question: str                   # English problem statement (BTC format)
    domain: str                     # canonical 6-way domain (see taxonomy.py)
    answer_type: str                # numeric | yes_no | multi_value | text
    gold_answer: str
    gold_unit: str
    dataset_source: DatasetSource
    # optional context carried for the teacher route (e.g. original CoT / VN source)
    meta: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "ProblemSpec":
        return cls(**{k: d[k] for k in cls.__dataclass_fields__ if k in d})


@dataclass
class Provenance:
    """Where a trajectory came from — declared in the Data Disclosure Document."""

    route: Route
    gen_model: str                  # e.g. "Qwen/Qwen3.5-4B" or "deepseek-v4-pro"
    temperature: float
    retry_count: int = 0            # input-feedback retries before success
    sample_idx: int = 0             # which of the K self-gen samples this was
    created_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Trajectory:
    """An execution-verified PoT sample. `is_correct` must be True for SFT."""

    id: str                         # unique: f"{source_id}#{route}{sample_idx}"
    source_id: str
    question: str
    domain: str
    answer_type: str
    gold_answer: str
    gold_unit: str
    dataset_source: DatasetSource

    # the model output we train on
    assistant: str                  # full assistant turn (short reason + code block)
    code: str                       # extracted Python

    # execution-gate evidence
    exec_answer: str                # what the script printed for FINAL ANSWER
    exec_unit: str                  # what the script printed for UNIT
    exec_stdout: str
    is_correct: bool                # scorer verdict vs gold (must be True)

    provenance: Provenance

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Trajectory":
        prov = d.get("provenance", {})
        kwargs = {k: d[k] for k in cls.__dataclass_fields__ if k in d and k != "provenance"}
        kwargs["provenance"] = Provenance(**prov) if isinstance(prov, dict) else prov
        return cls(**kwargs)


# ------------------------------------------------------------------ JSONL I/O

def write_jsonl(path: str | Path, records: Iterable) -> int:
    """Write dataclass records (with .to_dict) or plain dicts as JSONL. Returns count."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            obj = r.to_dict() if hasattr(r, "to_dict") else r
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            n += 1
    return n


def read_jsonl(path: str | Path) -> Iterator[dict]:
    """Yield dicts from a JSONL file."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)
