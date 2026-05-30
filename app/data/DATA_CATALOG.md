# Physics Pre-training Data Catalog

## 1. MetaData (Siêu dữ liệu)
- **Tên Data Asset**: Exact Physics Textbook Pre-training Corpus
- **Định dạng dữ liệu**: Unstructured (Markdown Text) + JSONL intermediate pairs
- **Kích thước hiện tại**: 245 golden markdown samples
- **Nguồn gốc (Lineage)**: Trích xuất từ OpenStax College Physics 2e và Giancoli Physics: Principles with Applications 7th ed.
- **Source files**:
  - `app/data/openstax/college-physics-2e_-_WEB.pdf`
  - `app/data/Giancoli/Giancoli-Physics-Principles-with-Applications-7th-c2014-txtbk-1.pdf`
- **Phiên bản**: v1.0
- **Ngày cập nhật cuối**: 2026-05-30
- **Ngôn ngữ**: English (Physics explanations) & Mathematics (Formulas)

## 2. Thống kê & Mức độ tin cậy (Data Quality Assessment)
Bộ dữ liệu hiện gồm hai asset chính:
- **OpenStax Loại B**: lý thuyết + công thức + ví dụ, tách theo numbered sections.
- **Giancoli Loại A**: end-of-chapter problem statements paired with odd-numbered appendix answers, transformed into worked-solution markdown.

### 2.1 OpenStax College Physics 2e — Loại B
OpenStax được tách theo đúng mục lục PDF, chỉ giữ các numbered sections như `5.1`, `6.2`, `12.7`. Các phần outline, introduction, glossary, section summary, conceptual questions, và problems không được đưa vào corpus Loại B.

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

### 2.2 Giancoli Physics: Principles with Applications — End-of-Chapter Solutions
Giancoli được tách theo chapter 16-22, lấy `Problems`, `General Problems`, và appendix `Answers to Odd-Numbered Problems`. Pipeline ghép odd-numbered problem statements với source final answers, sau đó tạo worked-solution markdown.

| Chapter | Chủ đề | Paired Problems | Golden Solutions | Needs Review |
| :--- | :--- | :---: | :---: | :---: |
| Chapter 16 | Electric Charge and Electric Field | 21 | 21 | Included |
| Chapter 17 | Electric Potential | 25 | 25 | Included |
| Chapter 18 | Electric Currents | 33 | 33 | Included |
| Chapter 19 | DC Circuits | 30 | 30 | Included |
| Chapter 20 | Magnetism | 32 | 32 | Included |
| Chapter 21 | Electromagnetic Induction and Faraday's Law | 37 | 37 | Included |
| Chapter 22 | Electromagnetic Waves | 13 | 13 | Included |
| **Tổng cộng** | | **191** | **191** | **53 flagged** |

**Dung lượng hiện tại:**
- OpenStax source PDF: ~251.26 MiB
- OpenStax processed markdown: ~824 KiB
- OpenStax golden markdown: ~233 KiB
- Giancoli raw extracted PDFs: ~14.60 MiB
- Giancoli processed files: ~1.10 MiB
- Giancoli golden markdown: ~381 KiB

## 3. Data Lineage & Pipeline (Nguồn gốc & Quá trình xử lý)
Để đảm bảo tính minh bạch và khả năng tái lập (reproducibility), quá trình hình thành dữ liệu được thực hiện qua các bước:

### 3.1. OpenStax Extraction Pipeline (Tách chương và section)
- **Script/Công cụ**: `app/data/openstax/prepare_openstax_type_b.py`
- **Thư viện**: PyMuPDF (`fitz`)
- **Nguồn PDF**: `app/data/openstax/college-physics-2e_-_WEB.pdf`
- **Phạm vi**: Chapter 5 đến Chapter 12
- **Quy tắc tách dữ liệu**:
  - Dùng PDF table of contents để xác định chapter boundaries.
  - Chỉ lấy level-2 numbered sections có dạng `N.M Section Title`.
  - Bỏ qua chapter outline, introduction, glossary, section summary, conceptual questions, và problems.

