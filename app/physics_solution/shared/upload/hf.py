"""Push a model + tokenizer + model card to the Laplaces-Red-Devils HF org.

Naming convention (agreed 2026-05-18):
    physics-v{NN:02d}-{strategy}-{base}
e.g. physics-v01-zeroshot-qwen3.5-4b
     physics-v04-lora-qwen3.5-4b
     physics-v07-rag-finetune-qwen3.5-4b

The uploader is the same regardless of whether the weights were
fine-tuned or not — for baselines we push the upstream weights verbatim
so every version has its own immutable artefact + card.

The model card embeds **everything** we have on the run:
- inference config (model id, dtype, batch size, max_new_tokens, temperature, prefix)
- hardware (GPU name, VRAM, CUDA, torch / transformers versions)
- test set info (path, n, domain breakdown)
- metrics (accuracy, mean latency, per-domain accuracy)
- timestamps + free-text notes

So a teammate or judge looking at the HF page knows everything about how
the numbers were produced.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import HfApi, create_repo


DEFAULT_ORG = "Laplaces-Red-Devils"


@dataclass
class VersionMeta:
    # --- identity -----------------------------------------------------------
    version_num: int
    strategy: str  # "zeroshot", "fewshot", "rag", "lora", "lora-rag", ...
    base: str  # "qwen3.5-4b", "qwen3-4b-thinking", ...
    description: str
    base_model_id: str  # upstream HF id this artefact is built on

    # --- metrics ------------------------------------------------------------
    test_accuracy: float | None = None
    test_n: int | None = None
    test_correct: int | None = None
    mean_latency_s: float | None = None
    per_domain_accuracy: dict[str, float] = field(default_factory=dict)
    per_domain_count: dict[str, int] = field(default_factory=dict)

    # --- inference config ---------------------------------------------------
    dtype: str | None = None
    effective_dtype: str | None = None
    batch_size: int | None = None
    max_new_tokens: int | None = None
    temperature: float | None = None
    assistant_prefix: str | None = None
    n_examples: int | None = None  # for fewshot

    # --- hardware -----------------------------------------------------------
    device: str | None = None
    gpu_name: str | None = None
    gpu_vram_gb: float | None = None
    cuda_version: str | None = None
    torch_version: str | None = None
    transformers_version: str | None = None
    python_version: str | None = None

    # --- data ---------------------------------------------------------------
    test_file: str | None = None
    test_seed: int | None = None
    fewshot_pool_size: int | None = None

    # --- error analysis -----------------------------------------------------
    per_answer_type_accuracy: dict[str, float] = field(default_factory=dict)
    per_answer_type_count: dict[str, int] = field(default_factory=dict)
    failmode_counts: dict[str, int] = field(default_factory=dict)

    # --- misc ---------------------------------------------------------------
    timestamp_utc: str | None = None
    notes: str = ""

    def repo_name(self) -> str:
        return f"physics-v{self.version_num:02d}-{self.strategy}-{self.base}"


# ---------------------------------------------------------------------- env capture


def collect_env_info() -> dict:
    """Detect what GPU / torch / transformers we're running on. Best-effort."""
    info: dict = {}
    import sys

    info["python_version"] = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    try:
        import torch

        info["torch_version"] = torch.__version__
        info["cuda_version"] = torch.version.cuda
        if torch.cuda.is_available():
            info["device"] = "cuda"
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = round(
                torch.cuda.get_device_properties(0).total_memory / (1024**3), 2
            )
        else:
            info["device"] = "cpu"
    except Exception:
        pass
    try:
        import transformers

        info["transformers_version"] = transformers.__version__
    except Exception:
        pass
    return info


def per_domain_breakdown(rows: list[dict]) -> tuple[dict[str, float], dict[str, int]]:
    """Compute accuracy + count per domain prefix from a results-rows list."""
    import re

    prefix_re = re.compile(r"^([A-Z]+)")
    counts: dict[str, int] = {}
    correct: dict[str, int] = {}
    for r in rows:
        qid = str(r.get("id", ""))
        m = prefix_re.match(qid)
        prefix = m.group(1) if m else "UNK"
        counts[prefix] = counts.get(prefix, 0) + 1
        if r.get("is_correct"):
            correct[prefix] = correct.get(prefix, 0) + 1
    acc = {
        p: round(correct.get(p, 0) / counts[p], 4) if counts[p] else 0.0 for p in counts
    }
    return acc, counts


