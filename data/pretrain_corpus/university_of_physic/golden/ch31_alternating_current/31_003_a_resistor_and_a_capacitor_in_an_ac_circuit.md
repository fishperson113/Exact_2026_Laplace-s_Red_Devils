---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.2
example_number: 31.3
subtitle: A resistor and a capacitor in an ac circuit
needs_review: true
---

# Example 31.3: A resistor and a capacitor in an ac circuit

## Problem
A resistor is connected in series with a capacitor. The voltage across the resistor is

$$ 
v_R = (1.20\ \text{V})\cos(2500\ \text{rad/s}\, t)
 $$

for a $200\ \Omega $ resistor and a $5.0\ \mu\text{F} $ capacitor.

(a) Derive an expression for the circuit current.

(b) Determine the capacitive reactance of the capacitor.

(c) Derive an expression for the voltage across the capacitor.

## Setup
Since this is a series circuit, the current is the same through the capacitor as through the resistor.

Target variables:
- $i $
- $X_C $
- $v_C $

Use:
- Eq. (31.6) to find an expression for $i $ in terms of the angular frequency $\omega $,
- Eq. (31.18) to find $X_C $,
- Eq. (31.19) to find the capacitor voltage amplitude $V_C $,
- Eq. (31.16) to write an expression for $v_C $.

## Solution
### (a) Circuit current
From Eq. (31.6),

$$ 
v_R = iR
 $$

so

$$ 
i = \frac{v_R}{R}
= \frac{(1.20\ \text{V})\cos(2500\ \text{rad/s}\, t)}{200\ \Omega}
= (16.0\times 10^{-3}\ \text{A})\cos(2500\ \text{rad/s}\, t)
 $$

### (b) Capacitive reactance
From Eq. (31.18), the capacitive reactance at $\omega = 2500\ \text{rad/s} $ is

$$ 
X_C = \frac{1}{\omega C}
= \frac{1}{(2500\ \text{rad/s})(5.0\times 10^{-6}\ \text{F})}
= 80\ \Omega
 $$

### (c) Voltage across the capacitor
From Eq. (31.19), the capacitor voltage amplitude is

$$ 
V_C = IX_C = (16.0\times 10^{-3}\ \text{A})(80\ \Omega) = 0.48\ \text{V}
 $$

The capacitive reactance of the capacitor is 40% of the resistor’s resistance, so $V_C $ is 40% of $V_R $.

The instantaneous capacitor voltage is given by Eq. (31.16):

$$ 
v_C = V_C \cos(\omega t - 90^\circ)
 $$

or, in radians,

$$ 
v_C = (0.48\ \text{V})\cos(2500\ \text{rad/s}\, t - \pi/2)
 $$

## Evaluation
Although the same current passes through both the capacitor and the resistor, the voltages across them are different in both amplitude and phase.

Note that in the expression for $v_C $, the $90^\circ $ phase shift is converted to $\pi/2 $ rad so that all angular quantities have the same units. In ac circuit analysis, phase angles are often given in degrees, so be careful to convert to radians when necessary.

## Key concepts used
- In a series circuit, the current is the same through every element.
- For a resistor, $v_R = iR $ and voltage is in phase with current.
- For a capacitor, $X_C = 1/(\omega C) $.
- The capacitor voltage amplitude is $V_C = IX_C $.
- The capacitor voltage lags the current by $90^\circ $ $(\pi/2\ \text{rad}) $.
