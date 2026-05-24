# Pipeline logic (SFT + neuro-symbolic hooks)

> **Đổi tên gói:** `logic_pipeline` đã được tách thành `src/services/` + `src/data/` + `src/evaluation/` + `src/models/logic_model/`. Tài liệu dưới đây dùng đường dẫn mới.

## Kiến trúc (ý tưởng)

1. **NL → FOL** (`data/nl_to_fol.py`, `data/prompts.py`): prompt chat để LLM dịch premise NL sang FOL; khi SFT mặc định dùng FOL gold trong dataset.
2. **Data** (`data/splitting.py`, `data/dataset.py`, `services/drive.py`): flatten 808 câu, split 8:1:1 theo `record_id`, CSV + `DatasetDict` có `text`, `eval_prompt`, `gold_answer`.
3. **Metrics** (`evaluation/metrics.py`): nhãn **chỉ** được `A`/`B`/`C`/`D`/`Yes`/`No`/`Unknown` (đúng JSON). Lúc load data gọi `require_answer_label` — sai nhãn → `ValueError`. Output model phải trích ra đúng một trong 7 chuỗi đó (sau `Answer:` hoặc dòng đầu), không thì raise.
4. **Train** (`models/logic_model/train.py`, `trainer_accuracy.py`): LoRA + TRL `SFTTrainer`; **`metric_for_best_model=eval_accuracy`**, `greater_is_better=True` — checkpoint tốt nhất theo đúng/sai trắc nghiệm trên **dev** (explanation vẫn trong target SFT nhưng không dùng để chọn model). `test_accuracy.json` sau khi gọi `run_training` / `run_test_eval` trong notebook.

## Cấu hình

- `services/config.py` — `LogicSFTConfig` + **`LogicSFTConfig.from_env()`** đọc biến từ `.env`.
- **`.env.example`** — mẫu đầy đủ: `LOGIC_MODEL_NAME`, `LOGIC_REPO_*`, `HF_TOKEN`, … Sao chép thành **`.env`** (file này đã nằm trong `.gitignore` của repo). Cài **`python-dotenv`** để bootstrap tự nạp `.env`.
- **Tên repo Hugging Face** (khi không set `LOGIC_HF_REPO_ID`):
  `{LOGIC_HF_ORG}/logic-{LOGIC_REPO_VERSION}-{LOGIC_REPO_METHOD}-{slug}`
  - Ví dụ: `Laplaces-Red-Devils/logic-v01-fewshot-qwen3.5-4` với model `Qwen/Qwen3.5-4B`, method `fewshot`, version `v01`.
  - `slug` mặc định suy từ `LOGIC_MODEL_NAME`, hoặc ghi đè bằng `LOGIC_REPO_MODEL_SLUG`.

## Chạy trong notebook

1. Cài dependency (`trl`, `transformers`, `peft`, `python-dotenv`, …).
2. Chạy ô bootstrap trong `*_pipeline_official.ipynb` (tự tìm repo: Colab `/content` + Drive, Kaggle Input, `LOGIC_PROJECT_ROOT`, … rồi nạp `.env`).
3. `from services.config import LogicSFTConfig` rồi `cfg = LogicSFTConfig.from_env()` — có thể thêm tham số Python để ghi đè (vd. `LogicSFTConfig.from_env(data_source="local")`).
4. Nếu `cfg.data_source == "drive"`: chạy cell tải Drive (`download_and_extract_from_drive(cfg)` trong `logic_model_pipeline_official.ipynb`).
5. Fine-tune: trong notebook gọi `run_training(cfg)` rồi `run_test_eval(cfg, trainer, dataset_dict)` (xem cell tương ứng).
6. (Tuỳ chọn) Push HF: `push_merged_lora(cfg, token)` khi `LOGIC_PUSH_TO_HUB=true` và có `HF_TOKEN` / `HF_Token` (Kaggle secrets).

## Fine-tune / tối ưu accuracy

- **Loss** vẫn được log; **chọn checkpoint** dựa trên **`eval_accuracy`** (greedy generate trên `eval_prompt`, so khớp `gold_answer`).
- Chỉnh prompt SFT trong `data/prompts.py` (`SYSTEM_PROMPT_SFT`, `USER_TEMPLATE_SFT`, …).
- Giảm thời gian eval: `cfg.eval_accuracy_max_samples = 50` (ví dụ); full dev bỏ `None`.
- Sau train, `output/pipeline_sft/test_accuracy.json` báo accuracy trên **test** (cùng parser nhãn).

## Mở rộng neuro-symbolic (tuỳ chọn)

- Cài engine (vd. `z3-solver`), thêm module riêng (vd. `services/symbolic_solver.py`) và prompt LLM nếu cần giải thích từ output engine.
- Luồng gợi ý: `build_nl_to_fol_messages` → LLM → solver → LLM giải thích.
