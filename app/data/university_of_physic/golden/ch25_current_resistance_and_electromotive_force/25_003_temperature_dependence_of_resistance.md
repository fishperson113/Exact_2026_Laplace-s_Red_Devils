---
source: Young and Freedman University Physics, 13th ed.
chapter: 25
section: 25.4
example_number: 25.3
subtitle: Temperature dependence of resistance
needs_review: true
---

# Example 25.3: Temperature dependence of resistance

## Problem
Suppose the resistance of a copper wire is \(R_0 = 1.05\ \Omega\) at a reference temperature \(T_0 = 20^\circ\text{C}\). Find the resistance at \(T = 0^\circ\text{C}\) and at \(T = 100^\circ\text{C}\).

## Setup
We are given the resistance \(R_0\) at a reference temperature \(T_0\). We use Eq. (25.12) to find the resistances at \(T = 0^\circ\text{C}\) and \(T = 100^\circ\text{C}\) (our target variables), taking the temperature coefficient of resistivity from Table 25.2.

For copper,
\[
\alpha = 0.00393\ (\!^\circ\text{C})^{-1}.
\]

The resistance-temperature relation is
\[
R = R_0\left[1+\alpha (T-T_0)\right].
\]

## Solution
From Eq. (25.12),
\[
R = (1.05\ \Omega)\left[1 + (0.00393\ ^\circ\text{C}^{-1})(0^\circ\text{C} - 20^\circ\text{C})\right].
\]

So at \(T = 0^\circ\text{C}\),
\[
R = 0.97\ \Omega.
\]

At \(T = 100^\circ\text{C}\),
\[
R = (1.05\ \Omega)\left[1 + (0.00393\ ^\circ\text{C}^{-1})(100^\circ\text{C} - 20^\circ\text{C})\right].
\]

So at \(T = 100^\circ\text{C}\),
\[
R = 1.38\ \Omega.
\]

## Evaluation
The resistance at \(100^\circ\text{C}\) is greater than that at \(0^\circ\text{C}\) by a factor of
\[
\frac{1.38\ \Omega}{0.97\ \Omega} = 1.42.
\]

Thus, raising the temperature of the copper wire from \(0^\circ\text{C}\) to \(100^\circ\text{C}\) increases its resistance by \(42\%\).

From Eq. (25.11), this means that \(42\%\) more voltage is required to produce the same current at \(100^\circ\text{C}\) than at \(0^\circ\text{C}\). Designers of electric circuits that must operate over a wide temperature range must take this substantial effect into account.

## Key concepts used
- Temperature dependence of resistance
- Reference resistance \(R_0\) at temperature \(T_0\)
- Temperature coefficient of resistivity \(\alpha\)
- Linear approximation:
  \[
  R = R_0\left[1+\alpha (T-T_0)\right]
  \]
- Proportionality of voltage and current for ohmic behavior:
  \[
  V = IR
  \]
