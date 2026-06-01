406

10 • Rotational Motion and Angular Momentum

EXAMPLE  10.6

Calculating the Distance Traveled by a Fly on the Edge of a Microwave Oven Plate
A person decides to use a microwave oven to reheat some lunch. In the process, a fly accidentally flies into the
microwave and lands on the outer edge of the rotating plate and remains there. If the plate has a radius of 0.15 m
and rotates at 6.0 rpm, calculate the total distance traveled by the fly during a 2.0-min cooking period. (Ignore the
start-up and slow-down times.)

Strategy

First, find the total number of revolutions
because

 is given to be 6.0 rpm.

Solution

Entering known values into

 gives

, and then the linear distance

 traveled.

 can be used to find

As always, it is necessary to convert revolutions to radians before calculating a linear quantity like
quantity like  :

 from an angular

10.37

Now, using the relationship between

 and

, we can determine the distance traveled:

10.38

10.39

Discussion

Quite a trip (if it survives)! Note that this distance is the total distance traveled by the fly. Displacement is actually
zero for complete revolutions because they bring the fly back to its original position. The distinction between total
distance traveled and displacement was first noted in One-Dimensional Kinematics.

CHECK YOUR UNDERSTANDING

Rotational kinematics has many useful relationships, often expressed in equation form. Are these relationships laws
of physics or are they simply descriptive? (Hint: the same question applies to linear kinematics.)

Solution
Rotational kinematics (just like linear kinematics) is descriptive and does not represent laws of nature. With
kinematics, we can describe many things to great precision but kinematics does not consider causes. For example, a
large angular acceleration describes a very rapid change in angular velocity without any consideration of its cause.

10.3 Dynamics of Rotational Motion: Rotational Inertia

LEARNING OBJECTIVES
By the end of this section, you will be able to:

•  Understand the relationship between force, mass and acceleration.
•  Study the turning effect of force.
•  Study the analogy between force and torque, mass and moment of inertia, and linear acceleration and

angular acceleration.

If you have ever spun a bike wheel or pushed a merry-go-round, you know that force is needed to change angular
velocity as seen in Figure 10.9. In fact, your intuition is reliable in predicting many of the factors that are involved.
For example, we know that a door opens slowly if we push too close to its hinges. Furthermore, we know that the
more massive the door, the more slowly it opens. The first example implies that the farther the force is applied from

Access for free at openstax.org

10.3 • Dynamics of Rotational Motion: Rotational Inertia

407

the pivot, the greater the angular acceleration; another implication is that angular acceleration is inversely
proportional to mass. These relationships should seem very similar to the familiar relationships among force, mass,
and acceleration embodied in Newton’s second law of motion. There are, in fact, precise rotational analogs to both
force and mass.

FIGURE 10.9 Force is required to spin the bike wheel. The greater the force, the greater the angular acceleration produced. The more
massive the wheel, the smaller the angular acceleration. If you push on a spoke closer to the axle, the angular acceleration will be smaller.

To develop the precise relationship among force, mass, radius, and angular acceleration, consider what happens if
we exert a force
 from a pivot point, as shown in Figure 10.10. Because
the force is perpendicular to  , an acceleration

 is obtained in the direction of

. We can rearrange this

 that is at a distance

 on a point mass

equation such that
We note that

 and then look for ways to relate this expression to expressions for rotational quantities.

, and we substitute this expression into

, yielding

Recall that torque is the turning effectiveness of a force. In this case, because
simply

. So, if we multiply both sides of the equation above by  , we get torque on the left-hand side. That is,
10.41

10.40

 is perpendicular to  , torque is

or

This last equation is the rotational analog of Newton’s second law (
angular acceleration is analogous to translational acceleration, and
quantity
rotation.

 is called the rotational inertia or moment of inertia of a point mass

 a distance

 from the center of

10.42

), where torque is analogous to force,

 is analogous to mass (or inertia). The

FIGURE 10.10 An object is supported by a horizontal frictionless table and is attached to a pivot point by a cord that supplies centripetal
force. A force
perpendicular to  .

 is applied to the object perpendicular to the radius  , causing it to accelerate about the pivot point. The force is kept

MAKING CONNECTIONS: ROTATIONAL MOTION DYNAMICS

Dynamics for rotational motion is completely analogous to linear or translational dynamics. Dynamics is
concerned with force and mass and their effects on motion. For rotational motion, we will find direct analogs to
force and mass that behave just as we would expect from our earlier experiences.

408

10 • Rotational Motion and Angular Momentum

Rotational Inertia and Moment of Inertia

Before we can consider the rotation of anything other than a point mass like the one in Figure 10.10, we must
extend the idea of rotational inertia to all types of objects. To expand our concept of rotational inertia, we define the
moment of inertia

 for all the point masses of which it is composed. That is,

 of an object to be the sum of

. Here

 is analogous to

 in translational motion. Because of the distance  , the moment of inertia for

 is beyond the scope of this text except for one simple
