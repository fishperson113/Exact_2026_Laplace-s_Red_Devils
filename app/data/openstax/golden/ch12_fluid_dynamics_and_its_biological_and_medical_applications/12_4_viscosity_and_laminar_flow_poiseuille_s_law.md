# 12.4 Viscosity and Laminar Flow; Poiseuille’s Law

Source: OpenStax College Physics 2e, Chapter 12, Section 12.4

## Concept explanation
Viscosity is the property of a fluid that represents fluid friction, both within the fluid itself and between the fluid and its surroundings. Juice has low viscosity, while syrup has high viscosity.

Viscosity is defined in the context of laminar flow. Laminar flow is smooth flow in layers that do not mix. Turbulent flow is characterized by eddies and swirls that mix layers of fluid together. Streamlines are smooth and continuous for laminar flow, but break up and mix when flow is turbulent.

Turbulence can be caused by:
- an obstruction or sharp corner that gives the fluid velocities perpendicular to the flow
- high speeds, which increase drag between layers and can produce swirls and eddies

To measure viscosity, a fluid is placed between two parallel plates. The bottom plate is fixed and the top plate moves, dragging the fluid. In laminar flow, the layer of fluid touching each plate does not move relative to that plate. The speed varies continuously from the top plate speed to zero at the bottom plate.

The force required to keep the top plate moving at constant velocity depends on:
- the velocity of the plate
- the area of the plate
- the separation distance between the plates
- the coefficient of viscosity

For fluid flow in a tube, flow occurs from high pressure to low pressure. The greater the pressure difference, the greater the flow rate. Resistance to flow includes everything except pressure that affects flow rate. Resistance is greater for a long tube, greater for a more viscous fluid, greater with turbulence, and smaller for a larger tube diameter.

For a horizontal tube of uniform radius and length, Poiseuille’s law gives the resistance to laminar flow. Combining this with the pressure-flow relation gives the flow rate for laminar flow through a tube. The strong dependence on radius means that small changes in tube radius cause large changes in resistance and flow rate. For example, doubling the radius decreases resistance by a factor of 16.

This behavior is important in blood flow. Plaque deposits can reduce artery radius and greatly reduce blood flow. The circulatory system regulates flow by changing vessel size and blood pressure. During vigorous exercise, vessels dilate to increase flow to important muscles and organs. Narrowing of vessels can reduce blood flow and increase strain on the heart.

## Key formulas
\[
F = \eta A \frac{v}{d}
\]

\[
\eta = \frac{F d}{A v}
\]

\[
\Delta P = Q R
\]

\[
R = \frac{8 \eta l}{\pi r^4}
\]

\[
Q = \frac{\pi r^4 \Delta P}{8 \eta l}
\]

For the pressure-drop form:
\[
\Delta P = P_1 - P_2
\]

For laminar flow in a tube:
\[
Q \propto r^4
\]

## Variables and units
- \(F\): force required to move the top plate
- \(\eta\): coefficient of viscosity
- \(A\): area of the plate
- \(v\): speed of the moving plate
- \(d\): distance between the plates
- \(\Delta P\): pressure difference
- \(Q\): flow rate
- \(R\): resistance to flow
- \(P_1, P_2\): pressures at two points
- \(l\): length of tube
- \(r\): radius of tube

SI unit of viscosity:
\[
\mathrm{N \cdot s/m^2}
\]
equivalently
\[
\mathrm{Pa \cdot s}
\]

## Worked example
### Example 12.7: Using Flow Rate: Plaque Deposits Reduce Blood Flow
Suppose the flow rate of blood in a coronary artery has been reduced to half its normal value by plaque deposits. By what factor has the radius of the artery been reduced, assuming no turbulence occurs?

Assuming laminar flow and constant pressure difference, length, and viscosity:
\[
Q \propto r^4
\]

So,
\[
\frac{Q_{\text{new}}}{Q_{\text{old}}} = \left(\frac{r_{\text{new}}}{r_{\text{old}}}\right)^4
\]

Given:
\[
\frac{Q_{\text{new}}}{Q_{\text{old}}} = \frac{1}{2}
\]

Therefore,
\[
\frac{r_{\text{new}}}{r_{\text{old}}} = \left(\frac{1}{2}\right)^{1/4} \approx 0.84
\]

So the radius is reduced to about \(0.84\) of its original value, a decrease of about 16%.

### Example 12.8: What Pressure Produces This Flow Rate?
An intravenous (IV) system supplies saline solution to a patient at the rate of through a needle of radius \(0.150\ \text{mm}\) and length \(2.50\ \text{cm}\). What pressure is needed at the entrance of the needle to cause this flow, assuming the viscosity of the saline solution is the same as that of water? The gauge pressure of the blood in the patient’s vein is \(8.00\ \text{mm Hg}\). Assume the temperature is \(20^\circ\text{C}\).

Using Poiseuille’s law:
\[
Q = \frac{\pi r^4 (P_1 - P_2)}{8 \eta l}
\]

Solving for the entrance pressure:
\[
P_1 = P_2 + \frac{8 \eta l Q}{\pi r^4}
\]

With \(P_2 = 8.00\ \text{mm Hg}\) and the given values substituted, the required pressure is:
\[
P_1 = 1.61 \times 10^4\ \text{Pa}
\]

This pressure could be supplied by an IV bottle with the surface of the saline solution \(1.61\ \text{m}\) above the entrance to the needle, assuming negligible pressure drop in the tubing.

## Key concepts used
- viscosity
- laminar flow
- turbulent flow
- streamlines
- fluid resistance
- pressure difference
- Poiseuille’s law
- dependence on tube radius \(r^4\)
- blood flow through arteries and veins
- pressure drops due to resistance
- effect of plaque deposits on flow
