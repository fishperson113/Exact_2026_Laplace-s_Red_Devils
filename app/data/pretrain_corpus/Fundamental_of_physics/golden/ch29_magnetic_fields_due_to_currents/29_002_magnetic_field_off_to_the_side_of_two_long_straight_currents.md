---
source: Fundamentals of Physics
chapter: 29
section: 29-1
sample_problem_number: 29.02
subtitle: Magnetic field off to the side of two long straight currents
needs_review: true
---

# Sample Problem 29.02: Magnetic field off to the side of two long straight currents

## Problem
Figure 29-9a shows two long parallel wires carrying currents $i_1 $ and $i_2 $ in opposite directions. What are the magnitude and direction of the net magnetic field at point $P $? Assume the following values: $i_1 = 15\ \text{A} $, $i_2 = 32\ \text{A} $, and $d = 5.3\ \text{cm} $.

## Key ideas
1. The net magnetic field at point $P $ is the vector sum of the magnetic fields due to the currents in the two wires.  
2. We can find the magnetic field due to any current by applying the Biot-Savart law to the current. For points near the current in a long straight wire, that law leads to Eq. 29-4.

## Solution
Finding the vectors: In Fig. 29-9a, point $P $ is distance $R $ from both currents $i_1 $ and $i_2 $. Thus, Eq. 29-4 tells us that at point $P $ those currents produce magnetic fields $\vec B_1 $ and $\vec B_2 $ with magnitudes

$$ 
B_1 = \frac{\mu_0 i_1}{2\pi R}
\qquad \text{and} \qquad
B_2 = \frac{\mu_0 i_2}{2\pi R}.
 $$

In the right triangle of Fig. 29-9a, note that the base angles (between sides $R $ and $d $) are both $45^\circ $. This allows us to write

$$ 
\cos 45^\circ = \frac{R}{d}
 $$

and replace $R $ with $d\cos 45^\circ $. Then the field magnitudes $B_1 $ and $B_2 $ become

$$ 
B_1 = \frac{\mu_0 i_1}{2\pi d \cos 45^\circ}
\qquad \text{and} \qquad
B_2 = \frac{\mu_0 i_2}{2\pi d \cos 45^\circ}.
 $$

We want to combine $\vec B_1 $ and $\vec B_2 $ to find their vector sum, which is the net field $\vec B $ at $P $. To find the directions of $\vec B_1 $ and $\vec B_2 $, we apply the right-hand rule of Fig. 29-5 to each current in Fig. 29-9a. For wire 1, with current out of the page, we mentally grasp the wire with the right hand, with the thumb pointing out of the page. Then the curled fingers indicate that the field lines run counterclockwise. In particular, in the region of point $P $, they are directed upward to the left. Recall that the magnetic field at a point near a long, straight current-carrying wire must be directed perpendicular to a radial line between the point and the current. Thus, $\vec B_1 $ must be directed upward to the left as drawn in Fig. 29-9b.

Repeating this analysis for the current in wire 2, we find that $\vec B_2 $ is directed upward to the right as drawn in Fig. 29-9b.

Adding the vectors: We can now vectorially add $\vec B_1 $ and $\vec B_2 $ to find the net magnetic field $\vec B $ at point $P $, either by using a vector-capable calculator or by resolving the vectors into components and then combining the components of $\vec B $. However, in Fig. 29-9b, there is a third method: Because $\vec B_1 $ and $\vec B_2 $ are perpendicular to each other, they form the legs of a right triangle, with $\vec B $ as the hypotenuse. So,

$$ 
B = \sqrt{B_1^2 + B_2^2}
 $$

$$ 
= \frac{\mu_0}{2\pi d \cos 45^\circ}\sqrt{i_1^2 + i_2^2}
 $$

$$ 
= \frac{(4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})\sqrt{(15\ \text{A})^2 + (32\ \text{A})^2}}{(2\pi)(5.3\times 10^{-2}\ \text{m})(\cos 45^\circ)}
 $$

$$ 
= 1.89\times 10^{-4}\ \text{T} = 190\ \mu\text{T}.
 $$

The angle $\phi $ between the directions of $\vec B_1 $ and $\vec B_2 $ in Fig. 29-9b follows from

$$ 
\tan \phi = \frac{B_1}{B_2},
 $$

which, with $B_1 $ and $B_2 $ as given above, yields

$$ 
\phi = \tan^{-1}\left(\frac{i_1}{i_2}\right)
= \tan^{-1}\left(\frac{15\ \text{A}}{32\ \text{A}}\right)
= 25^\circ.
 $$

The angle between $\vec B $ and the $x $ axis shown in Fig. 29-9b is then

$$ 
\phi + 45^\circ = 25^\circ + 45^\circ = 70^\circ.
 $$

## Answer
$$ 
B = 1.89\times 10^{-4}\ \text{T} \approx 190\ \mu\text{T},
 $$
directed $70^\circ $ above the $+x $ axis.

## Key concepts used
- Magnetic field of a long straight current-carrying wire
- Vector addition of magnetic fields
- Right-hand rule for current directions
- Geometry of the $45^\circ $ right triangle in Fig. 29-9a
