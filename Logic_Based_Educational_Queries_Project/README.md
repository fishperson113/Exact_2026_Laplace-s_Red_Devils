# Logic_Based_Educational_Queries_Project

Dự án EXACT 2026 — **Logic Based Educational Queries**: EDA / tiền xử lý, fine-tune LoRA (SFT), đánh giá theo **accuracy** trên dev, inference.

Cấu trúc bám **Cookiecutter Data Science**: mã Python trong `src/` với `data` (ingestion, CSV trong `processed/`, prompts, HF dataset), `evaluation`, `models/logic_model` và `models/fol_model` (SFT), `services`. EDA và xuất split nằm trong `notebooks/`.

---

## Cây thư mục

```text
Logic_Based_Educational_Queries_Project/          # Gốc repo: cấu hình, dữ liệu, notebook, mã nguồn train/eval
├── LICENSE
├── README.md                 # Tài liệu dự án
├── Makefile                  # make data | validate | train | train-fol | …
├── requirements.txt          # Dependency Python
├── setup.py                  # pip install -e . (gói import từ src/)
├── .env                      # Secrets (không commit) — cùng cấp configs/
├── .env.example              # Mẫu biến môi trường (Logic / FOL / Hub)
├── configs/                  # Cấu hình tĩnh (YAML): tham chiếu siêu tham số; runtime ưu tiên .env
│   ├── logic_model.yaml
│   └── fol_model.yaml
├── data/                     # Dữ liệu theo Cookiecutter: raw → interim → processed (+ external)
│   ├── external/             # Bộ dữ liệu ngoài (vd. MALLS), script/README tải/merge tuỳ dự án
│   ├── interim/              # Kết quả trung gian (EDA, bảng tạm) — có thể tái tạo từ notebook
│   ├── processed/            # train/dev/test.csv + split_*.json — **chung** logic MCQ + FOL (mặc định)
│   └── raw/                  # JSON gốc immutable (Logic_Based_Educational_Queries.json)
├── docs/                     # Tài liệu bổ sung (kiến trúc pipeline, hướng dẫn chi tiết)
├── models/                   # Checkpoint / adapter / artifact huấn luyện (tuỳ bạn lưu; thường gitignore)
├── notebooks/                # EDA, tiền xử lý, pipeline train/eval tương tác (Jupyter)
│   ├── eda_and_preprocessing.ipynb   # EDA + chuẩn hóa + xuất CSV → data/processed/
│   ├── logic_model_pipeline_official.ipynb   # SFT trắc nghiệm + eval + Hub
│   ├── fol_model_pipeline_official.ipynb     # SFT NL→FOL + baseline + Hub
│   ├── fol_quiz_solver.ipynb
│   ├── pipeline_baseline.ipynb
│   └── test.ipynb
├── references/               # Tài liệu tham chiếu (paper, đặc tả bài toán) — không chứa mã train
├── reports/                  # Báo cáo / hình phân tích (ngoài notebook output)
│   └── figures/              # Hình EDA export (đường dẫn mặc định trong eda_and_preprocessing.ipynb)
└── src/                      # Mã Python gói dự án: PYTHONPATH=src khi chạy CLI / notebook
    ├── __init__.py
    ├── data/                 # Đọc/ghi dữ liệu, prompt, build HF Dataset (logic + FOL)
    │   ├── __init__.py
    │   ├── ingestion.py      # export → `data/processed/` (chung logic + FOL)
    │   ├── dataset.py        # đọc processed → DatasetDict chat (MCQ)
    │   ├── fol_dataset.py    # CSV → DatasetDict chat (premises NL → premises FOL)
    │   ├── merge_malls_augmentation.py   # Gộp/augment từ nguồn ngoài (vd. MALLS) → processed
    │   ├── nl_to_fol.py      # Khối FOL trong prompt logic (tuỳ cấu hình)
    │   ├── prompts.py        # System / user template cho SFT
    │   └── validation.py     # Kiểm tra số câu raw + đủ file split processed
    ├── evaluation/           # Nhãn chuẩn, metric accuracy, đọc log JSON sau train
    │   ├── __init__.py
    │   ├── metrics.py        # require_answer_label, trích đáp án từ text model
    │   └── json_logs.py      # Đọc/ghi train_metrics, test_accuracy, …
    ├── services/             # Cấu hình ứng dụng (.env/YAML), Hugging Face Hub, Drive
    │   ├── __init__.py
    │   ├── config.py         # LogicSFTConfig + from_env
    │   ├── config_fol.py     # FolSFTConfig + biến FOL_*
    │   ├── drive.py          # Tải dữ liệu từ Drive khi bật nguồn Drive
    │   ├── hf_repo_naming.py # Quy ước tên repo HF
    │   └── hub_push.py       # Đẩy adapter / artifact lên Hub
    └── models/               # Huấn luyện và đánh giá theo từng bài toán (logic vs FOL)
        ├── logic_model/      # SFT câu hỏi trắc nghiệm / Yes–No: LoRA, eval_accuracy, predict
        │   ├── dataloader.py
        │   ├── experiment_log.py
        │   ├── generation_eval.py
        │   ├── hyperparameters_tuning.py
        │   ├── model.py
        │   ├── predict.py
        │   ├── preprocessing.py
        │   ├── train.py
        │   └── trainer_accuracy.py
        └── fol_model/        # SFT sinh JSON premises_fol; baseline, greedy exact-match, Hub
            ├── experiment_log.py
            ├── fol_preflight.py
            ├── generation_fol_eval.py
            ├── hub_reload_eval.py
            └── train.py
```

