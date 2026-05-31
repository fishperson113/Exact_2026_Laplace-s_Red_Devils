---
source: Fundamentals of Physics
chapter: 26
section: 26-3
sample_problem_number: 26.03
subtitle: In a current, the conduction electrons move very slowly
needs_review: true
---

# Sample Problem 26.03: In a current, the conduction electrons move very slowly

## Problem
What is the drift speed of the conduction electrons in a copper wire with radius \(r = 900\ \text{mm}\) when it has a uniform current \(i = 17\ \text{mA}\)? Assume that each copper atom contributes one conduction electron to the current and that the current density is uniform across the wire’s cross section.

## Key ideas
1. The drift speed \(v_d\) is related to the current density and the number \(n\) of conduction electrons per unit volume according to Eq. 26-7, which we can write as
   \[
   J = ne v_d.
   \]
2. Because the current density is uniform, its magnitude \(J\) is related to the given current \(i\) and wire size by Eq. 26-5:
   \[
   J = \frac{i}{A},
   \]
   where \(A\) is the cross-sectional area of the wire.
3. Because we assume one conduction electron per atom, the number \(n\) of conduction electrons per unit volume is the same as the number of atoms per unit volume.

## Solution
Calculations: Let us start with the third idea by writing

\[
n = \left(\frac{\text{atoms}}{\text{unit volume}}\right)
= \left(\frac{\text{atoms}}{\text{per mole}}\right)
\left(\frac{\text{moles}}{\text{per unit mass}}\right)
\left(\frac{\text{mass}}{\text{per unit volume}}\right).
\]

The number of atoms per mole is just Avogadro’s number \(N_A\) \((= 6.02 \times 10^{23}\ \text{mol}^{-1})\). Moles per unit mass is the inverse of the mass per mole, which here is the molar mass \(M\) of copper. The mass per unit volume is the (mass) density \(\rho_{\text{mass}}\) of copper. Thus,

\[
n = N_A \left(\frac{1}{M}\right)\rho_{\text{mass}}
= \frac{N_A \rho_{\text{mass}}}{M}.
\]

From the relation

\[
J = ne v_d,
\]

and using \(J = i/A\), we have

\[
v_d = \frac{J}{ne} = \frac{i}{Ane}.
\]

With the wire radius \(r = 900\ \text{mm}\), the cross-sectional area is

\[
A = \pi r^2.
\]

Using the given current \(i = 17\ \text{mA}\) and the values for copper, substitution into the above expressions gives the drift speed.

## Answer
The drift speed of the conduction electrons is

\[
v_d \approx 4 \times 10^{-6}\ \text{m/s}.
\]

## Key concepts used
- Drift speed
- Current density \(J\)
- Conduction electron density \(n\)
- Cross-sectional area \(A\)
- Relation \(J = ne v_d\)
- Relation \(J = i/A\)
