Sample Problem 30.04
Induced electric field due to changing B field, inside and outside
In Fig. 30-11b, take R
8.5 cm and dB/dt
0.13 T/s.
(a) Find an expression for the magnitude E of the induced
electric field at points within the magnetic field, at radius r
from the center of the magnetic field. Evaluate the expres-
sion for r ! 5.2 cm.
KEY IDEA
An electric field is induced by the changing magnetic field,
according to Faraday’s law.
Calculations: To calculate the field magnitude E, we ap-
ply Faraday’s law in the form of Eq. 30-20. We use a circu-
lar path of integration with radius r
R because we want
E for points within the magnetic field. We assume from
the symmetry that 
in Fig. 30-11b is tangent to the circu-
lar path at all points.The path vector 
is also always tan-
gent to the circular path; so the dot product 
in Eq.
30-20 must have the magnitude E ds at all points on the
path. We can also assume from the symmetry that E has
the same value at all points along the circular path. Then
the left side of Eq. 30-20 becomes
(30-23)
(The integral 
is the circumference 2pr of the circular
path.)
Next, we need to evaluate the right side of Eq. 30-20.
Because 
is uniform over the area A encircled by the path
of integration and is directed perpendicular to that area, the
magnetic flux is given by Eq. 30-2:
0B ! BA ! B(pr 2).
(30-24)
Substituting this and Eq. 30-23 into Eq. 30-20 and dropping
B
:
- ds
, E
:!ds
: !, E ds ! E, ds ! E(2pr).
E
:!ds
:
ds
:
E
:
2
!
!

879
30-4 INDUCTORS AND INDUCTANCE
Substituting this and Eq. 30-23 into Eq. 30-20 (without the
minus sign) and solving for E yield
(Answer)
(30-27)
Because E is not zero here, we know that an electric field is
induced even at points that are outside the changing mag-
netic field, an important result that (as you will see in
Module 31-6) makes transformers possible.
With the given data, Eq. 30-27 yields the magnitude of
at r ! 12.5 cm:
(Answer)
! 3.8 $ 10 %3 V/m ! 3.8 mV/m. 
E !
(8.5 $ 10 %2 m)2
(2)(12.5 $ 10 %2 m)  (0.13 T/s)
E
:
E ! R2
2r
dB
dt .
Additional examples, video, and practice available at WileyPLUS
Figure 30-12 A plot of the induced electric field E(r).
6
4
2
00 
10 
20 
30 
40 
r  (cm) 
E (mV/m) 
Equations 30-25 and 30-27 give the same result for 
r ! R. Figure 30-12 shows a plot of E(r). Note that the in-
side and outside plots meet at r ! R.
30-4 INDUCTORS AND INDUCTANCE
After reading this module, you should be able to . . .
30.19 Identify an inductor.
30.20 For an inductor, apply the relationship between
inductance L, total flux N0, and current i.
30.21 For a solenoid, apply the relationship between the
inductance per unit length L/l, the area A of each turn,
and the number of turns per unit length n.
Learning Objectives
●An inductor is a device that can be used to produce a known
magnetic field in a specified region. If a current i is established
through each of the N windings of an inductor, a magnetic flux
0B links those windings. The inductance L of the inductor is
(inductance defined).
L ! N0B
i
Key Ideas
●The SI unit of inductance is the henry (H), where 1 henry 
1 H ! 1 T ) m2/A.
●The inductance per unit length near the middle of a long so-
lenoid of cross-sectional area A and n turns per unit length is
(solenoid).
L
l ! m0n2A
!
Inductors and Inductance
We found in Chapter 25 that a capacitor can be used to produce a desired elec-
tric field. We considered the parallel-plate arrangement as a basic type of ca-
pacitor. Similarly, an inductor (symbol 
) can be used to produce a desired
magnetic field. We shall consider a long solenoid (more specifically, a short
length near the middle of a long solenoid, to avoid any fringing effects) as our
basic type of inductor.
If we establish a current i in the windings (turns) of the solenoid we are
taking as our inductor, the current produces a magnetic flux 0B through the
central region of the inductor. The inductance of the inductor is then defined in
terms of that flux as
(inductance defined),
(30-28)
L ! N0B
i

