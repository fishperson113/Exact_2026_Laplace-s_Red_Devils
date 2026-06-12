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
| vLLM BASE + 2 LoRA | 18000 | served-names `base`, `sft` (physics), `qa` (logic stage 2 = v04-QA-CoT) |
| vLLM FOL (composite) | 18001 | served-name `fol`; logic stage 1 (NL->FOL), full finetune da graft |
| gateway (FastAPI) | 9000 | `POST /predict` — BTC goi cai nay |

> **Mac dinh `SERVE_MODE=combined`** (FULL stack ca 2 task type — DUNG CHO SUBMIT, xem muc
> rieng ben duoi). 2 vLLM server tren 1 GPU: :18000 (base Qwen3.5-4B + 2 LoRA adapter
> sft/qa) + :18001 (fol). Mac dinh `RESIDENT_ALL=1` -> ca 2 server awake (base 4B + fol 4B
> = ~8B parallel, BTC §6.3 cho phep) -> KHONG swap, type1 nhanh. Moi vLLM server co
> `/v1/models` rieng cho BTC verify (2 URL: :18000 liet ke base,sft,qa; :18001 liet ke fol).

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
  https://raw.githubusercontent.com/fishperson113/Exact_2026_Laplace-s_Red_Devils/Nguyen/Submission_v02/setup_env.sh
chmod +x setup_env.sh
bash setup_env.sh
```

`setup_env.sh` (idempotent) se: cai vLLM cu13 + deps (qua `uv`, ben net yeu) ->
clone repo -> chay `serve_all.sh` -> in **PUBLIC URLs** `https://xxx.trycloudflare.com/predict` (+ 2 /v1/models)
cho BTC. Doi gi trong setup chi can sua file tren GitHub, may moi tu keo ban moi nhat.

### Cach 2: Chay tay (da SSH vao box CUDA-13)

```bash
ssh -o StrictHostKeyChecking=no -i ~/.ssh/vastai_key -p <PORT> root@<HOST>
export HF_TOKEN=hf_...
curl -fsSL -o setup_env.sh https://raw.githubusercontent.com/fishperson113/Exact_2026_Laplace-s_Red_Devils/Nguyen/Submission_v02/setup_env.sh
bash setup_env.sh
```

### Test

