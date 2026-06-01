---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.3
example_number: 30.4
subtitle: Calculating self-induced emf
needs_review: true
---

# Example 30.4: Calculating self-induced emf

## Problem
If the current in the toroidal solenoid in Example 30.3 increases uniformly from 0 to 6.0 A in 3.0 ms, find the magnitude and direction of the self-induced emf.

## Setup
**IDENTIFY and SET UP:** We are given the self-inductance $L $ and the rate of change of the solenoid current. We find the magnitude of the self-induced emf using Eq. (30.7) and its direction using Lenz’s law.

From Example 30.3, the self-inductance is
$$ 
L = 140 \times 10^{-6}\ \text{H}.
 $$

The current changes from $0 $ to $6.0\ \text{A} $ in
$$ 
\Delta t = 3.0 \times 10^{-3}\ \text{s},
 $$
so
$$ 
\frac{di}{dt} = \frac{6.0\ \text{A}}{3.0 \times 10^{-3}\ \text{s}} = 2.0 \times 10^{3}\ \text{A/s}.
 $$

## Solution
**EXECUTE:** Using Eq. (30.7),
$$ 
|\mathcal{E}| = L \left|\frac{di}{dt}\right|
 $$
$$ 
|\mathcal{E}| = (140 \times 10^{-6}\ \text{H})(2.0 \times 10^{3}\ \text{A/s}) = 0.28\ \text{V}.
 $$

Because the current is increasing, Lenz’s law says that the induced emf must oppose the increase in current. Therefore, the emf is directed opposite to the current.

For the terminals shown in the figure from Example 30.3, this corresponds to an emf directed from $b $ to $a $, like a battery with $a $ as the negative terminal and $b $ as the positive terminal, tending to oppose the current increase from the external circuit.

## Evaluation
This example shows that even a small inductance can give rise to a substantial induced emf if the current changes rapidly.

## Key concepts used
- Self-induced emf in an inductor:
  $$ 
  \mathcal{E} = -L\frac{di}{dt}
   $$
- Magnitude:
  $$ 
  |\mathcal{E}| = L\left|\frac{di}{dt}\right|
   $$
- Lenz’s law: the induced emf opposes the change in current
- Direction of emf follows the direction needed to oppose an increasing current
