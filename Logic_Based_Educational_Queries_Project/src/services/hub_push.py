from __future__ import annotations

from pathlib import Path

from huggingface_hub import HfApi
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from services.config import LogicSFTConfig
from services.config_fol import FolSFTConfig

_HUB_ARTIFACT_SUBDIR = "experiment_artifacts"


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
    tok.save_pretrained(merged_dir)

    repo = cfg.resolved_hf_repo()
    readme = merged_dir / "README.md"
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

## Artifacts

Trong `{_HUB_ARTIFACT_SUBDIR}/`:

- **experiment_log.json** — siêu tham số (gần `configs/fol_model.yaml`), `fol_eval_*` sau eval greedy.
- **train_metrics.json** — metrics cuối từ `Trainer`.
- **fol_eval_metrics.json** — exact match FOL (nếu có).

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
