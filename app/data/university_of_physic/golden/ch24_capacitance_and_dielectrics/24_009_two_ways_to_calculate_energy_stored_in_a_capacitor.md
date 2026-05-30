---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.3
example_number: 24.9
subtitle: Two ways to calculate energy stored in a capacitor
needs_review: true
---

# Example 24.9: Two ways to calculate energy stored in a capacitor

## Problem
The spherical capacitor described in Example 24.3 (Section 24.1) has charges \(+Q\) and \(-Q\) on its inner and outer conductors. Find the electric potential energy stored in the capacitor (a) by using the capacitance \(C\) found in Example 24.3 and (b) by integrating the electric-field energy density \(u\).

## Setup
IDENTIFY and SET UP: We can determine the energy \(U\) stored in a capacitor in two ways: in terms of the work done to put the charges on the two conductors, and in terms of the energy in the electric field between the conductors. The descriptions are equivalent, so they must give us the same result. In Example 24.3 we found the capacitance \(C\) and the field magnitude \(E\) in the space between the conductors. (The electric field is zero inside the inner sphere and is also zero outside the outer surface of the outer sphere, because a Gaussian surface with radius \(r < r_a\) or \(r > r_b\) encloses zero net charge. Hence the energy density is nonzero only in the space between the spheres, \(r_a < r < r_b\).) In part (a) we use Eq. (24.9) to find \(U\). In part (b) we use Eq. (24.11) to find \(u\), which we integrate over the volume between the spheres to find \(U\).

## Solution
EXECUTE: (a) From Example 24.3, the spherical capacitor has capacitance
\[
C = 4\pi P_0 \frac{r_a r_b}{r_b - r_a}
\]
where \(r_a\) and \(r_b\) are the radii of the inner and outer conducting spheres, respectively. From Eq. (24.9) the energy stored in this capacitor is
\[
U = \frac{Q^2}{2C}
= \frac{Q^2}{8\pi P_0}\frac{r_b - r_a}{r_a r_b}.
\]

(b) The electric field in the region \(r_a < r < r_b\) between the two conducting spheres has magnitude
\[
E = \frac{Q}{4\pi P_0 r^2}.
\]
The energy density in this region is
\[
u = \frac{1}{2}P_0E^2
= \frac{1}{2}P_0\left(\frac{Q}{4\pi P_0 r^2}\right)^2
= \frac{Q^2}{32\pi^2 P_0 r^4}.
\]
The energy density is not uniform; it decreases rapidly with increasing distance from the center of the capacitor. To find the total electric-field energy, we integrate \(u\) (the energy per unit volume) over the region \(r_a < r < r_b\). We divide this region into spherical shells of radius \(r\), surface area \(4\pi r^2\), thickness \(dr\), and volume
\[
dV = 4\pi r^2\,dr.
\]
Then
\[
U = \int u\,dV
= \int_{r_a}^{r_b}\left(\frac{Q^2}{32\pi^2 P_0 r^4}\right)(4\pi r^2\,dr)
= \frac{Q^2}{8\pi P_0}\int_{r_a}^{r_b}\frac{dr}{r^2}
= \frac{Q^2}{8\pi P_0}\left(-\frac{1}{r_b}+\frac{1}{r_a}\right)
= \frac{Q^2}{8\pi P_0}\frac{r_b-r_a}{r_a r_b}.
\]

## Evaluation
Electric potential energy can be regarded as being associated with either the charges, as in part (a), or the field, as in part (b); the calculated amount of stored energy is the same in either case.

## Key concepts used
- Capacitance of a spherical capacitor
- Energy stored in a capacitor: \(U = \dfrac{Q^2}{2C}\)
- Electric field of a spherical capacitor
- Electric energy density: \(u = \dfrac{1}{2}P_0E^2\)
- Volume element for spherical shells: \(dV = 4\pi r^2\,dr\)
