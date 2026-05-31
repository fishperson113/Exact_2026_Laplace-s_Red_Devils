---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.7
example_number: 28.10
subtitle: Field of a toroidal solenoid
needs_review: false
---

# Example 28.10: Field of a toroidal solenoid

## Problem
Figure 28.25a shows a doughnut-shaped toroidal solenoid, tightly wound with $N $ turns of wire carrying a current $I $. (In a practical solenoid the turns would be much more closely spaced than they are in the figure.) Find the magnetic field at all points.

## Setup
**IDENTIFY and SET UP:** Ignoring the slight pitch of the helical windings, we can consider each turn of a tightly wound toroidal solenoid as a loop lying in a plane perpendicular to the large, circular axis of the toroid. The symmetry of the situation then tells us that the magnetic field lines must be circles concentric with the toroid axis. Therefore we choose circular integration paths (of which Fig. 28.25b shows three) for use with Ampere’s law, so that the field $\mathbf{B} $ (if any) is tangent to each path at all points along the path.

## Solution
**EXECUTE:** Along each path,
$$ 
\oint \mathbf{B}\cdot d\mathbf{l}
 $$
equals the product of $B $ and the path circumference $2\pi r $.

The total current enclosed by path 1 is zero, so from Ampere’s law the field $\mathbf{B}=0 $ everywhere on this path.

Each turn of the winding passes twice through the area bounded by path 3, carrying equal currents in opposite directions. The net enclosed current is therefore zero, and hence $\mathbf{B}=0 $ at all points on this path as well. We conclude that the field of an ideal toroidal solenoid is confined to the space enclosed by the windings.

For path 2, we have
$$ 
\oint \mathbf{B}\cdot d\mathbf{l}=2\pi r B.
 $$
Each turn of the winding passes once through the area bounded by this path, so
$$ 
I_{\text{encl}}=NI.
 $$
We note that $I_{\text{encl}} $ is positive for the clockwise direction of integration in Fig. 28.25b, so $\mathbf{B} $ is in the direction shown. Ampere’s law then says that
$$ 
2\pi r B=\mu_0 NI,
 $$
so
$$ 
B=\frac{\mu_0 NI}{2\pi r}
\qquad\text{(toroidal solenoid)} \tag{28.24}
 $$

## Evaluation
Equation (28.24) indicates that $B $ is not uniform over the interior of the core, because different points in the interior are different distances $r $ from the toroid axis. However, if the radial extent of the core is small in comparison to $r $, the variation is slight. In that case, considering that $2\pi r $ is the circumferential length of the toroid and that $N/2\pi r $ is the number of turns per unit length $n $, the field may be written as
$$ 
B=\mu_0 n I
 $$
just as it is at the center of a long, straight solenoid.

In a real toroidal solenoid the turns are not precisely circular loops but rather segments of a bent helix. As a result, the external field is not exactly zero. To estimate its magnitude, we imagine Fig. 28.25a as being very roughly equivalent, for points outside the torus, to a single-turn circular loop with radius $r $. At the center of such a loop, Eq. (28.17) gives
$$ 
B=\frac{\mu_0 I}{2r};
 $$
this is smaller than the field inside the solenoid by the factor $N/\pi $.

The equations we have derived for the field in a closely wound straight or toroidal solenoid are strictly correct only for windings in vacuum. For most practical purposes, however, they can be used for windings in air or on a core of any nonmagnetic, nonsuperconducting material. In the next section we will show how these equations are modified if the core is a magnetic material.

## Key concepts used
- Ampere’s law
- Magnetic field symmetry
- Toroidal solenoid field confined to the interior region
- Enclosed current $I_{\text{encl}} $
- Circular integration paths concentric with the toroid axis
