"""v05 prompts: classification + code-generation pipeline prompts.

Two prompt stages:
  1. Classification (re-exported from v04)
  2. Code generation — LLM writes a Python script to solve the problem
"""

from __future__ import annotations

# Re-export router + direct-solve prompts from v04 (which re-exports v03).
from app.physics_solution.versions.v04_optimized_routing.prompts import (  # noqa: F401
    CLASSIFY_SYSTEM,
    CLASSIFY_EXAMPLES,
    DOMAIN_PROMPTS,
    FORMAT_HINTS,
    build_system_prompt,
    build_routed_template,
)

from app.physics_solution.versions.v05_code_execution.formula_kb import get_formula_hints

# -- answer types suitable for code execution --------------------------------

_CODE_FRIENDLY_TYPES = {"pure_numeric", "sci_notation", "yes_no", "multi_value"}


def should_use_code_execution(answer_type: str) -> bool:
    """Return True if code execution is appropriate for this answer type."""
    return answer_type in _CODE_FRIENDLY_TYPES


# -- code generation prompt --------------------------------------------------

CODEGEN_SYSTEM = """\
You are a physics solver. First, briefly state the key physics principle and formula. Then write a self-contained Python script to compute the answer.

RULES:
- Allowed imports: math, sympy (for symbolic/equation solving), scipy.constants (for physical constants), numpy (for matrix/vector computation).
- Read ALL physical constants from scipy.constants. NEVER hardcode constant values. Key constants:
    scipy.constants.e            # elementary charge (1.602e-19 C)
    scipy.constants.epsilon_0    # vacuum permittivity (8.854e-12 F/m)
    scipy.constants.mu_0         # vacuum permeability (1.257e-6 T*m/A)
    scipy.constants.c            # speed of light (3e8 m/s)
    scipy.constants.g            # standard gravity (9.807 m/s^2)
    scipy.constants.pi           # pi
    scipy.constants.k            # Boltzmann constant (1.381e-23 J/K) — NOT Coulomb!
    Coulomb constant: k_e = 1 / (4 * scipy.constants.pi * scipy.constants.epsilon_0)
- Define all given values at the top with SI unit conversions.
- Write the key formula as a comment before each computation.
- The script MUST print exactly two lines at the end:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute the relevant quantity, compare, and print "Yes" or "No".
- For multi_value: print values separated by semicolons (e.g. "0.6; 1.2").
- Round numeric answers to 2-4 significant figures unless the problem specifies otherwise.

Example:
Coulomb force: F = k_e|q1||q2|/r². Convert units to SI, plug in, compute.

```python
import scipy.constants as const

k_e = 1 / (4 * const.pi * const.epsilon_0)  # Coulomb constant

# Given
q1 = 5e-6  # 5 uC -> C
q2 = 3e-6  # 3 uC -> C
r = 0.08   # 8 cm -> m

# Coulomb's law: F = k_e * |q1| * |q2| / r^2
F = k_e * abs(q1) * abs(q2) / r**2

print(f"FINAL ANSWER: {F:.4g}")
print("UNIT: N")
```"""


def build_codegen_prompt(
    question: str,
    domain: str,
    answer_type: str,
    formula_hints: str | None = None,
) -> list[dict]:
    """Build the full code-generation prompt as a chat message list.

    If *formula_hints* is None, it is fetched automatically from the formula KB.
    """
    if formula_hints is None:
        formula_hints = get_formula_hints(domain)

    user_content = (
        f"DOMAIN: {domain}\n"
        f"ANSWER TYPE: {answer_type}\n"
        f"\n"
        f"REFERENCE (unit conversions & formulas):\n"
        f"{formula_hints}\n"
        f"\n"
        f"PROBLEM:\n"
        f"{question}\n"
        f"\n"
        f"Write a Python script to solve this."
    )

    return [
        {"role": "system", "content": CODEGEN_SYSTEM},
        {"role": "user", "content": user_content},
    ]


# -- direct-solve fallback (delegates to v03/v04) ----------------------------

DIRECT_SOLVE_SYSTEM = build_system_prompt  # alias — call as DIRECT_SOLVE_SYSTEM(domain, answer_type)


# -- chain-of-thought explanation prompt -------------------------------------

COT_SYSTEM = """\
You are a physics tutor. The answer to the following problem has already been computed.
Write a clear step-by-step explanation showing how to arrive at the given answer.
Use LaTeX inline math ($...$). End with FINAL ANSWER and UNIT lines.

Format:
Step 1: <one short sentence>
Step 2: <one short sentence>
...
FINAL ANSWER: <answer>
UNIT: <unit>

For large/small numbers (|exponent| >= 4), write a * 10^{n}. NEVER use e-notation.
Keep it tight: 3-5 steps."""


def build_cot_prompt(
    question: str,
    answer: str,
    unit: str,
    domain: str,
) -> list[dict]:
    """Build a chain-of-thought explanation prompt as a chat message list."""
    user_content = (
        f"PROBLEM: {question}\n"
        f"COMPUTED ANSWER: {answer}\n"
        f"UNIT: {unit}\n"
        f"DOMAIN: {domain}\n"
        f"\n"
        f"Explain step by step how to get this answer."
    )

    return [
        {"role": "system", "content": COT_SYSTEM},
        {"role": "user", "content": user_content},
    ]


# -- demo / verification ----------------------------------------------------

if __name__ == "__main__":
    sample_q = (
        "Two point charges q1 = 5 uC and q2 = -3 uC are placed 8 cm apart "
        "in vacuum. Calculate the magnitude of the electrostatic force between them."
    )

    print("=" * 70)
    print("  1. CODE GENERATION PROMPT")
    print("=" * 70)
    for msg in build_codegen_prompt(sample_q, "LD", "pure_numeric"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  2. DIRECT SOLVE PROMPT (fallback)")
    print("=" * 70)
    print(f"\n[SYSTEM]")
    print(build_system_prompt("LD", "pure_numeric"))

    print("\n" + "=" * 70)
    print("  3. CHAIN-OF-THOUGHT PROMPT")
    print("=" * 70)
    for msg in build_cot_prompt(sample_q, "21.09", "N", "LD"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  4. should_use_code_execution()")
    print("=" * 70)
    for at in ["pure_numeric", "sci_notation", "yes_no", "multi_value", "text_only", "mixed"]:
        print(f"  {at:15s} -> {should_use_code_execution(at)}")
