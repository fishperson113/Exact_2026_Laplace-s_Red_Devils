---
source: Fundamentals of Physics
chapter: 26
section: 26-2
sample_problem_number: 26.02
subtitle: Current density, uniform and nonuniform
needs_review: false
---

# Sample Problem 26.02: Current density, uniform and nonuniform

## Problem
(a) The current density in a cylindrical wire of radius $R = 2.0\ \text{mm} $ is uniform across a cross section of the wire and is $J = 2.0 \times 10^{5}\ \text{A/m}^2 $. What is the current through the outer portion of the wire between radial distances $R/2 $ and $R $ (Fig. 26-6a)?

(b) Suppose, instead, that the current density through a cross section varies with radial distance $r $ as $J = ar^2 $, in which $a = 3.0 \times 10^{11}\ \text{A/m}^4 $ and $r $ is in meters. What now is the current through the same outer portion of the wire?

## Key ideas
Because the current density is uniform across the cross section, the current density $J $, the current $i $, and the cross-sectional area $A $ are related by Eq. 26-5:

$$ 
J = \frac{i}{A}.
 $$

Because the current density is not uniform across a cross section, we must use

$$ 
i = \int \vec{J}\cdot d\vec{A}.
 $$

## Solution
### (a)
We want only the current through a reduced cross-sectional area $A' $ of the wire, rather than the entire area, where

$$ 
A' = \pi R^2 - \pi\left(\frac{R}{2}\right)^2
= \pi\left(\frac{3R^2}{4}\right).
 $$

With $R = 0.0020\ \text{m} $,

$$ 
A' = \frac{3\pi}{4}(0.0020\ \text{m})^2
= 9.424\times 10^{-6}\ \text{m}^2.
 $$

Rewrite Eq. 26-5 as

$$ 
i = JA',
 $$

and substitute the data:

$$ 
i = (2.0\times 10^{5}\ \text{A/m}^2)(9.424\times 10^{-6}\ \text{m}^2).
 $$

### (b)
Because the current density is not uniform across the cross section of the wire, we must integrate the current density over the portion of the wire from $r = R/2 $ to $r = R $.

The current density vector and the differential area vector have the same direction. Thus,

$$ 
\vec{J}\cdot d\vec{A} = J\,dA\cos 0 = J\,dA.
 $$

We replace the differential area $dA $ with the area of a thin ring of circumference $2\pi r $ and width $dr $:

$$ 
dA = 2\pi r\,dr.
 $$

Then

$$ 
i = \int \vec{J}\cdot d\vec{A}
= \int_{R/2}^{R} ar^2(2\pi r\,dr)
= 2\pi a\int_{R/2}^{R} r^3\,dr.
 $$

So,

$$ 
i = 2\pi a\left[\frac{r^4}{4}\right]_{R/2}^{R}
= \frac{\pi a}{2}\left(R^4 - \frac{R^4}{16}\right)
= \frac{15}{32}\pi aR^4.
 $$

Substitute $a = 3.0\times 10^{11}\ \text{A/m}^4 $ and $R = 0.0020\ \text{m} $:

$$ 
i = \frac{15}{32}\pi(3.0\times 10^{11}\ \text{A/m}^4)(0.0020\ \text{m})^4.
 $$

## Answer
(a) $\boxed{1.9\ \text{A}} $

(b) $\boxed{7.1\ \text{A}} $

## Key concepts used
- Uniform current density: $J = i/A $
- Current through a specified region is proportional to the area when $J $ is uniform
- Nonuniform current density requires integration: $i = \int \vec{J}\cdot d\vec{A} $
- For a thin cylindrical ring, $dA = 2\pi r\,dr $
- Cylindrical symmetry and radial integration
