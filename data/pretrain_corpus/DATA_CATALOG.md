# Physics Pre-training Data Catalog

## 1. MetaData (Siêu dữ liệu)
- **Tên Data Asset**: Exact Physics Textbook Pre-training Corpus
- **Định dạng dữ liệu**: Unstructured (Markdown Text) + JSONL intermediate pairs
- **Kích thước hiện tại**: 451 golden markdown samples
- **Nguồn gốc (Lineage)**: Trích xuất từ OpenStax College Physics 2e, Giancoli Physics: Principles with Applications 7th ed., Young & Freedman University Physics 13th ed., và Fundamentals of Physics.
- **Source files**:
  - `app/data/openstax/college-physics-2e_-_WEB.pdf`
  - `app/data/Giancoli/Giancoli-Physics-Principles-with-Applications-7th-c2014-txtbk-1.pdf`
  - `app/data/university_of_physic/Young-Freedman-University-Physics-13th-txtbk_compressed.pdf`
  - `app/data/Fundamental_of_physics/Fundamental_of_physics.pdf`
- **Phiên bản**: v1.0
- **Ngày cập nhật cuối**: 2026-05-31
- **Ngôn ngữ**: English (Physics explanations) & Mathematics (Formulas)

## 2. Thống kê & Mức độ tin cậy (Data Quality Assessment)
Bộ dữ liệu hiện gồm bốn asset chính:
- **OpenStax Loại B**: lý thuyết + công thức + ví dụ, tách theo numbered sections.
- **Giancoli Loại A**: end-of-chapter problem statements paired with odd-numbered appendix answers, transformed into worked-solution markdown.
- **Young & Freedman Worked Examples**: textbook worked examples from Chapters 21-31, transformed into standalone markdown named by example subtitle.
- **Fundamentals of Physics Sample Problems**: sample problems from Chapters 21-33, transformed into standalone worked-example markdown named by sample subtitle.

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

### 2.3 Young & Freedman University Physics — Worked Examples
Young & Freedman được tách theo chapter 21-31, chỉ lấy worked examples có nhãn `Example <chapter>.<number>` trước phần `Summary`. File markdown được đặt tên theo quy ước `<example_number>_<subtitle_slug>.md`.

| Chapter | Chủ đề | Parsed Examples | Golden Examples | Needs Review |
| :--- | :--- | :---: | :---: | :---: |
| Chapter 21 | Electric Charge and Electric Field | 14 | 14 | Included |
| Chapter 22 | Gauss's Law | 13 | 13 | Included |
| Chapter 23 | Electric Potential | 14 | 14 | Included |
| Chapter 24 | Capacitance and Dielectrics | 12 | 12 | Included |
| Chapter 25 | Current, Resistance, and Electromotive Force | 11 | 11 | Included |
| Chapter 26 | Direct-Current Circuits | 14 | 14 | Included |
| Chapter 27 | Magnetic Field and Magnetic Forces | 12 | 12 | Included |
| Chapter 28 | Sources of Magnetic Field | 12 | 12 | Included |
| Chapter 29 | Electromagnetic Induction | 11 | 11 | Included |
| Chapter 30 | Inductance | 10 | 10 | Included |
| Chapter 31 | Alternating Current | 9 | 9 | Included |
| **Tổng cộng** | | **132** | **132** | **120 flagged** |

### 2.4 Fundamentals of Physics — Sample Problems
Fundamentals of Physics được tách theo chapter 21-33, chỉ lấy các worked sample problems có nhãn `Sample Problem <chapter>.<number>`. File markdown được đặt tên theo quy ước `<sample_number>_<subtitle_slug>.md`.

| Chapter | Chủ đề | Parsed Sample Problems | Golden Sample Problems | Needs Review |
| :--- | :--- | :---: | :---: | :---: |
| Chapter 21 | Coulomb's Law | 4 | 4 | 4 |
| Chapter 22 | Electric Fields | 5 | 5 | 5 |
| Chapter 23 | Gauss' Law | 7 | 7 | 7 |
| Chapter 24 | Electric Potential | 7 | 7 | 7 |
| Chapter 25 | Capacitance | 6 | 6 | 6 |
| Chapter 26 | Current and Resistance | 6 | 6 | 6 |
| Chapter 27 | Circuits | 5 | 5 | 5 |
| Chapter 28 | Magnetic Fields | 7 | 7 | 7 |
| Chapter 29 | Magnetic Fields Due to Currents | 4 | 4 | 4 |
| Chapter 30 | Induction and Inductance | 8 | 8 | 7 |
| Chapter 31 | Electromagnetic Oscillations and Alternating Current | 8 | 8 | 8 |
| Chapter 32 | Maxwell's Equations; Magnetism of Matter | 4 | 4 | 4 |
| Chapter 33 | Electromagnetic Waves | 3 | 3 | 3 |
| **Tổng cộng** | | **74** | **74** | **73 flagged** |

**Dung lượng hiện tại:**
- OpenStax source PDF: ~251.26 MiB
- OpenStax processed markdown: ~824 KiB
- OpenStax golden markdown: ~233 KiB
- Giancoli raw extracted PDFs: ~14.60 MiB
- Giancoli processed files: ~1.10 MiB
- Giancoli golden markdown: ~381 KiB
- Young & Freedman raw extracted PDFs: ~13.88 MiB
- Young & Freedman processed files: ~2.68 MiB
- Young & Freedman golden markdown: ~346 KiB
- Fundamentals raw extracted PDFs: ~38.54 MiB
- Fundamentals processed files: ~4.06 MiB
- Fundamentals golden markdown: ~205 KiB

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

