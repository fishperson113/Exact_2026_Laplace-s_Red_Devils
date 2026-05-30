---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.4
example_number: 22.6
subtitle: Field of a uniform line charge
needs_review: true
---

# Example 22.6: Field of a uniform line charge

## Problem
Electric charge is distributed uniformly along an infinitely long, thin wire. The charge per unit length is \(\lambda\) (assumed positive). Find the electric field using Gauss’s law.

## Setup
**Identify and set up:** From the symmetry of a uniformly charged, infinite wire, the electric field is radially outward if \(\lambda > 0\) and radially inward if \(\lambda < 0\). The field magnitude \(E\) depends only on the radial distance \(r\) from the wire.

This suggests using a cylindrical Gaussian surface of radius \(r\) and arbitrary length \(l\), coaxial with the wire and with its ends perpendicular to the wire.

## Solution
**Execute:** The flux through the flat ends of the Gaussian surface is zero because the radial electric field is parallel to these ends, so
\[
\mathbf{E}\cdot \mathbf{\hat n} = E\cos 90^\circ = 0.
\]

On the cylindrical part of the surface, \(\mathbf{E}\) is everywhere parallel to the outward normal, so
\[
\mathbf{E}\cdot \mathbf{\hat n} = E.
\]

The area of the cylindrical surface is
\[
A = 2\pi r l,
\]
so the total flux through the Gaussian surface is
\[
\Phi_E = EA = E(2\pi r l).
\]

The total enclosed charge is
\[
Q_{\text{encl}} = \lambda l.
\]

Using Gauss’s law,
\[
\Phi_E = \frac{Q_{\text{encl}}}{\varepsilon_0},
\]
we get
\[
E(2\pi r l) = \frac{\lambda l}{\varepsilon_0}.
\]

Solving for \(E\),
\[
E = \frac{\lambda}{2\pi \varepsilon_0 r}.
\]

Thus the electric field of an infinite line charge is
\[
\boxed{E = \frac{1}{2\pi \varepsilon_0}\frac{\lambda}{r}}.
\]

If \(\lambda < 0\), the field is directed radially inward, and \(\lambda\) should be interpreted as the absolute value of the charge per unit length in the magnitude expression.

## Evaluation
This result agrees with the field found earlier by a more laborious method. Even though the entire wire contributes to the field at any point, Gauss’s law uses only the charge enclosed by the Gaussian surface.

If the wire is short, the symmetry of the infinite wire is lost, and \(E\) is not uniform over a coaxial cylindrical Gaussian surface. In that case, Gauss’s law cannot be used to find \(E\) directly; the problem must be solved by other methods.

The same Gaussian-surface argument can also be used to show that the field outside a long, uniformly charged cylinder is the same as if all the charge were concentrated on a line along its axis. It can also be used for the region between a charged cylinder and a coaxial hollow conducting cylinder surrounding it.

## Key concepts used
- Gauss’s law: \(\displaystyle \Phi_E = \frac{Q_{\text{encl}}}{\varepsilon_0}\)
- Cylindrical symmetry of an infinite line charge
- Choice of a coaxial cylindrical Gaussian surface
- Zero flux through surfaces parallel to the electric field
- Enclosed charge for a uniform line: \(\displaystyle Q_{\text{encl}}=\lambda l\)
- Electric field of an infinite line charge: \(\displaystyle E=\frac{\lambda}{2\pi\varepsilon_0 r}\)
