# GPU Server Setup Guide

> **Ctrl+H** thay `<HOST>` va `<PORT>` bang IP va port thuc te cua server.

---

## Quick Start — SUBMISSION STACK (1 endpoint /predict, ca 2 task type, Qwen3.5-4B)

> **MOT** endpoint `POST /predict` (BTC 2026 Submission Guide) cho ca 2 task type,
> route theo field **`type`**: `type=="type1"` -> logic (FOL+QA); `type=="type2"`
> -> physics (ensemble). Tra ve **JSON LIST** 1 phan tu/query (`{query_id, answer,
> unit, explanation, premises_used, reasoning}`). Endpoint cu `/ask` van con cho tooling.
> Dung template **"NVIDIA CUDA Development Environment"** (bare, tu cai vLLM).
> **BAT BUOC** driver CUDA 13 (>=580) — xem ben duoi.

| Thanh phan | Port | Ghi chu |
|---|---|---|
| vLLM SFT (physics-v07c) | 18000 | served-name `physics`; primary Type-2 solver |
| vLLM BASE (Qwen3.5-4B) | 18004 | served-name `base`; voter #2 **va** judge (chi mode `physics_ensemble`) |
| gateway (FastAPI) | 9000 | `POST /predict` — BTC goi cai nay |

> **Type 2 = ENSEMBLE** (mac dinh `SERVE_MODE=physics_ensemble`, xem muc rieng ben duoi):
> SFT + BASE chay **song song** (2x4B = 8B active, BTC cho phep), self-consistency vote
> moi con, trung thi xong / lech thi BASE lam judge. Moi vLLM co `/v1/models` rieng cho
> BTC verify.

> **Vi sao BAT BUOC CUDA 13 / driver >=580:** model la `Qwen3_5ForConditionalGeneration`,
> chi vLLM moi (>=0.21) nhan dien, ma ban do build tren **torch CUDA 13** (can driver
> >=580). Driver 565/535 -> `torch.cuda.is_available()=False`. Khi rent, chon host
> hien **CUDA Version 13.x**. (Da test OK: RTX 3090, driver 595/CUDA13.2, vLLM 0.22.1.)
> **RTX 5090 = Blackwell (sm_120)**: can torch **cu128** + vLLM du moi ho tro sm_120 +
> kernel GDN Qwen3.5; `setup_env.sh` cai "vllm latest" nen thuong OK — verify ngay bang
> `python -c "import torch;print(torch.cuda.get_device_name(0))"` + 1 request `/predict`.

### Cach 1 (KHUYEN DUNG): Custom template + On-start curl `setup_env.sh`

1. Tao **custom template** tu "NVIDIA CUDA Development Environment".
2. Them **Environment Variable**: `HF_TOKEN=hf_...` (de tai model gated). Cac "num" khac (`SERVE_MODE`, `SKIP_TUNNEL`, `FOL_REPO`...) cung
   set qua env Vast duoc — `setup_env.sh`/`serve_all.sh` deu doc.
3. **On-start Script**, dan 3 dong:

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
# vLLM model-info (BTC verify) — moi server 1 cai:
curl -s localhost:18000/v1/models   # id: "physics"
curl -s localhost:18004/v1/models   # id: "base"
# Type 2 (physics) — BTC /predict schema:
curl -s -X POST localhost:9000/predict -H "Content-Type: application/json" -d '{
  "query_id":"T2_0001","type":"type2",
  "query":"A 2 uF capacitor charged to 12 V stores how much energy?",
  "premises":[],"options":[]}'
# -> [{"query_id":"T2_0001","answer":"...","unit":"J","explanation":"...",
#      "premises_used":[],"reasoning":{"type":"cot","steps":[...]}}]
# Type 1 (logic):
curl -s -X POST localhost:9000/predict -H "Content-Type: application/json" -d '{
  "query_id":"T1_0001","type":"type1","query":"Is Socrates mortal?",
  "premises":["All men are mortal.","Socrates is a man."],"options":["Yes","No","Uncertain"]}'
