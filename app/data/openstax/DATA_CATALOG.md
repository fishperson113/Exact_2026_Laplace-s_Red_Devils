# Physics Pre-training Data Catalog

## 1. MetaData (Siêu dữ liệu)
- **Tên Data Asset**: OpenStax College Physics 2e Loại B Corpus
- **Định dạng dữ liệu**: Unstructured (Markdown Text)
- **Kích thước hiện tại**: 54 golden section samples từ 54 processed section files
- **Nguồn gốc (Lineage)**: Trích xuất từ OpenStax College Physics 2e PDF, Chapter 5-12
- **Source file**: `app/data/openstax/college-physics-2e_-_WEB.pdf`
- **Phiên bản**: v1.0
- **Ngày cập nhật cuối**: 2026-05-30
- **Ngôn ngữ**: English (Physics explanations) & Mathematics (Formulas)

## 2. Thống kê & Mức độ tin cậy (Data Quality Assessment)
Bộ dữ liệu đã được tách theo đúng mục lục PDF, chỉ giữ các numbered sections như `5.1`, `6.2`, `12.7`. Các phần outline, introduction, glossary, section summary, conceptual questions, và problems không được đưa vào corpus Loại B.

| Chapter | Chủ đề | Processed Markdown | Golden Markdown | Tỷ lệ giữ lại |
| :--- | :--- | :---: | :---: | :---: |
| Chapter 5 | Further Applications of Newton's Laws | 3 | 3 | 100% |
| Chapter 6 | Uniform Circular Motion and Gravitation | 6 | 6 | 100% |
| Chapter 7 | Work, Energy, and Energy Resources | 9 | 9 | 100% |
| Chapter 8 | Linear Momentum and Collisions | 7 | 7 | 100% |
| Chapter 9 | Statics and Torque | 6 | 6 | 100% |
| Chapter 10 | Rotational Motion and Angular Momentum | 7 | 7 | 100% |
| Chapter 11 | Fluid Statics | 9 | 9 | 100% |
| Chapter 12 | Fluid Dynamics | 7 | 7 | 100% |
| **Tổng cộng** | | **54** | **54** | **100%** |

**Dung lượng hiện tại:**
- Source PDF: ~251.26 MiB
- Processed Markdown: ~824 KiB
- Golden Markdown: ~233 KiB

## 3. Data Lineage & Pipeline (Nguồn gốc & Quá trình xử lý)
Để đảm bảo tính minh bạch và khả năng tái lập (reproducibility), quá trình hình thành dữ liệu được thực hiện qua các bước:

### 3.1. Extraction Pipeline (Tách chương và section)
- **Script/Công cụ**: `app/data/openstax/prepare_openstax_type_b.py`
- **Thư viện**: PyMuPDF (`fitz`)
- **Nguồn PDF**: `app/data/openstax/college-physics-2e_-_WEB.pdf`
- **Phạm vi**: Chapter 5 đến Chapter 12
- **Quy tắc tách dữ liệu**:
  - Dùng PDF table of contents để xác định chapter boundaries.
  - Chỉ lấy level-2 numbered sections có dạng `N.M Section Title`.
  - Bỏ qua chapter outline, introduction, glossary, section summary, conceptual questions, và problems.

### 3.2. Processing Pipeline (PDF sang Markdown)
- **Script xử lý**: `app/data/openstax/prepare_openstax_type_b.py convert`
- **Công cụ chuyển đổi**: Microsoft MarkItDown
- **Model/API**: Đọc từ `.env` qua `OPENAI_API_KEY` và `OPENAI_API_MODEL`
- **Output**: `app/data/openstax/processed/<chapter_slug>/<section_slug>.md`
- **Vai trò**: Chuyển từng section PDF thành Markdown thô để giữ lại nội dung textbook, công thức, ví dụ và đơn vị.

### 3.3. Golden Transformation Pipeline (Chuẩn hóa Loại B)
- **Script xử lý**: `app/data/openstax/prepare_openstax_type_b.py transform`
- **LLM provider**: OpenAI
- **Model/API**: Đọc từ `.env` qua `OPENAI_API_KEY` và `OPENAI_API_MODEL`
- **Output**: `app/data/openstax/golden/<chapter_slug>/<section_slug>.md`
- **Tiêu chuẩn chất lượng (Inclusion)**:
  - Có concept explanation rõ ràng.
  - Có key formulas và giải thích biến số/đơn vị.
  - Có worked example nếu section nguồn có ví dụ.
  - Có danh sách key concepts used.
- **Tiêu chuẩn loại trừ (Exclusion)**:
  - Không tạo JSONL/CSV.
  - Không tự bịa ví dụ nếu source section không có ví dụ.
  - Loại bỏ header/footer, page number, navigation text và boilerplate PDF.

## 4. Cấu trúc dữ liệu & Xem trước (Data Schema & Preview)
Mỗi data asset là một file Markdown độc lập cho một numbered section của sách. Golden files dùng cấu trúc Loại B thống nhất để phục vụ continue pre-training.

**Schema chuẩn:**
```markdown
# <section number> <section title>

Source: OpenStax College Physics 2e, Chapter <n>, Section <n.m>

## Concept explanation
...

## Key formulas
...

## Variables and units
...

## Worked example
...

## Key concepts used
...
```

**Preview (Mẫu dữ liệu):**
```markdown
# 5.1 Friction

Source: OpenStax College Physics 2e, Chapter 5, Section 5.1

## Concept explanation
Friction is a force that opposes relative motion between surfaces in contact.

## Key formulas
f_s <= mu_s N
f_k = mu_k N

## Variables and units
- f_s: static friction force, in newtons (N)
- f_k: kinetic friction force, in newtons (N)
- mu_s, mu_k: coefficients of friction, unitless

## Worked example
A skier with a mass of 62 kg is sliding down a snowy slope...

## Key concepts used
- Static friction
- Kinetic friction
- Normal force
- Coefficient of friction
```

## 5. Quy định sử dụng & Tuân thủ (Compliance & Usage)
- **Mục đích sử dụng**: Sử dụng nội bộ cho việc Continue Pre-training (CPT), giúp mô hình nâng cao kiến thức nền về cơ học, năng lượng, động lượng, chuyển động quay, và chất lưu.
- **Hạn chế**: Không sử dụng trực tiếp bộ dữ liệu này cho Supervised Fine-Tuning (SFT) nếu chưa format lại thành dạng Instruction/Response hoặc JSONL phù hợp.
- **Bản quyền**: Dữ liệu nguồn đến từ OpenStax College Physics 2e. Khi phân phối hoặc tái sử dụng bên ngoài, cần giữ attribution và tuân thủ license của OpenStax.
- **Tái lập dữ liệu**: Có thể chạy lại pipeline bằng `app/data/openstax/prepare_openstax_type_b.py`.

---
*Data Catalog Generated Auto-magically by Exact 2026 Script*
