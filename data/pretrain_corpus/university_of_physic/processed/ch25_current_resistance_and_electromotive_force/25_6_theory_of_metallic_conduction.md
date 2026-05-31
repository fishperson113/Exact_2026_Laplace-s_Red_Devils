838

CHAPTER 25 Current, Resistance, and Electromotive Force

25.26 Random motions of an electron in
a metallic crystal (a) with zero electric
ﬁeld and (b) with an electric ﬁeld that
causes drift. The curvatures of the paths
are greatly exaggerated.

(a)

Collision
with crystal

S
E

Without E field:
random motion

END START

(b)

S
With E field:
random motion
plus drift

S
E

S
E

START

S
E

END

Net displacement

PhET: Conductivity

25.27 The motion of a ball rolling down
an inclined plane and bouncing off pegs in
its path is analogous to the motion of an
electron in a metallic conductor with an
electric ﬁeld present.

resistor connected to a

Test Your Understanding of Section 25.5 Rank the following circuits
in order from highest to lowest values of the net power output of the battery. (i) a
1.4 - Æ
0.10 Æ;
3.6 V
battery that has an internal resistance of

but an unknown internal resistance; (iii) an unknown resistor connected to a
0.20 Æ

1.5-V
resistor connected to a

battery that has an internal resistance of

and a terminal voltage of

11.0 V.

1.8-Æ

battery that has a terminal voltage of

4.0-V

(ii) a

12.0-V
❙

25.6 Theory of Metallic Conduction

We can gain additional insight into electrical conduction by looking at the micro-
scopic origin of conductivity. We’ll consider a very simple model that treats the
electrons as classical particles and ignores their quantum-mechanical behavior in
solids. Using this model, we’ll derive an expression for the resistivity of a metal.
Even though this model is not entirely correct, it will still help you to develop an
intuitive idea of the microscopic basis of conduction.

In the simplest microscopic model of conduction in a metal, each atom in the
metallic crystal gives up one or more of its outer electrons. These electrons are
then  free  to  move  through  the  crystal,  colliding  at  intervals  with  the  stationary
positive  ions. The  motion  of  the  electrons  is  analogous  to  the  motion  of  mole-
cules of a gas moving through a porous bed of sand.

If there is no electric ﬁeld, the electrons move in straight lines between colli-
sions, the directions of their velocities are random, and on average they never get
anywhere (Fig. 25.26a). But if an electric ﬁeld is present, the paths curve slightly
because of the acceleration caused by electric-ﬁeld forces. Figure 25.26b shows a
few paths of an electron in an electric ﬁeld directed from right to left. As we men-
tioned  in  Section  25.1,  the  average  speed  of  random  motion  is  of  the  order  of
10-4 m>s.
106 m>s,
while the average drift speed is much slower, of the order of
t.
The average time between collisions is called the mean free time, denoted by
Figure 25.27 shows a mechanical analog of this electron motion.

We would like to derive from this model an expression for the resistivity  of

r

a material, deﬁned by Eq. (25.5):

r = E
J

(25.21)

E

J
where
tively. The current density

and

S
J

is in turn given by Eq. (25.4):

are  the  magnitudes  of  electric  ﬁeld  and  current  density,  respec-

S
J

(cid:2) nqv

S
d

(25.22)

q = - e

is the charge of

n

where
each, and

S
v
d

is the number of free electrons per unit volume,

is their average drift velocity.

S
E

S
v

S
v
d

.

We need to relate the drift velocity

to the electric ﬁeld  The value of

is
d
determined by a steady-state condition in which, on average, the velocity gains
S
E
of  the  charges  due  to  the  force  of  the
ﬁeld  are  just  balanced  by  the  velocity
losses due to collisions. To clarify this process, let’s imagine turning on the two
there is no ﬁeld. The elec-
effects one at a time. Suppose that before time
at time
tron motion is then completely random. A typical electron has velocity
t = 0,
averaged over many electrons (that is, the initial veloc-
02av (cid:2) 0.
ity of an average electron) is zero:
we turn on a
S
.
E
constant electric ﬁeld  The ﬁeld exerts a force
on each charge, and this
S
a
causes an acceleration

in the direction of the force, given by

Then at time
S
S
(cid:2) qE
F

and the value of

t = 0

t = 0

1v

S
v

S
v

S

0

0

S

S (cid:2) F
a
m

(cid:2)

S
qE
m

where

m

is the electron mass. Every electron has this acceleration.

25.6 Theory of Metallic Conduction

839

We wait for a time

t,

the collisions. An electron that has velocity
t = t

equal to

0

the average time between collisions, and then “turn on”
has a velocity at time

