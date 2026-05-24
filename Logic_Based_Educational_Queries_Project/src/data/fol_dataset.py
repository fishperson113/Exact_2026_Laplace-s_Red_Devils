"""Dataset SFT: premises NL → premises FOL (JSON), lọc mẫu lệch độ dài."""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import pandas as pd
from datasets import Dataset, DatasetDict

from data.dataset import read_split_csv
from data.prompts import SYSTEM_PROMPT_FOL_SFT, format_nl_block_numbered
from services.config_fol import FolSFTConfig

_LOG = logging.getLogger(__name__)


def _discover_fol_or_logic_processed_dir() -> Path | None:
    seen: set[str] = set()
    for start in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
        key = str(start)
        if key in seen:
            continue
        seen.add(key)
        for rel in (
            ("app", "data", "processed", "fol_sft"),
            ("data", "processed", "fol_sft"),
            ("app", "data", "processed", "logic_sft"),
            ("data", "processed", "logic_sft"),
        ):
            d = start.joinpath(*rel)
            if (d / "train.csv").is_file():
                return d.resolve()
    return None


def resolve_fol_processed_dir(cfg: FolSFTConfig) -> Path:
    if cfg.sft_processed_dir is not None:
        return Path(cfg.sft_processed_dir).resolve()
    env = os.environ.get("FOL_SFT_PROCESSED_DIR", "").strip()
    if env:
        return Path(env).expanduser().resolve()
    env2 = os.environ.get("LOGIC_SFT_PROCESSED_DIR", "").strip()
    if env2:
        return Path(env2).expanduser().resolve()
    found = _discover_fol_or_logic_processed_dir()
    if found is None:
        raise FileNotFoundError(
            "Không thấy train.csv trong fol_sft hoặc logic_sft. "
            "Đặt FOL_SFT_PROCESSED_DIR / LOGIC_SFT_PROCESSED_DIR hoặc chạy export fol_sft."
        )
    return found


def prepare_fol_training_paths(cfg: FolSFTConfig, processed_dir: Path) -> None:
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
    cfg.out_dir = cfg.notebook_root / "output" / "pipeline_fol_sft"
    cfg.checkpoint_dir = cfg.out_dir / "final_lora"
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    cfg.processed_dir.mkdir(parents=True, exist_ok=True)


def filter_rows_parallel_premises(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Giữ hàng có len(premises_nl) == len(premises_fol) > 0."""
    if "premises_nl" not in df.columns or "premises_fol" not in df.columns:
        raise ValueError("Thiếu cột premises_nl / premises_fol")

    def ok(row) -> bool:
        nl = row["premises_nl"]
        fo = row["premises_fol"]
        if not isinstance(nl, list) or not isinstance(fo, list):
            return False
        if len(nl) != len(fo):
            return False
        return len(nl) > 0

    mask = df.apply(ok, axis=1)
    n_drop = int((~mask).sum())
    return df.loc[mask].reset_index(drop=True), n_drop


def build_fol_assistant_content(row: dict) -> str:
    fol = row["premises_fol"]
    return json.dumps({"premises_fol": list(fol)}, ensure_ascii=False)


def build_fol_user_content(row: dict) -> str:
    nl = row["premises_nl"]
    block = format_nl_block_numbered(list(nl))
    return (
        "Natural language premises (numbered):\n"
        f"{block}\n\n"
        "Task: output JSON only: {\"premises_fol\": [ ... ]} with one FOL string per line above, same order."
    )


def build_fol_messages(row: dict) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT_FOL_SFT.strip()},
        {"role": "user", "content": build_fol_user_content(row)},
        {"role": "assistant", "content": build_fol_assistant_content(row)},
    ]


def attach_fol_chat_text_and_eval_prompt(example: dict, tokenizer) -> dict:
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
        "gold_assistant": example["gold_assistant"],
    }


def _to_hf_dataset(split_df: pd.DataFrame) -> Dataset:
    rows = []
    for row in split_df.to_dict(orient="records"):
        rows.append(
            {
                "record_id": int(row["record_id"]) if row.get("record_id") is not None else -1,
                "q_idx": int(row["q_idx"]) if row.get("q_idx") is not None else -1,
                "gold_assistant": build_fol_assistant_content(row),
                "messages": build_fol_messages(row),
            }
        )
    return Dataset.from_list(rows)


def build_fol_dataset_dict(cfg: FolSFTConfig, tokenizer) -> tuple[DatasetDict, dict[str, int]]:
    proc = resolve_fol_processed_dir(cfg)
    prepare_fol_training_paths(cfg, proc)
    splits: dict[str, pd.DataFrame] = {}
    dropped: dict[str, int] = {}
    for name in ("train", "dev", "test"):
        raw_df = read_split_csv(proc, name)
        filt, n_drop = filter_rows_parallel_premises(raw_df)
        dropped[name] = n_drop
        splits[name] = filt
        _LOG.info(
            "FOL split %s: kept %d rows, dropped %d (len NL != len FOL or empty)",
            name,
            len(filt),
            n_drop,
        )

    raw_splits = {name: _to_hf_dataset(splits[name]) for name in ("train", "dev", "test")}

    def _map_split(ds: Dataset) -> Dataset:
        return ds.map(
            lambda ex: attach_fol_chat_text_and_eval_prompt(ex, tokenizer),
            remove_columns=["messages"],
        )

    ds_out = DatasetDict({k: _map_split(v) for k, v in raw_splits.items()})
    return ds_out, dropped


def export_filtered_fol_csvs(
    src_processed_dir: str | Path,
    dst_processed_dir: str | Path,
    *,
    splits: tuple[str, ...] = ("train", "dev", "test"),
) -> dict[str, int]:
    """
    Đọc logic_sft (hoặc bất kỳ thư mục có cùng schema CSV), lọc độ dài, ghi ra fol_sft.
    Trả về số dòng bị loại theo từng split.
    """
    src = Path(src_processed_dir).resolve()
    dst = Path(dst_processed_dir).resolve()
    dst.mkdir(parents=True, exist_ok=True)
    dropped_out: dict[str, int] = {}
    for sp in splits:
        df = read_split_csv(src, sp)
        filt, n_drop = filter_rows_parallel_premises(df)
        dropped_out[sp] = n_drop
        out_p = dst / f"{sp}.csv"
        filt.to_csv(out_p, index=False)
        _LOG.info("Exported %s -> %s (dropped %d)", sp, out_p, n_drop)
    return dropped_out
