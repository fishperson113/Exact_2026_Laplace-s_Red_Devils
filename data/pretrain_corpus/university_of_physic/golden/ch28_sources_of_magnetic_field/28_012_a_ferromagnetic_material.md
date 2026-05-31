---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.8
example_number: 28.12
subtitle: A ferromagnetic material
needs_review: true
---

# Example 28.12: A ferromagnetic material

## Problem
A cube-shaped permanent magnet is made of a ferromagnetic material with a magnetization $M $ of about $8 \times 10^5\ \text{A/m} $. The side length is $2\ \text{cm} $.

(a) Find the magnetic dipole moment of the magnet.  
(b) Estimate the magnetic field due to the magnet at a point $10\ \text{cm} $ from the magnet along its axis.

## Setup
This problem uses the relationship between magnetization $M $ and magnetic dipole moment $m $, and the idea that a magnetic dipole produces a magnetic field.

We find the dipole moment using Eq. (28.28). To estimate the field, we approximate the magnet as a current loop with this same magnetic moment and use Eq. (28.18).

## Solution
(a) From Eq. (28.28),
$$ 
m = MV
 $$
with
$$ 
V = (2 \times 10^{-2}\ \text{m})^3
 $$
so
$$ 
m = (8 \times 10^5\ \text{A/m})(2 \times 10^{-2}\ \text{m})^3 = 6\ \text{A}\cdot\text{m}^2.
 $$

(b) From Eq. (28.18), the magnetic field on the axis of a current loop with magnetic moment $m $ is
$$ 
B = \frac{\mu_0 m}{2\pi (x^2 + a^2)^{3/2}}
 $$
where $x $ is the distance from the loop and $a $ is its radius.

We can use this expression here if we take $a $ to refer to the size of the permanent magnet. Strictly speaking, there are complications because our magnet does not have the same geometry as a circular current loop. But because $x $ is fairly large in comparison to the $2\ \text{cm} $ size of the magnet, the term $a^2 $ is negligible in comparison to $x^2 $ and can be ignored. So
$$ 
B \approx \frac{\mu_0 m}{2\pi x^3}.
 $$

Substituting $x = 10\ \text{cm} = 0.1\ \text{m} $, $m = 6\ \text{A}\cdot\text{m}^2 $, and $\mu_0 = 4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A} $,
$$ 
B \approx \frac{(4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})(6\ \text{A}\cdot\text{m}^2)}{2\pi (0.1\ \text{m})^3}
= 1 \times 10^{-3}\ \text{T}.
 $$
This is about ten times stronger than the earth’s magnetic field.

## Evaluation
We calculated $B $ at a point outside the magnetic material and therefore used $\mu_0 $, not the permeability $\mu $ of the magnetic material, in our calculation.

You would substitute permeability $\mu $ for $\mu_0 $ if you were calculating $B $ inside a material with relative permeability $\kappa_m $, for which
$$ 
\mu = \kappa_m \mu_0.
 $$

## Key concepts used
- Magnetization and magnetic dipole moment: $m = MV $
- Magnetic field on the axis of a magnetic dipole/current loop
- Far-field approximation: if $x \gg a $, then $x^2 + a^2 \approx x^2 $
- Use of $\mu_0 $ for fields outside magnetic material