### 3.5. Young & Freedman Worked Example Pipeline
- **Script xử lý**: `app/data/university_of_physic/prepare_university_physics_examples.py`
- **Nguồn PDF**: `app/data/university_of_physic/Young-Freedman-University-Physics-13th-txtbk_compressed.pdf`
- **Phạm vi**: Chapter 21 đến Chapter 31
- **Raw output**: `app/data/university_of_physic/raw/<chapter_slug>/`
- **Processed output**: `app/data/university_of_physic/processed/<chapter_slug>/worked_examples.jsonl`
- **Golden output**: `app/data/university_of_physic/golden/<chapter_slug>/<example_number>_<subtitle_slug>.md`
- **Quy trình**:
  - Dùng PyMuPDF để tách chapter và numbered sections.
  - Dùng Microsoft MarkItDown để chuyển section PDFs sang Markdown.
  - Parse worked examples từ source text bằng nhãn `Example N.M`, loại bỏ summary và end-of-chapter problems.
  - Dùng OpenAI để chuẩn hóa mỗi worked example thành Markdown độc lập.
- **Quality flag**: `needs_review: true` cho ví dụ phụ thuộc hình vẽ, bảng, OCR không chắc chắn, hoặc công thức bị mất ký hiệu.

### 3.6. Fundamentals of Physics Sample Problem Pipeline
- **Script xử lý**: `app/data/Fundamental_of_physics/prepare_fundamentals_physics_examples.py`
- **Nguồn PDF**: `app/data/Fundamental_of_physics/Fundamental_of_physics.pdf`
- **Phạm vi**: Chapter 21 đến Chapter 33
- **Raw output**: `app/data/Fundamental_of_physics/raw/<chapter_slug>/`
- **Processed output**: `app/data/Fundamental_of_physics/processed/<chapter_slug>/sample_problems.jsonl`
- **Golden output**: `app/data/Fundamental_of_physics/golden/<chapter_slug>/<sample_number>_<subtitle_slug>.md`
- **Quy trình**:
  - Dùng PyMuPDF để tách chapter và numbered sections.
  - Dùng Microsoft MarkItDown để chuyển section PDFs sang Markdown.
  - Parse sample problems từ source text bằng nhãn `Sample Problem N.NN`, loại bỏ summary và end-of-chapter problems.
  - Dùng OpenAI để chuẩn hóa mỗi sample problem thành Markdown độc lập.
- **Quality flag**: `needs_review: true` cho sample problem phụ thuộc hình vẽ, bảng, OCR không chắc chắn, hoặc công thức bị mất ký hiệu.

## 4. Cấu trúc dữ liệu & Xem trước (Data Schema & Preview)
Mỗi data asset là một file Markdown độc lập. OpenStax dùng schema Loại B theo section lý thuyết; Giancoli dùng schema problem-solution theo từng bài odd-numbered; Young & Freedman dùng schema worked-example theo từng ví dụ trong textbook; Fundamentals of Physics dùng schema sample-problem theo từng worked sample problem.

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

**Young & Freedman worked-example schema:**
```markdown
---
source: Young and Freedman University Physics, 13th ed.
chapter: <chapter number>
section: <section number>
example_number: <example number>
subtitle: <example subtitle>
needs_review: <true|false>
---

# Example <example number>: <example subtitle>

## Problem
...

## Setup
...

## Solution
...

## Evaluation
...

## Key concepts used
...
```

**Young & Freedman filename convention:**
```text
<example_number>_<subtitle_slug>.md
```

Example:
```text
30_010_an_underdamped_l_r_c_series_circuit.md
```

**Fundamentals of Physics sample-problem schema:**
```markdown
---
source: Fundamentals of Physics
chapter: <chapter number>
section: <section number>
sample_problem_number: <sample problem number>
subtitle: <sample problem subtitle>
needs_review: <true|false>
---

# Sample Problem <sample problem number>: <sample problem subtitle>

## Problem
...

## Key ideas
...

## Solution
...

## Answer
...

## Key concepts used
...
```

**Fundamentals of Physics filename convention:**
```text
<sample_number>_<subtitle_slug>.md
```

Example:
```text
30_008_mutual_inductance_of_two_parallel_coils.md
```

## 5. Quy định sử dụng & Tuân thủ (Compliance & Usage)
- **Mục đích sử dụng**: Sử dụng nội bộ cho việc Continue Pre-training (CPT), giúp mô hình nâng cao kiến thức nền và khả năng giải bài tập vật lý.
- **Hạn chế**: Không sử dụng trực tiếp bộ dữ liệu này cho Supervised Fine-Tuning (SFT) nếu chưa format lại thành dạng Instruction/Response hoặc JSONL phù hợp.
- **Bản quyền**: Dữ liệu nguồn đến từ OpenStax College Physics 2e, Giancoli Physics: Principles with Applications 7th ed., Young & Freedman University Physics 13th ed., và Fundamentals of Physics. Khi phân phối hoặc tái sử dụng bên ngoài, cần kiểm tra license/rights của từng nguồn.
- **Tái lập dữ liệu**:
  - OpenStax: `app/data/openstax/prepare_openstax_type_b.py`
  - Giancoli: `app/data/Giancoli/prepare_giancoli_solutions.py`
  - Young & Freedman: `app/data/university_of_physic/prepare_university_physics_examples.py`
  - Fundamentals of Physics: `app/data/Fundamental_of_physics/prepare_fundamentals_physics_examples.py`

---
*Data Catalog Generated Auto-magically by Exact 2026 Script*
