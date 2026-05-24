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
