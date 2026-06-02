# Vast AI bring-up notes — v06 Phase 2 (errors + fixes)

Log of issues hit bringing up a Vast box for Phase-2 self-gen on **2026-06-01**, with the
working fixes. Keep for troubleshooting / when switching instances. Box: RTX 3090 24 GB,
128 host CPUs, vLLM template `vllm/vllm-openai:v0.21.0`, ssh `-p 23308 root@151.237.25.234`.

## Issue 1 — template serves the WRONG model and it's FP8
- Template env: `VLLM_MODEL=Qwen/Qwen3-8B-FP8` (not our `Qwen/Qwen3.5-4B`), plus
  `VLLM_ARGS=--kv-cache-dtype turboquant_k8v4 ...`.
- vLLM `EXITED` at boot. RTX 3090 is **Ampere (sm_86) → no FP8** support; the FP8 model +
  turboquant KV cache can't init. (Exactly the README_GPU_SETUP "vLLM EXITED (Triton FP8
  error)" row.)
- **Fix:** stop the template vLLM, serve our model manually in bf16:
  `supervisorctl stop vllm; printf '' > /etc/vllm-args.conf`.

## Issue 2 — `libgomp: Thread creation failed: Resource temporarily unavailable`
- After switching to `Qwen/Qwen3.5-4B --dtype bfloat16`, the model **downloaded + loaded
  fine** (arch `Qwen3_5ForConditionalGeneration`, 8.61 GiB) but the engine crashed at
  thread creation.
- Root cause: cgroup **`pids.max=1536`** and ~**1055 already used** at idle, while the host
  exposes **128 CPUs** → vLLM/OpenMP/torch thread pools try to spawn ~128 threads each and
  blow the PID ceiling. (`ulimit -u` is unlimited; the real cap is the cgroup pids.)
- **Fix:** cap thread envs + skip torch.compile:
  ```bash
  OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8 NUMEXPR_NUM_THREADS=8 \
  TOKENIZERS_PARALLELISM=false \
  nohup vllm serve Qwen/Qwen3.5-4B --dtype bfloat16 --host 127.0.0.1 --port 18000 \
      --max-model-len 4096 --gpu-memory-utilization 0.90 \
      --download-dir /workspace/models --enforce-eager \
      </dev/null >/var/log/vllm_manual.log 2>&1 &
  ```
- ⚠️ **Headroom is tight** (~360 free PIDs). The Phase-2 **execution gate** spawns a Python
  subprocess per generated script (`code_executor`), and numpy/scipy in those children can
  spawn their own OpenMP threads. So **run selfgen with the same thread caps exported** (the
  subprocess inherits the env) and a **modest `--concurrency` (≈8–16)**, e.g.:
  ```bash
  OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  PYTHONPATH=. /usr/bin/python3 -m ...selfgen --limit 20 --concurrency 12
  ```
  If execution still hits "Thread creation failed", the host's `pids.max` is too low for
  concurrent code execution → **switch to an instance with a higher pids limit** (or fewer
  host CPUs visible).

## Issue 3 — selfgen 404s with `Qwen/Qwen3-8B-FP8 does not exist`
- `vllm_client.default_model()` reads env **`VLLM_MODEL`**, which the template sets to the
  stale `Qwen/Qwen3-8B-FP8` while vLLM actually serves `Qwen/Qwen3.5-4B` → every request 404s.
- **Fix:** pass `--model Qwen/Qwen3.5-4B` to selfgen (or `export VLLM_MODEL=Qwen/Qwen3.5-4B`
  in the run shell). This is the README's "template sets VLLM_MODEL differently" gotcha.

## Issue 4 — 400 `maximum context length is 4096 tokens`
- The v05 codegen prompt (system + verbose formula hints + question) is **~2097 tokens**;
  with `max_tokens=2000` that's 4097 > the `--max-model-len 4096` we first set, so a chunk of
  samples 400'd (cost diversity; the harder/longer ones can fail entirely).
- **Fix:** serve with **`--max-model-len 8192`** (Qwen3.5-4B supports up to 40960; 8192 fits
  the 3090's KV cache with the model at 8.6 GiB). Alternatively lower selfgen `--max-tokens`.

## Validation result (subset, 2026-06-01)
- `selfgen --limit 10 --model Qwen/Qwen3.5-4B` → **10/10 solved, 57 trajectories** — code is
  genuinely computed PoT (e.g. LD183 law-of-cosines → 5.568 vs gold 5.5678), not echoes.
- `guards --cap 4` → 57 → **35 kept, 0 spurious, 0 dup, 22 over-cap** (histogram {1:1,2:1,4:8}).
  Pipeline validated on real Qwen output. (Run was under the 4096 limit, hence Issue 4 losses.)
- **teacher** not yet exercised on-server: selfgen solved 10/10 so there was no residual, and
  `DEEPSEEK_API_KEY`/.env isn't on the box yet. (teacher reuses the same verified `verify`
  path + Phase-1's `ds_client`, so low risk.)

## SSH / ops gotchas on vast.ai
- **`pkill -f 'vllm serve'` self-kills the SSH shell** — the remote command string itself
  contains "vllm serve", so `pkill -f` matches its own bash and drops the connection
  (exit 255). Kill by the resolved binary path instead: `pkill -f '/usr/local/bin/vllm'`
  (your launch line uses bare `vllm`, so it won't match), or kill by PID.
- **Detach background jobs fully**: `nohup ... </dev/null >log 2>&1 & disown`. Without
  `</dev/null`, ssh hangs/!returns.
- **vast.ai ssh is flaky** — intermittent exit 255 with only the banner; just retry.
- Python split: vLLM runs in `/venv/main/bin/python`; run our pipeline with
  `/usr/bin/python3` (has openai/numpy/tqdm; we added scipy/sympy/pyyaml/python-dotenv).
- Portal port map: vLLM internal `:18000` → external `:8000`; Jupyter on `:8080`.

## State at end of bring-up
- vLLM `Qwen/Qwen3.5-4B` loaded (GPU ~12 GB used), finishing eager warmup / KV-cache init.
- Code rsynced to `/root/project/app`; deps installed in `/usr/bin/python3`; imports OK.
- Next: confirm `/v1/models` serves, then `selfgen --limit` subset with thread caps.
