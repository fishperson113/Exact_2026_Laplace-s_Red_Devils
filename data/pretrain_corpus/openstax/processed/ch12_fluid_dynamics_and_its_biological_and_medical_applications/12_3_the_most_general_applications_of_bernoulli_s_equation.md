502

12 • Fluid Dynamics and Its Biological and Medical Applications

FIGURE 12.7 Measurement of fluid speed based on Bernoulli’s principle. (a) A manometer is connected to two tubes that are close together
and small enough not to disturb the flow. Tube 1 is open at the end facing the flow. A dead spot having zero speed is created there. Tube 2
has an opening on the side, and so the fluid has a speed
 across the opening; thus, pressure there drops. The difference in pressure at the
manometer is

. (b) This type of velocity measuring device is a Prandtl tube, also known as a pitot

 is proportional to

, and so

tube.

12.3 The Most General Applications of Bernoulli’s Equation

LEARNING OBJECTIVES
By the end of this section, you will be able to:
•  Calculate using Torricelli’s theorem.
•  Calculate power in fluid flow.

Torricelli’s Theorem

Figure 12.8 shows water gushing from a large tube through a dam. What is its speed as it emerges? Interestingly, if
resistance is negligible, the speed is just what it would be if the water fell a distance
reservoir; the water’s speed is independent of the size of the opening. Let us check this out. Bernoulli’s equation
must be used since the depth is not constant. We consider water flowing from the surface (point 1) to the tube’s
outlet (point 2). Bernoulli’s equation as stated in previously is

 from the surface of the

12.29

 and

 equal atmospheric pressure (

Both
reservoir.
have a pressure different from atmospheric pressure.) and subtract out of the equation, leaving

 is atmospheric pressure because it is the pressure at the top of the
 must be atmospheric pressure, since the emerging water is surrounded by the atmosphere and cannot

Solving this equation for

, noting that the density

 cancels (because the fluid is incompressible), yields

We let

; the equation then becomes

12.30

12.31

12.32

 is the height dropped by the water. This is simply a kinematic equation for any object falling a distance

where
with negligible resistance. In fluids, this last equation is called Torricelli’s theorem. Note that the result is
independent of the velocity’s direction, just as we found when applying conservation of energy to falling objects.

Access for free at openstax.org

12.3 • The Most General Applications of Bernoulli’s Equation

503

FIGURE 12.8 (a) Water gushes from the base of the Studen Kladenetz dam in Bulgaria. (credit: Kiril Kapustin;
http://www.ImagesFromBulgaria.com) (b) In the absence of significant resistance, water flows from the reservoir with the same speed it
would have if it fell the distance

 without friction. This is an example of Torricelli’s theorem.

FIGURE 12.9 Pressure in the nozzle of this fire hose is less than at ground level for two reasons: the water has to go uphill to get to the
nozzle, and speed increases in the nozzle. In spite of its lowered pressure, the water can exert a large force on anything it strikes, by virtue
of its kinetic energy. Pressure in the water stream becomes equal to atmospheric pressure once it emerges into the air.

All preceding applications of Bernoulli’s equation involved simplifying conditions, such as constant height or
constant pressure. The next example is a more general application of Bernoulli’s equation in which pressure,

504

12 • Fluid Dynamics and Its Biological and Medical Applications

velocity, and height all change. (See Figure 12.9.)

EXAMPLE  12.5

Calculating Pressure: A Fire Hose Nozzle
Fire hoses used in major structure fires have inside diameters of 6.40 cm. Suppose such a hose carries a flow of
40.0 L/s starting at a gauge pressure of
inside diameter of 3.00 cm. Assuming negligible resistance, what is the initial water pressure at the base of the
hose?

. The hose goes 10.0 m up a ladder to a nozzle having an

Strategy

Here we must use Bernoulli’s equation to solve for the pressure, since depth is not constant.

Solution

Bernoulli’s equation states

12.33

where the subscripts 1 and 2 refer to the initial conditions at ground level and the final conditions inside the nozzle,
respectively. We must first find the speeds

 , we get

. Since

 and

Similarly, we find

12.34

12.35

(This rather large speed is helpful in reaching the fire.) Now, taking

 to be zero, we solve Bernoulli’s equation for

:

In the proposed solution,

, so

12.36

12.37

Discussion

This value is a gauge pressure, since the initial pressure was given as a gauge pressure. Thus the nozzle pressure is
very close to atmospheric pressure, as it must because the water exits into the atmosphere without changes in its
conditions.

Power in Fluid Flow

Power is the rate at which work is done or energy in any form is used or supplied. To see the relationship of power to
fluid flow, consider Bernoulli’s equation:

12.38

All three terms have units of energy per unit volume, as discussed in the previous section. Now, considering units, if
we multiply energy per unit volume by flow rate (volume per unit time), we get units of power. That is,
. This means that if we multiply Bernoulli’s equation by flow rate

, we get power. In equation

form, this is

Access for free at openstax.org
