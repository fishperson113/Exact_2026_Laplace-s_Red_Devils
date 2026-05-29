"""Config loader cho FOL_Z3 pipeline.

Doc configs/fol_z3.yaml, cho phep override bang env vars.
Duoc import boi: pipeline.py, fol_inference.py, qa_inference.py
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class FOLz3Config:
    # FOL model
    fol_hub_repo_id: str = "Laplaces-Red-Devils/fol-v03-cot-origin-qwen2.5-3"
    fol_base_model: str = "Qwen/Qwen2.5-3B-Instruct"
    fol_max_new_tokens: int = 512

    # QA model
    qa_model_name: str = "Qwen/Qwen2.5-3B-Instruct"
    qa_max_new_tokens: int = 768

    # Z3
    z3_timeout_ms: int = 5000
    z3_max_premises: int = 50

    # Refinement (Neurosymbolic loop)
    refinement_max_retries: int = 2  # Z3 reject → FOL model sinh lai, toi da N lan

    # Inference
    device: str = "auto"
    load_in_8bit: bool = True
    trust_remote_code: bool = True
    batch_size: int = 1

    # Ablation
    use_fol: bool = True  # False = baseline (chi NL, khong FOL/Z3)

    # Hub
    hub_push_results: bool = True
    hub_repo_id: str = "Laplaces-Red-Devils/fol-z3-pipeline-results"
    hub_private: bool = False

    @classmethod
    def from_yaml(cls, yaml_path: str | Path) -> FOLz3Config:
        """Load config tu YAML, override bang env vars FOL_Z3_*."""
        yaml_path = Path(yaml_path)
        cfg: dict = {}
        if yaml_path.exists():
            with open(yaml_path, "r", encoding="utf-8") as f:
                raw = yaml.safe_load(f) or {}
            fm = raw.get("fol_model", {})
            qa = raw.get("qa_model", {})
            z3 = raw.get("z3", {})
            ref = raw.get("refinement", {})
            inf = raw.get("inference", {})
            abl = raw.get("ablation", {})
            hub = raw.get("hub", {})
            cfg = {
                "fol_hub_repo_id": fm.get("hub_repo_id"),
                "fol_base_model": fm.get("base_model"),
                "fol_max_new_tokens": fm.get("max_new_tokens"),
                "qa_model_name": qa.get("model_name"),
                "qa_max_new_tokens": qa.get("max_new_tokens"),
                "z3_timeout_ms": z3.get("timeout_ms"),
                "z3_max_premises": z3.get("max_premises"),
                "refinement_max_retries": ref.get("max_retries"),
                "device": inf.get("device"),
                "load_in_8bit": inf.get("load_in_8bit"),
                "trust_remote_code": inf.get("trust_remote_code"),
                "batch_size": inf.get("batch_size"),
                "use_fol": abl.get("use_fol"),
                "hub_push_results": hub.get("push_results"),
                "hub_repo_id": hub.get("repo_id"),
                "hub_private": hub.get("private"),
            }
            cfg = {k: v for k, v in cfg.items() if v is not None}

        # Env overrides
        if v := os.environ.get("FOL_Z3_HUB_REPO"):
            cfg["fol_hub_repo_id"] = v
        if v := os.environ.get("FOL_Z3_BASE_MODEL"):
            cfg["fol_base_model"] = v
        if v := os.environ.get("FOL_Z3_QA_MODEL"):
            cfg["qa_model_name"] = v
        if v := os.environ.get("FOL_Z3_DEVICE"):
            cfg["device"] = v
        if v := os.environ.get("FOL_Z3_USE_FOL"):
            cfg["use_fol"] = v.lower() in ("1", "true", "yes")

        return cls(**cfg)
