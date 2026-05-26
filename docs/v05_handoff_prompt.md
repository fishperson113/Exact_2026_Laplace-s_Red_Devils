# V05 Handoff Prompts — Modular

v05 is split into **4 independent modules** (A/B/C/D). Each can be done in a separate chat session. Copy the relevant block and paste as the first message.

**Dependency order**: A and B are independent (can run in parallel) → C depends on A's output format → D integrates A+B+C.

```
Module A: Formula KB          ← no deps, do first or in parallel with B
Module B: Code Executor       ← no deps, do first or in parallel with A
Module C: Prompts             ← needs to know A's output format
Module D: Pipeline Runner     ← integrates A+B+C, do last
```

---

# Module A: Formula Knowledge Base

---START-A---

## Context

I'm working on EXACT 2026 competition — a physics QA system. Model: Qwen 3.5 4B. Questions are in English about circuits, electrostatics, capacitors, induction. There are 8 physics domains (Vietnamese abbreviations):

- **LD** (397 questions, accuracy 24.7%): Coulomb forces between point charges
- **CH** (290, 61.7%): AC/RLC circuits, resonance, impedance
- **NL** (190, 72.1%): Energy in capacitors/inductors, LC oscillations
- **TD** (177, 73.5%): Standalone capacitor calculations (geometry, dielectric, charge)
- **DDT** (130, 68.5%): Electromagnetic induction, solenoids, Faraday's law
- **THCB** (80, 86.3%): Measurement errors, basic DC circuits
- **DT** (68, 32.4%): Electric field strength, electric potential
- **CHLT** (20, 80.0%): Yes/No questions about circuit properties

## Task: Create Formula Knowledge Base

Create two files under `app/physics_solution/versions/v05_code_execution/`:

### 1. `input/formulas.yaml`

A YAML file mapping each domain to its key formulas. Each formula needs: name, formula string, variables with descriptions and SI units, and the result unit. This will be injected into a code-generation prompt so the LLM knows which formula to use.

**Requirements:**
- 5-10 formulas per domain (cover the most common problem types)
- Variables must show SI unit conversion hints (e.g., `uC -> 1e-6 C`, `cm -> 0.01 m`)
- Include physical constants where needed (k = 9e9, epsilon_0 = 8.854e-12, mu_0 = 4*pi*1e-7, etc.)
- Formulas should be written as Python-executable expressions (use `**` for power, `math.sqrt` for sqrt, `math.pi` for pi)

**Existing domain prompts to expand from** — these are already in `app/physics_solution/versions/v03_routed_fewshot/prompts.py` in the `DOMAIN_PROMPTS` dict. Read that file to see the current formula hints per domain, then expand them for code generation.

**Example structure:**
```yaml
LD:
  constants:
    k: {value: 9e9, unit: "N*m^2/C^2", desc: "Coulomb constant"}
  unit_conversions:
    - "uC = 1e-6 C (microcoulomb)"
    - "nC = 1e-9 C (nanocoulomb)"
    - "cm = 0.01 m"
    - "mm = 0.001 m"
  formulas:
    - name: "Coulomb's Law"
      formula: "F = k * abs(q1) * abs(q2) / r**2"
      result_unit: "N"
      notes: "Force magnitude between two point charges"
    - name: "Superposition of forces"
      formula: "F_net = vector_sum of individual F_i"
      notes: "Add forces as vectors; use components if not collinear"
    # ... more formulas
```

### 2. `formula_kb.py`

A Python module that loads `formulas.yaml` and returns formatted formula hints for a given domain.

**Interface:**
```python
def get_formula_hints(domain: str) -> str:
    """Return a formatted string of formula hints for the given domain.
    
    This string will be injected into the code-generation prompt.
    If domain is unknown, return hints for the most common domain (LD).
    """
```

**Output format** (what the function returns as a string):
```
Constants:
- k = 9e9 N*m^2/C^2 (Coulomb constant)

Unit conversions:
- uC = 1e-6 C, nC = 1e-9 C, cm = 0.01 m, mm = 0.001 m

Formulas:
1. Coulomb's Law: F = k * abs(q1) * abs(q2) / r**2 → result in N
2. Superposition: F_net = vector sum of individual forces
3. ...
```

**Testing**: Add a `if __name__ == "__main__":` block that prints hints for each domain so I can verify.

**Codebase pattern**: Look at how other modules in the `versions/` directory are structured. The file should be importable as:
```python
from app.physics_solution.versions.v05_code_execution.formula_kb import get_formula_hints
```

Also create:
- `app/physics_solution/versions/v05_code_execution/__init__.py` (can be empty for now, Module D will fill it)
- `app/physics_solution/versions/v05_code_execution/input/` directory

After creating the files, push the changes.

