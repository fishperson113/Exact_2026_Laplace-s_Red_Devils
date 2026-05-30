994

CHAPTER 30 Inductance

30.3 A long solenoid with cross-sectional area  and
surrounded at its center by a coil with

turns.

A

N2

N1

turns is

B1 = m0n 1i1 =

m0N1i1
l

Cross-sectional area A

l

N1 turns N2 turns

at the center of
an expression [Eq. (28.23)] for the ﬁeld magnitude
B1
the solenoid (coil 1) in terms of the solenoid current
This allows
i1.
us to determine the ﬂux through a cross section of the solenoid. Since
there is no magnetic ﬁeld outside a very long solenoid, this is also
equal to the ﬂux
through each turn of the outer coil (2). We then
use Eq. (30.5), in the form

M = N2£B2>i1,
EXECUTE: Equation (28.23) is expressed in terms of the number of
turns  per  unit  length,  which  for  solenoid  (1)  is
.  We
then have

n 1 = N1>L

to determine

£B2

M.

Example 30.2

Emf due to mutual inductance

In Example 30.1, suppose the current
in the outer coil is given by
i2 = 12.0 * 106 A>s2t
. (Currents in wires can indeed increase this
what  is  the  average
rapidly  for  brief  periods.)  (a)  At
magnetic ﬂux through each turn of the solenoid (coil 1) due to the
current in the outer coil? (b) What is the induced emf in the solenoid?

t = 3.0 ms,

i2

SOLUTION

IDENTIFY  and SET  UP:  In  Example  30.1  we  found  the  mutual
inductance by relating the current in the solenoid to the ﬂux pro-
duced in the outer coil; to do that, we used Eq. (30.5) in the form
M = N2£B2>i1.
in the outer coil
Here we are given the current
in the solenoid. The mutual
and want to ﬁnd the resulting ﬂux
M = 25 mH
inductance  is  the  same in  either  case,  and  we  have
M = N1£B1>i2
from Example 30.1. We use Eq. (30.5) in the form
£B1
through each turn of the solenoid
to determine the average ﬂux
in the outer coil. We then use Eq. (30.4)
caused by a given current
to determine the emf induced in the solenoid by the time variation
of

£1

i2

i2

i2.

EXECUTE: (a)  At
outer  coil  is

t = 3.0 ms = 3.0 * 10-6 s,

i2 = 12.0 * 106 A>s213.0 * 10-6 s2 = 6.0 A.

the  current  in  the
We

B1A.
As we
The ﬂux through a cross section of the solenoid equals
through each turn
mentioned above, this also equals the ﬂux
of  the  outer  coil,  independent  of  its  cross-sectional  area.  From
Eq. (30.5), the mutual inductance
N2£B2
i1

is then
m0N1i1
l

m0AN1N2
l

N2B1A
i1

N2
i1

M =

£B2

A =

M

=

=

N1N2

EVALUATE:  The mutual inductance M of any two coils is propor-
tional to the product
of their numbers of turns. Notice that M
depends only on the geometry of the two coils, not on the current.
Here’s a numerical example to give you an idea of magnitudes.
N1 = 1000

l = 0.50 m, A = 10 cm2 = 1.0 * 10-3 m2,
N2 = 10 turns.
14p * 10-7 Wb>A # m211.0 * 10-3 m221100021102
0.50 m

Suppose
turns, and

M =

Then

= 25 * 10-6 Wb>A = 25 * 10-6 H = 25 mH

solve Eq. (30.5) for the ﬂux
(coil 1):

£B1

through each turn of the solenoid

£B1 =

Mi2
N1

=

125 * 10-6 H216.0 A2
1000

= 1.5 * 10-7 Wb

We emphasize that this is an average value; the ﬂux can vary con-
siderably between the center and the ends of the solenoid.
di2>dt =

2.0 *
then, from Eq. (30.4), the induced emf in the solenoid is

i2 = 12.0 * 106 A>s2t

(b)  We  are  given

106 A>s;

,  so

E1 = - M

di2
dt

= - 125 * 10-6 H212.0 * 106 A>s2 = - 50 V

EVALUATE: This is a substantial induced emf in response to a very
rapid  current  change.  In  an  operating  Tesla  coil,  there  is  a  high-
frequency alternating current rather than a continuously increasing
alternate  as  well,
current  as  in  this  example;  both
with amplitudes that can be thousands of times larger than in this
example.

