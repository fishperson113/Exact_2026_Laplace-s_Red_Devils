---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.5
example_number: 30.8
subtitle: An oscillating circuit
needs_review: true
---

# Example 30.8: An oscillating circuit

## Problem
A 300-V dc power supply is used to charge a capacitor. After the capacitor is fully charged, it is disconnected from the power supply and connected across a 10-mH inductor. The resistance in the circuit is negligible.

(a) Find the frequency and period of oscillation of the circuit.

(b) Find the capacitor charge and the circuit current 1.2 ms after the inductor and capacitor are connected.

## Setup
IDENTIFY and SET UP: Our target variables are the oscillation frequency and period, as well as the charge \(q\) and current \(i\) at a particular time \(t\). We are given the capacitance \(C\) and the inductance \(L\), from which we can calculate the frequency and period using Eq. (30.22). We find the charge and current using Eqs. (30.21) and (30.23). Initially the capacitor is fully charged and the current is zero, as in Fig. 30.14a, so the phase angle is \(f = 0\) [see the discussion that follows Eq. (30.23)].

## Solution
EXECUTE:  
(a) The natural angular frequency is

\[
\omega = \sqrt{\frac{1}{LC}} = \sqrt{\frac{1}{(10 \times 10^{-3}\ \mathrm{H})(25 \times 10^{-6}\ \mathrm{F})}} = 2.0 \times 10^3\ \mathrm{rad/s}.
\]

The frequency and period \(T\) are then

\[
f = \frac{\omega}{2\pi} = \frac{2.0 \times 10^3\ \mathrm{rad/s}}{2\pi\ \mathrm{rad/cycle}} = 320\ \mathrm{Hz}
\]

and

\[
T = \frac{1}{f} = \frac{1}{320\ \mathrm{Hz}} = 3.1 \times 10^{-3}\ \mathrm{s} = 3.1\ \mathrm{ms}.
\]

(b) Since the period of the oscillation is \(T = 3.1\ \mathrm{ms}\), \(t = 1.2\ \mathrm{ms}\) equals \(0.38T\); this corresponds to a situation intermediate between Fig. 30.14b and Fig. 30.14c. Comparing those figures with Fig. 30.15, we expect the capacitor charge \(q\) to be negative (that is, there will be negative charge on the left-hand plate of the capacitor) and the current \(i\) to be negative as well (that is, current will flow counterclockwise).

To find the value of \(q\), we use Eq. (30.21),

\[
q = Q \cos(\omega t + f).
\]

The charge is maximum at \(t = 0\), so \(Q = CE\) and \(f = 0\). Hence Eq. (30.21) becomes

\[
q = (7.5 \times 10^{-3}\ \mathrm{C}) \cos(\omega t).
\]

At time \(t = 1.2 \times 10^{-3}\ \mathrm{s}\),

\[
\omega t = (2.0 \times 10^3\ \mathrm{rad/s})(1.2 \times 10^{-3}\ \mathrm{s}) = 2.4\ \mathrm{rad},
\]

so

\[
q = (7.5 \times 10^{-3}\ \mathrm{C})\cos(2.4\ \mathrm{rad}) = -5.5 \times 10^{-3}\ \mathrm{C}.
\]

From Eq. (30.23), the current \(i\) at any time is

\[
i = -\omega Q \sin(\omega t).
\]

At \(t = 1.2 \times 10^{-3}\ \mathrm{s}\),

\[
i = -(2.0 \times 10^3\ \mathrm{rad/s})(7.5 \times 10^{-3}\ \mathrm{C})\sin(2.4\ \mathrm{rad}) = -10\ \mathrm{A}.
\]

## Evaluation
The signs of \(q\) and \(i\) are both negative, as predicted.

## Key concepts used
- Oscillations in an ideal \(L C\) circuit
- Natural angular frequency: \(\omega = 1/\sqrt{LC}\)
- Frequency and period: \(f = \omega/2\pi\), \(T = 1/f\)
- Charge and current in an oscillating circuit:
  \[
  q = Q\cos(\omega t + \phi), \qquad i = -\omega Q \sin(\omega t + \phi)
  \]
- Initial conditions for a fully charged capacitor with zero current imply \(\phi = 0\)