---END-A---

---

# Module B: Code Executor

---START-B---

## Context

I'm working on EXACT 2026 competition — a physics QA system. In our new pipeline (v05), an LLM generates Python code that computes the answer to a physics problem. I need a module that **safely executes that code** and **parses the output**.

The generated code follows this pattern:
```python
import math

# Given values (SI units)
q1 = 2e-6    # 2 uC -> C
q2 = -3e-6   # -3 uC -> C
r = 0.10     # 10 cm -> m
k = 9e9      # Coulomb constant

# F = k * |q1| * |q2| / r^2
F = k * abs(q1) * abs(q2) / r**2

print(f"FINAL ANSWER: {F}")
print(f"UNIT: N")
```

The code only uses `import math` (no numpy, scipy, sympy, or external libraries). Output is always two print lines: `FINAL ANSWER: <value>` and `UNIT: <unit>`.

## Task: Create `code_executor.py`

Create `app/physics_solution/versions/v05_code_execution/code_executor.py` with these functions:

### 1. `extract_code(llm_output: str) -> str | None`
Extract Python code from the LLM's response. The LLM wraps code in markdown code blocks:
````
```python
import math
...
```
````
Should handle: with/without `python` language tag, multiple code blocks (take the last complete one), no code block at all (return None).

### 2. `execute_code(code: str, timeout: int = 10) -> ExecutionResult`

```python
@dataclass
class ExecutionResult:
    success: bool
    stdout: str        # raw stdout
    stderr: str        # raw stderr (for error feedback)
    answer: str | None # parsed FINAL ANSWER value
    unit: str | None   # parsed UNIT value
    error_type: str | None  # "syntax", "runtime", "timeout", "parse", None
```

**Requirements:**
- Execute via `subprocess.run()` in a temp file with the given timeout
- Parse stdout for `FINAL ANSWER:` and `UNIT:` lines
- If code only imports `math` (or nothing) — that's valid. If it tries to import anything else, prepend a comment warning but still try to run it.
- Handle edge cases: code prints extra lines, answer in scientific notation (e.g., `5.4e+06`), empty output, infinite loops (timeout)
- On Windows, use `sys.executable` for the Python path instead of hardcoding `"python"`
- Clean up temp files after execution

### 3. `format_answer(answer: str, unit: str) -> str`
Format the executed result into the competition output format:
```
FINAL ANSWER: {answer}
UNIT: {unit}
```
Handle scientific notation: if the answer is like `5400000.0`, keep as-is. If it's like `5.4e-06`, convert to `5.4 * 10^{-6}` format (the competition format). Use a regex or float parsing to detect and convert e-notation.

### Testing

Add a comprehensive `if __name__ == "__main__":` block that tests:

1. **Happy path**: valid code that prints FINAL ANSWER + UNIT
2. **Syntax error**: code with a typo
3. **Runtime error**: division by zero
4. **Timeout**: infinite loop (`while True: pass`)
5. **No FINAL ANSWER line**: code runs but doesn't print the expected format
6. **Extra output**: code prints debug lines before FINAL ANSWER
7. **Scientific notation**: answer is `5.4e-06`
8. **Code extraction**: test `extract_code()` with various markdown formats
9. **No code block**: LLM just outputs text without code fences

Run the tests and make sure they all pass. The module should work standalone:
```
python -m app.physics_solution.versions.v05_code_execution.code_executor
```

**Codebase note**: This module has NO dependencies on the rest of the codebase — it's pure Python stdlib (subprocess, tempfile, re, dataclasses, sys).

Also create `app/physics_solution/versions/v05_code_execution/__init__.py` if it doesn't exist yet (can be empty).

After creating the file and verifying tests pass, push the changes.

---END-B---

---

# Module C: Prompts

---START-C---

## Context

I'm working on EXACT 2026 competition — a physics QA system using Qwen 3.5 4B. The v05 pipeline has 3 stages: Router → Code Generator → Execute. I need prompt templates for each stage.

**Prerequisite**: Module A (Formula KB) should already be committed. Check that `app/physics_solution/versions/v05_code_execution/formula_kb.py` exists and read it to understand the `get_formula_hints(domain)` output format.

### Current prompt architecture (v03/v04)

Read these files to understand existing patterns:
- `app/physics_solution/versions/v03_routed_fewshot/prompts.py` — domain prompts, format hints, `build_routed_template()`
- `app/physics_solution/versions/v04_optimized_routing/prompts.py` — classification prompt (`CLASSIFY_SYSTEM`, `CLASSIFY_EXAMPLES`)
- `app/physics_solution/shared/prompts/system.py` — base system prompt, `ASSISTANT_PREFIX`

