# GPU Server Setup Guide

> **Ctrl+H** thay `<HOST>` va `<PORT>` bang IP va port thuc te cua server.

---

## Quick Start — Vast AI vLLM Template (khuyen dung)

### Buoc 1: Tao instance Vast AI

Chon template **vLLM**, GPU **RTX 3090** tro len, cau hinh env vars:

| Env var | Gia tri |
|---|---|
| `VLLM_MODEL` | `Qwen/Qwen3.5-4B` |
| `VLLM_ARGS` | `--max-model-len 4096 --gpu-memory-utilization 0.90 --dtype bfloat16` |
| `PIP_PACKAGES` | *(optional)* `fastapi uvicorn pydantic-settings httpx python-dotenv scipy sympy pandas` |

> **Luu y:** Template se tu download model va start vLLM. Mat ~2-3 phut.
> vLLM chay tren internal port **18000** (external 8000).
> Neu set `PIP_PACKAGES`, deps duoc cai tu dong khi boot — khoi can chay buoc 4.

### Buoc 2: SSH vao server

```bash
ssh -p <PORT> root@<HOST>
```

Verify vLLM da san sang:

```bash
curl -s http://localhost:18000/health
# Ket qua mong doi: (empty = healthy)

curl -s http://localhost:18000/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])"
# Ket qua mong doi: Qwen/Qwen3.5-4B
```

> Neu vLLM chua san sang, kiem tra log: `tail -50 /var/log/vllm.log`
> Neu model sai (vd: Qwen3-8B-FP8), xem muc **Troubleshooting** ben duoi.

### Buoc 3: SCP code len server (terminal local)

```bash
cd D:\Git\Exact_2026_Laplace-s_Red_Devils

# Tao folder truoc
ssh -p <PORT> -o StrictHostKeyChecking=no root@<HOST> "mkdir -p /root/project"

# Upload code
scp -P <PORT> -o StrictHostKeyChecking=no -r app root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no -r scripts root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no pyproject.toml uv.lock .env.example root@<HOST>:/root/project/
```

### Buoc 4: Cai deps + tao .env (tren server)

```bash
# vLLM template da co san: torch, transformers, vllm, numpy, openai, tqdm, pyyaml
# Chi can cai them phan gateway + code execution:
uv pip install --system fastapi "uvicorn[standard]" pydantic-settings \
    httpx python-dotenv scipy sympy pandas

# Tao .env tu example
cp /root/project/.env.example /root/project/.env
```

> **Khong can** `uv sync` hay tao virtualenv — dung system Python cua template.
> Flag `--system` bat uv cai vao system Python thay vi tao venv.

### Buoc 5: Start FastAPI gateway

**Cach A — Dung script (khuyen dung, co cloudflared tunnel):**

```bash
cd /root/project
SKIP_TUNNEL=1 bash scripts/start_server.sh
# Script tu detect model tu vLLM, start gateway tren port 8001
```

**Cach B — Chay truc tiep:**

```bash
cd /root/project
VLLM_MODEL=Qwen/Qwen3.5-4B uvicorn app.main:app \
    --host 0.0.0.0 --port 8001 --workers 1 --loop uvloop
```

> **Quan trong:** Phai truyen `VLLM_MODEL=Qwen/Qwen3.5-4B` vi template co the
> set env var `VLLM_MODEL` khac (vd: `Qwen3-8B-FP8`). Hoac dung `start_server.sh`
> de tu detect.

### Buoc 6: Verify gateway

```bash
# Health check
curl -s http://localhost:8001/health
# Ket qua: {"status":"ok","vllm":"up"}

# Thu 1 cau physics
curl -s -X POST http://localhost:8001/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Calculate the energy stored in a capacitor when C = 100 uF and U = 30 V."}' \
  | python3 -m json.tool
# Ket qua: {"answer":"0.045","unit":"J",...}
```

### Buoc 7: Truy cap tu local

**Cach A — SSH tunnel (don gian, chac chan):**

```bash
# Tren local — mo tunnel
ssh -p <PORT> root@<HOST> -L 8001:localhost:8001

# Sau do mo trinh duyet:
#   http://localhost:8001/docs     ← Swagger UI (test truc quan)
#   http://localhost:8001/health   ← Health check
```

