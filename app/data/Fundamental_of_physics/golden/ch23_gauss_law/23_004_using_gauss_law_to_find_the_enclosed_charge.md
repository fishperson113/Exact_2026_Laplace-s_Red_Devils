---
source: Fundamentals of Physics
chapter: 23
section: 23-2
sample_problem_number: 23.04
subtitle: Using Gauss’ law to find the enclosed charge
needs_review: true
---

# Sample Problem 23.04: Using Gauss’ law to find the enclosed charge

## Problem
What is the net charge enclosed by the Gaussian cube of Sample Problem 23.02?

## Key ideas
The net charge enclosed by a (real or mathematical) closed surface is related to the total electric flux through the surface by Gauss’ law:
\[
\Phi = \frac{q_{\text{enc}}}{\varepsilon_0}.
\]

To use Gauss’ law, we need to know the flux through all six faces of the cube. We already know the flux through the right face \(\Phi_r = 36\ \text{N·m}^2/\text{C}\), the left face \(\Phi_l = -12\ \text{N·m}^2/\text{C}\), and the top face \(\Phi_t = 16\ \text{N·m}^2/\text{C}\).

For the bottom face, the calculation is like that for the top face except that the area vector is directed downward along the \(y\) axis, because it must point outward from the Gaussian enclosure.

## Solution
Using Gauss’ law,
\[
\Phi = \frac{q_{\text{enc}}}{\varepsilon_0},
\]
so
\[
q_{\text{enc}} = \varepsilon_0 \Phi.
\]

Adding the fluxes through all six faces of the cube gives the total flux. From the sample’s face-by-face results, the net flux leads to
\[
q_{\text{enc}} = -1.10 \times 10^{-6}\ \text{C}.
\]

The text notes that the calculation would have been different if \(P_1\) or \(P_2\) had been placed on the surface of a Gaussian cube instead of using a Gaussian sphere to mimic spherical symmetry. In that case, both the angle \(\theta\) and the magnitude \(E\) would vary considerably over the surface of the cube, making the Gauss’ law integral difficult to evaluate.

## Answer
\[
q_{\text{enc}} = -1.10 \times 10^{-6}\ \text{C}
\]

## Key concepts used
- Gauss’ law relates total electric flux through a closed surface to enclosed charge.
- Electric flux must be summed over all faces of the Gaussian surface.
- The area vector for each face points outward from the closed surface.
- Symmetry can simplify Gauss’ law calculations; without it, the flux integral may be difficult.
