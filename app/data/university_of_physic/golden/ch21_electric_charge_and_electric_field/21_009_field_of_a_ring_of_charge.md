---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.5
example_number: 21.9
subtitle: Field of a ring of charge
needs_review: true
---

# Example 21.9: Field of a ring of charge

## Problem
Charge is uniformly distributed around a conducting ring of radius \(a\) (Fig. 21.23). Find the electric field at a point \(P\) on the ring axis at a distance \(x\) from its center.

## Setup
This is a problem in the superposition of electric fields. Each bit of charge around the ring produces an electric field at an arbitrary point on the \(x\)-axis; our target variable is the total field at this point due to all such bits of charge.

We divide the ring into infinitesimal segments \(ds\). In terms of the linear charge density \(\lambda\), the charge in a segment of length \(ds\) is

\[
dQ = \lambda\, ds.
\]

Consider two identical segments, one as shown in the figure at \(y=a\) and another halfway around the ring at \(y=-a\). From Example 21.4, the net force \(d\vec F\) they exert on a point test charge at \(P\), and thus their net field \(d\vec E\), are directed along the \(x\)-axis. The same is true for any such pair of segments around the ring, so the net field at \(P\) is along the \(x\)-axis:

\[
\vec E = E_x \,\hat{\mathbf i}.
\]

To calculate \(dE\), note that the square of the distance from a single ring segment to the point \(P\) is

\[
r^2 = x^2 + a^2.
\]

Hence the magnitude of this segment’s contribution to the electric field at \(P\) is

\[
dE = \frac{1}{4\pi\varepsilon_0}\frac{dQ}{x^2+a^2}.
\]

The \(x\)-component of this field is

\[
dE_x = dE \cos\alpha.
\]

We know \(dQ=\lambda\,ds\) and

\[
\cos\alpha = \frac{x}{r} = \frac{x}{(x^2+a^2)^{1/2}},
\]

so

\[
dE_x = \frac{1}{4\pi\varepsilon_0}\frac{\lambda x}{(x^2+a^2)^{3/2}}\, ds.
\]

## Solution
To find \(E_x\), we integrate this expression over the entire ring—that is, for \(s\) from \(0\) to \(2\pi a\) (the circumference of the ring). The integrand has the same value for all points on the ring, so it can be taken outside the integral. Hence we get

\[
E_x = \int dE_x
= \frac{1}{4\pi\varepsilon_0}\frac{\lambda x}{(x^2+a^2)^{3/2}} \int_0^{2\pi a} ds
= \frac{1}{4\pi\varepsilon_0}\frac{\lambda x}{(x^2+a^2)^{3/2}} (2\pi a).
\]

Using \(Q = \lambda(2\pi a)\), this becomes

\[
\vec E = E_x \,\hat{\mathbf i}
= \frac{1}{4\pi\varepsilon_0}\frac{Qx}{(x^2+a^2)^{3/2}}\,\hat{\mathbf i}.
\]

## Evaluation
Equation (21.8) shows that \(\vec E = 0\) at the center of the ring, \(x=0\). This makes sense; charges on opposite sides of the ring push in opposite directions on a test charge at the center, and the vector sum of each such pair of forces is zero.

When the field point \(P\) is much farther from the ring than the ring’s radius, we have \(x \gg a\), and the denominator in Eq. (21.8) becomes approximately equal to \(x^3\). In this limit the electric field at \(P\) is

\[
\vec E \approx \frac{1}{4\pi\varepsilon_0}\frac{Q}{x^2}\,\hat{\mathbf i}.
\]

That is, when the ring is so far away that its radius is negligible in comparison to the distance \(x\), its field is the same as that of a point charge.

## Key concepts used
- Superposition of electric fields
- Symmetry arguments for cancelling transverse components
- Linear charge density: \(dQ=\lambda\,ds\)
- Field of a point charge: \(dE=\dfrac{1}{4\pi\varepsilon_0}\dfrac{dQ}{r^2}\)
- Projection onto the axis: \(dE_x=dE\cos\alpha\)
- Integration around the full ring circumference