---

## Chuẩn bị môi trường

1. Tạo venv và cài dependency:

   ```bash
   cd Logic_Based_Educational_Queries_Project
   python -m venv .venv
   .venv\Scripts\activate          # Windows
   pip install -r requirements.txt
   pip install -e .
   ```

2. Sao chép `.env.example` → `.env` (cùng thư mục với `configs/`), điền ít nhất:

   - `LOGIC_SFT_PROCESSED_DIR` — nếu cần: đường dẫn tuyệt đối tới thư mục chứa `train.csv` (mặc định `.../data/processed/` khi chạy từ gốc repo; có thể trỏ tới bản legacy `.../data/processed/logic_sft`).
   - `HF_TOKEN` — nếu bật `LOGIC_PUSH_TO_HUB=true`.

3. Đặt JSON gốc vào `data/raw/` (xem `data/raw/README.md`).

---

## Luồng dữ liệu (ingestion → train)

| Bước | Thành phần | Mô tả |
|------|------------|--------|
| Thu thập | `src/data/ingestion.py` | Định vị / đọc `data/raw/*.json`. |
| Nhãn + split CSV | `src/data/ingestion.py` | Ghi `data/processed/*.csv` + metadata; notebook dùng `export_from_records(records_norm, …)`; `make data` = `export_from_json_path`. |
| Kiểm tra | `src/data/validation.py` | 808 câu + đủ file CSV/metadata. |
| Features / HF | `src/data/dataset.py` | `build_dataset_dict` (chat template HF). |

**EDA / export:** `notebooks/eda_and_preprocessing.ipynb` — sau ô chuẩn hóa FOL, ô xuất gọi `export_from_records(records_norm, …)`; `make data` dùng `export_from_json_path` (raw chưa qua notebook).

**CLI nhanh:**

```bash
make data        # export CSV + split_*.json
make validate    # kiểm tra raw + processed
```

---

## Tutorial: Fine-tune (LoRA SFT)

1. Hoàn tất **export** (`make data` hoặc cell export trong `notebooks/eda_and_preprocessing.ipynb`).
2. Mở `notebooks/logic_model_pipeline_official.ipynb` (hoặc chạy trên Kaggle sau khi copy project / clone).
3. Thứ tự cell:

   - **Dependency** (`%pip` trong notebook hoặc `requirements.txt`).
   - **HF token** (Kaggle secrets hoặc biến môi trường).
   - Ô bootstrap: tìm gốc repo (`src/services`), `sys.path`, `%cd` vào `notebooks/`.
   - `cfg = LogicSFTConfig.from_env()` — chỉnh thêm trong cell nếu cần.
   - **Drive** chỉ khi `LOGIC_DATA_SOURCE=drive` (gọi `download_and_extract_from_drive` trong cell).
   - **Train:** `run_training(cfg)` rồi `run_test_eval(...)` (xem cell trong `logic_model_pipeline_official.ipynb`).
   - **Push Hub:** `push_merged_lora(cfg, token)` khi `LOGIC_PUSH_TO_HUB=true`.

4. Checkpoint tốt nhất theo **`eval_accuracy`** (không dùng `eval_loss`). Output mặc định: `notebooks/output/pipeline_sft/` (khi `notebook_root` trỏ tới `notebooks/` của project).

5. Siêu tham số: chỉnh `.env` hoặc đối chiếu `configs/logic_model.yaml`. Module `models/logic_model/hyperparameters_tuning.py` có thể đọc YAML (cần `pyyaml`).

