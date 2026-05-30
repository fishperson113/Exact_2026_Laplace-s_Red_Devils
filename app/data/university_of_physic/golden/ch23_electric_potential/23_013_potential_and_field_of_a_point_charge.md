---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.5
example_number: 23.13
subtitle: Potential and field of a point charge
needs_review: true
---

# Example 23.13: Potential and field of a point charge

## Problem
From Eq. (23.14), the potential at a radial distance \(r\) from a point charge \(q\) is
\[
V=\frac{q}{4\pi\varepsilon_0 r}.
\]
Find the vector electric field from this expression for \(V\).

## Setup
**IDENTIFY and SET UP:** This problem uses the general relationship between the electric potential as a function of position and the electric-field vector. By symmetry, the electric field here has only a radial component \(E_r\). We use Eq. (23.23) to find this component.

## Solution
**EXECUTE:** From Eq. (23.23),
\[
E_r=-\frac{dV}{dr}
=-\frac{d}{dr}\left(\frac{1}{4\pi\varepsilon_0}\frac{q}{r}\right)
=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}.
\]
So the vector electric field is
\[
\vec E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r.
\]

An alternative approach is to ignore the radial symmetry, write the radial distance as
\[
r=\sqrt{x^2+y^2+z^2},
\]
and take the derivatives of
\[
V=\frac{q}{4\pi\varepsilon_0 r}
\]
with respect to \(x\), \(y\), and \(z\), as in Eq. (23.20). We find
\[
\frac{\partial V}{\partial x}
=-\frac{1}{4\pi\varepsilon_0}\frac{qx}{(x^2+y^2+z^2)^{3/2}},
\]
\[
\frac{\partial V}{\partial y}
=-\frac{qy}{4\pi\varepsilon_0 r^3},
\qquad
\frac{\partial V}{\partial z}
=-\frac{qz}{4\pi\varepsilon_0 r^3}.
\]
Then from Eq. (23.20),
\[
\vec E
= -\left(\hat i\,\frac{\partial V}{\partial x}
+\hat j\,\frac{\partial V}{\partial y}
+\hat k\,\frac{\partial V}{\partial z}\right)
=
\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r
=
\hat i\left(\frac{qx}{4\pi\varepsilon_0 r^3}\right)
+\hat j\left(\frac{qy}{4\pi\varepsilon_0 r^3}\right)
+\hat k\left(\frac{qz}{4\pi\varepsilon_0 r^3}\right).
\]

## Evaluation
Our result agrees with Eq. (21.7), as it must.

This approach gives us the same answer, but with more effort. Clearly it’s best to exploit the symmetry of the charge distribution whenever possible.

## Key concepts used
- Relation between electric field and electric potential:
  \[
  \vec E = -\nabla V
  \]
- For spherical symmetry:
  \[
  E_r = -\frac{dV}{dr}
  \]
- Potential of a point charge:
  \[
  V=\frac{q}{4\pi\varepsilon_0 r}
  \]
- The field of a point charge is radial:
  \[
  \vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r
  \]
