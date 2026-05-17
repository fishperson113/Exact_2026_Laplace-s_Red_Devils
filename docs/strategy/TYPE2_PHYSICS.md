# Chiến lược Type 2 — Physics Problems

> **Đội:** Laplace's Red Devils
> **Ngày:** 2026-05-17
> **Phạm vi:** Task Type 2 — Giải bài tập Vật lý (Mạch điện & Tĩnh điện)
> **Timeline:** Phase 1 eval: Jun 1-2 | Phase 2 eval: Jun 5-7 | Top 10: Jun 10 | Public Test Day: Jun 15

---

## 1. Tóm tắt bài toán

Xây dựng API endpoint nhận câu hỏi Vật lý tiếng Anh (gốc dịch máy từ tiếng Việt), trả về:

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| `answer` | **Có** | Đáp án số học (có dung sai) |
| `explanation` | **Có** | Giải thích tự nhiên |
| `cot` | Tùy chọn (khuyến khích) | Chain-of-Thought step-by-step |
| `confidence` | Tùy chọn | Độ tin cậy |

**Tiêu chí chấm:**
- **P1 — Correctness (trọng số cao nhất):** Đáp án đúng + đơn vị đúng
- **P2 — Explanation Quality:** Giải thích rõ ràng, mạch lạc
- **P3 — Reasoning Depth:** Độ sâu suy luận (CoT, tool call logs)

**Triết lý:** Đáp án đúng là nền tảng — khi đáp án đúng, CoT tự nhiên sẽ đúng. Ưu tiên tuyệt đối Correctness.

---

## 2. Phần cứng & ràng buộc

### 2.1 Phần cứng (Colab Pro+)

| GPU | VRAM | Phù hợp cho |
|---|---|---|
| A100 | 40 GB | Fine-tune fp16, inference nặng |
| L4 | 22.5 GB | Fine-tune 4-bit, inference chính |
| T4 | 16 GB | Inference nhẹ, testing |

### 2.2 Ràng buộc cuộc thi

| Ràng buộc | Chi tiết |
|---|---|
| Model size | Open-source, **≤ 8B params** (tổng params, MoE tính tổng) |
| Model "8B-class" | Chấp nhận model gắn nhãn 8B dù thực tế ~8.19B (ví dụ: DeepSeek-R1-0528-Qwen3-8B) |
| Pipeline | Nhiều model ≤ 8B OK nhưng **sequential only** — cấm chạy song song |
| Hosting | **Tự host bằng vLLM** (hoặc tương đương), endpoint `/v1/models` phải kiểm tra được |
| Timeout | **60 giây / request** |
| Tool calling | Được phép Python/SymPy/Z3/calculator — log tool call phải nằm trong CoT |
| Dữ liệu ngoài | Được crawl, synthetic data từ GPT-4/Claude để train — **cấm gọi API lúc inference** |
| API format | **Single endpoint** xử lý cả Type 1 (Logic) và Type 2 (Physics) |

### 2.3 Điểm cần lưu ý so với setup hiện tại

Codebase hiện tại dùng **Ollama** để serve model (xem `MODEL_CONTRACT.md`). Tuy nhiên, quy định cuộc thi yêu cầu **vLLM** (hoặc tương đương có `/v1/models`). Cần chuyển sang vLLM trước khi nộp, hoặc đảm bảo Ollama expose endpoint tương thích mà BTC chấp nhận.

---

## 3. Dữ liệu

### 3.1 Dataset BTC cung cấp

| Phiên bản | Trạng thái | Số dòng |
|---|---|---|
| 2026-05-09 | **Lỗi thời** — nhiều nhiễu, 401 dòng QA rỗng, lỗi dán nhãn | 1,755 |
| 2026-05-15 | **Bắt buộc dùng** — đã fix bug, drop 403 dòng | 1,352 |

**Phân phối theo ID prefix (domain):**