880
CHAPTER 30
INDUCTION AND INDUCTANCE
The crude inductors with which Michael
Faraday discovered the law of induction. In
those days amenities such as insulated wire
were not commercially available. It is said
that Faraday insulated his wires by wrap-
ping them with strips cut from one of his
wife’s petticoats.
The Royal Institution/Bridgeman Art Library/NY
in which N is the number of turns. The windings of the inductor are said to be
linked by the shared flux, and the product N0B is called the magnetic flux linkage.
The inductance L is thus a measure of the flux linkage produced by the inductor
per unit of current.
Because the SI unit of magnetic flux is the tesla-square meter, the SI unit of
inductance is the tesla-square meter per ampere (T)m2/A). We call this the
henry (H), after American physicist Joseph Henry, the codiscoverer of the law of
induction and a contemporary of Faraday.Thus,
1 henry ! 1 H ! 1 T)m2/A.
(30-29)
Through the rest of this chapter we assume that all inductors, no matter what
their geometric arrangement, have no magnetic materials such as iron in their
vicinity. Such materials would distort the magnetic field of an inductor.
Inductance of a Solenoid
Consider a long solenoid of cross-sectional area A. What is the inductance
per unit length near its middle? To use the defining equation for inductance
(Eq. 30-28), we must calculate the flux linkage set up by a given current in the so-
lenoid windings. Consider a length l near the middle of this solenoid. The flux
linkage there is
N0B ! (nl)(BA),
in which n is the number of turns per unit length of the solenoid and B is the 
magnitude of the magnetic field within the solenoid.
The magnitude B is given by Eq. 29-23,
B ! m0in,
and so from Eq. 30-28,
(30-30)
Thus, the inductance per unit length near the center of a long solenoid is
(solenoid).
(30-31)
Inductance-like capacitance-depends only on the geometry of the device.
The dependence on the square of the number of turns per unit length is to be
expected. If you, say, triple n, you not only triple the number of turns (N) but you
also triple the flux (0B ! BA ! m0inA) through each turn, multiplying the flux
linkage N0B and thus the inductance L by a factor of 9.
If the solenoid is very much longer than its radius, then Eq. 30-30 gives its
inductance to a good approximation. This approximation neglects the spreading
of the magnetic field lines near the ends of the solenoid, just as the parallel-plate
capacitor formula (C ! ´0A/d) neglects the fringing of the electric field lines near
the edges of the capacitor plates.
From Eq. 30-30, and recalling that n is a number per unit length, we can see
that an inductance can be written as a product of the permeability constant m0
and a quantity with the dimensions of a length. This means that m0 can be ex-
pressed in the unit henry per meter:
(30-32)
The latter is the more common unit for the permeability constant.
! 4p $ 10 %7 H/m.
m0 ! 4p $ 10 %7 T)m/A
L
l ! m0n2A
! m0n2lA.
L ! N0B
i
! (nl)(BA)
i
! (nl)(m 0in)(A)
i

881
30-5 SELF-INDUCTION
30-5 SELF-INDUCTION
After reading this module, you should be able to . . .
30.22 Identify that an induced emf appears in a coil when
the current through the coil is changing.
30.23 Apply the relationship between the induced emf in 
a coil, the coil’s inductance L, and the rate di/dt at
which the current is changing.
30.24 When an emf is induced in a coil because the current
in the coil is changing, determine the direction of the emf
by using Lenz’s law to show that the emf always opposes
the change in the current, attempting to maintain the initial
current.
Learning Objectives
●If a current i in a coil changes with time, an emf is induced in the coil. This self-induced emf is
●The direction of 
is found from Lenz’s law: The self-induced emf acts to oppose the change that produces it.
#L
#L ! %L di
dt .
Key Ideas
Self-Induction
If two coils-which we can now call inductors-are near each other, a current i in
one coil produces a magnetic flux 0B through the second coil.We have seen that if
we change this flux by changing the current, an induced emf appears in the second
coil according to Faraday’s law.An induced emf appears in the first coil as well.
An induced emf #L appears in any coil in which the current is changing.
This process (see Fig. 30-13) is called self-induction, and the emf that appears is
called a self-induced emf. It obeys Faraday’s law of induction just as other
induced emfs do.
For any inductor, Eq. 30-28 tells us that
N0B ! Li.
(30-33)
Faraday’s law tells us that
(30-34)
By combining Eqs. 30-33 and 30-34 we can write
(self-induced emf).
(30-35)
Thus, in any inductor (such as a coil, a solenoid, or a toroid) a self-induced emf
appears whenever the current changes with time. The magnitude of the current
has no influence on the magnitude of the induced emf; only the rate of change of
the current counts.
Direction. You can find the direction of a self-induced emf from Lenz’s law.
The minus sign in Eq. 30-35 indicates that-as the law states-the self-induced
emf #L has the orientation such that it opposes the change in current i. We can
drop the minus sign when we want only the magnitude of #L.
Suppose that you set up a current i in a coil and arrange to have the current
increase with time at a rate di/dt. In the language of Lenz’s law, this increase in
the current in the coil is the “change” that the self-induction must oppose.
Thus, a self-induced emf must appear in the coil, pointing so as to oppose the
increase in the current, trying (but failing) to maintain the initial condition, as
#L ! %L di
dt
# L ! % d(N0B)
dt
.
Figure 30-13 If the current in a coil is changed
by varying the contact position on a vari-
able resistor,a self-induced emf #L will ap-
pear in the coil while the current is changing.
i
i
L
-
+
R

