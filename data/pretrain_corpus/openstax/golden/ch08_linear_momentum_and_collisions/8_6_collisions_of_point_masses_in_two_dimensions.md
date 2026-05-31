# 8.6 Collisions of Point Masses in Two Dimensions

Source: OpenStax College Physics 2e, Chapter 8, Section 8.6

## Concept explanation
Two-dimensional collisions extend the one-dimensional analysis by resolving motion into components along perpendicular axes and solving the resulting one-dimensional momentum equations simultaneously.

To avoid complications from rotation, the section considers only the scattering of point masses, meaning structureless particles that cannot rotate or spin.

A common and useful case is when one particle is initially at rest. A coordinate system is chosen with the incoming particle initially moving parallel to the x-axis and the stationary particle at rest. In this setup, momentum is conserved along both the x-axis and the y-axis, giving two equations that can be used to analyze the collision.

For collisions of two equal-mass objects that are elastic, the combination of momentum conservation and conservation of internal kinetic energy leads to three possible outcomes:
- head-on collision; incoming ball stops
- no collision; incoming ball continues unaffected
- angle of separation is 90° after the collision

These results are often a good approximation for billiard-ball collisions, though spin can change the outcome.

## Key formulas
Conservation of momentum along the x-axis:
$$ 
m_1 v_{1x} + m_2 v_{2x} = m_1 v'_{1x} + m_2 v'_{2x}
 $$

For the common case where particle 2 is initially at rest and particle 1 initially moves along the x-axis:
$$ 
m_1 v_{1x} = m_1 v'_{1x} + m_2 v'_{2x}
 $$

Conservation of momentum along the y-axis:
$$ 
m_1 v_{1y} + m_2 v_{2y} = m_1 v'_{1y} + m_2 v'_{2y}
 $$

For the common case where particle 1 initially moves along the x-axis and particle 2 is initially at rest:
$$ 
0 = m_1 v'_{1y} + m_2 v'_{2y}
 $$

For an elastic collision of two equal masses with one initially at rest:
$$ 
v_{1x}' = -v_{2x}'
 $$
$$ 
v_{1y}' = -v_{2y}'
 $$
which implies
$$ 
0 = \left(v_1' + v_2'\right)\left(v_1' - v_2'\right)
 $$

The scattering angle result for equal-mass elastic collisions:
$$ 
\theta_1 + \theta_2 = 90^\circ
 $$

## Variables and units
- $m_1, m_2 $: masses of the two particles, in kilograms (kg)
- $v_{1x}, v_{1y}, v_{2x}, v_{2y} $: initial velocity components, in meters per second (m/s)
- $v'_{1x}, v'_{1y}, v'_{2x}, v'_{2y} $: final velocity components after collision, in m/s
- $v_1, v_2 $: speeds of the particles, in m/s
- $\theta_1, \theta_2 $: scattering angles, measured from the initial direction; angles are defined as positive in the counterclockwise direction, in degrees or radians as used
- A prime indicates the value after the collision

## Worked example
Suppose a 0.250-kg object is slid on a frictionless surface into a dark room, where it strikes an initially stationary object with mass 0.400 kg. The 0.250-kg object emerges from the room at an angle of $\theta_1 $ with its incoming direction.

The speed of the 0.250-kg object is originally 2.00 m/s and is 1.50 m/s after the collision. Calculate the magnitude and direction of the velocity of the 0.400-kg object after the collision.

Using conservation of momentum in the x- and y-directions, the angle of the second object is found from
$$ 
\tan \theta_2 = \frac{m_1 v_1' \sin \theta_1}{m_1 v_1 - m_1 v_1' \cos \theta_1}
 $$
Substituting the known values gives
$$ 
\theta_2 = -35.9^\circ
 $$
The negative sign means the object is scattered to the right.

Then using conservation of momentum along the y-axis:
$$ 
m_2 v_2' \sin \theta_2 = m_1 v_1' \sin \theta_1
 $$
Substituting the known values gives
$$ 
v_2' = 1.29\ \text{m/s}
 $$

So the initially stationary 0.400-kg object leaves with speed 1.29 m/s at an angle of $-35.9^\circ $.

## Key concepts used
- Two-dimensional collision analysis
- Point masses
- Conservation of momentum
- Momentum components along perpendicular axes
- Laboratory coordinate system
- Elastic collisions
- Internal kinetic energy
- Scattering angle
- Equal-mass collision result of 90° separation
