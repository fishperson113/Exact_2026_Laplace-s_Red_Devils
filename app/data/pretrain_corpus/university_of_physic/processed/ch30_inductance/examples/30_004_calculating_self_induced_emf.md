Example 30.4
Calculating self-induced emf
If the current in the toroidal solenoid in Example 30.3 increases
uniformly from 0 to 6.0 A in 
find the magnitude and direc-
tion of the self-induced emf.
SOLUTION
IDENTIFY and SET UP: We are given L, the self-inductance, and
the rate of change of the solenoid current. We find the mag-
nitude of self-induced emf 
using Eq. (30.7) and its direction
using Lenz’s law.
EXECUTE:
We have 
From Eq. (30.7), the magnitude of the induced emf is
106 A>s.
= 16.0 A2>13.0 * 10-6 s2 = 2.0 *
di>dt
E
di>dt,
3.0 ms,
The current is increasing, so according to Lenz’s law the direction
of the emf is opposite to that of the current. This corresponds to the
situation in Fig. 30.6c; the emf is in the direction from b to a, like a
battery with a as the
terminal and b the
terminal, tending to
oppose the current increase from the external circuit.
EVALUATE: This example shows that even a small inductance can
give rise to a substantial induced emf if the current changes
rapidly.
L
-
+
ƒEƒ = L ` di
dt ` = 140 * 10-6 H212.0 * 106 A>s2 = 80 V
Test Your Understanding of Section 30.2
Rank the following induc-
tors in order of the potential difference 
from most positive to most negative.
In each case the inductor has zero resistance and the current flows from point a
through the inductor to point b. (i) The current through a 
inductor increases 
from 1.0 A to 2.0 A in 0.50 s; (ii) the current through a 
inductor decreases from
3.0 A to 0 in 2.0 s; (iii) the current through a 
inductor remains constant at 4.0 A;
(iv) the current through a 
inductor increases from 0 to 4.0 A in 0.25 s.
❙
1.0-mH
1.0-mH
4.0-mH
2.0-mH
vab,
the coil. For this, we use the results of Example 28.10 (Section 28.7), 
in which we found the magnetic field in the interior of a toroidal
solenoid as a function of the current.

30.3 Magnetic-Field Energy
999
the current at some instant be i and let its rate of change be 
the current is
increasing, so 
The voltage between the terminals a and b of the induc-
tor at this instant is 
and the rate 
at which energy is being deliv-
ered to the inductor (equal to the instantaneous power supplied by the external
source) is
The energy dU supplied to the inductor during an infinitesimal time interval dt
is 
so
The total energy 
supplied while the current increases from zero to a final value is
(energy stored in an inductor)
(30.9)
After the current has reached its final steady value 
and no more
energy is input to the inductor. When there is no current, the stored energy 
is
zero; when the current is 
the energy is 
When the current decreases from to zero, the inductor acts as a source that
supplies a total amount of energy 
to the external circuit. If we interrupt the
circuit suddenly by opening a switch or yanking a plug from a wall socket, the
current decreases very rapidly, the induced emf is very large, and the energy may
be dissipated in an arc across the switch contacts. This large emf is the electrical
analog of the large force exerted by a car running into a brick wall and stopping
very suddenly.
CAUTION
Energy, resistors, and inductors It’s important not to confuse the behavior of
resistors and inductors where energy is concerned (Fig. 30.9). Energy flows into a resistor
whenever a current passes through it, whether the current is steady or varying; this energy
is dissipated in the form of heat. By contrast, energy flows into an ideal, zero-resistance
inductor only when the current in the inductor increases. This energy is not dissipated; it is
stored in the inductor and released when the current decreases. When a steady current
flows through an inductor, there is no energy flow in or out. ❙
Magnetic Energy Density
The energy in an inductor is actually stored in the magnetic field within the coil,
just as the energy of a capacitor is stored in the electric field between its plates.
We can develop relationships for magnetic-field energy analogous to those we
obtained for electric-field energy in Section 24.3 [Eqs. (24.9) and (24.11)]. We
will concentrate on one simple case, the ideal toroidal solenoid. This system has
the advantage that its magnetic field is confined completely to a finite region of
space within its core. As in Example 30.3, we assume that the cross-sectional
area 
is small enough that we can pretend that the magnetic field is uniform over
the area. The volume 
enclosed by the toroidal solenoid is approximately equal 
to the circumference 
multiplied by the area 
From Example 30.3,
the self-inductance of the toroidal solenoid with vacuum within its coils is
From Eq. (30.9), the energy 
stored in the toroidal solenoid when the current
is is
U = 1
2 LI 2 = 1
2
m0N 2A
2pr
I 2
I
U
L = m0N 2A
2pr
V = 2prA.
A:
2pr
V
A
1
2 LI 2I
1
2 LI 2.
I,
U
di>dt = 0
I,
U = L
L
I
0
i di = 1
2 LI 2  
I
U
dU = Li di
dU = P dt,
P = Vabi = Li di
dt
P
Vab = L di>dt,
di>dt 7 0.
di>dt;
i
a
b
L
i
a
b
R
Resistor with current i: energy is dissipated.
Inductor with current i: energy is stored.
30.9 A resistor is a device in which
energy is irrecoverably dissipated. By con-
trast, energy stored in a current-carrying
inductor can be recovered when the current
decreases to zero.

