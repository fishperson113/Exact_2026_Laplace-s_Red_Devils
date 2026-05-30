Example 30.2
Emf due to mutual inductance
In Example 30.1, suppose the current 
in the outer coil is given by
. (Currents in wires can indeed increase this
rapidly for brief periods.) (a) At 
what is the average
magnetic flux through each turn of the solenoid (coil 1) due to the
current in the outer coil? (b) What is the induced emf in the solenoid?
SOLUTION
IDENTIFY and SET UP: In Example 30.1 we found the mutual
inductance by relating the current in the solenoid to the flux pro-
duced in the outer coil; to do that, we used Eq. (30.5) in the form
Here we are given the current 
in the outer coil
and want to find the resulting flux 
in the solenoid. The mutual
inductance is the same in either case, and we have 
from Example 30.1. We use Eq. (30.5) in the form 
to determine the average flux 
through each turn of the solenoid
caused by a given current 
in the outer coil. We then use Eq. (30.4)
to determine the emf induced in the solenoid by the time variation
of
EXECUTE: (a) At 
the current in the
outer coil is 
We
i2 = 12.0 * 106 A>s213.0 * 10-6 s2 = 6.0 A.
t = 3.0 ms = 3.0 * 10-6 s,
i2.
i2
£B1
M = N1£B1>i2
M = 25 mH
£1
i2
M = N2£B2>i1.
t = 3.0 ms,
i2 = 12.0 * 106 A>s2t
i2
solve Eq. (30.5) for the flux 
through each turn of the solenoid 
(coil 1):
We emphasize that this is an average value; the flux can vary con-
siderably between the center and the ends of the solenoid.
(b) We are given 
, so 
then, from Eq. (30.4), the induced emf in the solenoid is
EVALUATE: This is a substantial induced emf in response to a very
rapid current change. In an operating Tesla coil, there is a high-
frequency alternating current rather than a continuously increasing
current as in this example; both 
and 
alternate as well,
with amplitudes that can be thousands of times larger than in this
example.
E1
di2>dt
E1 = -M di2
dt = -125 * 10-6 H212.0 * 106 A>s2 = -50 V
106 A>s;
2.0 *
di2>dt =
i2 = 12.0 * 106 A>s2t
£B1 = Mi2
N1
=
125 * 10-6 H216.0 A2
1000
= 1.5 * 10-7 Wb
£B1
Test Your Understanding of Section 30.1
Consider the Tesla coil
described in Example 30.1. If you make the solenoid out of twice as much wire, so
that it has twice as many turns and is twice as long, how much larger is the mutual
inductance? (i) 
is four times greater; (ii) 
is twice as great; (iii) 
is unchanged; 
(iv) 
is as great; (v) 
is as great.
❙
1
4
M
1
2
M
M
M
M

