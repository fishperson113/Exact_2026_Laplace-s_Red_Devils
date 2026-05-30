# 12.3 The Most General Applications of Bernoulli’s Equation

Source: OpenStax College Physics 2e, Chapter 12, Section 12.3

## Concept explanation
This section applies Bernoulli’s equation to situations where pressure, velocity, and height can all change.

Torricelli’s theorem follows from Bernoulli’s equation for fluid flowing from the surface of a reservoir to an outlet at a lower height. When resistance is negligible, and both the fluid surface and the outlet are at atmospheric pressure, the pressure terms cancel. For incompressible flow, the density also cancels, leaving the exit speed determined only by the vertical drop in height. The result is the same as the speed an object would have after falling that distance with negligible resistance. This result is independent of the direction of the velocity.

A more general application is a fire hose nozzle, where the water rises to a higher elevation and speeds up as the nozzle diameter decreases. Bernoulli’s equation must be used because the depth is not constant and both pressure and speed change. Even when the nozzle pressure is close to atmospheric pressure, the flowing water can still exert a large force because of its kinetic energy.

Bernoulli’s equation can also be used to relate fluid flow to power. Since each term in Bernoulli’s equation has units of energy per unit volume, multiplying by flow rate gives units of power.

## Key formulas
Bernoulli’s equation:
\[
P + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}
\]

For flow from a reservoir surface to an outlet with negligible resistance:
\[
P_1 + \frac{1}{2}\rho v_1^2 + \rho gh_1
=
P_2 + \frac{1}{2}\rho v_2^2 + \rho gh_2
\]

With both points at atmospheric pressure and the reservoir surface speed negligible, Torricelli’s theorem gives:
\[
v = \sqrt{2gh}
\]

For power in fluid flow, multiplying Bernoulli’s equation by volume flow rate \(\frac{\Delta V}{\Delta t}\) gives power.

## Variables and units
- \(P\): pressure, units of pascals (Pa)
- \(\rho\): density, units of kilograms per cubic meter (kg/m\(^3\))
- \(v\): fluid speed, units of meters per second (m/s)
- \(g\): acceleration due to gravity, units of meters per second squared (m/s\(^2\))
- \(h\): height, units of meters (m)
- \(\Delta V / \Delta t\): volume flow rate, units of cubic meters per second (m\(^3\)/s)
- Gauge pressure: pressure measured relative to atmospheric pressure
- Atmospheric pressure: pressure of the surrounding air

## Worked example
### Example 12.5: Calculating Pressure: A Fire Hose Nozzle
A fire hose has an inside diameter of 6.40 cm and carries a flow of 40.0 L/s. The hose starts at a gauge pressure of 0.0? The nozzle is 10.0 m above the ground and has an inside diameter of 3.00 cm. Assuming negligible resistance, find the initial water pressure at the base of the hose.

Using Bernoulli’s equation between the ground-level point and the nozzle:
\[
P_1 + \frac{1}{2}\rho v_1^2 + \rho gh_1
=
P_2 + \frac{1}{2}\rho v_2^2 + \rho gh_2
\]

First determine the speeds from the flow rate and hose areas:
\[
v_1 = \frac{\Delta V/\Delta t}{A_1}, \quad v_2 = \frac{\Delta V/\Delta t}{A_2}
\]

Using the given values yields:
\[
v_1 = 12.4\ \text{m/s}, \quad v_2 = 56.1\ \text{m/s}
\]

Taking the nozzle gauge pressure to be zero, solving Bernoulli’s equation for the initial pressure gives:
\[
P_1 = 1.25 \times 10^5\ \text{Pa}
\]

This is a gauge pressure, consistent with the fact that the nozzle pressure is very close to atmospheric pressure as the water exits into the air.

## Key concepts used
- Bernoulli’s equation relates pressure, speed, and height in fluid flow.
- Torricelli’s theorem is a special case of Bernoulli’s equation for flow from a reservoir.
- The exit speed from an opening depends on the vertical drop, not on the opening size, when resistance is negligible.
- Pressure can decrease where fluid speed increases.
- Power in fluid flow is found by multiplying energy per unit volume by volume flow rate.
- Gauge pressure is relative to atmospheric pressure.
