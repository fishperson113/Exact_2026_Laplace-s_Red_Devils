# Pipeline logic (SFT + neuro-symbolic hooks)

> **Đổi tên gói:** `logic_pipeline` đã được tách thành `src/services/` + `src/data/` + `src/evaluation/` + `src/models/logic_model/`. Tài liệu dưới đây dùng đường dẫn mới.

## Kiến trúc (ý tưởng)

1. **NL → FOL** (`data/nl_to_fol.py`, `data/prompts.py`): prompt chat để LLM dịch premise NL sang FOL; khi SFT mặc định dùng FOL gold trong dataset.
2. **Solver** (`services/solvers/`): interface `SymbolicSolver` — `NoOpSolver` (mặc định), `Z3SolverIfAvailable` (stub mở rộng Z3/Prover9).
3. **Explanation** (`services/explanation.py`): prompt kết hợp output solver + NL để sinh giải thích (tách khỏi nhãn SFT).
4. **Data** (`data/splitting.py`, `data/dataset.py`, `services/drive.py`): flatten 808 câu, split 8:1:1 theo `record_id`, CSV + `DatasetDict` có `text`, `eval_prompt`, `gold_answer`.
5. **Metrics** (`evaluation/metrics.py`): nhãn **chỉ** được `A`/`B`/`C`/`D`/`Yes`/`No`/`Unknown` (đúng JSON). Lúc load data gọi `require_answer_label` — sai nhãn → `ValueError`. Output model phải trích ra đúng một trong 7 chuỗi đó (sau `Answer:` hoặc dòng đầu), không thì raise.
6. **Train** (`models/logic_model/train.py`, `trainer_accuracy.py`): LoRA + TRL `SFTTrainer`; **`metric_for_best_model=eval_accuracy`**, `greater_is_better=True` — checkpoint tốt nhất theo đúng/sai trắc nghiệm trên **dev** (explanation vẫn trong target SFT nhưng không dùng để chọn model). `test_accuracy.json` sau khi chạy stage train.

## Cấu hình

- `services/config.py` — `LogicSFTConfig` + **`LogicSFTConfig.from_env()`** đọc biến từ `.env`.
- **`.env.example`** — mẫu đầy đủ: `LOGIC_MODEL_NAME`, `LOGIC_REPO_*`, `HF_TOKEN`, … Sao chép thành **`.env`** (file này đã nằm trong `.gitignore` của repo). Cài **`python-dotenv`** để bootstrap tự nạp `.env`.
- **Tên repo Hugging Face** (khi không set `LOGIC_HF_REPO_ID`):
  `{LOGIC_HF_ORG}/logic-{LOGIC_REPO_VERSION}-{LOGIC_REPO_METHOD}-{slug}`
  - Ví dụ: `Laplaces-Red-Devils/logic-v01-fewshot-qwen3.5-4` với model `Qwen/Qwen3.5-4B`, method `fewshot`, version `v01`.
  - `slug` mặc định suy từ `LOGIC_MODEL_NAME`, hoặc ghi đè bằng `LOGIC_REPO_MODEL_SLUG`.

## Chạy trong notebook

1. Cài dependency (`trl`, `transformers`, `peft`, `python-dotenv`, …).
2. `%run -i project_bootstrap.py` (nạp `.env` nếu có).
3. `from services.config import LogicSFTConfig` rồi `cfg = LogicSFTConfig.from_env()` — có thể thêm tham số Python để ghi đè (vd. `LogicSFTConfig.from_env(data_source="local")`).
4. Nếu `cfg.data_source == "drive"`: chạy cell tải Drive (`logic_model_stage_drive.py`).
5. Fine-tune: `%run -i logic_model_stage_train.py`
6. (Tuỳ chọn) Push HF: `%run -i logic_model_stage_push.py` — `LOGIC_PUSH_TO_HUB=true` trong `.env` và token `HF_TOKEN` (hoặc `HF_Token` từ notebook Kaggle).

## Fine-tune / tối ưu accuracy

- **Loss** vẫn được log; **chọn checkpoint** dựa trên **`eval_accuracy`** (greedy generate trên `eval_prompt`, so khớp `gold_answer`).
- Chỉnh prompt SFT trong `data/prompts.py` (`SYSTEM_PROMPT_SFT`, `USER_TEMPLATE_SFT`, …).
- Giảm thời gian eval: `cfg.eval_accuracy_max_samples = 50` (ví dụ); full dev bỏ `None`.
- Sau train, `output/pipeline_sft/test_accuracy.json` báo accuracy trên **test** (cùng parser nhãn).

## Mở rộng neuro-symbolic

- Cài engine (vd. `z3-solver`), triển khai `prove_or_model` trong `services/solvers/z3_solver.py`.
- Ở inference: gọi `build_nl_to_fol_messages` → LLM → `solver.prove_or_model` → `build_explain_from_solver_messages` → LLM.