The project uses LangChain for prompt templates: `ChatPromptTemplate`, `SystemMessagePromptTemplate`, `HumanMessagePromptTemplate`, `MessagesPlaceholder`.

### Answer Types (6 total)
- `pure_numeric`: plain number like `5.07`, `100`
- `sci_notation`: scientific notation like `5.07 * 10^{-6}`
- `text_only`: text answers like "Increases"
- `multi_value`: semicolon-separated values
- `mixed`: number with text
- `yes_no`: Yes/No

## Task: Create `prompts.py`

Create `app/physics_solution/versions/v05_code_execution/prompts.py` with:

### 1. Import and re-export router prompts from v04
```python
from app.physics_solution.versions.v04_optimized_routing.prompts import (
    CLASSIFY_SYSTEM,
    CLASSIFY_EXAMPLES,
    DOMAIN_PROMPTS,
    FORMAT_HINTS,
    build_system_prompt,
    build_routed_template,
)
```

### 2. `CODEGEN_SYSTEM` — System prompt for code generation

The code generation prompt should instruct the model to:
- Write a self-contained Python script using only `import math`
- Define given values with SI unit conversions at the top
- Show formulas as comments
- Print exactly: `FINAL ANSWER: <value>` and `UNIT: <unit>`
- Handle different answer types:
  - For `pure_numeric` and `sci_notation`: compute and print the number
  - For `yes_no`: compute the relevant quantity, compare, print "Yes" or "No"
  - For `multi_value`: print values separated by semicolons
  - For `text_only` and `mixed`: these are hard to code-generate, so mark as SKIP (the pipeline will fallback to direct solve for these)

### 3. `build_codegen_prompt(question, domain, answer_type, formula_hints) -> str`

Build the full code-generation prompt by combining CODEGEN_SYSTEM + domain context + formula hints + the question. Return it as a chat message list (compatible with the tokenizer).

**Template structure:**
```
System: {CODEGEN_SYSTEM}
User: 
DOMAIN: {domain}
ANSWER TYPE: {answer_type}

RELEVANT FORMULAS:
{formula_hints}

PROBLEM:
{question}

Write a Python script to solve this.
```

### 4. `DIRECT_SOLVE_SYSTEM` — Fallback system prompt

For when code execution fails, reuse the v03/v04 direct solving approach. This is basically `build_system_prompt(domain, answer_type)` from v03.

### 5. `COT_SYSTEM` — Chain-of-thought generation prompt (for P2/P3 scoring)

After code execution produces a numerical answer, we call the LLM again to generate a reasoning explanation. The prompt should:
- Tell the model the correct answer is already known
- Ask for a step-by-step explanation using LaTeX inline math
- Follow the existing format: `Step 1: ... Step 2: ... FINAL ANSWER: X  UNIT: Y`

```
System: You are a physics tutor. The answer to the following problem has already been computed. 
Write a clear step-by-step explanation showing how to arrive at the given answer.
Use LaTeX inline math ($...$). End with FINAL ANSWER and UNIT lines.

User:
PROBLEM: {question}
COMPUTED ANSWER: {answer}
UNIT: {unit}
DOMAIN: {domain}

Explain step by step how to get this answer.
```

### 6. `should_use_code_execution(answer_type: str) -> bool`

Returns True if code execution is appropriate for this answer type. Returns False for `text_only` and `mixed` (these need direct LLM solving, not code).

### Testing

Add `if __name__ == "__main__":` that prints example prompts for a sample question in each mode (codegen, direct solve, CoT). This helps verify the prompts look correct.

After creating the file, push the changes.

---END-C---

---

# Module D: Pipeline Runner (Integration)

---START-D---

## Context

I'm working on EXACT 2026 competition — a physics QA system using Qwen 3.5 4B (<=8B params, hosted via vLLM, 60s timeout per question, tool calling allowed).

v05 is a **3-stage pipeline**: Router → Code Generator → Execute+Format, with fallback to direct LLM solve if code execution fails.

**Prerequisites**: Modules A, B, C should already be committed. Verify these files exist:
- `app/physics_solution/versions/v05_code_execution/formula_kb.py` — `get_formula_hints(domain)`
- `app/physics_solution/versions/v05_code_execution/code_executor.py` — `extract_code()`, `execute_code()`, `format_answer()`
- `app/physics_solution/versions/v05_code_execution/prompts.py` — `CLASSIFY_SYSTEM`, `CLASSIFY_EXAMPLES`, `build_codegen_prompt()`, `should_use_code_execution()`, `COT_SYSTEM`, `build_routed_template()`

Read ALL of these files first to understand their interfaces.

