12.2 • Bernoulli’s Equation

497

5.0 L/min, the speed of blood in the capillaries is about 0.33 mm/s. Given that the average diameter of a capillary is

, calculate the number of capillaries in the blood circulatory system.

Strategy

We can use
continuity to calculate the number of capillaries as all of the other variables are known.

 to calculate the speed of flow in the aorta and then use the general form of the equation of

Solution for (a)

The flow rate is given by

 or

 for a cylindrical vessel.

Substituting the known values (converted to units of meters and seconds) gives

12.14

Solution for (b)

Using

, assigning the subscript 1 to the aorta and 2 to the capillaries, and solving for

 (the

number of capillaries) gives

. Converting all quantities to units of meters and seconds and substituting

into the equation above gives

Discussion

12.15

Note that the speed of flow in the capillaries is considerably reduced relative to the speed in the aorta due to the
significant increase in the total cross-sectional area at the capillaries. This low speed is to allow sufficient time for
effective exchange to occur although it is equally important for the flow not to become stationary in order to avoid
the possibility of clotting. Does this large number of capillaries in the body seem reasonable? In active muscle, one
finds about 200 capillaries per
about

 per 1 kg of muscle. For 20 kg of muscle, this amounts to

 capillaries.

, or about

12.2 Bernoulli’s Equation

LEARNING OBJECTIVES
By the end of this section, you will be able to:

•  Explain the terms in Bernoulli’s equation.
•  Explain how Bernoulli’s equation is related to conservation of energy.
•  Explain how to derive Bernoulli’s principle from Bernoulli’s equation.
•  Calculate with Bernoulli’s principle.
•  List some applications of Bernoulli’s principle.

When a fluid flows into a narrower channel, its speed increases. That means its kinetic energy also increases. Where
does that change in kinetic energy come from? The increased kinetic energy comes from the net work done on the
fluid to push it into the channel and the work done on the fluid by the gravitational force, if the fluid changes vertical
position. Recall the work-energy theorem,

12.16

There is a pressure difference when the channel narrows. This pressure difference results in a net force on the fluid:
recall that pressure times area equals force. The net work done increases the fluid’s kinetic energy. As a result, the
pressure will drop in a rapidly-moving fluid, whether or not the fluid is confined to a tube.

There are a number of common examples of pressure dropping in rapidly-moving fluids. Shower curtains have a

498

12 • Fluid Dynamics and Its Biological and Medical Applications

disagreeable habit of bulging into the shower stall when the shower is on. The high-velocity stream of water and air
creates a region of lower pressure inside the shower, and standard atmospheric pressure on the other side. The
pressure difference results in a net force inward pushing the curtain in. You may also have noticed that when
passing a truck on the highway, your car tends to veer toward it. The reason is the same—the high velocity of the air
between the car and the truck creates a region of lower pressure, and the vehicles are pushed together by greater
pressure on the outside. (See Figure 12.4.) This effect was observed as far back as the mid-1800s, when it was
found that trains passing in opposite directions tipped precariously toward one another.

FIGURE 12.4 An overhead view of a car passing a truck on a highway. Air passing between the vehicles flows in a narrower channel and
must increase its speed (
). Greater pressure on the
 is greater than
