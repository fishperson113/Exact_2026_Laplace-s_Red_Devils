---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.1
subtitle: Emf and current induced in a loop
needs_review: true
---

# Example 29.1: Emf and current induced in a loop

## Problem
The magnetic field between the poles of the electromagnet in Fig. 29.5 is uniform at any time, but its magnitude is increasing at the rate of 0.020 T/s. The area of the conducting loop in the field is 120 cm², and the total circuit resistance, including the meter, is 5.0 Ω.

(a) Find the induced emf and the induced current in the circuit.  
(b) If the loop is replaced by one made of an insulator, what effect does this have on the induced emf and induced current?

## Setup
The magnetic flux \(\Phi_B\) through the loop changes as the magnetic field changes. Hence there will be an induced emf \(\mathcal{E}\) and an induced current \(I\) in the loop.

We calculate the induced emf using Faraday’s law, then find the induced current using
\[
I=\frac{\mathcal{E}}{R},
\]
where \(R\) is the total resistance of the circuit that includes the loop.

For the direction, the area vector \(\vec{A}\) for the loop is perpendicular to the plane of the loop; we take \(\vec{A}\) to be vertically upward. Then \(\vec{B}\) and \(\vec{A}\) are parallel, and because \(\vec{B}\) is uniform the magnetic flux through the loop is
\[
\Phi_B = \vec{B}\cdot \vec{A} = BA\cos 0 = BA.
\]

The area is constant, so the rate of change of magnetic flux is
\[
\frac{d\Phi_B}{dt} = A\frac{dB}{dt}.
\]

## Solution
### (a)
Convert the area:
\[
A = 120\ \text{cm}^2 = 0.012\ \text{m}^2.
\]

Then
\[
\frac{d\Phi_B}{dt}
= \frac{d(BA)}{dt}
= A\frac{dB}{dt}
= (0.012\ \text{m}^2)(0.020\ \text{T/s})
= 2.4\times 10^{-4}\ \text{V}.
\]

This, apart from a sign that we haven’t discussed yet, is the induced emf:
\[
\mathcal{E} = 2.4\times 10^{-4}\ \text{V} = 0.24\ \text{mV}.
\]

The corresponding induced current is
\[
I=\frac{\mathcal{E}}{R}
=\frac{2.4\times 10^{-4}\ \text{V}}{5.0\ \Omega}
=4.8\times 10^{-5}\ \text{A}
=0.048\ \text{mA}.
\]

The direction is clockwise around the loop, as seen from above.

### (b)
By changing to an insulating loop, we’ve made the resistance of the loop very high. Faraday’s law does not involve the resistance of the circuit in any way, so the induced emf does not change. But the current will be smaller, as given by
\[
I=\frac{\mathcal{E}}{R}.
\]
If the loop is made of a perfect insulator with infinite resistance, the induced current is zero.

## Evaluation
Let’s verify unit consistency. One way to do this is to note that the magnetic-force relationship implies that the units of \(B\) are the units of force divided by the units of (charge times velocity):
\[
1\ \text{T} = 1\ \frac{\text{N}\cdot \text{s}}{\text{C}\cdot \text{m}}.
\]
The units of magnetic flux are then
\[
1\ \text{T}\cdot \text{m}^2 = 1\ \text{N}\cdot \text{s}\cdot \text{m}/\text{C}
= 1\ \text{J}/\text{C}
= 1\ \text{V}.
\]
Thus the unit of \(d\Phi_B/dt\) is the volt, as required by Faraday’s law. Also recall that the unit of magnetic flux is the weber (Wb):
\[
1\ \text{T}\cdot \text{m}^2 = 1\ \text{Wb},
\]
so
\[
1\ \text{V} = 1\ \text{Wb/s}.
\]

## Key concepts used
- Faraday’s law relates induced emf to the rate of change of magnetic flux:
  \[
  \mathcal{E} = -\frac{d\Phi_B}{dt}.
  \]
- For a uniform field and fixed loop area,
  \[
  \Phi_B = BA\cos\theta.
  \]
- The induced current is found from Ohm’s law:
  \[
  I=\frac{\mathcal{E}}{R}.
  \]
- A changing magnetic flux induces an emf; a constant flux does not.
- The resistance affects the induced current, not the induced emf.