30.2 Self-Inductance and Inductors
995
An important related effect occurs even if we consider only a single isolated
circuit. When a current is present in a circuit, it sets up a magnetic field that
causes a magnetic flux through the same circuit; this flux changes when the cur-
rent changes. Thus any circuit that carries a varying current has an emf induced
in it by the variation in its own magnetic field. Such an emf is called a self-
induced emf. By Lenz’s law, a self-induced emf always opposes the change in
the current that caused the emf and so tends to make it more difficult for varia-
tions in current to occur. For this reason, self-induced emfs can be of great impor-
tance whenever there is a varying current.
Self-induced emfs can occur in any circuit, since there is always some mag-
netic flux through the closed loop of a current-carrying circuit. But the effect is
greatly enhanced if the circuit includes a coil with 
turns of wire (Fig. 30.4). As
a result of the current there is an average magnetic flux 
through each turn of
the coil. In analogy to Eq. (30.5) we define the self-inductance
of the circuit as
(self-inductance)
(30.6)
When there is no danger of confusion with mutual inductance, the self-inductance
is called simply the inductance. Comparing Eqs. (30.5) and (30.6), we see that
the units of self-inductance are the same as those of mutual inductance; the SI
unit of self-inductance is the henry.
If the current i in the circuit changes, so does the flux 
from rearranging
Eq. (30.6) and taking the derivative with respect to time, the rates of change are
related by
From Faraday’s law for a coil with 
turns, Eq. (29.4), the self-induced emf is
so it follows that
(30.7)
The minus sign in Eq. (30.7) is a reflection of Lenz’s law; it says that the self-
induced emf in a circuit opposes any change in the current in that circuit. (Later
in this section we’ll explore in greater depth the significance of this minus sign.)
Equation (30.7) also states that the self-inductance of a circuit is the magni-
tude of the self-induced emf per unit rate of change of current. This relationship
makes it possible to measure an unknown self-inductance in a relatively simple
way: Change the current in the circuit at a known rate 
measure the induced
emf, and take the ratio to determine 
Inductors As Circuit Elements
A circuit device that is designed to have a particular inductance is called an
inductor, or a choke. The usual circuit symbol for an inductor is
Like resistors and capacitors, inductors are among the indispensable circuit
elements of modern electronics. Their purpose is to oppose any variations in the
current through the circuit. An inductor in a direct-current circuit helps to main-
tain a steady current despite any fluctuations in the applied emf; in an alternating-
current circuit, an inductor tends to suppress variations of the current that are
more rapid than desired. In this chapter and the next we will explore the behavior
and applications of inductors in circuits in more detail.
To understand the behavior of circuits containing inductors, we need to
develop a general principle analogous to Kirchhoff’s loop rule (discussed in
L.
di>dt,
E = -L di
dt  1self-induced emf)
E = -N d£B>dt,
N
N d£B
dt
= L di
dt
£B;
L = N£B
i   
L
£B
i,
N
Self-inductance: If the current i in the coil is
changing, the changing flux through the coil
induces an emf
in the coil.
i
+
B
S
30.4 The current i in the circuit causes a
magnetic field 
in the coil and hence a
flux through the coil.
B
S
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

Section 26.2). To apply that rule, we go around a conducting loop, measuring
potential differences across successive circuit elements as we go. The algebraic
sum of these differences around any closed loop must be zero because the electric
field produced by charges distributed around the circuit is conservative. In Sec-
tion 29.7 we denoted such a conservative field as 
When an inductor is included in the circuit, the situation changes. The mag-
netically induced electric field within the coils of the inductor is not conservative;
as in Section 29.7, we’ll denote it by 
We need to think very carefully about
the roles of the various fields. Let’s assume we are dealing with an inductor
whose coils have negligible resistance. Then a negligibly small electric field is
required to make charge move through the coils, so the total electric field
within the coils must be zero, even though neither field is individually
zero. Because 
is nonzero, there have to be accumulations of charge on the ter-
minals of the inductor and the surfaces of its conductors to produce this field.
Consider the circuit shown in Fig. 30.5; the box contains some combination of
batteries and variable resistors that enables us to control the current i in the cir-
cuit. According to Faraday’s law, Eq. (29.10), the line integral of 
around the
circuit is the negative of the rate of change of flux through the circuit, which in
turn is given by Eq. (30.7). Combining these two relationships, we get
where we integrate clockwise around the loop (the direction of the assumed cur-
rent). But 
is different from zero only within the inductor. Therefore the inte-
gral of 
around the whole loop can be replaced by its integral only from a to b
through the inductor; that is,
Next, because 
at each point within the inductor coils, we can
rewrite this as
But this integral is just the potential 
of point a with respect to point b, so we
finally obtain
(30.8)
We conclude that there is a genuine potential difference between the terminals of
the inductor, associated with conservative, electrostatic forces, despite the fact
that the electric field associated with the magnetic induction effect is nonconserv-
ative. Thus we are justified in using Kirchhoff’s loop rule to analyze circuits that
include inductors. Equation (30.8) gives the potential difference across an induc-
tor in a circuit.
CAUTION
Self-induced emf opposes changes in current Note that the self-induced emf
does not oppose the current i itself; rather, it opposes any change
in the current. Thus
the circuit behavior of an inductor is quite different from that of a resistor. Figure 30.6 com-
pares the behaviors of a resistor and an inductor and summarizes the sign relationships. ❙
Applications of Inductors
Because an inductor opposes changes in current, it plays an important role in flu-
orescent light fixtures (Fig. 30.7). In such fixtures, current flows from the wiring
1di>dt2
Vab = Va - Vb = L di
dt
Vab
L
b
a
E
S
c# dl
S = L di
dt
E
S
c  E
S
n  0
L
b
a
E
S
n# dl
S = -L di
dt
E
S
n
E
S
n
C
E
S
n# dl
S = -L di
dt
E
S
n
E
S
c
E
S
c  E
S
n
E
S
n.
E
S
c.
996
CHAPTER 30 Inductance
b
a
i
i
L
Variable
source
of emf
30.5 A circuit containing a source of
emf and an inductor. The source is vari-
able, so the current i and its rate of change
can be varied.
di>dt
i constant: di/dt 5 0
i increasing: di/dt . 0
i decreasing: di/dt , 0
a
b
E 5 0
(a) Resistor with current i flowing from a to b:
potential drops from a to b.
(b) Inductor with constant current i flowing
from a to b: no potential difference.
(c) Inductor with increasing current i flowing
from a to b: potential drops from a to b.
(d) Inductor with decreasing current i flowing
from a to b: potential increases from a to b.
a
b
+
-
+
-
E
i
Vab 5 iR . 0
a
b
R
+
-
a
b
E
. 0
Vab 5 L di
dt
, 0
Vab 5 L di
dt
5 0
Vab 5 L di
dt
30.6 (a) The potential difference across a
resistor depends on the current. (b), (c), (d)
The potential difference across an inductor
depends on the rate of change of the current.

