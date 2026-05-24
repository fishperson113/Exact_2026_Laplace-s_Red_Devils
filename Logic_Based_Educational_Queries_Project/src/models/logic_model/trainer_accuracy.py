from __future__ import annotations

from typing import Any

import torch
from trl import SFTTrainer

from services.config import LogicSFTConfig

from .generation_eval import accuracy_on_dataset


class AccuracySFTTrainer(SFTTrainer):
    """
    Giữ eval_loss từ Trainer, cộng thêm eval_accuracy (parse Answer: sau generate).
    Checkpoint tốt nhất theo eval_accuracy khi SFTConfig.metric_for_best_model='eval_accuracy'.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        self.logic_cfg: LogicSFTConfig = kwargs.pop("logic_cfg")
        self.logic_dataset_dict = kwargs.pop("logic_dataset_dict", None)
        super().__init__(*args, **kwargs)
        self.epoch_metric_rows: list[dict[str, Any]] = []

    def _last_logged_train_loss(self) -> tuple[float | None, float | None, int | None]:
        """Loss train gần nhất trong log_history (trước bước eval hiện tại)."""
        for h in reversed(self.state.log_history):
            if "loss" in h and h.get("loss") is not None and "eval_loss" not in h:
                return float(h["loss"]), h.get("epoch"), h.get("step")
        return None, None, None

    def _tok(self):
        return getattr(self, "processing_class", None) or self.tokenizer

    @torch.no_grad()
    def evaluate(
        self,
        eval_dataset=None,
        ignore_keys=None,
        metric_key_prefix: str = "eval",
    ):
        ds = eval_dataset if eval_dataset is not None else self.eval_dataset
        if ds is None:
            raise ValueError(
                "evaluate() requires eval_dataset or self.eval_dataset; "
                "cannot compute eval_loss / eval_accuracy without an eval split."
            )
        metrics = super().evaluate(eval_dataset, ignore_keys, metric_key_prefix)
        if "eval_prompt" not in ds.column_names:
            return metrics

        tokenizer = self._tok()
        model = self.model
        model.eval()
        lim = self.logic_cfg.eval_accuracy_max_samples

        acc = float(
            accuracy_on_dataset(
                self.logic_cfg,
                model,
                tokenizer,
                ds,
                max_samples=lim,
            )
        )
        metrics[f"{metric_key_prefix}_accuracy"] = acc
        self.log(metrics)

        tl, tl_epoch, tl_step = self._last_logged_train_loss()
        row: dict[str, Any] = {
            "global_step": int(self.state.global_step),
            "epoch": float(metrics.get("epoch", self.state.epoch or 0.0)),
            "train_loss_last_logged": tl,
            "train_loss_logged_at_epoch": tl_epoch,
            "train_loss_logged_at_step": tl_step,
            "dev_eval_loss": metrics.get("eval_loss"),
            "dev_accuracy": metrics.get(f"{metric_key_prefix}_accuracy"),
        }
        if (
            self.logic_dataset_dict is not None
            and self.logic_cfg.log_test_each_epoch
            and "test" in self.logic_dataset_dict
        ):
            row["test_accuracy"] = float(
                accuracy_on_dataset(
                    self.logic_cfg,
                    model,
                    tokenizer,
                    self.logic_dataset_dict["test"],
                    max_samples=self.logic_cfg.eval_accuracy_max_samples,
                )
            )
        else:
            row["test_accuracy"] = None
        self.epoch_metric_rows.append(row)

        return metrics
