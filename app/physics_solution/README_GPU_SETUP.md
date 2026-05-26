# GPU Server Setup Guide

> **Ctrl+H** thay `<HOST>` va `<PORT>` bang IP va port thuc te cua server.
>
> Server hien tai: `ssh -p <PORT> root@<HOST> -L 8080:localhost:8080`

---

## Quick Start (copy-paste full block)

### Tren server (SSH terminal)

```bash
mkdir -p /root/project/app
```

### Tren local (terminal moi)

**Cach A — Git (khuyen dung)**

```bash
cd /root/project
git clone https://github.com/<org>/Exact_2026_Laplace-s_Red_Devils.git .
```

**Cach B — SCP**

```bash
cd D:\Git\Exact_2026_Laplace-s_Red_Devils
scp -P <PORT> -o StrictHostKeyChecking=no pyproject.toml uv.lock root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution root@<HOST>:/root/project/app/
```

### Tren server (tiep tuc)

```bash
cd /root/project
uv sync
source /root/project/.venv/bin/activate
uv pip install --no-build-isolation causal-conv1d
```

### Chay inference

```bash
cd /root/project
source /root/project/.venv/bin/activate
python -m app.physics_solution.cli.inference \
    --version v05_code_execution \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --limit 10 --batch-size 80
```

### Sync output ve local

```bash
scp -P <PORT> -o StrictHostKeyChecking=no "root@<HOST>:/root/project/app/physics_solution/versions/v05_code_execution/output/results*" app/physics_solution/versions/v05_code_execution/output/
```

---

## Chi tiet tung buoc

### 1. SSH vao server

```bash
ssh -p <PORT> root@<HOST> -L 8080:localhost:8080
```

### 2. Check moi truong co san

Template vast.ai (PyTorch) thuong co san Python 3.12, uv, nvcc, GPU driver.

```bash
python --version && uv --version && nvcc --version && nvidia-smi -L
```

Can thay:
- Python >= 3.12
- uv (bat ky version)
- nvcc (bat ky version)
- GPU name (vd: RTX 3090)

### 3. Upload project

#### Cach A — Git (khuyen dung cho doi nhom)

Tren server:

```bash
cd /root
git clone https://github.com/<org>/Exact_2026_Laplace-s_Red_Devils.git project
```

Lan sau chi can pull:

```bash
cd /root/project && git pull
```

#### Cach B — SCP (khi code chua push len git)

Tren server:

```bash
mkdir -p /root/project/app
```

Tren local:

```bash
cd D:\Git\Exact_2026_Laplace-s_Red_Devils
scp -P <PORT> -o StrictHostKeyChecking=no pyproject.toml uv.lock root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution root@<HOST>:/root/project/app/
```

### 4. Cai dependencies

```bash
cd /root/project
uv sync
```

`uv sync` doc `uv.lock`, tao `.venv`, cai dung versions. Thuong mat < 1 phut.

### 5. Activate venv + cai fast kernels

```bash
source /root/project/.venv/bin/activate
uv pip install --no-build-isolation causal-conv1d
```

> **Tai sao `--no-build-isolation`?**
> `causal-conv1d` la CUDA C++ extension. Khong co flag nay, build process
> tao env rieng va co the link sai CUDA version → loi `undefined symbol`.
> Flag nay bat build dung dung torch da cai trong venv.

Verify:

```bash
python -c "import causal_conv1d; print('causal-conv1d OK')"
python -c "import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpu={torch.cuda.get_device_name(0)}')"
```

### 6. Chay inference

```bash
cd /root/project
source /root/project/.venv/bin/activate

# Smoke test 5 cau
python -m app.physics_solution.cli.inference \
    --version v05_code_execution \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --limit 5 --batch-size 80

# Full run 1352 cau
python -m app.physics_solution.cli.inference \
    --version v05_code_execution \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --out app/physics_solution/versions/v05_code_execution/output/results_golden.json \
    --batch-size 80
```

### 7. Sync output ve local

```bash
scp -P <PORT> -o StrictHostKeyChecking=no "root@<HOST>:/root/project/app/physics_solution/versions/v05_code_execution/output/results*" app/physics_solution/versions/v05_code_execution/output/
```

---

## Quan ly thu vien

### Them thu vien moi

**Tren local:**

```bash
cd D:\Git\Exact_2026_Laplace-s_Red_Devils
uv add <package-name>
```

→ Tu dong cap nhat `pyproject.toml` + `uv.lock`

**Dong bo len server:**

Cach A — Git:
```bash
# Local: commit + push
git add pyproject.toml uv.lock && git commit -m "add <package>" && git push

# Server:
cd /root/project && git pull && uv sync
```

Cach B — SCP:
```bash
# Local:
scp -P <PORT> -o StrictHostKeyChecking=no pyproject.toml uv.lock root@<HOST>:/root/project/

# Server:
cd /root/project && uv sync
```

### Cai nhanh tren server (tam thoi)

```bash
uv add <package-name>
```

> Nho sync `pyproject.toml` + `uv.lock` ve local sau de giu dong bo.

---

## Troubleshooting

| Van de | Nguyen nhan | Giai phap |
|--------|------------|-----------|
| `causal-conv1d` import loi `undefined symbol` | CUDA ABI mismatch | `uv pip install --no-build-isolation causal-conv1d` |
| Model download cham | Khong co HF_TOKEN | `export HF_TOKEN=hf_xxx` truoc khi chay |
| OOM tren RTX 3090 | batch_size qua lon | `--batch-size 32` hoac `--dtype int8` |
| `(main)` chong voi `(exact-2026)` | Template tu activate venv main | Khong sao, `exact-2026` override `main` |
| Port SSH doi sau reboot | vast.ai cap port moi | Check dashboard vast.ai, cap nhat `<PORT>` |
| SCP `Connection closed` | Port cu / server chua san sang | Check lai port, thu `ssh -p <PORT> root@<HOST> "echo OK"` |
