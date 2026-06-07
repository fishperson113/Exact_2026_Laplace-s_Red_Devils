"""Ensemble Pipeline: FOL Model → QA COT Model → answer + explanation.

Flow:
  1. FOL Model (HF Hub) sinh FOL từ NL premises
  2. QA Model (LoRA checkpoint) nhận NL + FOL + question → answer + explanation

Hỗ trợ 2 mode:
  - Evaluate: có gold answer → tính accuracy
  - Inference: không có gold → chỉ sinh answer

Usage:
    # Evaluate trên test set (có gold)
    python -m models.Ensemble_Model.inference --config configs/ensemble_model.yaml --mode evaluate

    # Inference (không có gold, chỉ sinh answer)
    python -m models.Ensemble_Model.inference --config configs/ensemble_model.yaml --mode inference --input data.json
"""
from __future__ import annotations

import argparse
import ast
import gc
import json
import random
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
import torch
import yaml
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from data.prompts import (
    SYSTEM_PROMPT_FOL_SFT,
    USER_TEMPLATE_FOL_SFT,
    format_nl_block_numbered,
)
from models.QA_model.prepare_data import (
    SYSTEM_PROMPT_QA_COT,
    USER_TEMPLATE_QA_COT,
    format_premises_fol,
    format_premises_nl,
)


# ─── Config ──────────────────────────────────────────────────────────────────

def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _render_no_think(tokenizer, messages) -> str:
    """apply_chat_template với thinking TẮT (Qwen3); fallback nếu tokenizer không nhận kwarg."""
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )


# ─── Result Dataclass ────────────────────────────────────────────────────────

@dataclass
class EnsembleResult:
    answer: str
    explanation: str
    premises_fol: list[str]
    fol_latency_sec: float = 0.0
    qa_latency_sec: float = 0.0
    total_latency_sec: float = 0.0
    fol_raw_output: str = ""


# ─── FOL Model ───────────────────────────────────────────────────────────────

class FOLModel:
    """Load FOL model từ HF Hub (merged) và sinh FOL từ NL."""

    def __init__(self, hub_repo_id: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[FOL] Loading: {hub_repo_id}")

        load_kwargs = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        self.tokenizer = AutoTokenizer.from_pretrained(hub_repo_id, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(hub_repo_id, **load_kwargs)
        self.model.eval()
        print(f"[FOL] Loaded on {self.device}")

    def generate(self, premises_nl: list[str], max_new_tokens: int = 650) -> tuple[list[str], str]:
        """NL premises → FOL premises. Returns (fol_list, raw_output)."""
        nl_block = format_nl_block_numbered(premises_nl)
        user_msg = USER_TEMPLATE_FOL_SFT.format(premises_nl=nl_block)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_FOL_SFT},
            {"role": "user", "content": user_msg},
        ]
        # enable_thinking=False: 2 model đều là Qwen3.5 (thinking) và được train với
        # no-think → BẮT BUỘC tắt thinking lúc inference, nếu không <think> sẽ ăn hết
        # token budget và JSON bị cắt. try/except cho tokenizer không hỗ trợ kwarg.
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=3500
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False, repetition_penalty=1.2,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_fol(raw), raw

    def generate_batch(self, premises_nl_list: list[list[str]], max_new_tokens: int = 650) -> list[tuple[list[str], str]]:
        """Batched: list[NL premises] → list[(fol_list, raw)]. Left-pad cho decoder-only."""
        self.tokenizer.padding_side = "left"
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        texts = []
        for nl in premises_nl_list:
            user_msg = USER_TEMPLATE_FOL_SFT.format(premises_nl=format_nl_block_numbered(nl))
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT_FOL_SFT},
                {"role": "user", "content": user_msg},
            ]
            texts.append(_render_no_think(self.tokenizer, messages))
        inputs = self.tokenizer(
            texts, return_tensors="pt", padding=True, truncation=True, max_length=3500
        ).to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False, repetition_penalty=1.2,
            )
        input_len = inputs["input_ids"].shape[1]
        res = []
        for i in range(out.shape[0]):
            raw = self.tokenizer.decode(out[i][input_len:], skip_special_tokens=True).strip()
            res.append((self._parse_fol(raw), raw))
        return res

    @staticmethod
    def _parse_fol(text: str) -> list[str]:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "premises_fol" in parsed and isinstance(parsed["premises_fol"], list):
                    return [str(f).strip() for f in parsed["premises_fol"]]
            except json.JSONDecodeError:
                pass
        lines = []
        for line in text.split("\n"):
            line = line.strip().lstrip("0123456789.)-  ")
            if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
                lines.append(line)
        return lines


