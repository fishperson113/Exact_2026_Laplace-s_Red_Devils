---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.4
subtitle: Generator II: A DC generator and back emf in a motor
needs_review: true
---

# Example 29.4: Generator II: A DC generator and back emf in a motor

## Problem
The alternator in Example 29.3 produces a sinusoidally varying emf and hence an alternating current. A direct-current (dc) generator produces an emf that always has the same sign by using a split-ring commutator that reverses the connections to the external circuit at angular positions where the emf reverses.

Commercial dc generators have many coils and commutator segments, which smooth the output so the terminal voltage is one-directional and nearly constant. The same brush-and-commutator arrangement is used in the direct-current motor discussed in Section 27.8.

A motor has a square, 500-turn coil 10.0 cm on a side. If the magnetic field has magnitude 0.200 T, at what rotation speed is the average back emf of the motor equal to 112 V?

## Setup
**IDENTIFY and SET UP:** As far as the rotating loop is concerned, the situation is the same as in Example 29.3 except that we now have $N $ turns of wire. Without the commutator, the emf would alternate between positive and negative values and have an average value of zero. With the commutator, the emf is never negative and its average value is positive.

We use the result from Example 29.3 to obtain an expression for this average value and solve it for the rotational speed $\omega $.

## Solution
**EXECUTE:** Comparison of Figs. 29.8b and 29.10b shows that the back emf of the motor is just $N $ times the absolute value of the emf found for an alternator in Example 29.3, as in Eq. (29.4):

$$ 
|\mathcal{E}| = N B A |\sin \omega t|
 $$

To find the average back emf, we replace $|\sin \omega t| $ by its average value. We find this by integrating over half a cycle, from $t = 0 $ to $t = T/2 = \pi/\omega $, and dividing by the elapsed time $\pi/\omega $. During this half cycle, the sine function is positive, so $|\sin \omega t| = \sin \omega t $, and we find

$$ 
\langle |\sin \omega t| \rangle
= \frac{\omega}{\pi}\int_0^{\pi/\omega} \sin \omega t \, dt
= \frac{2}{\pi}
 $$

The average back emf is then

$$ 
\mathcal{E}_{\text{av}} = \frac{2 N \omega B A}{\pi}
 $$

This confirms that the back emf is proportional to the rotation speed $\omega $. Solving for $\omega $, we obtain

$$ 
\omega = \frac{\pi \mathcal{E}_{\text{av}}}{2 N B A}
 $$

Using $N = 500 $, $B = 0.200 \ \text{T} $, $A = (0.100 \ \text{m})^2 = 0.0100 \ \text{m}^2 $, and $\mathcal{E}_{\text{av}} = 112 \ \text{V} $,

$$ 
\omega
= \frac{\pi (112 \ \text{V})}{2(500)(0.200 \ \text{T})(0.0100 \ \text{m}^2)}
= 176 \ \text{rad/s}
 $$

We used the unit relationship $1 \ \text{V} = 1 \ \text{Wb/s} = 1 \ \text{T} \cdot \text{m}^2/\text{s} $.

## Evaluation
The average back emf is directly proportional to $\omega $. Hence, the slower the rotation speed, the less the back emf and the greater the possibility of burning out the motor, as described in Example 27.11.

## Key concepts used
- Faraday’s law for a rotating coil
- Effect of a commutator in making the emf one-directional
- Average value of $|\sin \omega t| $ over half a cycle
- Back emf in a motor is proportional to rotation speed
- Unit conversion: $1 \ \text{V} = 1 \ \text{T} \cdot \text{m}^2/\text{s} $
