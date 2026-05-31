Example 25.3
Temperature dependence of resistance
Suppose the resistance of a copper wire is 
at 
Find
the resistance at 
and 
SOLUTION
IDENTIFY and SET UP: We are given the resistance 
at a reference temperature 
We use Eq. (25.12) to find
the resistances at 
and 
(our target variables),
taking the temperature coefficient of resistivity from Table 25.2.
EXECUTE: From Table 25.2, 
for copper. Then
from Eq. (25.12),
= 0.97 Æ at T = 0°C
= 11.05 Æ251 + 30.00393 1C°2-1430°C - 20°C46
R = R031 + a1T - T024
a = 0.00393 1C°2-1
T = 100°C
T = 0°C
T0 = 20°C.
R0 = 1.05 Æ
100°C.
0°C
20°C.
1.05 Æ
EVALUATE: The resistance at 
is greater than that at 
by a
factor of 
: Raising the temperature of
copper wire from 
to 
increases its resistance by 42%.
From Eq. (25.11), 
this means that 42% more voltage is
required to produce the same current at 
than at 
Designers of electric circuits that must operate over a wide temper-
ature range must take this substantial effect into account.
0°C.
100°C
V = IR,
100°C
0°C
11.38 Æ2>10.97 Æ2 = 1.42
0°C
100°C
= 1.38 Æ at T = 100°C
R = 11.05 Æ251 + 30.00393 1C°2-143100°C - 20°C46
Test Your Understanding of Section 25.3
Suppose you increase the voltage
across the copper wire in Examples 25.2 and 25.3. The increased voltage causes more
current to flow, which makes the temperature of the wire increase. (The same thing hap-
pens to the coils of an electric oven or a toaster when a voltage is applied to them. We’ll
explore this issue in more depth in Section 25.5.) If you double the voltage across the
wire, the current in the wire increases. By what factor does it increase? (i) 2; (ii) greater
than 2; (iii) less than 2.
❙
(c) After a very short time E2 has the same
magnitude as E1; then the total field is Etotal 5 0
and the current stops completely.
I
I
J
S
E1
S
(a) An electric field E1 produced inside an
isolated conductor causes a current.
S
S
S
S
S
-
-
-
I
I
+
+
+
J
S
E1
S
Etotal
S E2
S
(b) The current causes charge to build up at
the ends.
The charge buildup produces an opposing
field E2, thus reducing the current.
--
----
I  0
+
+
+
+
+
J  0
S
E1
S
Etotal  0
S
E2
S
25.11 If an electric field is produced 
inside a conductor that is not part of a
complete circuit, current flows for only 
a very short time.

