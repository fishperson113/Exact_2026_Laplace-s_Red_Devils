Example  30.3  increases
3.0 ms,
find the magnitude and direc-
uniformly from 0 to 6.0 A in
tion of the self-induced emf.

SOLUTION

IDENTIFY  and SET  UP:  We  are  given  L,  the  self-inductance,  and
di>dt,
the rate of change of the solenoid current. We find the mag-
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

The flux
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
In each case the inductor has zero resistance and the current flows from point a
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

needed to establish a final current

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

The energy dU supplied to the inductor during an infinitesimal time interval dt
dU = P dt,

so

is

dU = Li di

The total energy

U

supplied while the current increases from zero to a final value  is

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

After the current has reached its final steady value

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
resistors and inductors where energy is concerned (Fig. 30.9). Energy flows into a resistor
whenever a current passes through it, whether the current is steady or varying; this energy
is dissipated in the form of heat. By contrast, energy flows into an ideal, zero-resistance
inductor only when the current in the inductor increases. This energy is not dissipated; it is
stored  in  the  inductor  and  released  when  the  current  decreases. When  a  steady  current
flows through an inductor, there is no energy flow in or out. ❙

Magnetic Energy Density
The energy in an inductor is actually stored in the magnetic field within the coil,
just as the energy of a capacitor is stored in the electric field between its plates.
We  can  develop  relationships  for  magnetic-field  energy  analogous  to  those  we
obtained for electric-field energy in Section 24.3 [Eqs. (24.9) and (24.11)]. We
will concentrate on one simple case, the ideal toroidal solenoid. This system has
the advantage that its magnetic field is confined completely to a finite region of
space  within  its  core. As  in
