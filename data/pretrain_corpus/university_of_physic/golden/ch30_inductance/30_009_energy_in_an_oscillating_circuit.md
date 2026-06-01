---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.6
example_number: 30.9
subtitle: Energy in an oscillating circuit
needs_review: true
---

# Example 30.9: Energy in an oscillating circuit

## Problem
For the L-C circuit of Example 30.8, find the magnetic and electric energies (a) at `t = 0` and (b) at `t = 1.2 ms`.

## Setup
We must calculate the magnetic energy stored in the inductor and the electric energy stored in the capacitor at two times during the L-C circuit oscillation.

From Example 30.8, we know the values of the capacitor charge `q` and circuit current `i` for both times. We use them to calculate
- magnetic energy: `U_B = 1/2 L i^2`
- electric energy: `U_E = q^2 / (2C)`

## Solution
(a) At `t = 0` there is no current and `q = Q`. Hence there is no magnetic energy, and all the energy in the circuit is in the form of electric energy in the capacitor:

`U_B = 1/2 L i^2 = 0`

`U_E = Q^2 / (2C) = (17.5 × 10^-3 C)^2 / (125 × 10^-6 F) = 1.1 J`

(b) From Example 30.8, at `t = 1.2 ms` we have `q = -5.5 × 10^-3 C` and `i = -10 A`. Hence

`U_E = q^2 / (2C) = (-5.5 × 10^-3 C)^2 / (125 × 10^-6 F) = 0.6 J`

`U_B = 1/2 L i^2 = 1/2 (10 × 10^-3 H)(-10 A)^2 = 0.5 J`

## Evaluation
The magnetic and electric energies are the same at halfway between the situations in Figs. 30.14b and 30.14c. We saw in Example 30.8 that the time considered in part (b), `t = 1.2 ms`, equals `0.38T`; this is slightly later than `0.375T`, so `U_B` is slightly less than `U_E`. At all times the total energy `U_B + U_E` has the same value, `1.1 J`. An L-C circuit without resistance is a conservative system; no energy is dissipated.

## Key concepts used
- Magnetic energy stored in an inductor: `U_B = 1/2 L i^2`
- Electric energy stored in a capacitor: `U_E = q^2 / (2C)`
- In an ideal L-C circuit, energy oscillates between magnetic and electric forms while the total energy remains constant
