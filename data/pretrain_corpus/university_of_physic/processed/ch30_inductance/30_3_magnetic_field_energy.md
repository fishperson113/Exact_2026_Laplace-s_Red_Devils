998

CHAPTER 30 Inductance

30.8 Determining the self-inductance of a closely wound
toroidal solenoid. For clarity, only a few turns of the winding are
shown. Part of the toroid has been cut away to show the cross-
A
sectional area  and radius r.

L = N£B>i.
EXECUTE: From  Eq.  (30.6),  the  self-inductance  is
From Example 28.10, the ﬁeld magnitude at a distance r from the
B = m0Ni>2pr.
If we assume that the ﬁeld has this
toroid axis is
magnitude over the entire cross-sectional area
A,

then

Number of turns 5 N
(only a few are shown)

A

r

i

i

the coil. For this, we use the results of Example 28.10 (Section 28.7),
in which we found the magnetic ﬁeld in the interior of a toroidal
solenoid as a function of the current.

Example 30.4

Calculating self-induced emf

If  the  current  in  the  toroidal  solenoid  in  Example  30.3  increases
3.0 ms,
ﬁnd the magnitude and direc-
uniformly from 0 to 6.0 A in
tion of the self-induced emf.

SOLUTION

IDENTIFY  and SET  UP:  We  are  given  L,  the  self-inductance,  and
di>dt,
the rate of change of the solenoid current. We ﬁnd the mag-
nitude  of  self-induced  emf
using  Eq.  (30.7) and  its  direction
using Lenz’s law.

E

EXECUTE: We  have
106 A>s.

di>dt

= 16.0 A2>13.0 * 10-6 s2 = 2.0 *

From Eq. (30.7), the magnitude of the induced emf is

£B = BA =

m0NiA
2pr

£B

The ﬂux
L

is

is the same through each turn, and the self-inductance

L =

N£B
i

=

m0N 2A
2pr

(self-inductance of a toroidal solenoid)

N = 200
then

r = 0.10 m;

EVALUATE:  Suppose
10-4 m2,
and
14p * 10-7 Wb>A # m212002215.0 * 10-4 m22
2p10.10 m2

turns,

L =

A = 5.0 cm2 = 5.0 *

= 40 * 10-6 H = 40 mH

ƒEƒ = L ` di
dt

` = 140 * 10-6 H212.0 * 106 A>s2 = 80 V

The current is increasing, so according to Lenz’s law the direction
of the emf is opposite to that of the current. This corresponds to the
situation in Fig. 30.6c; the emf is in the direction from b to a, like a
battery with a as the
terminal, tending to
terminal and b the
oppose the current increase from the external circuit.

-

+

EVALUATE: This example shows that even a small inductance  can
give  rise  to  a  substantial  induced  emf  if  the  current  changes
rapidly.

L

Test Your Understanding of Section 30.2 Rank the following induc-
vab,
tors in order of the potential difference
from most positive to most negative.
In each case the inductor has zero resistance and the current ﬂows from point a
through the inductor to point b. (i) The current through a
from 1.0 A to 2.0 A in 0.50 s; (ii) the current through a
3.0 A to 0 in 2.0 s; (iii) the current through a
(iv) the current through a

inductor increases
inductor decreases from
inductor remains constant at 4.0 A;

inductor increases from 0 to 4.0 A in 0.25 s.

1.0-mH

1.0-mH

2.0-mH

4.0-mH

❙

30.3 Magnetic-Field Energy

Establishing a current in an inductor requires an input of energy, and an inductor car-
rying a current has energy stored in it. Let’s see how this comes about. In Fig. 30.5,
an increasing current i in the inductor causes an emf  between its terminals and
between the terminals of the source, with
a corresponding potential difference
point a at higher potential than point b. Thus the source must be adding energy to
the inductor, and the instantaneous power
(rate of transfer of energy into the
inductor) is

Vab

P

P = Vabi.

E

Energy Stored in an Inductor
in
We can calculate the total energy input
an inductor with inductance
if the initial current is zero. We assume that the
inductor has zero resistance, so no energy is dissipated within the inductor. Let

needed to establish a ﬁnal current

U

L

I

30.3 Magnetic-Field Energy

999

30.9 A resistor is a device in which
energy is irrecoverably dissipated. By con-
trast, energy stored in a current-carrying
inductor can be recovered when the current
decreases to zero.

Resistor with current i: energy is dissipated.
i

a

b

R

Inductor with current i: energy is stored.
i

a

b

L

di>dt 7 0.

the current is
the current at some instant be i and let its rate of change be
The voltage between the terminals a and b of the induc-
increasing, so
tor at this instant is
at which energy is being deliv-
and the rate
ered to the inductor (equal to the instantaneous power supplied by the external
source) is

Vab = L di>dt,

P

di>dt;

P = Vabi = Li

di
dt

The energy dU supplied to the inductor during an inﬁnitesimal time interval dt
dU = P dt,

so

is

dU = Li di

The total energy

U

supplied while the current increases from zero to a ﬁnal value  is

I

I
i di = 1

2 LI 2

U = L

L
0

(energy stored in an inductor)

(30.9)

and no more
is

After the current has reached its ﬁnal steady value

I,

di>dt = 0

1

I,

the energy is

When the current decreases from

energy is input to the inductor. When there is no current, the stored energy
zero; when the current is

2 LI 2.
to zero, the inductor acts as a source that
to the external circuit. If we interrupt the
supplies a total amount of energy
circuit suddenly by opening a switch or yanking a plug from a wall socket, the
current decreases very rapidly, the induced emf is very large, and the energy may
be dissipated in an arc across the switch contacts. This large emf is the electrical
analog of the large force exerted by a car running into a brick wall and stopping
very suddenly.