```
LD     397   ← Lực điện / Tĩnh điện (chiếm 29.4%) — domain lớn nhất
CH     290   ← Chất điện / Điện dung
NL     190   ← Năng lượng
TD     177   ← Tụ điện
DDT    130   ← Điện điện trường
THCB    80   ← Tổng hợp cơ bản
DT      68   ← Điện trường
CHLT    20   ← Chất lỏng / đặc biệt (ít nhất — mất cân bằng)
-----------
Total 1,352
```

### 3.2 Vấn đề chất lượng dữ liệu (dù bản 15/05)

Từ CHANGELOG và EDA notebook, các vấn đề đã biết:

1. **CoT có thể sai logic/tính toán** — dữ liệu sinh bởi máy, cross-check bằng SymPy là bắt buộc
2. **Format toán học không nhất quán** — lẫn lộn `*`, `·`, `×`, LaTeX, text thuần, scientific notation
3. **Gốc dịch máy từ tiếng Việt** — câu hỏi có thể thiếu thông tin, mơ hồ, hoặc dùng sai thuật ngữ
4. **Một số answer vẫn có thể sai** — ví dụ TD401 (answer = 45 thay vì 0.045), TD179 (283.2 → 283.1), TD181 (1.46 → 1.45) đã được fix, nhưng có thể còn case chưa phát hiện

### 3.3 Chiến lược xử lý dữ liệu

#### A. Phân tích & Làm sạch

- **EDA bổ sung trên bản 15/05:** Phân tích phân phối domain, độ dài câu hỏi, phân bố answer (range số, đơn vị), tìm outlier
- **Cross-check tự động:** Viết script Python/SymPy tự giải lại từ câu hỏi → so sánh với `answer` trong dataset → flag những dòng mismatch
- **Chuẩn hóa format toán học:** Pipeline tự động normalize: ký hiệu nhân (`×`), số mũ, đơn vị SI, scientific notation
- **Chuẩn hóa câu hỏi:** Dùng LLM thương mại (GPT-4o / DeepSeek) rewrite câu hỏi cho rõ ràng, chuẩn ngữ pháp tiếng Anh

#### B. Sinh CoT & Answer chất lượng cao

Vì CoT và Answer trong dataset gốc không đáng tin cậy:

- **Dùng LLM thương mại (GPT-4o, DeepSeek-R1, Claude) để sinh lại CoT và Answer** cho toàn bộ 1,352 bài
- So sánh answer sinh ra vs answer gốc → phân loại:
  - Match → giữ nguyên, dùng CoT mới
  - Mismatch → review thủ công hoặc tự động bằng SymPy để quyết định đâu là đúng
- Output: Dataset "golden" với CoT step-by-step chuẩn xác, phục vụ fine-tune

#### C. Knowledge Base cho RAG (Công thức Vật lý)

Xây dựng knowledge base bên ngoài bao gồm:

- **Tập công thức vật lý** theo từng domain trong dataset (tĩnh điện, mạch điện, tụ điện, năng lượng,...)
- **Bài giải mẫu (few-shot examples)** — mỗi domain 5-10 bài mẫu có CoT hoàn chỉnh
- **Lookup table đơn vị & hằng số** — ε₀, e, k (hằng số Coulomb), các bội số SI,...
- Format: structured (JSON/YAML) để dễ retrieve + inject vào prompt

#### D. Dữ liệu bên ngoài & Data Augmentation

- **Crawl bài Vật lý** từ:
  - Sách giáo khoa Vật lý (Physics textbook problems)
  - Các trang giải bài trực tuyến (Khan Academy, PhysicsForums, Chegg,...)
  - Đề thi Vật lý tiếng Anh (AP Physics, GCE, university exams)
- **Synthetic data:** Dùng GPT-4o/Claude sinh thêm bài tập mới cùng domain → tăng cường cho các domain ít mẫu (CHLT chỉ có 20, DT chỉ có 68)
- **Tất cả phải khai báo** trong Data Disclosure Document

---

## 4. Mô hình

### 4.1 Lựa chọn chính: Qwen3.5-4B

**Lý do chọn:**

