---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.6
example_number: 30.10
subtitle: An underdamped L-R-C series circuit
needs_review: true
---

# Example 30.10: An underdamped L-R-C series circuit

## Problem
What resistance is required, in terms of $L $ and $C $, to give an $L $-$R $-$C $ series circuit a frequency that is one-half the undamped frequency?

## Setup
**IDENTIFY and SET UP:** This problem concerns an underdamped $L $-$R $-$C $ series circuit. We want just enough resistance to reduce the oscillation frequency to one-half of the undamped value.

Equation (30.29) gives the angular frequency $\omega $ of an underdamped $L $-$R $-$C $ series circuit; Eq. (30.22) gives the angular frequency $\omega_0 $ of an undamped $L $-$C $ circuit. We use these two equations to solve for $R $.

## Solution
**EXECUTE:** From Eqs. (30.29) and (30.22), the requirement
$$ 
\omega=\frac{1}{2}\omega_0
 $$
yields
$$ 
\sqrt{\frac{1}{LC}-\frac{R^2}{4L^2}}=\frac{1}{2}\sqrt{\frac{1}{LC}}.
 $$

We square both sides and solve for $R $:
$$ 
\frac{1}{LC}-\frac{R^2}{4L^2}=\frac{1}{4LC},
 $$
$$ 
\frac{R^2}{4L^2}=\frac{3}{4LC},
 $$
$$ 
R^2=\frac{3L}{C},
 $$
so
$$ 
R=\sqrt{\frac{3L}{C}}.
 $$

For example, adding $R=35\,\Omega $ to the circuit of Example 30.8, with $L=10\,\text{mH} $ and $C=25\,\mu\text{F} $, would reduce the frequency from $320\,\text{Hz} $ to $160\,\text{Hz} $.

## Evaluation
**EVALUATE:** The circuit becomes critically damped with no oscillations when
$$ 
R=2\sqrt{\frac{L}{C}}.
 $$
Our result for $R $ is smaller than that, as it should be; we want the circuit to be underdamped.

## Key concepts used
- Underdamped $L $-$R $-$C $ series circuit frequency:
  $$ 
  \omega=\sqrt{\frac{1}{LC}-\frac{R^2}{4L^2}}.
   $$
- Undamped $L $-$C $ circuit frequency:
  $$ 
  \omega_0=\frac{1}{\sqrt{LC}}.
   $$
- Setting $\omega=\tfrac{1}{2}\omega_0 $ and solving for $R $ gives:
  $$ 
  R=\sqrt{\frac{3L}{C}}.
   $$
- Critical damping occurs at
  $$ 
  R=2\sqrt{\frac{L}{C}}.
   $$
