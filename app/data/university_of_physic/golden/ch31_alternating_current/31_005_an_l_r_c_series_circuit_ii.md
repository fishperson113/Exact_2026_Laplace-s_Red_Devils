---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.4
example_number: 31.5
subtitle: An L-R-C series circuit II
needs_review: true
---

# Example 31.5: An L-R-C series circuit II

## Problem
For the L-R-C series circuit of Example 31.4, find expressions for the time dependence of the instantaneous current `i` and the instantaneous voltages across the resistor (`vR`), inductor (`vL`), capacitor (`vC`), and ac source (`v`).

## Setup
**IDENTIFY and SET UP:** We describe the current using Eq. (31.2), which assumes that the current is maximum at `t = 0`. The voltages are then given by Eq. (31.8) for the resistor, Eq. (31.10) for the inductor, Eq. (31.16) for the capacitor, and Eq. (31.25) for the source.

## Solution
**EXECUTE:** The current and the voltages all oscillate with the same angular frequency, `v`, and hence with the same period,

\[
T = \frac{2\pi}{v} = \frac{2\pi}{110{,}000\ \text{rad/s}} = 6.3 \times 10^{-4}\ \text{s} = 0.63\ \text{ms}.
\]

From Eq. (31.2), the current is

\[
i = I\cos vt = (0.10\ \text{A})\cos(110{,}000\ \text{rad/s})t.
\]

The resistor voltage is in phase with the current, so

\[
v_R = V_R\cos vt = (30\ \text{V})\cos(110{,}000\ \text{rad/s})t.
\]

The inductor voltage leads the current by `90°`, so

\[
v_L = V_L\cos(vt + 90^\circ) = -V_L\sin vt = -(60\ \text{V})\sin(110{,}000\ \text{rad/s})t.
\]

The capacitor voltage lags the current by `90°`, so

\[
v_C = V_C\cos(vt - 90^\circ) = V_C\sin vt = (20\ \text{V})\sin(110{,}000\ \text{rad/s})t.
\]

We found in Example 31.4 that the source voltage (equal to the voltage across the entire combination of resistor, inductor, and capacitor) leads the current by `53°`, so

\[
v = V\cos(vt + \phi) = (150\ \text{V})\cos\!\big[(110{,}000\ \text{rad/s})t + 0.93\ \text{rad}\big].
\]

Equivalently,

\[
v = (150\ \text{V})\cos\!\left[(110{,}000\ \text{rad/s})t + \left(\frac{2\pi\ \text{rad}}{360^\circ}\right)(53^\circ)\right].
\]

## Evaluation
Figure 31.15 graphs the four voltages versus time. The inductor voltage has a larger amplitude than the capacitor voltage because `X_L > X_C`.

The instantaneous source voltage `v` is always equal to the sum of the instantaneous voltages `vR`, `vL`, and `vC`. You should verify this by measuring the values of the voltages shown in the graph at different values of the time `t`.

## Key concepts used
- In an L-R-C series circuit, the same current flows through all elements.
- The current can be written as a cosine function with a chosen phase reference.
- For a resistor, voltage is in phase with current.
- For an inductor, voltage leads current by `90°`.
- For a capacitor, voltage lags current by `90°`.
- The source voltage has the same frequency as the current but can have a phase shift.
- The source voltage equals the instantaneous sum of the element voltages in the series circuit.
