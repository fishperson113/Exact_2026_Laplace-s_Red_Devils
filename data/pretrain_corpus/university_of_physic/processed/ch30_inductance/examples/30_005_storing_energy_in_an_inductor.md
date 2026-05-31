Example 30.5
Storing energy in an inductor
The electric-power industry would like to find efficient ways to
store electrical energy generated during low-demand hours to help
meet customer requirements during high-demand hours. Could a
large inductor be used? What inductance would be needed to store
of energy in a coil carrying a 200-A current?
1.00 kW # h
30.10 The energy required to fire an
automobile spark plug is derived from
magnetic-field energy stored in the ignition
coil.
Application A Magnetic Eruption 
on the Sun
This composite of two images of the sun
shows a coronal mass ejection, a dramatic
event in which about 1012 kg (a billion tons) of
material from the sun’s outer atmosphere is
ejected into space at speeds of 500 km s or
faster. Such ejections happen at intervals of a
few hours to a few days. These immense
eruptions are powered by the energy stored in
the sun’s magnetic field. Unlike the earth’s rel-
atively steady magnetic field, the sun’s field is
constantly changing, and regions of unusually
strong field (and hence unusually high mag-
netic energy density) frequently form. A coro-
nal mass ejection occurs when the energy
stored in such a region is suddenly released.
>

30.4 The R-L Circuit
1001
30.4 The R-L Circuit
Let’s look at some examples of the circuit behavior of an inductor. One thing is
clear already; an inductor in a circuit makes it difficult for rapid changes in cur-
rent to occur, thanks to the effects of self-induced emf. Equation (30.7) shows
that the greater the rate of change of current 
the greater the self-induced
emf and the greater the potential difference between the inductor terminals. This
equation, together with Kirchhoff’s rules (see Section 26.2), gives us the princi-
ples we need to analyze circuits containing inductors.
di>dt,
SOLUTION
IDENTIFY and SET UP: We are given the required amount of stored
energy 
and the current 
A. We use Eq. (30.9) to find the
self-inductance .
EXECUTE: We have 
and 
Solving Eq. (30.9) for 
we
find
L = 2U
I 2 =
213.60 * 106 J2
1200 A22
= 180 H
L,
103 W213600 s2 = 3.60 * 106 J.
U = 1.00 kW # h = 11.00 *
I = 200 A
L
I = 200
U
EVALUATE: The required inductance is more than a million times
greater than the self-inductance of the toroidal solenoid of
Example 30.3. Conventional wires that are to carry 200 Awould have
to be of large diameter to keep the resistance low and avoid unaccept-
able energy losses due to 
heating. As a result, a 180-H inductor
using conventional wire would be very large (room-size). A super-
conducting inductor could be much smaller, since the resistance of
a superconductor is zero and much thinner wires could be used; but
the wires would have to be kept at low temperature to remain super-
conducting, and maintaining this temperature would itself require
energy. This scheme is impractical with present technology.
I 2R
Test Your Understanding of Section 30.3
The current in a solenoid is
reversed in direction while keeping the same magnitude. (a) Does this change the 
magnetic field within the solenoid? (b) Does this change the magnetic energy density in 
the solenoid?
❙
Problem-Solving Strategy 30.1
Inductors in Circuits
IDENTIFY the relevant concepts: An inductor is just another circuit
element, like a source of emf, a resistor, or a capacitor. One key
difference is that when an inductor is included in a circuit, all the
voltages, currents, and capacitor charges are in general functions
of time, not constants as they have been in most of our previous
circuit analysis. But Kirchhoff’s rules (see Section 26.2) are still
valid. When the voltages and currents vary with time, Kirchhoff’s
rules hold at each instant of time.
SET UP the problem using the following steps:
1. Follow the procedure described in Problem-Solving Strategy
26.2 (Section 26.2). Draw a circuit diagram and label all quan-
tities, known and unknown. Apply the junction rule immedi-
ately so as to express the currents in terms of as few quantities
as possible.
2. Determine which quantities are the target variables.
EXECUTE the solution as follows:
1. As in Problem-Solving Strategy 26.2, apply Kirchhoff’s loop
rule to each loop in the circuit.
2. Review the sign rules given in Problem-Solving Strategy 26.2.
To get the correct sign for the potential difference between the
terminals of an inductor, apply Lenz’s law and the sign rule
described in Section 30.2 in connection with Eq. (30.7) and
Fig. 30.6. In Kirchhoff’s loop rule, when we go through an
inductor in the same direction as the assumed current, we
encounter a voltage drop equal to 
so the corresponding
term in the loop equation is 
When we go through an
inductor in the opposite direction from the assumed current, the
potential difference is reversed and the term to use in the loop
equation is 
3. Solve for the target variables.
EVALUATE your answer: Check whether your answer is consistent
with the behavior of inductors. By Lenz’s law, if the current
through an inductor is changing, your result should indicate that
the potential difference across the inductor opposes the change.
+L di>dt.
-L di>dt.
L di>dt,
Current Growth in an R-L Circuit
We can learn several basic things about inductor behavior by analyzing the cir-
cuit of Fig. 30.11. A circuit that includes both a resistor and an inductor, and pos-
sibly a source of emf, is called an R-L circuit. The inductor helps to prevent
rapid changes in current, which can be useful if a steady current is required but
the external source has a fluctuating emf. The resistor 
may be a separate circuit
R
ActivPhysics 14.1: The RL Circuit

