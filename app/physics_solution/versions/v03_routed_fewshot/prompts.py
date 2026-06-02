"""v03 domain-specific system prompts, classification prompt, and routed template builder."""

from __future__ import annotations

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from app.physics_solution.shared.prompts.system import ZEROSHOT_USER_TEMPLATE


# ------------------------------------------------------------------ classification prompt (v03 original)
CLASSIFY_SYSTEM = """\
You are a physics question classifier. Given a physics question, output a JSON object with two keys:
- "domain": one of LD, CH, NL, TD, DDT, THCB, DT, CHLT
- "answer_type": one of pure_numeric, sci_notation, yes_no, multi_value, text_only, mixed

Domain descriptions:
- LD: Electrostatics / Coulomb forces, electric fields between point charges
- CH: Electric circuits / RLC circuits, resonance, impedance
- NL: Energy in capacitors/inductors, LC oscillations, power
- TD: Capacitor calculations: charge, capacitance, energy storage
- DDT: Solenoids, EMF, electromagnetic induction, inductance
- THCB: Basic combined circuits, measurement errors, simple DC
- DT: Electric field strength, electric potential, field lines
- CHLT: Yes/No questions about resonance conditions or circuit properties

Answer type descriptions:
- pure_numeric: a plain decimal number (e.g. 5.07, 100, 0.25)
- sci_notation: scientific notation (e.g. 5.07 x 10^-6)
- yes_no: Yes or No
- multi_value: multiple values separated by semicolons (e.g. 0.6; 1.2)
- text_only: text answer (e.g. "Doubled", "Increased")
- mixed: number with text or unit embedded in the answer

Output ONLY the JSON object, nothing else."""

CLASSIFY_EXAMPLES: list[dict] = []  # v03: zero-shot classification (no examples)


# ------------------------------------------------------------------ base suffix
# Shared output-format block appended to every domain prompt.
# The {format_hint} placeholder is filled per answer_type.
_BASE_SUFFIX = """
Write a short numbered reasoning chain using LaTeX inline math ($...$), then the final answer. Format:

Step 1: <one short sentence>
Step 2: <one short sentence>
...
{format_hint}

For large/small numbers (|exponent| >= 4), write a * 10^{{{{n}}}}. NEVER use e-notation.
WRONG: 2.97e6 | RIGHT: 2.97 * 10^{{{{6}}}}

Keep it tight: 3-5 steps. Commit to one reading of the problem. Stop after the UNIT line."""


# ------------------------------------------------------------------ format hints per answer type
FORMAT_HINTS: dict[str, str] = {
    "pure_numeric": "FINAL ANSWER: <answer>\nUNIT: <unit symbol, or - if dimensionless>",
    "sci_notation": "FINAL ANSWER: <a * 10^n, e.g. 5.07 * 10^{{-6}}>\nUNIT: <unit symbol, or - if dimensionless>",
    "yes_no": "FINAL ANSWER: <Yes or No>\nUNIT: -",
    "multi_value": "FINAL ANSWER: <values separated by semicolons, e.g. 0.6; 1.2>\nUNIT: <unit symbol, or - if dimensionless>",
    "text_only": "FINAL ANSWER: <short text answer>\nUNIT: -",
    "mixed": "FINAL ANSWER: <answer>\nUNIT: <unit symbol, or - if dimensionless>",
}


# ------------------------------------------------------------------ domain prompts
# Each is a short domain-context paragraph + key formula hints.
# Kept deliberately brief (~3-5 formula lines) to avoid echo.