# ─── QA Model ────────────────────────────────────────────────────────────────

class QAModel:
    """Load QA model (base + LoRA adapter) và sinh answer + explanation."""

    def __init__(self, hub_repo_id: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[QA] Loading from HF Hub: {hub_repo_id}")

        load_kwargs = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        # Base model name is read from adapter_config.json on Hub
        from peft import PeftConfig
        peft_config = PeftConfig.from_pretrained(hub_repo_id)
        base_model_name = peft_config.base_model_name_or_path
        print(f"[QA] Base model: {base_model_name}")

        # Tokenizer + chat_template lấy TỪ repo adapter (final_lora) để dùng ĐÚNG
        # template lúc train. Vocab giống base (LoRA không đổi tokenizer); chỉ weights
        # base lấy từ base_model_name.
        self.tokenizer = AutoTokenizer.from_pretrained(hub_repo_id, trust_remote_code=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(base_model_name, **load_kwargs)
        self.model = PeftModel.from_pretrained(base_model, hub_repo_id)
        self.model.eval()
        print(f"[QA] Loaded on {self.device}")

    def generate(self, premises_nl: list[str], premises_fol: list[str], question: str,
                 max_new_tokens: int = 200) -> dict[str, str]:
        """NL + FOL + question → {"answer": "...", "explanation": "..."}."""
        user_content = USER_TEMPLATE_QA_COT.format(
            premises_nl_block=format_premises_nl(premises_nl),
            premises_fol_block=format_premises_fol(premises_fol),
            question=question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
            {"role": "user", "content": user_content},
        ]
        # enable_thinking=False: 2 model đều là Qwen3.5 (thinking) và được train với
        # no-think → BẮT BUỘC tắt thinking lúc inference, nếu không <think> sẽ ăn hết
        # token budget và JSON bị cắt. try/except cho tokenizer không hỗ trợ kwarg.
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=4096
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_output(raw)

    def generate_batch(self, items: list[tuple], max_new_tokens: int = 256) -> list[dict]:
        """Batched: list[(premises_nl, premises_fol, question)] → list[{answer, explanation}]."""
        self.tokenizer.padding_side = "left"
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        texts = []
        for nl, fol, q in items:
            user_content = USER_TEMPLATE_QA_COT.format(
                premises_nl_block=format_premises_nl(nl),
                premises_fol_block=format_premises_fol(fol),
                question=q,
            )
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
                {"role": "user", "content": user_content},
            ]
            texts.append(_render_no_think(self.tokenizer, messages))
        inputs = self.tokenizer(
            texts, return_tensors="pt", padding=True, truncation=True, max_length=4096
        ).to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
        input_len = inputs["input_ids"].shape[1]
        res = []
        for i in range(out.shape[0]):
            raw = self.tokenizer.decode(out[i][input_len:], skip_special_tokens=True).strip()
            res.append(self._parse_output(raw))
        return res

    @staticmethod
    def _parse_output(text: str) -> dict[str, str]:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "answer" in parsed:
                    return {
                        "answer": str(parsed["answer"]).strip(),
                        "explanation": str(parsed.get("explanation", "")).strip(),
                    }
            except json.JSONDecodeError:
                pass
        # JSON cụt/lỗi: moi "answer": "..." (và explanation nếu có)
        m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
        if m:
            ans = m.group(1).strip()
            em = re.search(r'"explanation"\s*:\s*"(.*)', text, re.DOTALL)
            explanation = em.group(1).strip().rstrip('"}').strip() if em else ""
            return {"answer": ans, "explanation": explanation}
        # Last-resort: word-boundary + cue, KHÔNG đoán bừa chữ "A" trong văn xuôi
        m2 = re.search(
            r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|[ABCD])\b",
            text, re.I,
        )
        if m2:
            return {"answer": m2.group(1), "explanation": ""}
        for label in ("Unknown", "Yes", "No"):
            if re.search(rf"\b{label}\b", text):
                return {"answer": label, "explanation": ""}
        return {"answer": "Unknown", "explanation": ""}


