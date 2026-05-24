"""Flatten JSON → chuẩn 7 nhãn → split train/dev/test → ghi CSV + metadata vào `data/processed/logic_sft/`."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from evaluation.metrics import require_answer_label

from .ingestion import project_root


def get_fol(rec: dict) -> list[str]:
    return rec.get("premises-FOL", [])


def normalize_idx(idx: list, n_questions: int) -> list[list]:
    if not idx:
        return [[] for _ in range(n_questions)]
    if all(isinstance(x, int) for x in idx):
        return [list(idx)] if n_questions == 1 else [list(idx)] * n_questions
    return idx


def flatten_records(recs: list[dict]) -> pd.DataFrame:
    rows = []
    for rid, rec in enumerate(recs):
        fol_list = get_fol(rec)
        idx_lists = normalize_idx(rec["idx"], len(rec["questions"]))
        for qi, (q, a, exp, idx_used) in enumerate(
            zip(rec["questions"], rec["answers"], rec["explanation"], idx_lists)
        ):
            rows.append(
                {
                    "record_id": rid,
                    "q_idx": qi,
                    "n_premises_used": len(idx_used),
                    "question": q,
                    "answer": require_answer_label(str(a)),
                    "explanation": exp,
                    "premises_nl": list(rec["premises-NL"]),
                    "premises_fol": list(fol_list),
                }
            )
    return pd.DataFrame(rows)


def split_record_ids(
    n_records: int, ratios: tuple[float, float, float], seed: int
) -> tuple[list[int], list[int], list[int]]:
    train_r, dev_r, test_r = ratios
    ids = list(range(n_records))
    dev_test = dev_r + test_r
    train_ids, temp = train_test_split(ids, test_size=dev_test, random_state=seed)
    dev_ids, test_ids = train_test_split(
        temp, test_size=test_r / dev_test, random_state=seed
    )
    return sorted(train_ids), sorted(dev_ids), sorted(test_ids)


def export_from_json_path(
    json_path: Path,
    out_dir: Path,
    *,
    split_ratios: tuple[float, float, float] = (0.8, 0.1, 0.1),
    split_seed: int = 42,
    expected_questions: int = 808,
) -> None:
    """Ghi `train.csv`, `dev.csv`, `test.csv`, `split_record_ids.json`, `split_summary.json`."""
    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    records = json.loads(json_path.read_text(encoding="utf-8"))
    df_q = flatten_records(records)
    expected = sum(len(r["questions"]) for r in records)
    if len(df_q) != expected or expected != expected_questions:
        raise ValueError(
            f"Flatten lệch hoặc không đúng {expected_questions} câu: len_df={len(df_q)}, expected={expected}"
        )

    train_ids, dev_ids, test_ids = split_record_ids(
        len(records), split_ratios, split_seed
    )
    meta = {"train": train_ids, "dev": dev_ids, "test": test_ids}

    def _subset(name: str) -> pd.DataFrame:
        return df_q[df_q["record_id"].isin(meta[name])].reset_index(drop=True)

    splits = {k: _subset(k) for k in meta}
    for name, sdf in splits.items():
        sdf.to_csv(out_dir / f"{name}.csv", index=False)

    (out_dir / "split_record_ids.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )

    summary = {
        name: {
            "n_records": int(sdf["record_id"].nunique()),
            "n_questions": len(sdf),
        }
        for name, sdf in splits.items()
    }
    (out_dir / "split_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )


def export_logic_sft(
    json_path: Path | None = None,
    out_dir: Path | None = None,
    **kwargs,
) -> None:
    """Đọc JSON raw → flatten + nhãn chuẩn → split theo record_id → ghi CSV + JSON metadata."""
    root = project_root()
    json_path = json_path or (root / "data" / "raw" / "Logic_Based_Educational_Queries.json")
    out_dir = out_dir or (root / "data" / "processed" / "logic_sft")
    export_from_json_path(json_path, out_dir, **kwargs)


def main() -> None:
    export_logic_sft()
    print("OK:", project_root() / "data" / "processed" / "logic_sft")


if __name__ == "__main__":
    main()