882
CHAPTER 30
INDUCTION AND INDUCTANCE
Figure 30-14 (a) The current i is increasing,
and the self-induced emf #L appears along
the coil in a direction such that it opposes
the increase.The arrow representing #L can
be drawn along a turn of the coil or along-
side the coil. Both are shown. (b) The cur-
rent i is decreasing, and the self-induced
emf appears in a direction such that it
opposes the decrease.
i (increasing)
(a)
i (decreasing)
(b)
L
L
L
L
The changing 
current changes 
the flux, which
creates an emf 
that opposes 
the change.
Checkpoint 5
The figure shows an emf #L induced in a coil.Which of
the following can describe the current through the coil:
(a) constant and rightward, (b) constant and leftward,
(c) increasing and rightward, (d) decreasing and rightward, (e) increasing and left-
ward, (f) decreasing and leftward?
L
30-6 RL CIRCUITS
After reading this module, you should be able to . . .
30.25 Sketch a schematic diagram of an RL circuit in which
the current is rising.
30.26 Write a loop equation (a differential equation) for an
RL circuit in which the current is rising.
30.27 For an RL circuit in which the current is rising, apply
the equation i(t) for the current as a function of time.
30.28 For an RL circuit in which the current is rising, find equa-
tions for the potential difference V across the resistor, the rate
di/dt at which the current changes, and the emf of the inductor,
as functions of time.
30.29 Calculate an inductive time constant tL.
30.30 Sketch a schematic diagram of an RL circuit in which
the current is decaying.
30.31 Write a loop equation (a differential equation) for an
RL circuit in which the current is decaying.
30.32 For an RL circuit in which the current is decaying,
apply the equation i(t) for the current as a function of time.
30.33 From an equation for decaying current in an RL circuit,
find equations for the potential difference V across the
resistor, the rate di/dt at which current is changing, and the
emf of the inductor, as functions of time.
30.34 For an RL circuit, identify the current through the induc-
tor and the emf across it just as current in the circuit begins
to change (the initial condition) and a long time later when
equilibrium is reached (the final condition).
Learning Objectives
shown in Fig. 30-14a. If, instead, the current decreases with time, the self-induced
emf must point in a direction that tends to oppose the decrease (Fig. 30-14b),
again trying to maintain the initial condition.
Electric Potential. In Module 30-3 we saw that we cannot define an electric
potential for an electric field (and thus for an emf) that is induced by a changing
magnetic flux.This means that when a self-induced emf is produced in the induc-
tor of Fig. 30-13, we cannot define an electric potential within the inductor itself,
where the flux is changing. However, potentials can still be defined at points of
the circuit that are not within the inductor-points where the electric fields are
due to charge distributions and their associated electric potentials.
Moreover, we can define a self-induced potential difference VL across an
inductor (between its terminals, which we assume to be outside the region of
changing flux). For an ideal inductor (its wire has negligible resistance), the mag-
nitude of VL is equal to the magnitude of the self-induced emf #L.
If, instead, the wire in the inductor has resistance r, we mentally separate the
inductor into a resistance r (which we take to be outside the region of changing
flux) and an ideal inductor of self-induced emf #L. As with a real battery of emf
# and internal resistance r, the potential difference across the terminals of a real
inductor then differs from the emf. Unless otherwise indicated, we assume here
that inductors are ideal.
●If a constant emf 
is introduced into a single-loop circuit
containing a resistance R and an inductance L, the current
rises to an equilibrium value of #/R according to
(rise of current).
i ! #
R  (1 % e%t/tL)
#
Key Ideas
Here tL (
L/R) governs the rate of rise of the current and is
called the inductive time constant of the circuit. 
●When the source of constant emf is removed, the current
decays from a value i0 according to
(decay of current).
i ! i0e%t/tL
!

