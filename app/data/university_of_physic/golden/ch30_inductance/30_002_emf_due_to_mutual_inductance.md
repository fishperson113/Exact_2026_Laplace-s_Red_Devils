---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.2
example_number: 30.2
subtitle: Emf due to mutual inductance
needs_review: true
---

# Example 30.2: Emf due to mutual inductance

## Problem
In Example 30.1, suppose the current in the outer coil is given by \(i_2 = 12.0 \times 10^6\ \text{A/s}^2\, t\). (Currents in wires can indeed increase this rapidly for brief periods.)  
(a) At \(t = 3.0\ \text{ms}\), what is the average magnetic flux through each turn of the solenoid (coil 1) due to the current in the outer coil?  
(b) What is the induced emf in the solenoid?

## Setup
### IDENTIFY and SET UP
In Example 30.1 we found the mutual inductance by relating the current in the solenoid to the flux produced in the outer coil; to do that, we used Eq. (30.5) in the form
\[
M = \frac{N_1 \mathcal{E}_{B1}}{i_2}.
\]
Here we are given the current \(i_2\) in the outer coil and want to find the resulting flux \(\mathcal{E}_{B1}\) in the solenoid. The mutual inductance is the same in either case, and we have
\[
M = 25\ \text{mH}
\]
from Example 30.1. We use Eq. (30.5) in the form
\[
\mathcal{E}_{B1} = \frac{M i_2}{N_1}
\]
to determine the average flux through each turn of the solenoid caused by a given current \(i_2\) in the outer coil. We then use Eq. (30.4) to determine the emf induced in the solenoid by the time variation of \(i_2\).

## Solution
### EXECUTE
(a) At \(t = 3.0\ \text{ms} = 3.0 \times 10^{-3}\ \text{s}\), the current in the outer coil is
\[
i_2 = 12.0 \times 10^6\ \text{A/s}^2 (3.0 \times 10^{-3}\ \text{s}) = 6.0 \times 10^4\ \text{A}.
\]
We solve Eq. (30.5) for the flux through each turn of the solenoid (coil 1):
\[
\mathcal{E}_{B1} = \frac{Mi_2}{N_1}
= \frac{(25 \times 10^{-3}\ \text{H})(6.0 \times 10^4\ \text{A})}{1000}
= 1.5 \times 10^{-7}\ \text{Wb}.
\]
We emphasize that this is an average value; the flux can vary considerably between the center and the ends of the solenoid.

(b) We are given
\[
\frac{di_2}{dt} = 12.0 \times 10^6\ \text{A/s}^2,
\]
so then, from Eq. (30.4), the induced emf in the solenoid is
\[
\mathcal{E}_1 = -M \frac{di_2}{dt}
= -(25 \times 10^{-3}\ \text{H})(12.0 \times 10^6\ \text{A/s}^2)
= -50\ \text{V}.
\]

## Evaluation
This is a substantial induced emf in response to a very rapid current change. In an operating Tesla coil, there is a high-frequency alternating current rather than a continuously increasing current as in this example; both \(i_2\) and \(\mathcal{E}_1\) alternate as well, with amplitudes that can be thousands of times larger than in this example.

## Key concepts used
- Mutual inductance relates the flux through one coil to the current in the other:
  \[
  \mathcal{E}_{B1} = M i_2 / N_1.
  \]
- The induced emf due to a changing current is
  \[
  \mathcal{E}_1 = -M \, \frac{di_2}{dt}.
  \]
- The minus sign reflects Lenz’s law: the induced emf opposes the change in current.
