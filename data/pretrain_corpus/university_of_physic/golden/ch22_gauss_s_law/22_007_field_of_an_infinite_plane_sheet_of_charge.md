---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.4
example_number: 22.7
subtitle: Field of an infinite plane sheet of charge
needs_review: true
---

# Example 22.7: Field of an infinite plane sheet of charge

## Problem
Use Gauss’s law to find the electric field caused by a thin, flat, infinite sheet with a uniform positive surface charge density $ \sigma  $.

## Setup
IDENTIFY and SET UP: In Example 21.11 (Section 21.5) we found that the field of a uniformly charged infinite sheet is normal to the sheet, and that its magnitude is independent of the distance from the sheet. To take advantage of these symmetry properties, we use a cylindrical Gaussian surface with ends of area $A $ and with its axis perpendicular to the sheet of charge (Fig. 22.20).

## Solution
EXECUTE: The flux through the cylindrical part of our Gaussian surface is zero because $\vec E $ is parallel to that surface everywhere. The flux through each flat end of the surface is $EA $ because $\vec E $ is perpendicular to each end everywhere, so the total flux through both ends—and hence the total flux through the Gaussian surface—is $2EA $. The total enclosed charge is $\sigma A $, and so from Gauss’s law,
$$ 
2EA=\frac{\sigma A}{\varepsilon_0}.
 $$
Therefore,
$$ 
E=\frac{\sigma}{2\varepsilon_0}.
 $$

## Evaluation
If $\sigma $ is negative, $\vec E $ is directed toward the sheet, the flux through the Gaussian surface in Fig. 22.20 is negative, and $\sigma $ in the expression $E=\sigma/(2\varepsilon_0) $ denotes the magnitude (absolute value) of the charge density.

Again we see that, given favorable symmetry, we can deduce electric fields using Gauss’s law much more easily than using Coulomb’s law.

## Key concepts used
- Gauss’s law: $\displaystyle \oint \vec E\cdot d\vec A = \frac{Q_{\text{encl}}}{\varepsilon_0} $
- Symmetry of an infinite plane sheet of charge
- Electric field is uniform in magnitude and perpendicular to the sheet
- Choice of a cylindrical Gaussian surface
- Flux contributions:
  - curved surface: $0 $
  - each flat end: $EA $
- Enclosed charge: $Q_{\text{encl}}=\sigma A $
- Result: $\displaystyle E=\frac{\sigma}{2\varepsilon_0} $