**Cach B — Cloudflared tunnel (share URL cho nguoi khac):**

```bash
# Tren server
cloudflared tunnel --url http://localhost:8001
# Se in ra URL: https://xxx-yyy.trycloudflare.com
# Mo trinh duyet: https://xxx-yyy.trycloudflare.com/docs ← Swagger UI
```

**Cach C — Dung script (gateway + tunnel 1 lenh):**

```bash
cd /root/project
bash scripts/start_server.sh
# Tu dong start gateway + cloudflared tunnel
# Copy URL trycloudflare.com in ra
```

---

## Swagger UI

FastAPI tu tao Swagger UI tai `/docs`. Sau khi truy cap (SSH tunnel hoac cloudflared):

- Mo `http://localhost:8001/docs` (SSH tunnel) hoac `https://xxx.trycloudflare.com/docs`
- Click **POST /ask** → **Try it out**
- Nhap JSON: `{"question": "Tinh luc Coulomb giua 2 dien tich q1=5uC va q2=-3uC cach nhau 8cm trong chan khong."}`
- Click **Execute** → xem ket qua

Cac endpoint co san:

| Method | Path | Mo ta |
|---|---|---|
| GET | `/` | Thong tin API |
| GET | `/health` | Health check (vLLM status) |
| POST | `/ask` | **Physics pipeline** (Task Type 2) |
| POST | `/logic/ask` | Education logic (Task Type 1 — mock) |
| GET | `/logic/health` | Logic track health |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc UI |

---

## Batch evaluation tu local

Sau khi co URL (SSH tunnel hoac cloudflared):

```bash
# Sequential (--concurrency 1): giong dieu kien thi that, do latency/cau
python -m app.physics_solution.cli.eval_api \
    --api-url http://localhost:8001 \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --concurrency 1 \
    --limit 10   # smoke test truoc

# Parallel (--concurrency 8): fast batch eval, GPU luc nao cung ban
python -m app.physics_solution.cli.eval_api \
    --api-url http://localhost:8001 \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --concurrency 8 \
    --out app/physics_solution/versions/v05_best_vLLM/output/results_golden.json
```

| concurrency | Y nghia | Dung khi |
|---|---|---|
| 1 | Tuan tu, 1 request/lan | Benchmark latency, simulate dieu kien thi |
| 4-8 | Song song, GPU luon ban | Fast batch eval tren 3090 (4B model) |
| 8-16 | Song song, GPU luon ban | Fast batch eval tren 4090/5090 |

Output: `results_golden.json` + `results_golden.csv` — cung format voi inference.py.

---

## Doi version pipeline

Mac dinh la `v05_best_vLLM`. De doi (vi du khi v06 ra):

```bash
# Tren server, trong .env hoac truoc lenh uvicorn:
PIPELINE_VERSION=v06_finetune VLLM_MODEL=Qwen/Qwen3.5-4B \
    uvicorn app.main:app --host 0.0.0.0 --port 8001 --workers 1
```

Moi version chi can cung cap `pipeline.py` voi ham:
```python
async def solve(question: str, client, deadline: float) -> dict: ...
```

---

## Cap nhat code tren server

Moi khi thay doi code tren local:

```bash
# Chi SCP nhung folder da thay doi
cd D:\Git\Exact_2026_Laplace-s_Red_Devils
scp -P <PORT> -o StrictHostKeyChecking=no -r app root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no -r scripts root@<HOST>:/root/project/

# Tren server: restart gateway
ps aux | grep 'uvicorn app' | grep -v grep | awk '{print $2}' | xargs -r kill
cd /root/project
VLLM_MODEL=Qwen/Qwen3.5-4B uvicorn app.main:app \
    --host 0.0.0.0 --port 8001 --workers 1 --loop uvloop &
```

---

## LangSmith Tracing (optional)

> **Hien tai:** LangSmith chua duoc tich hop vao vLLM pipeline (v05_best_vLLM).
> `@traceable` decorator chi co trong HF pipeline (v05_best). De enable cho
> vLLM pipeline, can them decorator vao `pipeline.py` va goi `setup_tracing()`
> khi app startup. TODO cho version sau.

Neu muon enable cho cac version HF (v05_best, v05_code_execution):

```bash
# Them vao .env:
LANGSMITH_API_KEY=lsv2_xxx
```

