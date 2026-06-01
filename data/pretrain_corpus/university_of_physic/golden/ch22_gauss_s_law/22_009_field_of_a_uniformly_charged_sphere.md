---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.4
example_number: 22.9
subtitle: Field of a uniformly charged sphere
needs_review: true
---

# Example 22.9: Field of a uniformly charged sphere

## Problem
Positive electric charge is distributed uniformly throughout the volume of an insulating sphere with radius $R $. Find the magnitude of the electric field at a point a distance $r $ from the center of the sphere.

## Setup
**IDENTIFY and SET UP:** As in Example 22.5, the system is spherically symmetric. Hence we can use the conclusions of that example about the direction and magnitude of $\mathbf{E} $.

To make use of the spherical symmetry, we choose as our Gaussian surface a sphere with radius $r $ concentric with the charge distribution.

## Solution
**EXECUTE:** From symmetry, the direction of $\mathbf{E} $ is radial at every point on the Gaussian surface, so $\mathbf{E} $ and the field magnitude is the same at every point on the surface. Hence the total electric flux through the Gaussian surface is the product of $E $ and the total area of the surface $A = 4\pi r^2 $; that is,
$$ 
\Phi_E = EA = 4\pi r^2 E.
 $$

The amount of charge enclosed within the Gaussian surface depends on $r $.

To find $E $ inside the sphere, we choose $r < R $. The volume charge density $\rho $ is the charge $Q $ divided by the volume of the entire charged sphere of radius $R $:
$$ 
\rho = \frac{Q}{\frac{4}{3}\pi R^3}.
 $$
The volume $V_{\text{encl}} $ enclosed by the Gaussian surface is
$$ 
V_{\text{encl}}=\frac{4}{3}\pi r^3,
 $$
so the total charge $Q_{\text{encl}} $ enclosed by that surface is
$$ 
Q_{\text{encl}}=\rho V_{\text{encl}}=\left(\frac{Q}{\frac{4}{3}\pi R^3}\right)\left(\frac{4}{3}\pi r^3\right)=Q\frac{r^3}{R^3}.
 $$

Then Gauss’s law, Eq. (22.8), becomes
$$ 
4\pi r^2 E=\frac{Q_{\text{encl}}}{\varepsilon_0}
=\frac{Q}{\varepsilon_0}\frac{r^3}{R^3},
 $$
so
$$ 
E=\frac{1}{4\pi\varepsilon_0}\frac{Qr}{R^3}
\qquad (r<R).
 $$

The field magnitude is proportional to the distance $r $ of the field point from the center of the sphere.

To find $E $ outside the sphere, we take $r>R $. This surface encloses the entire charged sphere, so
$$ 
Q_{\text{encl}}=Q,
 $$
and Gauss’s law gives
$$ 
4\pi r^2 E=\frac{Q}{\varepsilon_0},
 $$
or
$$ 
E=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}
\qquad (r>R).
 $$

The field outside any spherically symmetric charged body varies as $1/r^2 $, as though the entire charge were concentrated at the center.

If the charge is negative, $\mathbf{E} $ is radially inward and in the expressions for $E $ we interpret $Q $ as the absolute value of the charge.

## Evaluation
Notice that if we set $r=R $ in either expression for $E $, we get the same result
$$ 
E=\frac{Q}{4\pi\varepsilon_0 R^2}
 $$
for the magnitude of the field at the surface of the sphere. This is because the magnitude $E $ is a continuous function of $r $.

By contrast, for the charged conducting sphere of Example 22.5 the electric-field magnitude is discontinuous at $r=R $ (it jumps from $E=0 $ just inside the sphere to $E=\frac{Q}{4\pi\varepsilon_0 R^2} $ just outside the sphere). In general, the electric field $\mathbf{E} $ is discontinuous in magnitude, direction, or both wherever there is a sheet of charge, such as at the surface of a charged conducting sphere (Example 22.5), at the surface of an infinite charged sheet (Example 22.7), or at the surface of a charged conducting plate (Example 22.8).

The approach used here can be applied to any spherically symmetric distribution of charge, even if it is not radially uniform, as it was here. Such charge distributions occur within many atoms and atomic nuclei, so Gauss’s law is useful in atomic and nuclear physics.

## Key concepts used
- Spherical symmetry allows a spherical Gaussian surface.
- On the Gaussian surface, $\mathbf{E} $ is radial and constant in magnitude.
- Electric flux through the sphere: $\Phi_E = 4\pi r^2 E $.
- Gauss’s law: $\Phi_E = Q_{\text{encl}}/\varepsilon_0 $.
- For $r<R $, enclosed charge scales as $r^3 $, giving $E \propto r $.
- For $r>R $, the sphere acts like a point charge at the center, giving $E \propto 1/r^2 $.
- The field is continuous at $r=R $ for a uniformly charged insulating sphere.
