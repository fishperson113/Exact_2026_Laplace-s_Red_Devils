"""v05_best prompts: classification + code-generation pipeline prompts.

Two prompt stages:
  1. Classification — domain + answer_type (merged groups)
  2. Code generation — simple direct prompt with inline example, k=9e9 hardcoded
"""

from __future__ import annotations

from app.physics_solution.versions.v05_best.formula_kb import get_formula_hints

# ================================================================== #
#  Classification prompt — merged domains & answer types             #
# ================================================================== #

CLASSIFY_SYSTEM = """\
Classify a physics question into domain and answer_type. Output ONLY: {"domain":"XX","answer_type":"YY"}

DOMAINS:
- LDDT: ELECTROSTATICS — Coulomb forces, electric field, electric potential, work done by field. The question involves point charges and asks for force, field strength E, potential V, potential difference, equilibrium position, or work. Keywords: "force", "net force", "Coulomb", "electric field", "potential", "field at point", "work done by field", "test charge", "superposition".
- CH: AC/RLC CIRCUIT calculations, including yes/no questions about circuit properties. The question involves circuit components (R, L, C) with an AC source and asks for current, voltage, impedance, frequency, resonance, phase, power, or whether a condition holds. Keywords: "RLC", "impedance", "resonance", "rms", "phase", "power factor", "voltage across", "is the resonant frequency equal to".
- NL: ENERGY, power, and LC oscillations. The question asks for energy stored in a capacitor or inductor, power dissipated, or LC oscillation quantities (charge/current vs time). Keywords: "energy stored", "LC oscillation", "maximum current", "oscillation period".
- TD: Standalone CAPACITOR calculations (no AC/RLC context). Capacitance from geometry, charge stored, dielectric, series/parallel combinations. Keywords: "parallel-plate capacitor", "capacitance", "dielectric", "equivalent capacitance".
- DDT: Electromagnetic INDUCTION and solenoids. Faraday's law, magnetic flux, induced EMF, self/mutual inductance. Keywords: "solenoid", "magnetic flux", "induced EMF", "Faraday", "self-inductance".
- THCB: MEASUREMENT errors and basic DC circuits. Measurement errors (absolute, relative), simple DC circuits with batteries. Keywords: "error", "absolute error", "internal resistance", "ammeter", "voltmeter".

ANSWER TYPES:
- numeric: a number (plain decimal like 5.07 or scientific notation like 5.07 x 10^-6)
- yes_no: Yes or No
- multi_value: multiple values separated by semicolons
- text: text answer (e.g. "Increases", "Doubled", or number with embedded text)

RULES:
- Charges asking for FORCE, FIELD, or POTENTIAL -> LDDT.
- Circuit with R,L,C asking for I, U, Z, f, phase, power, or yes/no about circuit -> CH.
- Energy stored or LC oscillation quantities -> NL.
- Capacitor geometry/charge with no AC context -> TD.
- Solenoid, flux, induced EMF -> DDT.
- Measurement error, basic DC battery -> THCB.
- Most physics answers are numeric. Only use yes_no/multi_value/text when clearly required."""

CLASSIFY_EXAMPLES: list[dict] = [
    {
        "q": "Two point charges q1 = 5 uC and q2 = -3 uC are 8 cm apart in vacuum. Calculate the magnitude of the electrostatic force between them.",
        "a": '{"domain":"LDDT","answer_type":"numeric"}',
    },
    {
        "q": "A point charge q = 10 nC is placed at the origin. Determine the electric field strength at a point 5 cm away in vacuum.",
        "a": '{"domain":"LDDT","answer_type":"numeric"}',
    },
    {
        "q": "A series RLC circuit has R = 50 ohm, L = 0.2 H, C = 20 uF, and is driven by a 220 V rms AC source at 50 Hz. Find the rms current in the circuit.",
        "a": '{"domain":"CH","answer_type":"numeric"}',
    },
    {
        "q": "An ideal LC circuit has L = 4 mH and C = 10 uF. The maximum charge on the capacitor is 2 uC. Find the maximum energy stored in the inductor.",
        "a": '{"domain":"NL","answer_type":"numeric"}',
    },
    {
        "q": "A parallel-plate capacitor has plates of area 100 cm2 separated by 2 mm of air. Calculate the capacitance in pF.",
        "a": '{"domain":"TD","answer_type":"numeric"}',
    },
    {
        "q": "A solenoid with 500 turns and length 25 cm carries a current that changes from 2 A to 0 A in 0.05 s. The cross-sectional area is 10 cm2. Calculate the induced EMF.",
        "a": '{"domain":"DDT","answer_type":"numeric"}',
    },
    {
        "q": "A student measures a resistor five times and gets 47.2, 47.5, 47.3, 47.4, 47.1 ohm. Calculate the mean value and the absolute error.",
        "a": '{"domain":"THCB","answer_type":"multi_value"}',
    },
    {
        "q": "An RLC series circuit has R = 100 ohm, L = 0.5 H, and C = 8 uF. Is the resonant frequency of this circuit equal to 80 Hz?",
        "a": '{"domain":"CH","answer_type":"yes_no"}',
    },
]

# -- answer types suitable for code execution --------------------------------

_CODE_FRIENDLY_TYPES = {"numeric", "yes_no", "multi_value"}


def should_use_code_execution(answer_type: str) -> bool:
    """Return True if code execution is appropriate for this answer type."""
    return answer_type in _CODE_FRIENDLY_TYPES


# ================================================================== #
#  Code generation prompt — simple, direct, with inline example      #
# ================================================================== #

CODEGEN_SYSTEM = """\
You are a physics solver. Write a self-contained Python script to solve the given problem.

RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- Define all given values at the top with SI unit conversions.
- Write the key formula as a comment before each computation.
- The script MUST print exactly two lines at the end:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute the relevant quantity, compare, and print "Yes" or "No".
- For multi_value: print values separated by semicolons (e.g. print("FINAL ANSWER: 0.6; 1.2")).
- NEVER use e-notation in output. Write 2.97 * 10^6, not 2.97e6.
- Round numeric answers to 2-4 significant figures unless the problem specifies otherwise.

Example:
```python
import math

# Given
q1 = 5e-6  # 5 uC -> C
q2 = 3e-6  # 3 uC -> C
r = 0.08   # 8 cm -> m
k = 9e9    # Coulomb constant

# Coulomb's law: F = k * |q1| * |q2| / r^2
F = k * abs(q1) * abs(q2) / r**2

print(f"FINAL ANSWER: {F:.4g}")
print("UNIT: N")
```"""


def build_codegen_prompt(
    question: str,
    domain: str,
    answer_type: str,
    formula_hints: str | None = None,
) -> list[dict]:
    """Build the code-generation prompt as a chat message list."""
    if formula_hints is None:
        formula_hints = get_formula_hints(domain)

    user_content = (
        f"DOMAIN: {domain}\n"
        f"ANSWER TYPE: {answer_type}\n"
        f"\n"
        f"REFERENCE:\n"
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


# -- chain-of-thought explanation prompt (post-hoc, for scoring) -------------

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