883
30-6 RL CIRCUITS
RL Circuits
In Module 27-4 we saw that if we suddenly introduce an emf # into a single-loop
circuit containing a resistor R and a capacitor C, the charge on the capacitor does
not build up immediately to its final equilibrium value C# but approaches it in an
exponential fashion:
(30-36)
The rate at which the charge builds up is determined by the capacitive time
constant tC, defined in Eq. 27-36 as
tC ! RC.
(30-37)
If we suddenly remove the emf from this same circuit, the charge does not
immediately fall to zero but approaches zero in an exponential fashion:
(30-38)
The time constant tC describes the fall of the charge as well as its rise.
An analogous slowing of the rise (or fall) of the current occurs if we intro-
duce an emf # into (or remove it from) a single-loop circuit containing a resis-
tor R and an inductor L. When the switch S in Fig. 30-15 is closed on a, for
example, the current in the resistor starts to rise. If the inductor were not pres-
ent, the current would rise rapidly to a steady value #/R. Because of the induc-
tor, however, a self-induced emf #L appears in the circuit; from Lenz’s law, this
emf opposes the rise of the current, which means that it opposes the battery
emf # in polarity.Thus, the current in the resistor responds to the difference be-
tween two emfs, a constant # due to the battery and a variable #L (! %L di/dt)
due to self-induction. As long as this #L is present, the current will be less
than #/R.
As time goes on, the rate at which the current increases becomes less rapid
and the magnitude of the self-induced emf, which is proportional to di/dt,
becomes smaller. Thus, the current in the circuit approaches #/R asymptotically.
We can generalize these results as follows:
q ! q0e%t/tC.
q ! C#(1 % e%t/tC).
Initially, an inductor acts to oppose changes in the current through it. A long time
later, it acts like ordinary connecting wire.
Figure 30-15 An RL circuit.When switch S is
closed on a,the current rises and approaches
a limiting value #/R.
S
a
b
R
L
-
+
Now let us analyze the situation quantitatively.With the switch S in Fig. 30-15
thrown to a, the circuit is equivalent to that of Fig. 30-16. Let us apply the loop
rule, starting at point x in this figure and moving clockwise around the loop along
with current i.
1. Resistor. Because we move through the resistor in the direction of current i,
the electric potential decreases by iR. Thus, as we move from point x to
point y, we encounter a potential change of %iR.
2. Inductor. Because current i is changing, there is a self-induced emf 
L in the
inductor.The magnitude of #L is given by Eq. 30-35 as L di/dt.The direction of
#L is upward in Fig. 30-16 because current i is downward through the inductor
and increasing. Thus, as we move from point y to point z, opposite the direc-
tion of #L, we encounter a potential change of %L di/dt.
3. Battery. As we move from point z back to starting point x, we encounter a
potential change of &# due to the battery’s emf.
Thus, the loop rule gives us
%iR % L di
dt & # ! 0
#
Figure 30-16 The circuit of Fig.30-15 with the
switch closed on a.We apply the loop rule
for the circuit clockwise,starting at x.
R
L
-
+
i
y
x
z
L

884
CHAPTER 30
INDUCTION AND INDUCTANCE
Figure 30-17 The variation with time of (a) VR, the potential difference across the resistor in
the circuit of Fig. 30-16, and (b) VL, the potential difference across the inductor in that cir-
cuit.The small triangles represent successive intervals of one inductive time constant tL !
L/R.The figure is plotted for R ! 2000 1, L ! 4.0 H, and # ! 10 V.
10
8
6
4
2
0
2 
4 
6 
8 
VR (V)
t (ms) 
(a)
0
2
4
6
8
VL (V)
t (ms)
(b)
10
8
6
4
2
The resistor’s potential
difference turns on.
The inductor’s potential
difference turns off.
or
(RL circuit).
(30-39)
Equation 30-39 is a differential equation involving the variable i and its first
derivative di/dt. To solve it, we seek the function i(t) such that when i(t) and its
first derivative are substituted in Eq. 30-39, the equation is satisfied and the initial
condition i(0) ! 0 is satisfied.
Equation 30-39 and its initial condition are of exactly the form of Eq. 27-32
for an RC circuit, with i replacing q, L replacing R, and R replacing 1/C.The solu-
tion of Eq. 30-39 must then be of exactly the form of Eq. 27-33 with the same
replacements.That solution is
(30-40)
which we can rewrite as
(rise of current).
(30-41)
Here tL, the inductive time constant, is given by
(time constant).
(30-42)
Let’s examine Eq. 30-41 for just after the switch is closed (at time t ! 0) and
for a time long after the switch is closed 
. If we substitute t ! 0 into
Eq. 30-41, the exponential becomes e%0
1. Thus, Eq. 30-41 tells us that the cur-
rent is initially i ! 0, as we expected. Next, if we let t go to ., then the exponential
goes to e%. ! 0. Thus, Eq. 30-41 tells us that the current goes to its equilibrium
value of #/R.
We can also examine the potential differences in the circuit. For example,
Fig. 30-17 shows how the potential differences VR (! iR) across the resistor and
VL (! L di/dt) across the inductor vary with time for particular values of #, L,
and R. Compare this figure carefully with the corresponding figure for an RC
circuit (Fig. 27-16).
!
(t : .)
tL ! L
R
i ! #
R  (1 % e%t/tL)
i ! #
R  (1 % e%Rt/L),
L di
dt & Ri ! #