6. **Log phiên bản / Hub:** sau train, `notebooks/output/.../experiment_log.json` gom siêu tham số (cấu trúc gần `configs/logic_model.yaml`), toàn bộ `trainer_log_history`, và bảng **theo từng epoch**: loss train (log gần nhất), `eval_loss` / `eval_accuracy` trên **dev**, `test_accuracy` trên **test** (có thể tắt bằng `LOGIC_LOG_TEST_EACH_EPOCH=false`). Sau `run_test_eval`, file được bổ sung `test_accuracy` + mẫu inference (`LOGIC_EXPERIMENT_INFERENCE_SAMPLES`). Khi `push_merged_lora`, các file này được đẩy lên Hub trong `experiment_artifacts/`.

---

## Tutorial: Fine-tune FOL (NL → premises-FOL)

1. Có `train.csv` / `dev.csv` / `test.csv` trong `data/processed/` (cùng bộ cho logic + FOL).
2. Mở `notebooks/fol_model_pipeline_official.ipynb` và chạy **theo thứ tự phase**: bootstrap → cấu hình (`FOL_EVAL_FOL_MAX_SAMPLES=all` nếu muốn eval đủ 3 split sau train; **`FOL_LOAD_IN_8BIT=true`** hoặc `FOL_GPU_PROFILE=8bit` / `kaggle_p100` nếu tràn VRAM — **INT8** bitsandbytes, chính xác hơn NF4) → build dataset + xem prompt → **baseline base model** (`fol_preflight`: 10 infer ngẫu nhiên + full test accuracy/NLL, lưu `fol_preflight_baseline.json`) → **SFT** → **push** (kèm `fol_test_benchmark.json` so sánh trước/sau trên test) → **Hub reload** + 20 mẫu test ngẫu nhiên.
3. CLI tương đương train (không gồm bước Hub reload): `make train-fol` hoặc từ gốc project `PYTHONPATH=src python src/models/fol_model/train.py`.

---

## Tutorial: Inference

Sau khi có thư mục adapter (vd. `notebooks/output/pipeline_sft/final_lora/`):

```python
import sys
from pathlib import Path

ROOT = Path(".../Logic_Based_Educational_Queries_Project").resolve()
sys.path.insert(0, str(ROOT / "src"))

from services.config import LogicSFTConfig
from models.logic_model.predict import generate_answer_text, predict_label

cfg = LogicSFTConfig.from_env()
# Đảm bảo cfg.checkpoint_dir trỏ tới final_lora sau train
text = generate_answer_text(cfg, "YOUR_CHAT_PROMPT_HERE")
label = predict_label(cfg, "YOUR_CHAT_PROMPT_HERE")  # parse Answer: → 1 trong 7 nhãn
```

`predict_label` dùng `extract_answer_from_completion` — completion phải có dạng parse được (xem `src/evaluation/metrics.py`).

---

## Bảo mật

- **Không** commit file `.env` (đã liệt kê trong `.gitignore`).
- Nếu token Hugging Face từng lộ trong lịch sử chat hoặc repo công khai, hãy **thu hồi / tạo lại token** trên Hugging Face.

---

## Makefile tham khảo

| Lệnh | Ý nghĩa |
|------|---------|
| `make install` | `pip install -r requirements.txt` |
| `make data` | Export `data/processed/` |
| `make validate` | Kiểm tra raw + processed |
| `make train` | `python -m models.logic_model.train` (cần `.env` + dữ liệu đã export) |
| `make train-fol` | `python -m models.fol_model.train` (FOL SFT; xem `configs/fol_model.yaml` + `FOL_*`) |

---

## Kiến trúc gói

- **`src/data/`**: dữ liệu thô → split CSV, prompt SFT/NL→FOL, `dataset.py` (HF `DatasetDict`).
- **`src/evaluation/`**: `metrics.py` (7 nhãn, parse completion, accuracy), `json_logs.py` (đọc artifact sau train).
- **`src/models/logic_model/`**: huấn luyện MCQ end-to-end (`train.py`, `trainer_accuracy.py`, `build_model`, inference `predict.py`).
- **`src/models/fol_model/`**: SFT sinh `premises_fol` từ `premises_nl` (nhãn JSON; xem `src/data/fol_dataset.py`).
- **`src/services/`**: `LogicSFTConfig`, đặt tên repo HF, push Hub, tải Drive — dùng chung khi train / đẩy artifact.

Chi tiết cấu hình và mở rộng: `docs/README_LOGIC_PIPELINE.md` (tài liệu pipeline; tên file giữ nguyên để không gãy link nội bộ).
