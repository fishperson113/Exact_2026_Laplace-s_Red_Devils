"""v05 prompts: classification + code-generation pipeline prompts.

Two prompt stages:
  1. Classification — domain + answer_type (merged groups)
  2. Code generation — ToRA-style interleaved reasoning + code with few-shot examples
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


# ================================================================== #
#  Code generation prompt — ToRA-style SETUP + code with few-shots   #
# ================================================================== #

_CODEGEN_SYSTEM_BASE = """\
Integrate step-by-step reasoning and Python code to solve this physics problem.

STEPS:
1. SETUP (1-3 lines): State the coordinate system, identify given quantities, and note directions/signs.
2. CODE: Write a self-contained Python script to compute the answer.

RULES:
- Allowed imports: math, sympy, scipy.constants, numpy.
- Read ALL physical constants from scipy.constants. NEVER hardcode constant values.
    Coulomb constant: k_e = 1 / (4 * scipy.constants.pi * scipy.constants.epsilon_0)
- Convert ALL given values to SI units at the top of the script.
- For 2D geometry: place charges/points at explicit (x,y) coordinates, compute vector components separately.
- The script MUST print exactly:
    FINAL ANSWER: <value>
    UNIT: <unit>
- For yes_no: print "Yes" or "No". For multi_value: print values separated by semicolons.
- Round to 2-4 significant figures unless the problem specifies otherwise."""

# -- Few-shot examples (self-authored, outputs verified by running Python) -----

_EXAMPLE_COLLINEAR = """\
Question: Two charges q1 = +3 uC and q2 = -5 uC are placed 10 cm apart. Find the net force on a charge q3 = +2 uC placed at the midpoint between them.

Solution:

SETUP: Place q1 at x=0, q2 at x=0.10 m. q3 is at x=0.05 m (midpoint). q1 repels q3 rightward (+x), q2 attracts q3 rightward (+x). Both forces are in the same direction.

```python
import scipy.constants as const

k_e = 1 / (4 * const.pi * const.epsilon_0)

# Given (SI units)
q1 = 3e-6   # +3 uC
q2 = -5e-6  # -5 uC
q3 = 2e-6   # +2 uC
d = 0.10    # 10 cm

# Distances from q3 (midpoint) to each charge
r1 = d / 2  # 0.05 m
r2 = d / 2  # 0.05 m

# Coulomb's law: F = k_e * |qi| * |q3| / r^2
F1 = k_e * abs(q1) * abs(q3) / r1**2  # repulsive -> +x
F2 = k_e * abs(q2) * abs(q3) / r2**2  # attractive -> +x (toward q2)

# Both forces push q3 in +x direction
F_net = F1 + F2

print(f"FINAL ANSWER: {F_net:.4g}")
print("UNIT: N")
```
```output
FINAL ANSWER: 57.52
UNIT: N
```
The net force on q3 is 57.52 N directed from q1 toward q2."""

_EXAMPLE_TRIANGLE_2D = """\
Question: Two charges q1 = +4e-8 C and q2 = +6e-8 C are placed at points A and B, 10 cm apart. A third charge q3 = -3e-8 C is placed at point C, where AC = 6 cm and BC = 8 cm. Calculate the magnitude of the net electrostatic force on q3.

Solution:

SETUP: Place A at (0,0), B at (0.10,0). Find C from distances: x_C = (AC^2 + AB^2 - BC^2)/(2*AB) = 0.036, y_C = sqrt(AC^2 - x_C^2) = 0.048. This is a 6-8-10 right triangle (right angle at C). Both q1 and q2 attract q3 (opposite signs).

