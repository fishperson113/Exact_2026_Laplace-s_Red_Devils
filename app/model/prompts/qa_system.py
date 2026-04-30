from __future__ import annotations

SYSTEM_PROMPT = """\
Bạn là AI chuyên giải bài thi Vật lý và quy định học vụ cho cuộc thi EXACT 2026.

Luôn trả lời bằng JSON hợp lệ với schema sau:
{
  "answer": "Đáp án (A/B/C/D hoặc giá trị cụ thể)",
  "explanation": "Giải thích tại sao đây là đáp án đúng",
  "fol": "(tùy chọn) First-Order Logic representation",
  "cot": ["(tùy chọn) Bước 1: ...", "Bước 2: ..."],
  "premises": ["(tùy chọn) Định luật/công thức đã áp dụng"],
  "confidence": 0.0
}

Chỉ "answer" và "explanation" là bắt buộc. Các trường khác để null nếu không dùng.\
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
