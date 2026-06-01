12.4 • Viscosity and Laminar Flow; Poiseuille’s Law 505
12.39
Each term has a clear physical meaning. For example, is the power supplied to a fluid, perhaps by a pump, to
give it its pressure . Similarly, is the power supplied to a fluid to give it its kinetic energy. And is the
power going to gravitational potential energy.
MAKING CONNECTIONS: POWER
Power is defined as the rate of energy transferred, or . Fluid flow involves several types of power. Each type
of power is identified with a specific type of energy being expended or changed in form.
EXAMPLE 12.6
Calculating Power in a Moving Fluid
Suppose the fire hose in the previous example is fed by a pump that receives water through a hose with a 6.40-cm
diameter coming from a hydrant with a pressure of . What power does the pump supply to the
water?
Strategy
Here we must consider energy forms as well as how they relate to fluid flow. Since the input and output hoses have
the same diameters and are at the same height, the pump does not change the speed of the water nor its height,
and so the water’s kinetic energy and gravitational potential energy are unchanged. That means the pump only
supplies power to increase water pressure by (from to ).
Solution
As discussed above, the power associated with pressure is
12.40
Discussion
Such a substantial amount of power requires a large pump, such as is found on some fire trucks. (This kilowatt value
converts to about 50 hp.) The pump in this example increases only the water’s pressure. If a pump—such as the
heart—directly increases velocity and height as well as pressure, we would have to calculate all three terms to find
the power it supplies.
12.4 Viscosity and Laminar Flow; Poiseuille’s Law
LEARNING OBJECTIVES
By the end of this section, you will be able to:
• Define laminar flow and turbulent flow.
• Explain what viscosity is.
• Calculate flow and resistance with Poiseuille’s law.
• Explain how pressure drops due to resistance.
Laminar Flow and Viscosity
When you pour yourself a glass of juice, the liquid flows freely and quickly. But when you pour syrup on your
pancakes, that liquid flows slowly and sticks to the pitcher. The difference is fluid friction, both within the fluid itself
and between the fluid and its surroundings. We call this property of fluids viscosity. Juice has low viscosity, whereas

506 12 • Fluid Dynamics and Its Biological and Medical Applications
syrup has high viscosity. In the previous sections we have considered ideal fluids with little or no viscosity. In this
section, we will investigate what factors, including viscosity, affect the rate of fluid flow.
The precise definition of viscosity is based on laminar, or nonturbulent, flow. Before we can define viscosity, then,
we need to define laminar flow and turbulent flow. Figure 12.10 shows both types of flow. Laminar flow is
characterized by the smooth flow of the fluid in layers that do not mix. Turbulent flow, or turbulence, is
characterized by eddies and swirls that mix layers of fluid together.
FIGURE 12.10 Smoke rises smoothly for a while and then begins to form swirls and eddies. The smooth flow is called laminar flow,
whereas the swirls and eddies typify turbulent flow. If you watch the smoke (being careful not to breathe on it), you will notice that it rises
more rapidly when flowing smoothly than after it becomes turbulent, implying that turbulence poses more resistance to flow. (credit:
Creativity103)
Figure 12.11 shows schematically how laminar and turbulent flow differ. Layers flow without mixing when flow is
laminar. When there is turbulence, the layers mix, and there are significant velocities in directions other than the
overall direction of flow. The lines that are shown in many illustrations are the paths followed by small volumes of
fluids. These are called streamlines. Streamlines are smooth and continuous when flow is laminar, but break up and
mix when flow is turbulent. Turbulence has two main causes. First, any obstruction or sharp corner, such as in a
faucet, creates turbulence by imparting velocities perpendicular to the flow. Second, high speeds cause turbulence.
The drag both between adjacent layers of fluid and between the fluid and its surroundings forms swirls and eddies,
if the speed is great enough. We shall concentrate on laminar flow for the remainder of this section, leaving certain
aspects of turbulence for later sections.
FIGURE 12.11 (a) Laminar flow occurs in layers without mixing. Notice that viscosity causes drag between layers as well as with the fixed
surface. (b) An obstruction in the vessel produces turbulence. Turbulent flow mixes the fluid. There is more interaction, greater heating, and
more resistance than in laminar flow.
Access for free at openstax.org

