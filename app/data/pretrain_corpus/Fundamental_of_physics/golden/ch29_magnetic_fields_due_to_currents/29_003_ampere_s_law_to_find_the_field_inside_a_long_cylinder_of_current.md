---
source: Fundamentals of Physics
chapter: 29
section: 29-3
sample_problem_number: 29.03
subtitle: Ampere’s law to find the field inside a long cylinder of current
needs_review: false
---

# Sample Problem 29.03: Ampere’s law to find the field inside a long cylinder of current

## Problem
Figure 29-16a shows the cross section of a long conducting cylinder with inner radius $a = 2.0\ \text{cm} $ and outer radius $b = 4.0\ \text{cm} $. The cylinder carries a current out of the page, and the magnitude of the current density in the cross section is given by $J = cr^2 $, with $c = 3.0 \times 10^6\ \text{A/m}^4 $ and $r $ in meters. What is the magnetic field at the dot in Fig. 29-16a, which is at radius $r = 3.0\ \text{cm} $ from the central axis of the cylinder?

## Key ideas
The point at which we want to evaluate $\vec B $ is inside the material of the conducting cylinder, between its inner and outer radii. We note that the current distribution has cylindrical symmetry (it is the same all around the cross section for any given radius). Thus, the symmetry allows us to use Ampere’s law to find $\vec B $ at the point. We first draw the Amperian loop shown in Fig. 29-16b. The loop is concentric with the cylinder and has radius $r = 3.0\ \text{cm} $ because we want to evaluate $\vec B $ at that distance from the cylinder’s central axis.

Next, we must compute the current $i_{\text{enc}} $ that is encircled by the Amperian loop. However, we cannot set up a proportionality as in Eq. 29-19, because here the current is not uniformly distributed. Instead, we must integrate the current density magnitude from the cylinder’s inner radius $a $ to the loop radius $r $, using the steps shown in Figs. 29-16c through h.

## Solution
We write the integral as
$$ 
i_{\text{enc}}=\int \vec J \cdot d\vec A = \int_a^r cr^2(2\pi r\,dr).
 $$
Note that in these steps we took the differential area $dA $ to be the area of the thin ring in Figs. 29-16d-f and then replaced it with its equivalent, the product of the ring’s circumference $2\pi r $ and its thickness $dr $.

For the Amperian loop, the direction of integration indicated in Fig. 29-16b is (arbitrarily) clockwise. Applying the right-hand rule for Ampere’s law to that loop, we find that we should take $i_{\text{enc}} $ as negative because the current is directed out of the page but our thumb is directed into the page.

We next evaluate the left side of Ampere’s law as we did in Fig. 29-15, and we again obtain Eq. 29-18. Then Ampere’s law,
$$ 
\vec B \cdot \oint d\vec s = \mu_0 i_{\text{enc}},
 $$
gives us
$$ 
B(2\pi r)= -\mu_0 c \frac{(r^4-a^4)}{2}.
 $$

Solving for $B $ and substituting known data yield
$$ 
B = -\frac{\mu_0 c}{4r}(r^4-a^4)
 $$
$$ 
= -\frac{(4\pi\times10^{-7}\ \text{T}\cdot\text{m/A})(3.0\times10^6\ \text{A/m}^4)}{4(0.030\ \text{m})}\left[(0.030\ \text{m})^4-(0.020\ \text{m})^4\right].
 $$

Thus, the magnetic field at a point $3.0\ \text{cm} $ from the central axis has magnitude
$$ 
B=2.0\times10^{-5}\ \text{T}
 $$
and forms magnetic field lines that are directed opposite our direction of integration, hence counterclockwise in Fig. 29-16b.

## Answer
$$ 
\vec B = -2.0\times10^{-5}\ \text{T}
 $$
so the field has magnitude
$$ 
2.0\times10^{-5}\ \text{T}
 $$
and is directed counterclockwise in Fig. 29-16b.

## Key concepts used
- Cylindrical symmetry allows the use of Ampere’s law.
- The enclosed current must be found by integrating the nonuniform current density.
- For a thin ring, $dA = 2\pi r\,dr $.
- The sign of $i_{\text{enc}} $ follows from the chosen Amperian-loop direction and the right-hand rule.
- For a circular Amperian loop, $\oint d\vec s = 2\pi r $.