| Tiêu chí | Qwen3.5-4B | Qwen2.5-7B-Instruct |
|---|---|---|
| GPQA | **76.2%** | 36.4% |
| IFEval | **89.8%** | 71.2% |
| MMLU-Pro | **79.1%** | 56.3% |
| MMLU-Redux | **88.8%** | 75.4% |
| Params | 4B | 7B |
| Context | 262K (native) → 1M+ | 128K |

- **MMLU-Pro và GPQA** là các benchmark phù hợp nhất cho bài toán Vật lý yêu cầu reasoning sâu
- **4B params** → còn **4B budget** cho model phụ hoặc các thành phần khác trong pipeline
- Context window cực lớn → thoải mái inject few-shot, CoT dài, tool call logs
- Dù đã ra khá lâu nhưng vẫn là top performer trong phân khúc small model

### 4.2 Ngân sách tham số (8B Budget)

```
┌────────────────────────────────────────────┐
│            8B Parameter Budget             │
├──────────────────┬─────────────────────────┤
│  Qwen3.5-4B      │  4B còn lại             │
│  (Main Solver)   │  (Dự phòng cho)         │
│                  │  - Router/Classifier     │
│                  │  - Tool-former           │
│                  │  - Verifier              │
│                  │  - Hoặc 1 con 4B khác    │
└──────────────────┴─────────────────────────┘
```

**Lưu ý quan trọng:** Dù có 4B còn lại, **cuộc thi cấm chạy song song nếu tổng vượt qua 8B**. Latency (timeout 60s).

### 4.3 Chiến lược Fine-tune

**Phương pháp:** LoRA fine-tune qua Unsloth (đã có guide tại `UNSLOTH_GUIDE.md`)

**Dữ liệu training phải đạt chất lượng cao trước khi train:**
- Dataset "golden" đã qua cross-check (Mục 3.3.B)
- Synthetic data bổ sung cho domain yếu
- Bài giải với CoT step-by-step chuẩn xác

**Quantization cho deploy:** `q4_k_m` (default) — ~2.3 GB cho 4B model, thoải mái trên mọi GPU. Hoặc có thể dùng A100 40GB VRAM/ L4 22.5GB VRAM / T4 16GB VRAM để chạy F8, F16.

**Lưu ý về serving:**
- Codebase hiện tại dùng Ollama + GGUF
- Cuộc thi yêu cầu vLLM → cần adapt pipeline
- vLLM hỗ trợ trực tiếp Qwen3.5 → có thể serve unquantized hoặc GPTQ/AWQ trên A100

### 4.4 Chiến lược Inference

Kết hợp nhiều kỹ thuật để tối đa hóa accuracy:

#### A. RAG (Retrieval-Augmented Generation)

```
Câu hỏi → Phân loại domain → Retrieve công thức + few-shot → Inject vào prompt → LLM giải
```

- Retrieve từ Knowledge Base (Mục 3.3.C)
- Few-shot examples giúp model hiểu format output và cách giải
- Đặc biệt hữu ích cho domain ít mẫu

#### B. CoT (Chain-of-Thought)

- Prompt model xuất reasoning step-by-step trước khi đưa ra answer
- CoT không chỉ để chấm điểm P3 mà còn giúp model reasoning chính xác hơn
- Format CoT chuẩn: `Step 1: Identify given values → Step 2: Recall formula → Step 3: Substitute → Step 4: Calculate → Step 5: State answer with unit`

#### C. PoT (Program-of-Thought)

- Model sinh code Python thay vì tính tay
- Thực thi code → lấy kết quả số học chính xác
- **Đây là chiến lược then chốt** vì LLM hay sai tính toán số học, còn code thì không

#### D. Symbolic Verification (SymPy/Z3)

- Sau khi model trả answer, chạy symbolic solver verify lại
- Nếu mismatch → retry hoặc trust kết quả symbolic
- Pipeline: `LLM giải → extract phương trình → SymPy verify → nếu sai → SymPy solve → trả kết quả symbolic`

