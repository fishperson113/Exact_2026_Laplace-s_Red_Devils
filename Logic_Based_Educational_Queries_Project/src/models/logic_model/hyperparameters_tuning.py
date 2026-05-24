"""Tinh chỉnh siêu tham số / sweep — mở rộng (Optuna, W&B sweep, v.v.).

Hiện tại siêu tham số chính nằm trong `configs/logic_model.yaml` (tham khảo) và biến môi trường
`LOGIC_*` trong `.env` (được `LogicSFTConfig.from_env()` đọc).
"""
from __future__ import annotations

from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


def load_yaml_config(path: Path) -> dict:
    if yaml is None:
        raise ImportError("Cài PyYAML để đọc configs: pip install pyyaml")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def suggest_from_config(config_path: Path | None = None) -> dict:
    """Đọc `configs/logic_model.yaml` nếu có — trả về dict gợi ý (không ghi đè .env tự động)."""
    root = Path(__file__).resolve().parent.parent.parent.parent
    p = config_path or (root / "configs" / "logic_model.yaml")
    if not p.is_file():
        return {}
    return load_yaml_config(p)