25.4 Electromotive Force and Circuits
829
“uphill,” from lower to higher potential energy, even though the electrostatic
force is trying to push it from higher to lower potential energy. The direction of
current in such a device is from lower to higher potential, just the opposite of
what happens in an ordinary conductor. The influence that makes current flow
from lower to higher potential is called electromotive force (abbreviated emf
and pronounced “ee-em-eff”). This is a poor term because emf is not a force but
an energy-per-unit-charge quantity, like potential. The SI unit of emf is the
same as that for potential, the volt 
A typical flashlight battery
has an emf of 
this means that the battery does 
of work on every
coulomb of charge that passes through it. We’ll use the symbol 
(a script capital
E) for emf.
Every complete circuit with a steady current must include some device that
provides emf. Such a device is called a source of emf. Batteries, electric genera-
tors, solar cells, thermocouples, and fuel cells are all examples of sources of emf.
All such devices convert energy of some form (mechanical, chemical, thermal,
and so on) into electric potential energy and transfer it into the circuit to which
the device is connected. An ideal source of emf maintains a constant potential
difference between its terminals, independent of the current through it. We define
electromotive force quantitatively as the magnitude of this potential difference.
As we will see, such an ideal source is a mythical beast, like the frictionless plane
and the massless rope. We will discuss later how real-life sources of emf differ in
their behavior from this idealized model.
Figure 25.13 is a schematic diagram of an ideal source of emf that maintains a
potential difference between conductors 
and , called the terminals of the
device. Terminal , marked 
is maintained at higher potential than terminal ,
marked 
Associated with this potential difference is an electric field 
in the
region around the terminals, both inside and outside the source. The electric field
inside the device is directed from 
to , as shown. A charge 
within the source
experiences an electric force 
But the source also provides an additional
influence, which we represent as a nonelectrostatic force 
This force, oper-
ating inside the device, pushes charge from to in an “uphill” direction against
the electric force 
Thus 
maintains the potential difference between the ter-
minals. If 
were not present, charge would flow between the terminals until the
potential difference was zero. The origin of the additional influence 
depends
on the kind of source. In a generator it results from magnetic-field forces on mov-
ing charges. In a battery or fuel cell it is associated with diffusion processes and
varying electrolyte concentrations resulting from chemical reactions. In an elec-
trostatic machine such as a Van de Graaff generator (see Fig. 22.26), an actual
mechanical force is applied by a moving belt or wheel.
If a positive charge 
is moved from 
to 
inside the source, the nonelectro-
static force 
does a positive amount of work 
on the charge. This dis-
placement is opposite to the electrostatic force 
so the potential energy
associated with the charge increases by an amount equal to 
where
is the (positive) potential of point 
with respect to point . For
the ideal source of emf that we’ve described, 
and 
are equal in magnitude
but opposite in direction, so the total work done on the charge 
is zero; there is
an increase in potential energy but no change in the kinetic energy of the charge.
It’s like lifting a book from the floor to a high shelf at constant speed. The
increase in potential energy is just equal to the nonelectrostatic work 
so
or
(ideal source of emf)
(25.13)
Now let’s make a complete circuit by connecting a wire with resistance 
to
the terminals of a source (Fig. 25.14). The potential difference between terminals
and sets up an electric field within the wire; this causes current to flow around
the loop from 
toward , from higher to lower potential. Where the wire bends,
equal amounts of positive and negative charge persist on the “inside” and “outside”
b
a
b
a
R
Vab = E
qE = qVab,
Wn,
q
F
S
n
F
S
e
b
a
Vab = Va - Vb
qVab,
F
S
e,
Wn = qE
F
S
n
a
b
q
F
S
n
F
S
n
F
S
n
F
S
e.
a
b
F
S
n.
F
S
e  qE
S.
q
b
a
E
S
-.
b
+,
a
b
a
E
1.5 J
1.5 V;
11 V = 1 J>C2.
25.12 Just as a water fountain requires a
pump, an electric circuit requires a source
of electromotive force to sustain a steady
current.
+
Ideal emf
source
Va
a
q
b
Vab 5 E
Vb
Terminal at higher
potential
Terminal at lower
potential
E
S
Fn
S
Fe 5 qE
S
S
Nonelectrostatic
force tending to
move charge to
higher potential
Force due to
electric field
When the emf source is not part of a closed
circuit, Fn 5 Fe and there is no net motion of
charge between the terminals.
25.13 Schematic diagram of a source of
emf in an “open-circuit” situation. The
electric-field force 
and the 
nonelectrostatic force 
are shown for a
positive charge .q
F
S
n
F
S
e  qE
S
PhET: Battery Voltage
PhET: Signal Circuit
ActivPhysics 12.1: DC Series Circuits 
(Qualitative)

