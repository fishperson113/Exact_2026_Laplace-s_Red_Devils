---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.1
example_number: 24.4
subtitle: A cylindrical capacitor
needs_review: true
---

# Example 24.4: A cylindrical capacitor

## Problem
Two long, coaxial cylindrical conductors are separated by vacuum. The inner cylinder has radius \(r_a\) and linear charge density \(+\lambda\). The outer cylinder has inner radius \(r_b\) and linear charge density \(-\lambda\). Find the capacitance per unit length for this capacitor.

## Setup
**IDENTIFY and SET UP:** As in Example 24.3, use the definition of capacitance,
\[
C=\frac{Q}{V_{ab}}.
\]
Use the result of Example 23.10 (Section 23.3) to find the potential difference between the cylinders, and find the charge \(Q\) on a length \(L\) of the cylinders from the linear charge density. Then find the corresponding capacitance \(C\) using Eq. (24.1). The target variable is the capacitance divided by \(L\).

## Solution
**EXECUTE:** As in Example 24.3, the potential \(V\) between the cylinders is not affected by the presence of the charged outer cylinder. Hence the result from Example 23.10 for the potential outside a charged conducting cylinder also holds here for the potential in the space between the cylinders:
\[
V(r)=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_0}{r}\right).
\]
Here \(r_0\) is the arbitrary finite radius at which \(V=0\). We take \(r_0=r_b\), the radius of the inner surface of the outer cylinder. Then the potential at the outer surface of the inner cylinder, \(r=r_a\), is just the potential difference \(V_{ab}\) of the inner (positive) cylinder with respect to the outer (negative) cylinder:
\[
V_{ab}=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_b}{r_a}\right).
\]
If \(\lambda\) is positive, then \(V_{ab}\) is positive as well: the inner cylinder is at higher potential than the outer.

The total charge in a length \(L\) is
\[
Q=\lambda L,
\]
so from Eq. (24.1) the capacitance of a length \(L\) is
\[
C=\frac{Q}{V_{ab}}
=\frac{\lambda L}{\dfrac{\lambda}{2\pi\varepsilon_0}\ln(r_b/r_a)}
=\frac{2\pi\varepsilon_0 L}{\ln(r_b/r_a)}.
\]
The capacitance per unit length is
\[
\frac{C}{L}=\frac{2\pi\varepsilon_0}{\ln(r_b/r_a)}.
\]

## Evaluation
The capacitance of coaxial cylinders is determined entirely by their dimensions, just as for parallel-plate and spherical capacitors. Ordinary coaxial cables are made like this but with an insulating material instead of vacuum between the conductors. A typical cable used for connecting a television to a cable TV feed has a capacitance per unit length of \(69\ \text{pF/m}\).

Using \(\varepsilon_0 = 8.85\times 10^{-12}\ \text{F/m} = 8.85\ \text{pF/m}\), the result is
\[
\frac{C}{L}=55.6\ \text{pF/m}.
\]

## Key concepts used
- Definition of capacitance: \(C=Q/V\)
- Potential difference for coaxial cylinders from Gauss’s law result
- Linear charge density: \(Q=\lambda L\)
- Capacitance per unit length for a cylindrical capacitor:
  \[
  \frac{C}{L}=\frac{2\pi\varepsilon_0}{\ln(r_b/r_a)}
  \]
