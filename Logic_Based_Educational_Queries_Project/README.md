# Logic_Based_Educational_Queries_Project

Dự án EXACT 2026 — **Logic Based Educational Queries**: EDA / tiền xử lý, fine-tune LoRA (SFT), đánh giá theo **accuracy** trên dev, inference.

Cấu trúc bám **Cookiecutter Data Science**: mã Python trong `src/` với `data` (CSV, split, prompts, HF dataset), `evaluation` (nhãn / accuracy / đọc JSON sau train), `models/logic_model` (SFT trắc nghiệm + trainer), `models/fol_model` (SFT NL→premises-FOL), `visualization`, và `services` (cấu hình chung, Hub, Drive, solver, giải thích sau train).

---

## Cây thư mục

```text
Logic_Based_Educational_Queries_Project/
├── LICENSE
├── README.md                 # Tài liệu này
├── Makefile                  # make data | validate | train | ...
├── requirements.txt
├── setup.py                  # pip install -e .
├── .env                      # Secrets (KHÔNG commit) — cùng cấp với configs/
├── .env.example              # Mẫu biến môi trường
├── configs/
│   ├── logic_model.yaml      # Tham khảo siêu tham số MCQ / logic SFT (ưu tiên .env)
│   └── fol_model.yaml        # Tham khảo FOL SFT (biến FOL_*)
├── data/
│   ├── external/
│   ├── interim/              # EDA tạm (vd. logic_flat.csv từ notebook)
│   ├── processed/
│   │   └── logic_sft/       # train.csv, dev.csv, test.csv, split_*.json
│   └── raw/                  # Logic_Based_Educational_Queries.json (immutable)
├── docs/
├── models/                   # Checkpoint / adapter export (tuỳ bạn lưu thêm)
├── notebooks/
│   ├── project_bootstrap.py  # %run từ notebook — PYTHONPATH + dotenv
│   ├── logic_model_pipeline_official.ipynb
│   ├── fol_model_pipeline_official.ipynb
│   ├── logic_model_stage_train.py
│   ├── fol_model_stage_train.py
│   ├── logic_model_stage_drive.py
│   ├── fol_model_stage_drive.py
│   ├── logic_model_stage_push.py
│   └── fol_model_stage_push.py
├── references/
├── reports/
│   └── figures/              # Hình EDA từ exploration.ipynb
└── src/
    ├── data/                 # Kỹ thuật dữ liệu: split, prompts, dataset SFT
    │   ├── ingestion.py
    │   ├── cleaning.py
    │   ├── splitting.py      # flatten + export logic_sft (CSV + metadata)
    │   ├── prompts.py
    │   ├── nl_to_fol.py
    │   ├── dataset.py
    │   └── validation.py
    ├── evaluation/           # Nhãn / accuracy + đọc train_metrics.json, test_accuracy.json
    │   ├── metrics.py
    │   └── json_logs.py
    ├── services/             # Config, Hub, Drive, solvers, explanation (hậu train)
    ├── models/
    │   ├── logic_model/        # MCQ SFT + eval_accuracy
    │   │   ├── model.py
    │   │   ├── train.py
    │   │   ├── trainer_accuracy.py
    │   │   ├── hyperparameters_tuning.py
    │   │   └── predict.py
    │   └── fol_model/          # NL → premises-FOL SFT
    │       └── train.py
    └── visualization/
        └── exploration.ipynb # EDA + export logic_sft (thay exploration.py)
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

   - `LOGIC_SFT_PROCESSED_DIR` — đường dẫn tuyệt đối tới `data/processed/logic_sft` sau bước export (hoặc để trống nếu chạy từ project root và đã có `data/processed/logic_sft/train.csv` — pipeline sẽ tự tìm).
   - `HF_TOKEN` — nếu bật `LOGIC_PUSH_TO_HUB=true`.

3. Đặt JSON gốc vào `data/raw/` (xem `data/raw/README.md`).

---

## Luồng dữ liệu (ingestion → train)

| Bước | Thành phần | Mô tả |
|------|------------|--------|
| Thu thập | `src/data/ingestion.py` | Định vị / đọc `data/raw/*.json`. |
| Làm sạch | `src/data/cleaning.py` | Giữ chỗ mở rộng (outlier, missing). |
| Nhãn + split | `src/data/splitting.py` | Flatten JSON, `require_answer_label` (qua `evaluation.metrics`), ghi `data/processed/logic_sft/`. |
| Kiểm tra | `src/data/validation.py` | 808 câu + đủ file CSV/metadata. |
| Features / HF | `src/data/dataset.py` | `build_dataset_dict` (chat template HF). |

**EDA / hình ảnh:** mở `src/visualization/exploration.ipynb` (notebook cũ `eda.ipynb` đã chỉnh path theo project). Cell cuối export `logic_sft`.

**CLI nhanh:**

```bash
make data        # export CSV + split_*.json
make validate    # kiểm tra raw + processed
```

---

## Tutorial: Fine-tune (LoRA SFT)

1. Hoàn tất bước **export** (`make data` hoặc chạy cell export trong `exploration.ipynb`).
2. Mở `notebooks/logic_model_pipeline_official.ipynb` (hoặc chạy trên Kaggle sau khi copy project / clone).
3. Thứ tự cell:

   - **Dependency** (cài `requirements.txt` nếu chưa).
   - **HF token** (Kaggle secrets hoặc biến môi trường).
   - Ô bootstrap: tìm gốc repo (`src/services`), gồm `LOGIC_PROJECT_ROOT`, đường `.ipynb`, `cwd`, `/kaggle/input`, `/content`, **Drive Colab** (`/content/drive/MyDrive`); rồi `%run` `project_bootstrap.py` hoặc nạp inline.
   - `cfg = LogicSFTConfig.from_env()` — chỉnh thêm trong cell nếu cần.
   - **Drive** chỉ khi `LOGIC_DATA_SOURCE=drive`.
   - `%run -i logic_model_stage_train.py` — huấn luyện + eval test.

4. Checkpoint tốt nhất theo **`eval_accuracy`** (không dùng `eval_loss`). Output mặc định: `notebooks/output/pipeline_sft/` (khi `notebook_root` trỏ tới `notebooks/` của project).

5. Siêu tham số: chỉnh `.env` hoặc đối chiếu `configs/logic_model.yaml`. Module `models/logic_model/hyperparameters_tuning.py` có thể đọc YAML (cần `pyyaml`).

6. **Log phiên bản / Hub:** sau train, `notebooks/output/.../experiment_log.json` gom siêu tham số (cấu trúc gần `configs/logic_model.yaml`), toàn bộ `trainer_log_history`, và bảng **theo từng epoch**: loss train (log gần nhất), `eval_loss` / `eval_accuracy` trên **dev**, `test_accuracy` trên **test** (có thể tắt bằng `LOGIC_LOG_TEST_EACH_EPOCH=false`). Sau `run_test_eval`, file được bổ sung `test_accuracy` + mẫu inference (`LOGIC_EXPERIMENT_INFERENCE_SAMPLES`). Khi `push_merged_lora`, các file này được đẩy lên Hub trong `experiment_artifacts/`.

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
| `make data` | Export `data/processed/logic_sft/` |
| `make validate` | Kiểm tra raw + processed |
| `make train` | `python -m models.logic_model.train` (cần `.env` + dữ liệu đã export) |
| `make train-fol` | `python -m models.fol_model.train` (FOL SFT; xem `configs/fol_model.yaml` + `FOL_*`) |

---

## Kiến trúc gói

- **`src/data/`**: dữ liệu thô → split CSV, prompt SFT/NL→FOL, `dataset.py` (HF `DatasetDict`).
- **`src/evaluation/`**: `metrics.py` (7 nhãn, parse completion, accuracy), `json_logs.py` (đọc artifact sau train).
- **`src/models/logic_model/`**: huấn luyện MCQ end-to-end (`train.py`, `trainer_accuracy.py`, `build_model`, inference `predict.py`).
- **`src/models/fol_model/`**: SFT sinh `premises_fol` từ `premises_nl` (nhãn JSON; xem `src/data/fol_dataset.py`).
- **`src/services/`**: `LogicSFTConfig`, đặt tên repo HF, push Hub, tải Drive, solver stub, prompt giải thích từ solver — dùng chung sau khi train xong hoặc cho bước neuro-symbolic.

Chi tiết cấu hình và mở rộng: `docs/README_LOGIC_PIPELINE.md` (tài liệu pipeline; tên file giữ nguyên để không gãy link nội bộ).
