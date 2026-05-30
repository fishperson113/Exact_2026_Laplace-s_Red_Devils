---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.3
example_number: 23.12
subtitle: Potential of a line of charge
needs_review: true
---

# Example 23.12: Potential of a line of charge

## Problem
Positive electric charge is distributed uniformly along a line of length \(2a\) lying along the \(y\)-axis between \(y=-a\) and \(y=+a\) (Fig. 23.21). Find the electric potential at a point \(P\) on the \(x\)-axis at a distance \(x\) from the origin.

## Setup
**IDENTIFY and SET UP:** This is the same situation as in Example 21.10 (Section 21.5), where we found an expression for the electric field at an arbitrary point on the \(x\)-axis. We can find \(V\) at point \(P\) by integrating over the charge distribution using Eq. (23.16). Unlike the situation in Example 23.11, each charge element \(dQ\) is a different distance from point \(P\), so the integration will take a little more effort.

For a rod of total charge \(Q\) and length \(2a\), the charge element corresponding to an element of length \(dy\) is
\[
dQ=\frac{Q}{2a}\,dy.
\]

The distance from \(dQ\) at coordinate \(y\) to point \(P\) on the \(x\)-axis is
\[
\sqrt{x^2+y^2}.
\]

The contribution that this charge element makes to the potential at \(P\) is
\[
dV=\frac{1}{4\pi\varepsilon_0}\frac{dQ}{\sqrt{x^2+y^2}}.
\]

To find the potential at \(P\) due to the entire rod, we integrate over the length of the rod from \(y=-a\) to \(y=+a\).

## Solution
\[
V=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\int_{-a}^{a}\frac{dy}{\sqrt{x^2+y^2}}.
\]

You can look up the integral in a table. The final result is
\[
V=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\ln\!\left(
\frac{a+\sqrt{a^2+x^2}}{-a+\sqrt{a^2+x^2}}
\right).
\]

## Evaluation
We can check our result by letting \(x\) approach infinity. In this limit the point \(P\) is infinitely far from all of the charge, so we expect \(V\) to approach zero; you can verify that it does.

We know the electric field at all points along the \(x\)-axis from Example 21.10. We invite you to use this information to find \(V\) along this axis by integrating \(E_x\) as in Eq. (23.17).

## Key concepts used
- Electric potential of a continuous charge distribution is found by integration.
- For a charge element \(dQ\), \(dV=\dfrac{1}{4\pi\varepsilon_0}\dfrac{dQ}{r}\).
- Uniform linear charge density on a rod of length \(2a\): \(dQ=\dfrac{Q}{2a}\,dy\).
- Distance from a point on the \(x\)-axis to an element on the \(y\)-axis: \(r=\sqrt{x^2+y^2}\).
- The potential is a scalar, so contributions add directly.
