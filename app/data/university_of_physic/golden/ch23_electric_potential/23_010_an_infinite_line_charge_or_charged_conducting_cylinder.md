---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.3
example_number: 23.10
subtitle: An infinite line charge or charged conducting cylinder
needs_review: true
---

# Example 23.10: An infinite line charge or charged conducting cylinder

## Problem
Find the potential at a distance from a very long line of charge with linear charge density \( \lambda \) (charge per unit length).

## Setup
**IDENTIFY and SET UP:** In both Example 21.10 (Section 21.5) and Example 22.6 (Section 22.4) we found that the electric field at a radial distance \( r \) from a long straight-line charge (Fig. 23.19a) has only a radial component given by

\[
E_r=\frac{\lambda}{2\pi \varepsilon_0 r}.
\]

We use this expression to find the potential by integrating as in Eq. (23.17).

## Solution
**EXECUTE:** Since the field has only a radial component, we have

\[
\mathbf{E}\cdot d\mathbf{l}=E_r\,dr.
\]

Hence from Eq. (23.17) the potential difference between any two points \( a \) and \( b \) at radial distances \( r_a \) and \( r_b \) from the line of charge is

\[
V_a-V_b=\int_b^a \mathbf{E}\cdot d\mathbf{l}
=\int_{r_b}^{r_a} E_r\,dr
=\frac{\lambda}{2\pi\varepsilon_0}\int_{r_b}^{r_a}\frac{dr}{r}
=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_a}{r_b}\right).
\]

If we take point \( b \) at infinity and set \( V_b=0 \), we find that \( V_a \) is infinite for any finite distance \( r_a \) from the line charge:

\[
V_a=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{\infty}{r_a}\right).
\]

This is not a useful way to define \( V \) for this problem. The difficulty is that the charge distribution itself extends to infinity.

Instead, as recommended in Problem-Solving Strategy 23.1, we set \( V=0 \) at point \( b \) at an arbitrary but finite radial distance \( r_0 \). Then the potential \( V \) at point \( a \) at a radial distance \( r \) is given by

\[
V-0=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_0}{r}\right),
\]

or

\[
V=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_0}{r}\right).
\]

## Evaluation
According to our result, if \( \lambda \) is positive, then \( V \) decreases as \( r \) increases. This is as it should be: \( V \) decreases as we move in the direction of \( \mathbf{E} \).

From Example 22.6, the expression for \( E_r \) with which we started also applies outside a long, charged conducting cylinder with charge per unit length \( \lambda \) (Fig. 23.19b). Hence our result also gives the potential for such a cylinder, but only for values of \( r \) equal to or greater than the radius \( R \) of the cylinder. If we choose \( r_0 \) to be the cylinder radius \( R \) so that \( V=0 \) when \( r=R \), then at any point for which \( r\ge R \),

\[
V=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{R}{r}\right).
\]

Inside the cylinder, \( \mathbf{E}=0 \), and \( V \) has the same value (zero) as on the cylinder’s surface.

## Key concepts used
- Potential difference from the electric field:
  \[
  V_a-V_b=\int_b^a \mathbf{E}\cdot d\mathbf{l}
  \]
- For a long line charge, the field is radial:
  \[
  E_r=\frac{\lambda}{2\pi\varepsilon_0 r}
  \]
- Integrating \( 1/r \) gives a logarithmic potential:
  \[
  V=\frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{r_0}{r}\right)
  \]
- For a conducting cylinder, \( \mathbf{E}=0 \) inside and the potential is constant there