885
30-6 RL CIRCUITS
To show that the quantity tL (! L/R) has the dimension of time (as it must,
because the argument of the exponential function in Eq. 30-41 must be dimen-
sionless), we convert from henries per ohm as follows:
The first quantity in parentheses is a conversion factor based on Eq. 30-35, and
the second one is a conversion factor based on the relation V ! iR.
Time Constant. The physical significance of the time constant follows from
Eq. 30-41. If we put t ! tL ! L/R in this equation, it reduces to
(30-43)
Thus, the time constant tL is the time it takes the current in the circuit to reach
about 63% of its final equilibrium value #/R. Since the potential difference VR
across the resistor is proportional to the current i, a graph of the increasing
current versus time has the same shape as that of VR in Fig. 30-17a.
Current Decay. If the switch S in Fig. 30-15 is closed on a long enough for the
equilibrium current #/R to be established and then is thrown to b, the effect will
be to remove the battery from the circuit. (The connection to b must actually be
made an instant before the connection to a is broken. A switch that does this is
called a make-before-break switch.) With the battery gone, the current through
the resistor will decrease. However, it cannot drop immediately to zero but must
decay to zero over time. The differential equation that governs the decay can be
found by putting # ! 0 in Eq. 30-39:
(30-44)
By analogy with Eqs. 27-38 and 27-39, the solution of this differential equation
that satisfies the initial condition i(0) ! i0 ! #/R is
(decay of current).
(30-45)
We see that both current rise (Eq. 30-41) and current decay (Eq. 30-45) in an RL
circuit are governed by the same inductive time constant, tL.
We have used i0 in Eq. 30-45 to represent the current at time t ! 0. In our
case that happened to be #/R, but it could be any other initial value.
i ! #
R e%t/tL ! i0e%t/tL
L di
dt & iR ! 0.
i ! #
R  (1 % e%1) ! 0.63 #
R .
1 H
1 ! 1 H
1 #
1 V) s
1 H)A$#
1 1)A
1 V $ ! 1 s.
Checkpoint 6
The figure shows three circuits with identical batteries, inductors, and resistors. Rank
the circuits according to the current through the battery (a) just after the switch is
closed and (b) a long time later, greatest first. (If you have trouble here, work through
the next sample problem and then try again.)
(1)
(2)
(3)

886
CHAPTER 30
INDUCTION AND INDUCTANCE
Calculations: We now have a circuit with three identical 
resistors in parallel; from Eq. 27-23, their equivalent resist-
ance is Req ! R/3 ! (9.0 1)/3 ! 3.0 1. The equivalent
circuit shown in Fig. 30-18d then yields the loop equation 
# % iReq ! 0, or
(Answer)
i !
#
Req
! 18 V
3.0 1 ! 6.0 A.
Figure 30-18a shows a circuit that contains three identical
resistors with resistance R ! 9.0 1, two identical inductors
with inductance L ! 2.0 mH, and an ideal battery with emf
# ! 18 V.
(a) What is the current i through the battery just after the
switch is closed?
KEY IDEA
Just after the switch is closed, the inductor acts to oppose a
change in the current through it.
Calculations: Because the current through each inductor
is zero before the switch is closed, it will also be zero just
afterward. Thus, immediately after the switch is closed, the
inductors act as broken wires, as indicated in Fig. 30-18b.
We then have a single-loop circuit for which the loop rule
gives us
# % iR ! 0.
Substituting given data, we find that
(Answer)
(b) What is the current i through the battery long after the
switch has been closed?
KEY IDEA
Long after the switch has been closed, the currents in the
circuit have reached their equilibrium values, and the
inductors act as simple connecting wires, as indicated in
Fig. 30-18c.
i ! #
R ! 18 V
9.0 1 ! 2.0 A.
Figure 30-18 (a) A multiloop RL circuit with an open switch. (b) The
equivalent circuit just after the switch has been closed. (c) The
equivalent circuit a long time later. (d) The single-loop circuit that
is equivalent to circuit (c).
L
-
+
R
R
R
L
-
+
R
R
R
(a)
(b)
-
+
R
R
R
(c)
-
+
R/3
(d)
Initially, an inductor
acts like broken wire.
Long later, it acts
like ordinary wire.
