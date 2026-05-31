Example 25.10
Power in a short circuit
For the short-circuit situation of Example 25.7, find the rates of
energy conversion and energy dissipation in the battery and the net
power output of the battery.
SOLUTION
IDENTIFY and SET UP: Our target variables are again the power
inputs and outputs associated with the battery. Figure 25.25 shows
the circuit. This is the same situation as in Example 25.8, but now
the external resistance 
is zero.
EXECUTE: We found in Example 25.7 that the current in this situa-
tion is 
From Eq. (25.19), the rate of energy conversion
(chemical to electrical) in the battery is then
and the rate of dissipation of energy in the battery is
The net power output of the source is 
. We get this
same result from the expression 
, because the terminal
voltage 
of the source is zero.
EVALUATE: With ideal wires and an ideal ammeter, so that 
all of the converted energy from the source is dissipated within the
source. This is why a short-circuited battery is quickly ruined and
may explode.
R = 0,
Vab
P = VabI
EI - I 2r = 0
I 2r = 16 A2212 Æ2 = 72 W
EI = 112 V216 A2 = 72 W
I = 6 A.
R
25.25 Our sketch for this problem.

25.6 Theory of Metallic Conduction
We can gain additional insight into electrical conduction by looking at the micro-
scopic origin of conductivity. We’ll consider a very simple model that treats the
electrons as classical particles and ignores their quantum-mechanical behavior in
solids. Using this model, we’ll derive an expression for the resistivity of a metal.
Even though this model is not entirely correct, it will still help you to develop an
intuitive idea of the microscopic basis of conduction.
In the simplest microscopic model of conduction in a metal, each atom in the
metallic crystal gives up one or more of its outer electrons. These electrons are
then free to move through the crystal, colliding at intervals with the stationary
positive ions. The motion of the electrons is analogous to the motion of mole-
cules of a gas moving through a porous bed of sand.
If there is no electric field, the electrons move in straight lines between colli-
sions, the directions of their velocities are random, and on average they never get
anywhere (Fig. 25.26a). But if an electric field is present, the paths curve slightly
because of the acceleration caused by electric-field forces. Figure 25.26b shows a
few paths of an electron in an electric field directed from right to left. As we men-
tioned in Section 25.1, the average speed of random motion is of the order of
while the average drift speed is much slower, of the order of 
The average time between collisions is called the mean free time, denoted by 
Figure 25.27 shows a mechanical analog of this electron motion.
We would like to derive from this model an expression for the resistivity 
of
a material, defined by Eq. (25.5):
(25.21)
where 
and 
are the magnitudes of electric field and current density, respec-
tively. The current density 
is in turn given by Eq. (25.4):
(25.22)
where is the number of free electrons per unit volume, 
is the charge of
each, and 
is their average drift velocity.
We need to relate the drift velocity 
to the electric field 
The value of 
is
determined by a steady-state condition in which, on average, the velocity gains
of the charges due to the force of the 
field are just balanced by the velocity
losses due to collisions. To clarify this process, let’s imagine turning on the two
effects one at a time. Suppose that before time 
there is no field. The elec-
tron motion is then completely random. A typical electron has velocity 
at time
and the value of 
averaged over many electrons (that is, the initial veloc-
ity of an average electron) is zero: 
Then at time 
we turn on a
constant electric field 
The field exerts a force 
on each charge, and this
causes an acceleration 
in the direction of the force, given by
where 
is the electron mass. Every electron has this acceleration.
m
a
S  F
S
m  qE
S
m
a
S
F
S  qE
S
E
S.
t = 0
1v
S
02av  0.
v
S
0
t = 0,
v
S
0
t = 0
E
S
v
S
d
E
S.
v
S
d
v
S
d
q = -e
n
J
S  nqv
S
d
J
S
J
E
r = E
J
r
t.
10-4 m>s.
106 m>s,
838
CHAPTER 25 Current, Resistance, and Electromotive Force
Test Your Understanding of Section 25.5
Rank the following circuits
in order from highest to lowest values of the net power output of the battery. (i) a
resistor connected to a 
battery that has an internal resistance of
(ii) a 
resistor connected to a 
battery that has a terminal voltage of
but an unknown internal resistance; (iii) an unknown resistor connected to a 
battery that has an internal resistance of 
and a terminal voltage of 
❙
11.0 V.
0.20 Æ
12.0-V
3.6 V
4.0-V
1.8-Æ
0.10 Æ;
1.5-V
1.4-Æ
(a)
(b)
Net displacement
Collision
with crystal
END
START
END
START
E
S
E
S
E
S
Without E field:
random motion
E
S
With E field:
random motion
plus drift
S
25.26 Random motions of an electron in
a metallic crystal (a) with zero electric
field and (b) with an electric field that
causes drift. The curvatures of the paths
are greatly exaggerated.
25.27 The motion of a ball rolling down
an inclined plane and bouncing off pegs in
its path is analogous to the motion of an
electron in a metallic conductor with an
electric field present.
PhET: Conductivity

