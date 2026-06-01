882

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

i (increasing)

L

L

(a)

i (decreasing)

The changing
current changes
the flux, which
creates an emf
that opposes
the change.

L

L

(b)

Figure 30-14 (a) The current i is increasing,
and the self-induced emf #L appears along
the coil in a direction such that it opposes
the increase. The arrow representing #L can
be drawn along a turn of the coil or along-
side the coil. Both are shown. (b) The cur-
rent i is decreasing, and the self-induced
emf appears in a direction such that it
opposes the decrease.

shown in Fig. 30-14a. If, instead, the current decreases with time, the self-induced
emf  must  point  in  a  direction  that  tends  to  oppose  the  decrease  (Fig. 30-14b),
again trying to maintain the initial condition.

Electric Potential. In Module 30-3 we saw that we cannot define an electric
potential for an electric field (and thus for an emf) that is induced by a changing
magnetic flux. This means that when a self-induced emf is produced in the induc-
tor of Fig. 30-13, we cannot define an electric potential within the inductor itself,
where the flux is changing. However, potentials can still be defined at points of
the circuit that are not within the inductor — points where the electric fields are
due to charge distributions and their associated electric potentials.

Moreover, we  can  define  a  self-induced  potential  difference  VL across  an
inductor (between  its  terminals, which  we  assume  to  be  outside  the  region  of
changing flux). For an ideal inductor (its wire has negligible resistance), the mag-
nitude of VL is equal to the magnitude of the self-induced emf #L.

If, instead, the wire in the inductor has resistance r, we mentally separate the
inductor into a resistance r (which we take to be outside the region of changing
flux) and an ideal inductor of self-induced emf #L. As with a real battery of emf
# and internal resistance r, the potential difference across the terminals of a real
inductor then differs from the emf. Unless otherwise indicated, we assume here
that inductors are ideal.

Checkpoint 5

The figure shows an emf #L induced in a coil. Which of
the following can describe the current through the coil:
(a) constant and rightward, (b) constant and leftward,
(c) increasing and rightward, (d) decreasing and rightward, (e) increasing and left-
ward, (f) decreasing and leftward?

L

30-6 RL CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .
30.25 Sketch a schematic diagram of an RL circuit in which

the current is rising.

30.31 Write a loop equation (a differential equation) for an

RL circuit in which the current is decaying.

30.26 Write a loop equation (a differential equation) for an

30.32 For an RL circuit in which the current is decaying,

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

Key Ideas
● If a constant emf
is introduced into a single-loop circuit
containing a resistance R and an inductance L, the current
rises to an equilibrium value of #/R according to

#

i !

#
R

 (1 % e%t/tL)

(rise of current).

apply the equation i(t) for the current as a function of time.
30.33 From an equation for decaying current in an RL circuit,
find equations for the potential difference V across the
resistor, the rate di/dt at which current is changing, and the
emf of the inductor, as functions of time.

30.34 For an RL circuit, identify the current through the induc-
tor and the emf across it just as current in the circuit begins
to change (the initial condition) and a long time later when
equilibrium is reached (the final condition).

Here tL ( L/R) governs the rate of rise of the current and is
called the inductive time constant of the circuit.

!

● When the source of constant emf is removed, the current
decays from a value i0 according to

i ! i0 e%t/tL

(decay of current).

RL Circuits
In Module 27-4 we saw that if we suddenly introduce an emf # into a single-loop
circuit containing a resistor R and a capacitor C, the charge on the capacitor does
not build up immediately to its final equilibrium value C# but approaches it in an
exponential fashion:

q ! C# (1 % e%t/tC).

(30-36)

The  rate  at  which  the  charge  builds  up  is  determined  by  the  capacitive  time
constant tC, defined in Eq. 27-36 as

tC ! RC.

(30-37)

If we suddenly remove the emf from this same circuit, the charge does not

immediately fall to zero but approaches zero in an exponential fashion:

q ! q0e%t/tC.

(30-38)

The time constant tC describes the fall of the charge as well as its rise.

An analogous slowing of the rise (or fall) of the current occurs if we intro-
duce an emf # into (or remove it from) a single-loop circuit containing a resis-
tor R and  an  inductor  L. When  the  switch  S  in  Fig. 30-15  is  closed  on  a, for
example, the current in the resistor starts to rise. If the inductor were not pres-
ent, the current would rise rapidly to a steady value #/R. Because of the induc-
tor, however, a self-induced emf #L appears in the circuit; from Lenz’s law, this
emf  opposes  the  rise  of  the  current, which  means  that  it  opposes  the  battery
emf # in polarity. Thus, the current in the resistor responds to the difference be-
tween two emfs, a constant # due to the battery and a variable #L (! %L di/dt)
due  to  self-induction. As  long  as  this  #L is  present, the  current  will  be  less
than #/R.

