from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from services.config import LogicSFTConfig
from services.config_fol import FolSFTConfig

_HUB_ARTIFACT_SUBDIR = "experiment_artifacts"


def _load_json_dict(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _md_num(x: Any, *, nd: int = 4) -> str:
    if isinstance(x, (int, float)):
        if isinstance(x, float):
            return f"{x:.{nd}f}".rstrip("0").rstrip(".")
        return str(x)
    return str(x) if x is not None else "—"


def _fol_hub_readme_metrics_section(out_dir: Path) -> str:
    """Markdown hiển thị trên model card — tóm tắt từ JSON local (đồng bộ với experiment_artifacts/)."""
    lines: list[str] = []
    exp = _load_json_dict(out_dir / "experiment_log.json")
    train_m = _load_json_dict(out_dir / "train_metrics.json")
    fol_m = _load_json_dict(out_dir / "fol_eval_metrics.json")
    lat = _load_json_dict(out_dir / "fol_inference_latency.json")

    lines.append("## Tóm tắt kết quả (tự động)")
    lines.append("")
    lines.append(
        f"Bản đầy đủ nằm trong [`{_HUB_ARTIFACT_SUBDIR}/`]({_HUB_ARTIFACT_SUBDIR}/) trên repo này."
    )
    lines.append("")

    if train_m:
        lines.append("### Trainer (`train_metrics.json`)")
        lines.append("")
        priority = (
            "eval_loss",
            "epoch",
            "eval_runtime",
            "eval_samples_per_second",
            "loss",
        )
        shown: set[str] = set()
        for key in priority:
            if key in train_m and train_m[key] is not None:
                lines.append(f"- **{key}:** {_md_num(train_m[key], nd=6)}")
                shown.add(key)
        extra = 0
        for k in sorted(train_m.keys()):
            if k in shown:
                continue
            if extra >= 15:
                break
            v = train_m[k]
            if isinstance(v, (dict, list)):
                continue
            lines.append(f"- **{k}:** {_md_num(v, nd=6)}")
            extra += 1
        lines.append("")

    if fol_m:
        lines.append("### FOL RM eval (`fol_rm_eval_metrics.json`)")
        lines.append("")
        lines.append("| Split | RM | LE | BLEU |")
        lines.append("|-------|-----|-----|------|")
        for split in ("dev", "test"):
            row = fol_m.get(split)
            if not isinstance(row, dict):
                continue
            rm = row.get("rm_score")
            le = row.get("le_score")
            bleu = row.get("fol_bleu")
            lines.append(
                f"| **{split}** | {_md_num(rm, nd=4)} | {_md_num(le, nd=4)} | {_md_num(bleu, nd=4)} |"
            )
        lines.append("")

    if exp:
        hp = exp.get("hyperparameters_effective")
        if isinstance(hp, dict):
            lines.append("### Siêu tham số (từ `experiment_log.json`)")
            lines.append("")
            m = hp.get("model") if isinstance(hp.get("model"), dict) else {}
            t = hp.get("training") if isinstance(hp.get("training"), dict) else {}
            if m.get("name"):
                lines.append(f"- **model:** `{m.get('name')}`")
            if m.get("max_seq_length") is not None:
                lines.append(f"- **max_seq_length:** {m.get('max_seq_length')}")
            for k in (
                "num_train_epochs",
                "load_in_8bit",
                "use_unsloth",
                "unsloth_load_in_4bit",
                "gradient_accumulation_steps",
            ):
                if k in t and t[k] is not None:
                    lines.append(f"- **{k}:** {t[k]}")
            lines.append("")

        bench = exp.get("fol_test_benchmark")
        if isinstance(bench, dict):
            lines.append("### Benchmark test (trước / sau FT)")
            lines.append("")
            before = bench.get("before_finetune_summary") or {}
            after = bench.get("after_finetune") or {}
            if isinstance(before, dict) or isinstance(after, dict):
                lines.append("| | Trước FT | Sau FT |")
                lines.append("|---|----------|--------|")
                em_b = before.get("test_exact_match_full")
                em_a = after.get("test_exact_match_full")
                lines.append(
                    f"| **test exact match (full)** | {_md_num(em_b)} | {_md_num(em_a)} |"
                )
                nll_b = before.get("test_mean_nll_completion_full")
                nll_a = after.get("test_mean_nll_completion_full")
                if nll_b is not None or nll_a is not None:
                    lines.append(
                        f"| **test mean NLL completion** | {_md_num(nll_b, nd=4)} | {_md_num(nll_a, nd=4)} |"
                    )
            lines.append("")

        lat_b = exp.get("fol_inference_latency_benchmark")
        if isinstance(lat_b, dict) and not lat:
            lat = lat_b

    if lat:
        lines.append("### Độ trễ greedy (`fol_inference_latency.json`)")
        lines.append("")
        lines.append(
            f"- **split:** `{lat.get('split', '—')}` — **n:** {lat.get('n_samples', '—')}"
        )
        if lat.get("mean_seconds_per_sample") is not None:
            lines.append(
                f"- **trung bình:** {_md_num(lat.get('mean_seconds_per_sample'), nd=3)} s / mẫu "
                f"(σ ≈ {_md_num(lat.get('std_seconds_per_sample'), nd=3)} s)"
            )
        lines.append("")

    if not any([train_m, fol_m, exp, lat]):
        lines.append("_Chưa tìm thấy JSON metrics trong `out_dir` — chỉ có mô tả Artifacts bên dưới._")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def _fol_hub_readme_hub_reload_append_markdown(
    hub_eval: dict[str, Any], *, random_preview_n: int = 2
) -> str:
    """Đoạn Markdown nối thêm vào README sau bước tải lại từ Hub (chỉ xem trước vài mẫu)."""
    lines: list[str] = ["## Xác minh sau khi tải merged từ Hub", ""]
    repo = hub_eval.get("repo_id", "")
    if hub_eval.get("eval_mode") == "random_test_only":
        lines.append(
            f"Tải lại merged từ `{repo}` rồi **chỉ greedy trên N mẫu test ngẫu nhiên**; bảng dưới là exact-match **trên đúng N mẫu đó**. **JSON đủ:** [`{_HUB_ARTIFACT_SUBDIR}/fol_hub_reload_eval.json`]({_HUB_ARTIFACT_SUBDIR}/fol_hub_reload_eval.json)."
        )
    else:
        lines.append(
            f"Tải lại merged từ `{repo}` rồi chạy exact-match + greedy. **JSON đủ:** [`{_HUB_ARTIFACT_SUBDIR}/fol_hub_reload_eval.json`]({_HUB_ARTIFACT_SUBDIR}/fol_hub_reload_eval.json)."
        )
    lines.append("")
    mbs = hub_eval.get("metrics_by_split") or {}
    if isinstance(mbs, dict) and mbs:
        title = (
            "### Exact match (N mẫu test ngẫu nhiên)"
            if hub_eval.get("eval_mode") == "random_test_only"
            else "### Exact match (verify từ Hub)"
        )
        lines.append(title)
        lines.append("| Split | Accuracy | Đúng / Tổng |")
        lines.append("|-------|----------|-------------|")
        for sp in ("train", "dev", "test"):
            row = mbs.get(sp)
            if not isinstance(row, dict):
                continue
            lines.append(
                f"| **{sp}** | {_md_num(row.get('exact_match_rate'), nd=4)} | "
                f"{row.get('exact_match_count', '—')} / {row.get('total', '—')} |"
            )
        lines.append("")
    rts = hub_eval.get("random_test_samples") or []
    if rts and random_preview_n > 0:
        show = min(random_preview_n, len(rts))
        lines.append(
            f"### Xem trước mẫu test ngẫu nhiên (README: **{show}** / {len(rts)} — terminal + JSON có đủ)"
        )
        lines.append("")
        for i, row in enumerate(rts[:show]):
            if not isinstance(row, dict):
                continue
            idx = row.get("split_index", i)
            g = str(row.get("gold_assistant", "")).replace("\n", " ")[:240]
            p = str(row.get("predicted_raw", "")).replace("\n", " ")[:240]
            lines.append(f"**Mẫu {i + 1}** (`split_index={idx}`)")
            lines.append(f"- **gold (rút gọn):** `{g}` …")
            lines.append(f"- **pred (rút gọn):** `{p}` …")
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def upload_fol_hub_readme_hub_reload_addon(
    cfg: FolSFTConfig,
    hf_token: str,
    hub_eval: dict[str, Any],
    *,
    random_preview_n: int = 2,
) -> None:
    """Nối mục xác minh Hub vào README local rồi upload lại lên model repo."""
    assert cfg.out_dir is not None
    readme_path = cfg.out_dir / "merged_for_hub" / "README.md"
    if not readme_path.is_file():
        return
    text = readme_path.read_text(encoding="utf-8")
    marker = "## Xác minh sau khi tải merged từ Hub"
    if marker in text:
        return
    addon = _fol_hub_readme_hub_reload_append_markdown(
        hub_eval, random_preview_n=random_preview_n
    )
    readme_path.write_text(text.rstrip() + "\n\n" + addon + "\n", encoding="utf-8")
    api = HfApi(token=hf_token)
    api.upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=cfg.resolved_hf_repo(),
        repo_type="model",
    )


