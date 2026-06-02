# v05 — Code Execution Pipeline

Per-sample classify-then-solve pipeline dung Qwen 3.5 4B.
Moi cau hoi duoc xu ly doc lap trong gioi han **60 giay** (bao gom ca phan loai va giai).

## Luong chay (Pipeline)

```
Question
  |
  v
[1. Classify] ── classify_question() ──> (domain, answer_type)
  |
  | check timeout
  v
[2. Code Generation] ── LLM sinh Python script
  |
  v
[3. Execute] ── chay script trong subprocess (timeout 10s)
  |
  |── success ──> format answer ──> DONE
  |
  |── fail + con thoi gian ──> [4. Retry] LLM sua code ──> execute lai
  |                                |── success ──> DONE
  |                                |── fail ──> FAILED (khong fallback)
  |
  |── fail + het thoi gian ──> FAILED
  |
  v
Score + ghi ket qua
```

**Khong co fallback**: neu code execution that bai (ca lan retry), cau hoi duoc danh dau `failed`.
Khong goi LLM tra loi truc tiep nhu cac version truoc.

## Timeout

- **60s hard limit** cho moi cau hoi (constant `QUESTION_TIMEOUT_S` trong `run.py`)
- Sau buoc classify, kiem tra con thoi gian khong → neu het thi `timeout`
- Truoc khi retry, kiem tra `deadline` → neu het thi bo qua retry
- Sau khi solve xong, neu tong thoi gian > 60s → danh dau `timeout`
- Code execution subprocess co timeout rieng 10s (`code_executor.py`)

## LangSmith Tracing

Moi cau hoi duoc track trong **1 chain duy nhat** `process_question`:

```
process_question (chain)
  ├── classify_question (goi tu shared/router.py)
  └── solve_with_code (chain)
        ├── LLM generate code
        ├── execute code
        └── [retry neu fail + con thoi gian]
```

## Cac file trong v05

| File | Muc dich |
|------|----------|
| `__init__.py` | Metadata: VERSION_NUM=5, model ID, description |
| `run.py` | **Pipeline chinh** — load model, vong lap xu ly tung cau, ghi output |
| `prompts.py` | Prompt cho classification (re-export tu v04) va code generation |
| `code_executor.py` | Extract code tu LLM output, chay subprocess, parse `FINAL ANSWER` / `UNIT` |
| `formula_kb.py` | Load `input/formulas.yaml`, tra ve formula hints theo domain |
| `input/formulas.yaml` | Knowledge base cong thuc vat ly theo tung domain (LD, DT, TD, ...) |

## Dependencies (shared modules)

| Module | Duoc goi tu | Muc dich |
|--------|-------------|----------|
| `shared/router.py` | `run.py` | `classify_question()` — phan loai cau hoi thanh (domain, answer_type) |
| `shared/model/loader.py` | `run.py` | `load_model()` — load Qwen 3.5 4B len GPU |
| `shared/model/batched_llm.py` | `run.py`, `run.py` (qua `_solve_with_code`) | `HFBatchedLLM` — wrapper goi model generate, `_apply_chat_template_no_think` — render chat messages |
| `shared/eval/scorer.py` | `run.py` | `score()`, `extract()`, `summarise()` — cham diem va tong hop ket qua |
| `shared/prompts/system.py` | `run.py` | `ASSISTANT_PREFIX` — prefix cho assistant response |
| `shared/runtime/tracing.py` | `run.py` | `setup_tracing()`, `@traceable` — ket noi LangSmith |

## Cac domain va answer type

**Domains** (tu router): `LD` (Luc Dien), `DT` (Dong Dien), `TD` (Tu Dien), `CH` (Co Hoc), `NL` (Nhiet Luc), `DDT` (Dao Dong & Song), `THCB` (Tong Hop), `CHLT` (Chat Long & Tinh Hoc)

**Answer types**: `pure_numeric`, `sci_notation`, `yes_no`, `multi_value`, `text_only`, `mixed`

**Code execution eligible**: `pure_numeric`, `sci_notation`, `yes_no`, `multi_value` (ham `should_use_code_execution` trong `prompts.py`)

## Lenh chay

```bash
python -m app.physics_solution.cli.inference \
    --version v05_code_execution \
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \
    --limit 10
```

## Output

- `output/results.json` — full results voi summary + tung row
- `output/results.csv` — bang ket qua de doc

Moi row gom: id, question, gold_answer, completion, is_correct, elapsed_s, va `extra` chua chi tiet (solve_method, generated_code, execution_stdout/stderr, routing info, ...).

`solve_method` co 3 gia tri: `code_execution` (thanh cong), `failed` (code that bai), `timeout` (qua 60s).
