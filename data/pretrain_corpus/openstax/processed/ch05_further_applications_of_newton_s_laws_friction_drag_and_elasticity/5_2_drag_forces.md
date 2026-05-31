206

5 • Further Applications of Newton's Laws: Friction, Drag, and Elasticity

FIGURE 5.6 The tip of a probe is deformed sideways by frictional force as the probe is dragged across a surface. Measurements of how the
force varies for different materials are yielding fundamental insights into the atomic nature of friction.

PHET EXPLORATIONS

Forces and Motion
Explore the forces at work when you try to push a filing cabinet. Create an applied force and see the resulting friction
force and total force acting on the cabinet. Charts show the forces, position, velocity, and acceleration vs. time. Draw
a free-body diagram of all the forces (including gravitational and normal forces).

Access multimedia content (http://openstax.org/books/college-physics-2e/pages/5-1-friction)

5.2 Drag Forces

LEARNING OBJECTIVES
By the end of this section, you will be able to:
•  Express mathematically the drag force.
•  Discuss the applications of drag force.
•  Define terminal velocity.
•  Determine the terminal velocity given mass.

Another interesting force in everyday life is the force of drag on an object when it is moving in a fluid (either a gas or
a liquid). You feel the drag force when you move your hand through water. You might also feel it if you move your
hand during a strong wind. The faster you move your hand, the harder it is to move. You feel a smaller drag force
when you tilt your hand so only the side goes through the air—you have decreased the area of your hand that faces
the direction of motion. Like friction, the drag force always opposes the motion of an object. Unlike simple friction,
the drag force is proportional to some function of the velocity of the object in that fluid. This functionality is
complicated and depends upon the shape of the object, its size, its velocity, and the fluid it is in. For most large
objects such as bicyclists, cars, and baseballs not moving too slowly, the magnitude of the drag force
be proportional to the square of the speed of the object. We can write this relationship mathematically as
When taking into account other factors, this relationship becomes

 is found to
.

5.13

 is the drag coefficient,

where
that density is mass per unit volume.) This equation can also be written in a more generalized fashion as
where

 is the area of the object facing the fluid, and

