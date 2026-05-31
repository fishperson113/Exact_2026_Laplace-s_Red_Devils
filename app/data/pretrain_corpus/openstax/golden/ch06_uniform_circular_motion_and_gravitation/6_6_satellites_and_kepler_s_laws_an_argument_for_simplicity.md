# 6.6 Satellites and Kepler’s Laws: An Argument for Simplicity

Source: OpenStax College Physics 2e, Chapter 6, Section 6.6

## Concept explanation
Examples of gravitational orbits include artificial satellites orbiting Earth, the Moon orbiting Earth, and planets, asteroids, meteors, and comets orbiting the Sun. These motions are governed by gravitational force, and some important orbits can be described without computers when two conditions are satisfied:

1. A small mass orbits a much larger mass, so the larger body can be treated as stationary to a good approximation.
2. The system is isolated from other masses, so outside influences can be neglected.

Under these conditions, Kepler’s laws of planetary motion apply. Although historically stated for planets orbiting the Sun, they are valid for all bodies satisfying the two conditions above.

Kepler’s laws are descriptive laws based on observation, not cause-and-effect explanations. Kepler discovered them after careful study of Tycho Brahe’s recorded observations. Newton later showed that gravity is the cause of the observed orbital behavior.

Kepler’s first law states that the orbit of each planet about the Sun is an ellipse with the Sun at one focus. A circle is a special case of an ellipse in which the two foci coincide.

Kepler’s second law states that each planet moves so that an imaginary line drawn from the Sun to the planet sweeps out equal areas in equal times.

Kepler’s third law states that the ratio of the squares of the periods of any two planets about the Sun is equal to the ratio of the cubes of their average distances from the Sun. This law is valid only for comparing satellites of the same parent body.

For a circular orbit, Newton’s second law and universal gravitation show why the orbital speed depends only on the orbital radius and the mass of the central body. The gravitational force supplies the centripetal force, and the orbiting mass cancels from the equations. This implies that at a given orbital radius all small satellites orbit at the same speed around the same parent body.

Kepler’s third law can be rearranged to determine the mass of a parent body from the orbit of a satellite. If the period and orbital radius of a satellite are known, the parent mass can be calculated. This principle is used extensively to find the masses of heavenly bodies that have satellites.

The section also compares the Ptolemaic and Copernican models. The Ptolemaic view placed Earth at the center and used complex combinations of circular paths, with no underlying causal explanation. The Copernican model is simpler and is explained by a small number of laws of physics, including Newton’s universal law of gravitation. The broad applicability and simplicity of these laws are presented as evidence for the unity of physics.

## Key formulas
Kepler’s third law for two bodies orbiting the same parent mass:
$$ 
\frac{T_1^2}{T_2^2}=\frac{r_1^3}{r_2^3}
 $$
where $T $ is the period and $r $ is the average orbital radius.

For a circular orbit, gravity supplies the centripetal force:
$$ 
\frac{Gm_1m_2}{r^2}=\frac{mv^2}{r}
 $$
After cancellation of the orbiting mass:
$$ 
\frac{GM}{r^2}=\frac{v^2}{r}
 $$
where $M $ is the mass of the central body.

Using orbital speed $v=\frac{2\pi r}{T} $, the circular-orbit relation becomes:
$$ 
\frac{GM}{r^2}=\frac{4\pi^2r}{T^2}
 $$

From this, for a single satellite orbiting a parent body:
$$ 
\frac{r^3}{T^2}=\frac{GM}{4\pi^2}
 $$

These relations are valid only for small masses orbiting the same large one, and the two-satellite form is valid only when the parent mass is the same in both cases.

## Variables and units
- $T $: period, time for one orbit
  - Units: s, d, or y depending on context
- $r $: average orbital radius
  - Units: m or km
- $v $: orbital speed
  - Units: m/s
- $G $: gravitational constant
  - Units: N·m$^2 $/kg$^2 $
- $M $: mass of the parent body
  - Units: kg
- $m $: mass of the satellite or orbiting object
  - Units: kg

The section uses:
- orbital radius measured from the center of the parent body
- average radius for elliptical orbits
- equal-area intervals in equal times for Kepler’s second law

## Worked example
**Find the Time for One Orbit of an Earth Satellite**

Given:
- The Moon orbits Earth each $27.3\ \text{d} $
- The Moon’s average distance from Earth’s center is $3.84\times10^5\ \text{km} $
- An artificial satellite orbits at an average altitude of $1500\ \text{km} $ above Earth’s surface
- Earth’s radius is $6380\ \text{km} $

We want the satellite’s period $T_2 $.

The satellite’s orbital radius is:
$$ 
r_2 = 6380\ \text{km} + 1500\ \text{km} = 7880\ \text{km}
 $$

Using Kepler’s third law for the Moon (subscript 1) and satellite (subscript 2):
$$ 
\frac{T_1^2}{T_2^2}=\frac{r_1^3}{r_2^3}
 $$

Solving for $T_2 $:
$$ 
T_2=T_1\left(\frac{r_2}{r_1}\right)^{3/2}
 $$

Substituting values gives:
$$ 
T_2 \approx 1.77\ \text{d}
 $$

This is a reasonable period for a satellite in a fairly low orbit. The result also shows that any satellite at this altitude will orbit in the same amount of time, because the satellite’s mass is small compared with Earth’s.

## Key concepts used
- Gravitational orbits
- Small mass orbiting a much larger mass
- Isolated system approximation
- Kepler’s first law
- Kepler’s second law
- Kepler’s third law
- Elliptical orbit
- Circular-orbit approximation
- Centripetal force supplied by gravity
- Newton’s universal law of gravitation
- Orbital period
- Average orbital radius
- Determination of central mass from satellite motion
- Descriptive laws versus causal explanation
- Ptolemaic model
- Copernican model