#### E. Self-Consistency / Majority Voting (nếu đủ budget thời gian)

- Sinh nhiều lời giải (temperature > 0) → vote answer phổ biến nhất
- Trade-off: tốn thời gian (timeout 60s), nhưng tăng accuracy đáng kể

---

## 5. Kiến trúc Pipeline

### 5.1 Pipeline tổng quan

```
                        ┌─────────────────────────────────┐
                        │        API Endpoint (:8000)      │
                        │      POST /ask                   │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   1. Preprocessor                │
                        │   - Chuẩn hóa câu hỏi           │
                        │   - Detect domain (LD/CH/TD/...) │
                        │   - Normalize math notation      │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   2. RAG Retriever               │
                        │   - Retrieve công thức by domain │
                        │   - Retrieve few-shot examples   │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   3. Qwen3.5-4B (Main Solver)    │
                        │   - Input: question + context    │
                        │   - Output: CoT + Python code    │
                        │     hoặc CoT + direct answer     │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   4. Code Executor (Sandbox)     │
                        │   - Chạy Python/SymPy code       │
                        │   - Timeout 10s per execution    │
                        │   - Return numerical result      │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   5. Verifier                    │
                        │   - SymPy cross-check            │
                        │   - Unit consistency check       │
                        │   - Nếu fail → retry (tối đa 1) │
                        └────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────────┐
                        │   6. Response Formatter          │
                        │   - Đóng gói JSON theo schema    │
                        │   - answer, explanation, cot,    │
                        │     confidence                   │
                        └─────────────────────────────────┘
```

### 5.2 Mapping vào LangGraph (mở rộng pipeline hiện có)

Pipeline hiện tại:
```
[load_history] → [generate] → [parse] → [save_memory] → END
```

Pipeline mục tiêu:
```
[preprocess] → [retrieve] → [generate_with_pot] → [execute_code]
    → [verify] → [format_response] → END
```

Mỗi bước là một node trong LangGraph, tuân theo pattern `DEVELOPMENT.md`:
- Thêm field vào `QAState`
- Viết `node_xxx()` → return dict chỉ chứa key thay đổi
- Nối edge vào graph

### 5.3 Tool Calling Integration

| Tool | Mục đích | Implementation |
|---|---|---|
| **Python executor** | Chạy code sinh bởi model | Sandbox (subprocess hoặc Docker) |
| **SymPy solver** | Giải phương trình symbolic | `app/tools/sympy_solver.py` |
| **Unit converter** | Đổi đơn vị SI | `app/tools/unit_converter.py` |
| **Formula lookup** | Tra công thức theo domain | RAG retriever |
| **Web search** | Tra cứu bổ sung (nếu cần) | MCP tool hoặc API |

Tool call logs phải được append vào `cot` field trong response để tính điểm P3.

---

## 6. Kế hoạch thực hiện (Gợi ý)

### Tuần 1 (17/05 → 23/05): Data & Foundation

- [ ] EDA bổ sung trên dataset 15/05 — phân tích domain, độ khó, phân bố answer
- [ ] Pipeline làm sạch & chuẩn hóa dataset
- [ ] Sinh CoT + Answer chất lượng cao bằng LLM thương mại
- [ ] Cross-check tự động bằng SymPy
- [ ] Xây dựng Knowledge Base công thức vật lý

### Tuần 2 (24/05 → 30/05): Model & Pipeline

- [ ] Fine-tune Qwen3.5-4B trên dataset golden
- [ ] Implement pipeline mới trong LangGraph (preprocess → retrieve → generate → execute → verify)
- [ ] Implement PoT (code generation + execution sandbox)
- [ ] Implement SymPy verifier
- [ ] Chuyển từ Ollama sang vLLM serving
- [ ] End-to-end testing trên toàn bộ dataset

### Tuần 3 (31/05 → 01/06): Optimization & Phase 1

- [ ] Benchmark accuracy trên dev set → tìm bottleneck
- [ ] Iterate: thêm data, tune prompt, adjust pipeline
- [ ] **Phase 1 eval: Jun 1-2** — API phải online

