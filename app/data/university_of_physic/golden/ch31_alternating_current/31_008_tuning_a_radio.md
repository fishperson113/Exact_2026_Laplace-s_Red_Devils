---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.5
example_number: 31.8
subtitle: Tuning a radio
needs_review: false
---

# Example 31.8: Tuning a radio

## Problem
The series circuit in Fig. 31.20 is similar to some radio tuning circuits. It is connected to a variable-frequency ac source with an rms terminal voltage of 1.0 V.

(a) Find the resonance frequency. At the resonance frequency, find  
(b) the inductive reactance \(X_L\), the capacitive reactance \(X_C\), and the impedance \(Z\);  
(c) the rms current \(I_{\mathrm{rms}}\);  
(d) the rms voltage across each circuit element.

## Setup
**IDENTIFY and SET UP:** Figure 31.20 shows an L-R-C series circuit, with ideal meters inserted to measure the rms current and voltages, our target variables.

Equations (31.32) include the formula for the resonance angular frequency
\[
\omega_0=\frac{1}{\sqrt{LC}}
\]
from which we find the resonance frequency
\[
f_0=\frac{\omega_0}{2\pi}.
\]

We use Eqs. (31.12) and (31.18) to find \(X_L\) and \(X_C\), which are equal at resonance; at resonance, from Eq. (31.23),
\[
Z=R.
\]

We use Eqs. (31.7), (31.13), and (31.19) to find the voltages across the circuit elements.

## Solution
**EXECUTE:**  
(a) The values of \(L\) and \(C\) are
\[
L=0.40\ \text{mH}, \qquad C=100\ \text{pF}.
\]
So,
\[
\omega_0=\frac{1}{\sqrt{LC}}
=\frac{1}{\sqrt{(0.40\times 10^{-3}\ \text{H})(100\times 10^{-12}\ \text{F})}}
=5.0\times 10^{6}\ \text{rad/s}.
\]
Then
\[
f_0=\frac{\omega_0}{2\pi}=8.0\times 10^{5}\ \text{Hz}=800\ \text{kHz}.
\]
This frequency is in the lower part of the AM radio band.

(b) At this frequency,
\[
X_L=\omega L=(5.0\times 10^{6}\ \text{rad/s})(0.40\times 10^{-3}\ \text{H})=2000\ \Omega,
\]
\[
X_C=\frac{1}{\omega C}
=\frac{1}{(5.0\times 10^{6}\ \text{rad/s})(100\times 10^{-12}\ \text{F})}
=2000\ \Omega.
\]
Since \(X_L=X_C\) at resonance as stated above, \(Z=R\), so
\[
Z=R=500\ \Omega.
\]

(c) From Eq. (31.26) the rms current at resonance is
\[
I_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{Z}
=\frac{1.0\ \text{V}}{500\ \Omega}
=0.0020\ \text{A}
=2.0\ \text{mA}.
\]

(d) The rms potential difference across the resistor is
\[
V_{R,\mathrm{rms}}=I_{\mathrm{rms}}R=(0.0020\ \text{A})(500\ \Omega)=1.0\ \text{V}.
\]
The rms potential differences across the inductor and capacitor are
\[
V_{L,\mathrm{rms}}=I_{\mathrm{rms}}X_L=(0.0020\ \text{A})(2000\ \Omega)=4.0\ \text{V},
\]
\[
V_{C,\mathrm{rms}}=I_{\mathrm{rms}}X_C=(0.0020\ \text{A})(2000\ \Omega)=4.0\ \text{V}.
\]

## Evaluation
The potential differences across the inductor and the capacitor have equal rms values and amplitudes, but are \(180^\circ\) out of phase and so add to zero at each instant. Note also that at resonance, \(V_{R,\mathrm{rms}}\) is equal to the source voltage \(V_{\mathrm{rms}}\), while in this example, \(V_{L,\mathrm{rms}}\) and \(V_{C,\mathrm{rms}}\) are both considerably larger than \(V_{\mathrm{rms}}\).

## Key concepts used
- Resonance in a series \(L\)-\(R\)-\(C\) circuit occurs when \(X_L=X_C\).
- Resonance angular frequency:
  \[
  \omega_0=\frac{1}{\sqrt{LC}}
  \]
- Resonance frequency:
  \[
  f_0=\frac{\omega_0}{2\pi}
  \]
- At resonance, the impedance of a series \(L\)-\(R\)-\(C\) circuit is
  \[
  Z=R
  \]
- Ohm’s law for ac:
  \[
  I_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{Z}
  \]
- Element voltages in ac circuits:
  \[
  V_{R,\mathrm{rms}}=I_{\mathrm{rms}}R,\quad
  V_{L,\mathrm{rms}}=I_{\mathrm{rms}}X_L,\quad
  V_{C,\mathrm{rms}}=I_{\mathrm{rms}}X_C
  \]
