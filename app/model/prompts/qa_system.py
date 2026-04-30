from __future__ import annotations

SYSTEM_PROMPT = """\
Bạn là trợ lý AI, có thể trả lời mọi câu hỏi.

Luôn trả lời bằng JSON hợp lệ với schema sau:
{
  "answer": "Câu trả lời chính",
  "explanation": "Giải thích thêm nếu cần, để trống nếu không cần",
  "fol": null,
  "cot": null,
  "premises": null,
  "confidence": null
}

Chỉ "answer" là bắt buộc. Các trường khác để null.\
"""


def build_prompt(
    question: str,
    context: str = "",
    history: list[dict] | None = None,
) -> str:
    parts: list[str] = [SYSTEM_PROMPT, ""]

    if context:
        parts += [f"Tài liệu tham khảo:\n{context}", ""]

    if history:
        parts.append("Lịch sử hội thoại:")
        for turn in history:
            parts.append(f"Người dùng: {turn['q']}")
            parts.append(f"Trợ lý: {turn['a']}")
        parts.append("")

    parts.append(f"Câu hỏi: {question}")
    return "\n".join(parts)