### 3.2. OpenStax Processing Pipeline (PDF sang Markdown)
- **Script xử lý**: `app/data/openstax/prepare_openstax_type_b.py convert`
- **Công cụ chuyển đổi**: Microsoft MarkItDown
- **Model/API**: Đọc từ `.env` qua `OPENAI_API_KEY` và `OPENAI_API_MODEL`
- **Output**: `app/data/openstax/processed/<chapter_slug>/<section_slug>.md`
- **Vai trò**: Chuyển từng section PDF thành Markdown thô để giữ lại nội dung textbook, công thức, ví dụ và đơn vị.

### 3.3. OpenStax Golden Transformation Pipeline (Chuẩn hóa Loại B)
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

### 3.4. Giancoli Problem-Solution Pipeline
- **Script xử lý**: `app/data/Giancoli/prepare_giancoli_solutions.py`
- **Nguồn PDF**: `app/data/Giancoli/Giancoli-Physics-Principles-with-Applications-7th-c2014-txtbk-1.pdf`
- **Phạm vi**: Chapter 16 đến Chapter 22
- **Raw output**: `app/data/Giancoli/raw/<chapter_slug>/`
- **Processed output**: `app/data/Giancoli/processed/<chapter_slug>/problem_answer_pairs.jsonl`
- **Golden output**: `app/data/Giancoli/golden/<chapter_slug>/<chapter>_<problem>.md`
- **Quy trình**:
  - Dùng PyMuPDF để tách chapter, `Problems`, `General Problems`, và appendix answers.
  - Dùng Microsoft MarkItDown để chuyển PDF extracts sang Markdown.
  - Parse odd-numbered problems và ghép với appendix answers.
  - Dùng OpenAI để tạo worked solutions, ràng buộc final answer theo source answer.
- **Quality flag**: `needs_review: true` cho bài phụ thuộc hình vẽ, bảng, OCR không chắc chắn, hoặc lời giải cần kiểm tra thủ công.

## 4. Cấu trúc dữ liệu & Xem trước (Data Schema & Preview)
Mỗi data asset là một file Markdown độc lập. OpenStax dùng schema Loại B theo section lý thuyết; Giancoli dùng schema problem-solution theo từng bài odd-numbered.

**OpenStax Loại B schema:**
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

**OpenStax preview (Mẫu dữ liệu):**
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

**Giancoli worked-solution schema:**
```markdown
---
source: Giancoli Physics: Principles with Applications, 7th ed.
chapter: <chapter number>
problem_number: <problem number>
answer_source: Answers to Odd-Numbered Problems
needs_review: <true|false>
---

# Problem <chapter>.<problem_number>

## Question
...

## Final answer from source
...

## Worked solution
...

## Key concepts used
...
```

**Giancoli preview (Mẫu dữ liệu):**
```markdown
# Problem 22.7

## Question
In an EM wave traveling west, the B field oscillates up and down vertically...

## Final answer from source
90.0 kHz, along the horizontal north-south line.

## Worked solution
Use the EM wave relationship E_rms = c B_rms and the fact that E, B,
and propagation direction are mutually perpendicular.

## Key concepts used
- Electromagnetic wave propagation
- E and B field relationship
- Direction from vector cross product
```

## 5. Quy định sử dụng & Tuân thủ (Compliance & Usage)
- **Mục đích sử dụng**: Sử dụng nội bộ cho việc Continue Pre-training (CPT), giúp mô hình nâng cao kiến thức nền và khả năng giải bài tập vật lý.
- **Hạn chế**: Không sử dụng trực tiếp bộ dữ liệu này cho Supervised Fine-Tuning (SFT) nếu chưa format lại thành dạng Instruction/Response hoặc JSONL phù hợp.
- **Bản quyền**: Dữ liệu nguồn đến từ OpenStax College Physics 2e và Giancoli Physics: Principles with Applications 7th ed. Khi phân phối hoặc tái sử dụng bên ngoài, cần kiểm tra license/rights của từng nguồn.
- **Tái lập dữ liệu**:
  - OpenStax: `app/data/openstax/prepare_openstax_type_b.py`
  - Giancoli: `app/data/Giancoli/prepare_giancoli_solutions.py`

---
*Data Catalog Generated Auto-magically by Exact 2026 Script*