di2>dt

and

E1

Test Your Understanding of Section 30.1 Consider the Tesla coil
described in Example 30.1. If you make the solenoid out of twice as much wire, so
that it has twice as many turns and is twice as long, how much larger is the mutual
inductance? (i)
1
(iv)
2M

is four times greater; (ii)

is twice as great; (iii)

is  as great; (v)

is  as great.

1
4M

M

M

M

is unchanged;

❙

30.2 Self-Inductance and Inductors

In our discussion of mutual inductance we considered two separate, independent
circuits: A current in one circuit creates a magnetic ﬁeld that gives rise to a ﬂux
through  the  second  circuit.  If  the  current  in  the  ﬁrst  circuit  changes,  the  ﬂux
through the second circuit changes and an emf is induced in the second circuit.

30.2 Self-Inductance and Inductors

995

An important related effect occurs even if we consider only a single isolated
circuit.  When  a  current  is  present  in  a  circuit,  it  sets  up  a  magnetic  ﬁeld  that
causes a magnetic ﬂux through the same circuit; this ﬂux changes when the cur-
rent changes. Thus any circuit that carries a varying current has an emf induced
in  it  by  the  variation  in  its  own magnetic  ﬁeld.  Such  an  emf  is  called  a  self-
induced emf. By Lenz’s law, a self-induced emf always opposes the change in
the current that caused the emf and so tends to make it more difﬁcult for varia-
tions in current to occur. For this reason, self-induced emfs can be of great impor-
tance whenever there is a varying current.

30.4 The current i in the circuit causes a
magnetic ﬁeld
ﬂux through the coil.

in the coil and hence a

S
B

Self-inductance: If the current i in the coil is
changing, the changing flux through the coil
induces an emf
in the coil.

S
B

+

i

Application Inductors, Power
Transmission, and
Lightning Strikes
If lightning strikes part of an electrical power
transmission system, it causes a sudden spike
in voltage that can damage the components of
the system as well as anything connected to
that system (for example, home appliances).
To minimize these effects, large inductors are
incorporated into the transmission system.
These use the principle that an inductor
opposes and suppresses any rapid changes in
the current.

Self-induced emfs can occur in any circuit, since there is always some mag-
netic ﬂux through the closed loop of a current-carrying circuit. But the effect is
turns of wire (Fig. 30.4). As
greatly enhanced if the circuit includes a coil with
through each turn of
a result of the current
of the circuit as
the coil. In analogy to Eq. (30.5) we deﬁne the self-inductance

there is an average magnetic ﬂux

£B

N

L

i,

L =

N£B
i

(self-inductance)

(30.6)

When there is no danger of confusion with mutual inductance, the self-inductance
is called simply the inductance. Comparing Eqs. (30.5) and (30.6), we see that
the units of self-inductance are the same as those of mutual inductance; the SI
unit of self-inductance is the henry.

If the current i in the circuit changes, so does the ﬂux

from rearranging
Eq. (30.6) and taking the derivative with respect to time, the rates of change are
related by

£B;

N

d£B
dt

= L

di
dt

From Faraday’s law for a coil with
E = - N d£B>dt,

so it follows that

N

turns, Eq. (29.4), the self-induced emf is

E = - L

di
dt

    1self-induced emf )

(30.7)

The minus sign in Eq. (30.7) is a reﬂection of Lenz’s law; it says that the self-
induced emf in a circuit opposes any change in the current in that circuit. (Later
in this section we’ll explore in greater depth the signiﬁcance of this minus sign.)
Equation (30.7) also states that the self-inductance of a circuit is the magni-
tude of the self-induced emf per unit rate of change of current. This relationship
makes it possible to measure an unknown self-inductance in a relatively simple
way: Change the current in the circuit at a known rate
measure the induced
emf, and take the ratio to determine

di>dt,

L.

Inductors As Circuit Elements
A circuit  device  that  is  designed  to  have  a  particular  inductance  is  called  an
inductor, or a choke. The usual circuit symbol for an inductor is

Like  resistors  and  capacitors,  inductors  are  among  the  indispensable  circuit
elements of modern electronics. Their purpose is to oppose any variations in the
current through the circuit. An inductor in a direct-current circuit helps to main-
tain a steady current despite any ﬂuctuations in the applied emf; in an alternating-
current  circuit,  an  inductor  tends  to  suppress  variations  of  the  current  that  are
more rapid than desired. In this chapter and the next we will explore the behavior
and applications of inductors in circuits in more detail.