### Tuần 4 (03/06 → 07/06): Refinement & Phase 2

- [ ] Phân tích kết quả Phase 1 → fix weakness
- [ ] Model refinement (Jun 3-4)
- [ ] **Phase 2 eval: Jun 5-7** — API phải online
- [ ] Chuẩn bị Data Disclosure Document + Solution Description

---

## 7. Rủi ro & Mitigation

| Rủi ro | Xác suất | Mitigation |
|---|---|---|
| Model tính sai số học | Cao | PoT + SymPy verification — không dựa hoàn toàn vào LLM tính tay |
| Timeout 60s | Trung bình | Giới hạn retry = 1, cache few-shot, optimize prompt length |
| Dataset có answer sai chưa phát hiện | Trung bình | Cross-check toàn bộ bằng SymPy trước khi train |
| Colab disconnect giữa chừng | Trung bình | Checkpoint thường xuyên (`save_steps=50`), dùng A100 cho tốc độ |
| vLLM không tương thích Qwen3.5-4B | Thấp | Qwen family được vLLM hỗ trợ tốt — verify trước khi commit |
| Domain CHLT/DT ít mẫu → accuracy thấp | Trung bình | Data augmentation + synthetic data cho domain yếu |
| Overhead multi-model swapping | Trung bình | Đánh giá xem 1 model mạnh có tốt hơn 2 model yếu không |

---

## 8. Quyết định mở (cần thảo luận thêm)

1. **Ollama vs vLLM:** Codebase hiện tại dùng Ollama. Chuyển sang vLLM ngay hay giữ Ollama dev rồi swap cuối?
2. **Single model vs Multi-model:** Dùng 1 Qwen3.5-4B cho mọi thứ, hay tách router + solver?
3. **PoT vs Direct answer:** Luôn sinh code hay chỉ khi bài khó? (Rule-based routing hay model tự quyết?)
4. **Serving trên Colab:** vLLM + ngrok/Cloudflare tunnel đủ ổn định cho 2 ngày eval không?
5. **Fine-tune strategy:** Full dataset fine-tune hay domain-specific adapter?
6. **Type 1 (Logic):** Tài liệu này chỉ cover Type 2. Type 1 cần chiến lược riêng và cùng chung 1 API endpoint.

---

## Appendix A: Tham chiếu file trong project

| File | Vai trò |
|---|---|
| `EXACT Materials/EXTRACT_Slides.md` | Tóm tắt cuộc thi |
| `EXACT Materials/QA.md` | Q&A chính thức từ BTC — **binding rules** |
| `EXACT Materials/Datasets/.../CHANGELOG_TYPE2.md` | Changelog dataset Type 2 |
| `MODEL_CONTRACT.md` | Interface contract giữa Team Model & Team BE |
| `MLOPS_DIAGRAM.md` | Sơ đồ MLOps pipeline |
| `UNSLOTH_GUIDE.md` | Hướng dẫn fine-tune với Unsloth |
| `DEVELOPMENT.md` | Pattern mở rộng LangGraph pipeline |
| `app/core/pipeline.py` | Pipeline LangGraph hiện tại |
| `app/model/prompts/qa_system.py` | System prompt hiện tại |
| `app/api/schemas.py` | Schema request/response |
| `app/notebooks/01_EDA_Dataset_Physics.ipynb` | EDA notebook (trên data cũ) |

## Appendix B: Benchmark tham khảo Qwen3.5-4B

```
Model              | GPQA   | IFEval | MMLU-Pro | MMLU-Redux | Params
--------------------|--------|--------|----------|------------|-------
Qwen3.5-4B          | 76.2%  | 89.8%  | 79.1%    | 88.8%      | 4B
Qwen2.5-7B-Instruct | 36.4%  | 71.2%  | 56.3%    | 75.4%      | 7B
```

Context Length: 262,144 tokens (native), extensible up to 1,010,000 tokens.
