---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.6
example_number: 24.12
subtitle: A spherical capacitor with dielectric
needs_review: true
---

# Example 24.12: A spherical capacitor with dielectric

## Problem
Use Gauss’s law to find the capacitance of the spherical capacitor of Example 24.3 (Section 24.1) if the volume between the shells is filled with an insulating oil with dielectric constant \(K\).

## Setup
**Identify and Set Up:** The spherical symmetry of the problem is not changed by the presence of the dielectric, so as in Example 24.3, use a concentric spherical Gaussian surface of radius \(r\) between the shells. Since a dielectric is present, use Gauss’s law in the form of Eq. (24.23).

## Solution
**Execute:** From Eq. (24.23),
\[
\mathbf{E}=\frac{Q}{4\pi K \varepsilon_0 r^2}=\frac{Q}{4\pi \varepsilon r^2},
\]
where \(\varepsilon = K\varepsilon_0\).

Compared to the case in which there is vacuum between the shells, the electric field is reduced by a factor of \(K\). The potential difference \(V_{ab}\) between the shells is reduced by the same factor, and so the capacitance \(C=Q/V_{ab}\) is increased by a factor of \(K\), just as for a parallel-plate capacitor when a dielectric is inserted. Using the result of Example 24.3, we find that the capacitance with the dielectric is
\[
C = 4\pi K\varepsilon_0 \frac{r_a r_b}{r_b-r_a}
= 4\pi \varepsilon \frac{r_a r_b}{r_b-r_a}.
\]

## Evaluation
If the dielectric fills the volume between the two conductors, the capacitance is just \(K\) times the value with no dielectric. The result is more complicated if the dielectric only partially fills this volume (see Challenge Problem 24.78).

## Key concepts used
- Gauss’s law in a dielectric: \(\displaystyle \oint \mathbf{E}\cdot d\mathbf{A} = \frac{Q}{\varepsilon}\)
- Spherical symmetry and Gaussian surfaces
- Relation between electric field and potential difference
- Capacitance definition: \(\displaystyle C=\frac{Q}{V_{ab}}\)
- Dielectric constant \(K\) with \(\varepsilon = K\varepsilon_0\)
