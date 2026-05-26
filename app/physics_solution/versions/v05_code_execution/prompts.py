"""v05 prompts: classification + code-generation pipeline prompts.

Two prompt stages:
  1. Classification — domain + answer_type (merged groups)
  2. Code generation — LLM writes a Python script directly (no brief)
"""

from __future__ import annotations

from app.physics_solution.versions.v05_code_execution.formula_kb import get_formula_hints

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


# -- code generation prompt (code-first, no brief) ---------------------------

CODEGEN_SYSTEM = """\
Write a self-contained Python script to solve this physics problem. No explanation needed — go straight to code.

RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- Read ALL physical constants from scipy.constants. NEVER hardcode constant values.
    scipy.constants.epsilon_0    # vacuum permittivity
    scipy.constants.mu_0         # vacuum permeability
    scipy.constants.e            # elementary charge
    scipy.constants.pi           # pi
    Coulomb constant: k_e = 1 / (4 * scipy.constants.pi * scipy.constants.epsilon_0)
- Convert ALL given values to SI units at the top.
- Write the key formula as a comment before each computation step.
- For 2D/3D geometry: set up explicit x,y coordinates for each charge/point, compute distances with sqrt, decompose forces into x,y components separately, then compute magnitude with sqrt(Fx^2+Fy^2).
- The script MUST print exactly:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: compute, compare, print "Yes" or "No".
- For multi_value: print values separated by semicolons.
- Round to 2-4 significant figures.

```python
import scipy.constants as const

k_e = 1 / (4 * const.pi * const.epsilon_0)

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


# -- demo / verification ----------------------------------------------------

if __name__ == "__main__":
    sample_q = (
        "Two point charges q1 = 5 uC and q2 = -3 uC are placed 8 cm apart "
        "in vacuum. Calculate the magnitude of the electrostatic force between them."
    )

    print("=" * 70)
    print("  1. CODE GENERATION PROMPT")
    print("=" * 70)
    for msg in build_codegen_prompt(sample_q, "LDDT", "numeric"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  2. CHAIN-OF-THOUGHT PROMPT")
    print("=" * 70)
    for msg in build_cot_prompt(sample_q, "21.09", "N", "LDDT"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  3. should_use_code_execution()")
    print("=" * 70)
    for at in ["numeric", "yes_no", "multi_value", "text"]:
        print(f"  {at:15s} -> {should_use_code_execution(at)}")
