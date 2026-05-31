---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.2
subtitle: Magnitude and direction of an induced emf
needs_review: true
---

# Example 29.2: Magnitude and direction of an induced emf

## Problem
A 500-loop circular wire coil with radius 4.00 cm is placed between the poles of a large electromagnet. The magnetic field is uniform and makes an angle of 30° with the plane of the coil; it decreases at 0.200 T/s. What are the magnitude and direction of the induced emf?

## Setup
IDENTIFY and SET UP: Our target variable is the emf induced by a varying magnetic flux through the coil. The flux varies because the magnetic field decreases in amplitude. We choose the area vector to be in the direction shown in Fig. 29.7. With this choice, the geometry is similar to that of Fig. 29.6b. That figure will help us determine the direction of the induced emf.

The magnetic field is uniform over the loop, so we can calculate the flux using Eq. (29.2):
$$ 
\Phi_B = BA\cos\phi
 $$
where $\phi $ is the angle between $\vec B $ and the area vector $\vec A $.

In this expression, the only quantity that changes with time is the magnitude $B $ of the field, so
$$ 
\frac{d\Phi_B}{dt} = \frac{dB}{dt}A\cos\phi
 $$

CAUTION: Remember how $\phi $ is defined. You may have been tempted to say that $\phi = 30^\circ $ in this problem. If so, remember that $\phi $ is the angle between $\vec B $ and $\vec A $, not the angle between $\vec B $ and the plane of the loop.

Because the field makes an angle of $30^\circ $ with the plane of the coil, the angle between $\vec B $ and $\vec A $ is
$$ 
\phi = 60^\circ
 $$

## Solution
From Eq. (29.4), the induced emf in the coil of $N = 500 $ turns is
$$ 
\mathcal{E} = -N\frac{d\Phi_B}{dt}
= -N\frac{d}{dt}(BA\cos\phi)
 $$
Since only $B $ changes with time,
$$ 
\mathcal{E} = -N A\cos\phi \,\frac{dB}{dt}
 $$

Using
$$ 
N = 500,\quad r = 0.0400\ \text{m},\quad A = \pi r^2,\quad \phi = 60^\circ,\quad \frac{dB}{dt} = -0.200\ \text{T/s}
 $$
the magnitude is
$$ 
\mathcal{E} = 500\,(0.200\ \text{T/s})\bigl[\pi(0.0400\ \text{m})^2\bigr]\cos 30^\circ = 0.435\ \text{V}
 $$

The positive answer means that when you point your right thumb in the direction of the area vector $\vec A $ (below the magnetic field $\vec B $ in Fig. 29.7), the positive direction for the emf is in the direction of the curled fingers of your right hand. If you viewed the coil from the left in Fig. 29.7 and looked in the direction of $\vec A $, the emf would be clockwise.

## Evaluation
If the ends of the wire are connected, the direction of current in the coil is in the same direction as the emf—that is, clockwise as seen from the left side of the coil. A clockwise current increases the magnetic flux through the coil, and therefore tends to oppose the decrease in total flux. This is an example of Lenz’s law, which we’ll discuss in Section 29.3.

## Key concepts used
- Magnetic flux through a loop: $\Phi_B = BA\cos\phi $
- Faraday’s law for induced emf: $\mathcal{E} = -N\,d\Phi_B/dt $
- Relationship between angle to the plane and angle to the area vector
- Right-hand rule for the sign/direction of induced emf
- Lenz’s law
