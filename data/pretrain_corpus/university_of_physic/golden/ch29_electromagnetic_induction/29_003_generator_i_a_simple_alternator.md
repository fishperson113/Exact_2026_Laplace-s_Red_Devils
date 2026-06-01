---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.3
subtitle: Generator I: A simple alternator
needs_review: true
---

# Example 29.3: Generator I: A simple alternator

## Problem
Figure 29.8a shows a simple alternator, a device that generates an emf. A rectangular loop is rotated with constant angular speed about the axis shown. The magnetic field is uniform and constant. At time $t = 0 $, determine the induced emf.

## Setup
IDENTIFY and SET UP: The magnetic field $\mathbf{B} $ and the area $A $ of the loop are both constant, but the flux through the loop varies because the loop rotates and so the angle between $\mathbf{B} $ and the area vector $\mathbf{A} $ changes (Fig. 29.8a). Because the angular speed is constant and $f = 0 $ at $t = 0 $, the angle as a function of time is given by
$$ 
f = vt.
 $$

## Solution
EXECUTE: The magnetic field is uniform over the loop, so the magnetic flux is
$$ 
\mathcal{F}_B = BA\cos f = BA\cos(vt).
 $$
Hence, by Faraday’s law [Eq. (29.3)] the induced emf is
$$ 
\mathcal{E} = -\frac{d\mathcal{F}_B}{dt}
= -\frac{d}{dt}\bigl(BA\cos vt\bigr)
= vBA\sin vt.
 $$

## Evaluation
The induced emf $\mathcal{E} $ varies sinusoidally with time (Fig. 29.8b). When the plane of the loop is perpendicular to $\mathbf{B} $ or $\mathcal{F}_B $ reaches its maximum and minimum values, its instantaneous rate of change is zero and $\mathcal{E} $ is zero. Conversely, $\mathcal{F}_B $ reaches its maximum and minimum values when the plane of the loop is parallel to $\mathbf{B} $ or $\mathcal{E} $ is changing most rapidly. We note that the induced emf does not depend on the shape of the loop, but only on its area.

We can use the alternator as a source of emf in an external circuit by using two slip rings that rotate with the loop, as shown in Fig. 29.8a. The rings slide against stationary contacts called brushes, which are connected to the output terminals a and b. Since the emf varies sinusoidally, the current that results in the circuit is an alternating current that also varies sinusoidally in magnitude and direction. The amplitude of the emf can be increased by increasing the rotation speed, the field magnitude, or the loop area or by using $N $ loops instead of one, as in Eq. (29.4).

Alternators are used in automobiles to generate the currents in the ignition, the lights, and the entertainment system. The arrangement is a little different than in this example; rather than having a rotating loop in a magnetic field, the loop stays fixed and an electromagnet rotates. (The rotation is provided by a mechanical connection between the alternator and the engine.) But the result is the same; the flux through the loop varies sinusoidally, producing a sinusoidally varying emf. Larger alternators of this same type are used in electric power plants (Fig. 29.9).

## Key concepts used
- Magnetic flux through a rotating loop varies as $\mathcal{F}_B = BA\cos\theta $.
- With constant angular speed, $\theta = \omega t $ and the flux becomes sinusoidal.
- Faraday’s law gives the induced emf:
  $$ 
  \mathcal{E} = -\frac{d\mathcal{F}_B}{dt}.
   $$
- A rotating loop in a uniform magnetic field produces an alternating emf.
