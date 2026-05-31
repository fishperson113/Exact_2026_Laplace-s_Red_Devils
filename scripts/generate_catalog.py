import json
import os
import re
import sys

# Đảm bảo output hỗ trợ UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def count_md_problems(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return len(re.findall(r'^## Problem:', content, flags=re.MULTILINE))

def count_jsonl_lines(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def generate_catalog():
    input_dir = 'data/vietjack_physics_spider/'
    processed_dir = 'data/pretrain_processed/'
    output_file = os.path.join(processed_dir, 'DATA_CATALOG.md')

    grades = ['6', '7', '8', '9', '10', '11', '12']
    stats = []

    total_raw = 0
    total_high = 0

    for grade in grades:
        raw_file = f'lop-{grade}.jsonl'
        proc_file = f'lop-{grade}_high_quality.md'

        raw_path = os.path.join(input_dir, raw_file)
        proc_path = os.path.join(processed_dir, proc_file)

        raw_count = count_jsonl_lines(raw_path)
        high_count = count_md_problems(proc_path)

        retention = (high_count / raw_count * 100) if raw_count > 0 else 0

        stats.append({
            'grade': f'Lớp {grade}',
            'raw': raw_count,
            'high': high_count,
            'retention': f'{retention:.2f}%'
        })

        total_raw += raw_count
        total_high += high_count

    catalog_content = f"""# Physics Pre-training Data Catalog

## 1. MetaData (Siêu dữ liệu)
- **Tên Data Asset**: Exact Physics High-Quality Pretrain Corpus
- **Định dạng dữ liệu**: Unstructured (Markdown Text)
- **Kích thước dự kiến**: ~{total_high} samples (sau khi lọc từ {total_raw} raw samples)
- **Nguồn gốc (Lineage)**: Thu thập từ hệ thống Vietjack (Chuyên mục bài tập Vật lý tự luận/trắc nghiệm có lời giải)
- **Phiên bản**: v1.0
- **Ngày cập nhật cuối**: 2026-05-30
- **Ngôn ngữ**: Tiếng Việt (Giải nghĩa) & Toán học (Công thức)

## 2. Thống kê & Mức độ tin cậy (Data Quality Assessment)
Bộ dữ liệu đã trải qua bước đánh giá và lọc (Quality Control) gắt gao. Dưới đây là tỷ lệ giữ lại sau khi loại bỏ dữ liệu rác:

| Grade (Khối) | Dữ liệu sạch (High-Quality) | Dữ liệu thô (Raw) | Tỷ lệ giữ lại (Retention) |
| :--- | :---: | :---: | :---: |
"""
    for s in stats:
        catalog_content += f"| {s['grade']} | {s['high']} | {s['raw']} | {s['retention']} |\n"

    catalog_content += f"| **Tổng cộng** | **{total_high}** | **{total_raw}** | **{(total_high/total_raw*100):.2f}%** |\n\n"

    catalog_content += """## 3. Data Lineage & Pipeline (Nguồn gốc & Quá trình xử lý)
Để đảm bảo tính minh bạch và khả năng tái lập (reproducibility), quá trình hình thành dữ liệu được thực hiện qua các bước:

### 3.1. Crawling Pipeline (Thu thập)
- **Script/Công cụ**: Spider crawler (Scrapy/Selenium).
- **Target URL**: Các chuyên mục giải bài tập Vật lý từ lớp 6-12 trên Vietjack.online.
- **Dữ liệu thô**: Được lưu dưới dạng `JSONL` (`lop-10.jsonl`, `lop-11.jsonl`...), chứa các trường `url`, `question_content`, `question_answers`, `question_reason`.

### 3.2. Processing Pipeline (Làm sạch & Làm giàu)
- **Script xử lý**: `scripts/filter_dataset.py`
- **Tiêu chuẩn chất lượng (Inclusion)**:
  - Lời giải (`question_reason`) dài trên 200 ký tự.
  - Bắt buộc chứa **con số** và **phép toán logic** (=, >, <, +, -).
  - Phải có các từ khóa thể hiện lập luận: "Ta có", "Áp dụng", "Suy ra".
- **Tiêu chuẩn loại trừ (Exclusion)**:
  - Loại bỏ hoàn toàn câu hỏi phụ thuộc vào **hình vẽ**, **đồ thị**, **bảng biểu** (do model không có ngữ cảnh thị giác).
  - Loại bỏ các câu hỏi phân tích Đúng/Sai thuần túy.
  - Xóa bỏ **rác trắc nghiệm** ("Đáp án A", "Chọn B").

## 4. Cấu trúc dữ liệu & Xem trước (Data Schema & Preview)
Mỗi data asset (bài tập) được cấu trúc thành một block Markdown độc lập để model dễ dàng phân biệt Đề bài và Lời giải.

**Preview (Mẫu dữ liệu):**
```markdown
## Problem: Tính cường độ điện trường do một điện tích điểm...

**Question:**
Một điện tích điểm q = 5.10^-9 C đặt tại O trong chân không. Tính cường độ điện trường tại điểm M cách O một khoảng 10 cm.

### Solution
Đổi đơn vị: r = 10 cm = 0.1 m.
Áp dụng công thức tính cường độ điện trường do điện tích điểm gây ra:
E = k * |q| / r^2
Thay số: E = 9.10^9 * |5.10^-9| / (0.1)^2 = 4500 V/m.
Vì q > 0 nên véc tơ cường độ điện trường hướng ra xa điện tích.
---
```

## 5. Quy định sử dụng & Tuân thủ (Compliance & Usage)
- **Mục đích sử dụng**: Sử dụng nội bộ cho việc Continue Pre-training (CPT) mô hình Qwen 3.5 4B, giúp mô hình nâng cao khả năng lập luận (reasoning) và tính toán vật lý bằng tiếng Việt.
- **Hạn chế**: Không sử dụng trực tiếp bộ dữ liệu này cho Fine-Tuning (SFT) nếu không format lại thành dạng Instruction/Response JSON. Bộ dữ liệu chỉ nhằm mục đích cung cấp "kiến thức thô" (Corpus).
- **Bản quyền**: Dữ liệu được trích xuất từ internet nhằm mục đích nghiên cứu học máy.

---
*Data Catalog Generated Auto-magically by Exact 2026 Script*
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(catalog_content)

    print(f"Catalog generated successfully at: {output_file}")

if __name__ == "__main__":
    generate_catalog()
