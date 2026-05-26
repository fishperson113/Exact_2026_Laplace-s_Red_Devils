"""Huấn luyện LoRA SFT: premises NL → premises FOL (JSON)."""
from __future__ import annotations

import gc
import inspect
import json
import os
import shutil
from pathlib import Path
from typing import Any

import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Unsloth patch TRL/SFT (vd. SFTConfig.eos_token placeholder): cộng đồng + tài liệu Unsloth khuyên import *trước* `trl`.
try:
    from unsloth import FastLanguageModel as _UnslothFastLanguageModel  # noqa: F401
except ImportError:
    try:
        import unsloth  # noqa: F401
    except ImportError:
        pass

from transformers import EarlyStoppingCallback
from transformers.trainer_callback import TrainerCallback
from trl import SFTConfig, SFTTrainer

from data.fol_dataset import build_fol_dataset_dict
from services.config_fol import FolSFTConfig, fol_should_load_in_8bit

from .experiment_log import (
    build_fol_experiment_log_document,
    write_experiment_log_json,
)
from .tokenizer_fix import scrub_sft_config_eos_pad_args, sync_eos_token_string_with_id
from .fol_preflight import load_preflight_baseline, mean_nll_completion_on_split
from .generation_fol_eval import (
    benchmark_fol_greedy_latency_per_sample,
    collect_fol_inference_samples,
    fol_exact_match_on_splits,
    fol_exact_match_rate,
)


def _fol_metric_key_for_best(metric_for_best_model: str | None) -> str:
    """Khớp logic HF ``_determine_best_metric``: thiếu tiền tố ``eval_`` thì thêm."""
    if not metric_for_best_model:
        return "eval_loss"
    m = str(metric_for_best_model).strip()
    return m if m.startswith("eval_") else f"eval_{m}"


def _fol_best_metric_uses_dev_exact_match(metric_for_best_model: str | None) -> bool:
    m = (metric_for_best_model or "").strip().lower()
    if m.startswith("eval_"):
        m = m[5:]
    return "exact_match" in m


class FolDevExactMatchForBestModelCallback(TrainerCallback):
    """Trước EarlyStopping: greedy exact-match trên **dev**, ghi ``eval_exact_match_rate`` vào ``metrics``."""

    def __init__(self, cfg: FolSFTConfig, dev_dataset: Any):
        self.cfg = cfg
        self.dev_dataset = dev_dataset
        self.suppress_exact_match_metric = False
        self.trainer_ref: Any | None = None

    def on_evaluate(
        self,
        args: Any,
        state: Any,
        control: Any,
        metrics: dict[str, Any] | None,
        model: Any = None,
        processing_class: Any = None,
        **kwargs: Any,
    ) -> None:
        if metrics is None or self.suppress_exact_match_metric:
            return
        if not _fol_best_metric_uses_dev_exact_match(getattr(args, "metric_for_best_model", None)):
            return
        tok = processing_class or kwargs.get("tokenizer")
        if model is None or tok is None:
            return
        r = fol_exact_match_rate(
            self.cfg,
            model,
            tok,
            self.dev_dataset,
            max_samples=self.cfg.best_model_exact_match_max_samples,
            split_label="dev_best_model_metric",
        )
        rate = float(r["exact_match_rate"])
        metrics["eval_exact_match_rate"] = rate
        tr = self.trainer_ref
        if tr is not None and getattr(tr, "is_world_process_zero", lambda: True)():
            tr.log({"eval_exact_match_rate": rate, "epoch": state.epoch})


def _fol_prune_trainer_checkpoint_dirs(out_dir: Path) -> int:
    """Xóa các thư mục ``checkpoint-*`` do Trainer tạo trong ``out_dir`` (sau khi đã lưu bản chính vào ``final_lora``)."""
    if not out_dir.is_dir():
        return 0
    n = 0
    for p in sorted(out_dir.iterdir()):
        if p.is_dir() and p.name.startswith("checkpoint-"):
            shutil.rmtree(p, ignore_errors=True)
            n += 1
    return n


