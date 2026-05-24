# Dữ liệu ngoài (augmentation)

Thư mục này dành cho bản tải **ngoài** repo (không commit dữ liệu lớn).

## MALLS-v0 (Hugging Face)

Dataset gốc: [`yuan-yang/MALLS-v0`](https://huggingface.co/datasets/yuan-yang/MALLS-v0).

### Tải snapshot (CLI)

```bash
huggingface-cli download yuan-yang/MALLS-v0 --repo-type dataset --local-dir data/external/MALLS-v0
```

Hoặc trong Python:

```python
from datasets import load_dataset

ds = load_dataset("yuan-yang/MALLS-v0")
# Lưu parquet / CSV theo nhu cầu vào data/external/MALLS-v0/
```

### Gộp vào pipeline FOL (augmented)

Sau khi có thư mục snapshot, chạy (từ project root, `PYTHONPATH=src`):

```bash
python -m data.merge_malls_augmentation --malls-root data/external/MALLS-v0 --out-dir data/processed/fol_sft_augmented
```

Script sẽ cố đọc các split quen thuộc (`train`/`validation`/`test` hoặc file parquet trong thư mục), map cột chứa NL/FOL nếu tên khớp một phần, **dedup** theo hash nội dung + `record_id`, và ghi `train.csv` / `dev.csv` / `test.csv` cùng schema `logic_sft`.

Đặt huấn luyện:

- `FOL_SFT_PROCESSED_DIR=<đường dẫn tuyệt đối>/data/processed/fol_sft_augmented`
- `FOL_DATA_VARIANT=augmented` (tên repo Hub: `fol-*-augmented-*`).

Nếu schema MALLS khác với heuristic trong script, chỉnh mapping trong `src/data/merge_malls_augmentation.py` cho khớp cột thực tế.