outside pushes the car and truck together.

), causing the pressure between them to drop (

 is less than

MAKING CONNECTIONS: TAKE-HOME INVESTIGATION WITH A SHEET OF PAPER

Hold the short edge of a sheet of paper parallel to your mouth with one hand on each side of your mouth. The
page should slant downward over your hands. Blow over the top of the page. Describe what happens and explain
the reason for this behavior.

Bernoulli’s Equation

The relationship between pressure and velocity in fluids is described quantitatively by Bernoulli’s equation, named
after its discoverer, the Swiss scientist Daniel Bernoulli (1700–1782). Bernoulli’s equation states that for an
incompressible, frictionless fluid, the following sum is constant:

12.17

 is the absolute pressure,

where
reference point, and
quantities in the sum may change, but the total remains constant. Let the subscripts 1 and 2 refer to any two points
along the path that the bit of fluid follows; Bernoulli’s equation becomes

 is the acceleration due to gravity. If we follow a small volume of fluid along its path, various

 is the velocity of the fluid,

 is the height above some

 is the fluid density,

12.18

Bernoulli’s equation is a form of the conservation of energy principle. Note that the second and third terms are the
kinetic and potential energy with
volume. We can prove this for the second term by substituting

. In fact, each term in the equation has units of energy per unit

 into it and gathering terms:

 replaced by

 is the kinetic energy per unit volume. Making the same substitution into the third term in the equation, we

So

find

12.19

Access for free at openstax.org

12.2 • Bernoulli’s Equation

499

12.20

 is the gravitational potential energy per unit volume. Note that pressure

so
volume, too. Since
energy per unit volume. Bernoulli’s equation is, in fact, just a convenient statement of conservation of energy for an
incompressible fluid in the absence of friction.

 has units of energy per unit
, or

. If we multiply these by m/m, we obtain

, its units are

MAKING CONNECTIONS: CONSERVATION OF ENERGY

Conservation of energy applied to fluid flow produces Bernoulli’s equation. The net work done by the fluid’s
pressure results in changes in the fluid’s

 per unit volume. If other forms of energy are involved in

 and

fluid flow, Bernoulli’s equation can be modified to take these forms into account. Such forms of energy include
thermal energy dissipated because of fluid viscosity.

The general form of Bernoulli’s equation has three terms in it, and it is broadly applicable. To understand it better,
we will look at a number of specific situations that simplify and illustrate its use and meaning.

Bernoulli’s Equation for Static Fluids

Let us first consider the very simple situation where the fluid is static—that is,
that case is

. Bernoulli’s equation in

12.21

We can further simplify the equation by taking
often have done for other situations involving the gravitational force, and take all other heights to be relative to this).
In that case, we get

 (we can always choose some height to be zero, just as we

12.22

This equation tells us that, in static fluids, pressure increases with depth. As we go from point 1 to point 2 in the
fluid, the depth increases by
case,

, and consequently,
 is zero at the top of the fluid, and we get the familiar relationship

 is greater than

 by an amount

. (Recall that

. In the very simplest

) Bernoulli’s equation includes the fact that the pressure due to the weight of a fluid is

 and
. Although

we introduce Bernoulli’s equation for fluid flow, it includes much of what we studied for static fluids in the preceding
chapter.

Bernoulli’s Principle—Bernoulli’s Equation at Constant Depth

Another important situation is one in which the fluid moves but its depth is constant—that is,
condition, Bernoulli’s equation becomes

. Under that

12.23

Situations in which fluid flows at a constant depth are so important that this equation is often called Bernoulli’s
principle. It is Bernoulli’s equation for fluids at constant depth. (Note again that this applies to a small volume of
fluid as we follow it along its path.) As we have just discussed, pressure drops as speed increases in a moving fluid.
We can see this from Bernoulli’s principle. For example, if
less than

 for the equality to hold.

 in the equation, then

 is greater than

 must be

EXAMPLE  12.4

Calculating Pressure: Pressure Drops as a Fluid Speeds Up
In Example 12.2, we found that the speed of water in a hose increased from 1.96 m/s to 25.5 m/s going from the
hose to the nozzle. Calculate the pressure in the hose, given that the absolute pressure in the nozzle is
 (atmospheric, as it must be) and assuming level, frictionless flow.

500

12 • Fluid Dynamics and Its Biological and Medical Applications

Strategy

Level flow means constant depth, so Bernoulli’s principle applies. We use the subscript 1 for values in the hose and
2 for those in the nozzle. We are thus asked to find

.

Solution

Solving Bernoulli’s principle for

 yields

Substituting known values,

Discussion

12.24

12.25

 is greater in the nozzle. The

This absolute pressure in the hose is greater than in the nozzle, as expected since
pressure
conditions.

 in the nozzle must be atmospheric since it emerges into the atmosphere without other changes in

Applications of Bernoulli’s Principle

There are a number of devices and situations in which fluid flows at a constant height and, thus, can be analyzed
with Bernoulli’s principle.

Entrainment
People have long put the Bernoulli principle to work by using reduced pressure in high-velocity fluids to move things
about. With a higher pressure on the outside, the high-velocity fluid forces other fluids into the stream. This process
is called entrainment. Entrainment devices have been in use since ancient times, particularly as pumps to raise
water small heights, as in draining swamps, fields, or other low-lying areas. Some other devices that use the concept
of entrainment are shown in Figure 12.5.

FIGURE 12.5 Examples of entrainment devices that use increased fluid speed to create low pressures, which then entrain one fluid into
another. (a) A Bunsen burner uses an adjustable gas nozzle, entraining air for proper combustion. (b) An atomizer uses a squeeze bulb to
create a jet of air that entrains drops of perfume. Paint sprayers and carburetors use very similar techniques to move their respective
liquids. (c) A common aspirator uses a high-speed stream of water to create a region of lower pressure. Aspirators may be used as suction
pumps in dental and surgical situations or for draining a flooded basement or producing a reduced pressure in a vessel. (d) The chimney of
a water heater is designed to entrain air into the pipe leading through the ceiling.

Wings and Sails
The airplane wing is a beautiful example of Bernoulli’s principle in action. Figure 12.6(a) shows the characteristic
shape of a wing. The wing is tilted upward at a small angle and the upper surface is longer, causing air to flow faster
over it. The pressure on top of the wing is therefore reduced, creating a net upward force or lift. (Wings can also gain
lift by pushing air downward, utilizing the conservation of momentum principle. The deflected air molecules result in
an upward force on the wing — Newton’s third law.) Sails also have the characteristic shape of a wing. (See Figure
.
12.6(b).) The pressure on the front side of the sail,

, is lower than the pressure on the back of the sail,

Access for free at openstax.org

12.2 • Bernoulli’s Equation

501

This results in a forward force and even allows you to sail into the wind.

MAKING CONNECTIONS: TAKE-HOME INVESTIGATION WITH TWO STRIPS OF
PAPER

For a good illustration of Bernoulli’s principle, make two strips of paper, each about 15 cm long and 4 cm wide.
Hold the small end of one strip up to your lips and let it drape over your finger. Blow across the paper. What
happens? Now hold two strips of paper up to your lips, separated by your fingers. Blow between the strips. What
happens?

Velocity measurement
Figure 12.7 shows two devices that measure fluid velocity based on Bernoulli’s principle. The manometer in Figure
12.7(a) is connected to two tubes that are small enough not to appreciably disturb the flow. The tube facing the
oncoming fluid creates a dead spot having zero velocity (
velocity

. This means that Bernoulli’s principle as stated in

) in front of it, while fluid passing the other tube has

 becomes

12.26

FIGURE 12.6 (a) The Bernoulli principle helps explain lift generated by a wing. (b) Sails use the same technique to generate part of their
thrust.

Thus pressure

 over the second opening is reduced by

, and so the fluid in the manometer rises by

 on the

side connected to the second opening, where

(Recall that the symbol

 means “proportional to.”) Solving for

, we see that

12.27

12.28

Figure 12.7(b) shows a version of this device that is in common use for measuring various fluid velocities; such
devices are frequently used as air speed indicators in aircraft.