def _strip_notebook_progress_callback(trainer: Any) -> None:
    """Trong Jupyter/Colab, ``NotebookProgressCallback.on_train_end`` đặt ``training_tracker = None``;
    gọi ``trainer.evaluate()`` **sau** ``train()`` sẽ lỗi ``on_train_begin must be called before on_evaluate``.
    Gỡ callback này trước các lần evaluate hậu huấn luyện.
    """
    try:
        from transformers.utils.notebook import NotebookProgressCallback
    except ImportError:
        return
    removed = trainer.pop_callback(NotebookProgressCallback)
    if removed is not None:
        print(
            "[FOL train] Đã gỡ NotebookProgressCallback (notebook) để evaluate sau train không crash.",
            flush=True,
        )


def _fol_cuda_bootstrap() -> None:
    """Giảm phân mảnh VRAM + dọn cache trước train (đặc biệt T4 ~15GB)."""
    os.environ.setdefault("PYTORCH_ALLOC_CONF", "expandable_segments:True")
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def load_tokenizer(cfg: FolSFTConfig):
    tok = AutoTokenizer.from_pretrained(
        cfg.model_name, trust_remote_code=cfg.trust_remote_code
    )
    sync_eos_token_string_with_id(tok)
    if tok.pad_token is None or tok.pad_token in ("<EOS_TOKEN>", "<PAD_TOKEN>"):
        tok.pad_token = tok.eos_token
    # Decoder-only + batched generate: pad bên trái để token cuối cùng của prompt nằm sát phải.
    tok.padding_side = "left"
    return tok


def build_model(cfg: FolSFTConfig):
    if fol_should_load_in_8bit(cfg):
        print("[FOL train] Nạp base weights: INT8 8-bit (BitsAndBytes), tiết kiệm VRAM hơn full fp16/bf16.", flush=True)
        bnb_config = BitsAndBytesConfig(load_in_8bit=True)
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            quantization_config=bnb_config,
            device_map={"": 0},
            trust_remote_code=cfg.trust_remote_code,
            attn_implementation="sdpa",
        )
        model = prepare_model_for_kbit_training(model)
        train_bf16, train_fp16 = False, True
    else:
        dtype = torch.bfloat16 if cfg.bf16 else torch.float16
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            torch_dtype=dtype,
            trust_remote_code=cfg.trust_remote_code,
            device_map={"": 0},
            attn_implementation="sdpa",
        )
        train_bf16, train_fp16 = cfg.bf16, not cfg.bf16

    model.config.use_cache = False
    peft_config = LoraConfig(
        r=cfg.lora_r,
        lora_alpha=cfg.lora_alpha,
        lora_dropout=cfg.lora_dropout,
        target_modules=list(cfg.lora_target_modules),
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    if cfg.gradient_checkpointing:
        model.enable_input_require_grads()
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )
    return model, train_bf16, train_fp16


def _build_fol_sft_config(
    cfg: FolSFTConfig,
    train_bf16: bool,
    train_fp16: bool,
    tokenizer: Any | None = None,
) -> SFTConfig:
    optim = "adamw_8bit" if cfg.use_adamw_8bit else "adamw_torch"
    sft_kw: dict[str, Any] = dict(
        output_dir=str(cfg.out_dir),
        num_train_epochs=cfg.num_train_epochs,
        per_device_train_batch_size=cfg.per_device_train_batch_size,
        per_device_eval_batch_size=cfg.per_device_eval_batch_size,
        gradient_accumulation_steps=cfg.gradient_accumulation_steps,
        learning_rate=cfg.learning_rate,
        warmup_ratio=cfg.warmup_ratio,
        lr_scheduler_type="cosine",
        weight_decay=cfg.weight_decay,
        logging_steps=cfg.logging_steps,
        logging_strategy="steps",
        logging_first_step=True,
        disable_tqdm=False,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=max(1, int(cfg.save_total_limit)),
        load_best_model_at_end=cfg.load_best_model_at_end,
        metric_for_best_model=cfg.metric_for_best_model,
        greater_is_better=cfg.greater_is_better,
        bf16=train_bf16,
        fp16=train_fp16,
        optim=optim,
        gradient_checkpointing=False,
        seed=cfg.train_seed,
        report_to="none",
        max_length=cfg.max_seq_length,
        dataset_text_field="text",
        packing=False,
        remove_unused_columns=False,
    )
    if "max_seq_length" in inspect.signature(SFTConfig.__init__).parameters:
        sft_kw["max_seq_length"] = cfg.max_seq_length
    if "eval_accumulation_steps" in inspect.signature(SFTConfig.__init__).parameters:
        sft_kw["eval_accumulation_steps"] = max(1, int(cfg.eval_accumulation_steps))
    cfg_out = SFTConfig(**sft_kw)
    if tokenizer is not None:
        scrub_sft_config_eos_pad_args(cfg_out, tokenizer)
    return cfg_out


