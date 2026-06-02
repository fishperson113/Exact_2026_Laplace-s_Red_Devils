# Prompt Proposal: ToRA-style Interleaved Reasoning for Physics

## Overview

Three changes to recover the 13 regressions caused by removing CoT:
1. `repetition_penalty=1.15` in model generation (breaks loops)
2. New CODEGEN_SYSTEM prompt with "SETUP (1-3 lines)" structured rationale
3. Self-authored few-shot examples verified by running actual Python

---

## 1. Repetition Penalty

Add `repetition_penalty=1.15` to `generate_text()` and `generate_batch()` in `loader.py`.

Location: `app/physics_solution/shared/model/loader.py` — both `gen_kwargs` dicts.

```python
gen_kwargs = dict(
    max_new_tokens=max_new_tokens,
    do_sample=do_sample,
    pad_token_id=tokenizer.eos_token_id,
    repetition_penalty=1.15,
)
```

---

## 2. New CODEGEN_SYSTEM Prompt

### Design Principles
- Restore rationale as ToRA-style "reasoning before code" but STRUCTURED and SHORT
- "SETUP (1-3 lines)" constrains model output — prevents both repetition loops and loss of geometry reasoning
- Domain-aware few-shot injection: LDDT gets geometry examples, other domains get simpler ones
- Single unified system prompt for all domains (few-shots vary per domain)

### Proposed CODEGEN_SYSTEM

```
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
- Round to 2-4 significant figures unless the problem specifies otherwise.
```

Key change vs old prompt:
- Old "briefly state..." was too open-ended → model rambled → repetition loops
- Old "go straight to code" killed CoT → 13 regressions
- New "SETUP (1-3 lines)" is constrained: model writes 1-3 lines of text, then immediately enters code

---

## 3. Few-Shot Examples (all verified by running Python)

### Example 1: Collinear charges — force on a line (simple, no 2D geometry)
Domain: LDDT | Tests: basic Coulomb + superposition, direction reasoning

**Question:** Two charges q1 = +3 uC and q2 = -5 uC are placed 10 cm apart. Find the net force on a charge q3 = +2 uC placed at the midpoint between them.

**Solution:**

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
The net force on q3 is **57.52 N** directed from q1 toward q2.

---

### Example 2: Right triangle — forces in 2D (critical for LDDT geometry problems)
Domain: LDDT | Tests: coordinate setup, distance from triangle, vector decomposition

**Question:** Two charges q1 = +4e-8 C and q2 = +6e-8 C are placed at points A and B, 10 cm apart. A third charge q3 = -3e-8 C is placed at point C, where AC = 6 cm and BC = 8 cm. Calculate the magnitude of the net electrostatic force on q3.

**Solution:**

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
The net force on q3 is **3.92 x 10^-3 N**.

---

### Example 3: RLC circuit — no geometry needed (for CH/NL/TD/DDT/THCB domains)
Domain: CH | Tests: direct formula application, no coordinate setup

**Question:** A series RLC circuit has R = 40 Ohm, L = 0.3 H, C = 30 uF, connected to a 120 V rms AC source at 50 Hz. Calculate the rms current.

**Solution:**

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
The rms current is **2.876 A**.

---

## 4. How few-shots are injected into the prompt

The examples go into the SYSTEM prompt after the rules:

```
Here are examples showing the expected format:

---

Question: [question text]

Solution:
[SETUP + code + output + final line]

---
```

**Domain routing:**
- LDDT: Example 1 (collinear) + Example 2 (2D triangle) — these show both simple and geometry cases
- CH, NL, TD, DDT, THCB: Example 3 (RLC) — no geometry needed, shows the SETUP+code format

This keeps prompts manageable: ~400-600 tokens for examples.

---

## 5. Implementation Plan

### File: `app/physics_solution/shared/model/loader.py`
- Add `repetition_penalty=1.15` to `gen_kwargs` in both `generate_text()` and `generate_batch()`

### File: `app/physics_solution/versions/v05_code_execution/prompts.py`
- Replace `CODEGEN_SYSTEM` with the new prompt (SETUP+RULES section)
- Add `CODEGEN_EXAMPLES_LDDT` and `CODEGEN_EXAMPLES_OTHER` constants with the few-shot examples
- Update `build_codegen_prompt()` to inject domain-appropriate examples into the system prompt

### No changes to:
- `run.py` (pipeline logic unchanged)
- `formula_kb.py` (formula hints still injected the same way)
- Classification prompt (already working perfectly at 60/60)
