import json
import os
import re
from html.parser import HTMLParser
import sys

# Đảm bảo output hỗ trợ UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class StripHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return ' '.join(t.strip() for t in self.text if t.strip())

def strip_html(html):
    if not html: return ""
    p = StripHTML()
    p.feed(html)
    return p.get_text()

def is_high_quality(content, reason):
    # Loại bỏ các câu hỏi dạng phân tích đúng/sai (nhận biết lý thuyết đơn thuần)
    exclude_patterns = [
        "phát biểu nào sau đây là sai",
        "phát biểu nào sau đây là đúng",
        "chọn câu sai",
        "chọn câu đúng",
        "tìm phát biểu sai",
        "chọn phát biểu đúng",
        "hệ thức nào sau đây là đúng",
        "biểu thức nào sau đây là sai",
        "chọn câu phát biểu sai",
        "chọn câu phát biểu đúng",
        "chọn phương án đúng",
        "chọn phương án sai",
        "hình vẽ",
        "hình bên",
        "hình dưới",
        "đồ thị",
        "như hình",
        "bảng bên",
        "cho bảng",
        "sơ đồ"
    ]

    content_lower = content.lower()
    reason_lower = reason.lower()

    for pattern in exclude_patterns:
        if pattern in content_lower or pattern in reason_lower:
            return False

    # Tiêu chí: Lời giải dài và có các từ khóa logic
    if len(reason) < 200:
        return False

    # Kiểm tra xem lời giải có mang tính tính toán không (phải có số hoặc ký hiệu so sánh)
    # Tìm sự hiện diện của các con số
    has_numbers = bool(re.search(r'\d+', reason))
    # Tìm sự hiện diện của các phép toán/so sánh
    has_math = bool(re.search(r'[=><+*/-]', reason))

    if not (has_numbers and has_math):
        return False

    # Các từ khóa thường thấy trong bài giải chi tiết
    keywords = [
        "Ta có", "áp dụng", "công thức", "thay số", "suy ra",
        "chiếu lên", "hệ tọa độ", "đổi đơn vị", "bước", "theo đề",
        "tương đương", "giả sử", "định luật"
    ]

    match_count = sum(1 for kw in keywords if kw.lower() in reason_lower)

    # Cần ít nhất 2 từ khóa logic hoặc lời giải rất dài (>500)
    # Và phải có tính toán cụ thể
    return match_count >= 2 or len(reason) > 500

def clean_solution(text):
    # Loại bỏ các dấu vết của trắc nghiệm triệt để hơn
    patterns = [
        r"Đáp án [A-D]",
        r"Đáp án: [A-D]",
        r"Chọn [A-D]",
        r"Đáp án chính xác",
        r"Đáp án cần chọn là:? [A-D]?",
        r"Câu [A-D] đúng",
        r"ần chọn là:? [A-D]?",
        r"Hướng dẫn giải",
        r"Giải chi tiết:?",
        r"\+ \s*Đáp án[:\s]*[A-D]",
    ]

    cleaned = text
    for p in patterns:
        cleaned = re.sub(p, "", cleaned, flags=re.IGNORECASE)

    # Loại bỏ các đoạn thừa ở cuối nếu nó chỉ là nhắc lại đáp án
    cleaned = re.sub(r"\s*Chọn\s*$", "", cleaned, flags=re.IGNORECASE)

    return cleaned.strip()

def format_to_md(record):
    content = strip_html(record.get('question_content', ''))
    reason = strip_html(record.get('question_reason', ''))

    # Làm sạch lời giải khỏi MCQ noise
    solution = clean_solution(reason)

    # Tạo tiêu đề thông minh hơn
    title = content.split('.')[0] if '.' in content else content
    if len(title) > 120:
        title = title[:117] + "..."
    elif len(title) < 10 and len(content) > 10:
        title = content[:117] + "..."

    title = title.strip()

    md = f"## Problem: {title}\n\n"
    md += f"**Question:**\n{content}\n\n"
    md += "### Solution\n\n"
    md += f"{solution}\n\n"
    md += "---\n\n"
    return md

def process_files():
    input_dir = 'data/vietjack_physics_spider/'
    output_dir = 'data/pretrain_processed/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = ['lop-6.jsonl', 'lop-7.jsonl', 'lop-8.jsonl', 'lop-9.jsonl', 'lop-10.jsonl', 'lop-11.jsonl', 'lop-12.jsonl']

    for filename in files:
        input_path = os.path.join(input_dir, filename)
        if not os.path.exists(input_path):
            print(f"Skipping {filename}: Not found")
            continue

        output_path = os.path.join(output_dir, filename.replace('.jsonl', '_high_quality.md'))
        count = 0
        total = 0

        print(f"Processing {filename}...")

        with open(input_path, 'r', encoding='utf-8') as f_in, \
             open(output_path, 'w', encoding='utf-8') as f_out:

            f_out.write(f"# Processed Data from {filename}\n\n")

            for line in f_in:
                total += 1
                try:
                    record = json.loads(line)
                    content = strip_html(record.get('question_content', ''))
                    reason = strip_html(record.get('question_reason', ''))

                    if is_high_quality(content, reason):
                        f_out.write(format_to_md(record))
                        count += 1
                except Exception as e:
                    continue

        print(f"Finished {filename}: Saved {count}/{total} high-quality records to {output_path}")

if __name__ == "__main__":
    process_files()