element, or it may be the resistance of the inductor windings; every real-life
inductor has some resistance unless it is made of superconducting wire. By clos-
ing switch 
we can connect the R-L combination to a source with constant emf
(We assume that the source has zero internal resistance, so the terminal voltage
equals the emf.)
Suppose both switches are open to begin with, and then at some initial time
we close switch 
The current cannot change suddenly from zero to some
final value, since 
and the induced emf in the inductor would both be infi-
nite. Instead, the current begins to grow at a rate that depends only on the value
of 
in the circuit.
Let i be the current at some time t after switch 
is closed, and let 
be its
rate of change at that time. The potential difference 
across the resistor at that
time is
and the potential difference 
across the inductor is
Note that if the current is in the direction shown in Fig. 30.11 and is increasing,
then both 
and 
are positive; a is at a higher potential than b, which in turn
is at a higher potential than c. (Compare to Figs. 30.6a and c.) We apply Kirch-
hoff’s loop rule, starting at the negative terminal and proceeding counterclock-
wise around the loop:
(30.12)
Solving this for 
we find that the rate of increase of current is
(30.13)
At the instant that switch 
is first closed, 
and the potential drop across
is zero. The initial rate of change of current is
As we would expect, the greater the inductance 
the more slowly the current
increases.
As the current increases, the term 
in Eq. (30.13) also increases, and the
rate of increase of current given by Eq. (30.13) becomes smaller and smaller.
This means that the current is approaching a final, steady-state value 
When the
current reaches this value, its rate of increase is zero. Then Eq. (30.13) becomes
The final current does not depend on the inductance 
it is the same as it would
be if the resistance 
alone were connected to the source with emf 
Figure 30.12 shows the behavior of the current as a function of time. To derive
the equation for this curve (that is, an expression for current as a function of
time), we proceed just as we did for the charging capacitor in Section 26.4. First
we rearrange Eq. (30.13) to the form
di
i - 1E>R2 = - R
L dt
E.
R
L;
I
I = E
R
a di
dt b
final
= 0 = E
L - R
L I and
I.
1R>L2i
L,
a di
dt b
initial
= E
L
R
i = 0
S1
di
dt = E - iR
L
= E
L - R
L i
di>dt,
E - iR - L di
dt = 0
vbc
vab
vbc = L di
dt
vbc
vab = iR
vab
di>dt
S1
L
di>dt
S1.
t = 0
E.
S1,
1002
CHAPTER 30 Inductance
Closing switch S1 connects the R-L combination
in series with a source of emf E.
Closing switch S2 while opening switch S1
disconnnects the combination from the source.
+
S1
S2
E
a
b
c
R
L
i
30.11 An R-L circuit.
R
S1
L
E
i
O
t
t 5 t 5 L
R
1 2
I
1
e
E
R
i
I 5
t
+
(           )
Switch S1 is closed at t 5 0.
30.12 Graph of i versus t for growth of
current in an R-L circuit with an emf in
series. The final current is 
after
one time constant 
the current is 
of this value.
1 - 1>e
t,
I = E>R;