# ─── Ensemble Pipeline ────────────────────────────────────────────────────────

class EnsemblePipeline:
    """FOL Model + QA Model chạy theo 2 PHA — mỗi thời điểm CHỈ 1 LLM trong VRAM.

    Tuân thủ luật BTC (EXACT 2026): không để 2 LLM cùng resident trên GPU.
      - PHA 1: nạp FOL → sinh FOL cho TOÀN BỘ mẫu → GIẢI PHÓNG GPU.
      - PHA 2: nạp QA → sinh đáp án (dùng FOL đã sinh) → giải phóng GPU.
    `generate_fol_all` / `answer_all` tự quản lý vòng đời model + log VRAM để
    chứng minh tại mọi thời điểm chỉ có một model ≤8B được nạp.
    """

    def __init__(self, cfg: dict):
        fol_cfg = cfg["fol_model"]
        qa_cfg = cfg["qa_model"]
        inf_cfg = cfg.get("inference", {})
        # KHÔNG nạp model ở đây — nạp lần lượt trong từng pha để chỉ 1 LLM/lúc.
        self.fol_repo = fol_cfg["hub_repo_id"]
        self.qa_repo = qa_cfg["hub_repo_id"]
        self.load_8bit = inf_cfg.get("load_in_8bit", True)
        self.fol_max_new_tokens = fol_cfg.get("max_new_tokens", 650)
        self.qa_max_new_tokens = qa_cfg.get("max_new_tokens", 200)
        self.batch_size = max(1, int(inf_cfg.get("batch_size", 4)))

    @staticmethod
    def _vram_gb() -> float:
        return torch.cuda.memory_allocated() / 1e9 if torch.cuda.is_available() else 0.0

    def _unload(self, holder) -> None:
        """Xoá model+tokenizer khỏi VRAM và dọn sạch cache trước khi nạp model kế tiếp."""
        for attr in ("model", "tokenizer"):
            if hasattr(holder, attr):
                try:
                    delattr(holder, attr)
                except Exception:
                    pass
        del holder
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # ───── PHA 1: chỉ FOL trong VRAM ─────
    def generate_fol_all(self, premises_nl_list: list[list[str]]) -> list[dict]:
        n = len(premises_nl_list)
        bs = self.batch_size
        print(f"\n[PHA 1] Nạp FOL model (chỉ 1 LLM trong VRAM)… batch_size={bs}")
        fol_model = FOLModel(self.fol_repo, self.load_8bit)
        print(f"[VRAM] sau khi nạp FOL: {self._vram_gb():.2f} GB")
        out: list[dict] = []
        for s in range(0, n, bs):
            chunk = premises_nl_list[s:s + bs]
            t0 = time.perf_counter()
            batch_res = fol_model.generate_batch(chunk, self.fol_max_new_tokens)
            dt = time.perf_counter() - t0
            per = dt / len(chunk)
            for fol, raw in batch_res:
                out.append({"premises_fol": fol, "fol_raw": raw, "fol_latency_sec": per})
            print(f"  [FOL {min(s + bs, n):3d}/{n}] batch {len(chunk)} → {dt:.1f}s ({per:.1f}s/mẫu)", flush=True)
        self._unload(fol_model)
        print(f"[VRAM] sau khi GIẢI PHÓNG FOL: {self._vram_gb():.2f} GB  (đã unload trước khi nạp QA)")
        return out

    # ───── PHA 2: chỉ QA trong VRAM ─────
    def answer_all(self, items: list[tuple]) -> list[dict]:
        n = len(items)
        bs = self.batch_size
        print(f"\n[PHA 2] Nạp QA model (FOL đã unload; chỉ 1 LLM trong VRAM)… batch_size={bs}")
        qa_model = QAModel(self.qa_repo, self.load_8bit)
        print(f"[VRAM] sau khi nạp QA: {self._vram_gb():.2f} GB")
        out: list[dict] = []
        for s in range(0, n, bs):
            chunk = items[s:s + bs]
            t0 = time.perf_counter()
            batch_res = qa_model.generate_batch(chunk, self.qa_max_new_tokens)
            dt = time.perf_counter() - t0
            per = dt / len(chunk)
            for res in batch_res:
                out.append({"answer": res["answer"], "explanation": res["explanation"], "qa_latency_sec": per})
            print(f"  [QA {min(s + bs, n):3d}/{n}] batch {len(chunk)} → {dt:.1f}s ({per:.1f}s/mẫu)", flush=True)
        self._unload(qa_model)
        print(f"[VRAM] sau khi GIẢI PHÓNG QA: {self._vram_gb():.2f} GB")
        return out


