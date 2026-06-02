# Dữ liệu ngoài (`data/external`)

Thư mục này dùng để **tải và lưu snapshot dataset bên ngoài** (không commit dữ liệu lớn lên Git). Đường dẫn gốc trên máy bạn:

`E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\external`

Các lệnh dưới đây giả định bạn đang mở terminal tại **thư mục gốc project** (cùng cấp với `README.md` của repo), tức:

`E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project`

---

## 1. Chuẩn bị

- Cài [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) (hoặc dùng `pip install huggingface_hub` rồi dùng `huggingface-cli`).
- Đăng nhập (nếu dataset yêu cầu quyền):
  ```bash
  huggingface-cli login
  ```

---

## 2. MALLS-v0 — tải vào `data/external/MALLS-v0`

Dataset: `[yuan-yang/MALLS-v0](https://huggingface.co/datasets/yuan-yang/MALLS-v0)`.

### Cách A: `huggingface-cli` (khuyến nghị)

Từ thư mục gốc project:

```bash
huggingface-cli download yuan-yang/MALLS-v0 --repo-type dataset --local-dir "E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\external\MALLS-v0"
```

Hoặc dùng đường dẫn tương đối (vẫn trỏ vào cùng thư mục `data\external`):

```bash
huggingface-cli download yuan-yang/MALLS-v0 --repo-type dataset --local-dir data/external/MALLS-v0
```

Sau khi chạy xong, bạn sẽ có ví dụ:

`E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\external\MALLS-v0\`

### Cách B: Python (`datasets`)

Trong Python (hoặc notebook), có thể tải và lưu local:

```python
from pathlib import Path
from datasets import load_dataset

root = Path(r"E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\external\MALLS-v0")
root.mkdir(parents=True, exist_ok=True)

ds = load_dataset("yuan-yang/MALLS-v0")
# Ví dụ lưu parquet theo split (tuỳ schema thực tế của dataset)
for split in ds:
    ds[split].to_parquet(root / f"{split}.parquet")
```

(Tên file / split có thể khác tùy phiên bản dataset; mở `ds` trong REPL để xem `ds.keys()`.)

---

## 3. Gộp MALLS vào pipeline FOL (CSV augmented)

Sau khi đã có thư mục snapshot (ví dụ `...\data\external\MALLS-v0`), từ thư mục gốc project, với `PYTHONPATH=src`:

```bash
set PYTHONPATH=src
python -m data.merge_malls_augmentation --malls-root "E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\external\MALLS-v0" --out-dir "E:\exact_2026\Exact_2026_Laplace-s_Red_Devils\Logic_Based_Educational_Queries_Project\data\processed\fol_sft_augmented"
```

Trên Git Bash / WSL có thể dùng dạng Unix:

```bash
PYTHONPATH=src python -m data.merge_malls_augmentation \
  --malls-root "E:/exact_2026/Exact_2026_Laplace-s_Red_Devils/Logic_Based_Educational_Queries_Project/data/external/MALLS-v0" \
  --out-dir "E:/exact_2026/Exact_2026_Laplace-s_Red_Devils/Logic_Based_Educational_Queries_Project/data/processed/fol_sft_augmented"
```

Khi train FOL trên bản augmented, trong `.env` (hoặc biến môi trường) đặt:

- `FOL_SFT_PROCESSED_DIR` trỏ tới thư mục `fol_sft_augmented` vừa tạo.
- `FOL_DATA_VARIANT=augmented` (tên repo Hub dạng `fol-*-augmented-*`).

---

## 4. Git

Thư mục con như `MALLS-v0/` thường **rất lớn** — nên thêm vào `.gitignore` (ví dụ `data/external/MALLS-v0/`) để không commit nhầm. Chỉ commit file `README.md` này nếu bạn muốn giữ hướng dẫn trong repo.