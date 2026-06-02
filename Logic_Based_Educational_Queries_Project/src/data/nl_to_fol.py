from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from data.prompts import (
    SYSTEM_PROMPT_NL_TO_FOL,
    USER_TEMPLATE_NL_TO_FOL,
    format_nl_block_numbered,
)


class FolBackend(Protocol):
    """Giao diện tùy chọn: gọi API / local LLM để sinh FOL."""

    def infer_fol(self, premises_nl: list[str]) -> str: ...


@dataclass
class GoldFolBackend:
    """Dùng FOL có sẵn trong dataset (mặc định khi SFT)."""

    premises_fol: list[str]

    def infer_fol(self, premises_nl: list[str]) -> str:  # noqa: ARG002
        if not self.premises_fol:
            return ""
        return "\n".join(f"{i}. {f}" for i, f in enumerate(self.premises_fol, 1))


def build_nl_to_fol_messages(premises_nl: list[str]) -> list[dict[str, str]]:
    """Tin nhắn chat cho bước NL→FOL (huấn luyện / inference tách bước)."""
    nl_block = format_nl_block_numbered(premises_nl)
    return [
        {"role": "system", "content": SYSTEM_PROMPT_NL_TO_FOL.strip()},
        {"role": "user", "content": USER_TEMPLATE_NL_TO_FOL.format(nl_block=nl_block)},
    ]


def premises_fol_for_training(
    premises_nl: list[str],
    premises_fol: list[str],
    backend: FolBackend | None = None,
) -> list[str]:
    """
    Trả về list chuỗi FOL dùng trong user message SFT.
    Mặc định: gold `premises_fol`. Nếu truyền `backend`, dùng output backend (parse thành list nếu cần).
    """
    if backend is not None:
        raw = backend.infer_fol(premises_nl)
        lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
        out: list[str] = []
        for ln in lines:
            if len(ln) > 2 and ln[0].isdigit() and ln[1] in ".)":
                out.append(ln.split(".", 1)[-1].strip())
            else:
                out.append(ln)
        return out if out else list(premises_fol)
    return list(premises_fol)


def fol_block_from_lists(premises_fol: list[str], header: str) -> str:
    if not premises_fol:
        return ""
    return header + "\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(premises_fol, 1))
