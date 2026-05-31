---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.4
example_number: 22.8
subtitle: Field between oppositely charged parallel conducting plates
needs_review: true
---

# Example 22.8: Field between oppositely charged parallel conducting plates

## Problem
Two large plane parallel conducting plates are given charges of equal magnitude and opposite sign; the surface charge densities are not legible in the source text. Find the electric field in the region between the plates.

## Setup
**IDENTIFY and SET UP:** Figure 22.21a shows the field. Because opposite charges attract, most of the charge accumulates at the opposing faces of the plates. A small amount of charge resides on the outer surfaces of the plates, and there is some spreading or “fringing” of the field at the edges. But if the plates are very large in comparison to the distance between them, the amount of charge on the outer surfaces is negligibly small, and the fringing can be neglected except near the edges.

In this case we can assume that the field is uniform in the interior region between the plates, as in Fig. 22.21b, and that the charges are distributed uniformly over the opposing surfaces. To exploit this symmetry, we can use the shaded Gaussian surfaces $S_1 $, $S_2 $, $S_3 $, and $S_4 $. These surfaces are cylinders with flat ends of area $A $; one end of each surface lies within a plate.

The field between the two plates is nearly uniform, pointing from the positive plate toward the negative one.

## Solution
**EXECUTE:** The left-hand end of surface $S_1 $ is within the positive plate 1. Since the field is zero within the volume of any solid conductor under electrostatic conditions, there is no electric flux through this end. The electric field between the plates is perpendicular to the right-hand end, so on that end $\vec E \cdot d\vec A = E\,dA $, and the flux is $EA $; this is positive, since $\vec E $ is directed out of the Gaussian surface.

There is no flux through the side walls of the cylinder, since these walls are parallel to $\vec E $. So the total flux integral in Gauss’s law is
$$ 
\Phi_E = EA.
 $$

The net charge enclosed by the cylinder is $sA $, so Eq. (22.8) yields
$$ 
EA = \frac{sA}{\varepsilon_0}.
 $$
Thus,
$$ 
E = \frac{s}{\varepsilon_0}.
 $$

The field is uniform and perpendicular to the plates, and its magnitude is independent of the distance from either plate. The Gaussian surface $S_1 $ yields the same result. Surfaces $S_2 $, $S_3 $, and $S_4 $ yield $E=0 $ to the left of plate 1 and to the right of plate 2, respectively. We leave these calculations to you (see Exercise 22.29).

## Evaluation
We obtained the same results in Example 21.11 by using the principle of superposition of electric fields. The fields due to the two sheets of charge (one on each plate) are $\vec E_1 $ and $\vec E_2 $. From Example 22.7, both of these have magnitude $s/(2\varepsilon_0) $.

The total electric field at any point is the vector sum
$$ 
\vec E = \vec E_1 + \vec E_2.
 $$

At points $a $ and $b $ in Fig. 22.21b, $\vec E_1 $ and $\vec E_2 $ point in opposite directions, and their sum is zero. At point $c $, $\vec E_1 $ and $\vec E_2 $ are in the same direction; their sum has magnitude $s/\varepsilon_0 $, just as we found above using Gauss’s law.

## Key concepts used
- Gauss’s law
- Symmetry of the electric field between large parallel plates
- Electric flux through a Gaussian surface
- Electric field of a conductor in electrostatic equilibrium
- Superposition of electric fields
