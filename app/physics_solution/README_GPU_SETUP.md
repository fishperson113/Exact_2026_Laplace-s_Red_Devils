# GPU Server Setup Guide

> **Ctrl+H** thay `<HOST>` va `<PORT>` bang IP va port thuc te cua server.

---

## Quick Start — SUBMISSION STACK (1 endpoint /ask, ca 2 task type, Qwen3.5-4B)

> **MOT** endpoint `POST /ask` cho ca 2 task type, route theo shape request:
> co `premises-NL` -> Type 1 (logic FOL+QA); chi co `question` -> Type 2
> (physics code-exec). Dung template **"NVIDIA CUDA Development Environment"**
> (bare, tu cai vLLM). **BAT BUOC** driver host CUDA 13 (>=580) — xem ben duoi.

| Thanh phan | Port | Ghi chu |
|---|---|---|
| vLLM (Qwen3.5-4B) | 18000 | GDN-hybrid; vLLM co kernel GDN/conv1d **san** -> KHONG can fla/conv1d/transformers de serve |
| gateway (FastAPI) | 9000 | `POST /ask` — BTC goi cai nay |

> **Vi sao BAT BUOC CUDA 13 / driver >=580:** model la `Qwen3_5ForConditionalGeneration`,
> chi vLLM moi (>=0.21) nhan dien, ma ban do build tren **torch CUDA 13** (can driver
> >=580). Driver 565/535 -> `torch.cuda.is_available()=False`. Khi rent Vast, chon host
> hien **CUDA Version 13.x**. (Da test OK: RTX 3090, driver 595/CUDA13.2, vLLM 0.22.1.)

### Cach 1 (KHUYEN DUNG): Custom template + On-start curl `setup_env.sh`

1. Tao **custom template** tu "NVIDIA CUDA Development Environment".
2. Them **Environment Variable**: `HF_TOKEN=hf_...` (de tai model gated). Cac "num" khac (`SERVE_MODE`, `SKIP_TUNNEL`, `FOL_REPO`...) cung
   set qua env Vast duoc — `setup_env.sh`/`serve_all.sh` deu doc.
3. O o **On-start Script**, dan 3 dong:

```bash
curl -fsSL -o setup_env.sh \
  https://raw.githubusercontent.com/fishperson113/Exact_2026_Laplace-s_Red_Devils/Nguyen/submition_v1/setup_env.sh
chmod +x setup_env.sh
bash setup_env.sh
```

`setup_env.sh` (idempotent) se: cai vLLM cu13 + deps (qua `uv`, ben net yeu) ->
clone repo -> chay `serve_all.sh` -> in **PUBLIC URL** `https://xxx.trycloudflare.com/ask`
cho BTC. Doi gi trong setup chi can sua file tren GitHub, may moi tu keo ban moi nhat.

### Cach 2: Chay tay (da SSH vao box CUDA-13)

```bash
ssh -o StrictHostKeyChecking=no -i ~/.ssh/vastai_key -p <PORT> root@<HOST>
export HF_TOKEN=hf_...
curl -fsSL -o setup_env.sh https://raw.githubusercontent.com/fishperson113/Exact_2026_Laplace-s_Red_Devils/Nguyen/submition_v1/setup_env.sh
bash setup_env.sh
```

### Test

```bash
# tren box (hoac SSH -L 9000:localhost:9000 roi mo tu laptop):
curl -s localhost:9000/health     # {"status":"ok",...}
# Type 2 (physics):
curl -s -X POST localhost:9000/ask -H "Content-Type: application/json" \
  -d '{"question":"A 2 uF capacitor charged to 12 V stores how much energy?"}'
# Type 1 (logic):
curl -s -X POST localhost:9000/ask -H "Content-Type: application/json" \
  -d '{"premises-NL":["All men are mortal.","Socrates is a man."],"question":"Is Socrates mortal? Yes or No."}'
```

### Ghi chu quan trong

- **Luc serve, model nam o VRAM** (khong phai /dev/shm). HF cache mac dinh `/dev/shm`
  (RAM) cho load nhanh; de disk cung chay y het, chi cham lan load dau. shm bi cap =
  container_RAM/2 — muon to hon thi set `--shm-size` trong custom template.
- **Mac dinh `SERVE_MODE=shared`**: 1 con Qwen3.5-4B ~19GB VRAM lo ca 3 role (vi 2 model
  logic Qwen3.5-4B that chua upload — `physics-v04` lam placeholder). Vua 24GB.