12.4 • Viscosity and Laminar Flow; Poiseuille’s Law 507
MAKING CONNECTIONS: TAKE-HOME EXPERIMENT: GO DOWN TO THE RIVER
Try dropping simultaneously two sticks into a flowing river, one near the edge of the river and one near the
middle. Which one travels faster? Why?
Figure 12.12 shows how viscosity is measured for a fluid. Two parallel plates have the specific fluid between them.
The bottom plate is held fixed, while the top plate is moved to the right, dragging fluid with it. The layer (or lamina)
of fluid in contact with either plate does not move relative to the plate, and so the top layer moves at while the
bottom layer remains at rest. Each successive layer from the top down exerts a force on the one below it, trying to
drag it along, producing a continuous variation in speed from to 0 as shown. Care is taken to insure that the flow is
laminar; that is, the layers do not mix. The motion in Figure 12.12 is like a continuous shearing motion. Fluids have
zero shear strength, but the rate at which they are sheared is related to the same geometrical factors and as is
shear deformation for solids.
FIGURE 12.12 The graphic shows laminar flow of fluid between two plates of area . The bottom plate is fixed. When the top plate is
pushed to the right, it drags the fluid along with it.
A force is required to keep the top plate in Figure 12.12 moving at a constant velocity , and experiments have
shown that this force depends on four factors. First, is directly proportional to (until the speed is so high that
turbulence occurs—then a much larger force is needed, and it has a more complicated dependence on ). Second,
is proportional to the area of the plate. This relationship seems reasonable, since is directly proportional to the
amount of fluid being moved. Third, is inversely proportional to the distance between the plates . This
relationship is also reasonable; is like a lever arm, and the greater the lever arm, the less force that is needed.
Fourth, is directly proportional to the coefficient of viscosity, . The greater the viscosity, the greater the force
required. These dependencies are combined into the equation
12.41
which gives us a working definition of fluid viscosity . Solving for gives
12.42
which defines viscosity in terms of how it is measured. The SI unit of viscosity is
. Table 12.1 lists the coefficients of viscosity for various fluids.
Viscosity varies from one fluid to another by several orders of magnitude. As you might expect, the viscosities of
gases are much less than those of liquids, and these viscosities are often temperature dependent. The viscosity of
blood can be reduced by aspirin consumption, allowing it to flow more easily around the body. (When used over the
long term in low doses, aspirin can help prevent heart attacks, and reduce the risk of blood clotting.)
Laminar Flow Confined to Tubes—Poiseuille’s Law
What causes flow? The answer, not surprisingly, is pressure difference. In fact, there is a very simple relationship
between horizontal flow and pressure. Flow rate is in the direction from high to low pressure. The greater the
pressure differential between two points, the greater the flow rate. This relationship can be stated as

508 12 • Fluid Dynamics and Its Biological and Medical Applications
12.43
where and are the pressures at two points, such as at either end of a tube, and is the resistance to flow.
The resistance includes everything, except pressure, that affects flow rate. For example, is greater for a long
tube than for a short one. The greater the viscosity of a fluid, the greater the value of . Turbulence greatly
increases , whereas increasing the diameter of a tube decreases .
If viscosity is zero, the fluid is frictionless and the resistance to flow is also zero. Comparing frictionless flow in a
tube to viscous flow, as in Figure 12.13, we see that for a viscous fluid, speed is greatest at midstream because of
drag at the boundaries. We can see the effect of viscosity in a Bunsen burner flame, even though the viscosity of
natural gas is small.
The resistance to laminar flow of an incompressible fluid having viscosity through a horizontal tube of uniform
radius and length , such as the one in Figure 12.14, is given by
12.44
This equation is called Poiseuille’s law for resistance after the French scientist J. L. Poiseuille (1799–1869), who
derived it in an attempt to understand the flow of blood, an often turbulent fluid.
FIGURE 12.13 (a) If fluid flow in a tube has negligible resistance, the speed is the same all across the tube. (b) When a viscous fluid flows
through a tube, its speed at the walls is zero, increasing steadily to its maximum at the center of the tube. (c) The shape of the Bunsen
burner flame is due to the velocity profile across the tube. (credit: Jason Woodhead)
Let us examine Poiseuille’s expression for to see if it makes good intuitive sense. We see that resistance is directly
proportional to both fluid viscosity and the length of a tube. After all, both of these directly affect the amount of
friction encountered—the greater either is, the greater the resistance and the smaller the flow. The radius of a tube
affects the resistance, which again makes sense, because the greater the radius, the greater the flow (all other
factors remaining the same). But it is surprising that is raised to the fourth power in Poiseuille’s law. This exponent
means that any change in the radius of a tube has a very large effect on resistance. For example, doubling the radius
of a tube decreases resistance by a factor of .
Taken together, and give the following expression for flow rate:
12.45
This equation describes laminar flow through a tube. It is sometimes called Poiseuille’s law for laminar flow, or
simply Poiseuille’s law.
Access for free at openstax.org

