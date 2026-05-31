---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.3
example_number: 23.11
subtitle: A ring of charge
needs_review: true
---

# Example 23.11: A ring of charge

## Problem
Electric charge $Q $ is distributed uniformly around a thin ring of radius $a $ (Fig. 23.20). Find the potential at a point $P $ on the ring axis at a distance $x $ from the center of the ring.

## Setup
**IDENTIFY and SET UP:** We divide the ring into infinitesimal segments and use Eq. (23.16) to find $V $. All parts of the ring (and therefore all elements of the charge distribution) are at the same distance from $P $.

We know the electric field at all points along the $x $-axis from Example 21.9 (Section 21.5), so we can also find $V $ along this axis by integrating $\mathbf{E} \cdot d\mathbf{l} $ as in Eq. (23.17).

## Solution
**EXECUTE:** Figure 23.20 shows that the distance from each charge element $dq $ to $P $ is

$$ 
r = \sqrt{x^2 + a^2}.
 $$

Hence we can take the factor $1/r $ outside the integral in Eq. (23.16), and

$$ 
V = \frac{1}{4\pi\epsilon_0}\int \frac{dq}{r}
= \frac{1}{4\pi\epsilon_0}\frac{1}{\sqrt{x^2+a^2}}\int dq
= \frac{1}{4\pi\epsilon_0}\frac{Q}{\sqrt{x^2+a^2}}.
 $$

## Evaluation
When $x $ is much larger than $a $, our expression for $V $ becomes approximately

$$ 
V \approx \frac{Q}{4\pi\epsilon_0 x},
 $$

which is the potential at a distance $x $ from a point charge $Q $. Very far away from a charged ring, its electric potential looks like that of a point charge. We drew a similar conclusion about the electric field of a ring in Example 21.9 (Section 21.5).

## Key concepts used
- Electric potential from a continuous charge distribution
- All charge elements on a ring are the same distance from a point on the axis
- Superposition of potentials
- Far-field approximation: a ring looks like a point charge at large distances