```bash
# tren box (hoac SSH -L 9000:localhost:9000 roi mo tu laptop):
curl -s localhost:9000/health     # {"status":"ok",...}
# vLLM model-info (BTC verify) — moi server 1 cai:
curl -s localhost:18000/v1/models   # ids: base, sft, qa
curl -s localhost:18001/v1/models   # id:  fol
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
- **`SERVE_MODE=combined`** (FULL stack — CA 2 task type, dung cho submit, MAC DINH): :18000
  = base Qwen3.5-4B + 2 LoRA (`sft` physics, `qa` logic-stage2) + :18001 = `fol` (full finetune
  da **graft** sang composite). `RESIDENT_ALL=1` (mac dinh) -> ca 2 awake, ko swap. Xem muc rieng.
- **`SERVE_MODE=physics_ensemble`** (chi Type-2, de test/benchmark): 1 vLLM :18000 = BASE +
  SFT-LoRA, CUDA graphs ON, KHONG swap. Xem muc rieng.
- **`SERVE_MODE=shared`**: 1 con Qwen3.5-4B ~19GB VRAM lo ca 3 role (placeholder `physics-v04`).
- **Expose BTC = 3 URL (BTC §6.3 yeu cau /v1/models cho MOI vLLM server):** `serve_all.sh combined`
  tao 3 cloudflared tunnel -> `submission/urls.txt`: gateway :9000 (`/predict`) + :18000 (`/v1/models`
  = base,sft,qa) + :18001 (`/v1/models` = fol). Gateway cung proxy `/v1/models` gop tat ca (tien).
  URL cloudflared **doi** moi lan restart -> lay urls.txt NGAY truoc grading slot. Fallback rate-limit: reverse-SSH sang VPS:
  ```bash
  ssh -fN -R <VPS_PORT>:localhost:9000 <user>@<vps_ip>
  # BTC goi: http://<vps_ip>:<VPS_PORT>/predict   (mo <VPS_PORT> tren firewall VPS)
  ```

---

## SERVE_MODE=combined — FULL stack ca 2 task type (DUNG CHO SUBMIT)

Mot GPU, **2 vLLM server**. Model set khop `app/logic_solution/config.yaml` (chuan logic).

| vLLM server | Port | Model / adapter | Role | Params |
|---|---|---|---|---|
| base + 2 LoRA | :18000 | base `Qwen/Qwen3.5-4B` + `sft` + `qa` | type2 solver/judge; type1 stage-2 QA | ~4B (+adapter nho) |
| fol | :18001 | `fol-v06-cot-augmented` (graft composite) | type1 stage-1 NL->FOL | ~4B |

- **`sft`** = `Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b` (LoRA, physics).
- **`qa`**  = `Laplaces-Red-Devils/v04-QA-CoT` (LoRA, logic stage-2). Dung CHUNG :18000 voi physics
  -> `qa_base_url` == physics endpoint, gateway chi swap `fol` (neu bat swap).
- **`fol`** = `Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4` (full finetune).

**GRAFT (mau chot):** FOL ship dang text-only `Qwen3_5ForCausalLM` -> vLLM 0.22.1 KHONG serve
duoc. `scripts/graft_text_to_composite.py` ghi de `model.language_model.*` cua finetune len base
composite (giu `model.visual.*`+mtp+config, keys khop 1:1) -> composite hop le. QA la LoRA adapter
-> serve thang tren base (KHONG graft). `serve_all.sh combined` chay tu dong (idempotent ->
`/dev/shm/models/fol-composite`).

```bash
HF_TOKEN=hf_... SERVE_MODE=combined bash scripts/serve_all.sh start
# env tuy chon (mac dinh):
#   BASE_REPO=Qwen/Qwen3.5-4B  SFT_ADAPTER=Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b
#   QA_ADAPTER=Laplaces-Red-Devils/v04-QA-CoT
#   FOL_FT=Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4
#   RESIDENT_ALL=1 (mac dinh: ca 2 awake, ko swap; base 4B + fol 4B = ~8B parallel, BTC §6.3 OK)
#     -> FOL_GPU_RESIDENT=0.40  GPU_UTIL_RESIDENT=0.48 (co-resident tren 32GB)
#   RESIDENT_ALL=0 -> fallback sleep-swap fol theo type (cho GPU nho hon)
#   MAX_LORA_RANK=32 MAX_LORAS=2 (2 adapter sft+qa tren 1 base)
```
Gateway env: `SLEEP_SWAP_ENABLED=0` (resident), VLLM_MODEL=sft/:18000, JUDGE=base/:18000,
FOL=fol/:18001, QA=qa/:18000. Warmup CA 2 type. Da do (RTX 5090 32GB, qua tunnel public):
type2 ~7-9s, type1 ~2-4s, ca 2 <60s; VRAM ~26.7/32GB. Verify: `curl :18000/v1/models` (base,sft,qa)
+ `curl :18001/v1/models` (fol) + `curl :9000/predict -d '{"type":"type1",...}'` / `'{"type":"type2",...}'`.

## SERVE_MODE=physics_ensemble — BASE + SFT-LoRA tren 1 vLLM (chi Type 2, test)

**1 vLLM serve BASE `Qwen/Qwen3.5-4B` + SFT (v07c) lam LoRA adapter** (`--enable-lora
--lora-modules sft=<adapter>`). vLLM 0.22.1 KHONG serve duoc merged (arch `Qwen3_5ForCausalLM`/
`qwen3_5_text`); chi serve composite `Qwen3_5ForConditionalGeneration` = base. Adapter co keys
khop `model.language_model.*` cua base -> LoRA chay ngon. `/v1/models` liet ke ca `base`+`sft`,
~4B tong (1 base + adapter nho) << 8B. **Can transformers 5.10 + vLLM 0.22.1** (tf4.56 fail: ko
biet qwen3_5_text; 2 model composite roi se >8B vi vision tower -> LoRA la dung).

**Bat:**
```bash
SERVE_MODE=physics_ensemble bash scripts/serve_all.sh start
# env tuy chon (mac dinh):
#   BASE_REPO=Qwen/Qwen3.5-4B
#   SFT_ADAPTER=Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b   # ADAPTER, khong phai -merged
#   GPU_UTIL=0.85  MAX_LORA_RANK=16
```
Gateway set `PIPELINE_VERSION=v07_ensemble_vLLM`, `VLLM_MODEL=sft` + `JUDGE_MODEL=base` (cung
:18000). CUDA graphs ON (default mode nay) + serve_all gui 1 warmup /predict.

**Pipeline** (`versions/v07_ensemble_vLLM/pipeline.py`): classify -> BASE.chat_n(K=5) ∥
SFT.chat_n(K=5) (asyncio.gather, **concurrent, vLLM batch chung 10 seq tren 1 engine**) -> exec
het -> **POOL 10 mau vote chung, da so thang** -> BASE viet explanation+CoT cho dap an da chon
(judge BO khoi viec chon vi 3-4/13 < ngau nhien). Het gio -> dung reasoning cua bai chon.

**Ket qua (5090):** val_56 0.875, golden_60 0.733, latency median ~9-11s / max ~23s. Ensemble
KHONG hon single model; golden ORACLE 0.917 / minority-lost 11 -> nut that la SELECTION (data
lever), khong phai voting. Do bang `measure_pool.py` / `investigate_ensemble.py`.

> **VRAM 32GB (5090):** 1 base (~9GB) + KV cache lon (concurrency ~57x). Stop: `serve_all.sh stop`.

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
