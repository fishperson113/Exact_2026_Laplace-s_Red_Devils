"""Tiền xử lý nội dung chat (user/assistant blocks) trước khi tokenize."""
from __future__ import annotations

from data.dataset import (
    build_assistant_content,
    build_messages,
    build_user_content,
)

__all__ = ["build_messages", "build_user_content", "build_assistant_content"]