25.6 Theory of Metallic Conduction
839
We wait for a time 
the average time between collisions, and then “turn on”
the collisions. An electron that has velocity 
at time 
has a velocity at time
equal to
The velocity 
of an average electron at this time is the sum of the averages of
the two terms on the right. As we have pointed out, the initial velocity 
is zero
for an average electron, so
(25.23)
After time 
the tendency of the collisions to decrease the velocity of an
average electron (by means of randomizing collisions) just balances the tendency
of the 
field to increase this velocity. Thus the velocity of an average electron,
given by Eq. (25.23), is maintained over time and is equal to the drift velocity 
Now we substitute this equation for the drift velocity 
into Eq. (25.22):
Comparing this with Eq. (25.21), which we can rewrite as 
and substi-
tuting 
for an electron, we see that the resistivity 
is given by
(25.24)
If 
and 
are independent of 
then the resistivity is independent of 
and the
conducting material obeys Ohm’s law.
Turning the interactions on one at a time may seem artificial. But the deriva-
tion would come out the same if each electron had its own clock and the 
times were different for different electrons. If is the average time between colli-
sions, then 
is still the average electron drift velocity, even though the motions
of the various electrons aren’t actually correlated in the way we postulated.
What about the temperature dependence of resistivity? In a perfect crystal
with no atoms out of place, a correct quantum-mechanical analysis would let the
free electrons move through the crystal with no collisions at all. But the atoms
vibrate about their equilibrium positions. As the temperature increases, the
amplitudes of these vibrations increase, collisions become more frequent, and the
mean free time 
decreases. So this theory predicts that the resistivity of a metal
increases with temperature. In a superconductor, roughly speaking, there are no
inelastic collisions, is infinite, and the resistivity 
is zero.
In a pure semiconductor such as silicon or germanium, the number of charge
carriers per unit volume, , is not constant but increases very rapidly with
increasing temperature. This increase in far outweighs the decrease in the mean
free time, and in a semiconductor the resistivity always decreases rapidly with
increasing temperature. At low temperatures, 
is very small, and the resistivity
becomes so large that the material can be considered an insulator.
Electrons gain energy between collisions through the work done on them by
the electric field. During collisions they transfer some of this energy to the atoms
of the material of the conductor. This leads to an increase in the material’s internal
energy and temperature; that’s why wires carrying current get warm. If the electric
field in the material is large enough, an electron can gain enough energy between
collisions to knock off electrons that are normally bound to atoms in the material.
These can then knock off more electrons, and so on, leading to an avalanche of
current. This is the basis of dielectric breakdown in insulators (see Section 24.4).
n
n
n
r
t
t
v
S
d
t
t = 0
E
S
E
S,
t
n
r =
m
ne2t
r
q = -e
J
S  E
S>r,
J
S  nqv
S
d  nq2t
m E
S
v
S
d
v
S
d  qt
m E
S
v
S
d:
E
S
t = t,
v
S
av  a
St  qt
m E
S
v
S
0
v
S
av
v
S  v
S
0  a
St
t = t
t = 0
v
S
0
t,

840
CHAPTER 25 Current, Resistance, and Electromotive Force
