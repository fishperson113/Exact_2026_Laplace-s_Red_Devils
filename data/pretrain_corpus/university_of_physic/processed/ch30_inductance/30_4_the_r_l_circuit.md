SOLUTION

IDENTIFY and SET UP: We are given the required amount of stored
energy
A. We use Eq. (30.9) to ﬁnd the
U
self-inductance

and the current
.
L

I = 200

EXECUTE: We  have
103 W213600 s2 = 3.60 * 106 J.
ﬁnd

I = 200 A

and

U = 1.00 kW # h = 11.00 *
Solving  Eq.  (30.9) for
we

L,

L = 2U
I 2

=

213.60 * 106 J2
1200 A22

= 180 H

30.4 The R-L Circuit

1001

EVALUATE: The required inductance is more than a million times
greater  than  the  self-inductance  of  the  toroidal  solenoid  of
Example 30.3. Conventional wires that are to carry 200 A would have
to be of large diameter to keep the resistance low and avoid unaccept-
able energy losses due to
heating. As a result, a 180-H inductor
using conventional wire would be very large (room-size). A super-
conducting inductor could be much smaller, since the resistance of
a superconductor is zero and much thinner wires could be used; but
the wires would have to be kept at low temperature to remain super-
conducting,  and  maintaining  this  temperature  would  itself  require
energy. This scheme is impractical with present technology.

I 2R

Test Your Understanding of Section 30.3 The current in a solenoid is
reversed in direction while keeping the same magnitude. (a) Does this change the
magnetic ﬁeld within the solenoid? (b) Does this change the magnetic energy density in
the solenoid?

❙

30.4 The R-L Circuit

Let’s look at some examples of the circuit behavior of an inductor. One thing is
clear already; an inductor in a circuit makes it difﬁcult for rapid changes in cur-
rent  to  occur,  thanks  to  the  effects  of  self-induced  emf.  Equation  (30.7) shows
the greater the self-induced
that the greater the rate of change of current
emf and the greater the potential difference between the inductor terminals. This
equation, together with Kirchhoff’s rules (see Section 26.2), gives us the princi-
ples we need to analyze circuits containing inductors.

di>dt,

ActivPhysics 14.1: The RLCircuit

Problem-Solving Strategy 30.1

Inductors in Circuits

IDENTIFY the relevant concepts: An inductor is just another circuit
element,  like  a  source  of  emf,  a  resistor,  or  a  capacitor.  One  key
difference is that when an inductor is included in a circuit, all the
voltages,  currents,  and  capacitor  charges  are  in  general  functions
of time, not constants as they have been in most of our previous
circuit  analysis.  But  Kirchhoff’s  rules  (see  Section  26.2)  are  still
valid. When the voltages and currents vary with time, Kirchhoff’s
rules hold at each instant of time.

SET UP the problem using the following steps:
1. Follow  the  procedure  described  in  Problem-Solving  Strategy
26.2 (Section 26.2). Draw a circuit diagram and label all quan-
tities,  known  and  unknown. Apply  the  junction  rule  immedi-
ately so as to express the currents in terms of as few quantities
as possible.

2. Determine which quantities are the target variables.

EXECUTE the solution as follows:
1. As  in  Problem-Solving  Strategy  26.2,  apply  Kirchhoff’s  loop

rule to each loop in the circuit.

2. Review the sign rules given in Problem-Solving Strategy 26.2.
To get the correct sign for the potential difference between the
terminals  of  an  inductor,  apply  Lenz’s  law  and  the  sign  rule
described  in  Section  30.2  in  connection  with  Eq.  (30.7) and
Fig.  30.6.  In  Kirchhoff’s  loop  rule,  when  we  go  through  an
inductor  in  the  same direction  as  the  assumed  current,  we
so the corresponding
encounter a voltage drop equal to
term in the loop equation is
When we go through an
inductor in the opposite direction from the assumed current, the
potential difference is reversed and the term to use in the loop
equation is

