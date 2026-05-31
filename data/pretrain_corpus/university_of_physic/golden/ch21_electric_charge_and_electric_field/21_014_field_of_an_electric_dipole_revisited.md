---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.7
example_number: 21.14
subtitle: Field of an electric dipole, revisited
needs_review: true
---

# Example 21.14: Field of an electric dipole, revisited

## Problem
An electric dipole is centered at the origin, with the dipole moment in the direction of the $y $-axis (Fig. 21.33). Derive an approximate expression for the electric field at a point $P $ on the $y $-axis for which $y $ is much larger than $d $. To do this, use the binomial expansion valid for the case $|x| \ll 1 $:

$$ 
(1+x)^n \approx 1 + nx + \frac{n(n-1)}{2}x^2 + \cdots
 $$

## Setup
**IDENTIFY and SET UP:** Use the principle of superposition: the total electric field is the vector sum of the field produced by the positive charge and the field produced by the negative charge. At the field point $P $ shown in Fig. 21.33, the field of the positive charge has a positive (upward) $y $-component and the field of the negative charge has a negative (downward) $y $-component. Add these components to find the total field, then apply the approximation that $y \gg d $.

## Solution
**EXECUTE:** The total $y $-component of electric field from the two charges is

$$ 
E_y
= \frac{q}{4\pi \varepsilon_0}
\left[
\frac{1}{(y-d/2)^2} - \frac{1}{(y+d/2)^2}
\right].
 $$

We used this same approach in Example 21.8 (Section 21.5). Now apply the approximation: when we are far from the dipole compared to its size, so $d/2y \ll 1 $, we have

$$ 
\left(1-\frac{d}{2y}\right)^{-2} \approx 1+\frac{d}{y},
\qquad
\left(1+\frac{d}{2y}\right)^{-2} \approx 1-\frac{d}{y}.
 $$

With $n=-2 $ and with $x=d/2y $ replaced in the binomial expansion, keep only the first two terms (the terms discarded are much smaller). Then

$$ 
E_y
= \frac{q}{4\pi \varepsilon_0 y^2}
\left[
\left(1+\frac{d}{y}\right)
-
\left(1-\frac{d}{y}\right)
\right].
 $$

Hence $E_y $ is given approximately by

$$ 
E_y \approx \frac{q}{4\pi \varepsilon_0 y^2}\left(\frac{2d}{y}\right)
= \frac{qd}{2\pi \varepsilon_0 y^3}
= \frac{p}{2\pi \varepsilon_0 y^3},
 $$

where $p = qd $ is the magnitude of the dipole moment.

## Evaluation
An alternative route to this result is to put the fractions in the first expression for $E_y $ over a common denominator, add, and then approximate the denominator as $y^4 $. We leave the details to you (see Exercise 21.60).

For points off the coordinate axes, the expressions are more complicated, but at all points far away from the dipole (in any direction) the field drops off as $1/r^3 $. We can compare this with the behavior of a point charge, the $1/r^2 $ behavior of a long line charge, and the independence of $r $ for a large sheet of charge. There are charge distributions for which the field drops off even more quickly. At large distances, the field of an electric quadrupole, which consists of two equal dipoles with opposite orientation separated by a small distance, drops off as $1/r^4 $.

## Key concepts used
- Superposition of electric fields
- Electric field of a point charge
- Binomial expansion for small $x $
- Far-field approximation for an էլectric dipole
- Dipole moment magnitude $p = qd $