def upload_fol_experiment_artifacts_refresh(cfg: FolSFTConfig, hf_token: str) -> list[str]:
    """Upload lại toàn bộ JSON trong ``out_dir`` lên ``experiment_artifacts/`` (sau khi có file mới)."""
    api = HfApi(token=hf_token)
    return _upload_experiment_bundle(api, cfg.resolved_hf_repo(), cfg.out_dir)


def _upload_experiment_bundle(api: HfApi, repo: str, out_dir: Path) -> list[str]:
    """Đẩy log train / metrics / inference (một file JSON tổng hợp + JSON phụ)."""
    uploaded: list[str] = []
    if not out_dir.is_dir():
        return uploaded
    for name in (
        "experiment_log.json",
        "train_metrics.json",
        "test_accuracy.json",
        "fol_eval_metrics.json",
        "fol_preflight_baseline.json",
        "fol_test_benchmark.json",
        "fol_inference_latency.json",
        "fol_hub_reload_eval.json",
    ):
        p = out_dir / name
        if not p.is_file():
            continue
        path_in_repo = f"{_HUB_ARTIFACT_SUBDIR}/{name}"
        api.upload_file(
            path_or_fileobj=str(p),
            path_in_repo=path_in_repo,
            repo_id=repo,
            repo_type="model",
        )
        uploaded.append(path_in_repo)
    return uploaded


