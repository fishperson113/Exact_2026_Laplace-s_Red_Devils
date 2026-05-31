---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.5
example_number: 29.11
subtitle: Induced electric fields
needs_review: true
---

# Example 29.11: Induced electric fields

## Problem
Suppose the long solenoid in Fig. 29.17a has 500 turns per meter and cross-sectional area 4.0 cm$^2 $. The current in its windings is increasing at 100 A/s.  
(a) Find the magnitude of the induced emf in the wire loop outside the solenoid.  
(b) Find the magnitude of the induced electric field within the loop if its radius is 2.0 cm.

## Setup
**IDENTIFY and SET UP:** As in Fig. 29.17b, the increasing magnetic field inside the solenoid causes a change in the magnetic flux through the wire loop and hence induces an electric field around the loop. Our target variables are the induced emf $\mathcal{E} $ and the electric-field magnitude $E $. We use Eq. (29.8) to determine the emf.

Determining the field magnitude $E $ is simplified because the loop and the solenoid share the same central axis. Hence, by symmetry, the electric field is tangent to the loop and has the same magnitude all the way around its circumference. We can therefore use Eq. (29.9) to find $E $.

## Solution
**EXECUTE:** (a) From Eq. (29.8), the induced emf is
$$ 
\mathcal{E}=-\frac{d\Phi_B}{dt}=-\mu_0 n A \frac{dI}{dt}
 $$
Substituting the given values,
$$ 
\mathcal{E}=-(14\pi\times 10^{-7}\ \mathrm{Wb/(A\cdot m)})(500\ \mathrm{turns/m})(14.0\times10^{-4}\ \mathrm{m^2})(100\ \mathrm{A/s})
 $$
$$ 
=-25\times10^{-6}\ \mathrm{Wb/s}=-25\times10^{-6}\ \mathrm{V}=-25\ \mathrm{mV}
 $$

(b) By symmetry the line integral
$$ 
\oint \mathbf{E}\cdot d\mathbf{l}
 $$
has absolute value no matter which direction we integrate around the loop. This is equal to the absolute value of the emf, so
$$ 
E=\frac{|\mathcal{E}|}{2\pi r}
=\frac{25\times10^{-6}\ \mathrm{V}}{2\pi(2.0\times10^{-2}\ \mathrm{m})}
=2.0\times10^{-4}\ \mathrm{V/m}
 $$

## Evaluation
In Fig. 29.17b the magnetic flux into the plane of the figure is increasing. According to the right-hand rule for induced emf (illustrated in Fig. 29.6), a positive emf would be clockwise around the loop; the negative sign of $\mathcal{E} $ shows that the emf is in the counterclockwise direction. Can you also show this using Lenz’s law?

## Key concepts used
- Faraday’s law for induced emf: $\mathcal{E}=-d\Phi_B/dt $
- Magnetic field inside a solenoid: $B=\mu_0 n I $
- Flux through the solenoid cross section: $\Phi_B = BA $
- Symmetry of the induced electric field around a circular loop
- Line integral of $\mathbf{E} $ around a closed path: $\oint \mathbf{E}\cdot d\mathbf{l} = \mathcal{E} $