-L di>dt.

+L di>dt.

L di>dt,

3. Solve for the target variables.

EVALUATE your answer: Check whether your answer is consistent
with  the  behavior  of  inductors.  By  Lenz’s  law,  if  the  current
through  an  inductor  is  changing,  your  result  should  indicate  that
the potential difference across the inductor opposes the change.

Current Growth in an R-L Circuit
We can learn several basic things about inductor behavior by analyzing the cir-
cuit of Fig. 30.11. A circuit that includes both a resistor and an inductor, and pos-
sibly  a  source  of  emf,  is  called  an  R-L circuit. The  inductor  helps  to  prevent
rapid changes in current, which can be useful if a steady current is required but
the external source has a ﬂuctuating emf. The resistor  may be a separate circuit

R

1002

CHAPTER 30 Inductance

30.11 An R-L circuit.

Closing switch S1 connects the R-L combination
in series with a source of emf E.

E

+

a

R

b

i

c

S1

L

S2

element,  or  it  may  be  the  resistance  of  the  inductor  windings;  every  real-life
inductor has some resistance unless it is made of superconducting wire. By clos-
ing switch
we can connect the R-L combination to a source with constant emf
E.
(We assume that the source has zero internal resistance, so the terminal voltage
equals the emf.)

S1,

we close switch
di>dt

Suppose both switches are open to begin with, and then at some initial time
t = 0
S1.
The current cannot change suddenly from zero to some
ﬁnal value, since
and the induced emf in the inductor would both be inﬁ-
nite. Instead, the current begins to grow at a rate that depends only on the value
of

in the circuit.

L
Let i be the current at some time t after switch
S1
rate of change at that time. The potential difference
time is

is closed, and let
vab

be its
across the resistor at that

di>dt

Closing switch S2 while opening switch S1
disconnnects the combination from the source.

and the potential difference

vbc

vab = iR
across the inductor is

vbc = L

di
dt

vab

and

Note that if the current is in the direction shown in Fig. 30.11 and is increasing,
then both
are positive; a is at a higher potential than b, which in turn
is at a higher potential than c. (Compare to Figs. 30.6a and c.) We apply Kirch-
hoff’s loop rule, starting at the negative terminal and proceeding counterclock-
wise around the loop:

vbc

E - iR - L

di
dt

= 0

(30.12)

Solving this for

di>dt,

we ﬁnd that the rate of increase of current is

=

di
dt

E - iR
L

=

E

- R
L
L
i = 0

i

(30.13)

and the potential drop across

At the instant that switch
is zero. The initial rate of change of current is

is ﬁrst closed,

S1

R

a di
dt

b

initial

=

E

L

As we would expect, the greater the inductance
increases.

L,

the more slowly the current

As the current increases, the term

1R>L2i
in Eq. (30.13) also increases, and the
rate of  increase  of  current  given  by  Eq.  (30.13) becomes  smaller  and  smaller.
This means that the current is approaching a ﬁnal, steady-state value  When the
current reaches this value, its rate of increase is zero. Then Eq. (30.13) becomes

I.

I  and

- R
L

a di
dt

b

final

= 0 =

I =

E

L
E

R

The ﬁnal current  does not depend on the inductance
be if the resistance  alone were connected to the source with emf

it is the same as it would
E.

L;

R

I

Figure 30.12 shows the behavior of the current as a function of time. To derive
the  equation  for  this  curve  (that  is,  an  expression  for  current  as  a  function  of
time), we proceed just as we did for the charging capacitor in Section 26.4. First
we rearrange Eq. (30.13) to the form

30.12 Graph of i versus t for growth of
current in an R-L circuit with an emf in
series. The ﬁnal current is
one time constant
of this value.

I = E>R;
the current is

after
1 - 1>e

t,

Switch S1 is closed at t 5 0.

E

+

S1

R

i

L

