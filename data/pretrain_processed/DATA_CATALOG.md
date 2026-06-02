# Physics Pre-training Data Catalog

## 1. MetaData (Siêu dữ liệu)
- **Tên Data Asset**: Exact Physics High-Quality Pretrain Corpus
- **Định dạng dữ liệu**: Unstructured (Markdown Text)
- **Kích thước dự kiến**: ~2261 samples (sau khi lọc từ 74807 raw samples)
- **Nguồn gốc (Lineage)**: Thu thập từ hệ thống Vietjack (Chuyên mục bài tập Vật lý tự luận/trắc nghiệm có lời giải)
- **Phiên bản**: v1.0
- **Ngày cập nhật cuối**: 2026-05-30
- **Ngôn ngữ**: Tiếng Việt (Giải nghĩa) & Toán học (Công thức)

## 2. Thống kê & Mức độ tin cậy (Data Quality Assessment)
Bộ dữ liệu đã trải qua bước đánh giá và lọc (Quality Control) gắt gao. Dưới đây là tỷ lệ giữ lại sau khi loại bỏ dữ liệu rác:

| Grade (Khối) | Dữ liệu sạch (High-Quality) | Dữ liệu thô (Raw) | Tỷ lệ giữ lại (Retention) |
| :--- | :---: | :---: | :---: |
| Lớp 6 | 14 | 1440 | 0.97% |
| Lớp 7 | 8 | 2670 | 0.30% |
| Lớp 8 | 89 | 4117 | 2.16% |
| Lớp 9 | 203 | 5174 | 3.92% |
| Lớp 10 | 547 | 11327 | 4.83% |
| Lớp 11 | 270 | 16601 | 1.63% |
| Lớp 12 | 1130 | 33478 | 3.38% |
| **Tổng cộng** | **2261** | **74807** | **3.02%** |

## 3. Data Lineage & Pipeline (Nguồn gốc & Quá trình xử lý)
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