# ─── Data Loading ─────────────────────────────────────────────────────────────

def load_test_csv(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "processed" / "test.csv", encoding="utf-8")


def parse_list_field(value) -> list[str]:
    if pd.isna(value) or not str(value).strip():
        return []
    try:
        return ast.literal_eval(str(value))
    except (ValueError, SyntaxError):
        return []


def load_inference_json(path: str) -> list[dict]:
    """Load input JSON cho inference mode (không có gold).
    Format: [{"premises_nl": [...], "question": "..."}, ...]
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ─── Evaluate Mode ────────────────────────────────────────────────────────────

def evaluate(pipeline: EnsemblePipeline, cfg: dict):
    """Evaluate trên test.csv (có gold answer) → accuracy + latency."""
    project_root = resolve_project_root()
    data_dir = project_root / "data"
    output_dir = Path(cfg.get("output_dir", str(project_root / "outputs" / "ensemble")))
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_test_csv(data_dir)
    slow_threshold = cfg.get("inference", {}).get("slow_threshold_sec", 60)
    n = len(df)

    print(f"\n{'='*70}")
    print(f"  ENSEMBLE EVALUATE — {n} samples  (2 PHA: FOL → giải phóng GPU → QA)")
    print(f"  Slow threshold: {slow_threshold}s")
    print(f"{'='*70}\n")

    # Gom input
    premises_nl_list, questions, golds, gold_expls, fol_golds = [], [], [], [], []
    for _, row in df.iterrows():
        premises_nl_list.append(parse_list_field(row["premises_nl"]))
        questions.append(str(row["question"]))
        golds.append(str(row["answer"]).strip())
        gold_expls.append(str(row.get("explanation", "")))
        fol_golds.append(parse_list_field(row.get("premises_fol", "[]")))

    # PHA 1: FOL (chỉ FOL trong VRAM) → PHA 2: QA (FOL đã unload, chỉ QA trong VRAM)
    fol_results = pipeline.generate_fol_all(premises_nl_list)
    items = [(premises_nl_list[i], fol_results[i]["premises_fol"], questions[i]) for i in range(n)]
    qa_results = pipeline.answer_all(items)

    # Tổng hợp + log + accuracy (format giữ nguyên)
    correct = 0
    total = n
    results = []
    slow_samples = []
    log_path = output_dir / "ensemble_eval_log.jsonl"
    log_file = open(log_path, "w", encoding="utf-8")

    print(f"\n{'='*70}\n  Tổng hợp kết quả\n{'='*70}")
    for i in range(n):
        fol_lat = fol_results[i]["fol_latency_sec"]
        qa_lat = qa_results[i]["qa_latency_sec"]
        total_lat = fol_lat + qa_lat
        pred = qa_results[i]["answer"]
        expl = qa_results[i]["explanation"]
        gold_answer = golds[i]

        is_correct = pred.strip().upper() == gold_answer.upper()
        correct += int(is_correct)

        status = "✓" if is_correct else "✗"
        latency_warn = ""
        if total_lat > slow_threshold:
            latency_warn = " SLOW"
            slow_samples.append(i)

        print(
            f"  [{i+1:3d}/{n}] {status} pred={pred:8s} gold={gold_answer:8s} "
            f"| FOL:{fol_lat:.1f}s QA:{qa_lat:.1f}s Total:{total_lat:.1f}s{latency_warn}",
            flush=True,
        )

        sample_record = {
            "idx": i,
            "correct": is_correct,
            "input": {
                "premises_nl": premises_nl_list[i],
                "premises_fol_gold": fol_golds[i],
                "question": questions[i],
            },
            "fol_generated": fol_results[i]["premises_fol"],
            "gold": {
                "answer": gold_answer,
                "explanation": gold_expls[i],
            },
            "prediction": {
                "answer": pred,
                "explanation": expl,
            },
            "latency": {
                "fol_sec": round(fol_lat, 3),
                "qa_sec": round(qa_lat, 3),
                "total_sec": round(total_lat, 3),
            },
        }
        results.append(sample_record)
        log_file.write(json.dumps(sample_record, ensure_ascii=False) + "\n")
        log_file.flush()

    log_file.close()
    print(f"\n[Log] Streaming log: {log_path}")

    # In chi tiết JSON từng mẫu (giống QA "DETAILED PREDICTIONS") + thêm fol_prediction.
    # eval_print_samples: 0/absent = in TẤT CẢ; >0 = in ngẫu nhiên N mẫu.
    print_n = int(cfg.get("inference", {}).get("eval_print_samples", 0))
    sel = list(range(n)) if print_n <= 0 else sorted(random.sample(range(n), min(print_n, n)))
    if sel:
        print(f"\n{'━'*70}")
        print(f"  DETAILED PREDICTIONS ({len(sel)} samples)")
        print(f"{'━'*70}")
        for i in sel:
            r = results[i]
            detail = {
                "idx": r["idx"],
                "correct": r["correct"],
                "input": {
                    "premises_nl": r["input"]["premises_nl"],
                    "premises_fol": r["input"]["premises_fol_gold"],
                    "question": r["input"]["question"],
                },
                "fol_prediction": r["fol_generated"],
                "gold": r["gold"],
                "prediction": r["prediction"],
            }
            status_full = "✅ CORRECT" if r["correct"] else "❌ WRONG"
            print(f"\n  ── Sample [{r['idx']}] {status_full} ──")
            print(json.dumps(detail, ensure_ascii=False, indent=4))
        print(f"\n{'━'*70}")

    # Summary
    accuracy = correct / total if total > 0 else 0
    avg_total = sum(r["latency"]["total_sec"] for r in results) / total if total > 0 else 0
    avg_fol = sum(r["latency"]["fol_sec"] for r in results) / total if total > 0 else 0
    avg_qa = sum(r["latency"]["qa_sec"] for r in results) / total if total > 0 else 0

    summary = {
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "avg_total_latency_sec": round(avg_total, 3),
        "avg_fol_latency_sec": round(avg_fol, 3),
        "avg_qa_latency_sec": round(avg_qa, 3),
        "slow_samples_count": len(slow_samples),
        "slow_sample_indices": slow_samples,
    }

    print(f"\n{'='*70}")
    print(f"  RESULTS")
    print(f"{'='*70}")
    print(f"  Accuracy     : {correct}/{total} = {accuracy:.1%}")
    print(f"  Avg latency  : {avg_total:.2f}s/sample (FOL:{avg_fol:.2f}s + QA:{avg_qa:.2f}s)")
    if slow_samples:
        print(f"  SLOW (>{slow_threshold}s): {len(slow_samples)} samples -- indices: {slow_samples}")
    print(f"{'='*70}\n")

    # Save summary
    summary_path = output_dir / "ensemble_eval_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"[Log] Summary: {summary_path}")

    # Build full eval log text (giống screenshot)
    eval_log_lines = []
    for r in results:
        idx = r["idx"]
        status = "OK" if r["correct"] else "WRONG"
        pred = r["prediction"]["answer"]
        gold = r["gold"]["answer"]
        t = r["latency"]["total_sec"]
        warn = " !! SLOW" if t > slow_threshold else ""
        eval_log_lines.append(f"[{idx+1:2d}/{total}] {status:5s} pred={pred:8s} gold={gold:8s} time={t:.2f}s{warn}")
    eval_log_text = "\n".join(eval_log_lines)

    # Save eval log text
    eval_log_txt_path = output_dir / "eval_log.txt"
    with open(eval_log_txt_path, "w", encoding="utf-8") as f:
        f.write(eval_log_text + "\n")

    # Push to HF Hub
    hub_cfg = cfg.get("hub", {})
    if hub_cfg.get("push_results", False):
        _push_to_hub(cfg, summary, results, eval_log_text, log_path, summary_path, output_dir)

    return {"summary": summary, "results": results}


def _push_to_hub(cfg: dict, summary: dict, results: list, eval_log_text: str,
                 log_path: Path, summary_path: Path, output_dir: Path):
    """Build README + push log files lên HF Hub."""
    from huggingface_hub import HfApi, create_repo

    hub_cfg = cfg["hub"]
    fol_cfg = cfg["fol_model"]
    qa_cfg = cfg["qa_model"]
    inf_cfg = cfg.get("inference", {})
    slow_threshold = inf_cfg.get("slow_threshold_sec", 60)

    org = hub_cfg.get("org", "")
    repo_name = hub_cfg.get("repo_name", "Logic-Final-Result-V01")
    hub_repo_id = f"{org}/{repo_name}" if org else repo_name
    private = hub_cfg.get("private", False)

    accuracy = summary["accuracy"]
    correct = summary["correct"]
    total = summary["total"]
    avg_total = summary["avg_total_latency_sec"]
    avg_fol = summary["avg_fol_latency_sec"]
    avg_qa = summary["avg_qa_latency_sec"]
    n_slow = summary["slow_samples_count"]
    slow_indices = summary["slow_sample_indices"]

    # Build README
    readme = f"""---
