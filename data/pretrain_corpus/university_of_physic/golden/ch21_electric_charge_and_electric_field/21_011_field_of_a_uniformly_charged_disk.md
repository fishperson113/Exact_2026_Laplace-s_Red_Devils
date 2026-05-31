---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.5
example_number: 21.11
subtitle: Field of a uniformly charged disk
needs_review: true
---

# Example 21.11: Field of a uniformly charged disk

## Problem
A nonconducting disk of radius $R $ has a uniform positive surface charge density $s $. Find the electric field at a point along the axis of the disk a distance $x $ from its center. Assume that $x $ is positive.

## Setup
**IDENTIFY and SET UP:** Figure 21.25 shows the situation. We represent the charge distribution as a collection of concentric rings of charge $dQ $. In Example 21.9 we obtained Eq. (21.8) for the field on the axis of a single uniformly charged ring, so all we need do here is integrate the contributions of our rings.

A typical ring has charge $dQ $, inner radius $r $, and outer radius $r+dr $. Its area is approximately equal to its width $dr $ times its circumference $2\pi r $, or
$$ 
dA = 2\pi r\,dr.
 $$
The charge per unit area is
$$ 
s = \frac{dQ}{dA},
 $$
so the charge of the ring is
$$ 
dQ = s\,dA = 2\pi s r\,dr.
 $$

## Solution
We use $dQ $ in place of $Q $ in Eq. (21.8), the expression for the field due to a ring that we found in Example 21.9, and replace the ring radius $r $ with $r $. Then the field component $dE_x $ at point $P $ due to this ring is
$$ 
dE_x=\frac{1}{4\pi\varepsilon_0}\,\frac{(2\pi s r\,dr)x}{(x^2+r^2)^{3/2}}.
 $$

To find the total field due to all the rings, we integrate $dE_x $ over $r $ from $0 $ to $R $ (not from $-R $ to $R $):
$$ 
E_x=\int_0^R dE_x
=\frac{s x}{4\varepsilon_0}\int_0^R \frac{2r\,dr}{(x^2+r^2)^{3/2}}.
 $$

You can evaluate this integral by making the substitution
$$ 
t=x^2+r^2
 $$
(which yields
$$ 
dt=2r\,dr
 $$
); you can work out the details.

The result is
$$ 
E_x=\frac{s}{2\varepsilon_0}\left(1-\frac{x}{\sqrt{x^2+R^2}}\right).
 $$

## Evaluation
If the disk is very large (or if we are very close to it), so that $R\gg x $, the term
$$ 
\frac{x}{\sqrt{x^2+R^2}}
 $$
in Eq. (21.11) is very much less than 1. Then Eq. (21.11) becomes
$$ 
E=\frac{s}{2\varepsilon_0}.
 $$

Our final result does not contain the distance $x $ from the plane. Hence the electric field produced by an infinite plane sheet of charge is independent of the distance from the sheet. The field direction is everywhere perpendicular to the sheet, away from it. There is no such thing as an infinite sheet of charge, but if the dimensions of the sheet are much larger than the distance $x $ of the field point $P $ from the sheet, the field is very nearly given by Eq. (21.12).

If $P $ is to the left of the plane, the result is the same except that the direction of $E $ is to the left instead of the right. If the surface charge density is negative, the directions of the fields on both sides of the plane are toward it rather than away from it.

## Key concepts used
- Model the disk as a sum of concentric charged rings.
- Use the electric field on the axis of a uniformly charged ring.
- Express ring charge with surface charge density: $dQ=s\,dA $.
- Integrate contributions from $r=0 $ to $r=R $.
- For $R\gg x $, the field approaches the infinite-sheet result $E=s/(2\varepsilon_0) $.
