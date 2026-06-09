"""v07 SFT training (Unsloth QLoRA) — E step.

Modules:
- sft_model.py : load Qwen3.5-4B via Unsloth + LoRA (+ tf5 gotchas)
- sft_data.py  : load output/{train,val}.jsonl chat messages -> HF Dataset(text)
- train.py     : orchestrate SFTTrainer -> save adapter+tokenizer -> merge -> push
- merge_push.py: merge LoRA + push adapter & merged + model card with metrics
"""
