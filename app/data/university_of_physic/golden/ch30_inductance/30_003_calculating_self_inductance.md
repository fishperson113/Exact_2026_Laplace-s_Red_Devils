---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.2
example_number: 30.3
subtitle: Calculating self-inductance
needs_review: true
---

# Example 30.3: Calculating self-inductance

## Problem
Determine the self-inductance of a toroidal solenoid with cross-sectional area \(A\) and mean radius \(r\), closely wound with \(N\) turns of wire on a nonmagnetic core (Fig. 30.8). Assume that \(B\) is uniform across a cross section (that is, neglect the variation of \(B\) with distance from the toroid axis).

## Setup
**IDENTIFY** and **SET UP**: Our target variable is the self-inductance \(L\) of the toroidal solenoid. We can find \(L\) using Eq. (30.6), which requires knowing the flux \(\Phi_B\) through each turn and the current \(i\) in the solenoid:
\[
L=\frac{N\Phi_B}{i}.
\]

From Example 28.10, the field magnitude at a distance \(r\) from the toroid axis is
\[
B=\frac{\mu_0 N i}{2\pi r}.
\]

If we assume that the field has this magnitude over the entire cross-sectional area \(A\), then
\[
\Phi_B = BA.
\]

The flux \(\Phi_B\) is the same through each turn, and the self-inductance is
\[
L=\frac{N\Phi_B}{i}.
\]

## Solution
From Eq. (30.6), the self-inductance is
\[
L=\frac{N\Phi_B}{i}.
\]

Using the magnetic field of a toroid,
\[
B=\frac{\mu_0 N i}{2\pi r},
\]
and assuming the field is uniform over the cross-sectional area \(A\), the flux through one turn is
\[
\Phi_B=BA=\left(\frac{\mu_0 N i}{2\pi r}\right)A.
\]

Substituting into the expression for \(L\),
\[
L=\frac{N\Phi_B}{i}
=\frac{N}{i}\left(\frac{\mu_0 N iA}{2\pi r}\right)
=\frac{\mu_0 N^2 A}{2\pi r}.
\]

Thus,
\[
\boxed{L=\frac{\mu_0 N^2 A}{2\pi r}}
\]
(self-inductance of a toroidal solenoid)

## Evaluation
Suppose
\[
N=200,\qquad A=5.0\ \text{cm}^2=5.0\times10^{-4}\ \text{m}^2,\qquad r=0.10\ \text{m}.
\]

Then
\[
L=\frac{(4\pi\times10^{-7}\ \text{Wb/(A}\cdot\text{m)}) (200)^2 (5.0\times10^{-4}\ \text{m}^2)}{2\pi(0.10\ \text{m})}
=40\times10^{-6}\ \text{H}=40\ \text{mH}.
\]

## Key concepts used
- Self-inductance definition: \(L = N\Phi_B/i\)
- Magnetic field inside a toroidal solenoid: \(B=\mu_0 N i/(2\pi r)\)
- Magnetic flux through one turn: \(\Phi_B=BA\)
- Substitution and algebra to obtain \(L=\mu_0 N^2 A/(2\pi r)\)
