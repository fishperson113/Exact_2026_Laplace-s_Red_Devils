"""Thu thập và định vị dữ liệu raw (immutable trong `data/raw/`)."""
from __future__ import annotations

import json
import shutil
from pathlib import Path


def project_root() -> Path:
    """Thư mục gốc dự án (chứa `data/`, `src/`, `configs/`)."""
    return Path(__file__).resolve().parent.parent.parent


def raw_json_path() -> Path:
    return project_root() / "data" / "raw" / "Logic_Based_Educational_Queries.json"


def load_raw_records(path: Path | None = None) -> list[dict]:
    path = path or raw_json_path()
    if not path.is_file():
        raise FileNotFoundError(
            f"Thiếu raw JSON: {path}. Sao chép từ repo EXACT vào data/raw/ hoặc chỉnh LOGIC_DATA_ROOT."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def stage_raw_copy(src: Path, dst: Path | None = None) -> Path:
    """Sao chép một file JSON nguồn vào `data/raw/` (metadata / backup tại đây)."""
    dst = dst or raw_json_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return dst


def export_from_records(
    records: list[dict],
    out_dir: Path,
    *,
    split_ratios: tuple[float, float, float] = (0.8, 0.1, 0.1),
    split_seed: int = 42,
    expected_questions: int = 808,
) -> None:
    """Flatten list record → chuẩn 7 nhãn → split theo record_id → `logic_sft/*.csv` + metadata JSON.

    Dùng list đã tiền xử lý trong memory (vd. notebook đã ghi `premises-FOL` chuẩn hóa vào `records_norm`).
    """
    import pandas as pd
    from sklearn.model_selection import train_test_split

    from evaluation.metrics import require_answer_label

    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    def _fol(rec: dict) -> list[str]:
        return list(rec.get("premises-FOL", []))

    def _norm_idx(idx: list, nq: int) -> list[list]:
        if not idx:
            return [[] for _ in range(nq)]
        if all(isinstance(x, int) for x in idx):
            return [list(idx)] if nq == 1 else [list(idx)] * nq
        return idx

    rows = []
    for rid, rec in enumerate(records):
        fol = _fol(rec)
        idx_lists = _norm_idx(rec["idx"], len(rec["questions"]))
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
                    "premises_fol": fol,
                }
            )
    df_q = pd.DataFrame(rows)
    expected = sum(len(r["questions"]) for r in records)
    if len(df_q) != expected or expected != expected_questions:
        raise ValueError(
            f"Flatten lệch hoặc không đúng {expected_questions} câu: len_df={len(df_q)}, expected={expected}"
        )

    train_r, dev_r, test_r = split_ratios
    ids = list(range(len(records)))
    dev_test = dev_r + test_r
    train_ids, temp = train_test_split(ids, test_size=dev_test, random_state=split_seed)
    dev_ids, test_ids = train_test_split(
        temp, test_size=test_r / dev_test, random_state=split_seed
    )
    meta = {"train": sorted(train_ids), "dev": sorted(dev_ids), "test": sorted(test_ids)}
    splits = {k: df_q[df_q["record_id"].isin(meta[k])].reset_index(drop=True) for k in meta}
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


def export_from_json_path(
    json_path: Path,
    out_dir: Path,
    *,
    split_ratios: tuple[float, float, float] = (0.8, 0.1, 0.1),
    split_seed: int = 42,
    expected_questions: int = 808,
) -> None:
    """Đọc JSON từ đĩa rồi gọi `export_from_records` (không qua bước chuẩn hóa FOL trong notebook)."""
    records = json.loads(Path(json_path).read_text(encoding="utf-8"))
    export_from_records(
        records,
        out_dir,
        split_ratios=split_ratios,
        split_seed=split_seed,
        expected_questions=expected_questions,
    )


def export_default_logic_sft() -> None:
    """CLI / Makefile: raw mặc định → `data/processed/logic_sft/`."""
    export_from_json_path(raw_json_path(), project_root() / "data" / "processed" / "logic_sft")
