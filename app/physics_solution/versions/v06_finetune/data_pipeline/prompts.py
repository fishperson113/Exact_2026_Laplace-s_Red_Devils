"""v06 self-gen generation prompt — short REASONING then ONE Python code block.

This replaces the v05_best code-only prompt (which made the model jump straight to
```python with no reasoning — 208/211 of the first self-gen samples had zero reasoning).
v06 trains Qwen to think briefly first, the way the user wants it at inference:

    Reasoning: <5-10 short lines — givens, key formula, plan>
    ```python
    ...compute... print FINAL ANSWER / UNIT
    ```

Two builders share the same system prompt so EVERY route emits the SAME shape:
  - build_gen_messages   — plain self-gen (Route 1), gold-free.
  - build_hinted_messages — self-gen guided by a reference solution (the QC hint_code),
    used only for problems Qwen can't solve on its own / too few correct samples. The
    model must write ITS OWN reasoning + code (on-policy); the execution gate verifies it.

Keep it tight: the 4B burns its budget on LaTeX walls, so the reasoning is capped at a few
short lines (the hard-won "short prompts win for 4B" lesson — see V06_HANDOFF_PROMPT.md).
"""

from __future__ import annotations

GEN_SYSTEM = """\
You are a physics problem solver. Answer in TWO parts, in this exact order:

1. Reasoning: 5-10 SHORT lines — list the given quantities (with units), the key
   formula(s), and the solution plan. Be terse; no LaTeX walls, no restating the problem.
2. Then exactly ONE self-contained Python code block that COMPUTES the answer.

CODE RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- HARDCODE standard physical constants (more reliable than importing them):
  k = 9e9, epsilon_0 = 8.854e-12, mu_0 = 4*math.pi*1e-7, e = 1.602e-19, g = 9.8.
- Define every GIVEN value at the top with SI unit conversions.
- NO HARDCODING of computed values: every non-given number must be COMPUTED by the code
  (sympy symbolic is fine when the problem gives no numbers). Never print a pre-computed
  answer — the script must derive it.
- The script MUST print exactly two lines at the end:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute the quantity and compare WITH ~1% tolerance (textbooks round, e.g.
  79.57 -> 80), then print "Yes" or "No".
- For multi_value: print values separated by semicolons.
- NEVER use e-notation in output. Write 2.97 * 10^6, not 2.97e6.
- Round numeric answers to 2-4 significant figures unless the problem specifies otherwise."""


def _user_block(question: str, domain: str, answer_type: str, formula_hints: str | None) -> str:
    if formula_hints is None:
        from app.physics_solution.versions.v05_best.formula_kb import get_formula_hints
        formula_hints = get_formula_hints(domain)
    return (
        f"DOMAIN: {domain}\n"
        f"ANSWER TYPE: {answer_type}\n\n"
        f"REFERENCE:\n{formula_hints}\n\n"
        f"PROBLEM:\n{question}\n"
    )


def build_gen_messages(question: str, domain: str, answer_type: str,
                       formula_hints: str | None = None) -> list[dict]:
    """Plain self-gen prompt (Route 1): reason briefly, then code. Gold is never shown."""
    user = _user_block(question, domain, answer_type, formula_hints) + \
        "\nReason briefly (5-10 lines), then write the Python script."
    return [
        {"role": "system", "content": GEN_SYSTEM},
        {"role": "user", "content": user},
    ]


def build_hinted_messages(question: str, domain: str, answer_type: str, hint_code: str,
                          formula_hints: str | None = None) -> list[dict]:
    """Hinted self-gen: a reference solution is shown for METHOD only; Qwen must write its
    OWN reasoning + code (kept on-policy; the execution gate still verifies it). Used only
    when plain self-gen fails / yields too few correct samples.

    The reference is a verified solve from the QC hint pool (DeepSeek/Claude) — declare it
    in the Data Disclosure Document. It is a teaching signal, NOT a copy target.
    """
    user = (
        _user_block(question, domain, answer_type, formula_hints)
        + "\nA REFERENCE SOLUTION is shown below — use it ONLY to find the correct method, "
        "then solve the problem in your OWN words and code (do not copy it verbatim):\n"
        f"```python\n{hint_code.strip()}\n```\n\n"
        "Now reason briefly (5-10 lines), then write your own Python script."
    )
    return [
        {"role": "system", "content": GEN_SYSTEM},
        {"role": "user", "content": user},
    ]