12.4 • Viscosity and Laminar Flow; Poiseuille’s Law 509
EXAMPLE 12.7
Using Flow Rate: Plaque Deposits Reduce Blood Flow
Suppose the flow rate of blood in a coronary artery has been reduced to half its normal value by plaque deposits. By
what factor has the radius of the artery been reduced, assuming no turbulence occurs?
Strategy
Assuming laminar flow, Poiseuille’s law states that
12.46
We need to compare the artery radius before and after the flow rate reduction.
Solution
With a constant pressure difference assumed and the same length and viscosity, along the artery we have
12.47
| So, given that  | , we find that                             | .   |     |
| --------------- | ------------------------------------------ | --- | --- |
| Therefore,      | , a decrease in the artery radius of 16%.  |     |     |
Discussion
This decrease in radius is surprisingly small for this situation. To restore the blood flow in spite of this buildup would
require an increase in the pressure difference   of a factor of two, with subsequent strain on the heart.
|     | Fluid  | Temperature (ºC)  | Viscosity  |
| --- | ------ | ----------------- | ---------- |
Gases
|     |     | 0   | 0.0171  |
| --- | --- | --- | ------- |
|     |     | 20  | 0.0181  |
Air
|     |                 | 40   | 0.0190   |
| --- | --------------- | ---- | -------- |
|     |                 | 100  | 0.0218   |
|     | Ammonia         | 20   | 0.00974  |
|     | Carbon dioxide  | 20   | 0.0147   |
|     | Helium          | 20   | 0.0196   |
|     | Hydrogen        | 0    | 0.0090   |
|     | Mercury         | 20   | 0.0450   |
|     | Oxygen          | 20   | 0.0203   |
TABLE 12.1 Coefficients of Viscosity of Various Fluids

510 12 • Fluid Dynamics and Its Biological and Medical Applications
| Fluid  | Temperature (ºC)  | Viscosity  |
| ------ | ----------------- | ---------- |
| Steam  | 100               | 0.0130     |
Liquids
|        | 0    | 1.792   |
| ------ | ---- | ------- |
|        | 20   | 1.002   |
| Water  | 37   | 0.6947  |
|        | 40   | 0.653   |
|        | 100  | 0.282   |
|        | 20   | 3.015   |
1
Whole blood
|     | 37  | 2.084  |
| --- | --- | ------ |
|     | 20  | 1.810  |
2
Blood plasma
|                      | 37  | 1.257       |
| -------------------- | --- | ----------- |
| Ethyl alcohol        | 20  | 1.20        |
| Methanol             | 20  | 0.584       |
| Oil (heavy machine)  | 20  | 660         |
| Oil (motor, SAE 10)  | 30  | 200         |
| Oil (olive)          | 20  | 138         |
| Glycerin             | 20  | 1500        |
| Honey                | 20  | 2000–10000  |
| Maple Syrup          | 20  | 2000–3000   |
| Milk                 | 20  | 3.0         |
| Oil (Corn)           | 20  | 65          |
TABLE 12.1 Coefficients of Viscosity of Various Fluids
The circulatory system provides many examples of Poiseuille’s law in action—with blood flow regulated by changes
in vessel size and blood pressure. Blood vessels are not rigid but elastic. Adjustments to blood flow are primarily
made by varying the size of the vessels, since the resistance is so sensitive to the radius. During vigorous exercise,
blood vessels are selectively dilated to important muscles and organs and blood pressure increases. This creates
both greater overall blood flow and increased flow to specific areas. Conversely, decreases in vessel radii, perhaps
1  The ratios of the viscosities of blood to water are nearly constant between 0°C and 37°C.
2  See note on Whole Blood.
Access for free at openstax.org

