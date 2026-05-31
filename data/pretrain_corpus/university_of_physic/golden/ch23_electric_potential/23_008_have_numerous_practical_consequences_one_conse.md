---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.3
example_number: 23.8
subtitle: have numerous practical consequences. One conse-
needs_review: true
---

# Example 23.8: have numerous practical consequences. One conse-

## Problem
A solid conducting sphere of radius $R $ has a total charge $q $. Find the electric potential everywhere, both outside and inside the sphere.

## Setup
IDENTIFY and SET UP: In Example 22.5 (Section 22.4) we used Gauss’s law to find the electric field at all points for this charge distribution. We can use that result to determine the corresponding potential.

For a conducting sphere, the electric field outside the sphere is the same as if the sphere were removed and replaced by a point charge $q $ at the center. We take $V=0 $ at infinity, as we did for a point charge.

## Solution
EXECUTE: The potential at a point outside the sphere at a distance $r $ from its center is the same as that due to a point charge at the center:

$$ 
V=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}
 $$

The potential at the surface of the sphere is

$$ 
V_{\text{surface}}=\frac{1}{4\pi\varepsilon_0}\frac{q}{R}
 $$

Inside the sphere, $E=0 $ everywhere. Hence no work is done on a test charge that moves from any point to any other point inside the sphere. This means that the potential is the same at every point inside the sphere and is equal to its value at the surface.

Thus,

$$ 
V=\frac{1}{4\pi\varepsilon_0}\frac{q}{R}
\qquad \text{for } r\le R
 $$

and

$$ 
V=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}
\qquad \text{for } r\ge R
 $$

## Evaluation
EVALUATE: For a positive charge $q $, the electric field points radially away from the sphere. As you move away from the sphere, in the direction of $E $, $V $ decreases (as it should).

The field and potential are:

$$ 
E=
\begin{cases}
\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}, & r\ge R \\
0, & r<R
\end{cases}
 $$

$$ 
V=
\begin{cases}
\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}, & r\ge R \\
\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}, & r\le R
\end{cases}
 $$

## Key concepts used
- A charged conducting sphere produces the same external field as a point charge $q $ at its center.
- The potential is defined relative to $V=0 $ at infinity.
- Inside a conductor in electrostatic equilibrium, $E=0 $, so the potential is constant.
- The potential inside the conducting sphere equals the surface potential.
