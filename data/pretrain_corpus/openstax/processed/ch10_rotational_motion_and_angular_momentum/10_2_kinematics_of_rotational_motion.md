10.2 • Kinematics of Rotational Motion

401

the magnitudes of these quantities.

CHECK YOUR UNDERSTANDING

Angular acceleration is a vector, having both magnitude and direction. How do we denote its magnitude and
direction? Illustrate with an example.

Solution

The magnitude of angular acceleration is
acceleration along a fixed axis is denoted by a + or a – sign, just as the direction of linear acceleration in one
dimension is denoted by a + or a – sign. For example, consider a gymnast doing a forward flip. Her angular
momentum would be parallel to the mat and to her left. The magnitude of her angular acceleration would be
proportional to her angular velocity (spin rate) and her moment of inertia about her spin axis.

 and its most common units are

. The direction of angular

LADYBUG REVOLUTION

Join the ladybug in an exploration of rotational motion. Rotate the merry-go-round to change its angle, or
choose a constant angular velocity or angular acceleration. Explore how circular motion relates to the bug's x,y
position, velocity, and acceleration using vectors or graphs.

Click to view content (https://openstax.org/l/28ladybugrevolutionrotation).

10.2 Kinematics of Rotational Motion

LEARNING OBJECTIVES
By the end of this section, you will be able to:

•  Observe the kinematics of rotational motion.
•  Derive rotational kinematic equations.
•  Evaluate problem solving strategies for rotational kinematics.

Just by using our intuition, we can begin to see how rotational quantities like
 are related to one another.
For example, if a motorcycle wheel has a large angular acceleration for a fairly long time, it ends up spinning rapidly
and rotates through many revolutions. In more technical terms, if the wheel’s angular acceleration
long period of time  , then the final angular velocity
motion is exactly analogous to the fact that the motorcycle’s large translational acceleration produces a large final
velocity, and the distance traveled will also be large.

 are large. The wheel’s rotational

 and angle of rotation

 is large for a

, and

,

Kinematics is the description of motion. The kinematics of rotational motion describes the relationships among
rotation angle, angular velocity, angular acceleration, and time. Let us start by finding an equation relating
. To determine this equation, we recall a familiar kinematic equation for translational, or straight-line, motion:

,

, and

Note that in rotational motion
on. As in linear kinematics, we assume
. Now, let us substitute
because

, and we shall use the symbol

 is constant, which means that angular acceleration

 is also a constant,

 and

 into the linear equation above:

 for tangential or linear acceleration from now

10.17

The radius

 cancels in the equation, yielding

10.18

10.19

 is the initial angular velocity. This last equation is a kinematic relationship among

where
describes their relationship without reference to forces or masses that may affect rotation. It is also precisely
analogous in form to its translational counterpart.

, and   —that is, it

,

402

10 • Rotational Motion and Angular Momentum

MAKING CONNECTIONS

Kinematics for rotational motion is completely analogous to translational kinematics, first presented in One-
Dimensional Kinematics. Kinematics is concerned with the description of motion without regard to force or
mass. We will find that translational kinematic quantities, such as displacement, velocity, and acceleration have
direct analogs in rotational motion.

Starting with the four kinematic equations we developed in One-Dimensional Kinematics, we can derive the
following four rotational kinematic equations (presented together with their translational counterparts):

Rotational

Translational

(constant

,  )

(constant

,  )

(constant

,  )

TABLE 10.2 Rotational Kinematic Equations

In these equations, the subscript 0 denotes initial values (
 are defined as follows:
velocity

 and average velocity

,

, and

 are initial values), and the average angular

10.20

The equations given above in Table 10.2 can be used to solve any rotational or translational kinematics problem in
which

 are constant.

 and

PROBLEM-SOLVING STRATEGY FOR ROTATIONAL KINEMATICS

1.  Examine the situation to determine that rotational kinematics (rotational motion) is involved. Rotation

must be involved, but without the need to consider forces or masses that affect the motion.

2.  Identify exactly what needs to be determined in the problem (identify the unknowns). A sketch of the

situation is useful.

3.  Make a list of what is given or can be inferred from the problem as stated (identify the knowns).
4.  Solve the appropriate equation or equations for the quantity to be determined (the unknown). It can be
useful to think in terms of a translational analog because by now you are familiar with such motion.
5.  Substitute the known values along with their units into the appropriate equation, and obtain numerical

solutions complete with units. Be sure to use units of radians for angles.
6.  Check your answer to see if it is reasonable: Does your answer make sense?

EXAMPLE  10.3

Calculating the Acceleration of a Fishing Reel
A deep-sea fisherman hooks a big fish that swims away from the boat pulling the fishing line from his fishing reel.
The whole system is initially at rest and the fishing line unwinds from the reel at a radius of 4.50 cm from its axis of
rotation. The reel is given an angular acceleration of

 for 2.00 s as seen in Figure 10.7.

(a) What is the final angular velocity of the reel?

Access for free at openstax.org

10.2 • Kinematics of Rotational Motion

403

(b) At what speed is fishing line leaving the reel after 2.00 s elapses?

(c) How many revolutions does the reel make?

(d) How many meters of fishing line come off the reel in this time?

Strategy

In each part of this example, the strategy is the same as it was for solving problems in linear kinematics. In
particular, known values are identified and a relationship is then sought that can be used to solve for the unknown.

Solution for (a)

 and   are given and

Here
because the unknown is already on one side and all other terms are known. That equation states that

 needs to be determined. The most straightforward equation to use is

We are also given that

 (it starts from rest), so that

Solution for (b)

Now that

 is known, the speed

 can most easily be found using the relationship

where the radius

 of the reel is given to be 4.50 cm; thus,

10.21

10.22

10.23

10.24

Note again that radians must always be used in any calculation relating linear and angular quantities. Also, because
radians are dimensionless, we have

.

Solution for (c)

Here, we are asked to find the number of revolutions. Because
revolutions by finding

 in radians. We are given

 and  , and we know

, we can find the number of

 is zero, so that

 can be obtained using

.

Converting radians to revolutions gives

Solution for (d)

The number of meters of fishing line is

, which can be obtained through its relationship with  :

10.25

10.26

10.27

Discussion

This example illustrates that relationships among rotational quantities are highly analogous to those among linear
quantities. We also see in this example how linear and rotational quantities are connected. The answers to the
questions are realistic. After unwinding for two seconds, the reel is found to spin at 220 rad/s, which is 2100 rpm.
(No wonder reels sometimes make high-pitched sounds.) The amount of fishing line played out is 9.90 m, about
right for when the big fish bites.

404

10 • Rotational Motion and Angular Momentum

FIGURE 10.7 Fishing line coming off a rotating reel moves linearly. Example 10.3 and Example 10.4 consider relationships between
rotational and linear quantities associated with a fishing reel.

EXAMPLE  10.4

Calculating the Duration When the Fishing Reel Slows Down and Stops
Now let us consider what happens if the fisherman applies a brake to the spinning reel, achieving an angular
. How long does it take the reel to come to a stop?
acceleration of

Strategy

We are asked to find the time   for the reel to come to a stop. The initial and final conditions are different from those
in the previous problem, which involved the same fishing reel. Now we see that the initial angular velocity is

 and the final angular velocity

 is zero. The angular acceleration is given to be

.
 making it easiest to use

Examining the available equations, we see all quantities but t are known in
this equation.

Solution

The equation states

We solve the equation algebraically for t, and then substitute the known values as usual, yielding

10.28

10.29

Discussion

Note that care must be taken with the signs that indicate the directions of various quantities. Also, note that the time
to stop the reel is fairly small because the acceleration is rather large. Fishing lines sometimes snap because of the
accelerations involved, and fishermen often let the fish swim for a while before applying brakes on the reel. A tired
fish will be slower, requiring a smaller acceleration.

EXAMPLE  10.5

Calculating the Slow Acceleration of Trains and Their Wheels
Large freight trains accelerate very slowly. Suppose one such train accelerates from rest, giving its 0.350-m-radius
wheels an angular acceleration of
. After the wheels have made 200 revolutions (assume no slippage):
(a) How far has the train moved down the track? (b) What are the final angular velocity of the wheels and the linear
velocity of the train?

Strategy

In part (a), we are asked to find

, and in (b) we are asked to find

 and

. We are given the number of revolutions

,

Access for free at openstax.org

10.2 • Kinematics of Rotational Motion

405

the radius of the wheels  , and the angular acceleration

.

Solution for (a)

The distance

 is very easily found from the relationship between distance and rotation angle:

Solving this equation for

 yields

10.30

10.31

Before using this equation, we must convert the number of revolutions into radians, because we are dealing with a
relationship between linear and rotational quantities:

Now we can substitute the known values into

 to find the distance the train moved down the track:

Solution for (b)

10.32

10.33

We cannot use any equation that incorporates   to find
values. The equation

 will work, because we know the values for all variables except

, because the equation would have at least two unknown

:

10.34

10.35

10.36

Taking the square root of this equation and entering the known values gives

We can find the linear velocity of the train,

, through its relationship to

:

Discussion

The distance traveled is fairly large and the final velocity is fairly slow (just under 32 km/h).

There is translational motion even for something spinning in place, as the following example illustrates. Figure 10.8
shows a fly on the edge of a rotating microwave oven plate. The example below calculates the total distance it
travels.

FIGURE 10.8 The image shows a microwave plate. The fly makes revolutions while the food is heated (along with the fly).
