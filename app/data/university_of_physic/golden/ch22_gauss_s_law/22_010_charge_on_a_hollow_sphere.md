---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.5
example_number: 22.10
subtitle: Charge on a hollow sphere
needs_review: true
---

# Example 22.10: Charge on a hollow sphere

## Problem
A thin-walled, hollow sphere of radius 0.250 m has an unknown charge distributed uniformly over its surface. At a distance of 0.300 m from the center of the sphere, the electric field points radially inward and has magnitude \(1.80 \times 10^2\ \text{N/C}\). How much charge is on the sphere?

## Setup
IDENTIFY and SET UP: The charge distribution is spherically symmetric. As in Examples 22.5 and 22.9, it follows that the electric field is radial everywhere and its magnitude is a function only of the radial distance from the center of the sphere. We use a spherical Gaussian surface that is concentric with the charge distribution and has radius \(r = 0.300\ \text{m}\). Our target variable is \(q\).

## Solution
EXECUTE: The charge distribution is the same as if the charge were on the surface of a 0.250-m-radius conducting sphere. Hence we can borrow the results of Example 22.5. We note that the electric field here is directed toward the sphere, so that \(q\) must be negative. Furthermore, the electric field is directed into the Gaussian surface, so that
\[
\vec E \cdot d\vec A = -E\,dA
\]
and
\[
\oint \vec E \cdot d\vec A = -E(4\pi r^2).
\]

By Gauss’s law, the flux is equal to the charge \(q\) on the sphere (all of which is enclosed by the Gaussian surface) divided by \(\varepsilon_0\):
\[
\oint \vec E \cdot d\vec A = \frac{q}{\varepsilon_0}.
\]

Solving for \(q\), we find
\[
q = -E(4\pi \varepsilon_0 r^2).
\]

Substituting the given values,
\[
q = -(1.80 \times 10^2\ \text{N/C})\left(4\pi (8.854 \times 10^{-12}\ \text{C}^2/\text{N}\cdot\text{m}^2)(0.300\ \text{m})^2\right).
\]

Thus,
\[
q = -1.80 \times 10^{-9}\ \text{C} = -1.80\ \text{nC}.
\]

## Evaluation
To determine the charge, we had to know the electric field at all points on the Gaussian surface so that we could calculate the flux integral. This was possible here because the charge distribution is highly symmetric. If the charge distribution is irregular or lacks symmetry, Gauss’s law is not very useful for calculating the charge distribution from the field, or vice versa.

## Key concepts used
- Spherical symmetry implies \(\vec E\) is radial and depends only on \(r\).
- For a spherical Gaussian surface, \(\oint \vec E \cdot d\vec A = E(4\pi r^2)\), with a negative sign here because the field points inward.
- Gauss’s law: \(\oint \vec E \cdot d\vec A = q_{\text{encl}}/\varepsilon_0\).
- The inward electric field direction implies the enclosed charge is negative.