To  understand  the  behavior  of  circuits  containing  inductors,  we  need  to
develop  a  general  principle  analogous  to  Kirchhoff’s  loop  rule  (discussed  in

996

CHAPTER 30 Inductance

30.5 A circuit containing a source of
emf and an inductor. The source is vari-
able, so the current i and its rate of change
di>dt

can be varied.

Variable
source
of emf

a

L

b

i

i

30.6 (a) The potential difference across a
resistor depends on the current. (b), (c), (d)
The potential difference across an inductor
depends on the rate of change of the current.

(a) Resistor with current i flowing from a to b:
potential drops from a to b.

a

+

i

R

b

–

Vab

5 iR . 0

(b) Inductor with constant current i flowing
from a to b: no potential difference.

i constant: di/dt 5 0

a

E 5 0

b

Vab

5 L

di
dt

5 0

(c) Inductor with increasing current i flowing
from a to b: potential drops from a to b.

i increasing: di/dt . 0

a

+

E

b

–

Vab

5 L

di
dt

. 0

(d) Inductor with decreasing current i flowing
from a to b: potential increases from a to b.
i decreasing: di/dt , 0

a

–

E

b

+

Vab

5 L

di
dt

, 0

Section  26.2).  To  apply  that  rule,  we  go  around  a  conducting  loop,  measuring
potential differences across successive circuit elements as we go. The algebraic
sum of these differences around any closed loop must be zero because the electric
ﬁeld produced by charges distributed around the circuit is conservative. In Sec-
tion 29.7 we denoted such a conservative ﬁeld as

S
E

c.

S
E

When an inductor is included in the circuit, the situation changes. The mag-
netically induced electric ﬁeld within the coils of the inductor is not conservative;
n.
as in Section 29.7, we’ll denote it by  We need to think very carefully about
the  roles  of  the  various  ﬁelds.  Let’s  assume  we  are  dealing  with  an  inductor
whose coils have negligible resistance. Then a negligibly small electric ﬁeld is
required  to  make  charge  move  through  the  coils,  so  the  total electric  ﬁeld
S
E
within the coils must be zero, even though neither ﬁeld is individually
zero. Because
is nonzero, there have to be accumulations of charge on the ter-
minals of the inductor and the surfaces of its conductors to produce this ﬁeld.

c (cid:2) E

S
E

S

n

c

Consider the circuit shown in Fig. 30.5; the box contains some combination of
batteries and variable resistors that enables us to control the current i in the cir-
cuit. According to Faraday’s law, Eq. (29.10), the line integral of
around the
circuit is the negative of the rate of change of ﬂux through the circuit, which in
turn is given by Eq. (30.7). Combining these two relationships, we get

S
E

n

# d l

S

S
E

n

C

= - L

di
dt

where we integrate clockwise around the loop (the direction of the assumed cur-
S
is different from zero only within the inductor. Therefore the inte-
rent). But
E
around the whole loop can be replaced by its integral only from a to b
gral of
through the inductor; that is,

S
E

n

n

b

S
E

n

# d l

S

L
a

= - L

di
dt

Next,  because
rewrite this as

S
E

S

c (cid:2) E

n (cid:3) 0

at  each  point  within  the  inductor  coils,  we  can

b

S
E

c

# d l

S

L
a

= L

di
dt

But this integral is just the potential
ﬁnally obtain

Vab

of point a with respect to point b, so we

Vab = Va - Vb = L

di
dt

(30.8)

We conclude that there is a genuine potential difference between the terminals of
the  inductor,  associated  with  conservative,  electrostatic  forces,  despite  the  fact
that the electric ﬁeld associated with the magnetic induction effect is nonconserv-
ative. Thus we are justiﬁed in using Kirchhoff’s loop rule to analyze circuits that
include inductors. Equation (30.8) gives the potential difference across an induc-
tor in a circuit.

CAUTION Self-induced  emf  opposes  changes  in  current Note that the self-induced emf
does not oppose the current i itself; rather, it opposes any change
in the current. Thus
the circuit behavior of an inductor is quite different from that of a resistor. Figure 30.6 com-
pares the behaviors of a resistor and an inductor and summarizes the sign relationships. ❙