30.4 The R-L Circuit
1003
This separates the variables, with i on the left side and t on the right. Then we
integrate both sides, renaming the integration variables 
and 
so that we can
use i and t as the upper limits. (The lower limit for each integral is zero, corre-
sponding to zero current at the initial time 
We get
Now we take exponentials of both sides and solve for i. We leave the details for
you to work out; the final result is
(current in an 
circuit with emf)
(30.14)
This is the equation of the curve in Fig. 30.12. Taking the derivative of Eq. (30.14),
we find
(30.15)
At time 
and 
As 
and 
as we
predicted.
As Fig. 30.12 shows, the instantaneous current i first rises rapidly, then increases
more slowly and approaches the final value 
asymptotically. At a time
equal to 
, the current has risen to 
or about 63%, of its final value.
The quantity 
is therefore a measure of how quickly the current builds toward
its final value; this quantity is called the time constant for the circuit, denoted by 
(30.16)
In a time equal to 
the current reaches 86% of its final value; in 
99.3%; and
in 
99.995%. (Compare the discussion in Section 26.4 of charging a capaci-
tor of capacitance 
that was in series with a resistor of resistance 
the time
constant for that situation was the product 
The graphs of i versus t have the same general shape for all values of 
For a
given value of 
the time constant is greater for greater values of 
When 
is
small, the current rises rapidly to its final value; when 
is large, it rises more
slowly. For example, if 
and 
and the current increases to about 63% of its final value in 0.10 s. (Recall that
But if 
and the rise
is much more rapid.
Energy considerations offer us additional insight into the behavior of an R-L
circuit. The instantaneous rate at which the source delivers energy to the circuit is
The instantaneous rate at which energy is dissipated in the resistor is 
and the rate at which energy is stored in the inductor is 
[or,
equivalently, 
]. When we multiply Eq. (30.12) by i and
rearrange, we find
(30.17)
Of the power 
supplied by the source, part 
is dissipated in the resistor and
part 
goes to store energy in the inductor. This discussion is completely
analogous to our power analysis for a charging capacitor, given at the end of
Section 26.4.
1Li di>dt2
1i2R2
Ei
Ei = i2R + Li di
dt
1d>dt2A1
2 Li2B = Li di>dt
ivbc = Li di>dt
i2R,
P = Ei.
L = 0.010 H, t = 1.0 * 10-4 s = 0.10 ms,
1 H = 1 Æ # s.2
t = L
R =
10 H
100 Æ = 0.10 s
L = 10 H,
R = 100 Æ
L
L
L.
t
R,
L.
RC.)
R;
C
10t,
5t,
2t,
t = L
R  (time constant for an R-L circuit)
t:
L>R
11 - 1>e2,
L>R
I = E>R
di>dt S 0,
i S E>R
t S q,
di>dt = E>L.
i = 0
t = 0,
di
dt = E
L e-1R>L2t
R-L
i = E
R 11 - e-1R>L2t2  
 lna
i - 1E>R2
-E>R
b = - R
L t
L
i
0
di¿
i¿ - 1E>R2 = -
L
t
0
R
L dt¿
t = 0.)
t¿
i¿

1004
CHAPTER 30 Inductance