any object depends on the chosen axis. Actually, calculating
case—that of a hoop, which has all its mass at the same distance from its axis. A hoop’s moment of inertia around its
axis is therefore
distinguish them from
table is piece of artwork that has shapes as well as formulae) for formulas for
integration over the continuous body. Note that
might expect from its definition.

 for point masses.) In all other cases, we must consult Figure 10.11 (note that the

 has units of mass multiplied by distance squared (

 that have been derived from

 for an entire object to

 is its total mass and

 its radius. (We use

, where
 and

), as we

 and

The general relationship among torque, moment of inertia, and angular acceleration is

or

10.43

10.44

 is the total torque from all forces relative to a chosen axis. For simplicity, we will only consider torques

where net
exerted by forces in the plane of the rotation. Such torques are either positive or negative and add like ordinary
numbers. The relationship in

 is the rotational analog to Newton’s second law and is very generally

applicable. This equation is actually valid for any torque, applied to any object, relative to any axis.

As we might expect, the larger the torque is, the larger the angular acceleration is. For example, the harder a child
pushes on a merry-go-round, the faster it accelerates. Furthermore, the more massive a merry-go-round, the slower
it accelerates for the same torque. The basic relationship between moment of inertia and angular acceleration is
that the larger the moment of inertia, the smaller is the angular acceleration. But there is an additional twist. The
moment of inertia depends not only on the mass of an object, but also on its distribution of mass relative to the axis
around which it rotates. For example, it will be much easier to accelerate a merry-go-round full of children if they
stand close to its axis than if they all stand at the outer edge. The mass is the same in both cases, but the moment of
inertia is much larger when the children are at the edge.

TAKE-HOME EXPERIMENT

Cut out a circle that has about a 10 cm radius from stiff cardboard. Near the edge of the circle, write numbers 1
to 12 like hours on a clock face. Position the circle so that it can rotate freely about a horizontal axis through its
center, like a wheel. (You could loosely nail the circle to a wall.) Hold the circle stationary and with the number
12 positioned at the top, attach a lump of blue putty (sticky material used for fixing posters to walls) at the
number 3. How large does the lump need to be to just rotate the circle? Describe how you can change the
moment of inertia of the circle. How does this change affect the amount of blue putty needed at the number 3 to
just rotate the circle? Change the circle’s moment of inertia and then try rotating the circle by using different
amounts of blue putty. Repeat this process several times.

PROBLEM-SOLVING STRATEGY FOR ROTATIONAL DYNAMICS

1.  Examine the situation to determine that torque and mass are involved in the rotation. Draw a careful

sketch of the situation.

2.  Determine the system of interest.
3.  Draw a free body diagram. That is, draw and label all external forces acting on the system of interest.
4.  Apply

, the rotational equivalent of Newton’s second law, to solve the problem. Care

Access for free at openstax.org

10.3 • Dynamics of Rotational Motion: Rotational Inertia

409

must be taken to use the correct moment of inertia and to consider the torque about the point of rotation.

5.  As always, check the solution to see if it is reasonable.

MAKING CONNECTIONS

In statics, the net torque is zero, and there is no angular acceleration. In rotational motion, net torque is the
cause of angular acceleration, exactly as in Newton’s second law of motion for rotation.

FIGURE 10.11 Some rotational inertias.

EXAMPLE  10.7

Calculating the Effect of Mass Distribution on a Merry-Go-Round
Consider the father pushing a playground merry-go-round in Figure 10.12. He exerts a force of 250 N at the edge of
the 50.0-kg merry-go-round, which has a 1.50 m radius. Calculate the angular acceleration produced (a) when no
one is on the merry-go-round and (b) when an 18.0-kg child sits 1.25 m away from the center. Consider the merry-
go-round itself to be a uniform disk with negligible retarding friction.

410

10 • Rotational Motion and Angular Momentum

FIGURE 10.12 A father pushes a playground merry-go-round at its edge and perpendicular to its radius to achieve maximum torque.

Strategy

Angular acceleration is given directly by the expression

 :

10.45

, we must first calculate the torque

To solve for
is greater in the second case). To find the torque, we note that the applied force is perpendicular to the radius and
friction is negligible, so that

 (which is the same in both cases) and moment of inertia

 (which

Solution for (a)

The moment of inertia of a solid disk about this axis is given in Figure 10.11 to be

where

 and

, so that

Now, after we substitute the known values, we find the angular acceleration to be

10.46

10.47

10.48

10.49

Solution for (b)

We expect the angular acceleration for the system to be less in this part, because the moment of inertia is greater
, we first find the child’s moment of
when the child is on the merry-go-round. To find the total moment of inertia
inertia

 by considering the child to be equivalent to a point mass at a distance of 1.25 m from the axis. Then,

10.50

The total moment of inertia is the sum of moments of inertia of the merry-go-round and the child (about the same
axis). To justify this sum to yourself, examine the definition of

:

Substituting known values into the equation for

 gives

10.51

10.52

Discussion

The angular acceleration is less when the child is on the merry-go-round than when the merry-go-round is empty, as
expected. The angular accelerations found are quite large, partly due to the fact that friction was considered to be

Access for free at openstax.org