### Key codebase files to read
- `app/physics_solution/versions/v04_optimized_routing/run.py` — the v04 runner to use as a structural template
- `app/physics_solution/shared/router.py` — `classify_batch()` function
- `app/physics_solution/shared/model/loader.py` — `LoadedModel`, `load_model()`, `generate_batch()`
- `app/physics_solution/shared/model/batched_llm.py` — `HFBatchedLLM`, `RenderPrompt`, `_apply_chat_template_no_think()`
- `app/physics_solution/shared/eval/scorer.py` — `score()`, `extract()`, `RowResult`, `summarise()`
- `app/physics_solution/shared/prompts/helpers.py` — `fewshot_messages_from()`
- `app/physics_solution/cli/inference.py` — version registry
- `app/physics_solution/config.py` — default config values

### Accuracy context
| Version | Strategy | Accuracy (golden) |
|---------|----------|-------------------|
| v01 | zero-shot | 0.3817 |
| v02 | 3-shot | 0.5229 |
| v03 | routed 3-shot | 0.5473 |

### Error analysis (why code execution helps)
~70-80% of numeric errors are pure ARITHMETIC (correct formula, wrong exponent tracking). Code execution eliminates these. Error breakdown (v03, 612 wrong): magnitude_wrong 30.9%, off_by_power10 19.3%, numeric_far 11.4%, sci_scale_wrong 9.8%, formula_off 9.8%.

## Task: Create the pipeline runner

### 1. `__init__.py`
```python
VERSION_NUM = 5
STRATEGY_TAG = "code_execution"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "3-stage pipeline: (1) Router classifies domain+answer_type, "
    "(2) Code Generator produces Python code to compute the answer, "
    "(3) Execute code and format output. Falls back to direct LLM "
    "solve for text-based answers or when code execution fails."
)
```

### 2. `run.py` — Main pipeline

Must have `def run(args) -> dict:` matching the signature from v04's runner.

**Pipeline per question:**
```
1. Route: classify_batch() → (domain, answer_type)
2. For each question:
   a. Get formula hints from KB
   b. If should_use_code_execution(answer_type):
      - Build codegen prompt
      - Call LLM → get completion
      - Extract code from completion
      - Execute code → get result
      - If execution fails: retry once with error in prompt
      - If still fails: fallback to direct solve
      - If success: optionally generate CoT explanation
   c. Else (text_only, mixed):
      - Direct solve using v03-style routed few-shot
   d. Score the result
3. Summarise and write output
```

**Important implementation details:**
- Routing can be batched (all questions at once, like v04)
- Code generation CANNOT be batched if we need to handle retries per question — process questions one at a time, or batch code-gen and only retry failures
- Use `_apply_chat_template_no_think()` for prompt rendering (Qwen 3.5's thinking mode must be OFF)
- max_new_tokens for code gen should be at least 640 (same default), code is usually shorter than CoT
- Track which questions used code execution vs direct solve vs fallback in the results `extra` dict
- Test file: use golden data (`app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv`) — v05+ only evaluates on golden data

**Results format** — match v04's output structure exactly:
- JSON with `{"summary": {...}, "rows": [{...}, ...]}`
- Each row is a `evaluator.RowResult` with extra metadata
- Also write CSV
- Print accuracy summary at the end

**Extra metadata to track per row:**
```python
extra = {
    "rendered_prompt": prompt,
    "solve_method": "code_execution" | "direct_solve" | "fallback",
    "generated_code": code_string,  # if code execution was used
    "execution_stdout": stdout,
    "execution_stderr": stderr,
    "retry_count": 0 | 1,
    "routed_domain": route.domain,
    "routed_answer_type": route.answer_type,
    "route_confidence": route.confidence,
}
```

### 3. Register in CLI

Add v05 to `app/physics_solution/cli/inference.py`:
```python
VERSIONS = {
    ...existing entries...,
    "v05_code_execution": "app.physics_solution.versions.v05_code_execution.run",
}
```

### 4. Create output directory
```
app/physics_solution/versions/v05_code_execution/output/.gitkeep
```

### Fallback strategy in detail
```
answer_type in {text_only, mixed}? → direct solve (v03 routed few-shot)
                                     (code can't produce text answers)

Code gen succeeds?
  No → direct solve (v03 routed few-shot)
  Yes ↓

extract_code() finds code?
  No → direct solve
  Yes ↓

execute_code() succeeds?
  No → retry: re-prompt LLM with error message appended
       Still fails? → direct solve
  Yes ↓

Answer parsed?
  No → direct solve
  Yes → format answer, generate CoT explanation, return
```

### Testing

No GPU available locally (Windows 11). The pipeline will be tested on Colab. But verify:
- All imports resolve (no import errors)
- The CLI registration works (`python -m app.physics_solution.cli.inference --help` shows v05)
- The module structure is correct

After creating all files, push the changes.

---END-D---
