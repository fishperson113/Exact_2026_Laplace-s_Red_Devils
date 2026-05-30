---
source: Young and Freedman University Physics, 13th ed.
chapter: 25
section: 25.4
example_number: 25.5
subtitle: A source in a complete circuit
needs_review: true
---

# Example 25.5: A source in a complete circuit

## Problem
We add a resistor to the battery in Conceptual Example 25.4, forming a complete circuit (Fig. 25.17). What are the voltmeter and ammeter readings \(V_{ab}\) and \(I\) now?

## Setup
**IDENTIFY and SET UP:** Our target variables are the current \(I\) through the circuit and the potential difference \(V_{ab}\). We first find \(I\) using Eq. (25.16). To find \(V_{ab}\), we can use either Eq. (25.11) or Eq. (25.15).

The source has emf \(E = 12\ \text{V}\), internal resistance \(r = 2\ \Omega\), and the external resistor has resistance \(R = 4\ \Omega\).

## Solution
**EXECUTE:** The ideal ammeter has zero resistance, so the total resistance external to the source is \(R = 4\ \Omega\). From Eq. (25.16), the current through the circuit is then

\[
I=\frac{E}{R+r}=\frac{12\ \text{V}}{4\ \Omega+2\ \Omega}=2\ \text{A}
\]

Our idealized conducting wires and the idealized ammeter have zero resistance, so there is no potential difference between points \(a\) and \(a'\) or between points \(b'\) and \(b\); that is,

\[
V_{ab}=V_{a'b'}.
\]

We find \(V_{a'b'}\) by considering \(a'\) and \(b'\) as the terminals of the resistor: From Ohm’s law, Eq. (25.11), we then have

\[
V_{a'b'} = IR = (2\ \text{A})(4\ \Omega)=8\ \text{V}.
\]

Alternatively, we can consider \(a\) and \(b\) as the terminals of the source. Then, from Eq. (25.15),

\[
V_{ab}=E-Ir=(12\ \text{V})-(2\ \text{A})(2\ \Omega)=8\ \text{V}.
\]

Either way, we see that the voltmeter reading is \(8\ \text{V}\).

## Evaluation
With current flowing through the source, the terminal voltage \(V_{ab}\) is less than the emf \(E\). The smaller the internal resistance \(r\), the less the difference between \(V_{ab}\) and \(E\).

## Key concepts used
- Ideal ammeter has zero resistance.
- Ohm’s law: \(V=IR\).
- Terminal voltage of a source with internal resistance: \(V_{ab}=E-Ir\).
- Current in a complete circuit: \(I=\dfrac{E}{R+r}\).
