"""v04 prompts: optimized classification prompt + domain-specific solving prompts.

The solving prompts (DOMAIN_PROMPTS, build_routed_template) are inherited from
v03 — only the classification prompt is changed in this version.

See ROUTING_PROMPT_DESIGN.md for the methodology behind the keyword selection.
"""

from __future__ import annotations

# Re-export solving prompts from v03 (unchanged).
from app.physics_solution.versions.v03_routed_fewshot.prompts import (  # noqa: F401
    DOMAIN_PROMPTS,
    FORMAT_HINTS,
    build_system_prompt,
    build_routed_template,
)


# ------------------------------------------------------------------ classification prompt (v04 optimized)

CLASSIFY_SYSTEM = """\
Classify a physics question into domain and answer_type. Output ONLY: {"domain":"XX","answer_type":"YY"}

DOMAINS:
- LD: Coulomb FORCES between point charges. The question asks to compute force magnitude/direction, net or resultant force on a charge, or equilibrium position. Keywords: "force", "net force", "resultant force", "force acting on", "exerted on", "Coulomb", "repulsive", "attractive", "interaction between charges", "test charge". May involve geometric arrangements of charges but the TARGET quantity is always a FORCE.
- DT: Electric FIELD or POTENTIAL at a point. The question asks for field strength E, potential V, or work done by the field at/between specific points. Keywords: "electric field strength", "field at point", "potential at", "potential difference", "field vector", "where the field is zero", "equipotential". Both LD and DT involve charges, but DT asks for field/potential, LD asks for force.
- CH: AC/RLC CIRCUIT calculations. The question involves circuit components (R, L, C) with an AC source and asks for current, voltage, impedance, frequency, resonance conditions, phase angle, or power in the circuit. Keywords: "RLC circuit", "series circuit", "impedance", "reactance", "resonance", "rms", "angular frequency", "phase", "power consumed", "power factor", "voltage across".
- NL: ENERGY, power, and LC oscillations. The question asks for energy stored in a capacitor or inductor, power dissipated, or properties of LC oscillation (charge/current as function of time). Keywords: "energy stored", "energy in the capacitor/inductor", "magnetic field energy", "electric field energy", "LC oscillation", "instantaneous current/charge", "maximum current", "ideal LC circuit", "oscillation period".
- TD: Standalone CAPACITOR calculations (no AC/RLC context). The question is about a capacitor's own properties: capacitance from geometry, charge stored, effect of dielectric, series/parallel combinations. Keywords: "parallel-plate capacitor", "plate area", "plate separation", "capacitance", "dielectric", "charge stored", "series/parallel capacitors", "equivalent capacitance", "disconnected from source".
- DDT: Electromagnetic INDUCTION and solenoids. The question involves Faraday's law, magnetic flux change, induced EMF, solenoid properties, or self/mutual inductance. Keywords: "solenoid", "turns", "magnetic flux", "induced EMF", "electromotive force", "Faraday", "Lenz", "self-inductance", "mutual inductance", "rate of change of current".
- THCB: MEASUREMENT errors and basic DC circuits. The question involves calculating measurement errors (absolute, relative, percentage), or simple DC circuits with batteries, internal resistance, ammeters, voltmeters. Keywords: "error", "absolute error", "relative error", "uncertainty", "measured value", "least count", "mean value", "internal resistance", "ammeter", "voltmeter", "battery".
- CHLT: YES/NO questions about circuit or physics properties. The question asks whether a specific condition holds (e.g. does resonance occur at a given frequency). The expected answer is Yes or No.

ANSWER TYPES:
- pure_numeric: plain decimal number (e.g. 5.07, 100, 0.25)
- sci_notation: scientific notation with powers of 10 (e.g. 5.07 x 10^-6)
- yes_no: Yes or No
- multi_value: multiple values separated by semicolons
- text_only: text answer (e.g. "Increases", "Doubled")
- mixed: number with embedded text

DISAMBIGUATION RULES:
- Question about charges but asks for FORCE -> LD. Asks for FIELD or POTENTIAL -> DT.
- Circuit with R,L,C asking for I, U, Z, f, phase, or power -> CH. Asking for ENERGY stored or LC oscillation quantities -> NL.
- Question only about a capacitor (geometry, dielectric, charge) with no AC/RLC context -> TD. If it asks for energy in a capacitor -> NL.
- Solenoid, flux, induced EMF, inductance -> DDT.
- Measurement error, mean value, precision, basic DC with battery -> THCB.
- Question ending with yes/no format ("does ... ?", "is ... ?") -> CHLT with answer_type=yes_no."""

# Synthetic few-shot classification examples (not from test set).
CLASSIFY_EXAMPLES: list[dict] = [
    {
        "q": "Two point charges q1 = 5 uC and q2 = -3 uC are 8 cm apart in vacuum. Calculate the magnitude of the electrostatic force between them.",
        "a": '{"domain":"LD","answer_type":"pure_numeric"}',
    },
    {
        "q": "A point charge q = 10 nC is placed at the origin. Determine the electric field strength at a point 5 cm away in vacuum.",
        "a": '{"domain":"DT","answer_type":"pure_numeric"}',
    },
    {
        "q": "A series RLC circuit has R = 50 ohm, L = 0.2 H, C = 20 uF, and is driven by a 220 V rms AC source at 50 Hz. Find the rms current in the circuit.",
        "a": '{"domain":"CH","answer_type":"pure_numeric"}',
    },
    {
        "q": "An ideal LC circuit has L = 4 mH and C = 10 uF. The maximum charge on the capacitor is 2 uC. Find the maximum energy stored in the inductor.",
        "a": '{"domain":"NL","answer_type":"pure_numeric"}',
    },
    {
        "q": "A parallel-plate capacitor has plates of area 100 cm2 separated by 2 mm of air. Calculate the capacitance in pF.",
        "a": '{"domain":"TD","answer_type":"pure_numeric"}',
    },
    {
        "q": "A solenoid with 500 turns and length 25 cm carries a current that changes from 2 A to 0 A in 0.05 s. The cross-sectional area is 10 cm2. Calculate the induced EMF.",
        "a": '{"domain":"DDT","answer_type":"pure_numeric"}',
    },
    {
        "q": "A student measures a resistor five times and gets 47.2, 47.5, 47.3, 47.4, 47.1 ohm. Calculate the mean value and the absolute error.",
        "a": '{"domain":"THCB","answer_type":"multi_value"}',
    },
    {
        "q": "An RLC series circuit has R = 100 ohm, L = 0.5 H, and C = 8 uF. Is the resonant frequency of this circuit equal to 80 Hz?",
        "a": '{"domain":"CHLT","answer_type":"yes_no"}',
    },
]
