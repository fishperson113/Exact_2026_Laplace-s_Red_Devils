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
    format_options,
    format_premises_fol,
    format_premises_nl,
    neutralize_epistemic_fol,
)
from models.QA_model.postprocess import clean_explanation, snap_answer_to_options


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
    premises_used: list[int] = field(default_factory=list)
    reasoning_steps: list[str] = field(default_factory=list)
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
                 options: list[str] | None = None,
                 max_new_tokens: int = 200) -> dict[str, str]:
        """NL + FOL + options + question → {answer, explanation, premises_used, reasoning_steps}."""
        # Lưới an toàn: ô FOL của mệnh đề epistemic → giữ NL gắn cờ [UNCERTAIN] (khớp QA_model/inference
        # + build SFT). Bất kể Model 1 sinh gì, QA không bao giờ suy ¬X từ "vắng mặt thông tin".
        premises_fol = neutralize_epistemic_fol(premises_nl, premises_fol)
        user_content = USER_TEMPLATE_QA_COT.format(
            premises_nl_block=format_premises_nl(premises_nl),
            premises_fol_block=format_premises_fol(premises_fol),
            options_block=format_options(options or []),
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
        for item in items:
            nl, fol, q = item[0], item[1], item[2]
            options = item[3] if len(item) > 3 else []   # (nl, fol, q, options) — options có thể rỗng
            fol = neutralize_epistemic_fol(nl, fol)      # epistemic → giữ NL gắn cờ [UNCERTAIN]
            user_content = USER_TEMPLATE_QA_COT.format(
                premises_nl_block=format_premises_nl(nl),
                premises_fol_block=format_premises_fol(fol),
                options_block=format_options(options or []),
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

    _STEP_PREFIXES = ("Rule:", "Fact:", "Derive:", "Conclusion:")

    @classmethod
    def _parse_output(cls, text: str) -> dict:
        """Parse output dạng <reasoning steps> + JSON cuối {premises_used, explanation, answer}.

        ĐỒNG NHẤT với QA_model/inference.py + train.py: trả answer, explanation,
        premises_used, reasoning_steps (robust với JSON cụt/lỗi).
        """
        reasoning_steps = [ln.strip() for ln in text.split("\n")
                           if ln.strip().startswith(cls._STEP_PREFIXES)]

        def _premises(parsed) -> list:
            pu = parsed.get("premises_used", [])
            out = []
            if isinstance(pu, list):
                for v in pu:
                    try:
                        out.append(int(v))
                    except (ValueError, TypeError):
                        pass
            return out

        def _from_expl(expl) -> list:
            # premises_used CHUẨN = các "premise N" model tự trích trong explanation (0-based).
            return sorted({int(n) for n in re.findall(r"premise\s+(\d+)", expl or "", re.I)})

        # 1. JSON CUỐI cùng có "answer"
        for m in reversed(list(re.finditer(r"\{.*?\}", text, re.DOTALL))):
            try:
                parsed = json.loads(m.group())
            except json.JSONDecodeError:
                continue
            if "answer" in parsed:
                expl = str(parsed.get("explanation", "")).strip()
                pu_expl = _from_expl(expl)
                return {
                    "answer": str(parsed["answer"]).strip(),
                    "explanation": expl,
                    "premises_used": pu_expl if pu_expl else _premises(parsed),
                    "reasoning_steps": reasoning_steps,
                }

        # 2. JSON cụt/lỗi: moi từng trường (explanation NON-GREEDY → hết rác)
        m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
        if m:
            em = re.search(r'"explanation"\s*:\s*"(.*?)"\s*[,}]', text, re.DOTALL)
            pm = re.search(r'"premises_used"\s*:\s*\[([^\]]*)\]', text)
            expl = em.group(1).strip() if em else ""
            pu_model = [int(x) for x in re.findall(r"\d+", pm.group(1))] if pm else []
            pu_expl = _from_expl(expl)
            return {
                "answer": m.group(1).strip(),
                "explanation": expl,
                "premises_used": pu_expl if pu_expl else pu_model,
                "reasoning_steps": reasoning_steps,
            }

        # 3. Last-resort: Conclusion hoặc cue, KHÔNG đoán bừa A/B/C/D
        concl = next((s for s in reversed(reasoning_steps) if s.startswith("Conclusion:")), "")
        m2 = re.search(r"\b(Yes|No|Unknown|Uncertain|[ABCD])\b\s*$", concl)
        if not m2:
            m2 = re.search(
                r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|Uncertain|[ABCD])\b",
                text, re.I,
            )
        if m2:
            return {"answer": m2.group(1), "explanation": "",
                    "premises_used": [], "reasoning_steps": reasoning_steps}
        for label in ("Uncertain", "Unknown", "Yes", "No"):
            if re.search(rf"\b{label}\b", text):
                return {"answer": label, "explanation": "",
                        "premises_used": [], "reasoning_steps": reasoning_steps}
        return {"answer": "Uncertain", "explanation": "",
                "premises_used": [], "reasoning_steps": reasoning_steps}


# ─── Ensemble Pipeline ────────────────────────────────────────────────────────

class EnsemblePipeline:
    """FOL Model + QA Model. 2 chế độ nạp (config inference.load_both_models):

      - load_both_models=True (MẶC ĐỊNH): nạp CẢ 2 model 1 lần, GIỮ resident
        (BTC cho phép 2 LLM/VRAM). FOL sinh hết → QA sinh hết, KHÔNG unload/reload.
        Nhanh hơn nhiều khi serving (nhiều lượt /predict không phải nạp lại model).
      - load_both_models=False: 2-pha cũ — nạp FOL → unload → nạp QA (máy thiếu VRAM).

    `generate_fol_all` / `answer_all` cache model (`self._fol`, `self._qa`) → tái dùng
    qua nhiều lượt gọi. Tốc độ thật do BATCH generation + giữ model resident.
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
        # Ablation: use_fol=False → BỎ pha FOL, QA nhận NL + FOL RỖNG (cùng prompt train)
        # → đo đóng góp thuần của FOL mà KHÔNG đổi prompt (so sánh công bằng).
        self.use_fol = bool(inf_cfg.get("use_fol", True))
        # load_both_models=True → nạp CẢ 2 model, GIỮ resident (BTC cho phép 2 LLM/VRAM).
        # Tránh unload/reload giữa pha & giữa các lượt /predict → nhanh hơn nhiều khi serving.
        # False → 2-pha cũ (load FOL → unload → load QA) cho máy thiếu VRAM.
        self.load_both = bool(inf_cfg.get("load_both_models", True))
        self._fol = None   # cache model đã nạp (None = chưa nạp)
        self._qa = None

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
        if self._fol is None:
            print(f"\n[FOL] Nạp FOL model… batch_size={bs} (load_both={self.load_both})")
            self._fol = FOLModel(self.fol_repo, self.load_8bit)
            print(f"[VRAM] sau khi nạp FOL: {self._vram_gb():.2f} GB")
        fol_model = self._fol
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
        if not self.load_both:   # 2-pha: giải phóng FOL trước khi nạp QA
            self._unload(fol_model); self._fol = None
            print(f"[VRAM] sau khi GIẢI PHÓNG FOL: {self._vram_gb():.2f} GB")
        return out

    def run_fol_stage(self, premises_nl_list: list[list[str]]) -> list[dict]:
        """PHA 1 — sinh FOL (use_fol=True) HOẶC bỏ FOL cho ablation (use_fol=False).

        Ablation: KHÔNG nạp FOL model, trả FOL rỗng → QA dùng ĐÚNG prompt train
        nhưng block FOL trống. Chỉ đổi 1 biến (có/không FOL), prompt giữ nguyên.
        """
        if self.use_fol:
            return self.generate_fol_all(premises_nl_list)
        print("\n[ABLATION] use_fol=False → BỎ pha FOL. QA nhận NL + FOL RỖNG (prompt train giữ nguyên).")
        return [{"premises_fol": [], "fol_raw": "", "fol_latency_sec": 0.0}
                for _ in premises_nl_list]

    # ───── PHA 2: chỉ QA trong VRAM ─────
    def answer_all(self, items: list[tuple]) -> list[dict]:
        n = len(items)
        bs = self.batch_size
        if self._qa is None:
            print(f"\n[QA] Nạp QA model… batch_size={bs} (load_both={self.load_both})")
            self._qa = QAModel(self.qa_repo, self.load_8bit)
            print(f"[VRAM] sau khi nạp QA: {self._vram_gb():.2f} GB"
                  + ("  (cả FOL+QA cùng resident)" if self.load_both and self._fol is not None else ""))
        qa_model = self._qa
        out: list[dict] = []
        for s in range(0, n, bs):
            chunk = items[s:s + bs]
            t0 = time.perf_counter()
            batch_res = qa_model.generate_batch(chunk, self.qa_max_new_tokens)
            dt = time.perf_counter() - t0
            per = dt / len(chunk)
            for res in batch_res:
                out.append({
                    "answer": res["answer"], "explanation": res["explanation"],
                    "premises_used": res.get("premises_used", []),
                    "reasoning_steps": res.get("reasoning_steps", []),
                    "qa_latency_sec": per,
                })
            print(f"  [QA {min(s + bs, n):3d}/{n}] batch {len(chunk)} → {dt:.1f}s ({per:.1f}s/mẫu)", flush=True)
        if not self.load_both:
            self._unload(qa_model); self._qa = None
            print(f"[VRAM] sau khi GIẢI PHÓNG QA: {self._vram_gb():.2f} GB")
        return out

    # ───── Chế độ INTERLEAVE: load CẢ 2 model, mỗi mẫu FOL→QA liền mạch ─────
    def load_models(self) -> None:
        """Nạp CẢ 2 model 1 lần, giữ resident (BTC cho phép). Gọi trước khi inference."""
        if self.use_fol and self._fol is None:
            print("[LOAD] FOL model…")
            self._fol = FOLModel(self.fol_repo, self.load_8bit)
            print(f"[VRAM] sau khi nạp FOL: {self._vram_gb():.2f} GB")
        if self._qa is None:
            print("[LOAD] QA model…")
            self._qa = QAModel(self.qa_repo, self.load_8bit)
            print(f"[VRAM] CẢ 2 model resident: {self._vram_gb():.2f} GB")

    def process_one(self, premises_nl: list[str], question: str,
                    options: list[str] | None = None) -> dict:
        """1 mẫu: FOL → QA liền mạch (như /predict thật). Trả kèm fol/qa latency riêng."""
        self.load_models()
        t0 = time.perf_counter()
        if self.use_fol:
            fol, fol_raw = self._fol.generate(premises_nl, self.fol_max_new_tokens)
        else:
            fol, fol_raw = [], ""
        fol_time = time.perf_counter() - t0
        t1 = time.perf_counter()
        qa = self._qa.generate(premises_nl, fol, question, options=options,
                               max_new_tokens=self.qa_max_new_tokens)
        qa_time = time.perf_counter() - t1
        return {
            "premises_fol": fol, "fol_raw": fol_raw,
            "answer": qa["answer"], "explanation": qa["explanation"],
            "premises_used": qa.get("premises_used", []),
            "reasoning_steps": qa.get("reasoning_steps", []),
            "fol_latency_sec": fol_time, "qa_latency_sec": qa_time,
        }

    def run_interleaved(self, premises_nl_list: list[list[str]], questions: list[str],
                        options_list: list[list[str]], slow_threshold: float = 60.0):
        """Mỗi mẫu FOL→QA liền, IN time ngay khi xong (giống logic_solution + /predict).
        Trả (fol_results, qa_results) cùng cấu trúc 2-pha → downstream dùng y nguyên."""
        self.load_models()
        n = len(premises_nl_list)
        print(f"\n[INTERLEAVE] {n} mẫu — mỗi mẫu FOL→QA liền (2 model resident)")
        fol_results, qa_results = [], []
        for i in range(n):
            opts = options_list[i] if i < len(options_list) else []
            r = self.process_one(premises_nl_list[i], questions[i], opts)
            fol_results.append({"premises_fol": r["premises_fol"], "fol_raw": r["fol_raw"],
                                "fol_latency_sec": r["fol_latency_sec"]})
            qa_results.append({"answer": r["answer"], "explanation": r["explanation"],
                               "premises_used": r["premises_used"],
                               "reasoning_steps": r["reasoning_steps"],
                               "qa_latency_sec": r["qa_latency_sec"]})
            tot = r["fol_latency_sec"] + r["qa_latency_sec"]
            warn = " ⚠️ SLOW" if tot > slow_threshold else ""
            print(f"  [{i + 1:3d}/{n}] FOL:{r['fol_latency_sec']:5.1f}s  QA:{r['qa_latency_sec']:5.1f}s  "
                  f"Total:{tot:5.1f}s{warn} | answer={str(r['answer'])[:45]}", flush=True)
        return fol_results, qa_results


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

    # Gom input — tên BTC: premises/query/options (fallback tên cũ premises_nl/question)
    premises_nl_list, questions, options_list, golds, gold_expls, fol_golds = [], [], [], [], [], []
    for _, row in df.iterrows():
        premises_nl_list.append(parse_list_field(row.get("premises", row.get("premises_nl"))))
        questions.append(str(row.get("query", row.get("question", ""))))
        options_list.append(parse_list_field(row.get("options", "[]")))
        golds.append(str(row["answer"]).strip())
        gold_expls.append(str(row.get("explanation", "")))
        fol_golds.append(parse_list_field(row.get("premises_fol", "[]")))

    # INTERLEAVE: load CẢ 2 model, mỗi mẫu FOL→QA liền mạch + in time ngay (giống logic_solution)
    fol_results, qa_results = pipeline.run_interleaved(
        premises_nl_list, questions, options_list, slow_threshold)

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
        pred = snap_answer_to_options(qa_results[i]["answer"], options_list[i])
        expl = clean_explanation(qa_results[i]["explanation"])
        gold_answer = golds[i]

        _na = lambda s: re.sub(r"\s+", " ", str(s).strip().lower()).rstrip(" .;:!?")
        is_correct = _na(pred) == _na(gold_answer)
        correct += int(is_correct)

        status = "✓" if is_correct else "✗"
        if total_lat > slow_threshold:
            slow_samples.append(i)
        # time đã in live ở run_interleaved → đây chỉ tổng hợp đúng/sai (answer full-text → cắt 35)
        print(f"  [{i+1:3d}/{n}] {status} pred={str(pred)[:35]:35s} gold={str(gold_answer)[:35]}",
              flush=True)

        sample_record = {
            "idx": i,
            "correct": is_correct,
            "input": {
                "query": questions[i],
                "premises": premises_nl_list[i],
                "options": options_list[i],
                "premises_fol_gold": fol_golds[i],
            },
            "fol_generated": fol_results[i]["premises_fol"],
            "gold": {
                "answer": gold_answer,
                "explanation": gold_expls[i],
            },
            "prediction": {
                "answer": pred,
                "premises_used": qa_results[i].get("premises_used", []),
                "reasoning_steps": qa_results[i].get("reasoning_steps", []),
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
                    "query": r["input"]["query"],
                    "premises": r["input"]["premises"],
                    "options": r["input"]["options"],
                    "premises_fol": r["input"]["premises_fol_gold"],
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

    # Gom input — BTC: query/premises/options (fallback tên cũ)
    premises_nl_list = [item.get("premises", item.get("premises_nl")) for item in data]
    questions = [item.get("query", item.get("question", "")) for item in data]
    options_list = [item.get("options", []) for item in data]
    n = len(data)

    # INTERLEAVE: load CẢ 2 model, mỗi mẫu FOL→QA liền mạch + in time ngay (giống logic_solution)
    fol_results, qa_results = pipeline.run_interleaved(
        premises_nl_list, questions, options_list, slow_threshold)

    results = []
    slow_samples = []
    print(f"\n{'='*70}\n  Tổng hợp kết quả\n{'='*70}")
    for i in range(n):
        fol_lat = fol_results[i]["fol_latency_sec"]
        qa_lat = qa_results[i]["qa_latency_sec"]
        total_lat = fol_lat + qa_lat

        if total_lat > slow_threshold:
            slow_samples.append(i)
        # (đã in time live trong run_interleaved — không in lại ở đây)

        results.append({
            "idx": i,
            "query": questions[i],
            "premises": premises_nl_list[i],
            "options": options_list[i],
            "answer": snap_answer_to_options(qa_results[i]["answer"], options_list[i]),
            "premises_used": qa_results[i].get("premises_used", []),
            "reasoning_steps": qa_results[i].get("reasoning_steps", []),
            "explanation": clean_explanation(qa_results[i]["explanation"]),
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
                    "query": r["query"],
                    "premises": r["premises"],
                    "options": r["options"],
                },
                "fol_prediction": r["premises_fol_generated"],
                "prediction": {
                    "answer": r["answer"],
                    "premises_used": r.get("premises_used", []),
                    "reasoning_steps": r.get("reasoning_steps", []),
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