DOMAIN_PROMPTS: dict[str, str] = {
    "LD": (
        "You are a physics tutor specialising in electrostatics and Coulomb forces. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Coulomb's law: F = k*q1*q2 / r^2, k = 9 x 10^9 N.m^2/C^2\n"
        "- Electric field of point charge: E = k*q / r^2\n"
        "- Superposition: vector sum of individual forces/fields\n"
        "- Equilibrium: net force = 0, solve for unknown charge or position\n"
        "- Common units: N, C, uC (10^-6 C), V/m"
    ),
    "CH": (
        "You are a physics tutor specialising in electric circuits, RLC circuits, and resonance. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Ohm's law: V = I*R, P = I^2*R = V^2/R\n"
        "- RLC series impedance: Z = sqrt(R^2 + (ZL - ZC)^2)\n"
        "- Resonance: omega_0 = 1/sqrt(LC), at resonance ZL = ZC, Z = R\n"
        "- Power factor: cos(phi) = R/Z\n"
        "- Common units: Ohm, A, V, mH, uF, Hz"
    ),
    "NL": (
        "You are a physics tutor specialising in energy in electric circuits, capacitors, "
        "inductors, and LC oscillations. You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Capacitor energy: W = q^2/(2C) = C*U^2/2\n"
        "- Inductor energy: W = L*I^2/2\n"
        "- LC oscillation: q = Q0*cos(omega*t + phi), omega = 1/sqrt(LC)\n"
        "- Energy conservation in LC: Q0^2/(2C) = L*I0^2/2\n"
        "- Common units: J, mJ, uJ, F, H, uF, mH"
    ),
    "TD": (
        "You are a physics tutor specialising in capacitor calculations. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Capacitance: C = epsilon_0 * S / d (parallel plate)\n"
        "- Charge: Q = C*U\n"
        "- Energy: W = C*U^2/2 = Q^2/(2C)\n"
        "- Series: 1/C_eq = 1/C1 + 1/C2 + ...\n"
        "- Parallel: C_eq = C1 + C2 + ...\n"
        "- Common units: F, nF, pF, uF, nC, uC, nJ"
    ),
    "DDT": (
        "You are a physics tutor specialising in electromagnetic induction, solenoids, and EMF. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Faraday's law: EMF = -d(Phi)/dt\n"
        "- Magnetic flux: Phi = B*S*cos(alpha)\n"
        "- Solenoid field: B = mu_0 * n * I\n"
        "- Self-inductance EMF: e = -L * dI/dt\n"
        "- Common units: T, Wb, V, mH, H, A"
    ),
    "THCB": (
        "You are a physics tutor specialising in basic combined circuits and measurement problems. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Kirchhoff's voltage law: sum of EMFs = sum of I*R around a loop\n"
        "- Kirchhoff's current law: sum of currents at a node = 0\n"
        "- Internal resistance: U = EMF - I*r\n"
        "- Measurement error: delta = |measured - true| / true * 100%\n"
        "- Common units: V, A, Ohm, W"
    ),
    "DT": (
        "You are a physics tutor specialising in electric field and electric potential calculations. "
        "You answer in English using SI units.\n\n"
        "Key formulas:\n"
        "- Electric field: E = k*q/r^2 = V/d (uniform)\n"
        "- Electric potential: V = k*q/r\n"
        "- Work by electric field: A = q*E*d = q*(V1-V2)\n"
        "- Potential energy: W = q*V\n"
        "- Common units: V/m, V, J, C, kV/m"
    ),
    "CHLT": (
        "You are a physics tutor answering Yes/No questions about circuit properties and resonance conditions. "
        "You answer in English.\n\n"
        "Key concepts:\n"
        "- Resonance occurs when ZL = ZC, i.e. omega = 1/sqrt(LC)\n"
        "- At resonance: Z = R (minimum), I = max, cos(phi) = 1\n"
        "- Power max at resonance; voltage across L or C can exceed source voltage\n"
        "- Answer Yes or No based on whether the stated condition is satisfied"
    ),
}


def build_system_prompt(domain: str, answer_type: str) -> str:
    """Compose a domain-specific system prompt with answer-type format hint."""
    base = DOMAIN_PROMPTS.get(domain, DOMAIN_PROMPTS["LD"])
    fmt = FORMAT_HINTS.get(answer_type, FORMAT_HINTS["pure_numeric"])
    return base + _BASE_SUFFIX.format(format_hint=fmt)


def build_routed_template(domain: str, answer_type: str) -> ChatPromptTemplate:
    """Build a ChatPromptTemplate with domain-specific system prompt."""
    system_text = build_system_prompt(domain, answer_type)
    return ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                system_text, template_format="f-string",
            ),
            MessagesPlaceholder("few_shot_messages", optional=True),
            HumanMessagePromptTemplate.from_template(ZEROSHOT_USER_TEMPLATE),
        ]
    )
