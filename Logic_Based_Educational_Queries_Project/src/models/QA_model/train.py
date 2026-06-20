"""Train QA Stage 2: LoRA SFT — COT reasoning (NL + FOL → answer + explanation).

Metric chính: **Accuracy** (greedy decode trên dev mỗi epoch).
Tối ưu hoá: early stop + best model chọn theo eval_accuracy.
Log: in mẫu predictions mỗi epoch + benchmark latency sau training.

Usage:
    python -m models.QA_model.train --config configs/qa_model.yaml
    python -m models.QA_model.train --config configs/qa_model.yaml --debug-samples 10
"""
from __future__ import annotations

import argparse
import gc
import inspect
import json
import os
import random
import re
import time
from pathlib import Path
from typing import Any

import torch
import yaml
from datasets import DatasetDict, load_from_disk
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    EarlyStoppingCallback,
)
from transformers.trainer_callback import TrainerCallback
from trl import SFTConfig, SFTTrainer

from .prepare_data import build_qa_dataset_dict


# ─── Config ──────────────────────────────────────────────────────────────────

def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


# ─── Dataset ─────────────────────────────────────────────────────────────────

def get_or_build_dataset(cfg: dict, project_root: Path) -> DatasetDict:
    """Load cached dataset or build from raw data."""
    data_dir = project_root / "data"
    cache_dir = data_dir / "processed" / "qa_sft"

    if cache_dir.exists() and (cache_dir / "dataset_dict.json").exists():
        print(f"[Data] Loading cached dataset from {cache_dir}")
        return load_from_disk(str(cache_dir))

    print("[Data] Building dataset from raw data...")
    ds_dict = build_qa_dataset_dict(data_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    ds_dict.save_to_disk(str(cache_dir))
    print(f"[Data] Cached to {cache_dir}")
    return ds_dict


# ─── Model Loading ───────────────────────────────────────────────────────────

def load_model_and_tokenizer(cfg: dict):
    """Load base model with quantization + LoRA."""
    model_cfg = cfg["model"]
    lora_cfg = cfg["lora"]
    train_cfg = cfg["training"]

    model_name = model_cfg["name"]
    print(f"[Model] Loading: {model_name}")

    # Quantization
    quant_config = None
    if train_cfg.get("load_in_8bit", False):
        quant_config = BitsAndBytesConfig(load_in_8bit=True)
    elif train_cfg.get("load_in_4bit", False):
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, trust_remote_code=model_cfg.get("trust_remote_code", True)
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    load_kwargs = {
        "trust_remote_code": model_cfg.get("trust_remote_code", True),
        "device_map": "auto",
    }
    if quant_config:
        load_kwargs["quantization_config"] = quant_config
    if train_cfg.get("bf16", True):
        load_kwargs["torch_dtype"] = torch.bfloat16

    model = AutoModelForCausalLM.from_pretrained(model_name, **load_kwargs)

    # Prepare for kbit training if quantized
    if quant_config:
        model = prepare_model_for_kbit_training(
            model, use_gradient_checkpointing=train_cfg.get("gradient_checkpointing", True)
        )

    # LoRA
    lora = LoraConfig(
        r=lora_cfg.get("r", 16),
        lora_alpha=lora_cfg.get("alpha", 32),
        lora_dropout=lora_cfg.get("dropout", 0.05),
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=lora_cfg.get("target_modules", ["q_proj", "k_proj", "v_proj", "o_proj"]),
    )
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()

    return model, tokenizer


# ─── Accuracy Evaluation ─────────────────────────────────────────────────────

def parse_qa_output(text: str) -> str:
    """Extract answer label from model output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            parsed = json.loads(match.group())
            if "answer" in parsed:
                return str(parsed["answer"]).strip()
        except json.JSONDecodeError:
            pass
    # Fallback: tìm label đầu tiên
    for label in ("A", "B", "C", "D", "Yes", "No", "Unknown"):
        if label in text:
            return label
    return "Unknown"


def _norm_answer(s: str) -> str:
    """Chuẩn hoá answer để so khớp (full-text MCQ / Yes-No-Uncertain / number-text).
    lowercase + gộp khoảng trắng + bỏ dấu câu cuối → robust hơn exact-match."""
    s = re.sub(r"\s+", " ", str(s).strip().lower())
    return s.rstrip(" .;:!?")


def _parse_user_content(user_content: str) -> dict[str, Any]:
    """Extract NL, FOL, options, question từ user message → dict cho display."""
    sections = re.split(r"\n(?=Premises \((?:NL|FOL)\):|Options:|Question:)", user_content)
    nl_lines, fol_lines, options, question = [], [], [], ""
    for section in sections:
        section = section.strip()
        if section.startswith("Premises (NL):"):
            body = section[len("Premises (NL):"):].strip()
            for line in body.split("\n"):
                m = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if m:
                    nl_lines.append(m.group(1))
        elif section.startswith("Premises (FOL):"):
            body = section[len("Premises (FOL):"):].strip()
            for line in body.split("\n"):
                m = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if m:
                    fol_lines.append(m.group(1))
        elif section.startswith("Options:"):
            body = section[len("Options:"):].strip()
            for line in body.split("\n"):
                m = re.match(r"^[A-J]\.\s*(.+)$", line.strip())
                if m:
                    options.append(m.group(1))
        elif section.startswith("Question:"):
            question = section[len("Question:"):].strip()
    return {"premises_nl": nl_lines, "premises_fol": fol_lines, "options": options, "question": question}


_STEP_PREFIXES = ("Rule:", "Fact:", "Derive:", "Conclusion:")


def _extract_steps(text: str) -> list[str]:
    """Gom các dòng reasoning (Rule:/Fact:/Derive:/Conclusion:) trước JSON cuối."""
    return [ln.strip() for ln in text.split("\n") if ln.strip().startswith(_STEP_PREFIXES)]


def _parse_full_output(text: str) -> dict:
    """Parse output dạng <reasoning steps> + JSON cuối {premises_used, explanation, answer}.

    Khớp định dạng target mới (answer ở cuối). Trả: answer, explanation,
    premises_used, reasoning_steps. Robust với JSON cụt/lỗi.
    """
    reasoning_steps = _extract_steps(text)

    def _premises(parsed) -> list[int]:
        pu = parsed.get("premises_used", [])
        out = []
        if isinstance(pu, list):
            for v in pu:
                try:
                    out.append(int(v))
                except (ValueError, TypeError):
                    pass
        return out

    # 1. JSON CUỐI cùng có "answer" (reasoning đứng trước → lấy match cuối)
    for m in reversed(list(re.finditer(r"\{.*?\}", text, re.DOTALL))):
        try:
            parsed = json.loads(m.group())
        except json.JSONDecodeError:
            continue
        if "answer" in parsed:
            return {
                "answer": str(parsed["answer"]).strip(),
                "explanation": str(parsed.get("explanation", "")).strip(),
                "premises_used": _premises(parsed),
                "reasoning_steps": reasoning_steps,
            }

    # 2. JSON cụt/lỗi: moi từng trường (explanation NON-GREEDY → hết rác)
    m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
    if m:
        answer = m.group(1).strip()
        em = re.search(r'"explanation"\s*:\s*"(.*?)"\s*[,}]', text, re.DOTALL)
        explanation = em.group(1).strip() if em else ""
        pm = re.search(r'"premises_used"\s*:\s*\[([^\]]*)\]', text)
        premises_used = [int(x) for x in re.findall(r"\d+", pm.group(1))] if pm else []
        return {"answer": answer, "explanation": explanation,
                "premises_used": premises_used, "reasoning_steps": reasoning_steps}

    # 3. Last-resort: từ Conclusion: hoặc cue, KHÔNG đoán bừa A/B/C/D
    concl = next((s for s in reversed(reasoning_steps) if s.startswith("Conclusion:")), "")
    m2 = re.search(r"\b(Yes|No|Unknown|[ABCD])\b\s*$", concl)
    if not m2:
        m2 = re.search(
            r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|[ABCD])\b",
            text, re.I,
        )
    if m2:
        return {"answer": m2.group(1), "explanation": "",
                "premises_used": [], "reasoning_steps": reasoning_steps}
    for label in ("Unknown", "Yes", "No"):
        if re.search(rf"\b{label}\b", text):
            return {"answer": label, "explanation": "",
                    "premises_used": [], "reasoning_steps": reasoning_steps}
    return {"answer": "Unknown", "explanation": "",
            "premises_used": [], "reasoning_steps": reasoning_steps}


def _apply_chat_template_no_think(
    tokenizer, messages: list[dict], add_generation_prompt: bool = True
) -> str:
    """Render chat template with thinking DISABLED — consistent train & eval.

    Mirror cách FOL làm (data/fol_dataset.py): `enable_thinking=False` ở CẢ
    training (`add_generation_prompt=False`, render full conversation) lẫn
    eval/inference (`add_generation_prompt=True`, render prompt). Nhất quán
    prompt 2 phía + đầu ra cuối luôn là JSON thuần, không có <think>.
    `enable_thinking` là flag Qwen3; tokenizer không hỗ trợ sẽ bỏ qua kwarg.
    """
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False,
            add_generation_prompt=add_generation_prompt, enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=add_generation_prompt,
        )


def _detect_stop_strings_support(model, tokenizer) -> bool:
    """Check once if model.generate() supports stop_strings (transformers >= 4.40)."""
    import inspect
    sig = inspect.signature(model.generate)
    return "stop_strings" in sig.parameters or "stopping_criteria" in sig.parameters


def _generate_batch(model, tokenizer, texts: list[str], max_new_tokens: int, use_stop_strings: bool) -> list[str]:
    """Batched generation: tokenize + generate + decode."""
    # Left-pad for decoder-only generation
    tokenizer.padding_side = "left"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    inputs = tokenizer(
        texts, return_tensors="pt", padding=True, truncation=True, max_length=4096
    ).to(model.device)

    gen_kwargs = dict(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
    )

    if use_stop_strings:
        try:
            outputs = model.generate(**gen_kwargs, tokenizer=tokenizer, stop_strings=["}"])
        except TypeError:
            outputs = model.generate(**gen_kwargs)
    else:
        outputs = model.generate(**gen_kwargs)

    # Decode only generated part (skip input tokens)
    input_len = inputs["input_ids"].shape[1]
    results = []
    for i in range(outputs.shape[0]):
        generated_ids = outputs[i][input_len:]
        text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        results.append(text)

    return results


def compute_accuracy_on_split(
    model,
    tokenizer,
    dataset,
    max_samples: int | None = None,
    max_new_tokens: int = 150,
    print_n: int = 6,
    log_file: Any = None,
    eval_batch_size: int = 4,
) -> dict[str, Any]:
    """Batched greedy decode trên dataset, tính accuracy + in mẫu random full JSON.

    Returns: {"accuracy": float, "correct": int, "total": int, "avg_latency_sec": float, "samples": list}
    """
    model.eval()
    # gradient_checkpointing set use_cache=False → generate recompute attention mỗi
    # token (chậm gấp nhiều lần). Bật cache khi generate, restore sau khi eval xong
    # để không ảnh hưởng training epoch kế tiếp.
    _prev_use_cache = getattr(model.config, "use_cache", True)
    model.config.use_cache = True
    if max_samples:
        dataset = dataset.select(range(min(max_samples, len(dataset))))

    n_total = len(dataset)

    # Chọn trước print_n indices random để in full detail
    print_indices = set(random.sample(range(n_total), min(print_n, n_total)))

    # Check stop_strings support once
    use_stop_strings = _detect_stop_strings_support(model, tokenizer)

    # Pre-compute all inputs + gold
    all_texts = []
    all_gold = []
    for item in dataset:
        messages = item["messages"]
        gold_text = messages[2]["content"]
        all_gold.append(_parse_full_output(gold_text))

        input_messages = messages[:2]
        text = _apply_chat_template_no_think(tokenizer, input_messages)
        all_texts.append(text)

    # Batched generation
    all_generated = []
    total_time = 0.0
    for batch_start in range(0, n_total, eval_batch_size):
        batch_end = min(batch_start + eval_batch_size, n_total)
        batch_texts = all_texts[batch_start:batch_end]

        t0 = time.perf_counter()
        with torch.no_grad():
            batch_outputs = _generate_batch(model, tokenizer, batch_texts, max_new_tokens, use_stop_strings)
        batch_time = time.perf_counter() - t0
        total_time += batch_time

        all_generated.extend(batch_outputs)

        # Progress
        done = batch_end
        print(f"    eval: {done}/{n_total} ({batch_time:.1f}s for batch of {len(batch_texts)})", flush=True)

    avg_latency = total_time / n_total if n_total > 0 else 0.0

    # Compute accuracy + collect detail samples
    correct = 0
    all_results = []
    detail_samples = []

    for i in range(n_total):
        gold_parsed = all_gold[i]
        pred_parsed = _parse_full_output(all_generated[i])
        is_correct = _norm_answer(pred_parsed["answer"]) == _norm_answer(gold_parsed["answer"])
        correct += int(is_correct)

        all_results.append({
            "idx": i,
            "pred_answer": pred_parsed["answer"],
            "gold_answer": gold_parsed["answer"],
            "correct": is_correct,
        })

        # Full detail cho mẫu random
        if i in print_indices:
            messages = dataset[i]["messages"]
            user_content = messages[1]["content"]
            parsed_input = _parse_user_content(user_content)
            detail_samples.append({
                "idx": i,
                "correct": is_correct,
                "input": {
                    "query": parsed_input["question"],
                    "premises": parsed_input["premises_nl"],
                    "premises_fol": parsed_input["premises_fol"],
                    "options": parsed_input.get("options", []),
                },
                "gold": {
                    "answer": gold_parsed["answer"],
                    "premises_used": gold_parsed.get("premises_used", []),
                    "reasoning_steps": gold_parsed.get("reasoning_steps", []),
                    "explanation": gold_parsed["explanation"],
                },
                "prediction": {
                    "answer": pred_parsed["answer"],
                    "premises_used": pred_parsed.get("premises_used", []),
                    "reasoning_steps": pred_parsed.get("reasoning_steps", []),
                    "explanation": pred_parsed["explanation"],
                },
            })

    accuracy = correct / n_total if n_total > 0 else 0.0

    result = {
        "accuracy": accuracy,
        "correct": correct,
        "total": n_total,
        "avg_latency_sec": avg_latency,
        "total_time_sec": round(total_time, 2),
        "samples": all_results,
        "detail_samples": detail_samples,
    }

    # In full detail JSON cho các mẫu random
    if detail_samples:
        print(f"\n  {'━'*70}")
        print(f"  DETAILED PREDICTIONS ({len(detail_samples)} random samples)")
        print(f"  {'━'*70}")
        for s in detail_samples:
            status = "✅ CORRECT" if s["correct"] else "❌ WRONG"
            print(f"\n  ── Sample [{s['idx']}] {status} ──")
            print(json.dumps(s, ensure_ascii=False, indent=4))
        print(f"\n  {'━'*70}")

    # Ghi log file
    if log_file:
        log_file.write(json.dumps(result, ensure_ascii=False) + "\n")
        log_file.flush()

    # Restore use_cache như trước khi eval (training với gradient checkpointing cần False)
    model.config.use_cache = _prev_use_cache

    return result


# ─── Accuracy Callback ───────────────────────────────────────────────────────

class QAAccuracyCallback(TrainerCallback):
    """Mỗi epoch: greedy decode trên dev → eval_accuracy.

    Ghi vào metrics để EarlyStopping + load_best_model_at_end sử dụng.
    """

    def __init__(self, cfg: dict, dev_dataset, log_path: Path | None = None):
        self.cfg = cfg
        self.dev_dataset = dev_dataset
        self.log_path = log_path
        self.log_file = None
        self.epoch_results: list[dict] = []

    def on_train_begin(self, args, state, control, **kwargs):
        if self.log_path:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            self.log_file = open(self.log_path, "w", encoding="utf-8")

    def on_train_end(self, args, state, control, **kwargs):
        if self.log_file:
            self.log_file.close()
            self.log_file = None

    def on_evaluate(self, args, state, control, metrics=None, model=None, processing_class=None, **kwargs):
        if metrics is None or model is None:
            return

        tokenizer = processing_class or kwargs.get("tokenizer")
        if tokenizer is None:
            return

        eval_cfg = self.cfg.get("eval", {})
        max_samples = eval_cfg.get("eval_accuracy_max_samples")
        print_n = eval_cfg.get("eval_print_samples", 6)
        max_new_tokens = self.cfg["model"].get("gen_max_new_tokens", 150)
        eval_batch_size = self.cfg["training"].get("per_device_eval_batch_size", 4)

        epoch = state.epoch or 0
        print(f"\n{'='*60}")
        print(f"  [Epoch {epoch:.0f}] Computing accuracy on dev (batch_size={eval_batch_size})...")

        result = compute_accuracy_on_split(
            model=model,
            tokenizer=tokenizer,
            dataset=self.dev_dataset,
            max_samples=max_samples,
            max_new_tokens=max_new_tokens,
            print_n=print_n,
            log_file=self.log_file,
            eval_batch_size=eval_batch_size,
        )

        accuracy = result["accuracy"]
        metrics["eval_accuracy"] = accuracy

        print(f"  [Epoch {epoch:.0f}] Accuracy: {result['correct']}/{result['total']} = {accuracy:.1%}")
        print(f"  [Epoch {epoch:.0f}] Total eval time: {result['total_time_sec']:.1f}s | Avg: {result['avg_latency_sec']:.2f}s/sample")
        print(f"{'='*60}\n")

        self.epoch_results.append({"epoch": epoch, **result})


# ─── Latency Benchmark ───────────────────────────────────────────────────────

def benchmark_latency(model, tokenizer, dataset, cfg: dict):
    """Benchmark latency sau training (warmup + N samples)."""
    eval_cfg = cfg.get("eval", {})
    n = eval_cfg.get("inference_latency_benchmark_n", 30)
    warmup = eval_cfg.get("inference_latency_warmup", 2)
    max_new_tokens = cfg["model"].get("gen_max_new_tokens", 512)

    if n <= 0:
        return

    total = min(warmup + n, len(dataset))
    subset = dataset.select(range(total))

    print(f"\n{'='*60}")
    print(f"  Latency Benchmark: {warmup} warmup + {n} measured samples")
    print(f"{'='*60}")

    latencies = []
    model.eval()

    for i, item in enumerate(subset):
        messages = item["messages"][:2]
        text = _apply_chat_template_no_think(tokenizer, messages)
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=4096).to(model.device)

        t0 = time.perf_counter()
        with torch.no_grad():
            model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
        elapsed = time.perf_counter() - t0

        if i >= warmup:
            latencies.append(elapsed)
            print(f"    [{i - warmup + 1:3d}/{n}] {elapsed:.3f}s")

    if not latencies:
        print(f"{'='*60}\n")
        return None

    avg = sum(latencies) / len(latencies)
    min_l = min(latencies)
    max_l = max(latencies)
    print(f"\n  Avg: {avg:.3f}s | Min: {min_l:.3f}s | Max: {max_l:.3f}s")
    print(f"{'='*60}\n")

    return {"avg_sec": avg, "min_sec": min_l, "max_sec": max_l, "n": len(latencies)}


# ─── Full Evaluation (train + dev + test) ────────────────────────────────────

def evaluate_all_splits(model, tokenizer, ds_dict: DatasetDict, cfg: dict, output_dir: Path):
    """Final eval sau training, ghi eval_results.json (kèm per-sample predictions cho dev/test).

    Eval là generation-based (~500 token/mẫu) nên RẤT đắt → MẶC ĐỊNH chỉ chạy "test" để khỏi
    đốt thời gian generate lại dev/train. Per-epoch dev eval (AccuracyCallback) vẫn chạy mỗi epoch.
      - Splits chạy: eval.final_eval_splits (default ["test"]; có thể thêm "dev","train").
      - train (nếu bật) chỉ sample `eval_train_sample` mẫu (default 50) → tín hiệu overfit-gap.
      - dev/test lưu đầy đủ samples + detail_samples vào eval_results.json để soi lỗi.
    """
    max_new_tokens = cfg["model"].get("gen_max_new_tokens", 512)
    eval_cfg = cfg.get("eval", {})
    print_n = eval_cfg.get("eval_print_samples", 5)
    train_sample_n = eval_cfg.get("eval_train_sample", 50)
    eval_batch_size = cfg.get("training", {}).get("per_device_eval_batch_size", 8)

    # gradient_checkpointing lúc train tắt use_cache → generate không cache thì
    # chậm thảm họa (recompute attention mỗi token). Bật lại trước khi eval.
    model.config.use_cache = True

    # (split, max_samples). MẶC ĐỊNH CHỈ "test" sau epoch cuối — KHÔNG chạy lại dev/train
    # (generation-based, rất tốn time). Per-epoch dev eval (AccuracyCallback) VẪN chạy độc lập
    # mỗi epoch nên log dev qua các epoch không mất. Muốn eval thêm dev/train ở bước cuối:
    # đặt eval.final_eval_splits: ["test", "dev", "train"] trong config.
    _plan_max = {"test": None, "dev": None, "train": train_sample_n}
    final_splits = eval_cfg.get("final_eval_splits", ["test"])
    plan = [(s, _plan_max[s]) for s in final_splits if s in _plan_max]

    results = {}
    eval_path = output_dir / "eval_results.json"
    for split_name, max_samples in plan:
        if split_name not in ds_dict:
            continue
        n_show = min(max_samples or len(ds_dict[split_name]), len(ds_dict[split_name]))
        print(f"\n{'='*60}")
        print(f"  Final Accuracy — [{split_name}] ({n_show}/{len(ds_dict[split_name])} samples, batch={eval_batch_size})")
        print(f"{'='*60}")

        result = compute_accuracy_on_split(
            model=model,
            tokenizer=tokenizer,
            dataset=ds_dict[split_name],
            max_samples=max_samples,
            max_new_tokens=max_new_tokens,
            print_n=print_n if split_name != "train" else 3,
            eval_batch_size=eval_batch_size,
        )
        results[split_name] = {
            "accuracy": result["accuracy"],
            "correct": result["correct"],
            "total": result["total"],
            "avg_latency_sec": result["avg_latency_sec"],
        }
        # dev/test: giữ per-sample predictions + detail để phân tích lỗi offline
        if split_name in ("dev", "test"):
            results[split_name]["samples"] = result["samples"]
            results[split_name]["detail_samples"] = result["detail_samples"]
        print(f"  → {split_name}: {result['correct']}/{result['total']} = {result['accuracy']:.1%}")

        # Ghi ngay sau mỗi split — lỡ bị ngắt giữa chừng vẫn còn kết quả test
        with open(eval_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    # Summary
    print(f"\n{'='*60}")
    print(f"  FINAL ACCURACY SUMMARY")
    print(f"{'='*60}")
    for split_name, r in results.items():
        note = f" (sampled {train_sample_n})" if split_name == "train" else ""
        print(f"  {split_name:5s}: {r['accuracy']:.1%} ({r['correct']}/{r['total']}){note}, avg {r['avg_latency_sec']:.2f}s/sample")
    print(f"{'='*60}\n")
    print(f"[Eval] Results saved to: {eval_path}")

    return results


# ─── Training ────────────────────────────────────────────────────────────────

def train(cfg: dict, debug_max_samples: int | None = None):
    """Full training pipeline."""
    project_root = resolve_project_root()
    train_cfg = cfg["training"]
    model_cfg = cfg["model"]
    hub_cfg = cfg.get("hub", {})

    # 1. Dataset
    ds_dict = get_or_build_dataset(cfg, project_root)

    if debug_max_samples:
        for split in ds_dict:
            n = min(debug_max_samples, len(ds_dict[split]))
            ds_dict[split] = ds_dict[split].select(range(n))
        print(f"[Debug] Limited to {debug_max_samples} samples per split")

    # train_sample: giới hạn SỐ MẪU TRAIN (chỉ split train) để chạy thử nhanh.
    # null/0 = train full. dev/test luôn giữ nguyên để đánh giá không đổi.
    train_sample = train_cfg.get("train_sample")
    if train_sample:
        n = min(int(train_sample), len(ds_dict["train"]))
        ds_dict["train"] = ds_dict["train"].select(range(n))
        print(f"[train_sample] Giới hạn train → {n} mẫu (dev/test giữ nguyên)")

    print(f"[Data] Train: {len(ds_dict['train'])}, Dev: {len(ds_dict['dev'])}, Test: {len(ds_dict['test'])}")

    # 2. Model
    model, tokenizer = load_model_and_tokenizer(cfg)

    # 2b. Dataset cho trainer ở định dạng prompt–completion, thinking TẮT
    #     (nhất quán train & eval, giống FOL data/fol_dataset.py):
    #       - prompt     = system+user + generation prompt (add_generation_prompt=True)
    #       - completion = assistant JSON đáp án
    #     Kết hợp completion_only_loss=True → loss CHỈ trên completion (mask prompt).
    #     Giữ nguyên ds_dict (có "messages") cho accuracy callback + final eval.
    def _to_prompt_completion(example):
        msgs = example["messages"]
        return {
            "prompt": _apply_chat_template_no_think(
                tokenizer, msgs[:2], add_generation_prompt=True
            ),
            "completion": msgs[2]["content"],
        }

    train_ds_pc = ds_dict["train"].map(
        _to_prompt_completion,
        remove_columns=ds_dict["train"].column_names,
        desc="Build prompt-completion (train)",
    )
    dev_ds_pc = ds_dict["dev"].map(
        _to_prompt_completion,
        remove_columns=ds_dict["dev"].column_names,
        desc="Build prompt-completion (dev)",
    )

    # 3. Output dir
    version = hub_cfg.get("repo_version", "v01")
    model_type = hub_cfg.get("type", "QA")
    method = hub_cfg.get("method", "CoT")
    slug = model_cfg["name"].split("/")[-1]
    output_dir = project_root / "outputs" / f"{model_type.lower()}-{version}-{method.lower()}-{slug}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 4. SFT Config
    max_seq_len = model_cfg.get("max_seq_length", 3500)

    sft_kw: dict[str, Any] = dict(
        output_dir=str(output_dir),
        num_train_epochs=train_cfg.get("num_train_epochs", 20),
        per_device_train_batch_size=train_cfg.get("per_device_train_batch_size", 1),
        per_device_eval_batch_size=train_cfg.get("per_device_eval_batch_size", 8),
        gradient_accumulation_steps=train_cfg.get("gradient_accumulation_steps", 8),
        learning_rate=float(train_cfg.get("learning_rate", 2e-5)),
        warmup_ratio=train_cfg.get("warmup_ratio", 0.05),
        weight_decay=train_cfg.get("weight_decay", 0.01),
        logging_steps=train_cfg.get("logging_steps", 10),
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=train_cfg.get("save_total_limit", 1),
        load_best_model_at_end=train_cfg.get("load_best_model_at_end", True),
        metric_for_best_model=train_cfg.get("metric_for_best_model", "eval_accuracy"),
        greater_is_better=train_cfg.get("greater_is_better", True),
        bf16=train_cfg.get("bf16", True),
        gradient_checkpointing=train_cfg.get("gradient_checkpointing", True),
        seed=train_cfg.get("train_seed", 3407),
        report_to="none",
        max_length=max_seq_len,
        packing=False,
        # Loss CHỈ trên completion (assistant JSON), mask toàn bộ prompt system+user.
        completion_only_loss=train_cfg.get("completion_only_loss", True),
        # Liger fused CE: giảm mạnh VRAM ở bước loss (cần `pip install liger-kernel`).
        use_liger_kernel=train_cfg.get("use_liger_kernel", False),
    )
    # TRL version compat: một số version dùng max_seq_length thay vì max_length
    if "max_seq_length" in inspect.signature(SFTConfig.__init__).parameters:
        sft_kw["max_seq_length"] = max_seq_len

    sft_config = SFTConfig(**sft_kw)

    # 5. Callbacks
    callbacks = []

    # Accuracy callback (ghi eval_accuracy vào metrics mỗi epoch)
    log_path = output_dir / "accuracy_log.jsonl"
    accuracy_cb = QAAccuracyCallback(cfg, ds_dict["dev"], log_path=log_path)
    callbacks.append(accuracy_cb)

    # Early stopping
    patience = train_cfg.get("early_stopping_patience", 7)
    if patience > 0:
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=patience))

    if sft_kw.get("completion_only_loss", True):
        print("[Train] Completion-only loss BẬT — loss chỉ trên assistant JSON, mask prompt system+user")

    # 6. Trainer (train/eval trên dataset prompt–completion đã dựng ở bước 2b)
    trainer = SFTTrainer(
        model=model,
        args=sft_config,
        train_dataset=train_ds_pc,
        eval_dataset=dev_ds_pc,
        processing_class=tokenizer,
        callbacks=callbacks,
    )

    # 7. Train
    print(f"\n{'='*60}")
    print(f"  Starting QA COT SFT Training")
    print(f"  Model: {model_cfg['name']}")
    print(f"  Type: {model_type} | Method: {method} | Version: {version}")
    print(f"  Metric: accuracy (early_stop patience={patience})")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}\n")

    trainer.train()

    # 8. Save final LoRA adapter
    final_dir = output_dir / "final_lora"
    trainer.save_model(str(final_dir))
    tokenizer.save_pretrained(str(final_dir))
    print(f"\n[Save] LoRA adapter saved to: {final_dir}")

    # 9. Final evaluation — mặc định CHỈ test (xem eval.final_eval_splits để thêm dev/train)
    evaluate_all_splits(model, tokenizer, ds_dict, cfg, output_dir)

    # 10. Latency benchmark
    bench_split = cfg.get("eval", {}).get("inference_latency_benchmark_split", "test")
    latency_result = None
    if bench_split in ds_dict:
        latency_result = benchmark_latency(model, tokenizer, ds_dict[bench_split], cfg)
    if latency_result:
        latency_path = output_dir / "inference_latency.json"
        with open(latency_path, "w", encoding="utf-8") as f:
            json.dump(latency_result, f, ensure_ascii=False, indent=2)
        print(f"[Log] Latency benchmark saved to: {latency_path}")

    # 11. Save epoch accuracy history
    if accuracy_cb.epoch_results:
        history_path = output_dir / "epoch_accuracy_history.json"
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump(accuracy_cb.epoch_results, f, ensure_ascii=False, indent=2)
        print(f"[Log] Epoch history saved to: {history_path}")

    # 12. Push to Hub (optional)
    if hub_cfg.get("push_to_hub", False):
        org = hub_cfg.get("org", "")
        repo_name = f"{model_type.lower()}-{version}-{method.lower()}-{slug}"
        hub_repo_id = f"{org}/{repo_name}" if org else repo_name
        print(f"[Hub] Pushing to: {hub_repo_id}")
        trainer.push_to_hub(repo_id=hub_repo_id, private=hub_cfg.get("hf_private", True))

    # 13. Cleanup
    del model, trainer
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("\n[Done] Training complete.")
    return str(final_dir)


# ─── Merge LoRA → Full Model ─────────────────────────────────────────────────

def merge_and_push(cfg: dict, lora_dir: str | None = None):
    """Merge LoRA adapter into base model and optionally push to Hub."""
    from peft import PeftModel

    project_root = resolve_project_root()
    model_cfg = cfg["model"]
    hub_cfg = cfg.get("hub", {})
    version = hub_cfg.get("repo_version", "v01")
    model_type = hub_cfg.get("type", "QA")
    method = hub_cfg.get("method", "CoT")
    slug = model_cfg["name"].split("/")[-1]

    if lora_dir is None:
        lora_dir = str(project_root / "outputs" / f"{model_type.lower()}-{version}-{method.lower()}-{slug}" / "final_lora")

    print(f"[Merge] Loading base: {model_cfg['name']}")
    base_model = AutoModelForCausalLM.from_pretrained(
        model_cfg["name"],
        trust_remote_code=model_cfg.get("trust_remote_code", True),
        torch_dtype=torch.bfloat16,
        device_map="cpu",
    )
    tokenizer = AutoTokenizer.from_pretrained(
        model_cfg["name"], trust_remote_code=model_cfg.get("trust_remote_code", True)
    )

    print(f"[Merge] Loading LoRA from: {lora_dir}")
    model = PeftModel.from_pretrained(base_model, lora_dir)
    model = model.merge_and_unload()

    merged_dir = str(
        project_root / "outputs" / f"{model_type.lower()}-{version}-{method.lower()}-{slug}" / "merged"
    )
    model.save_pretrained(merged_dir)
    tokenizer.save_pretrained(merged_dir)
    print(f"[Merge] Merged model saved to: {merged_dir}")

    if hub_cfg.get("push_to_hub", False):
        org = hub_cfg.get("org", "")
        repo_name = f"{model_type.lower()}-{version}-{method.lower()}-{slug}"
        hub_repo_id = f"{org}/{repo_name}" if org else repo_name
        print(f"[Hub] Pushing merged model to: {hub_repo_id}")
        model.push_to_hub(hub_repo_id, private=hub_cfg.get("hf_private", True))
        tokenizer.push_to_hub(hub_repo_id, private=hub_cfg.get("hf_private", True))

    print("[Done] Merge complete.")
    return merged_dir


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Train QA COT model (Stage 2)")
    parser.add_argument("--config", type=str, default="configs/qa_model.yaml")
    parser.add_argument("--debug-samples", type=int, default=None, help="Limit samples for quick test")
    parser.add_argument("--merge", action="store_true", help="Merge LoRA after training")
    parser.add_argument("--merge-only", action="store_true", help="Only merge (skip training)")
    parser.add_argument("--lora-dir", type=str, default=None, help="Path to LoRA adapter for merge")
    args = parser.parse_args()

    cfg = load_config(args.config)

    if args.merge_only:
        merge_and_push(cfg, args.lora_dir)
    else:
        lora_dir = train(cfg, debug_max_samples=args.debug_samples)
        if args.merge:
            merge_and_push(cfg, lora_dir)


if __name__ == "__main__":
    main()
