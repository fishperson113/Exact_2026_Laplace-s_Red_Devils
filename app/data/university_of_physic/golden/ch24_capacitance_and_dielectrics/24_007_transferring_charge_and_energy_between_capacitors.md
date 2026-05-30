---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.3
example_number: 24.7
subtitle: Transferring charge and energy between capacitors
needs_review: true
---

# Example 24.7: Transferring charge and energy between capacitors

## Problem
We connect a capacitor \(C_1\) to a power supply, charge it to a potential difference \(V_0\), and disconnect the power supply (Fig. 24.12). Switch \(S\) is open.

(a) What is the charge \(Q_0\) on \(C_1\)?  
(b) What is the energy stored in \(C_1\)?  
(c) Capacitor \(C_2\) is initially uncharged. We close switch \(S\). After charge no longer flows, what are the potential difference across each capacitor and the charge on each capacitor?  
(d) What is the final energy of the system?

Given:
- \(C_1 = 8.0\ \text{mF}\)
- \(C_2 = 4.0\ \text{mF}\)
- \(V_0 = 120\ \text{V}\)

## Setup
**IDENTIFY and SET UP:** In parts (a) and (b) we find the charge \(Q_0\) and stored energy \(U_{\text{initial}}\) for the single charged capacitor \(C_1\) using Eqs. (24.1) and (24.9), respectively. After we close switch \(S\), one wire connects the upper plates of the two capacitors and another wire connects the lower plates; the capacitors are now connected in parallel. In part (c) we use the character of the parallel connection to determine how \(Q_0\) is shared between the two capacitors. In part (d) we again use Eq. (24.9) to find the energy stored in capacitors \(C_1\) and \(C_2\); the energy of the system is the sum of these values.

## Solution
**EXECUTE:**

(a) The initial charge on \(C_1\) is
\[
Q_0 = C_1 V_0 = (8.0\ \text{mF})(120\ \text{V}) = 960\ \text{mC}.
\]

(b) The energy initially stored in \(C_1\) is
\[
U_{\text{initial}} = \frac{1}{2} Q_0 V_0
= \frac{1}{2}(960\times 10^{-6}\ \text{C})(120\ \text{V})
= 0.058\ \text{J}.
\]

(c) When we close the switch, the positive charge \(Q_0\) is distributed over the upper plates of both capacitors and the negative charge \(-Q_0\) is distributed over the lower plates. Let \(Q_1\) and \(Q_2\) be the magnitudes of the final charges on the capacitors. Conservation of charge requires that
\[
Q_1 + Q_2 = Q_0.
\]
The potential difference between the plates is the same for both capacitors because they are connected in parallel, so
\[
Q_1 = C_1 V, \qquad Q_2 = C_2 V.
\]
We now have three independent equations relating the three unknowns \(Q_1\), \(Q_2\), and \(V\). Solving these, we find
\[
V = \frac{Q_0}{C_1 + C_2}
= \frac{960\ \text{mC}}{8.0\ \text{mF} + 4.0\ \text{mF}}
= 80\ \text{V},
\]
so
\[
Q_1 = (8.0\ \text{mF})(80\ \text{V}) = 640\ \text{mC},
\qquad
Q_2 = (4.0\ \text{mF})(80\ \text{V}) = 320\ \text{mC}.
\]

(d) The final energy of the system is
\[
U_{\text{final}} = \frac{1}{2}Q_1V + \frac{1}{2}Q_2V
= \frac{1}{2}Q_0V
= \frac{1}{2}(960\times 10^{-6}\ \text{C})(80\ \text{V})
= 0.038\ \text{J}.
\]

## Evaluation
The final energy is less than the initial energy; the difference was converted to energy of some other form. The conductors become a little warmer because of their resistance, and some energy is radiated as electromagnetic waves. We’ll study the behavior of capacitors in more detail in Chapters 26 and 31.

## Key concepts used
- Capacitance relation: \(Q = CV\)
- Energy stored in a capacitor: \(U = \tfrac{1}{2}QV = \tfrac{1}{2}CV^2 = \tfrac{Q^2}{2C}\)
- Conservation of charge
- Capacitors connected in parallel have the same potential difference
- Total energy after redistribution is the sum of the energies of the individual capacitors