30.2 Self-Inductance and Inductors
997
into the gas that fills the tube, ionizing the gas and causing it to glow. However,
an ionized gas or plasma is a highly nonohmic conductor: The greater the cur-
rent, the more highly ionized the plasma becomes and the lower its resistance. If
a sufficiently large voltage is applied to the plasma, the current can grow so much
that it damages the circuitry outside the fluorescent tube. To prevent this problem,
an inductor or magnetic ballast is put in series with the fluorescent tube to keep
the current from growing out of bounds.
The ballast also makes it possible for the fluorescent tube to work with the
alternating voltage provided by household wiring. This voltage oscillates sinu-
soidally with a frequency of 60 Hz, so that it goes momentarily to zero 120 times
per second. If there were no ballast, the plasma in the fluorescent tube would rap-
idly deionize when the voltage went to zero and the tube would shut off. With a
ballast present, a self-induced emf sustains the current and keeps the tube lit.
Magnetic ballasts are also used for this purpose in streetlights (which obtain their
light from a glowing vapor of mercury or sodium atoms) and in neon lights. (In
compact fluorescent lamps, the magnetic ballast is replaced by a more compli-
cated scheme for regulating current. This scheme utilizes transistors, discussed in
Chapter 42.)
The self-inductance of a circuit depends on its size, shape, and number of
turns. For 
turns close together, it is always proportional to 
It also depends
on the magnetic properties of the material enclosed by the circuit. In the follow-
ing examples we will assume that the circuit encloses only vacuum (or air, which
from the standpoint of magnetism is essentially vacuum). If, however, the flux is
concentrated in a region containing a magnetic material with permeability 
then in the expression for 
we must replace 
(the permeability of vacuum) by
as discussed in Section 28.8. If the material is diamagnetic or para-
magnetic, this replacement makes very little difference, since 
is very close to
1. If the material is ferromagnetic, however, the difference is of crucial impor-
tance. A solenoid wound on a soft iron core having 
can have an
inductance approximately 5000 times as great as that of the same solenoid with
an air core. Ferromagnetic-core inductors are very widely used in a variety of
electronic and electric-power applications.
An added complication is that with ferromagnetic materials the magnetization
is in general not a linear function of magnetizing current, especially as saturation
is approached. As a result, the inductance is not constant but can depend on current
in a fairly complicated way. In our discussion we will ignore this complication
and assume always that the inductance is constant. This is a reasonable assumption
even for a ferromagnetic material if the magnetization remains well below the
saturation level.
Because automobiles contain steel, a ferromagnetic material, driving an
automobile over a coil causes an appreciable increase in the coil’s induc-
tance. This effect is used in traffic light sensors, which use a large, current-carrying
coil embedded under the road surface near an intersection. The circuitry con-
nected to the coil detects the inductance change as a car drives over. When a pre-
programmed number of cars have passed over the coil, the light changes to green
to allow the cars through the intersection.
Km = 5000
Km
m = Kmm0,
m0
B
m,
N 2.
N
30.7 These fluorescent light tubes are
wired in series with an inductor, or ballast,
that helps to sustain the current flowing
through the tubes.
?