```python
import scipy.constants as const
import math

k_e = 1 / (4 * const.pi * const.epsilon_0)

# Given (SI units)
q1 = 4e-8    # +4e-8 C at A
q2 = 6e-8    # +6e-8 C at B
q3 = -3e-8   # -3e-8 C at C
d_AB = 0.10  # 10 cm

# Coordinate setup: A at origin, B on x-axis
x_A, y_A = 0.0, 0.0
x_B, y_B = d_AB, 0.0

# Find C from distances AC=0.06, BC=0.08
d_AC = 0.06
d_BC = 0.08
x_C = (d_AC**2 + d_AB**2 - d_BC**2) / (2 * d_AB)
y_C = math.sqrt(d_AC**2 - x_C**2)

# Distances (verify)
r_AC = math.sqrt((x_C - x_A)**2 + (y_C - y_A)**2)
r_BC = math.sqrt((x_C - x_B)**2 + (y_C - y_B)**2)

# Force from q1 on q3: q1(+) and q3(-) attract -> direction C->A
F1 = k_e * abs(q1) * abs(q3) / r_AC**2
F1_x = F1 * (x_A - x_C) / r_AC
F1_y = F1 * (y_A - y_C) / r_AC

# Force from q2 on q3: q2(+) and q3(-) attract -> direction C->B
F2 = k_e * abs(q2) * abs(q3) / r_BC**2
F2_x = F2 * (x_B - x_C) / r_BC
F2_y = F2 * (y_B - y_C) / r_BC

# Net force
Fx = F1_x + F2_x
Fy = F1_y + F2_y
F_net = math.sqrt(Fx**2 + Fy**2)

print(f"FINAL ANSWER: {F_net:.4g}")
print("UNIT: N")
```
```output
FINAL ANSWER: 0.00392
UNIT: N
```
The net force on q3 is 3.92 x 10^-3 N."""

_EXAMPLE_RLC = """\
Question: A series RLC circuit has R = 40 Ohm, L = 0.3 H, C = 30 uF, connected to a 120 V rms AC source at 50 Hz. Calculate the rms current.

Solution:

SETUP: Series RLC at f=50Hz. Compute ZL, ZC, Z, then I = V/Z.

```python
import scipy.constants as const
import math

# Given (SI units)
R = 40        # Ohm
L = 0.3       # H
C = 30e-6     # 30 uF -> F
U_rms = 120   # V
f = 50        # Hz

omega = 2 * const.pi * f

# Reactances
ZL = omega * L
ZC = 1 / (omega * C)

# Impedance: Z = sqrt(R^2 + (ZL - ZC)^2)
Z = math.sqrt(R**2 + (ZL - ZC)**2)

# Ohm's law for AC: I = U / Z
I_rms = U_rms / Z

print(f"FINAL ANSWER: {I_rms:.4g}")
print("UNIT: A")
```
```output
FINAL ANSWER: 2.876
UNIT: A
```
The rms current is 2.876 A."""

# -- Compose system prompt per domain -----------------------------------------

_EXAMPLES_LDDT = (
    "\n\nHere are examples showing the expected format:\n\n---\n\n"
    + _EXAMPLE_COLLINEAR
    + "\n\n---\n\n"
    + _EXAMPLE_TRIANGLE_2D
    + "\n\n---"
)

_EXAMPLES_OTHER = (
    "\n\nHere are examples showing the expected format:\n\n---\n\n"
    + _EXAMPLE_RLC
    + "\n\n---"
)


def _get_codegen_system(domain: str) -> str:
    """Return the full system prompt with domain-appropriate few-shot examples."""
    if domain == "LDDT":
        return _CODEGEN_SYSTEM_BASE + _EXAMPLES_LDDT
    return _CODEGEN_SYSTEM_BASE + _EXAMPLES_OTHER


# -- Public: kept as module-level for backward compat (uses LDDT examples) -----

CODEGEN_SYSTEM = _get_codegen_system("LDDT")


def build_codegen_prompt(
    question: str,
    domain: str,
    answer_type: str,
    formula_hints: str | None = None,
) -> list[dict]:
    """Build the code-generation prompt as a chat message list."""
    if formula_hints is None:
        formula_hints = get_formula_hints(domain)

    system_prompt = _get_codegen_system(domain)

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
        {"role": "system", "content": system_prompt},
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
    print("  1. CODE GENERATION PROMPT (LDDT domain)")
    print("=" * 70)
    for msg in build_codegen_prompt(sample_q, "LDDT", "numeric"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  2. CODE GENERATION PROMPT (CH domain)")
    print("=" * 70)
    sample_q_ch = (
        "A series RLC circuit has R = 100 ohm, L = 0.5 H, C = 10 uF. "
        "Connected to 220V rms at 50Hz. Find the rms current."
    )
    for msg in build_codegen_prompt(sample_q_ch, "CH", "numeric"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  3. CHAIN-OF-THOUGHT PROMPT")
    print("=" * 70)
    for msg in build_cot_prompt(sample_q, "21.09", "N", "LDDT"):
        print(f"\n[{msg['role'].upper()}]")
        print(msg["content"])

    print("\n" + "=" * 70)
    print("  4. should_use_code_execution()")
    print("=" * 70)
    for at in ["numeric", "yes_no", "multi_value", "text"]:
        print(f"  {at:15s} -> {should_use_code_execution(at)}")
