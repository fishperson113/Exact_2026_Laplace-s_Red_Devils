---
source: Fundamentals of Physics
chapter: 23
section: 23-2
sample_problem_number: 23.03
subtitle: Using Gauss’ law to find the electric field
needs_review: true
---

# Sample Problem 23.03: Using Gauss’ law to find the electric field

## Problem
Figure 23-10a shows, in cross section, a plastic, spherical shell with uniform charge \(Q = -16e\) and radius \(R = 10\text{ cm}\). A particle with charge \(q = +5e\) is at the center. What is the electric field (magnitude and direction) at (a) point \(P_1\) at radial distance \(r_1 = 6.00\text{ cm}\) and (b) point \(P_2\) at radial distance \(r_2 = 12.0\text{ cm}\)?

## Key ideas
1. Because the situation in Fig. 23-10a has spherical symmetry, we can apply Gauss’ law (Eq. 23-7) to find the electric field at a point if we use a Gaussian surface in the form of a sphere concentric with the particle and shell.  
2. To find the electric field at a point, we put that point on a Gaussian surface so that \(\vec E\) is parallel to \(d\vec A\) in the dot product inside the integral in Gauss’ law.  
3. Gauss’ law relates the net electric flux through a closed surface to the net enclosed charge. Any external charge is not included.

## Solution
For a charged particle, the field has spherical symmetry: the field depends on the distance \(r\) from the particle but not on direction. So we enclose the particle in a Gaussian sphere centered on the particle.

At each point on the spherical surface, the electric field \(\vec E\) has the same magnitude \(E\) and points radially outward for positive enclosed charge, or inward for negative enclosed charge. The area vector \(d\vec A\) is outward.

Gauss’ law is

\[
\varepsilon_0 \oint \vec E \cdot d\vec A = q_{\text{enc}}.
\]

Because \(\vec E\) is everywhere parallel to \(d\vec A\) for a spherically symmetric Gaussian surface around a central charge, the dot product becomes

\[
\vec E \cdot d\vec A = E\, dA.
\]

Thus,

\[
\varepsilon_0 \oint E\, dA = q_{\text{enc}}.
\]

Since \(E\) is constant on the Gaussian sphere, it can be taken outside the integral:

\[
\varepsilon_0 E \oint dA = q_{\text{enc}}.
\]

The remaining integral is the surface area of a sphere:

\[
\oint dA = 4\pi r^2.
\]

So Gauss’ law gives

\[
\varepsilon_0 E(4\pi r^2)=q_{\text{enc}},
\]

or

\[
E=\frac{1}{4\pi\varepsilon_0}\frac{q_{\text{enc}}}{r^2}.
\]

### (a) Field at \(P_1\), \(r_1 = 6.00\text{ cm}\)
The Gaussian sphere through \(P_1\) encloses only the central particle, so

\[
q_{\text{enc}} = q = +5e.
\]

Thus,

\[
E=\frac{q_{\text{enc}}}{4\pi\varepsilon_0 r_1^2}
= \frac{5(1.60\times10^{-19}\text{ C})}
{4\pi(8.85\times10^{-12}\text{ C}^2/\text{N}\cdot\text{m}^2)(0.0600\text{ m})^2}.
\]

This gives

\[
E = 2.00\times10^6\text{ N/C}.
\]

Because the enclosed charge is positive, the field points radially outward.

### (b) Field at \(P_2\), \(r_2 = 12.0\text{ cm}\)
Now the Gaussian sphere through \(P_2\) encloses both the particle and the spherical shell. Thus,

\[
q_{\text{enc}} = q+Q = 5e + (-16e) = -11e.
\]

Since the net enclosed charge is negative, the field points radially inward.

Its magnitude is

\[
E=\frac{|q_{\text{enc}}|}{4\pi\varepsilon_0 r_2^2}
=\frac{11(1.60\times10^{-19}\text{ C})}
{4\pi(8.85\times10^{-12}\text{ C}^2/\text{N}\cdot\text{m}^2)(0.120\text{ m})^2}.
\]

This gives

\[
E = 6.87\times10^5\text{ N/C}.
\]

## Answer
(a) At \(P_1\), the electric field is

\[
\boxed{2.00\times10^6\ \text{N/C}}
\]

radially outward.

(b) At \(P_2\), the electric field is

\[
\boxed{6.87\times10^5\ \text{N/C}}
\]

radially inward.

## Key concepts used
- Gauss’ law
- Spherical symmetry
- Gaussian surface
- Electric flux
- Enclosed charge
- Radial electric field of a spherically symmetric charge distribution
