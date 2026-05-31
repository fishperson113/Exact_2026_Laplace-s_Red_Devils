---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.5
example_number: 21.10
subtitle: Field of a charged line segment
needs_review: true
---

# Example 21.10: Field of a charged line segment

## Problem
Positive charge is distributed uniformly along the $y $-axis between $y=-a $ and $y=+a $. Find the electric field at point $P $ on the $x $-axis at a distance $x $ from the origin.

## Setup
**IDENTIFY and SET UP:** Figure 21.24 shows the situation. As in Example 21.9, we must find the electric field due to a continuous distribution of charge. Our target variable is an expression for the electric field at $P $ as a function of $x $. The $x $-axis is a perpendicular bisector of the segment, so we can use a symmetry argument.

Let the total charge on the segment be $Q $, so the linear charge density is
$$ 
\lambda = \frac{Q}{2a}.
 $$
For an infinitesimal segment of length $dy $,
$$ 
dQ = \lambda\,dy = \frac{Q}{2a}\,dy.
 $$

The distance from a segment at height $y $ to the field point $P $ is
$$ 
r = \sqrt{x^2+y^2}.
 $$

## Solution
**EXECUTE:** The magnitude of the field at $P $ due to the segment at height $y $ is
$$ 
dE=\frac{1}{4\pi\varepsilon_0}\frac{dQ}{r^2}
=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\frac{dy}{x^2+y^2}.
 $$

From Figure 21.24, the components of this field are
$$ 
dE_x=dE\cos\alpha,\qquad dE_y=-dE\sin\alpha,
 $$
where
$$ 
\cos\alpha=\frac{x}{r},\qquad \sin\alpha=\frac{y}{r}.
 $$

Thus
$$ 
dE_x=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\frac{x\,dy}{(x^2+y^2)^{3/2}},
 $$
$$ 
dE_y=-\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\frac{y\,dy}{(x^2+y^2)^{3/2}}.
 $$

To find the total field at $P $, integrate from $y=-a $ to $y=+a $:
$$ 
E_x=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\int_{-a}^{+a}\frac{x\,dy}{(x^2+y^2)^{3/2}},
 $$
$$ 
E_y=\frac{1}{4\pi\varepsilon_0}\frac{Q}{2a}\int_{-a}^{+a}\frac{-y\,dy}{(x^2+y^2)^{3/2}}.
 $$

The results are
$$ 
E_y=0,
 $$
and
$$ 
E_x=\frac{1}{4\pi\varepsilon_0}\frac{Q}{x\sqrt{x^2+a^2}}.
 $$

So, in vector form,
$$ 
\vec E=\frac{1}{4\pi\varepsilon_0}\frac{Q}{x\sqrt{x^2+a^2}}\;\hat{\mathbf{i}}.
 $$
This points away from the line of charge if $Q $ is positive and toward the line of charge if $Q $ is negative.

## Evaluation
Using a symmetry argument as in Example 21.9, we could have guessed that $E_y $ would be zero; if we place a positive test charge at $P $, the upper half of the line of charge pushes downward on it, and the lower half pushes up with equal magnitude. Symmetry also tells us that the upper and lower halves of the segment contribute equally to the total field at $P $.

If the segment is very short (or the field point is very far from the segment) so that $a \ll x $, we can neglect $a $ in the denominator of Eq. (21.9). Then the field becomes that of a point charge:
$$ 
\vec E \approx \frac{1}{4\pi\varepsilon_0}\frac{Q}{x^2}\,\hat{\mathbf{i}}.
 $$

To see what happens if the segment is very long (or the field point is very close to it) so that $a \gg x $, rewrite Eq. (21.9) slightly:
$$ 
\vec E=\frac{1}{4\pi\varepsilon_0}\frac{1}{x^2\sqrt{x^2/a^2+1}}\,Q\,\hat{\mathbf{i}}.
 $$
In the limit $a \gg x $, we can neglect $x^2/a^2 $ in the denominator, so
$$ 
\vec E \approx \frac{1}{4\pi\varepsilon_0}\frac{Q}{ax}\,\hat{\mathbf{i}}
= \frac{\lambda}{2\pi\varepsilon_0 x}\,\hat{\mathbf{i}}.
 $$

This is the field of an infinitely long line of charge. At any point a perpendicular distance $r $ from the line in any direction,
$$ 
E=\frac{\lambda}{2\pi\varepsilon_0 r}.
 $$
Note that this field is proportional to $1/r $ rather than to $1/r^2 $ as for a point charge.

There’s really no such thing in nature as an infinite line of charge. But when the field point is close enough to the line, there’s very little difference between the result for an infinite line and the real-life finite case. For example, if the distance of the field point from the center of the line is 1% of the length of the line, the value of $E $ differs from the infinite-length value by less than 0.02%.

## Key concepts used
- Electric field due to a continuous charge distribution
- Linear charge density $\lambda = Q/(2a) $
- Differential charge element $dQ=\lambda\,dy $
- Superposition and symmetry
- Component resolution of vectors
- Limiting cases: point-charge limit and infinite-line limit
