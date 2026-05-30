# 5.2 Drag Forces

Source: OpenStax College Physics 2e, Chapter 5, Section 5.2

## Concept explanation
Drag force is the force on an object moving in a fluid, either a gas or a liquid. It opposes the motion of the object, like friction does. The magnitude of the drag force depends on the object’s shape, size, velocity, and the fluid it moves through.

For many large objects moving through air at ordinary or high speeds, the drag force is proportional to the square of the speed. This is written as

\[
F_D \propto v^2
\]

and more specifically as

\[
F_D = \frac{1}{2} C \rho A v^2
\]

where \(C\) is the drag coefficient, \(\rho\) is the density of the fluid, and \(A\) is the area of the object facing the fluid.

The drag coefficient is determined empirically, usually with a wind tunnel, and is dimensionless. It can depend on velocity, but in this section it is treated as constant.

Drag has many applications in sports and vehicle design. Aerodynamic shaping can reduce drag and improve fuel efficiency or speed. At highway speeds, over 50% of a car’s power may be used to overcome air drag.

A key consequence of drag is terminal velocity. For a falling object such as a skydiver, gravity acts downward with constant magnitude while drag increases with speed. Eventually drag can equal weight, making the net force zero. Then acceleration stops and the object falls at constant terminal velocity.

For a skydiver at terminal velocity, the drag force equals the weight:

\[
F_D = mg
\]

Combining this with the drag-force equation gives

\[
mg = \frac{1}{2} C \rho A v^2
\]

so the terminal velocity is

\[
v = \sqrt{\frac{2mg}{C\rho A}}
\]

The section also notes that for very small objects, very slow motion, or motion in a denser fluid, drag may be proportional to velocity rather than \(v^2\). In that case Stokes’ law applies:

\[
F_D = 6\pi r \eta v
\]

where \(r\) is the radius of the object, \(\eta\) is the viscosity of the fluid, and \(v\) is the object’s velocity.

## Key formulas
\[
F_D \propto v^2
\]

\[
F_D = \frac{1}{2} C \rho A v^2
\]

\[
F_D = mg \quad \text{at terminal velocity}
\]

\[
v = \sqrt{\frac{2mg}{C\rho A}}
\]

\[
F_D = 6\pi r \eta v
\]

## Variables and units
- \(F_D\): drag force, in newtons (N)
- \(v\): speed or velocity of the object, in meters per second (m/s)
- \(C\): drag coefficient, dimensionless
- \(\rho\): density of the fluid, in kilograms per cubic meter (kg/m\(^3\))
- \(A\): projected area facing the fluid, in square meters (m\(^2\))
- \(m\): mass of the object, in kilograms (kg)
- \(g\): acceleration due to gravity, in m/s\(^2\)
- \(r\): radius of the object, in meters (m)
- \(\eta\): viscosity of the fluid, in pascal-seconds (Pa·s)

## Worked example
### Example 5.2: A Terminal Velocity
Find the terminal velocity of an 85-kg skydiver falling in a spread-eagle position.

At terminal velocity, the drag force equals the skydiver’s weight:

\[
mg = \frac{1}{2} C \rho A v^2
\]

Solving for \(v\),

\[
v = \sqrt{\frac{2mg}{C\rho A}}
\]

Using the projected area for an adult falling spread-eagle, the text finds a terminal velocity of about \(95 \text{ m/s}\), which is about \(340 \text{ km/h}\).

## Key concepts used
- Drag force opposes motion through a fluid.
- For many large objects in air, drag is proportional to \(v^2\).
- Drag depends on shape, size, speed, fluid density, and drag coefficient.
- The drag coefficient is empirical and dimensionless.
- Terminal velocity occurs when drag equals weight, so net force and acceleration are zero.
- Smaller projected area leads to a larger terminal velocity for the same mass.
- For very small or very slow objects, drag may be proportional to velocity, as in Stokes’ law.
