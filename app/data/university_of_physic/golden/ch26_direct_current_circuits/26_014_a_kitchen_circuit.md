---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.5
example_number: 26.14
subtitle: A kitchen circuit
needs_review: false
---

# Example 26.14: A kitchen circuit

## Problem
An 1800-W toaster, a 1.3-kW electric frying pan, and a 100-W lamp are plugged into the same 20-A, 120-V circuit.

(a) What current is drawn by each device, and what is the resistance of each device?

(b) Will this combination trip the circuit breaker?

## Setup
**IDENTIFY and SET UP:** When plugged into the same circuit, the three devices are connected in parallel, so the voltage across each appliance is \(V = 120\ \text{V}\).

We find the current \(I\) drawn by each device using the relationship \(P = VI\), where \(P\) is the power input of the device. To find the resistance \(R\) of each device we use the relationship \(P = V^2/R\).

## Solution
**EXECUTE:**  
(a) To simplify the calculation of current and resistance, we note that
\[
I = \frac{P}{V}
\qquad \text{and} \qquad
R = \frac{V^2}{P}.
\]

Hence
\[
R_{\text{lamp}} = \frac{(120\ \text{V})^2}{100\ \text{W}} = 144\ \Omega
\]
\[
I_{\text{lamp}} = \frac{100\ \text{W}}{120\ \text{V}} = 0.83\ \text{A}
\]

\[
R_{\text{frying pan}} = \frac{(120\ \text{V})^2}{1300\ \text{W}} = 11\ \Omega
\]
\[
I_{\text{frying pan}} = \frac{1300\ \text{W}}{120\ \text{V}} = 11\ \text{A}
\]

\[
R_{\text{toaster}} = \frac{(120\ \text{V})^2}{1800\ \text{W}} = 8\ \Omega
\]
\[
I_{\text{toaster}} = \frac{1800\ \text{W}}{120\ \text{V}} = 15\ \text{A}
\]

For constant voltage the device with the least resistance (in this case the toaster) draws the most current and receives the most power.

(b) The total current through the line is the sum of the currents drawn by the three devices:
\[
I = I_{\text{toaster}} + I_{\text{frying pan}} + I_{\text{lamp}}
\]
\[
I = 15\ \text{A} + 11\ \text{A} + 0.83\ \text{A} = 27\ \text{A}
\]

This exceeds the 20-A rating of the line, and the circuit breaker will indeed trip.

## Evaluation
We could also find the total current by using
\[
I = \frac{P_{\text{toaster}} + P_{\text{frying pan}} + P_{\text{lamp}}}{V}
\]
and dividing the total power \(P\) delivered to all three devices by the voltage:
\[
I = \frac{1800\ \text{W} + 1300\ \text{W} + 100\ \text{W}}{120\ \text{V}} = 27\ \text{A}
\]

A third way to determine \(I\) is to use
\[
I = \frac{V}{R_{\text{eq}}}
\]
where \(R_{\text{eq}}\) is the equivalent resistance of the three devices in parallel:
\[
I = (120\ \text{V})\left(\frac{1}{8\ \Omega} + \frac{1}{11\ \Omega} + \frac{1}{144\ \Omega}\right) = 27\ \text{A}
\]

Appliances with such current demands are common, so modern kitchens have more than one 20-A circuit. To keep currents safely below 20 A, the toaster and frying pan should be plugged into different circuits.

## Key concepts used
- Devices in the same household circuit are connected in parallel, so each has the same voltage.
- Power, current, and voltage are related by \(P = VI\).
- Resistance can be found from \(P = V^2/R\).
- Currents in parallel branches add to give the total line current.
- If the total current exceeds the circuit breaker rating, the breaker trips.
