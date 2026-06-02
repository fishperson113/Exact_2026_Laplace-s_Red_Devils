"""Baseline FOL: base model (chưa LoRA), NLL trên completion, exact-match, inference ngẫu nhiên."""
from __future__ import annotations

import gc
import json
import random
from pathlib import Path
from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from services.config_fol import FolSFTConfig, fol_should_load_in_8bit

from .generation_fol_eval import (
    _normalize_ws,
    _parse_premises_fol_list,
    collect_fol_inference_at_indices,
    fol_exact_match_rate,
)


def load_base_causal_lm_for_fol_eval(cfg: FolSFTConfig):
    """Base weights (không LoRA) để đo baseline trước SFT."""
    if fol_should_load_in_8bit(cfg):
        bnb_config = BitsAndBytesConfig(load_in_8bit=True)
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            quantization_config=bnb_config,
            device_map={"": 0},
            trust_remote_code=cfg.trust_remote_code,
        )
    else:
        dtype = torch.bfloat16 if cfg.bf16 else torch.float16
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            torch_dtype=dtype,
            device_map={"": 0},
            trust_remote_code=cfg.trust_remote_code,
        )
    model.config.use_cache = True
    model.eval()
    return model


@torch.no_grad()
def mean_nll_completion_on_split(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    *,
    max_samples: int | None = None,
) -> dict[str, Any]:
    """Trung bình CE (mean trên token completion) theo từng mẫu rồi macro-average."""
    model.eval()
    device = next(model.parameters()).device
    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    total_i = len(idxs)
    print(f"[FOL NLL] {total_i} mẫu (completion CE) …", flush=True)
    losses: list[float] = []
    for j, i in enumerate(idxs, start=1):
        prompt = ds[i]["eval_prompt"]
        completion = ds[i]["gold_assistant"]
        full = tokenizer(
            prompt + completion,
            return_tensors="pt",
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        prompt_tok = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        input_ids = full["input_ids"].to(device)
        plen = int(prompt_tok["input_ids"].shape[1])
        if input_ids.shape[1] <= plen:
            continue
        labels = input_ids.clone()
        labels[:, :plen] = -100
        out = model(input_ids=input_ids, labels=labels)
        losses.append(float(out.loss.item()))
        if total_i >= 80 and j % max(1, total_i // 10) == 0:
            print(f"[FOL NLL] tiến độ {j}/{total_i}", flush=True)
    mean_loss = sum(losses) / len(losses) if losses else 0.0
    print(f"[FOL NLL] xong — n_examples={len(losses)}", flush=True)
    return {
        "mean_nll_completion": mean_loss,
        "n_examples": len(losses),
        "split_size": n,
    }


def print_fol_prompt_previews(
    dataset_dict,
    tokenizer,
    n: int = 3,
    *,
    unique_eval_prompt: bool = True,
    seed: int = 42,
) -> None:
    """In vài `eval_prompt` (đầy đủ template) từ tập train.

    Nhiều dòng train khác ``record_id``/``q_idx`` (MCQ vs Yes–No) nhưng **cùng premises_nl**;
    bước dịch FOL chỉ đưa premises vào user → ``eval_prompt`` có thể **giống hệt** nhau.
    Mặc định ``unique_eval_prompt=True``: chọn ``n`` dòng có prompt khác nhau (duyệt theo thứ tự).
    """
    _ = tokenizer  # giữ chữ ký API; tokenizer đã dùng khi build dataset
    if n <= 0:
        return
    ds = dataset_dict["train"]
    k = min(n, len(ds))

    def _row_meta(i: int) -> str:
        parts: list[str] = []
        if "record_id" in ds.column_names:
            parts.append(f"record_id={ds[i]['record_id']}")
        if "q_idx" in ds.column_names:
            parts.append(f"q_idx={ds[i]['q_idx']}")
        return " | ".join(parts)

    if unique_eval_prompt:
        seen: set[str] = set()
        idxs: list[int] = []
        for i in range(len(ds)):
            ep = ds[i]["eval_prompt"]
            if ep in seen:
                continue
            seen.add(ep)
            idxs.append(i)
            if len(idxs) >= k:
                break
        if len(idxs) < k:
            rest = [i for i in range(len(ds)) if i not in idxs]
            rng = random.Random(seed)
            rng.shuffle(rest)
            for i in rest:
                idxs.append(i)
                if len(idxs) >= k:
                    break
    else:
        idxs = list(range(k))

    print(f"\n=== Xem trước {len(idxs)} eval_prompt (train) ===\n")
    if (
        unique_eval_prompt
        and len(ds) >= 2
        and ds[0]["eval_prompt"] == ds[1]["eval_prompt"]
    ):
        print(
            "Ghi chú: các dòng đầu train thường trùng eval_prompt (cùng premises NL, khác câu hỏi). "
            "Đang hiển thị các prompt **khác nhau**; đặt unique_eval_prompt=False để xem đúng n dòng đầu.\n"
        )

    for j, i in enumerate(idxs):
        meta = _row_meta(i)
        if meta:
            head = f"--- mẫu {j} (index train={i}, {meta}) ---"
        else:
            head = f"--- mẫu {j} (index train={i}) ---"
        print(head)
        print(ds[i]["eval_prompt"][:6000])
        print()


def print_fol_baseline_infer_row(row: dict[str, Any], *, sample_tag: str | None = None) -> None:
    """In NL + FOL gold/pred từng dòng (Phase 6 baseline)."""
    parts: list[str] = []
    if sample_tag is not None:
        parts.append(sample_tag)
    parts.append(f"idx={row['split_index']}")
    if "record_id" in row:
        parts.append(f"record_id={row['record_id']}")
    if "q_idx" in row:
        parts.append(f"q_idx={row['q_idx']}")
    print("--- " + " | ".join(parts) + " ---\n")

    nl = row.get("premises_nl")
    if isinstance(nl, list) and nl:
        print("### Premises (NL)")
        wn = len(str(len(nl)))
        for k, line in enumerate(nl, 1):
            print(f"{k:{wn}d}. {line}")
        print()
    else:
        print("### Premises (NL)\n(không có trong row — rebuild dataset sau khi pull code mới)\n")

    gold_txt = str(row.get("gold_assistant") or "")
    pred_txt = str(row.get("predicted_raw") or "")

    gold_list = _parse_premises_fol_list(gold_txt)
    if gold_list is None:
        pf = row.get("premises_fol")
        if isinstance(pf, list) and pf:
            gold_list = [_normalize_ws(str(x)) for x in pf]

    pred_list = _parse_premises_fol_list(pred_txt)

    def _block(title: str, lst: list[str] | None, raw: str) -> None:
        print(f"### {title}")
        if lst:
            wg = len(str(len(lst)))
            for k, f in enumerate(lst, 1):
                print(f"{k:{wg}d}. {f}")
        else:
            print("(parse JSON thất bại — raw, tối đa 2500 ký tự)")
            print(raw[:2500].strip() or "(rỗng)")
        print()

    _block("Ground truth (FOL)", gold_list, gold_txt)
    _block("Prediction (FOL)", pred_list, pred_txt)


def run_random_base_inference(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    *,
    n: int,
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    pool = list(range(len(ds)))
    k = min(n, len(pool))
    idxs = rng.sample(pool, k=k) if k < len(pool) else pool
    return collect_fol_inference_at_indices(cfg, model, tokenizer, ds, idxs)


def run_preflight_baseline_and_save(
    cfg: FolSFTConfig,
    tokenizer,
    dataset_dict,
    *,
    random_infer_n: int = 10,
    random_seed: int = 3407,
    preview_rows: int = 3,
) -> dict[str, Any]:
    """
    Base model: in preview prompt, inference ngẫu nhiên, full-test exact-match + mean NLL.
    Ghi `fol_preflight_baseline.json` vào cfg.out_dir.
    """
    assert cfg.out_dir is not None
    print_fol_prompt_previews(dataset_dict, tokenizer, n=preview_rows)
    model = load_base_causal_lm_for_fol_eval(cfg)
    try:
        rnd_rows = run_random_base_inference(
            cfg,
            model,
            tokenizer,
            dataset_dict["train"],
            n=random_infer_n,
            seed=random_seed,
        )
        print(f"\n=== Base model — {len(rnd_rows)} mẫu ngẫu nhiên (train), greedy ===\n")
        for j, row in enumerate(rnd_rows):
            print_fol_baseline_infer_row(row, sample_tag=f"[{j}]")
            print()

        test_ds = dataset_dict["test"]
        acc = fol_exact_match_rate(
            cfg, model, tokenizer, test_ds, max_samples=None, split_label="test_preflight"
        )
        nll = mean_nll_completion_on_split(cfg, model, tokenizer, test_ds, max_samples=None)
        print("=== Base model — FULL test (trước fine-tune) ===")
        print("exact_match:", acc)
        print("nll:", nll)

        doc: dict[str, Any] = {
            "model_name": cfg.model_name,
            "phase": "preflight_base_model",
            "random_train_infer_n": random_infer_n,
            "random_train_infer_seed": random_seed,
            "random_train_samples": rnd_rows,
            "test_exact_match_full": acc,
            "test_mean_nll_completion_full": nll,
        }
        path = cfg.out_dir / "fol_preflight_baseline.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Đã lưu:", path.resolve())
        return doc
    finally:
        del model
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def load_preflight_baseline(out_dir: Path | None) -> dict[str, Any] | None:
    if out_dir is None:
        return None
    p = out_dir / "fol_preflight_baseline.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))
