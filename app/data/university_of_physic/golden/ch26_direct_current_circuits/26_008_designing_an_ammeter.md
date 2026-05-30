---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.3
example_number: 26.8
subtitle: Designing an ammeter
needs_review: false
---

# Example 26.8: Designing an ammeter

## Problem
What shunt resistance is required to make the 1.00-mA meter described above into an ammeter with a range of 0 to 50.0 mA?

## Setup
Since the meter is being used as an ammeter, its internal connections are as shown in Fig. 26.15a. Our target variable is the shunt resistance \(R_{\text{sh}}\), which we will find using Eq. (26.7). The ammeter must handle a maximum current
\[
I_a = 50.0 \times 10^{-3}\ \text{A}.
\]
The coil resistance is
\[
R_c = 20.0\ \Omega,
\]
and the meter shows full-scale deflection when the current through the coil is
\[
I_{fs} = 1.00 \times 10^{-3}\ \text{A}.
\]

## Solution
Solving Eq. (26.7) for \(R_{\text{sh}}\), we find
\[
R_{\text{sh}}=\frac{I_{fs}R_c}{I_a-I_{fs}}
=\frac{(1.00\times 10^{-3}\ \text{A})(20.0\ \Omega)}{50.0\times 10^{-3}\ \text{A}-1.00\times 10^{-3}\ \text{A}}
=0.408\ \Omega.
\]

## Evaluation
It’s useful to consider the equivalent resistance of the ammeter as a whole. From Eq. (26.2),
\[
R_{\text{eq}}=\left(\frac{1}{R_c}+\frac{1}{R_{\text{sh}}}\right)^{-1}
=\left(\frac{1}{20.0\ \Omega}+\frac{1}{0.408\ \Omega}\right)^{-1}
=0.400\ \Omega.
\]
The shunt resistance is so small in comparison to the coil resistance that the equivalent resistance is very nearly equal to the shunt resistance. The result is an ammeter with a low equivalent resistance and the desired 0-50.0-mA range. At full-scale deflection, the current through the galvanometer is 1.00 mA, the current through the shunt resistor is 49.0 mA, and
\[
V_{ab}=0.0200\ \text{V}.
\]
If the current \(I\) is less than 50.0 mA, the coil current and the deflection are proportionally less.

## Key concepts used
- An ammeter is made by connecting a shunt resistance in parallel with the meter coil.
- The shunt diverts most of the current, allowing the meter to measure larger currents.
- Full-scale deflection occurs when the coil current reaches \(I_{fs}\).
- The shunt resistance is found from the current-splitting relation for parallel branches.
- The equivalent resistance of the ammeter should be small.
