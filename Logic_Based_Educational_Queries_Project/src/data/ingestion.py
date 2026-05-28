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


def _discovery_anchor_dirs() -> list[Path]:
    """Thư mục neo để tìm `data/processed/...`: gốc repo trước (ổn định trên Kaggle khi CWD ≠ repo), rồi CWD."""
    anchors: list[Path] = []
    seen: set[str] = set()

    def _add(p: Path) -> None:
        try:
            r = p.resolve()
        except OSError:
            return
        k = str(r)
        if k in seen:
            return
        seen.add(k)
        anchors.append(r)

    _add(project_root())
    _add(Path.cwd().resolve())
    for p in Path.cwd().resolve().parents:
        _add(p)
    return anchors


def discover_processed_splits_dir() -> Path | None:
    """Tìm thư mục có `train.csv` (chung logic + FOL): ưu tiên `data/processed/`, rồi legacy `fol_sft`/`logic_sft`."""
    rels = (
        ("data", "processed"),
        ("app", "data", "processed"),
        ("data", "processed", "fol_sft"),
        ("app", "data", "processed", "fol_sft"),
        ("data", "processed", "logic_sft"),
        ("app", "data", "processed", "logic_sft"),
    )
    seen_dirs: set[str] = set()
    for start in _discovery_anchor_dirs():
        for rel in rels:
            d = start.joinpath(*rel)
            try:
                key = str(d.resolve())
            except OSError:
                continue
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            if (d / "train.csv").is_file():
                return d.resolve()
    return None


def export_from_records(
    records: list[dict],
    out_dir: Path,
    *,
    split_ratios: tuple[float, float, float] = (0.8, 0.1, 0.1),
    split_seed: int = 42,
    expected_questions: int | None = None,
    stratify: bool = True,
) -> None:
    """Flatten list record → chuẩn 7 nhãn → split theo record_id → `out_dir/*.csv` + metadata JSON.

    Dùng list đã tiền xử lý trong memory (vd. notebook đã ghi `premises-FOL` chuẩn hóa vào `records_norm`).

    Parameters
    ----------
    stratify : bool
        Nếu True, split stratified theo loại câu hỏi chủ đạo của mỗi record
        (mcq / yesno / unknown) để đảm bảo phân phối nhãn đồng đều.
    expected_questions : int | None
        Nếu None thì bỏ qua kiểm tra; nếu int thì raise nếu lệch.
    """
    import re

    import pandas as pd
    from sklearn.model_selection import train_test_split

    from evaluation.metrics import require_answer_label

    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    MCQ_RE = re.compile(r"\nA[\.\)]")

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
    actual_q = sum(len(r["questions"]) for r in records)
    if expected_questions is not None:
        if len(df_q) != actual_q or actual_q != expected_questions:
            raise ValueError(
                f"Flatten lệch hoặc không đúng {expected_questions} câu: "
                f"len_df={len(df_q)}, actual={actual_q}"
            )

    # --- Stratify key per record ---
    strat_labels = None
    if stratify:
        strat_labels = []
        for rec in records:
            answers = [str(a).strip() for a in rec.get("answers", [])]
            questions = rec.get("questions", [])
            has_mcq = any(MCQ_RE.search(q) for q in questions)
            has_unknown = any(a == "Unknown" for a in answers)
            if has_mcq:
                strat_labels.append("mcq_unknown" if has_unknown else "mcq_known")
            else:
                strat_labels.append("non_mcq_unknown" if has_unknown else "non_mcq_known")

    train_r, dev_r, test_r = split_ratios
    ids = list(range(len(records)))
    dev_test = dev_r + test_r

    try:
        train_ids, temp, train_lab, temp_lab = train_test_split(
            ids, strat_labels, test_size=dev_test,
            random_state=split_seed, stratify=strat_labels,
        ) if strat_labels else (
            *train_test_split(ids, test_size=dev_test, random_state=split_seed),
            None, None,
        )
        if temp_lab is not None:
            dev_ids, test_ids = train_test_split(
                temp, test_size=test_r / dev_test,
                random_state=split_seed, stratify=temp_lab,
            )
        else:
            dev_ids, test_ids = train_test_split(
                temp, test_size=test_r / dev_test, random_state=split_seed,
            )
    except ValueError:
        # Fallback: nếu class quá ít để stratify
        print("[export] Stratify failed (class quá ít), fallback random split")
        train_ids, temp = train_test_split(ids, test_size=dev_test, random_state=split_seed)
        dev_ids, test_ids = train_test_split(
            temp, test_size=test_r / dev_test, random_state=split_seed,
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
    """CLI / Makefile: raw mặc định → `data/processed/` (chung cho logic + FOL)."""
    export_from_json_path(raw_json_path(), project_root() / "data" / "processed")
