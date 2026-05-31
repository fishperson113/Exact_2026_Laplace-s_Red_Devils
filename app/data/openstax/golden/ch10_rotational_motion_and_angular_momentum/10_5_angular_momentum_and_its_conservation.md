# 10.5 Angular Momentum and Its Conservation

Source: OpenStax College Physics 2e, Chapter 10, Section 10.5

## Concept explanation
Angular momentum is the rotational analog to linear momentum. Like linear momentum, it describes how motion is carried forward and is conserved when the net external torque is zero.

The section defines angular momentum as
$$ 
L = I\omega
 $$
which is analogous to the linear momentum relation
$$ 
p = mv.
 $$

This definition shows that an object with a large moment of inertia, such as Earth, can have a very large angular momentum. An object with a large angular velocity, such as a centrifuge, can also have a large angular momentum.

The relationship between torque and angular momentum is
$$ 
\sum \tau = \frac{dL}{dt}.
 $$
This is the rotational form of Newton’s second law and is exactly analogous to the relationship between force and linear momentum.

Angular momentum is conserved when the net external torque is zero:
$$ 
\sum \tau = 0 \quad \Rightarrow \quad L = \text{constant}.
 $$
For a system in which the moment of inertia changes, conservation gives
$$ 
I\omega = I'\omega'.
 $$
Thus, if the moment of inertia decreases, angular velocity must increase to keep angular momentum constant.

## Key formulas
$$ 
L = I\omega
 $$

$$ 
p = mv
 $$

$$ 
\sum \tau = \frac{dL}{dt}
 $$

$$ 
\sum \tau = 0 \Rightarrow L = \text{constant}
 $$

$$ 
I\omega = I'\omega'
 $$

For a sphere:
$$ 
I = \frac{2}{5}MR^2
 $$

For a disk:
$$ 
I = \frac{1}{2}MR^2
 $$

Rotational kinetic energy:
$$ 
K_{\text{rot}} = \frac{1}{2}I\omega^2
 $$

Angular acceleration from torque:
$$ 
\alpha = \frac{\tau}{I}
 $$

## Variables and units
- $L $: angular momentum, units $\text{kg} \cdot \text{m}^2/\text{s} $
- $I $: moment of inertia, units $\text{kg} \cdot \text{m}^2 $
- $\omega $: angular velocity, units $\text{rad/s} $
- $p $: linear momentum, units $\text{kg} \cdot \text{m/s} $
- $m $: mass, units $\text{kg} $
- $v $: linear speed, units $\text{m/s} $
- $\tau $: torque, units $\text{N} \cdot \text{m} $
- $t $: time, units $\text{s} $
- $\alpha $: angular acceleration, units $\text{rad/s}^2 $
- $K_{\text{rot}} $: rotational kinetic energy, units $\text{J} $

For angular momentum calculations involving revolutions per second, convert to radians per second using
$$ 
1\ \text{rev} = 2\pi\ \text{rad}.
 $$

## Worked example
### Calculating Angular Momentum of the Earth
Use
$$ 
L = I\omega
 $$
with Earth modeled as a sphere:
$$ 
I = \frac{2}{5}MR^2.
 $$

The section states Earth’s mass is $5.98\times10^{24}\ \text{kg} $ and its radius is $6.37\times10^6\ \text{m} $. Earth rotates once per day, so its angular velocity must be converted to SI units:
$$ 
\omega = \frac{2\pi\ \text{rad}}{1\ \text{rev}} \cdot \frac{1\ \text{rev}}{24\times3600\ \text{s}}.
 $$

Substituting the values gives Earth a very large angular momentum. The result is approximate because the calculation assumes Earth has constant density.

### Calculating the torque putting angular momentum into a rotating food tray
A person exerts a $2.50\ \text{N} $ force perpendicular to a lazy Susan of radius $0.260\ \text{m} $ for $0.150\ \text{s} $. The tray starts from rest and friction is negligible.

The torque is
$$ 
\tau = rF
 $$
because the force is perpendicular to the radius.

The angular momentum added is found from
$$ 
\sum \tau = \frac{dL}{dt},
 $$
so for a constant torque over the time interval,
$$ 
\Delta L = \tau \Delta t.
 $$

Using the given values yields the final angular momentum. To find the final angular velocity, use
$$ 
L = I\omega
 $$
with the moment of inertia of a disk:
$$ 
I = \frac{1}{2}MR^2.
 $$
The section states the lazy Susan’s mass is $4.00\ \text{kg} $. The resulting angular velocity is equivalent to one revolution in $8.71\ \text{s} $.

### Calculating the torque in a kick
A lower leg is kicked by a force of $2000\ \text{N} $ with an effective perpendicular lever arm of $2.20\ \text{cm} $. The section gives the moment of inertia of the lower leg as a specified value.

The torque is
$$ 
\tau = rF.
 $$

The angular acceleration follows from
$$ 
\alpha = \frac{\tau}{I}.
 $$

If the leg rotates through $1.00\ \text{rad} $ from rest, then the final angular velocity can be found from rotational kinematics:
$$ 
\omega^2 = \omega_0^2 + 2\alpha\Delta\theta,
 $$
and the rotational kinetic energy is
$$ 
K_{\text{rot}} = \frac{1}{2}I\omega^2.
 $$

## Key concepts used
- Angular momentum is the rotational analog of linear momentum.
- Angular momentum depends on both moment of inertia and angular velocity.
- Torque changes angular momentum according to $\sum \tau = dL/dt $.
- If net external torque is zero, angular momentum is conserved.
- When moment of inertia decreases, angular velocity increases if angular momentum is conserved.
- Conservation of angular momentum explains Earth’s persistent rotation, ice skater spins, tornado intensification, and rotational changes in contracting clouds.
