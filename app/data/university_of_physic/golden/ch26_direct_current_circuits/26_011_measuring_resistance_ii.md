---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.3
example_number: 26.11
subtitle: Measuring resistance II
needs_review: true
---

# Example 26.11: Measuring resistance II

## Problem
Suppose the meters of Example 26.10 are connected to a different resistor as shown in Fig. 26.16b, and the readings obtained on the meters are the same as in Example 26.10. What is the value of this new resistance \(R\), and what is the power dissipated in the resistor?

## Setup
IDENTIFY and SET UP: In Example 26.10 the ammeter read the actual current through the resistor, but the voltmeter reading was not the same as the potential difference across the resistor. Now the situation is reversed: The voltmeter reading shows the actual potential difference across the resistor, but the ammeter reading is not equal to the current \(I\) through the resistor.

Applying the junction rule at \(b\) in Fig. 26.16b shows that
\[
I_A = I + I_V,
\]
where \(I_V\) is the current through the voltmeter.

We find \(I_V\) from the given values of \(V\) and the voltmeter resistance \(R_V\), and we use this value to find the resistor current \(I\). We then determine the resistance \(R\) from \(I\) and the voltmeter reading, and calculate the power as in Example 26.10.

Given values:
\[
I_A = 0.100\ \text{A}, \quad V = 12.0\ \text{V}, \quad R_A = 2.00\ \Omega, \quad R_V = 10{,}000\ \Omega.
\]

## Solution
From Ohm’s law,
\[
V_{bc} = I_A R_A = (0.100\ \text{A})(2.00\ \Omega) = 0.200\ \text{V}.
\]

Then
\[
V_{ab} = V - V_{bc} = 12.0\ \text{V} - 0.200\ \text{V} = 11.8\ \text{V}.
\]

The current through the voltmeter is
\[
I_V = \frac{V}{R_V} = \frac{12.0\ \text{V}}{10{,}000\ \Omega} = 1.20\ \text{mA}.
\]

So the actual current in the resistor is
\[
I = I_A - I_V = 0.100\ \text{A} - 0.0012\ \text{A} = 0.0988\ \text{A}.
\]

Hence the resistance is
\[
R = \frac{V_{ab}}{I} = \frac{11.8\ \text{V}}{0.0988\ \text{A}} \approx 121\ \Omega.
\]

The power dissipated in the resistor is
\[
P = V_{ab} I = (11.8\ \text{V})(0.0988\ \text{A}) \approx 1.18\ \text{W}.
\]

## Evaluation
Had the meters been ideal, our results would have been \(R = 12.0\ \text{V}/0.100\ \text{A} = 120\ \Omega\) and \(P = 12.0\ \text{V} \times 0.100\ \text{A} = 1.2\ \text{W}\), both here and in Example 26.10.

The actual (correct) results are not too different in either case. That’s because the ammeter and voltmeter are nearly ideal: compared with the resistance \(R\) under test, the ammeter resistance \(R_A\) is very small and the voltmeter resistance \(R_V\) is very large. Under these conditions, treating the meters as ideal yields pretty good results; accurate work requires calculations as in these two examples.

## Key concepts used
- Ammeter and voltmeter are nonideal measuring instruments.
- Kirchhoff’s junction rule.
- Ohm’s law, \(V = IR\).
- Power dissipated in a resistor: \(P = VI\).
- Meter loading effects: ammeter resistance should be small, voltmeter resistance should be large.