```

### Ghi chu quan trong

- **Luc serve, model nam o VRAM** (khong phai /dev/shm). HF cache mac dinh `/dev/shm`
  (RAM) cho load nhanh; de disk cung chay y het, chi cham lan load dau. shm bi cap =
  container_RAM/2 — muon to hon thi set `--shm-size` trong custom template.
- **`SERVE_MODE=physics_ensemble`** (Type-2 hien tai): SFT(:18000) + BASE(:18004) **resident
  song song**, `--gpu-memory-utilization 0.45` moi con (~29GB tren 32GB), KHONG sleep-swap.
  Xem muc rieng ben duoi. Type-1 tam route qua SFT endpoint (chinh sau).
- **`SERVE_MODE=shared`**: 1 con Qwen3.5-4B ~19GB VRAM lo ca 3 role (placeholder `physics-v04`).
- **Khi co 3 model finetune rieng** -> dung `SERVE_MODE=triple` (sleep-mode swap) o duoi.
- **Expose BTC:** `setup_env.sh` tu bat cloudflared -> in public `/ask` URL. URL **doi**
  moi lan tunnel restart. Neu IP host (xai chung) bi cloudflared rate-limit, fallback
  reverse-SSH cong FastAPI sang VPS rieng:
  ```bash
  ssh -fN -R <VPS_PORT>:localhost:9000 <user>@<vps_ip>
  # BTC goi: http://<vps_ip>:<VPS_PORT>/ask   (mo <VPS_PORT> tren firewall VPS)
  ```

---

## SERVE_MODE=physics_ensemble — SFT + BASE song song (Type 2 hien tai)

Hai model 4B nam **cung luc** tren 1 GPU (2x4B = 8B active, BTC cho phep — Q3): SFT la
solver chinh, BASE la voter #2 **va** judge. KHONG sleep-swap (chay song song de toi uu
deadline 60s: wall-time ≈ max(2 con) chu khong phai tong).

**Bat:**
```bash
SERVE_MODE=physics_ensemble bash scripts/serve_all.sh start
# env tuy chon (mac dinh):
#   SFT_REPO=Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged   # :18000 served "physics"
#   BASE_REPO=Qwen/Qwen3.5-4B                                          # :18004 served "base"
#   SFT_GPU=0.45  BASE_GPU=0.45  ENS_BASE_PORT=18004
```
`serve_all.sh` start SFT (:18000) roi BASE (:18004), ca 2 resident (KHONG ngu). Gateway
set `PIPELINE_VERSION=v07_ensemble_vLLM`, `VLLM_*`=SFT, `JUDGE_*`=BASE. Moi vLLM co
`/v1/models` rieng (`physics` / `base`) cho BTC verify.

**Pipeline** (`versions/v07_ensemble_vLLM/pipeline.py`): classify -> SFT.chat_n(K=5) ∥
BASE.chat_n(K=5) (asyncio.gather, 2 server song song) -> exec + vote moi con -> trung
(scorer) thi xong / lech thi BASE judge A/B (chi doc text, KHONG chay code, KHONG thay so
phieu) -> explanation+CoT dung tu bai giai da chon (khong ton call). Het gio -> bo judge,
fallback ve vote SFT.

> **VRAM 32GB (5090):** 0.45+0.45 = ~29GB, du headroom. Neu OOM (KV cache chat / seq dai),
> giam `SFT_GPU`/`BASE_GPU` xuong 0.42 hoac `MAX_MODEL_LEN`. Stop: `serve_all.sh stop`
> (da kill ca 2 vLLM + GPU worker).

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
| 5090: `no kernel image` / `sm_120` loi | vLLM/torch cu chua ho tro Blackwell sm_120 | Cai `vllm` ban moi (cu128) — `setup_env.sh` da lay "latest"; check `torch.cuda.get_device_name` |
| ensemble OOM (2 model) | util 0.45+0.45 + seq dai | Giam `SFT_GPU`/`BASE_GPU` (0.42) hoac `MAX_MODEL_LEN` |
| vLLM init `Free memory ... less than ...` | GPU con tien trinh cu giu VRAM (EngineCore orphan) | `serve_all.sh stop` (da kill GPU pid), hoac `nvidia-smi` -> kill pid |
| `/sleep` `/wake_up` 404 | Thieu `VLLM_SERVER_DEV_MODE=1` | serve_all triple mode da set san |
| cloudflared khong ra URL | IP host (xai chung) bi rate-limit | Fallback reverse-SSH sang VPS (xem tren) |
| Model download cham / 401 | Thieu `HF_TOKEN` | Set env `HF_TOKEN=hf_...` |
| OOM khi triple | Util qua cao | Giam `FOL_GPU`/`QA_GPU`/`PHYSICS_GPU` hoac `MAX_MODEL_LEN` |