def _epoch_metrics_from_history(trainer: SFTTrainer) -> list[dict]:
    rows: list[dict] = []
    for h in trainer.state.log_history:
        if "eval_loss" not in h and "eval_exact_match_rate" not in h:
            continue
        row: dict[str, Any] = {
            "epoch": h.get("epoch"),
            "step": h.get("step"),
            "eval_loss": h.get("eval_loss"),
        }
        if "eval_exact_match_rate" in h:
            row["eval_exact_match_rate"] = h.get("eval_exact_match_rate")
        rows.append(row)
    return rows


def _persist_fol_experiment_log(
    cfg: FolSFTConfig,
    trainer: SFTTrainer,
    train_result,
    train_metrics_final: dict | None,
    fol_eval: dict | None,
    filter_stats: dict | None,
    fol_inference_samples: list | None,
    *,
    fol_preflight_baseline: dict | None = None,
    fol_test_benchmark: dict | None = None,
    fol_inference_latency_benchmark: dict | None = None,
) -> None:
    if cfg.out_dir is None:
        return
    tr_metrics = getattr(train_result, "metrics", None) or {}
    doc = build_fol_experiment_log_document(
        cfg,
        epoch_metrics=_epoch_metrics_from_history(trainer),
        trainer_log_history=[dict(x) for x in trainer.state.log_history],
        train_metrics_final=train_metrics_final,
        train_result_global_step=getattr(train_result, "global_step", None),
        train_result_epochs=(
            float(trainer.state.epoch)
            if getattr(trainer.state, "epoch", None) is not None
            else tr_metrics.get("epoch")
        ),
        fol_eval=fol_eval,
        filter_stats=filter_stats,
        fol_inference_samples=fol_inference_samples,
        fol_preflight_baseline=fol_preflight_baseline,
        fol_test_benchmark=fol_test_benchmark,
        fol_inference_latency_benchmark=fol_inference_latency_benchmark,
    )
    write_experiment_log_json(cfg.out_dir / "experiment_log.json", doc)


