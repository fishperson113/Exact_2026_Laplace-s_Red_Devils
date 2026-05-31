---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.7
example_number: 28.8
subtitle: Field of a long cylindrical conductor
needs_review: true
---

# Example 28.8: Field of a long cylindrical conductor

## Problem
A cylindrical conductor with radius $R $ carries a current $I $ (Fig. 28.20). The current is uniformly distributed over the cross-sectional area of the conductor. Find the magnetic field as a function of the distance $r $ from the conductor axis for points both inside and outside the conductor.

## Setup
**IDENTIFY and SET UP:** As in Example 28.7, the current distribution has cylindrical symmetry, and the magnetic field lines must be circles concentric with the conductor axis. To find the magnetic field inside and outside the conductor, we choose circular integration paths with radii $r < R $ and $r > R $, respectively (see Fig. 28.20).

## Solution
**EXECUTE:** In either case the field $B $ has the same magnitude at every point on the circular integration path and is tangent to the path. Thus the magnitude of the line integral is simply
$$ 
\oint \mathbf{B}\cdot d\mathbf{l}=B(2\pi r).
 $$

To find the current $I_{\text{encl}} $ enclosed by a circular integration path inside the conductor $(r<R) $, note that the current density (current per unit area) is
$$ 
J=\frac{I}{\pi R^2},
 $$
so
$$ 
I_{\text{encl}}=J(\pi r^2)=I\frac{r^2}{R^2}.
 $$

Hence Ampère’s law gives
$$ 
B(2\pi r)=\mu_0 I\frac{r^2}{R^2},
 $$
or
$$ 
B=\frac{\mu_0 I}{2\pi}\frac{r}{R^2}, \qquad (r<R). \tag{28.21}
 $$

A circular integration path outside the conductor encloses the total current in the conductor, so
$$ 
I_{\text{encl}}=I.
 $$
Applying Ampère’s law gives the same equation as in Example 28.7, with the same result for $B $:
$$ 
B=\frac{\mu_0 I}{2\pi r}, \qquad (r>R). \tag{28.22}
 $$

Outside the conductor, the magnetic field is the same as that of a long, straight conductor carrying current $I $, independent of the radius $R $ over which the current is distributed. Indeed, the magnetic field outside any cylindrically symmetric current distribution is the same as if the entire current were concentrated along the axis of the distribution.

## Evaluation
**EVALUATE:** Note that at the surface of the conductor $(r=R) $, Eqs. (28.21) and (28.22) agree, as they must. Figure 28.21 shows a graph of $B $ as a function of $r $.

## Key concepts used
- Cylindrical symmetry implies magnetic field lines are circles concentric with the conductor axis.
- Use Ampère’s law with circular integration paths.
- For $r<R $, the enclosed current scales with area: $I_{\text{encl}} = I(r^2/R^2) $.
- For $r>R $, the enclosed current is the full current $I $.
- The field is
  $$ 
  B=\frac{\mu_0 I}{2\pi}\frac{r}{R^2}\quad (r<R), \qquad
  B=\frac{\mu_0 I}{2\pi r}\quad (r>R).
   $$
