from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

from services.config import LogicSFTConfig


def _ensure_gdown() -> None:
    try:
        import gdown  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "gdown"])


def download_and_extract_from_drive(cfg: LogicSFTConfig) -> Path:
    """Tải zip Drive, giải nén, copy JSON về DATA_ROOT/app/data/raw/."""
    target = (cfg.data_root / "app" / "data" / "raw" / cfg.data_filename).resolve()
    if target.is_file():
        return target

    cache = (cfg.data_root / "_cache").resolve()
    cache.mkdir(parents=True, exist_ok=True)
    zip_path = cache / cfg.gdrive_zip_name

    _ensure_gdown()
    import gdown

    if not zip_path.is_file():
        gdown.download(
            f"https://drive.google.com/uc?id={cfg.gdrive_file_id}",
            str(zip_path),
            quiet=False,
        )

    extract_dir = cache / "extracted"
    marker = extract_dir / ".extracted"
    if not marker.exists():
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(extract_dir)
        marker.write_text("ok", encoding="utf-8")

    matches = sorted(extract_dir.rglob(cfg.data_filename))
    if not matches:
        matches = sorted(
            p
            for p in extract_dir.rglob("*.json")
            if "Logic" in p.name and "Educational" in p.name
        )
    if not matches:
        sample = [str(p.relative_to(extract_dir)) for p in extract_dir.rglob("*.json")][:15]
        raise FileNotFoundError(
            f"Không thấy {cfg.data_filename} trong zip.\nMột số .json: {sample}"
        )

    src = matches[0]
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, target)
    return target