def run_fol_eval_all_splits(
    cfg: FolSFTConfig,
    trainer: SFTTrainer,
    dataset_dict,
) -> dict[str, Any]:
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    lim = cfg.eval_fol_max_samples
    out = fol_exact_match_on_splits(
        cfg,
        trainer.model,
        tok,
        dataset_dict,
        splits=("train", "dev", "test"),
        max_samples=lim,
    )
    for split, m in out.items():
        print(
            f"[FOL eval] {split}: accuracy={m['exact_match_rate']:.4f} "
            f"({m['exact_match_count']}/{m['total']})"
        )
    if cfg.out_dir:
        with open(cfg.out_dir / "fol_eval_metrics.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
    return out


def run_training(cfg: FolSFTConfig):
    if not cfg.run_train:
        return None

    _fol_cuda_bootstrap()
    print("[FOL train] Bắt đầu: tokenizer + dataset + model (bước này có thể vài phút, chưa có thanh epoch).", flush=True)

    if cfg.use_unsloth:
        from .unsloth_sft import (
            apply_train_on_responses_only,
            is_unsloth_available,
            load_unsloth_model_and_tokenizer,
            unsloth_import_error_detail,
        )

        if not is_unsloth_available():
            import sys

            detail = unsloth_import_error_detail() or "import unsloth trả về lỗi (không có chi tiết)."
            raise RuntimeError(
                "cfg.use_unsloth=True nhưng không import được `unsloth` (pip có thể đã cài vào Python khác kernel đang chạy).\n"
                f"  → Chi tiết: {detail}\n"
                f"  → Python đang chạy: {sys.executable}\n"
                "  → Thử: trong notebook `%pip install unsloth` rồi **restart kernel**, hoặc `python -m pip install unsloth` "
                "trùng interpreter trên.\n"
                "  → Hoặc tắt Unsloth: FOL_USE_UNSLOTH=false / FolSFTConfig.from_env(use_unsloth=False)."
            )
        model, tokenizer, train_bf16, train_fp16 = load_unsloth_model_and_tokenizer(cfg)
        print("[FOL train] Đã nạp tokenizer (Unsloth).", flush=True)
        dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
    else:
        tokenizer = load_tokenizer(cfg)
        print("[FOL train] Đã nạp tokenizer.", flush=True)
        dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
        model, train_bf16, train_fp16 = build_model(cfg)

    print(
        "[FOL train] Dataset:",
        {k: len(dataset_dict[k]) for k in dataset_dict},
        "| filter_stats:",
        filter_stats,
        flush=True,
    )
    if not cfg.use_unsloth:
        print("[FOL train] Đã nạp model + LoRA. Chuẩn bị SFTTrainer.train() (tqdm từng epoch/step sẽ hiện bên dưới).", flush=True)
    else:
        print(
            "[FOL train][Unsloth] Dataset xong. optim="
            + ("adamw_8bit" if cfg.use_adamw_8bit else "adamw_torch")
            + "; train_on_responses_only="
            + str(cfg.unsloth_train_on_responses_only)
            + ".",
            flush=True,
        )

    assert cfg.out_dir is not None and cfg.checkpoint_dir is not None

    sft_config = _build_fol_sft_config(cfg, train_bf16, train_fp16, tokenizer)
    scrub_sft_config_eos_pad_args(sft_config, tokenizer)
    # TRL: chỉ khi None mới lấy theo tokenizer; gán rõ None tránh chuỗi lỗi từ metadata/CLI lọt vào SFTConfig.
    sft_config.eos_token = None
    sft_config.pad_token = None

    trainer_kwargs = dict(
        model=model,
        args=sft_config,
        train_dataset=dataset_dict["train"],
        eval_dataset=dataset_dict["dev"],
    )
    if "processing_class" in inspect.signature(SFTTrainer.__init__).parameters:
        trainer_kwargs["processing_class"] = tokenizer
    else:
        trainer_kwargs["tokenizer"] = tokenizer
    fol_em_cb: FolDevExactMatchForBestModelCallback | None = None
    _callbacks: list[Any] = []
    if _fol_best_metric_uses_dev_exact_match(cfg.metric_for_best_model):
        fol_em_cb = FolDevExactMatchForBestModelCallback(cfg, dataset_dict["dev"])
        _callbacks.append(fol_em_cb)
        print(
            f"[FOL train] Chọn checkpoint theo {_fol_metric_key_for_best(cfg.metric_for_best_model)!r} "
            f"(greedy exact-match trên dev; best_model_exact_match_max_samples="
            f"{cfg.best_model_exact_match_max_samples!r}).",
            flush=True,
        )
    if _fol_best_metric_uses_dev_exact_match(cfg.metric_for_best_model) and not cfg.greater_is_better:
        print(
            "[FOL train] Cảnh báo: metric exact-match nên đặt greater_is_better=true (tỉ lệ cao hơn = tốt hơn).",
            flush=True,
        )
    if int(getattr(cfg, "early_stopping_patience", 0) or 0) > 0:
        _callbacks.append(
            EarlyStoppingCallback(early_stopping_patience=int(cfg.early_stopping_patience))
        )
        print(
            f"[FOL train] EarlyStoppingCallback(patience={cfg.early_stopping_patience}), "
            f"metric={cfg.metric_for_best_model!r}, greater_is_better={cfg.greater_is_better}",
            flush=True,
        )
    if _callbacks:
        trainer_kwargs["callbacks"] = _callbacks
    trainer = SFTTrainer(**trainer_kwargs)
    if fol_em_cb is not None:
        fol_em_cb.trainer_ref = trainer

    if cfg.use_unsloth and cfg.unsloth_train_on_responses_only:
        print("[FOL train][Unsloth] Áp train_on_responses_only (loss chỉ trên assistant) …", flush=True)
        trainer = apply_train_on_responses_only(trainer, cfg)
        if fol_em_cb is not None:
            fol_em_cb.trainer_ref = trainer

    print("[FOL train] Bắt đầu trainer.train() …", flush=True)
    train_result = trainer.train()
    print("[FOL train] trainer.train() xong.", flush=True)
    _strip_notebook_progress_callback(trainer)
    cfg.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(cfg.checkpoint_dir))
    tokenizer.save_pretrained(str(cfg.checkpoint_dir))
    if cfg.delete_output_checkpoints_after_save and cfg.out_dir is not None:
        pruned = _fol_prune_trainer_checkpoint_dirs(cfg.out_dir)
        if pruned:
            print(
                f"[FOL train] Đã xóa {pruned} thư mục checkpoint-* trong {cfg.out_dir} "
                "(bản dùng tiếp theo: checkpoint_dir / final_lora).",
                flush=True,
            )

    _fol_cuda_bootstrap()
    print("[FOL train] trainer.evaluate() trên dev (loss) …", flush=True)
    metrics = trainer.evaluate()
    with open(cfg.out_dir / "train_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    _fol_cuda_bootstrap()
    print("[FOL train] trainer.evaluate() trên test (loss) …", flush=True)
    if fol_em_cb is not None:
        fol_em_cb.suppress_exact_match_metric = True
    try:
        test_trainer_metrics = trainer.evaluate(eval_dataset=dataset_dict["test"])
    finally:
        if fol_em_cb is not None:
            fol_em_cb.suppress_exact_match_metric = False

    _fol_cuda_bootstrap()
    print("[FOL train] Greedy exact-match JSON trên train/dev/test (lâu nếu full split + null max_samples) …", flush=True)
    fol_eval = run_fol_eval_all_splits(cfg, trainer, dataset_dict)
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    post_test_exact = fol_exact_match_rate(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        max_samples=None,
        split_label="test_post_ft_exact",
    )
    print("[FOL train] mean NLL completion trên test (full) …", flush=True)
    post_test_nll = mean_nll_completion_on_split(
        cfg, trainer.model, tok, dataset_dict["test"], max_samples=None
    )
    print("[Sau FT] test full exact_match:", post_test_exact)
    print("[Sau FT] test full mean NLL (completion):", post_test_nll)
    print("[Sau FT] trainer.evaluate(test):", test_trainer_metrics)

    fol_inference_latency: dict[str, Any] | None = None
    if cfg.inference_latency_benchmark_n > 0:
        split_lat = (cfg.inference_latency_benchmark_split or "test").strip().lower()
        if split_lat not in dataset_dict:
            for fb in ("test", "dev", "train"):
                if fb in dataset_dict:
                    print(
                        f"[FOL latency] Split '{cfg.inference_latency_benchmark_split}' không có trong dataset_dict, dùng '{fb}'.",
                        flush=True,
                    )
                    split_lat = fb
                    break
        if split_lat in dataset_dict:
            print(
                "[FOL train] Benchmark latency greedy (trung bình trên nhiều mẫu ngẫu nhiên) …",
                flush=True,
            )
            _fol_cuda_bootstrap()
            bseed = (
                cfg.inference_latency_benchmark_seed
                if cfg.inference_latency_benchmark_seed is not None
                else cfg.train_seed
            )
            fol_inference_latency = benchmark_fol_greedy_latency_per_sample(
                cfg,
                trainer.model,
                tok,
                dataset_dict[split_lat],
                n=cfg.inference_latency_benchmark_n,
                seed=int(bseed),
                warmup=cfg.inference_latency_warmup,
                split_name=split_lat,
            )
            with open(cfg.out_dir / "fol_inference_latency.json", "w", encoding="utf-8") as f:
                json.dump(fol_inference_latency, f, indent=2, ensure_ascii=False)
        else:
            print(
                "[FOL latency] Bỏ qua: không tìm thấy split train/dev/test trong dataset_dict.",
                flush=True,
            )

    preflight = load_preflight_baseline(cfg.out_dir)
    bench: dict[str, Any] = {
        "before_finetune_summary": {
            "test_exact_match_full": (preflight or {}).get("test_exact_match_full"),
            "test_mean_nll_completion_full": (preflight or {}).get(
                "test_mean_nll_completion_full"
            ),
        },
        "after_finetune": {
            "test_exact_match_full": post_test_exact,
            "test_mean_nll_completion_full": post_test_nll,
            "trainer_evaluate_test_metrics": test_trainer_metrics,
            "fol_eval_greedy_splits_respecting_FOL_EVAL_FOL_MAX_SAMPLES": fol_eval,
            "inference_latency_greedy": fol_inference_latency,
        },
    }
    with open(cfg.out_dir / "fol_test_benchmark.json", "w", encoding="utf-8") as f:
        json.dump(bench, f, indent=2, ensure_ascii=False)

    fol_samples = collect_fol_inference_samples(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        cfg.experiment_inference_sample_n,
        max_samples_cap=cfg.eval_fol_max_samples,
    )

    _persist_fol_experiment_log(
        cfg,
        trainer,
        train_result,
        train_metrics_final=metrics,
        fol_eval=fol_eval,
        filter_stats=filter_stats,
        fol_inference_samples=fol_samples,
        fol_preflight_baseline=preflight,
        fol_test_benchmark=bench,
        fol_inference_latency_benchmark=fol_inference_latency,
    )

    skip_hub = (os.environ.get("FOL_SKIP_HUB_PUSH") or "").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )
    trainer_return = trainer
    if cfg.push_to_hub and not skip_hub:
        hf_tok = (
            os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN") or ""
        ).strip()
        if not hf_tok:
            print(
                "[FOL train][Hub] push_to_hub=True nhưng thiếu HF_TOKEN / HUGGINGFACE_HUB_TOKEN "
                "(hoặc .env chưa nạp) — bỏ qua merge+push. Đặt FOL_SKIP_HUB_PUSH=1 để tắt rõ ràng.",
                flush=True,
            )
        else:
            print(
                "[FOL train][Hub] Merge LoRA + đẩy Hub (CPU, có thể vài phút; cần RAM đủ cho base ~FP16) …",
                flush=True,
            )
            from services.hub_push import (
                push_merged_fol_lora,
                upload_fol_experiment_artifacts_refresh,
                upload_fol_hub_readme_hub_reload_addon,
            )

            try:
                hub_url = push_merged_fol_lora(cfg, hf_tok)
                print("[FOL train][Hub] Xong:", hub_url, flush=True)
            except Exception as e:
                print(f"[FOL train][Hub] Push thất bại: {type(e).__name__}: {e}", flush=True)
            else:
                if cfg.hub_reload_after_push:
                    print(
                        "[FOL train][Hub reload] Giải phóng Trainer trên GPU/VRAM, tải merged từ Hub, "
                        "chỉ greedy trên mẫu test ngẫu nhiên (theo cấu hình) …",
                        flush=True,
                    )
                    from models.fol_model.hub_reload_eval import (
                        evaluate_fol_hub_model,
                        print_fol_hub_eval_summary,
                    )

                    trainer_return = None
                    try:
                        del trainer
                    except Exception:
                        pass
                    gc.collect()
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                    try:
                        hub_eval = evaluate_fol_hub_model(
                            cfg,
                            cfg.resolved_hf_repo(),
                            hf_token=hf_tok,
                            random_test_infer_n=cfg.hub_reload_random_test_n,
                            random_test_seed=cfg.hub_reload_random_seed,
                        )
                        hub_path = cfg.out_dir / "fol_hub_reload_eval.json"
                        with open(hub_path, "w", encoding="utf-8") as f:
                            json.dump(hub_eval, f, indent=2, ensure_ascii=False)
                        print(
                            f"[FOL train][Hub reload] Đã ghi metrics + toàn bộ mẫu inference → {hub_path}",
                            flush=True,
                        )
                        print_fol_hub_eval_summary(
                            hub_eval,
                            max_ordered_sample_print=cfg.experiment_inference_sample_n,
                            random_sample_print_limit=None,
                        )
                        up = upload_fol_experiment_artifacts_refresh(cfg, hf_tok)
                        if up:
                            print(
                                f"[FOL train][Hub reload] Đã upload/refresh {len(up)} file trong "
                                f"`experiment_artifacts/` (gồm fol_hub_reload_eval.json).",
                                flush=True,
                            )
                        upload_fol_hub_readme_hub_reload_addon(
                            cfg, hf_tok, hub_eval, random_preview_n=2
                        )
                        print(
                            "[FOL train][Hub reload] README trên Hub: thêm mục xác minh (~2 mẫu rút gọn); "
                            "log terminal + JSON local có đủ các mẫu ngẫu nhiên.",
                            flush=True,
                        )
                    except Exception as e:
                        print(
                            f"[FOL train][Hub reload] Thất bại: {type(e).__name__}: {e}",
                            flush=True,
                        )
    elif cfg.push_to_hub and skip_hub:
        print("[FOL train][Hub] Bỏ qua push (FOL_SKIP_HUB_PUSH).", flush=True)

    return train_result, trainer_return, tokenizer, dataset_dict


def run_train_and_eval(cfg: FolSFTConfig | None = None):
    cfg = cfg or FolSFTConfig.from_env()
    return run_training(cfg)


if __name__ == "__main__":
    out = run_train_and_eval()
    print("Done:", out is not None)
