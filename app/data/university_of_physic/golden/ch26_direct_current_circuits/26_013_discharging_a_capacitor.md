---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.5
example_number: 26.13
subtitle: Discharging a capacitor
needs_review: true
---

# Example 26.13: Discharging a capacitor

## Problem
The resistor and capacitor of Example 26.12 are reconnected as shown in Fig. 26.22. The capacitor has an initial charge \(Q_0 = 5.0 \times 10^{-6}\ \text{C}\) and is discharged by closing the switch at \(t = 0\). At what time will the charge be equal to \(q = 0.50\ \text{mC}\)? What is the current at this time?

## Setup
**IDENTIFY and SET UP:** Now the capacitor is being discharged, so \(q\) and \(i\) vary with time as in Fig. 26.23, with  
\[
q = Q_0 e^{-t/RC}
\]
and
\[
i = -\frac{Q_0}{RC}e^{-t/RC}.
\]

Again we have \(RC = 10\ \text{s}\).

Our target variables are:
- (a) the value of \(t\) at which \(q = 0.50\ \text{mC}\),
- (b) the value of \(i\) at this time.

We first solve Eq. (26.16) for \(t\), and then solve Eq. (26.17) for \(i\).

## Solution
**EXECUTE:**  

(a) Solving Eq. (26.16) for the time \(t\) gives
\[
t = -RC \ln \left(\frac{q}{Q_0}\right).
\]
With \(Q_0 = 5.0\ \text{mC}\) and \(q = 0.50\ \text{mC}\),
\[
t = -(10\ \text{s}) \ln \left(\frac{0.50\ \text{mC}}{5.0\ \text{mC}}\right)
= -(10\ \text{s}) \ln(0.10)
= 23\ \text{s} \approx 2.3t.
\]

(b) From Eq. (26.17), with \(e^{-t/RC} = 0.10\),
\[
i = -\frac{Q_0}{RC}e^{-t/RC}
= -\frac{5.0 \times 10^{-6}\ \text{C}}{10\ \text{s}}(0.10)
= -5.0 \times 10^{-8}\ \text{A}.
\]

## Evaluation
The current in part (b) is negative because \(i\) has the opposite sign when the capacitor is discharging than when it is charging.

Note that we could have avoided evaluating \(i\) by noticing that at the time in question,
\[
q = 0.10Q_0.
\]
From Eq. (26.16), this means that
\[
e^{-t/RC} = 0.10,
\]
which leads directly to the same result for \(i\).

## Key concepts used
- Exponential discharge of a capacitor:
  \[
  q = Q_0 e^{-t/RC}
  \]
- Discharge current:
  \[
  i = -\frac{Q_0}{RC}e^{-t/RC}
  \]
- Solving for time using a logarithm:
  \[
  t = -RC \ln\left(\frac{q}{Q_0}\right)
  \]
- During discharge, current is negative by the chosen sign convention.
