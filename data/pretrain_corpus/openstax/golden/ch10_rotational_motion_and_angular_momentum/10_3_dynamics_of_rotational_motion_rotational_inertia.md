# 10.3 Dynamics of Rotational Motion: Rotational Inertia

Source: OpenStax College Physics 2e, Chapter 10, Section 10.3

## Concept explanation
If a force is needed to change angular velocity, then rotational motion has a dynamics analogous to linear motion. Pushing farther from the pivot produces a larger angular acceleration, while a larger mass produces a smaller angular acceleration. This mirrors the relationship among force, mass, and acceleration in Newton’s second law.

For a point mass at distance $r $ from the axis, a force applied perpendicular to $r $ produces torque and angular acceleration. The rotational form of Newton’s second law is

$$ 
\tau_{\text{net}} = I\alpha
 $$

where $\tau_{\text{net}} $ is the total torque relative to the chosen axis, $I $ is the moment of inertia, and $\alpha $ is the angular acceleration. Torque is the rotational analog of force, moment of inertia is the rotational analog of mass, and angular acceleration is the rotational analog of translational acceleration.

The moment of inertia depends not only on total mass, but also on how that mass is distributed relative to the axis of rotation. Mass farther from the axis gives a larger moment of inertia and therefore a smaller angular acceleration for the same torque. For an object made of point masses, the moment of inertia is the sum

$$ 
I=\sum m_i r_i^2
 $$

For a hoop with all its mass at the same distance from the axis,

$$ 
I=MR^2
 $$

For a uniform solid disk about its central axis,

$$ 
I=\frac{1}{2}MR^2
 $$

Net torque is the sum of torques from all forces relative to the chosen axis. In this section, torques in the plane of rotation are treated as positive or negative and added algebraically.

## Key formulas
$$ 
\tau = rF \quad \text{(for force perpendicular to } r\text{)}
 $$

$$ 
\tau_{\text{net}} = I\alpha
 $$

$$ 
I=\sum m_i r_i^2
 $$

$$ 
I=MR^2 \quad \text{(hoop)}
 $$

$$ 
I=\frac{1}{2}MR^2 \quad \text{(uniform solid disk)}
 $$

$$ 
\tau = rF
 $$

$$ 
\alpha=\frac{\tau_{\text{net}}}{I}
 $$

## Variables and units
- $\tau $: torque, units of newton-meter $(\text{N}\cdot\text{m}) $
- $\tau_{\text{net}} $: net torque about the chosen axis, units $(\text{N}\cdot\text{m}) $
- $I $: moment of inertia, units of $\text{kg}\cdot\text{m}^2 $
- $\alpha $: angular acceleration, units of $\text{rad/s}^2 $
- $m_i $: mass of the $i $th point mass, units of kilograms $(\text{kg}) $
- $r_i $: distance of the $i $th point mass from the axis, units of meters $(\text{m}) $
- $M $: total mass, units of kilograms $(\text{kg}) $
- $R $: radius, units of meters $(\text{m}) $
- $F $: force, units of newtons $(\text{N}) $

## Worked example
**Example 10.7: Calculating the Effect of Mass Distribution on a Merry-Go-Round**

A father exerts a force of $250\ \text{N} $ at the edge of a merry-go-round with mass $50.0\ \text{kg} $ and radius $1.50\ \text{m} $. Find the angular acceleration:
(a) when no one is on the merry-go-round, and
(b) when an $18.0\ \text{kg} $ child sits $1.25\ \text{m} $ from the center.
Assume the merry-go-round is a uniform disk with negligible retarding friction.

### Strategy
Use

$$ 
\alpha=\frac{\tau_{\text{net}}}{I}
 $$

The applied force is perpendicular to the radius, so

$$ 
\tau = rF
 $$

is the same in both cases. The difference comes from the moment of inertia.

### Solution for (a)
For a uniform disk,

$$ 
I=\frac{1}{2}MR^2
 $$

with $M=50.0\ \text{kg} $ and $R=1.50\ \text{m} $. Using the torque from the applied force at the edge and substituting the known values gives the angular acceleration for the empty merry-go-round.

### Solution for (b)
Treat the child as a point mass at radius $1.25\ \text{m} $, so

$$ 
I_{\text{child}}=mr^2
 $$

with $m=18.0\ \text{kg} $. The total moment of inertia is the sum of the merry-go-round and child:

$$ 
I_{\text{total}}=I_{\text{merry-go-round}}+I_{\text{child}}
 $$

Substituting the known values into $\alpha=\tau_{\text{net}}/I $ gives the angular acceleration for the system.

### Discussion
The angular acceleration is smaller when the child is on the merry-go-round because the total moment of inertia is larger.

## Key concepts used
- Rotational motion has direct analogs to linear motion.
- Torque is the rotational effect of a force.
- Moment of inertia measures resistance to angular acceleration.
- The distribution of mass relative to the axis matters.
- Larger torque produces larger angular acceleration.
- Larger moment of inertia produces smaller angular acceleration.
- For point masses, moments of inertia add as $I=\sum m_ir_i^2 $.
- For a uniform disk, $I=\frac{1}{2}MR^2 $.
