---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.3
example_number: 31.4
subtitle: An L-R-C series circuit I
needs_review: true
---

# Example 31.4: An L-R-C series circuit I

## Problem
In the series circuit of Fig. 31.13a, suppose \(v = 10{,}000\ \text{rad/s}\), \(V = 50\ \text{V}\), \(C = 0.50\ \text{mF}\), \(L = 60\ \text{mH}\), and \(R = 300\ \Omega\). Find the reactances \(X_L\) and \(X_C\), the impedance \(Z\), the current amplitude \(I\), the phase angle \(\phi\), and the voltage amplitude across each circuit element.

## Setup
This problem uses the ideas developed in Section 31.2 and this section about the behavior of circuit elements in an ac circuit. Use Eqs. (31.12) and (31.18) to determine \(X_L\) and \(X_C\), and Eq. (31.23) to find \(Z\). Then use Eq. (31.22) to find the current amplitude and Eq. (31.24) to find the phase angle. The relationships in Table 31.1 then yield the voltage amplitudes.

## Solution
The inductive and capacitive reactances are
\[
X_L = vL = (10{,}000\ \text{rad/s})(60\ \text{mH}) = 600\ \Omega
\]
\[
X_C = \frac{1}{vC} = \frac{1}{(10{,}000\ \text{rad/s})(0.50\ \text{mF})} = 200\ \Omega
\]

The impedance of the circuit is then
\[
Z = \sqrt{R^2 + (X_L - X_C)^2}
= \sqrt{(300\ \Omega)^2 + (600\ \Omega - 200\ \Omega)^2}
= 500\ \Omega
\]

With source voltage amplitude \(V = 50\ \text{V}\), the current amplitude \(I\) and phase angle \(\phi\) are
\[
I = \frac{V}{Z} = \frac{50\ \text{V}}{500\ \Omega} = 0.10\ \text{A}
\]
\[
\phi = \arctan\!\left(\frac{X_L - X_C}{R}\right)
= \arctan\!\left(\frac{400\ \Omega}{300\ \Omega}\right)
= 53^\circ
\]

From Table 31.1, the voltage amplitudes across the resistor, inductor, and capacitor, respectively, are
\[
V_R = IR = (0.10\ \text{A})(300\ \Omega) = 30\ \text{V}
\]
\[
V_L = IX_L = (0.10\ \text{A})(600\ \Omega) = 60\ \text{V}
\]
\[
V_C = IX_C = (0.10\ \text{A})(200\ \Omega) = 20\ \text{V}
\]

## Evaluation
As in Fig. 31.13b, \(X_L > X_C\); hence the voltage amplitude across the inductor is greater than that across the capacitor and \(\phi\) is positive. The value \(\phi = 53^\circ\) means that the voltage leads the current by \(53^\circ\). Note that the source voltage amplitude \(V = 50\ \text{V}\) is not equal to the sum of the voltage amplitudes across the separate circuit elements: \(50\ \text{V} \neq 30\ \text{V} + 60\ \text{V} + 20\ \text{V}\). Instead, \(V\) is the vector sum of the \(V_R\) and \(V_L - V_C\) phasors. If you draw the phasor diagram like Fig. 31.13b for this particular situation, you’ll see that \(V_R\) and \(V_L - V_C\) constitute a 3-4-5 right triangle.

## Key concepts used
- Inductive reactance: \(X_L = vL\)
- Capacitive reactance: \(X_C = \dfrac{1}{vC}\)
- Impedance of a series \(L\)-\(R\)-\(C\) circuit: \(Z = \sqrt{R^2 + (X_L - X_C)^2}\)
- Current amplitude: \(I = \dfrac{V}{Z}\)
- Phase angle: \(\phi = \arctan\!\left(\dfrac{X_L - X_C}{R}\right)\)
- Voltage amplitudes in a series ac circuit: \(V_R = IR\), \(V_L = IX_L\), \(V_C = IX_C\)