tags:
- logic
- qa
- ensemble
- fol
- chain-of-thought
- education
language:
- en
---

# Logic-Based Educational QA — Ensemble Final Results

## Pipeline

```
NL premises + Question
        |
  Stage 1: FOL Model (NL -> FOL)
  Model: {fol_cfg['hub_repo_id']}
        |
  Stage 2: QA COT Model (NL + FOL + Question -> Answer + Explanation)
  Model: {qa_cfg['hub_repo_id']}
        |
  {{"answer": "B", "explanation": "Premise 1 states..."}}
```

## Models Used

| Stage | Model | Type |
|-------|-------|------|
| FOL (Stage 1) | [{fol_cfg['hub_repo_id']}](https://huggingface.co/{fol_cfg['hub_repo_id']}) | Merged (Qwen2.5-3B) |
| QA (Stage 2) | [{qa_cfg['hub_repo_id']}](https://huggingface.co/{qa_cfg['hub_repo_id']}) | LoRA adapter (Qwen2.5-3B-Instruct) |

## Inference Config

| Parameter | Value |
|-----------|-------|
| FOL max_new_tokens | {fol_cfg.get('max_new_tokens', 400)} |
| QA max_new_tokens | {qa_cfg.get('max_new_tokens', 200)} |
| Quantization | INT8 (bitsandbytes) |
| Decoding | Greedy (do_sample=False) |
| Slow threshold | {slow_threshold}s |

## Results on Test Set

| Metric | Value |
|--------|-------|
| **Accuracy** | **{correct}/{total} ({accuracy:.1%})** |
| Avg total latency | {avg_total:.2f}s / sample |
| Avg FOL latency | {avg_fol:.2f}s / sample |
| Avg QA latency | {avg_qa:.2f}s / sample |
| Slow samples (>{slow_threshold}s) | {n_slow} samples |

## Full Evaluation Log

```
{eval_log_text}
```

## Files

| File | Description |
|------|-------------|
| `ensemble_eval_log.jsonl` | Full detail per sample (NL, FOL gold, FOL generated, question, gold, prediction, latency) |
| `ensemble_eval_summary.json` | Summary statistics |
| `eval_log.txt` | Plain text evaluation log |
| `README.md` | This file |

## Team

**Laplace's Red Devils** — EXACT 2026 Competition
"""

    # Save README locally
    readme_path = output_dir / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)

    # Push to Hub
    print(f"\n[Hub] Pushing to: {hub_repo_id}")
    api = HfApi()
    try:
        create_repo(hub_repo_id, repo_type="dataset", private=private, exist_ok=True)
    except Exception as e:
        print(f"[Hub] create_repo: {e}")

    files_to_upload = [
        (str(readme_path), "README.md"),
        (str(log_path), "ensemble_eval_log.jsonl"),
        (str(summary_path), "ensemble_eval_summary.json"),
        (str(output_dir / "eval_log.txt"), "eval_log.txt"),
    ]
    for local_path, hub_path in files_to_upload:
        if Path(local_path).exists():
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=hub_path,
                repo_id=hub_repo_id,
                repo_type="dataset",
            )
            print(f"  Uploaded: {hub_path}")

    print(f"[Hub] Done: https://huggingface.co/datasets/{hub_repo_id}")


# ─── Inference Mode ───────────────────────────────────────────────────────────

def inference(pipeline: EnsemblePipeline, input_path: str, cfg: dict):
    """Inference (không có gold) → sinh answer + explanation."""
    output_dir = Path(cfg.get("output_dir", str(resolve_project_root() / "outputs" / "ensemble")))
    output_dir.mkdir(parents=True, exist_ok=True)

    data = load_inference_json(input_path)
    slow_threshold = cfg.get("inference", {}).get("slow_threshold_sec", 60)

    print(f"\n{'='*70}")
    print(f"  ENSEMBLE INFERENCE — {len(data)} samples")
    print(f"{'='*70}\n")

    # Gom input
    premises_nl_list = [item["premises_nl"] for item in data]
    questions = [item["question"] for item in data]
    n = len(data)

    # 2 PHA — mỗi thời điểm chỉ 1 LLM trong VRAM (tuân thủ luật BTC)
    fol_results = pipeline.generate_fol_all(premises_nl_list)
    items = [(premises_nl_list[i], fol_results[i]["premises_fol"], questions[i]) for i in range(n)]
    qa_results = pipeline.answer_all(items)

    results = []
    slow_samples = []
    print(f"\n{'='*70}\n  Tổng hợp kết quả\n{'='*70}")
    for i in range(n):
        fol_lat = fol_results[i]["fol_latency_sec"]
        qa_lat = qa_results[i]["qa_latency_sec"]
        total_lat = fol_lat + qa_lat

        latency_warn = ""
        if total_lat > slow_threshold:
            latency_warn = " ⚠️ SLOW"
            slow_samples.append(i)

        print(
            f"  [{i+1:3d}/{n}] answer={qa_results[i]['answer']:8s} "
            f"| FOL:{fol_lat:.1f}s QA:{qa_lat:.1f}s Total:{total_lat:.1f}s{latency_warn}"
        )

        results.append({
            "idx": i,
            "premises_nl": premises_nl_list[i],
            "question": questions[i],
            "answer": qa_results[i]["answer"],
            "explanation": qa_results[i]["explanation"],
            "premises_fol_generated": fol_results[i]["premises_fol"],
            "fol_latency_sec": round(fol_lat, 3),
            "qa_latency_sec": round(qa_lat, 3),
            "total_latency_sec": round(total_lat, 3),
        })

    # In chi tiết JSON từng mẫu: fol_prediction + prediction{answer, explanation}.
    # eval_print_samples: 0/absent = in TẤT CẢ; >0 = in ngẫu nhiên N mẫu.
    print_n = int(cfg.get("inference", {}).get("eval_print_samples", 0))
    sel = list(range(n)) if print_n <= 0 else sorted(random.sample(range(n), min(print_n, n)))
    if sel:
        print(f"\n{'━'*70}")
        print(f"  DETAILED PREDICTIONS ({len(sel)} samples)")
        print(f"{'━'*70}")
        for i in sel:
            r = results[i]
            detail = {
                "idx": r["idx"],
                "input": {
                    "premises_nl": r["premises_nl"],
                    "question": r["question"],
                },
                "fol_prediction": r["premises_fol_generated"],
                "prediction": {
                    "answer": r["answer"],
                    "explanation": r["explanation"],
                },
            }
            print(f"\n  ── Sample [{r['idx']}] ──")
            print(json.dumps(detail, ensure_ascii=False, indent=4))
        print(f"\n{'━'*70}")

    avg_total = sum(r["total_latency_sec"] for r in results) / len(results) if results else 0

    print(f"\n{'='*70}")
    print(f"  Avg latency: {avg_total:.2f}s/sample")
    if slow_samples:
        print(f"  ⚠️  SLOW (>{slow_threshold}s): {len(slow_samples)} samples — indices: {slow_samples}")
    print(f"{'='*70}\n")

    out_path = output_dir / "ensemble_inference_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[Log] Saved to: {out_path}")

    return results


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ensemble: FOL + QA Pipeline")
    parser.add_argument("--config", type=str, default="configs/ensemble_model.yaml")
    parser.add_argument("--mode", type=str, default="evaluate", choices=["evaluate", "inference"])
    parser.add_argument("--input", type=str, default=None, help="Input JSON for inference mode")
    args = parser.parse_args()

    cfg = load_config(args.config)
    pipeline = EnsemblePipeline(cfg)

    if args.mode == "evaluate":
        evaluate(pipeline, cfg)
    elif args.mode == "inference":
        if not args.input:
            raise ValueError("--input required for inference mode")
        inference(pipeline, args.input, cfg)


if __name__ == "__main__":
    main()
