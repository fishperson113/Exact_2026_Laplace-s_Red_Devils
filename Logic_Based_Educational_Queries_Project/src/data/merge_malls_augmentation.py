"""
Gộp / chuẩn hoá dữ liệu MALLS-v0 → CSV `logic_sft`-compatible (premises_nl, premises_fol, ...).

Chạy sau khi tải snapshot vào `data/external/MALLS-v0` (xem `data/external/README.md`).

    PYTHONPATH=src python -m data.merge_malls_augmentation \\
        --malls-root data/external/MALLS-v0 \\
        --out-dir data/processed/fol_sft_augmented
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

import pandas as pd

from data.fol_dataset import export_filtered_fol_csvs


def _maybe_parse_list(val) -> list | None:
    if isinstance(val, list):
        return val
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return None
    s = str(val).strip()
    if not s:
        return None
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        return None


def _find_nl_fol_columns(df: pd.DataFrame) -> tuple[str | None, str | None]:
    cols_lower = {c.lower(): c for c in df.columns}
    nl_c = cols_lower.get("premises_nl")
    fol_c = cols_lower.get("premises_fol")
    if nl_c and fol_c:
        return nl_c, fol_c
    nl_c = None
    fol_c = None
    for key, orig in cols_lower.items():
        if "premise" in key and "nl" in key:
            nl_c = orig
        if "premise" in key and "fol" in key:
            fol_c = orig
    return nl_c, fol_c


def _row_hash(row: dict) -> str:
    key = json.dumps(row, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:24]


def malls_split_to_frame(split_df: pd.DataFrame) -> pd.DataFrame:
    nl_c, fol_c = _find_nl_fol_columns(split_df)
    if nl_c is None or fol_c is None:
        raise ValueError(
            f"Không tìm thấy cột premises NL/FOL trong DataFrame. Cột có: {list(split_df.columns)}"
        )
    rows_out = []
    seen: set[str] = set()
    for idx, row in split_df.iterrows():
        nl = _maybe_parse_list(row.get(nl_c))
        fo = _maybe_parse_list(row.get(fol_c))
        if nl is None or fo is None:
            continue
        if "record_id" in split_df.columns and pd.notna(row.get("record_id")):
            rid = int(row["record_id"])
        elif isinstance(idx, int):
            rid = int(idx)
        else:
            rid = abs(hash(str(idx))) % (10**9)
        base = {
            "record_id": rid,
            "q_idx": 0,
            "premises_nl": nl,
            "premises_fol": fo,
            "question": str(row.get("question", row.get("query", "")) or ""),
            "answer": str(row.get("answer", row.get("label", "Unknown")) or "Unknown"),
            "explanation": str(row.get("explanation", row.get("rationale", "")) or ""),
        }
        h = _row_hash(base)
        if h in seen:
            continue
        seen.add(h)
        rows_out.append(base)
    return pd.DataFrame(rows_out)


def load_malls_as_dict(malls_root: Path) -> dict[str, pd.DataFrame]:
    """Thử `datasets` hoặc đọc file trong thư mục tải tay."""
    try:
        from datasets import load_dataset

        ds = load_dataset(str(malls_root))
        out = {}
        for k in ds.keys():
            out[str(k)] = ds[k].to_pandas()
        if out:
            return out
    except Exception:
        pass

    parquet_files = sorted(malls_root.rglob("*.parquet"))
    if parquet_files:
        df = pd.read_parquet(parquet_files[0])
        return {"train": df}

    csv_files = sorted(malls_root.rglob("*.csv"))
    if csv_files:
        df = pd.read_csv(csv_files[0])
        return {"train": df}

    raise FileNotFoundError(
        f"Không đọc được MALLS từ {malls_root}. Cài `datasets` hoặc đặt file parquet/csv trong thư mục."
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Merge MALLS-v0 → fol_sft_augmented CSV")
    ap.add_argument("--malls-root", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()
    root = args.malls_root.resolve()
    out = args.out_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    raw = load_malls_as_dict(root)
    parts: list[pd.DataFrame] = []
    for _k, v in raw.items():
        parts.append(malls_split_to_frame(v))
    full = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    if full.empty:
        raise ValueError("Không có hàng hợp lệ sau khi map MALLS → premises_nl / premises_fol.")

    n = len(full)
    if n < 3:
        train = dev = test = full
    else:
        i1 = max(1, int(0.8 * n))
        i2 = max(i1 + 1, min(n - 1, int(0.9 * n)))
        train, dev, test = full.iloc[:i1], full.iloc[i1:i2], full.iloc[i2:]

    interim = out.parent / "_malls_interim"
    interim.mkdir(parents=True, exist_ok=True)
    train.to_csv(interim / "train.csv", index=False)
    dev.to_csv(interim / "dev.csv", index=False)
    test.to_csv(interim / "test.csv", index=False)
    stats = export_filtered_fol_csvs(interim, out)
    print("Exported filtered FOL splits to", out, "drop stats:", stats)


if __name__ == "__main__":
    main()
