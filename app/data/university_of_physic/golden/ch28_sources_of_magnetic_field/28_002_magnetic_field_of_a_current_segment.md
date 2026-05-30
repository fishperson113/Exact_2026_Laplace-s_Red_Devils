---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.3
example_number: 28.2
subtitle: Magnetic field of a current segment
needs_review: true
---

# Example 28.2: Magnetic field of a current segment

## Problem
A copper wire carries a steady 125-A current to an electroplating tank. Find the magnetic field due to a 1.0-cm segment of this wire at a point 1.2 m away from it, if the point is:

(a) point straight out to the side of the segment, and

(b) point in the xy-plane and on a line at 30° to the segment.

## Setup
IDENTIFY and SET UP: Although Eqs. (28.5) and (28.6) apply only to infinitesimal current elements, we may use either of them here because the segment length is much less than the distance to the field point.

The current element points in the negative x-direction (the direction of the current), so \(d\vec{\ell} = -\,dl\,\hat{\mathbf{i}}\).

The unit vector \(\hat{\mathbf{r}}_n\) for each field point is directed from the current element toward that point:

- for point \(P_1\), \(\hat{\mathbf{r}}_n\) is in the \(+\!y\)-direction;
- for point \(P_2\), \(\hat{\mathbf{r}}_n\) is at an angle of 30° above the \(+\!x\)-direction.

## Solution
EXECUTE:

(a) At point \(P_1\), \(\hat{\mathbf{r}}_n = \hat{\mathbf{j}}\), so

\[
\vec{B}
= \frac{\mu_0}{4\pi}\frac{I\,d\vec{\ell}\times \hat{\mathbf{r}}_n}{r^2}
= \frac{\mu_0}{4\pi}\frac{(125\ \text{A})(1.0\times 10^{-2}\ \text{m})(-\hat{\mathbf{i}})\times \hat{\mathbf{j}}}{(1.2\ \text{m})^2}
\]

\[
= -\frac{\mu_0}{4\pi}\frac{I\,dl}{r^2}\hat{\mathbf{k}}
= -8.7\times 10^{-8}\ \text{T}\,\hat{\mathbf{k}}
\]

The direction of \(\vec{B}\) at \(P_1\) is into the xy-plane of Fig. 28.4.

(b) At \(P_2\), the unit vector is

\[
\hat{\mathbf{r}}_n = \cos 30^\circ\,\hat{\mathbf{i}} + \sin 30^\circ\,\hat{\mathbf{j}}
\]

From Eq. (28.6),

\[
\vec{B}
= \frac{\mu_0}{4\pi}\frac{I\,d\vec{\ell}\times \hat{\mathbf{r}}_n}{r^2}
= \frac{\mu_0}{4\pi}\frac{I\,dl(-\hat{\mathbf{i}})\times \left(\cos 30^\circ\,\hat{\mathbf{i}} + \sin 30^\circ\,\hat{\mathbf{j}}\right)}{r^2}
\]

\[
= -\frac{\mu_0}{4\pi}\frac{I\,dl\,\sin 30^\circ}{r^2}\hat{\mathbf{k}}
\]

\[
= -\left(10^{-7}\ \text{T}\cdot\text{m}/\text{A}\right)
\frac{(125\ \text{A})(1.0\times 10^{-2}\ \text{m})\sin 30^\circ}{(1.2\ \text{m})^2}\hat{\mathbf{k}}
\]

\[
= -4.3\times 10^{-8}\ \text{T}\,\hat{\mathbf{k}}
\]

The direction of \(\vec{B}\) at \(P_2\) is also into the xy-plane of Fig. 28.4.

## Evaluation
We can check our results for the direction of \(\vec{B}\) by comparing them with Fig. 28.3. The xy-plane in Fig. 28.4 corresponds to the beige plane in Fig. 28.3, but here the direction of the current and hence of \(d\vec{\ell}\) is the reverse of that shown in Fig. 28.3. Hence the direction of the magnetic field is reversed as well.

Hence the field at points in the xy-plane in Fig. 28.4 must point into, not out of, that plane. This is just what we concluded above.

## Key concepts used
- Biot–Savart law for a current element:
  \[
  d\vec{B}=\frac{\mu_0}{4\pi}\frac{I\,d\vec{\ell}\times \hat{\mathbf{r}}_n}{r^2}
  \]
- Right-hand rule for the direction of \(d\vec{B}\)
- Use of a finite short segment as an approximation to an infinitesimal current element when the segment length is much smaller than the distance to the field point
- Vector cross product and its dependence on the angle between \(d\vec{\ell}\) and \(\hat{\mathbf{r}}_n\)
