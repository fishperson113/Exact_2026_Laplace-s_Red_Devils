# Version template

Copy this folder to create a new version:

```bash
cp -r versions/_template versions/v03_rag
```

Then customize:

1. **`__init__.py`** — set `VERSION_NUM`, `STRATEGY_TAG`, `DEFAULT_BASE_MODEL_ID`, `DESCRIPTION`.
2. **`prompts.py`** — build your `ChatPromptTemplate` in `build_template()`.
3. **`run.py`** — wire `build_template()` + an `InputBuilder` into `run_solver()`.
4. **Register** in `cli/inference.py`'s `VERSIONS` dict.
5. **Copy** a sibling's `run.ipynb` and update the `--version` arg.

## Folder layout

```
v0X_strategy/
├── __init__.py        # version metadata
├── prompts.py         # build_template() -> ChatPromptTemplate
├── run.py             # run(args) -> dict
├── run.ipynb          # Colab notebook
├── README.md          # what this version does + how to run
├── input/             # version-specific inputs (examples, KB, etc.)
│   └── .gitkeep
└── output/            # inference results land here
    └── .gitkeep
```
