---
source: Fundamentals of Physics
chapter: 32
section: 32-3
sample_problem_number: 32.02
subtitle: Treating a changing electric field as a displacement current
needs_review: true
---

# Sample Problem 32.02: Treating a changing electric field as a displacement current

## Problem
A circular parallel-plate capacitor with plate radius \(R\) is being charged with a current \(i\).

(a) Between the plates, what is the magnitude of \(\oint \mathbf{B}\cdot d\mathbf{s}\), in terms of \(\mu_0\) and \(i\), at a radius \(r = R/5\) from their center?

(b) In terms of the maximum induced magnetic field, what is the magnitude of the magnetic field induced at \(r = R/5\), inside the capacitor?

## Key ideas
Because the capacitor has parallel circular plates, we can treat the space between the plates as an imaginary wire of radius \(R\) carrying the imaginary current \(i_d\). Then we can use the Ampere-Maxwell law to find the induced magnetic field magnitude \(B\) at any point inside the capacitor.

## Solution
### (a)
Between the plates, there is no real current, so the Ampere-Maxwell law reduces to

\[
\oint \mathbf{B}\cdot d\mathbf{s}=\mu_0 i_{d,\mathrm{enc}}.
\]

To evaluate this at radius \(r=R/5\) within the capacitor, the integration loop encircles only a portion \(i_{d,\mathrm{enc}}\) of the total displacement current \(i_d\).

Assume the displacement current is uniformly spread over the full plate area. Then the portion encircled by the loop is proportional to the area encircled by the loop:

\[
\frac{i_{d,\mathrm{enc}}}{i_d}=\frac{\pi r^2}{\pi R^2}.
\]

Thus,

\[
i_{d,\mathrm{enc}}=i_d\frac{\pi r^2}{\pi R^2}.
\]

Substituting this into the reduced Ampere-Maxwell law gives

\[
\oint \mathbf{B}\cdot d\mathbf{s}=\mu_0 i_d\frac{\pi r^2}{\pi R^2}.
\]

Now substitute \(i_d=i\) and \(r=R/5\):

\[
\oint \mathbf{B}\cdot d\mathbf{s}
=\mu_0 i \frac{(R/5)^2}{R^2}
=\mu_0 i \frac{1}{25}.
\]

### (b)
Because the capacitor has parallel circular plates, we can treat the space between the plates as an imaginary wire of radius \(R\) carrying the imaginary current \(i_d\). Then, from Eq. 32-16, the induced magnetic field inside the capacitor is

\[
B=\frac{\mu_0 i_d}{2\pi R^2}r.
\]

At \(r=R/5\),

\[
B=\frac{\mu_0 i_d}{2\pi R^2}\left(\frac{R}{5}\right)
=\frac{\mu_0 i_d}{10\pi R}.
\]

The maximum field within the capacitor occurs at \(r=R\), so

\[
B_{\max}=\frac{\mu_0 i_d}{2\pi R^2}R
=\frac{\mu_0 i_d}{2\pi R}.
\]

Dividing the field at \(r=R/5\) by \(B_{\max}\),

\[
\frac{B}{B_{\max}}=\frac{1}{5}.
\]

So the field at \(r=R/5\) is one-fifth of the maximum field.

## Answer
(a)
\[
\oint \mathbf{B}\cdot d\mathbf{s}=\frac{\mu_0 i}{25}.
\]

(b)
\[
B=\frac{1}{5}B_{\max}.
\]

## Key concepts used
- Ampere-Maxwell law
- Displacement current
- Symmetry of a circular parallel-plate capacitor
- Magnetic field inside the capacitor varies linearly with radius
