.PHONY: help data validate train train-fol inference install

# Thư mục gốc dự án (Makefile nằm tại đây)
ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
export PYTHONPATH := $(abspath $(ROOT)src)

help:
	@echo "Targets: install | data | validate | train | train-fol | inference"

install:
	python -m pip install -r requirements.txt

data:
	@echo "→ data/processed/ (train/dev/test.csv — chung logic + FOL; raw JSON mặc định hoặc notebook EDA)"
	cd "$(ROOT)" && PYTHONPATH=src python -c "from data.ingestion import export_default_logic_sft; export_default_logic_sft()"

validate:
	cd "$(ROOT)" && PYTHONPATH=src python -c "from data.validation import validate_raw_question_count, validate_processed_splits; validate_raw_question_count(); print(validate_processed_splits())"

train:
	cd "$(ROOT)" && PYTHONPATH=src python -m models.logic_model.train

train-fol:
	cd "$(ROOT)" && PYTHONPATH=src python -m models.fol_model.train

inference:
	@echo "Chạy notebook logic_model_pipeline_official.ipynb hoặc dùng models.logic_model.predict trong Python REPL (xem README)."