of the bend. These charges exert the forces that cause the current to follow the
bends in the wire.
From Eq. (25.11) the potential difference between the ends of the wire in 
Fig. 25.14 is given by 
Combining with Eq. (25.13), we have
(ideal source of emf)
(25.14)
That is, when a positive charge 
flows around the circuit, the potential rise
as
it passes through the ideal source is numerically equal to the potential drop
as it passes through the remainder of the circuit. Once 
and 
are
known, this relationship determines the current in the circuit.
CAUTION
Current is not “used up” in a circuit It’s a common misconception that
in a closed circuit, current is something that squirts out of the positive terminal of a
battery and is consumed or “used up” by the time it reaches the negative terminal. In fact
the current is the same at every point in a simple loop circuit like that in Fig. 25.14, even if
the thickness of the wires is different at different points in the circuit. This happens
because charge is conserved (that is, it can be neither created nor destroyed) and because
charge cannot accumulate in the circuit devices we have described. If charge did accumu-
late, the potential differences would change with time. It’s like the flow of water in an
ornamental fountain; water flows out of the top of the fountain at the same rate at which it
reaches the bottom, no matter what the dimensions of the fountain. None of the water is
“used up” along the way! ❙
Internal Resistance
Real sources of emf in a circuit don’t behave in exactly the way we have
described; the potential difference across a real source in a circuit is not equal to
the emf as in Eq. (25.14). The reason is that charge moving through the material
of any real source encounters resistance. We call this the internal resistance of
the source, denoted by . If this resistance behaves according to Ohm’s law, is
constant and independent of the current . As the current moves through , it
experiences an associated drop in potential equal to 
. Thus, when a current is
flowing through a source from the negative terminal 
to the positive terminal ,
the potential difference 
between the terminals is
(terminal voltage, source 
(25.15)
with internal resistance)
The potential 
called the terminal voltage, is less than the emf 
because of
the term 
representing the potential drop across the internal resistance .
Expressed another way, the increase in potential energy 
as a charge moves
from 
to 
within the source is now less than the work 
done by the nonelec-
trostatic force 
since some potential energy is lost in traversing the internal
resistance.
A
battery has an emf of 
but the terminal voltage 
of the battery
is equal to 
only if no current is flowing through it so that 
in 
Eq. (25.15). If the battery is part of a complete circuit through which current is
flowing, the terminal voltage will be less than 
For a real source of emf, the
terminal voltage equals the emf only if no current is flowing through the source
(Fig. 25.15). Thus we can describe the behavior of a source in terms of two prop-
erties: an emf 
which supplies a constant potential difference independent of
current, in series with an internal resistance .
The current in the external circuit connected to the source terminals and is
still determined by 
Combining this with Eq. (25.15), we find
or
(25.16)
(current, source with
internal resistance)
I =
E
R + r
E - Ir = IR
Vab = IR.
b
a
r
E,
1.5 V.
I = 0
1.5 V
Vab
1.5 V,
1.5-V
F
S
n,
qE
a
b
q
qVab
r
Ir
E
Vab,
Vab = E - Ir
Vab
a
b
Ir
r
I
r
r
R
E
Vab = IR
E
q
E = Vab = IR
Vab = IR.
830
CHAPTER 25 Current, Resistance, and Electromotive Force
+
S
S
When a real
(as opposed 
to ideal) emf source
is connected to a circuit, Vab and thus Fe fall, so
that Fn . Fe and Fn does work on the charges.
E
S
E
S
E
S
E
S
S
Ideal emf
source
Va
a
b
Vab 5 E
Vb
Fn
Fe
Potential across terminals creates electric
field in circuit, causing charges to move.
I
I
I
25.14 Schematic diagram of an ideal
source of emf in a complete circuit. The
electric-field force 
and the non-
electrostatic force 
are shown for a posi-
tive charge . The current is in the
direction from to in the external circuit
and from to within the source.
a
b
b
a
q
F
S
n
F
S
e  qE
S
?
Application Danger: Electric Ray!
Electric rays deliver electric shocks to stun
their prey and to discourage predators. (In
ancient Rome, physicians practiced a primitive
form of electroconvulsive therapy by placing
electric rays on their patients to cure
headaches and gout.) The shocks are pro-
duced by specialized flattened cells called elec-
troplaques. Such a cell moves ions across
membranes to produce an emf of about 
0.05 V. Thousands of electroplaques are
stacked on top of each other, so their emfs
add to a total of as much as 200 V. These
stacks make up more than half of an electric
ray’s body mass. A ray can use these to
deliver an impressive current of up to 30 A for
a few milliseconds.

25.4 Electromotive Force and Circuits
831
That is, the current equals the source emf divided by the total circuit resistance
CAUTION
A battery is not a “current source” You might have thought that a battery or
other source of emf always produces the same current, no matter what circuit it’s used in.
Equation (25.16) shows that this isn’t so! The greater the resistance R of the external cir-
cuit, the less current the source will produce. It’s analogous to pushing an object through a
thick, viscous liquid such as oil or molasses; if you exert a certain steady push (emf), you
can move a small object at high speed (small 
large ) or a large object at low speed
(large , small ). ❙
Symbols for Circuit Diagrams
An important part of analyzing any electric circuit is drawing a schematic circuit
diagram. Table 25.4 shows the usual symbols used in circuit diagrams. We will
use these symbols extensively in this chapter and the next. We usually assume
that the wires that connect the various elements of the circuit have negligible
resistance; from Eq. (25.11), 
the potential difference between the ends
of such a wire is zero.
Table 25.4 includes two meters that are used to measure the properties of cir-
cuits. Idealized meters do not disturb the circuit in which they are connected. A
voltmeter, introduced in Section 23.2, measures the potential difference between
its terminals; an idealized voltmeter has infinitely large resistance and measures
potential difference without having any current diverted through it. An ammeter
measures the current passing through it; an idealized ammeter has zero resist-
ance and has no potential difference between its terminals. Because meters act as
part of the circuit in which they are connected, these properties are important to
remember.
V = IR,
I
R
I
R,
1R + r2.
25.15 The emf of this battery-that is,
the terminal voltage when it’s not connected
to anything-is 
But because the
battery has internal resistance, the terminal
voltage of the battery is less than 
when it is supplying current to a light bulb.
12 V
12 V.
R
A
V
+
E
+ E
or
+
E
Table 25.4 Symbols for Circuit Diagrams
Conductor with negligible resistance
Resistor
Source of emf (longer vertical line always represents the positive
terminal, usually the terminal with higher potential)
Source of emf with internal resistance ( can be placed on either
side)
Voltmeter (measures potential difference between its terminals)
Ammeter (measures current through it)
r
r
Conceptual