---

## Troubleshooting

| Van de | Nguyen nhan | Giai phap |
|--------|------------|-----------|
| `/ask` tra ve 500 "model does not exist" | Template set `VLLM_MODEL` khac voi model dang serve | Truyen dung model khi start: `VLLM_MODEL=Qwen/Qwen3.5-4B uvicorn ...` Hoac dung `start_server.sh` (tu detect). |
| vLLM EXITED (Triton FP8 error) | Template mac dinh dung FP8 model, RTX 3090 khong ho tro FP8 | Doi `VLLM_MODEL` va `VLLM_ARGS` (bo FP8 args). Hoac chay vLLM thu cong: xem muc **Chay vLLM thu cong** ben duoi. |
| `cloudflared` 429 Too Many Requests | Cloudflare rate limit quick tunnels | Doi 5-10 phut roi thu lai. Hoac dung SSH tunnel thay the. |
| `ModuleNotFoundError: fastapi` | Chua cai deps | `uv pip install --system fastapi "uvicorn[standard]" pydantic-settings httpx python-dotenv scipy sympy pandas` |
| Model download cham | Khong co HF_TOKEN | `export HF_TOKEN=hf_xxx` truoc khi chay |
| OOM tren RTX 3090 | Model qua lon hoac max-model-len qua cao | Giam `--max-model-len 2048` hoac `--gpu-memory-utilization 0.85` |
| Port SSH doi sau reboot | vast.ai cap port moi | Check dashboard vast.ai, cap nhat `<PORT>` |
| SCP `Connection closed` | Port cu / server chua san sang | Check lai port, thu `ssh -p <PORT> root@<HOST> "echo OK"` |

### Chay vLLM thu cong (khi template gap loi)

Neu vLLM cua template crash (vd: FP8 error), stop no va chay thu cong:

```bash
# Stop template's vLLM
supervisorctl stop vllm
echo '' > /etc/vllm-args.conf

# Start manually
nohup vllm serve Qwen/Qwen3.5-4B \
    --dtype bfloat16 \
    --host 127.0.0.1 \
    --port 18000 \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90 \
    --download-dir /workspace/models \
    > /var/log/vllm_manual.log 2>&1 &

# Doi cho model load xong (~1-2 phut)
tail -f /var/log/vllm_manual.log
# Khi thay "Application startup complete." la xong
```

---

## Legacy: HF Inference Mode (v05_code_execution)

> Dung cho cac version HF-based (v01-v05_best) chay **tren server khong co vLLM template**.
> Approach nay can `uv sync` + `causal-conv1d` + HF Transformers.

<details>
<summary>Click de xem huong dan cu</summary>

### Quick Start

```bash
# Tren server
mkdir -p /root/project/app

# Tren local
cd D:\Git\Exact_2026_Laplace-s_Red_Devils
scp -P <PORT> -o StrictHostKeyChecking=no pyproject.toml uv.lock root@<HOST>:/root/project/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution/versions/v05_code_execution root@<HOST>:/root/project/app/physics_solution/versions/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution/shared root@<HOST>:/root/project/app/physics_solution/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution/data root@<HOST>:/root/project/app/physics_solution/
scp -P <PORT> -o StrictHostKeyChecking=no -r app/physics_solution/cli root@<HOST>:/root/project/app/physics_solution/
scp -P <PORT> -o StrictHostKeyChecking=no app/physics_solution/__init__.py app/physics_solution/config.py root@<HOST>:/root/project/app/physics_solution/

# Tren server
cd /root/project
uv sync
source /root/project/.venv/bin/activate
uv pip install --no-build-isolation causal-conv1d

# Chay inference
python -m app.physics_solution.cli.inference \
    --version v05_code_execution \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --limit 10

# Sync output ve local
scp -P <PORT> -o StrictHostKeyChecking=no "root@<HOST>:/root/project/app/physics_solution/versions/v05_code_execution/output/results*" \
    app/physics_solution/versions/v05_code_execution/output/
```

### Script tu dong

```powershell
.\scripts\run_and_pull.ps1 -HostAddr <HOST> -Port <PORT> -Limit 10
```

```bash
bash scripts/run_and_pull.sh <HOST> <PORT> 10
```

</details>