I
2 LI 2

U

1

CAUTION Energy, resistors, and inductors It’s important not to confuse the behavior of
resistors and inductors where energy is concerned (Fig. 30.9). Energy ﬂows into a resistor
whenever a current passes through it, whether the current is steady or varying; this energy
is dissipated in the form of heat. By contrast, energy ﬂows into an ideal, zero-resistance
inductor only when the current in the inductor increases. This energy is not dissipated; it is
stored  in  the  inductor  and  released  when  the  current  decreases. When  a  steady  current
ﬂows through an inductor, there is no energy ﬂow in or out. ❙

Magnetic Energy Density
The energy in an inductor is actually stored in the magnetic ﬁeld within the coil,
just as the energy of a capacitor is stored in the electric ﬁeld between its plates.
We  can  develop  relationships  for  magnetic-ﬁeld  energy  analogous  to  those  we
obtained for electric-ﬁeld energy in Section 24.3 [Eqs. (24.9) and (24.11)]. We
will concentrate on one simple case, the ideal toroidal solenoid. This system has
the advantage that its magnetic ﬁeld is conﬁned completely to a ﬁnite region of
space  within  its  core. As  in  Example  30.3,  we  assume  that  the  cross-sectional
is small enough that we can pretend that the magnetic ﬁeld is uniform over
area
enclosed by the toroidal solenoid is approximately equal
the area. The volume
to the circumference
From Example 30.3,
multiplied by the area
the self-inductance of the toroidal solenoid with vacuum within its coils is

V = 2prA.

V
2pr

A:

A

L =

m0N 2A
2pr

U

stored in the toroidal solenoid when the current

From Eq. (30.9), the energy
is

is

I

U = 1

2 LI 2 = 1

2

m0N 2A
2pr

I 2

1000

CHAPTER 30 Inductance

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
the sun’s magnetic ﬁeld. Unlike the earth’s rel-
atively steady magnetic ﬁeld, the sun’s ﬁeld is
constantly changing, and regions of unusually
strong ﬁeld (and hence unusually high mag-
netic energy density) frequently form. A coro-
nal mass ejection occurs when the energy
stored in such a region is suddenly released.

>

The  magnetic  ﬁeld  and  therefore  this  energy  are  localized  in  the  volume
enclosed by the windings. The energy per unit volume, or magnetic

V = 2prA
energy density, is

u = U>V:

u = U
2prA

= 1
2

m0

N 2I 2
12pr22

We can express this in terms of the magnitude  of the magnetic ﬁeld inside the
toroidal solenoid. From Eq. (28.24) in Example 28.10 (Section 28.7), this is

B

and so

B =

m0NI
2pr

N 2I 2
12pr22

= B2
m0
2

When we substitute this into the above equation for u, we ﬁnally ﬁnd the expres-
sion for magnetic energy density in vacuum:

u = B2
2m0

(magnetic energy density in vacuum)

(30.10)

This  is  the  magnetic  analog  of  the  energy  per  unit  volume  in  an  electric ﬁeld
in  vacuum,
which  we  derived  in  Section  24.3. As  an  example,  the
energy density in the 1.5-T magnetic ﬁeld of an MRI scanner (see Section 27.7)
is

u = B2>2m0 = 11.5 T22>12 * 4p * 10-7 T # m>A2 = 9.0 * 105 J>m3

u = 1
2

P0E 2,

.

When the material inside the toroid is not vacuum but a material with (con-
in Eq. (30.10). The

we replace

stant) magnetic permeability
energy per unit volume in the magnetic ﬁeld is then

m = Kmm0,

m0

by

m

30.10 The energy required to ﬁre an
automobile spark plug is derived from
magnetic-ﬁeld energy stored in the ignition
coil.

u = B2
2m

(magnetic energy density in a material)

(30.11)

Although we have derived Eq. (30.11) only for one special situation, it turns
out to be the correct expression for the energy per unit volume associated with
any magnetic-ﬁeld  conﬁguration  in  a  material  with  constant  permeability.  For
vacuum,  Eq.  (30.11) reduces  to  Eq.  (30.10).  We  will  use  the  expressions  for
electric-ﬁeld and magnetic-ﬁeld energy in Chapter 32 when we study the energy
associated with electromagnetic waves.

Magnetic-ﬁeld energy plays an important role in the ignition systems of gasoline-
powered automobiles. A primary coil of about 250 turns is connected to the car’s
battery and produces a strong magnetic ﬁeld. This coil is surrounded by a second-
ary coil with some 25,000 turns of very ﬁne wire. When it is time for a spark plug
to  ﬁre  (see  Fig.  20.5 in  Section  20.3),  the  current  to  the  primary  coil  is  inter-
rupted, the magnetic ﬁeld quickly drops to zero, and an emf of tens of thousands
of volts is induced in the secondary coil. The energy stored in the magnetic ﬁeld
thus goes into a powerful pulse of current that travels through the secondary coil
to  the  spark  plug,  generating  the  spark  that  ignites  the  fuel–air  mixture  in  the
engine’s cylinders (Fig. 30.10).

Example 30.5

Storing energy in an inductor

The  electric-power  industry  would  like  to  ﬁnd  efﬁcient  ways  to
store electrical energy generated during low-demand hours to help
meet  customer  requirements  during  high-demand  hours.  Could  a

large inductor be used? What inductance would be needed to store
1.00 kW # h

of energy in a coil carrying a 200-A current?
