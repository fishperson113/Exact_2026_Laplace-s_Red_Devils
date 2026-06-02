from __future__ import annotations

import re


def sanitize_repo_segment(s: str) -> str:
    """Chỉ chữ thường, số, gạch ngang — dùng cho version / method / slug."""
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9.\-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "x"


def default_model_slug_from_hf_id(model_id: str) -> str:
    """
    Từ id HF tạo slug ngắn cho tên repo, ví dụ:
    Qwen/Qwen3.5-4B -> qwen3.5-4
    Qwen/Qwen3-4B-Instruct-2507 -> qwen3-4-instruct-2507
    """
    tail = model_id.split("/")[-1].lower()
    # Giữ dấu chấm trong tên (vd. 3.5) — chỉ bỏ hậu tố instruct/chat
    tail = re.sub(r"-(instruct|chat)(-[\w]+)?$", "", tail)
    # 4b / 0.5b ở cuối -> bỏ chữ b (theo convention user: qwen3.5-4)
    tail = re.sub(r"(\d)b$", r"\1", tail)
    return sanitize_repo_segment(tail)


def build_fol_hf_repo_id(
    org: str,
    version: str,
    variant: str,
    model_id: str,
    method: str | None = None,
    model_slug_override: str | None = None,
) -> str:
    """Repo FOL: {org}/fol-{version}[-{method}]-{origin|augmented}-{slug}."""
    o = org.strip().strip("/")
    ver = sanitize_repo_segment(version)
    var_raw = variant.strip().lower()
    if var_raw in ("aug", "augment", "augmented"):
        var = "augmented"
    elif var_raw in ("orig", "origin", "original"):
        var = "origin"
    else:
        var = sanitize_repo_segment(var_raw) or "origin"
    slug = sanitize_repo_segment(model_slug_override or default_model_slug_from_hf_id(model_id))
    if method:
        meth = sanitize_repo_segment(method)
        return f"{o}/fol-{ver}-{meth}-{var}-{slug}"
    return f"{o}/fol-{ver}-{var}-{slug}"


def build_hf_repo_id(
    org: str,
    version: str,
    method: str,
    model_id: str,
    model_slug_override: str | None = None,
) -> str:
    # Giữ nguyên casing org (vd. Laplaces-Red-Devils)
    o = org.strip().strip("/")
    ver = sanitize_repo_segment(version)
    meth = sanitize_repo_segment(method)
    slug = sanitize_repo_segment(model_slug_override or default_model_slug_from_hf_id(model_id))
    return f"{o}/logic-{ver}-{meth}-{slug}"