As time goes on, the rate at which the current increases becomes less rapid
and  the  magnitude  of  the  self-induced  emf, which  is  proportional  to  di/dt,
becomes smaller. Thus, the current in the circuit approaches #/R asymptotically.

We can generalize these results as follows:

Initially, an inductor acts to oppose changes in the current through it. A long time
later, it acts like ordinary connecting wire.

Now let us analyze the situation quantitatively. With the switch S in Fig. 30-15
thrown to a, the circuit is equivalent to that of Fig. 30-16. Let us apply the loop
rule, starting at point x in this figure and moving clockwise around the loop along
with current i.

1. Resistor. Because we move through the resistor in the direction of current i,
the  electric  potential  decreases  by  iR. Thus, as  we  move  from  point  x to
point y, we encounter a potential change of %iR.

2. Inductor. Because current i is changing, there is a self-induced emf  L in the
inductor. The magnitude of #L is given by Eq. 30-35 as L di/dt. The direction of
#L is upward in Fig. 30-16 because current i is downward through the inductor
and increasing. Thus, as we move from point y to point z, opposite the direc-
tion of #L, we encounter a potential change of %L di/dt.

#

3. Battery. As  we  move  from  point  z back  to  starting  point  x, we  encounter  a

potential change of &# due to the battery’s emf.

Thus, the loop rule gives us

%iR % L

di
dt

& # ! 0

30-6 R L CI RCU ITS

883

Sa
b

+
–

R

L

Figure 30-15 An RL circuit. When switch S is
closed on a, the current rises and approaches
a limiting value #/R.

i

R

x

+
–

L

y

z

L

Figure 30-16 The circuit of Fig. 30-15 with the
switch closed on a.We apply the loop rule
for the circuit clockwise, starting at x.

884

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

or

L

di
dt

& Ri ! #

(RL circuit).

(30-39)

Equation  30-39  is  a  differential  equation  involving  the  variable  i and  its  first
derivative di/dt. To solve it, we seek the function i(t) such that when i(t) and its
first derivative are substituted in Eq. 30-39, the equation is satisfied and the initial
condition i(0) ! 0 is satisfied.

Equation 30-39 and its initial condition are of exactly the form of Eq. 27-32
for an RC circuit, with i replacing q, L replacing R, and R replacing 1/C. The solu-
tion  of  Eq. 30-39  must  then  be  of  exactly  the  form  of  Eq. 27-33  with  the  same
replacements. That solution is

i !

#
R

 (1 % e%Rt/L),

(30-40)

which we can rewrite as

i !

#
R

 (1 % e%t/tL)

(rise of current).

(30-41)

Here tL, the inductive time constant, is given by

tL !

L
R

(time constant).

(30-42)

Let’s examine Eq. 30-41 for just after the switch is closed (at time t ! 0) and
. If  we  substitute  t ! 0  into
for  a  time  long  after  the  switch  is  closed
Eq. 30-41, the exponential becomes e%0
!
1. Thus, Eq. 30-41 tells us that the cur-
rent is initially i ! 0, as we expected. Next, if we let t go to ., then the exponential
goes to e%. ! 0. Thus, Eq. 30-41 tells us that the current goes to its equilibrium
value of #/R.

(t : .)

We  can  also  examine  the  potential  differences  in  the  circuit. For  example,
Fig. 30-17 shows how the potential differences VR (! iR) across the resistor and
VL (! L di/dt) across the inductor vary with time for particular values of #, L,
and R. Compare  this  figure  carefully  with  the  corresponding  figure  for  an  RC
circuit (Fig. 27-16).

The resistor’s potential
difference turns on.
The inductor’s potential
difference turns off.

)
V
(

R
V

10
8
6
4
2

)
V
(

L
V

10
8
6
4
2

0

2

8

4
6
t (ms)

(a )

0

2

8

4
6
t (ms)

(b )

Figure 30-17 The variation with time of (a) VR, the potential difference across the resistor in
the circuit of Fig. 30-16, and (b) VL, the potential difference across the inductor in that cir-
cuit. The small triangles represent successive intervals of one inductive time constant tL !
L/R. The figure is plotted for R ! 2000 1, L ! 4.0 H, and # ! 10 V.

To show that the quantity tL (! L/R) has the dimension of time (as it must,
because the argument of the exponential function in Eq. 30-41 must be dimen-
sionless), we convert from henries per ohm as follows:

30-6 R L CI RCU ITS

885

1

H
1

! 1

H

1 # 1 V) s

1 H)A $ # 1 1)A

1 V $ ! 1 s.

The first quantity in parentheses is a conversion factor based on Eq. 30-35, and
the second one is a conversion factor based on the relation V ! iR.

Time Constant. The physical significance of the time constant follows from

Eq. 30-41. If we put t ! tL ! L/R in this equation, it reduces to

i !

#
R

 (1 % e%1) ! 0.63

#
R

.

(30-43)