i

I 5

E
R

t

(           )

1 2I

1
e

O

t 5 t 5 L
R

t

di
i - 1E>R2

= - R
L

dt

This separates the variables, with i on the left side and t on the right. Then we
so that we can
integrate both sides, renaming the integration variables
use i and t as the upper limits. (The lower limit for each integral is zero, corre-
sponding to zero current at the initial time

t = 0.)

We get

and

t¿

i¿

30.4 The R-L Circuit

1003

i

L
0

 ln a

di¿
i¿ - 1E>R2
i - 1E>R2
-E>R

= -

L
0
b = - R
L

t

t

R
L

dt¿

Now we take exponentials of both sides and solve for i. We leave the details for
you to work out; the ﬁnal result is

11 - e-1R>L2t2

i =

E

R

(current in an

R-L

circuit with emf )

(30.14)

This is the equation of the curve in Fig. 30.12. Taking the derivative of Eq. (30.14),
we ﬁnd

=

di
dt

E

L

e-1R>L2t

(30.15)

i = 0

and

di>dt = E>L.

As

t S q,

i S E>R

and

di>dt S 0,

as we

t = 0,

At time
predicted.

As Fig. 30.12 shows, the instantaneous current i ﬁrst rises rapidly, then increases
asymptotically.  At  a  time
or about 63%, of its ﬁnal value.
is therefore a measure of how quickly the current builds toward
t:

more  slowly  and  approaches  the  ﬁnal  value
L>R
equal to
The quantity
its ﬁnal value; this quantity is called the time constant for the circuit, denoted by

, the current has risen to
L>R

11 - 1>e2,

I = E>R

    (time constant for an R-L circuit)

t = L
R

(30.16)

2t,

10t,

In a time equal to
in
tor of capacitance
constant for that situation was the product

99.3%; and
the current reaches 86% of its ﬁnal value; in
99.995%. (Compare the discussion in Section 26.4 of charging a capaci-
that was in series with a resistor of resistance
the time
RC.)

R;

C

5t,

R,

The graphs of i versus t have the same general shape for all values of  For a
L.
is
is large, it rises more

is greater for greater values of  When
L

the time constant

given value of
small, the current rises rapidly to its ﬁnal value; when
R = 100 Æ
slowly. For example, if
t = L
R

and
= 10 H
100 Æ

L = 10 H,

= 0.10 s

L.

L

t

