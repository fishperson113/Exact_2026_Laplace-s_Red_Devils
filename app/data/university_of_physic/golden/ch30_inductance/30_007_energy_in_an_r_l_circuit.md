---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.5
example_number: 30.7
subtitle: Energy in an R-L circuit
needs_review: true
---

# Example 30.7: Energy in an R-L circuit

## Problem
When the current in an R-L circuit is decaying, what fraction of the original energy stored in the inductor has been dissipated after 2.3 time constants?

## Setup
**IDENTIFY and SET UP:** This problem concerns current decay in an R-L circuit as well as the relationship between the current in an inductor and the amount of stored energy. The current at any time is given by Eq. (30.18); the stored energy associated with this current is given by Eq. (30.9).

## Solution
**EXECUTE:** From Eq. (30.18), the current at any time is
$$ 
i = I_0 e^{-(R/L)t}.
 $$

We substitute this into
$$ 
U = \frac{1}{2}Li^2
 $$
to obtain an expression for the stored energy at any time:
$$ 
U = \frac{1}{2}L I_0^2 e^{-2(R/L)t} = U_0 e^{-2(R/L)t},
 $$
where
$$ 
U_0 = \frac{1}{2}LI_0^2
 $$
is the energy at the initial time $t=0 $.

When
$$ 
t = 2.3\,\frac{L}{R},
 $$
we have
$$ 
U = U_0 e^{-2(2.3)} = U_0 e^{-4.6} = 0.010\,U_0.
 $$

That is, only 0.010 or 1.0% of the energy initially stored in the inductor remains.

## Evaluation
So 99.0% has been dissipated in the resistor. To get a sense of what this result means, consider the R-L circuit we analyzed in Example 30.6, for which
$$ 
L = 69\ \text{mH}, \qquad I_0 = 36\ \text{mA}, \qquad t = \frac{L}{R} = 390\ \text{ms}.
 $$

The initial stored energy is
$$ 
U_0 = \frac{1}{2}LI_0^2
= \frac{1}{2}(0.069\ \text{H})(0.036\ \text{A})^2
= 4.5\times 10^{-5}\ \text{J}.
 $$

Of this, 99.0%, or
$$ 
4.4\times 10^{-5}\ \text{J},
 $$
is dissipated in $2.3t = 0.90\ \text{ms} $.

In other words, this circuit can be almost completely powered off (or powered on) in 0.90 ms, so the minimum time for a complete on-off cycle is 1.8 ms. Even shorter cycle times are required for many purposes, such as in fast switching networks for telecommunications. In such cases a smaller time constant $t = L/R $ is needed.

## Key concepts used
- Inductor energy in an R-L circuit: $\displaystyle U = \frac{1}{2}Li^2 $
- Exponential current decay: $\displaystyle i = I_0 e^{-(R/L)t} $
- Energy decays twice as fast as current: $\displaystyle U = U_0 e^{-2(R/L)t} $
- Fraction of energy dissipated after a given number of time constants
