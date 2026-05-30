---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.4
example_number: 22.5
subtitle: Field of a charged conducting sphere
needs_review: true
---

# Example 22.5: Field of a charged conducting sphere

## Problem
We place a total positive charge \(q\) on a solid conducting sphere with radius \(R\) (Fig. 22.18). Find the electric field \(\mathbf{E}\) at any point inside or outside the sphere.

## Setup
**IDENTIFY and SET UP:** As discussed earlier in this section, all of the charge must be on the surface of the sphere. The charge is free to move on the conductor, and there is no preferred position on the surface; the charge is therefore distributed uniformly over the surface, and the system is spherically symmetric.

To exploit this symmetry, take as the Gaussian surface a sphere of radius \(r\) centered on the conductor. We can calculate the field inside or outside the conductor by taking \(r < R\) or \(r > R\), respectively. In either case, the point at which we want to calculate \(\mathbf{E}\) lies on the Gaussian surface.

## Solution
**EXECUTE:** The spherical symmetry means that the direction of the electric field must be radial; there is no preferred direction parallel to the surface, so \(\mathbf{E}\) can have no component parallel to the surface. There is also no preferred orientation of the sphere, so the field magnitude \(E\) can depend only on the distance \(r\) from the center and must have the same value at all points on the Gaussian surface.

For \(r > R\), the entire conductor is within the Gaussian surface, so the enclosed charge is \(q\). The area of the Gaussian surface is \(4\pi r^2\), and \(\mathbf{E}\) is uniform over the surface and perpendicular to it at each point. The flux integral \(\oint \mathbf{E}\cdot d\mathbf{A}\) is then just \(E(4\pi r^2)\), and Eq. (22.8) gives
\[
E(4\pi r^2)=\frac{q}{\varepsilon_0}.
\]
Thus,
\[
E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}
\qquad (r>R).
\]

This expression is the same as that for a point charge; outside the charged sphere, its field is the same as though the entire charge were concentrated at its center. Just outside the surface of the sphere, where \(r=R\),
\[
E=\frac{1}{4\pi\varepsilon_0}\frac{q}{R^2}.
\]

For \(r<R\), we again have
\[
\oint \mathbf{E}\cdot d\mathbf{A}=\frac{Q_{\text{encl}}}{\varepsilon_0}.
\]
But now the Gaussian surface lies entirely within the conductor, so it encloses no charge:
\[
Q_{\text{encl}}=0.
\]
Therefore,
\[
E=0
\qquad (r<R).
\]

**CAUTION:** Flux can be positive or negative. We have chosen the charge \(q\) to be positive. If the charge is negative, the electric field is radially inward instead of radially outward, and the electric flux through the Gaussian surface is negative. The electric-field magnitudes outside and at the surface of the sphere are given by the same expressions as above, except that \(q\) denotes the magnitude (absolute value) of the charge.

## Evaluation
We already knew that \(\mathbf{E}=0\) inside a solid conductor (whether spherical or not) when the charges are at rest. Figure 22.18 shows \(E\) as a function of the distance \(r\) from the center of the sphere.

In the limit as \(R \to 0\), the sphere becomes a point charge; there is then only an “outside,” and the field is everywhere given by
\[
E=\frac{q}{4\pi\varepsilon_0 r^2}.
\]
Thus we have deduced Coulomb’s law from Gauss’s law. (In Section 22.3 we deduced Gauss’s law from Coulomb’s law; the two laws are equivalent.)

We can also use this method for a conducting spherical shell (a spherical conductor with a concentric spherical hole inside) if there is no charge inside the hole. We use a spherical Gaussian surface with radius less than the radius of the hole. If there were a field inside the hole, it would have to be radial and spherically symmetric as before, so
\[
\mathbf{E}\cdot d\mathbf{A}=E\,dA.
\]
But now there is no enclosed charge, so \(Q_{\text{encl}}=0\) and \(E=0\) inside the hole.

Can you use this same technique to find the electric field in the region between a charged sphere and a concentric hollow conducting sphere that surrounds it?

## Key concepts used
- Gauss’s law: \(\displaystyle \oint \mathbf{E}\cdot d\mathbf{A}=\frac{Q_{\text{encl}}}{\varepsilon_0}\)
- Spherical symmetry implies \(\mathbf{E}\) is radial and constant in magnitude on a spherical Gaussian surface
- For a charged conductor in electrostatic equilibrium, excess charge resides on the surface
- Outside a spherically symmetric charged conductor, the field is the same as that of a point charge at the center
- Inside a conductor in electrostatic equilibrium, \(\mathbf{E}=0\)