- **Khi co 3 model finetune rieng** -> dung `SERVE_MODE=triple` (sleep-mode swap) o duoi.
- **Expose BTC:** `setup_env.sh` tu bat cloudflared -> in public `/ask` URL. URL **doi**
  moi lan tunnel restart. Neu IP host (xai chung) bi cloudflared rate-limit, fallback
  reverse-SSH cong FastAPI sang VPS rieng:
  ```bash
  ssh -fN -R <VPS_PORT>:localhost:9000 <user>@<vps_ip>
  # BTC goi: http://<vps_ip>:<VPS_PORT>/ask   (mo <VPS_PORT> tren firewall VPS)
  ```

---

## SERVE_MODE=triple — 3 model rieng + sleep-mode swap

3 model Qwen3.5-4B khac nhau (fol, qa, physics) **khong nam cung luc tren 24GB**
(3 x ~9.3GB = ~28GB). Giai phap: moi vLLM chay voi `--enable-sleep-mode`
(+ `VLLM_SERVER_DEV_MODE=1`), gateway **danh thuc** nhom can dung va **ru ngu** nhom con
lai theo tung request. Weights luc ngu nam o **RAM process binh thuong** (full container
RAM, KHONG phai /dev/shm).

- Nhom thuc: `logic = {fol, qa}` (ca 2 thuc cung luc cho buoc FOL roi QA) | `physics = {physics}`.
- Doi nhom chi xay ra khi **task type doi** (~vai giay: ru ngu nhom cu, danh thuc nhom moi).
  O concurrency 1 (dieu kien thi) la an toan.

**Bat:** set env (qua Vast template env hoac truoc khi chay):
```bash
SERVE_MODE=triple
FOL_REPO=Laplaces-Red-Devils/<fol-qwen3.5-4b>
QA_REPO=Laplaces-Red-Devils/<qa-qwen3.5-4b>
PHYSICS_REPO=Laplaces-Red-Devils/<physics-qwen3.5-4b>
# (chua co model that thi bo trong -> ca 3 mac dinh = physics-v04 de test co che)
```
`serve_all.sh` se: start fol (:18001) -> ngu, start qa (:18002) -> ngu, start physics
(:18000) -> ngu (tuan tu + ngu-sau-khi-load de may sau co du VRAM); roi gateway tu
wake/sleep. VRAM luc nao cung ~20GB (1 nhom thuc). Da test OK tren 3090 24GB:
physics-only ~20.7GB, fol+qa ~20.6GB.

> Util mac dinh: `PHYSICS_GPU=0.85` (thuc 1 minh), `FOL_GPU=0.45` + `QA_GPU=0.45`
> (thuc cung luc ~0.9). Chinh qua env neu can.

Cach khac (neu khong muon swap): **8-bit** ca 3 (~15GB, nam cung luc 24GB) hoac **GPU >=40GB**.

---

## Quan ly + Troubleshooting

```bash
cd /workspace/project
bash scripts/serve_all.sh status   # health vllm + gateway
bash scripts/serve_all.sh stop     # tat het (kill ca GPU worker + cloudflared)
SKIP_TUNNEL=1 bash scripts/serve_all.sh start    # bat lai, khong mo tunnel
```

**Batch eval tu local** (qua SSH tunnel `-L 9000:localhost:9000`):
```bash
python -m app.physics_solution.cli.eval_api \
    --api-url http://localhost:9000 \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --concurrency 1 --limit 10     # --concurrency 1 = mo phong dieu kien thi
```

| Van de | Nguyen nhan | Giai phap |
|---|---|---|
| `torch.cuda.is_available()=False` | Driver < 580 (CUDA < 13), khong chay duoc torch cu13 | Thue host **CUDA 13.x** (driver >=580) |
| vLLM init `Free memory ... less than ...` | GPU con tien trinh cu giu VRAM (EngineCore orphan) | `serve_all.sh stop` (da kill GPU pid), hoac `nvidia-smi` -> kill pid |
| `/sleep` `/wake_up` 404 | Thieu `VLLM_SERVER_DEV_MODE=1` | serve_all triple mode da set san |
| cloudflared khong ra URL | IP host (xai chung) bi rate-limit | Fallback reverse-SSH sang VPS (xem tren) |
| Model download cham / 401 | Thieu `HF_TOKEN` | Set env `HF_TOKEN=hf_...` |
| OOM khi triple | Util qua cao | Giam `FOL_GPU`/`QA_GPU`/`PHYSICS_GPU` hoac `MAX_MODEL_LEN` |