def push_merged_lora(cfg: LogicSFTConfig, hf_token: str) -> str:
    assert cfg.checkpoint_dir is not None and cfg.out_dir is not None
    if not cfg.checkpoint_dir.exists():
        raise FileNotFoundError(f"Chưa có checkpoint: {cfg.checkpoint_dir}")

    base = AutoModelForCausalLM.from_pretrained(
        cfg.model_name,
        torch_dtype="auto",
        trust_remote_code=cfg.trust_remote_code,
        device_map="cpu",
    )
    model = PeftModel.from_pretrained(base, str(cfg.checkpoint_dir))
    merged = model.merge_and_unload()

    merged_dir = cfg.out_dir / "merged_for_hub"
    merged_dir.mkdir(parents=True, exist_ok=True)
    merged.save_pretrained(merged_dir)

    tok = AutoTokenizer.from_pretrained(
        str(cfg.checkpoint_dir), trust_remote_code=cfg.trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    tok.save_pretrained(merged_dir)

    repo = cfg.resolved_hf_repo()
    readme = merged_dir / "README.md"
    readme.write_text(
        f"""---
license: apache-2.0
base_model: {cfg.model_name}
tags:
  - exact-2026
  - logic
---

# {repo.split("/")[-1]}

Repo: `{repo}`

LoRA SFT; best checkpoint theo **eval_accuracy** (parse nhãn trắc nghiệm / Yes-No).

## Artifacts (phiên bản thí nghiệm)

Trong thư mục `{_HUB_ARTIFACT_SUBDIR}/` trên Hub:

- **experiment_log.json** — siêu tham số (dạng gần `configs/logic_model.yaml`), `trainer_log_history` đầy đủ, bảng **epoch_metrics_train_dev_test** (loss train gần nhất, dev loss/accuracy, test accuracy mỗi epoch nếu bật), mẫu inference sau `run_test_eval`.
- **train_metrics.json** — metrics eval cuối cùng từ `Trainer`.
- **test_accuracy.json** — accuracy test sau train (nếu đã chạy bước eval test).

Biến môi trường: `LOGIC_LOG_TEST_EACH_EPOCH`, `LOGIC_EXPERIMENT_INFERENCE_SAMPLES` (xem `LogicSFTConfig`).
""",
        encoding="utf-8",
    )

    merged.push_to_hub(
        repo,
        token=hf_token,
        private=cfg.hf_private,
        commit_message=cfg.hf_commit_message,
    )
    tok.push_to_hub(repo, token=hf_token, private=cfg.hf_private)
    api = HfApi(token=hf_token)
    api.upload_file(
        path_or_fileobj=str(readme),
        path_in_repo="README.md",
        repo_id=repo,
        repo_type="model",
    )
    _upload_experiment_bundle(api, repo, cfg.out_dir)
    return f"https://huggingface.co/{repo}"


def push_merged_fol_lora(cfg: FolSFTConfig, hf_token: str) -> str:
    """Merge LoRA FOL → full weights, đẩy lên Hub với prefix `fol-...`."""
    assert cfg.checkpoint_dir is not None and cfg.out_dir is not None
    if not cfg.checkpoint_dir.exists():
        raise FileNotFoundError(f"Chưa có checkpoint: {cfg.checkpoint_dir}")

    base = AutoModelForCausalLM.from_pretrained(
        cfg.model_name,
        torch_dtype="auto",
        trust_remote_code=cfg.trust_remote_code,
        device_map="cpu",
    )
    model = PeftModel.from_pretrained(base, str(cfg.checkpoint_dir))
    merged = model.merge_and_unload()

    merged_dir = cfg.out_dir / "merged_for_hub"
    merged_dir.mkdir(parents=True, exist_ok=True)
    merged.save_pretrained(merged_dir)

    tok = AutoTokenizer.from_pretrained(
        str(cfg.checkpoint_dir), trust_remote_code=cfg.trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    tok.save_pretrained(merged_dir)

    repo = cfg.resolved_hf_repo()
    readme = merged_dir / "README.md"
    metrics_section = _fol_hub_readme_metrics_section(cfg.out_dir)
    readme.write_text(
        f"""---
license: apache-2.0
base_model: {cfg.model_name}
tags:
  - exact-2026
  - fol
---

# {repo.split("/")[-1]}

Repo: `{repo}`

LoRA SFT — dịch **premises NL → premises FOL** (JSON `premises_fol` trong completion).

{metrics_section}
## Artifacts

Trong `{_HUB_ARTIFACT_SUBDIR}/`:

- **experiment_log.json** — siêu tham số (gần `configs/fol_model.yaml`), `fol_eval_*` sau eval greedy, `fol_inference_latency_benchmark` nếu bật benchmark.
- **train_metrics.json** — metrics cuối từ `Trainer`.
- **fol_eval_metrics.json** — exact match FOL (nếu có).
- **fol_inference_latency.json** — trung bình thời gian greedy một mẫu (sau FT, nếu có).
- **fol_hub_reload_eval.json** — sau push: tải merged từ Hub, greedy trên N mẫu test ngẫu nhiên + exact-match trên đúng N mẫu (CLI).

Biến môi trường: prefix `FOL_*` (xem `FolSFTConfig` trong `services/config_fol.py`).
""",
        encoding="utf-8",
    )

    merged.push_to_hub(
        repo,
        token=hf_token,
        private=cfg.hf_private,
        commit_message=cfg.hf_commit_message,
    )
    tok.push_to_hub(repo, token=hf_token, private=cfg.hf_private)
    api = HfApi(token=hf_token)
    api.upload_file(
        path_or_fileobj=str(readme),
        path_in_repo="README.md",
        repo_id=repo,
        repo_type="model",
    )
    _upload_experiment_bundle(api, repo, cfg.out_dir)
    return f"https://huggingface.co/{repo}"
