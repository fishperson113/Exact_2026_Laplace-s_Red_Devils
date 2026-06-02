"""v06 data pipeline: filter -> normalize -> self-gen -> teacher -> guards -> split.

Stage order (see ../README.md for the full map):
  Phase 0  extract_golden60, taxonomy, schema   (scaffolding, this commit)
  Phase 1  filter, vietjack_normalize           (DeepSeek, local)
  Phase 2  selfgen (Qwen vLLM), teacher, guards  (Vast AI + DeepSeek)
  Phase 3  build_sft                             (stratified split -> JSONL)
"""
