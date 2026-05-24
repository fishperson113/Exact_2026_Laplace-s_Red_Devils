"""SFT NL→FOL: lọc len(premises_nl)==len(premises_fol), build HF messages."""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import pandas as pd
from datasets import Dataset, DatasetDict

from data.dataset import read_split_csv
from data.ingestion import discover_processed_splits_dir, project_root
from data.prompts import (
    SYSTEM_PROMPT_FOL_SFT,
    USER_TEMPLATE_FOL_SFT,
    format_nl_block_numbered,
)
from services.config_fol import FolSFTConfig

_LOG = logging.getLogger(__name__)


def _discover_fol_or_logic_processed_dir() -> Path | None:
    """Giống logic SFT: ưu tiên `data/processed/`, rồi legacy `fol_sft` / `logic_sft`."""
    return discover_processed_splits_dir()


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
        pr = project_root()
        cw = Path.cwd().resolve()
        raise FileNotFoundError(
            "Không thấy train.csv. Đã thử các đường dẫn tương đối "
            f"data/processed, …/logic_sft, …/fol_sft dưới gốc repo ({pr}) rồi dưới CWD ({cw}); "
            "xem discover_processed_splits_dir trong src/data/ingestion.py. "
            "Cách xử lý: đặt FOL_SFT_PROCESSED_DIR hoặc LOGIC_SFT_PROCESSED_DIR trỏ tuyệt đối tới thư mục chứa train.csv; "
            "hoặc chép train/dev/test.csv vào <gốc_repo>/data/processed/ (hoặc …/data/processed/logic_sft/). "
            "Nếu thông báo lỗi của bạn chỉ có câu «trong fol_sft/logic_sft» mà không có gốc repo/CWD như trên, "
            "kernel đang dùng bản fol_dataset.py cũ — đồng bộ lại cả thư mục src/ và khởi động lại kernel (Kaggle)."
        )
    return found


def prepare_fol_training_paths(cfg: FolSFTConfig, processed_dir: Path) -> None:
    cfg.processed_dir = processed_dir.resolve()
    cfg.app_dir = project_root()
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
    return USER_TEMPLATE_FOL_SFT.format(premises_nl=block).strip()


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
        "premises_nl": list(example["premises_nl"]),
        "premises_fol": list(example["premises_fol"]),
    }


def _to_hf_dataset(split_df: pd.DataFrame) -> Dataset:
    rows = []
    for row in split_df.to_dict(orient="records"):
        fol = list(row["premises_fol"])
        row_n = {**row, "premises_fol": fol}
        rows.append(
            {
                "record_id": int(row_n["record_id"]) if row_n.get("record_id") is not None else -1,
                "q_idx": int(row_n["q_idx"]) if row_n.get("q_idx") is not None else -1,
                "gold_assistant": build_fol_assistant_content(row_n),
                "messages": build_fol_messages(row_n),
                "premises_nl": list(row_n["premises_nl"]),
                "premises_fol": fol,
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
        _LOG.info("FOL %s: kept %d dropped %d", name, len(filt), n_drop)

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
    """Lọc CSV nguồn → ghi thư mục đích; trả về số dòng loại mỗi split."""
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