def per_answer_type_breakdown(
    rows: list[dict],
) -> tuple[dict[str, float], dict[str, int]]:
    """Compute accuracy + count per answer type from results rows."""
    from app.physics_solution.shared.eval.scorer import detect_answer_type

    counts: dict[str, int] = {}
    correct: dict[str, int] = {}
    for r in rows:
        gold = str(r.get("gold_answer", ""))
        at = detect_answer_type(gold).value
        counts[at] = counts.get(at, 0) + 1
        if r.get("is_correct"):
            correct[at] = correct.get(at, 0) + 1
    acc = {
        t: round(correct.get(t, 0) / counts[t], 4) if counts[t] else 0.0 for t in counts
    }
    return acc, counts


def failmode_breakdown(rows: list[dict]) -> dict[str, int]:
    """Classify wrong rows into fail modes and return counts."""
    import pandas as pd
    from app.physics_solution.eda.scripts.v2.error_analysis import classify_row

    fm_counts: dict[str, int] = {}
    for r in rows:
        if r.get("is_correct"):
            continue
        row_series = pd.Series(r)
        mode = classify_row(row_series)
        fm_counts[mode] = fm_counts.get(mode, 0) + 1
    return fm_counts


# ---------------------------------------------------------------------- file IO


def load_token() -> str:
    """Read HF_TOKEN from app/physics_solution/.env (or env var)."""
    here = Path(__file__).resolve().parent.parent
    load_dotenv(here / ".env", override=False)
    token = (
        os.environ.get("HF_TOKEN")
        or os.environ.get("HF_TOKEN_CC")
        or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    )
    if not token:
        raise RuntimeError(
            "HF_TOKEN not found. Put it in app/physics_solution/.env as HF_TOKEN=hf_..."
        )
    return token


# ---------------------------------------------------------------------- model card


def _fmt(x, default: str = "—") -> str:
    if x is None or x == "":
        return default
    if isinstance(x, float):
        return f"{x:.4f}".rstrip("0").rstrip(".")
    return str(x)


def _domain_table(acc: dict[str, float], cnt: dict[str, int]) -> str:
    if not acc:
        return "(no per-domain breakdown available)"
    lines = ["| Domain | n | Accuracy |", "|---|---|---|"]
    for p in sorted(acc, key=lambda k: -cnt.get(k, 0)):
        lines.append(f"| `{p}` | {cnt.get(p, 0)} | {acc[p]:.3f} |")
    return "\n".join(lines)


def _answer_type_table(acc: dict[str, float], cnt: dict[str, int]) -> str:
    if not acc:
        return "(no per-answer-type breakdown available)"
    lines = ["| Answer type | n | Accuracy |", "|---|---|---|"]
    for t in sorted(acc, key=lambda k: -cnt.get(k, 0)):
        lines.append(f"| `{t}` | {cnt.get(t, 0)} | {acc[t]:.3f} |")
    return "\n".join(lines)


def _failmode_table(fm: dict[str, int]) -> str:
    if not fm:
        return "(no fail-mode breakdown available)"
    total_wrong = sum(fm.values())
    lines = ["| Fail mode | Count | % of wrong |", "|---|---:|---:|"]
    for mode, cnt in sorted(fm.items(), key=lambda kv: -kv[1]):
        pct = cnt / total_wrong if total_wrong else 0
        lines.append(f"| `{mode}` | {cnt} | {pct:.1%} |")
    return "\n".join(lines)