. We have set the exponent for these equations as 2 because, when an

 is the density of the fluid. (Recall

 is a constant equivalent to

,

Access for free at openstax.org

5.2 • Drag Forces

207

object is moving at high velocity through air, the magnitude of the drag force is proportional to the square of the
speed. As we shall see in a few pages on fluid dynamics, for small particles moving at low speeds in a fluid, the
exponent is equal to 1.

DRAG FORCE

Drag force

 is found to be proportional to the square of the speed of the object. Mathematically

5.14

5.15

where

 is the drag coefficient,

 is the area of the object facing the fluid, and

 is the density of the fluid.

Athletes as well as car designers seek to reduce the drag force to lower their race times. (See Figure 5.7).
“Aerodynamic” shaping of an automobile can reduce the drag force and so increase a car’s gas mileage.

FIGURE 5.7 From racing cars to bobsled racers, aerodynamic shaping is crucial to achieving top speeds. Bobsleds are designed for speed.
They are shaped like a bullet with tapered fins. (credit: U.S. Army, via Wikimedia Commons)

The value of the drag coefficient,
5.8).

 , is determined empirically, usually with the use of a wind tunnel. (See Figure

FIGURE 5.8 NASA researchers test a model plane in a wind tunnel. (credit: NASA/Ames)

The drag coefficient can depend upon velocity, but we will assume that it is a constant here. Table 5.2 lists some
typical drag coefficients for a variety of objects. Notice that the drag coefficient is a dimensionless quantity. At
highway speeds, over 50% of the power of a car is used to overcome air drag. The most fuel-efficient cruising speed
is about 70–80 km/h (about 45–50 mi/h). For this reason, during the 1970s oil crisis in the United States, maximum
speeds on highways were set at about 90 km/h (55 mi/h).

208

5 • Further Applications of Newton's Laws: Friction, Drag, and Elasticity

Object

C

Airfoil

Toyota Camry

Ford Focus

Honda Civic

0.05

0.28

0.32

0.36

Ferrari Testarossa

0.37

Dodge Ram pickup

0.43

Sphere

0.45

Hummer H2 SUV

0.64

Skydiver (feet first)

0.70

Bicycle

0.90

Skydiver (horizontal)  1.0

Circular flat plate

1.12

TABLE 5.2 Drag Coefficient Values
.
Typical values of drag coefficient

Substantial research is under way in the sporting world to minimize drag. The dimples on golf balls are being
redesigned as are the clothes that athletes wear. Bicycle racers and some swimmers and runners wear full
bodysuits. Australian Cathy Freeman wore a full body suit in the 2000 Sydney Olympics, and won the gold medal for
the 400 m race. Many swimmers in the 2008 Beijing Olympics wore (Speedo) body suits; it might have made a
difference in breaking many world records (See Figure 5.9). Most elite swimmers (and cyclists) shave their body hair.
Such innovations can have the effect of slicing away milliseconds in a race, sometimes making the difference
between a gold and a silver medal. One consequence is that careful and precise guidelines must be continuously
developed to maintain the integrity of the sport.

FIGURE 5.9 Body suits, such as this LZR Racer Suit, have been credited with many world records after their release in 2008. Smoother
“skin” and more compression forces on a swimmer’s body provide at least 10% less drag. (credit: NASA/Kathy Barnstorff)

Some interesting situations connected to Newton’s second law occur when considering the effects of drag forces

Access for free at openstax.org

5.2 • Drag Forces

209

upon a moving object. For instance, consider a skydiver falling through air under the influence of gravity. The two
forces acting on him are the force of gravity and the drag force (ignoring the buoyant force). The downward force of
gravity remains constant regardless of the velocity at which the person is moving. However, as the person’s velocity
increases, the magnitude of the drag force increases until the magnitude of the drag force is equal to the
gravitational force, thus producing a net force of zero. A zero net force means that there is no acceleration, as given
by Newton’s second law. At this point, the person’s velocity remains constant and we say that the person has
reached his terminal velocity (
 is proportional to the speed, a heavier skydiver must go faster for
equal his weight. Let’s see how this works out more quantitatively.

). Since

 to

At the terminal velocity,

Thus,

Using the equation for drag force, we have

Solving for the velocity, we obtain

Assume the density of air is
approximately

. A 75-kg skydiver descending head first will have an area

 and a drag coefficient of approximately

. We find that

5.16

5.17

5.18

5.19

5.20

This means a skydiver with a mass of 75 kg achieves a maximum terminal velocity of about 350 km/h while traveling
in a headfirst position, minimizing the area and his drag. In a spread-eagle position, that terminal velocity may
decrease to about 200 km/h as the area increases. This terminal velocity becomes much smaller after the parachute
opens.

TAKE-HOME EXPERIMENT

This interesting activity examines the effect of weight upon terminal velocity. Gather together some nested
coffee filters. Leaving them in their original shape, measure the time it takes for one, two, three, four, and five
nested filters to fall to the floor from the same height (roughly 2 m). (Note that, due to the way the filters are
nested, drag is constant and only mass varies.) They obtain terminal velocity quite quickly, so find this velocity
 versus mass. Also plot
as a function of mass. Plot the terminal velocity
relationships is more linear? What can you conclude from these graphs?

 versus mass. Which of these

EXAMPLE  5.2

A Terminal Velocity
Find the terminal velocity of an 85-kg skydiver falling in a spread-eagle position.

Strategy

At terminal velocity,

. Thus the drag force on the skydiver must equal the force of gravity (the person’s

210

5 • Further Applications of Newton's Laws: Friction, Drag, and Elasticity

weight). Using the equation of drag force, we find

.

Thus the terminal velocity

 can be written as

Solution

All quantities are known except the person’s projected area. This is an adult (85 kg) falling spread eagle. We can
estimate the frontal area as

5.21

Using our equation for

, we find that

5.22

5.23

Discussion

This result is consistent with the value for
He weighed less but had a smaller frontal area and so a smaller drag due to the air.

 mentioned earlier. The 75-kg skydiver going feet first had a

.

The size of the object that is falling through air presents another interesting application of air drag. The terminal
velocity of a small squirrel is less than the terminal velocity we found previously for the skydiver, and so the squirrel
can fall from a significant height without injury.

The following interesting quote on animal size and terminal velocity is from a 1928 essay by a British biologist, J.B.S.
Haldane, titled “On Being the Right Size.”

To the mouse and any smaller animal, [gravity] presents practically no dangers. You can drop a mouse down a
thousand-yard mine shaft; and, on arriving at the bottom, it gets a slight shock and walks away, provided that the
ground is fairly soft. A rat is killed, a man is broken, and a horse splashes. For the resistance presented to movement
by the air is proportional to the surface of the moving object. Divide an animal’s length, breadth, and height each by
ten; its weight is reduced to a thousandth, but its surface only to a hundredth. So the resistance to falling in the case
of the small animal is relatively ten times greater than the driving force.

The above quadratic dependence of air drag upon velocity does not hold if the object is very small, is going very
slow, or is in a denser medium than air. Then we find that the drag force is proportional just to the velocity. This
relationship is given by Stokes’ law, which states that

where

 is the radius of the object,

 is the viscosity of the fluid, and

 is the object’s velocity.

STOKES’ LAW

where

 is the radius of the object,

 is the viscosity of the fluid, and

 is the object’s velocity.

5.24

5.25

Good examples of this law are provided by microorganisms, pollen, and dust particles. Because each of these
objects is so small, we find that many of these objects travel unaided only at a constant (terminal) velocity. Terminal
. To move at a greater speed, many bacteria swim using
velocities for bacteria (size about
flagella (organelles shaped like little tails) that are powered by little motors embedded in the cell. Sediment in a lake
can move at a greater terminal velocity (about
being deposited on the surface.

), so it can take days to reach the bottom of the lake after

) can be about

Access for free at openstax.org