The magnetic field and therefore this energy are localized in the volume
enclosed by the windings. The energy per unit volume, or magnetic
energy density, is
We can express this in terms of the magnitude 
of the magnetic field inside the
toroidal solenoid. From Eq. (28.24) in Example 28.10 (Section 28.7), this is
and so
When we substitute this into the above equation for u, we finally find the expres-
sion for magnetic energy density in vacuum:
(magnetic energy density in vacuum)
(30.10)
This is the magnetic analog of the energy per unit volume in an electric field
in vacuum, 
which we derived in Section 24.3. As an example, the
energy density in the 1.5-T magnetic field of an MRI scanner (see Section 27.7)
is 
.
When the material inside the toroid is not vacuum but a material with (con-
stant) magnetic permeability 
we replace 
by 
in Eq. (30.10). The
energy per unit volume in the magnetic field is then
(magnetic energy density in a material)
(30.11)
Although we have derived Eq. (30.11) only for one special situation, it turns
out to be the correct expression for the energy per unit volume associated with
any magnetic-field configuration in a material with constant permeability. For
vacuum, Eq. (30.11) reduces to Eq. (30.10). We will use the expressions for
electric-field and magnetic-field energy in Chapter 32 when we study the energy
associated with electromagnetic waves.
Magnetic-field energy plays an important role in the ignition systems of gasoline-
powered automobiles. A primary coil of about 250 turns is connected to the car’s
battery and produces a strong magnetic field. This coil is surrounded by a second-
ary coil with some 25,000 turns of very fine wire. When it is time for a spark plug
to fire (see Fig. 20.5 in Section 20.3), the current to the primary coil is inter-
rupted, the magnetic field quickly drops to zero, and an emf of tens of thousands
of volts is induced in the secondary coil. The energy stored in the magnetic field
thus goes into a powerful pulse of current that travels through the secondary coil
to the spark plug, generating the spark that ignites the fuel-air mixture in the
engine’s cylinders (Fig. 30.10).
u = B2
2m  
m
m0
m = Kmm0,
u = B2>2m0 = 11.5 T22>12 * 4p * 10-7 T # m>A2 = 9.0 * 105 J>m3
u = 1
2 P0E2,
u = B2
2m0  
N 2I 2
12pr22 = B2
m0
2
B = m0NI
2pr
B
u =
U
2prA = 1
2 m0
N 2I 2
12pr22
u = U>V:
V = 2prA
1000
CHAPTER 30 Inductance
