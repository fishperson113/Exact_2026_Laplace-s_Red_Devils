---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.2
example_number: 23.4
subtitle: Potential due to two point charges
needs_review: true
---

# Example 23.4: Potential due to two point charges

## Problem
An electric dipole consists of point charges $q_1 = +12\ \text{nC} $ and $q_2 = -12\ \text{nC} $ placed $10.0\ \text{cm} $ apart (Fig. 23.13). Compute the electric potentials at points $a $, $b $, and $c $.

## Setup
**IDENTIFY and SET UP:** This is the same arrangement as in Example 21.8, in which the electric field at each point was found by doing a vector sum. Here the target variable is the electric potential $V $ at three points, found by doing the algebraic sum in Eq. (23.15).

For point $a $, the distances are:
- $r_1 = 0.060\ \text{m} $
- $r_2 = 0.040\ \text{m} $

For point $b $, the distances are:
- $r_1 = r_2 = 0.130\ \text{m} $

For point $c $, the point is equidistant from the two charges, so the two contributions cancel.

The potential from point charges is
$$ 
V = \frac{1}{4\pi \varepsilon_0}\sum_i \frac{q_i}{r_i}
= \frac{1}{4\pi \varepsilon_0}\left(\frac{q_1}{r_1}+\frac{q_2}{r_2}\right).
 $$

## Solution
**EXECUTE:** At point $a $,
$$ 
V_a=\frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{r_1}+\frac{q_2}{r_2}\right)
 $$
with $q_1=+12\times10^{-9}\ \text{C} $, $q_2=-12\times10^{-9}\ \text{C} $, $r_1=0.060\ \text{m} $, and $r_2=0.040\ \text{m} $:
$$ 
V_a=(9.0\times10^9\ \text{N}\cdot\text{m}^2/\text{C}^2)\left(\frac{12\times10^{-9}\ \text{C}}{0.060\ \text{m}}+\frac{-12\times10^{-9}\ \text{C}}{0.040\ \text{m}}\right).
 $$
Thus,
$$ 
V_a=1800\ \text{V}-2700\ \text{V}=-900\ \text{V}.
 $$

In a similar way, at point $b $, where $r_1=r_2=0.130\ \text{m} $,
$$ 
V_b=\frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{r_1}+\frac{q_2}{r_2}\right)=1930\ \text{V}.
 $$

At point $c $, where the point is equidistant from the two charges,
$$ 
V_c=0.
 $$

## Evaluation
Let’s confirm that these results make sense. Point $a $ is closer to the $-12\ \text{nC} $ charge than to the $+12\ \text{nC} $ charge, so the potential at $a $ is negative. The potential is positive at point $b $, which is closer to the $+12\ \text{nC} $ charge than the $-12\ \text{nC} $ charge. Finally, point $c $ is equidistant from the $-12\ \text{nC} $ charge and the $+12\ \text{nC} $ charge, so the potential there is zero. The potential is also equal to zero at a point infinitely far from both charges.

Comparing this example with Example 21.8 shows that it is much easier to calculate electric potential, a scalar, than electric field, a vector.

## Key concepts used
- Electric potential due to point charges adds algebraically:
  $$ 
  V=\frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}.
   $$
- Potential is a scalar, so signs of the charges determine the sign of each contribution directly.
- If two equal and opposite charges are equidistant from a point, their potentials cancel.