at time

t = 0

S
v

S

S (cid:2) v
v

St
0 (cid:4) a

S
v

The velocity
the two terms on the right. As we have pointed out, the initial velocity
for an average electron, so

of an average electron at this time is the sum of the averages of
is zero

S
v
0

av

S
v

av (cid:2) a

St (cid:2)

qt
m

S
E

(25.23)

t = t,

After time

the tendency of the collisions to decrease the velocity of an
average electron (by means of randomizing collisions) just balances the tendency
of the  ﬁeld to increase this velocity. Thus the velocity of an average electron,
d:
given by Eq. (25.23), is maintained over time and is equal to the drift velocity

S
E

S
v

S
v

d (cid:2)

qt
m

S
E

Now we substitute this equation for the drift velocity

S
v
d

into Eq. (25.22):

S
J

S

(cid:2) nqv

d (cid:2)

nq 2t
m

S
E

Comparing this with Eq. (25.21), which we can rewrite as
r
tuting

for an electron, we see that the resistivity

q = - e

S

S
>r,
(cid:2) E
J
is given by

and substi-

r = m
ne2t

t

n

If  and  are independent of
conducting material obeys Ohm’s law.

,

S
E

then the resistivity is independent of

(25.24)

S
E

and the

Turning the interactions on one at a time may seem artiﬁcial. But the deriva-
t = 0
is the average time between colli-
is still the average electron drift velocity, even though the motions

tion would come out the same if each electron had its own clock and the
t
times were different for different electrons. If
sions, then
of the various electrons aren’t actually correlated in the way we postulated.

S
v
d

What  about  the  temperature  dependence  of  resistivity?  In  a  perfect  crystal
with no atoms out of place, a correct quantum-mechanical analysis would let the
free electrons move through the crystal with no collisions at all. But the atoms
vibrate  about  their  equilibrium  positions.  As  the  temperature  increases,  the
amplitudes of these vibrations increase, collisions become more frequent, and the
mean free time  decreases. So this theory predicts that the resistivity of a metal
increases with temperature. In a superconductor, roughly speaking, there are no
inelastic collisions,

is inﬁnite, and the resistivity

is zero.

r

t

t

In a pure semiconductor such as silicon or germanium, the number of charge
,  is  not  constant  but  increases  very  rapidly  with
carriers  per  unit  volume,
n
increasing temperature. This increase in
far outweighs the decrease in the mean
free  time,  and  in  a  semiconductor  the  resistivity  always  decreases  rapidly  with
is very small, and the resistivity
increasing temperature. At low temperatures,
becomes so large that the material can be considered an insulator.

n

n

Electrons gain energy between collisions through the work done on them by
the electric ﬁeld. During collisions they transfer some of this energy to the atoms
of the material of the conductor. This leads to an increase in the material’s internal
energy and temperature; that’s why wires carrying current get warm. If the electric
ﬁeld in the material is large enough, an electron can gain enough energy between
collisions to knock off electrons that are normally bound to atoms in the material.
These can then knock off more electrons, and so on, leading to an avalanche of
current. This is the basis of dielectric breakdown in insulators (see Section 24.4).

840

CHAPTER 25 Current, Resistance, and Electromotive Force

Example 25.11 Mean free time in copper

Calculate the mean free time between collisions in copper at room
temperature.

SOLUTION

t

IDENTIFY and SET UP: We can obtain an expression for mean free
er,
time
by rearranging Eq. (25.24). From
,
in terms of
and
Example 25.1 and Table 25.1, for copper
r = 1.72 * 10-8 Æ # m.
and
m = 9.11 * 10-31 kg

n = 8.5 * 1028 m-3
e = 1.60 * 10-19 C

for electrons.

In  addition,

, and

m

n

EXECUTE: From Eq. (25.24), we get
t = m
ne2r

=

9.11 * 10-31 kg
18.5 * 1028 m-3211.60 * 10-19 C2211.72 * 10-8 Æ # m2
= 2.4 * 10-14 s

EVALUATE:  The mean free time is the average time between colli-
sions  for  a  given  electron. Taking  the  reciprocal  of  this  time,  we
ﬁnd  that  each  electron  averages
collisions  per
second!

1>t = 4.2 * 1013

Test Your Understanding of Section 25.6 Which of the following factors
will, if increased, make it more difﬁcult to produce a certain amount of current in a
conductor? (There may be more than one correct answer.) (i) the mass of the moving
charged particles in the conductor; (ii) the number of moving charged particles per cubic
meter; (iii) the amount of charge on each moving particle; (iv) the average time between
collisions for a typical moving charged particle.

❙