Thus, the time constant tL is the time it takes the current in the circuit to reach
about 63% of its final equilibrium value #/R. Since the potential difference VR
across  the  resistor  is  proportional  to  the  current  i, a  graph  of  the  increasing
current versus time has the same shape as that of VR in Fig. 30-17a.

Current Decay. If the switch S in Fig. 30-15 is closed on a long enough for the
equilibrium current #/R to be established and then is thrown to b, the effect will
be to remove the battery from the circuit. (The connection to b must actually be
made an instant before the connection to a is broken. A switch that does this is
called a make-before-break switch.) With the battery gone, the current through
the resistor will decrease. However, it cannot drop immediately to zero but must
decay to zero over time. The differential equation that governs the decay can be
found by putting # ! 0 in Eq. 30-39:

L

di
dt

& iR ! 0.

(30-44)

By analogy with Eqs. 27-38 and 27-39, the solution of this differential equation
that satisfies the initial condition i(0) ! i0 ! #/R is

i !

#
R

e%t/tL ! i0e%t/tL

(decay of current).

(30-45)

We see that both current rise (Eq. 30-41) and current decay (Eq. 30-45) in an RL
circuit are governed by the same inductive time constant, tL.

We have used i0 in Eq. 30-45 to represent the current at time t ! 0. In our

case that happened to be #/R, but it could be any other initial value.

Checkpoint 6

The figure shows three circuits with identical batteries, inductors, and resistors. Rank
the circuits according to the current through the battery (a) just after the switch is
closed and (b) a long time later, greatest first. (If you have trouble here, work through
the next sample problem and then try again.)

(1)

(2)

(3)

886

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

Sample Problem 30.05 RL circuit, immediately after switching and after a long time

Figure  30-18a shows  a  circuit  that  contains  three  identical
resistors with resistance R ! 9.0 1, two identical inductors
with inductance L ! 2.0 mH, and an ideal battery with emf
# ! 18 V.

(a) What is the current i through the battery just after the
switch is closed?

KEY IDEA

Just after the switch is closed, the inductor acts to oppose a
change in the current through it.

Calculations: Because  the  current  through  each  inductor
is zero before the switch is closed, it will also be zero just
afterward. Thus, immediately after the switch is closed, the
inductors  act  as  broken  wires, as  indicated  in  Fig. 30-18b.
We then have a single-loop circuit for which the loop rule
gives us

# % iR ! 0.

Substituting given data, we find that

i !

#
R

!

18 V
9.0 1

! 2.0 A.

(Answer)

(b) What is the current i through the battery long after the
switch has been closed?

KEY IDEA

Long after the switch has been closed, the currents in the
circuit  have  reached  their  equilibrium  values, and  the
inductors  act  as  simple  connecting  wires, as  indicated  in
Fig. 30-18c.

+
–

(a)

+
–

(c)

L

R

R

R

R

R

Initially, an inductor
acts like broken wire.

+
–

(b)

R

L

R

R

R

Long later, it acts
like ordinary wire.

R/3

+
–

(d)

Figure 30-18 (a) A multiloop RL circuit with an open switch. (b) The
equivalent circuit just after the switch has been closed. (c) The
equivalent circuit a long time later. (d) The single-loop circuit that
is equivalent to circuit (c).

Calculations: We  now  have  a  circuit  with  three  identical
resistors in parallel; from Eq. 27-23, their equivalent resist-
ance  is  Req ! R/3 ! (9.0 1)/3 ! 3.0 1. The  equivalent
circuit shown in Fig. 30-18d then yields the loop equation
# % iReq ! 0, or

i !

#
Req

!

18 V
3.0 1

! 6.0 A.

(Answer)

Sample Problem 30.06 RL circuit, current during the transition

A solenoid has an inductance of 53 mH and a resistance of
0.37 1. If  the  solenoid  is  connected  to  a  battery, how  long
will  the  current  take  to  reach  half  its  final  equilibrium
value? (This is a real solenoid because we are considering its
small, but nonzero, internal resistance.)

KEY IDEA

Calculations: According  to  that  solution, current  i
in-
creases  exponentially  from  zero  to  its  final  equilibrium
value of #/R. Let t0 be the time that current i takes to reach
half its equilibrium value. Then Eq. 30-41 gives us

1
2

#
R

!

#
R

 (1 % e%t0 /tL).

We can mentally separate the solenoid into a resistance and
an  inductance  that  are  wired  in  series  with  a  battery, as  in
Fig. 30-16. Then  application  of  the  loop  rule  leads  to
Eq. 30-39, which has the solution of Eq. 30-41 for the current
i in the circuit.

We solve for t0 by canceling #/R, isolating the exponential,
and taking the natural logarithm of each side. We find

t0 ! tL ln 2 !

! 0.10 s.

L
R

 ln 2 !

53 $ 10 %3 H
0.37 1

 ln 2

(Answer)

Additional examples, video, and practice available at WileyPLUS