and the current increases to about 63% of its ﬁnal value in 0.10 s. (Recall that
1 H = 1 Æ # s.2
and the rise
is much more rapid.

L = 0.010 H, t = 1.0 * 10-4 s = 0.10 ms,

But if

Energy considerations offer us additional insight into the behavior of an R-L
circuit. The instantaneous rate at which the source delivers energy to the circuit is
P = Ei.
i 2R,
and  the  rate  at  which  energy  is  stored  in  the  inductor  is
[or,
2 Li 2B = Li di>dt
equivalently,
]. When we multiply Eq. (30.12) by i and
rearrange, we ﬁnd

The instantaneous rate at which energy is dissipated in the resistor is
ivbc = Li di>dt

1d>dt2A 1

Ei = i 2R + Li

di
dt
1i 2R2
Ei
Of the power
supplied by the source, part
is dissipated in the resistor and
1Li di>dt2
goes to store energy in the inductor. This discussion is completely
part
analogous  to  our  power  analysis  for  a  charging  capacitor,  given  at  the  end  of
Section 26.4.

(30.17)

1004

CHAPTER 30 Inductance

Example 30.6

Analyzing an R-L circuit

R = 175 Æ

A sensitive  electronic  device  of  resistance
is  to  be
connected to a source of emf (of negligible internal resistance) by
a switch. The device is designed to operate with a 36-mA current,
but to avoid damage to the device, the current can rise to no more
than 4.9 mA in the ﬁrst
after the switch is closed. An inductor
is  therefore  connected  in  series  with  the  device,  as  in  Fig.  30.11;
?E
the switch in question is
(b) What  is  the  required  inductance  L?  (c) What  is  the  R-L time
constant

(a) What is the required source emf

58 ms

S1.

t?

SOLUTION

. The graph shows that the ﬁnal current is
= 175 Æ

IDENTIFY and SET UP: This problem concerns current and current
growth in an R-L circuit, so we can use the ideas of this section.
Figure 30.12 shows the current i versus the time t that has elapsed
I = E>R
S1
since closing
;
we are given R
, so the emf is determined by the require-
=
36 mA. The other requirement is
ment that the ﬁnal current be I
i = 4.9 mA
that the current be no more than
to sat-
isfy this, we use Eq. (30.14) for the current as a function of time
and solve for the inductance, which is the only unknown quantity.
Equation (30.16) then tells us the time constant.

t = 58 ms;

at

EXECUTE: (a) We solve

I = E>R

for

E:

E = IR = 10.036 A21175 Æ2 = 6.3 V

(b) To ﬁnd the required inductance, we solve Eq. (30.14) for
1-R>E2

L.
and then add 1 to both sides

First we multiply through by
to obtain

1 - iR
E

= e-1R>L2t

Then we take natural logs of both sides, solve for
numbers:

L,

and insert the

L =

-Rt
ln11 - iR>E2

=

-1175 Æ2158 * 10-6 s2
ln31 - 14.9 * 10-3 A21175 Æ2>16.3 V24

= 69 mH

(c) From Eq. (30.16),

t = L
R

= 69 * 10-3 H
175 Æ

= 3.9 * 10-4 s = 390 ms

58 ms

EVALUATE: Note that
58 ms
of  its  ﬁnal  value  of  36  mA;  after
11 - 1>e2

is much less than the time constant. In
the current builds up from zero to 4.9 mA, a small fraction
the  current  equals
of its ﬁnal value, or about 10.632136 mA2 = 23 mA.

390 ms

30.13 Graph of  versus  for decay of
i
current in an R-L circuit. After one time
constant
of its initial
value.

the current is

1>e

t,

t

R

i

L

S2

Switch S2 is closed at t 5 0.

i

I0

O

t

I0
e
t 5 L
R

S1

Current Decay in an R-L Circuit
in the circuit of Fig. 30.11 has been closed for a while
Now suppose switch
I0.
and the current has reached the value  Resetting our stopwatch to redeﬁne the
t = 0,
initial time, we close switch
bypassing the battery. (At the same
to save the battery from ruin.) The current through  and
time we should open
L
does  not  instantaneously  go  to  zero  but  decays  smoothly,  as  shown  in  Fig.
30.13. The Kirchhoff’s-rule loop equation is obtained from Eq. (30.12) by simply
omitting the
term. We challenge you to retrace the steps in the above analysis
and show that the current i varies with time according to

at time

S2

S1

R

E

i = I0e-1R>L2t
t = 0.

(30.18)

is the
2t

I0

is the initial current at time

where
time for current to decrease to
it has dropped to 13.5%, in time

1>e,
5t

The time constant,

t = L>R,

or about 37%, of its original value. In time
to 0.67%, and in

to 0.0045%.

10t

The energy that is needed to maintain the current during this decay is provided
by  the  energy  stored  in  the  magnetic  ﬁeld  of  the  inductor. The  detailed  energy
analysis is simpler this time. In place of Eq. (30.17) we have

t

0 = i 2R + Li

di
dt

(30.19)

Li di>dt

In this case,
inductor decreases at a rate equal to the rate of dissipation of energy
resistor.

is negative; Eq. (30.19) shows that the energy stored in the
in the

i 2R

This entire discussion should look familiar; the situation is very similar to that
of a charging and discharging capacitor, analyzed in Section 26.4. It would be a
good idea to compare that section with our discussion of the R-L circuit.