1di>dt2

Applications of Inductors
Because an inductor opposes changes in current, it plays an important role in ﬂu-
orescent light ﬁxtures (Fig. 30.7). In such ﬁxtures, current ﬂows from the wiring

30.2 Self-Inductance and Inductors

997

30.7 These ﬂuorescent light tubes are
wired in series with an inductor, or ballast,
that helps to sustain the current ﬂowing
through the tubes.

into the gas that ﬁlls the tube, ionizing the gas and causing it to glow. However,
an ionized gas or plasma is a highly nonohmic conductor: The greater the cur-
rent, the more highly ionized the plasma becomes and the lower its resistance. If
a sufﬁciently large voltage is applied to the plasma, the current can grow so much
that it damages the circuitry outside the ﬂuorescent tube. To prevent this problem,
an inductor or magnetic ballast is put in series with the ﬂuorescent tube to keep
the current from growing out of bounds.

The  ballast  also  makes  it  possible  for  the  ﬂuorescent  tube  to  work  with  the
alternating  voltage  provided  by  household  wiring. This  voltage  oscillates  sinu-
soidally with a frequency of 60 Hz, so that it goes momentarily to zero 120 times
per second. If there were no ballast, the plasma in the ﬂuorescent tube would rap-
idly deionize when the voltage went to zero and the tube would shut off. With a
ballast  present,  a  self-induced  emf  sustains  the  current  and  keeps  the  tube  lit.
Magnetic ballasts are also used for this purpose in streetlights (which obtain their
light from a glowing vapor of mercury or sodium atoms) and in neon lights. (In
compact ﬂuorescent lamps, the magnetic ballast is replaced by a more compli-
cated scheme for regulating current. This scheme utilizes transistors, discussed in
Chapter 42.)

N

N 2.

turns close together, it is always proportional to

The  self-inductance  of  a  circuit  depends  on  its  size,  shape,  and  number  of
turns. For
It also depends
on the magnetic properties of the material enclosed by the circuit. In the follow-
ing examples we will assume that the circuit encloses only vacuum (or air, which
from the standpoint of magnetism is essentially vacuum). If, however, the ﬂux is
m,
concentrated  in  a  region  containing  a  magnetic  material  with  permeability
m0
(the permeability of vacuum) by
then in the expression for  we must replace
m = Kmm0,
as discussed in Section 28.8. If the material is diamagnetic or para-
is very close to
magnetic, this replacement makes very little difference, since
1. If the material is ferromagnetic, however, the difference is of crucial impor-
tance.  A solenoid  wound  on  a  soft  iron  core  having
can  have  an
inductance approximately 5000 times as great as that of the same solenoid with
an  air  core.  Ferromagnetic-core  inductors  are  very  widely  used  in  a  variety  of
electronic and electric-power applications.

Km = 5000

Km

B

An added complication is that with ferromagnetic materials the magnetization
is in general not a linear function of magnetizing current, especially as saturation
is approached. As a result, the inductance is not constant but can depend on current
in a fairly complicated way. In our discussion we will ignore this complication
and assume always that the inductance is constant. This is a reasonable assumption
even  for  a  ferromagnetic  material  if  the  magnetization  remains  well  below  the
saturation level.

Because  automobiles  contain  steel,  a  ferromagnetic  material,  driving  an
automobile  over  a  coil  causes  an  appreciable  increase  in  the  coil’s  induc-
tance. This effect is used in trafﬁc light sensors, which use a large, current-carrying
coil  embedded  under  the  road  surface  near  an  intersection.  The  circuitry  con-
nected to the coil detects the inductance change as a car drives over. When a pre-
programmed number of cars have passed over the coil, the light changes to green
to allow the cars through the intersection.

?

Example 30.3

Calculating self-inductance

A

Determine  the  self-inductance  of  a  toroidal  solenoid  with  cross-
N
sectional area
turns of
is uniform
wire on a nonmagnetic core (Fig. 30.8). Assume that
B
across a cross section (that is, neglect the variation of  with dis-
tance from the toroid axis).

and mean radius r, closely wound with
B

SOLUTION

IDENTIFY  and SET  UP: Our target variable is the self-inductance
of  the  toroidal  solenoid.  We  can  ﬁnd
requires knowing the ﬂux

L
using  Eq.  (30.6),  which
through each turn and the current i in

L

£B

Continued
