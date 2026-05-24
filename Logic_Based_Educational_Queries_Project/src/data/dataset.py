from __future__ import annotations

import ast
import os
from pathlib import Path

import pandas as pd
from datasets import Dataset, DatasetDict

from data.nl_to_fol import fol_block_from_lists, premises_fol_for_training
from data.prompts import (
    ASSISTANT_TEMPLATE_SFT,
    PREMISES_FOL_HEADER,
    PREMISES_NL_HEADER,
    SYSTEM_PROMPT_SFT,
    USER_TEMPLATE_SFT,
)
from services.config import LogicSFTConfig


def _discover_sft_processed_dir() -> Path | None:
    """Tìm thư mục chứa train.csv (logic_sft) từ cwd và parent."""
    seen: set[str] = set()
    for start in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
        key = str(start)
        if key in seen:
            continue
        seen.add(key)
        for rel in (
            ("app", "data", "processed", "logic_sft"),
            ("data", "processed", "logic_sft"),
        ):
            d = start.joinpath(*rel)
            if (d / "train.csv").is_file():
                return d.resolve()
    return None


def resolve_sft_processed_dir(cfg: LogicSFTConfig) -> Path:
    """Thư mục logic_sft đã export (train/dev/test.csv)."""
    if cfg.sft_processed_dir is not None:
        return Path(cfg.sft_processed_dir).resolve()
    env = os.environ.get("LOGIC_SFT_PROCESSED_DIR", "").strip()
    if env:
        return Path(env).expanduser().resolve()
    found = _discover_sft_processed_dir()
    if found is None:
        raise FileNotFoundError(
            "Không thấy data/processed/logic_sft/train.csv. "
            "Chạy src/visualization/exploration.ipynb (cell xuất logic_sft) hoặc `make data` / LOGIC_SFT_PROCESSED_DIR."
        )
    return found


def prepare_training_paths(cfg: LogicSFTConfig, processed_dir: Path) -> None:
    cfg.processed_dir = processed_dir.resolve()
    cfg.app_dir = processed_dir.parent.parent.parent
    nb_legacy = cfg.app_dir / "notebooks" / "Logic_Based_Educational_Queries"
    nb_project = cfg.app_dir / "notebooks"
    if nb_legacy.is_dir():
        cfg.notebook_root = nb_legacy
    elif nb_project.is_dir():
        cfg.notebook_root = nb_project
    else:
        cfg.notebook_root = Path.cwd()
    cfg.out_dir = cfg.notebook_root / "output" / "pipeline_sft"
    cfg.checkpoint_dir = cfg.out_dir / "final_lora"
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    cfg.processed_dir.mkdir(parents=True, exist_ok=True)


def _maybe_list(val) -> list:
    if isinstance(val, list):
        return val
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    s = str(val).strip()
    if not s:
        return []
    return ast.literal_eval(s)


def read_split_csv(processed_dir: Path, split: str) -> pd.DataFrame:
    p = processed_dir / f"{split}.csv"
    if not p.is_file():
        raise FileNotFoundError(f"Thiếu {p}. Chạy exploration.ipynb hoặc `make data`.")
    df = pd.read_csv(p)
    for col in ("premises_nl", "premises_fol"):
        if col in df.columns:
            df[col] = df[col].apply(_maybe_list)
    if "record_id" in df.columns:
        df["record_id"] = df["record_id"].astype(int)
    if "q_idx" in df.columns:
        df["q_idx"] = df["q_idx"].astype(int)
    return df


def load_split_frames(cfg: LogicSFTConfig) -> dict[str, pd.DataFrame]:
    proc = resolve_sft_processed_dir(cfg)
    prepare_training_paths(cfg, proc)
    return {name: read_split_csv(proc, name) for name in ("train", "dev", "test")}


def _numbered_lines(items: list[str], header: str) -> str:
    if not items:
        return ""
    return header + "\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(items, 1))


def build_user_content(row: dict, cfg: LogicSFTConfig) -> str:
    fol_used = premises_fol_for_training(
        row["premises_nl"], row["premises_fol"], backend=None
    )
    blocks = []
    if cfg.include_fol_in_user and fol_used:
        blocks.append(fol_block_from_lists(fol_used, PREMISES_FOL_HEADER))
    if row.get("premises_nl"):
        blocks.append(_numbered_lines(row["premises_nl"], PREMISES_NL_HEADER))
    return USER_TEMPLATE_SFT.format(
        premises_block="\n\n".join(blocks).strip(),
        question=row["question"],
    )


def build_assistant_content(row: dict) -> str:
    return ASSISTANT_TEMPLATE_SFT.format(
        answer=row["answer"], explanation=row["explanation"]
    )


def build_messages(row: dict, cfg: LogicSFTConfig) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT_SFT.strip()},
        {"role": "user", "content": build_user_content(row, cfg)},
        {"role": "assistant", "content": build_assistant_content(row)},
    ]


def to_hf_dataset(split_df: pd.DataFrame, cfg: LogicSFTConfig) -> Dataset:
    rows = []
    for row in split_df.to_dict(orient="records"):
        rows.append(
            {
                "record_id": row["record_id"],
                "q_idx": row["q_idx"],
                "gold_answer": row["answer"],
                "messages": build_messages(row, cfg),
            }
        )
    return Dataset.from_list(rows)


def attach_chat_text_and_eval_prompt(
    example: dict,
    tokenizer,
) -> dict:
    text = tokenizer.apply_chat_template(
        example["messages"],
        tokenize=False,
        add_generation_prompt=False,
    )
    prompt = tokenizer.apply_chat_template(
        example["messages"][:2],
        tokenize=False,
        add_generation_prompt=True,
    )
    return {
        "text": text,
        "eval_prompt": prompt,
        "gold_answer": example["gold_answer"],
    }


def build_dataset_dict(cfg: LogicSFTConfig, tokenizer) -> DatasetDict:
    splits_df = load_split_frames(cfg)
    raw_splits = {
        name: to_hf_dataset(splits_df[name], cfg) for name in ("train", "dev", "test")
    }

    def _map_split(ds: Dataset) -> Dataset:
        return ds.map(
            lambda ex: attach_chat_text_and_eval_prompt(ex, tokenizer),
            remove_columns=["messages"],
        )

    return DatasetDict({k: _map_split(v) for k, v in raw_splits.items()})
