---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.5
example_number: 26.12
subtitle: Charging a capacitor
needs_review: true
---

# Example 26.12: Charging a capacitor

## Problem
A resistor is connected in series with a capacitor and a battery with emf 12.0 V. Before the switch is closed, at time \(t = 0\), the capacitor is uncharged.  
(a) What is the time constant?  
(b) What fraction of the final charge is on the capacitor at \(t = 46\ \text{s}\)?  
(c) What fraction of the initial current is still flowing at \(t = 46\ \text{s}\)?

## Setup
IDENTIFY and SET UP: This is the same situation as shown in Fig. 26.20, with \(E = 12.0\ \text{V}\), \(C = 1.0\ \text{mF}\), and \(R = 10\ \text{M}\Omega\). The charge \(q\) and current \(i\) vary with time as shown in Fig. 26.21. Our target variables are (a) the time constant \(\tau\), (b) the ratio \(q/Q_f\) at \(t = 46\ \text{s}\), and (c) the ratio \(i/I_0\) at \(t = 46\ \text{s}\). Equation (26.14) gives \(\tau = RC\). For a capacitor being charged, Eq. (26.12) gives \(q\) and Eq. (26.13) gives \(i\).

## Solution
EXECUTE: (a) From Eq. (26.14),
\[
\tau = RC = \left(10 \times 10^6\ \Omega\right)\left(1.0 \times 10^{-6}\ \text{F}\right) = 10\ \text{s}
\]

(b) From Eq. (26.12),
\[
\frac{q}{Q_f} = 1 - e^{-t/RC} = 1 - e^{-46\ \text{s}/10\ \text{s}} = 0.99
\]

(c) From Eq. (26.13),
\[
\frac{i}{I_0} = e^{-t/RC} = e^{-46\ \text{s}/10\ \text{s}} = 0.010
\]

## Evaluation
After 4.6 time constants the capacitor is 99% charged and the charging current has decreased to 1.0% of its initial value. The circuit would charge more rapidly if we reduced the time constant by using a smaller resistance.

## Key concepts used
- RC time constant: \(\tau = RC\)
- Charging capacitor charge: \(q = Q_f \left(1 - e^{-t/RC}\right)\)
- Charging capacitor current: \(i = I_0 e^{-t/RC}\)
- Larger resistance gives a larger time constant and slower charging