12.4 • Viscosity and Laminar Flow; Poiseuille’s Law 511
from plaques in the arteries, can greatly reduce blood flow. If a vessel’s radius is reduced by only 5% (to 0.95 of its
original value), the flow rate is reduced to about of its original value. A 19% decrease in flow is
caused by a 5% decrease in radius. The body may compensate by increasing blood pressure by 19%, but this
presents hazards to the heart and any vessel that has weakened walls. Another example comes from automobile
engine oil. If you have a car with an oil pressure gauge, you may notice that oil pressure is high when the engine is
cold. Motor oil has greater viscosity when cold than when warm, and so pressure must be greater to pump the same
amount of cold oil.
FIGURE 12.14 Poiseuille’s law applies to laminar flow of an incompressible fluid of viscosity through a tube of length and radius . The
direction of flow is from greater to lower pressure. Flow rate is directly proportional to the pressure difference , and inversely
proportional to the length of the tube and viscosity of the fluid. Flow rate increases with , the fourth power of the radius.
EXAMPLE 12.8
What Pressure Produces This Flow Rate?
An intravenous (IV) system is supplying saline solution to a patient at the rate of through a needle of
radius 0.150 mm and length 2.50 cm. What pressure is needed at the entrance of the needle to cause this flow,
assuming the viscosity of the saline solution to be the same as that of water? The gauge pressure of the blood in the
patient’s vein is 8.00 mm Hg. (Assume that the temperature is .)
Strategy
Assuming laminar flow, Poiseuille’s law applies. This is given by
12.48
where is the pressure at the entrance of the needle and is the pressure in the vein. The only unknown is .
Solution
Solving for yields
12.49
is given as 8.00 mm Hg, which converts to . Substituting this and the other known values
yields
12.50
Discussion
This pressure could be supplied by an IV bottle with the surface of the saline solution 1.61 m above the entrance to
the needle (this is left for you to solve in this chapter’s Problems and Exercises), assuming that there is negligible
pressure drop in the tubing leading to the needle.

512 12 • Fluid Dynamics and Its Biological and Medical Applications
Flow and Resistance as Causes of Pressure Drops
You may have noticed that water pressure in your home might be lower than normal on hot summer days when
there is more use. This pressure drop occurs in the water main before it reaches your home. Let us consider flow
through the water main as illustrated in Figure 12.15. We can understand why the pressure to the home drops
during times of heavy use by rearranging
12.51
to
12.52
where, in this case, is the pressure at the water works and is the resistance of the water main. During times of
heavy use, the flow rate is large. This means that must also be large. Thus must decrease. It is
correct to think of flow and resistance as causing the pressure to drop from to . is valid for
both laminar and turbulent flows.
FIGURE 12.15 During times of heavy use, there is a significant pressure drop in a water main, and supplied to users is significantly less
than created at the water works. If the flow is very small, then the pressure drop is negligible, and .
We can use to analyze pressure drops occurring in more complex systems in which the tube radius
is not the same everywhere. Resistance will be much greater in narrow places, such as an obstructed coronary
artery. For a given flow rate , the pressure drop will be greatest where the tube is most narrow. This is how water
faucets control flow. Additionally, is greatly increased by turbulence, and a constriction that creates turbulence
greatly reduces the pressure downstream. Plaque in an artery reduces pressure and hence flow, both by its
resistance and by the turbulence it creates.
Figure 12.16 is a schematic of the human circulatory system, showing average blood pressures in its major parts for
an adult at rest. Pressure created by the heart’s two pumps, the right and left ventricles, is reduced by the
resistance of the blood vessels as the blood flows through them. The left ventricle increases arterial blood pressure
that drives the flow of blood through all parts of the body except the lungs. The right ventricle receives the lower
pressure blood from two major veins and pumps it through the lungs for gas exchange with atmospheric gases – the
disposal of carbon dioxide from the blood and the replenishment of oxygen. Only one major organ is shown
schematically, with typical branching of arteries to ever smaller vessels, the smallest of which are the capillaries,
and rejoining of small veins into larger ones. Similar branching takes place in a variety of organs in the body, and the
circulatory system has considerable flexibility in flow regulation to these organs by the dilation and constriction of
the arteries leading to them and the capillaries within them. The sensitivity of flow to tube radius makes this
flexibility possible over a large range of flow rates.
Access for free at openstax.org
