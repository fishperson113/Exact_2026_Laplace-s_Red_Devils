---
source: Fundamentals of Physics
chapter: 30
section: 30-3
sample_problem_number: 30.04
subtitle: Induced electric field due to changing B field, inside and outside
needs_review: true
---

# Sample Problem 30.04: Induced electric field due to changing B field, inside and outside

## Problem
In Fig. 30-11b, take \(R = 8.5\ \text{cm}\) and \(dB/dt = 0.13\ \text{T/s}\).

(a) Find an expression for the magnitude \(E\) of the induced electric field at points within the magnetic field, at radius \(r\) from the center of the magnetic field. Evaluate the expression for \(r = 5.2\ \text{cm}\).

## Key ideas
KEY IDEA

An electric field is induced by the changing magnetic field, according to Faraday’s law.

## Solution
To calculate the field magnitude \(E\), we apply Faraday’s law in the form of Eq. 30-20. We use a circular path of integration with radius \(r < R\) because we want \(E\) for points within the magnetic field.

We assume from the symmetry that \(\vec E\) in Fig. 30-11b is tangent to the circular path at all points. The path vector \(d\vec s\) is also always tangent to the circular path; so the dot product in Eq. 30-20 must have the magnitude \(E\,ds\) at all points on the path. We can also assume from symmetry that \(E\) has the same value at all points along the circular path. Then the left side of Eq. 30-20 becomes

\[
\oint \vec E \cdot d\vec s = E \oint ds = E(2\pi r).
\]

The integral \(\oint ds\) is the circumference \(2\pi r\) of the circular path.

Next, we need to evaluate the right side of Eq. 30-20. Because \(\vec B\) is uniform over the area \(A\) encircled by the path of integration and is directed perpendicular to that area, the magnetic flux is

\[
\Phi_B = BA = B(\pi r^2).
\]

Substituting this and the expression above into Faraday’s law and dropping the minus sign for the magnitude gives

\[
E(2\pi r) = \pi r^2 \frac{dB}{dt}.
\]

Solving for \(E\),

\[
E = \frac{r}{2}\,\frac{dB}{dt}.
\]

For \(r = 5.2\ \text{cm} = 5.2 \times 10^{-2}\ \text{m}\),

\[
E = \frac{(5.2 \times 10^{-2}\ \text{m})}{2}(0.13\ \text{T/s})
\]

\[
E = 3.38 \times 10^{-3}\ \text{V/m} \approx 3.4\ \text{mV/m}.
\]

## Answer
\[
E = \frac{r}{2}\,\frac{dB}{dt}
\]

For \(r = 5.2\ \text{cm}\),

\[
E \approx 3.4 \times 10^{-3}\ \text{V/m} = 3.4\ \text{mV/m}.
\]

## Key concepts used
- Faraday’s law of induction
- Symmetry of the induced electric field
- Magnetic flux through a circular area
- Circular path integration for \(\vec E\)