def build_model_card(meta: VersionMeta, org: str = DEFAULT_ORG) -> str:
    accuracy_line = (
        f"**{_fmt(meta.test_accuracy)}** "
        f"({_fmt(meta.test_correct)} / {_fmt(meta.test_n)} correct, "
        f"mean latency {_fmt(meta.mean_latency_s)} s)"
        if meta.test_accuracy is not None
        else "_(not measured yet)_"
    )

    return f"""---
license: apache-2.0
tags:
- physics
- exact-2026
- type2
- electrical-circuits
- electrostatics
base_model: {meta.base_model_id}
language:
- en
---

# {meta.repo_name()}

EXACT 2026 — Task Type 2 (Physics Problems).
Team: **Laplace's Red Devils**.

## TL;DR

| | |
|---|---|
| Strategy | `{meta.strategy}` |
| Base | `{meta.base}` ({meta.base_model_id}) |
| Accuracy | {accuracy_line} |
| Built | {_fmt(meta.timestamp_utc)} |

## Strategy

{meta.description}

## Inference configuration

| Knob | Value |
|---|---|
| `dtype` | {_fmt(meta.dtype)} (effective: {_fmt(meta.effective_dtype)}) |
| `batch_size` | {_fmt(meta.batch_size)} |
| `max_new_tokens` | {_fmt(meta.max_new_tokens)} |
| `temperature` | {_fmt(meta.temperature)} |
| `assistant_prefix` | `{_fmt(meta.assistant_prefix, default='')}` |
| `n_examples` (few-shot) | {_fmt(meta.n_examples)} |

## Hardware

| | |
|---|---|
| Device | {_fmt(meta.device)} |
| GPU | {_fmt(meta.gpu_name)} ({_fmt(meta.gpu_vram_gb)} GB) |
| CUDA | {_fmt(meta.cuda_version)} |
| Python | {_fmt(meta.python_version)} |
| `torch` | {_fmt(meta.torch_version)} |
| `transformers` | {_fmt(meta.transformers_version)} |

## Test set

| | |
|---|---|
| File | `{_fmt(meta.test_file)}` |
| Size | {_fmt(meta.test_n)} questions |
| Seed | {_fmt(meta.test_seed)} |
| Few-shot pool size | {_fmt(meta.fewshot_pool_size)} |

### Per-domain accuracy

{_domain_table(meta.per_domain_accuracy, meta.per_domain_count)}

### Per-answer-type accuracy

{_answer_type_table(meta.per_answer_type_accuracy, meta.per_answer_type_count)}

## Error analysis

{_failmode_table(meta.failmode_counts)}

## How to reproduce

```bash
# 1. Pull this repo
git clone https://github.com/Laplaces-Red-Devils/Exact_2026_Laplace-s_Red_Devils
cd Exact_2026_Laplace-s_Red_Devils

# 2. Rebuild the exact test sample
python -m app.physics_solution.cli.prepare_sample \\
    --n {_fmt(meta.test_n)} --seed {_fmt(meta.test_seed)}

# 3. Run inference (config.py provides the defaults shown above)
python -m app.physics_solution.cli.inference --version v{meta.version_num:02d}_{meta.strategy.replace('-', '_')}

# 4. Or use this exact upload as the model:
python -m app.physics_solution.cli.inference \\
    --version v{meta.version_num:02d}_{meta.strategy.replace('-', '_')} \\
    --model-id {org}/{meta.repo_name()}
```

## Notes

{meta.notes or "(none)"}
"""


# ---------------------------------------------------------------------- push


def push(
    local_model_dir: str | os.PathLike,
    meta: VersionMeta,
    org: str = DEFAULT_ORG,
    private: bool = True,
    token: str | None = None,
    extra_files: list[str | os.PathLike] | None = None,
) -> str:
    """Push the directory at `local_model_dir` to HF as `<org>/<repo_name>`.

    `extra_files` lets the caller stage e.g. the inference results JSON / CSV
    alongside the weights.

    Returns the full repo id.
    """
    token = token or load_token()
    api = HfApi(token=token)

    repo_id = f"{org}/{meta.repo_name()}"
    create_repo(
        repo_id=repo_id,
        token=token,
        private=private,
        exist_ok=True,
        repo_type="model",
    )

    local_model_dir = Path(local_model_dir)
    # Model card + machine-readable meta sit next to the weights.
    (local_model_dir / "README.md").write_text(
        build_model_card(meta, org=org), encoding="utf-8"
    )
    (local_model_dir / "version_meta.json").write_text(
        json.dumps(asdict(meta), indent=2, ensure_ascii=False), encoding="utf-8"
    )

    for path in extra_files or []:
        src = Path(path)
        if not src.exists():
            continue
        # Stage under reports/ so weights stay tidy at repo root.
        dst_dir = local_model_dir / "reports"
        dst_dir.mkdir(parents=True, exist_ok=True)
        (dst_dir / src.name).write_bytes(src.read_bytes())

    api.upload_folder(
        folder_path=str(local_model_dir),
        repo_id=repo_id,
        repo_type="model",
        commit_message=f"upload {meta.repo_name()}",
    )
    return repo_id


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
