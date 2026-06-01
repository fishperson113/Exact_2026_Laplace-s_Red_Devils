828

CHAPTER 25 Current, Resistance, and Electromotive Force

Example 25.3

Temperature dependence of resistance

Suppose the resistance of a copper wire is
the resistance at

100°C.

and

0°C

1.05 Æ

at

20°C.

Find

R = 11.05 Æ251 + 30.00393 1C°2-143100°C - 20°C46

= 1.38 Æ at T = 100°C

SOLUTION

IDENTIFY  and SET  UP: We are given the resistance
at a reference temperature
T = 0°C
the resistances at
taking the temperature coefﬁcient of resistivity from Table 25.2.

R0 = 1.05 Æ
We use Eq. (25.12) to ﬁnd
(our target variables),

T0 = 20°C.
and

T = 100°C

EXECUTE: From Table 25.2,
from Eq. (25.12),

a = 0.00393 1C°2-1

for copper. Then

R = R031 + a1T - T024

= 11.05 Æ251 + 30.00393 1C°2-1430°C - 20°C46
= 0.97 Æ at T = 0°C

100°C

is greater than that at

EVALUATE: The resistance at
by a
11.38 Æ2>10.97 Æ2 = 1.42
factor of
: Raising the temperature of
0°C
to
copper  wire  from
increases  its  resistance  by  42%.
V = IR,
this  means  that  42%  more  voltage  is
From  Eq.  (25.11),
100°C
0°C.
required  to  produce  the  same  current  at
Designers of electric circuits that must operate over a wide temper-
ature range must take this substantial effect into account.

than  at

100°C

0°C

Test Your Understanding of Section 25.3 Suppose you increase the voltage
across the copper wire in Examples 25.2 and 25.3. The increased voltage causes more
current to ﬂow, which makes the temperature of the wire increase. (The same thing hap-
pens to the coils of an electric oven or a toaster when a voltage is applied to them. We’ll
explore this issue in more depth in Section 25.5.) If you double the voltage across the
wire, the current in the wire increases. By what factor does it increase? (i) 2; (ii) greater
than 2; (iii) less than 2.

❙

25.4 Electromotive Force and Circuits

25.11 If an electric ﬁeld is produced
inside a conductor that is not part of a
complete circuit, current ﬂows for only
a very short time.

S
(a) An electric field E1 produced inside an
isolated conductor causes a current.

I

S
E1
S
J

I

(b) The current causes charge to build up at
the ends.

–
–
–

S
E1

I

S
J

I

S
S E2
Etotal

+
+
+

The charge buildup produces an opposing
field E2, thus reducing the current.

S

S

(c) After a very short time E2 has the same
magnitude as E1; then the total field is Etotal
and the current stops completely.

S

S

–
–
–
–
–
–

I (cid:4) 0

S

J (cid:2) 0

S
E1
S
Etotal

(cid:2) 0

S
E2

+
+
+
+
+

r

For a conductor to have a steady current, it must be part of a path that forms a
S
E
closed loop or complete circuit. Here’s why. If you establish an electric ﬁeld
1
that is not part of a complete cir-
inside an isolated conductor with resistivity
(Fig. 25.11a). As a
cuit, a current begins to ﬂow with current density
result a net positive charge quickly accumulates at one end of the conductor and a
net  negative  charge  accumulates  at  the  other  end  (Fig.  25.11b).  These  charges
themselves produce an electric ﬁeld
causing
2
the total electric ﬁeld and hence the current to decrease. Within a very small frac-
tion  of  a  second,  enough  charge  builds  up  on  the  conductor  ends  that  the  total
electric ﬁeld
as well, and
the current stops altogether (Fig. 25.11c). So there can be no steady motion of
charge in such an incomplete circuit.

in the direction opposite to

inside the conductor. Then

1 (cid:4) E

2 (cid:2) 0

(cid:2) E

(cid:2) E

(cid:2) 0

1>r

S
E

S
E

S
E

S
J

S
J

1,

S

S

S

To see how to maintain a steady current in a complete circuit, we recall a basic
fact about electric potential energy: If a charge  goes around a complete circuit
and returns to its starting point, the potential energy must be the same at the end
of the round trip as at the beginning. As described in Section 25.3, there is always
a decrease in potential energy when charges move through an ordinary conduct-
ing material with resistance. So there must be some part of the circuit in which
the potential energy increases.

q

The  problem  is  analogous  to  an  ornamental  water  fountain  that  recycles  its
water. The water pours out of openings at the top, cascades down over the ter-
races  and  spouts  (moving  in  the  direction  of  decreasing  gravitational  potential
energy), and collects in a basin in the bottom. A pump then lifts it back to the top
(increasing  the  potential  energy)  for  another  trip. Without  the  pump,  the  water
would just fall to the bottom and stay there.

5 0

Electromotive Force
In an electric circuit there must be a device somewhere in the loop that acts like
the water pump in a water fountain (Fig. 25.12). In this device a charge travels

25.4 Electromotive Force and Circuits

829

25.12 Just as a water fountain requires a
pump, an electric circuit requires a source
of electromotive force to sustain a steady
current.

“uphill,”  from  lower  to  higher  potential  energy,  even  though  the  electrostatic
force is trying to push it from higher to lower potential energy. The direction of
current in such a device is from lower to higher potential, just the opposite of
what happens in an ordinary conductor. The influence that makes current flow
from lower to higher potential is called electromotive force (abbreviated emf
and pronounced “ee-em-eff”). This is a poor term because emf is not a force but
an  energy-per-unit-charge  quantity,  like  potential.  The  SI  unit  of  emf  is  the
same as that for potential, the volt
A typical flashlight battery
1.5 V;
of  work  on  every
has  an  emf  of
E
coulomb of charge that passes through it. We’ll use the symbol
(a script capital
E) for emf.

this  means  that  the  battery  does

11 V = 1 J>C2.

1.5 J

Every  complete  circuit  with  a  steady  current  must  include  some  device  that
provides emf. Such a device is called a source of emf. Batteries, electric genera-
tors, solar cells, thermocouples, and fuel cells are all examples of sources of emf.
All such devices convert energy of some form (mechanical, chemical, thermal,
and so on) into electric potential energy and transfer it into the circuit to which
the  device  is  connected. An  ideal source  of  emf  maintains  a  constant  potential
difference between its terminals, independent of the current through it. We deﬁne
electromotive force quantitatively as the magnitude of this potential difference.
As we will see, such an ideal source is a mythical beast, like the frictionless plane
and the massless rope. We will discuss later how real-life sources of emf differ in
their behavior from this idealized model.

b

a

a

S
E

+,

and

, marked

is maintained at higher potential than terminal

Figure 25.13 is a schematic diagram of an ideal source of emf that maintains a
,  called  the  terminals of  the
potential  difference  between  conductors
b
device. Terminal
,
-.
marked  Associated with this potential difference is an electric ﬁeld
in the
region around the terminals, both inside and outside the source. The electric ﬁeld
a
b
to
, as shown. A charge  within the source
inside the device is directed from
S
S
e (cid:2) qE
.
F
But the source also provides an additional
experiences an electric force
S
n.
F
inﬂuence,  which  we  represent  as  a  nonelectrostatic  force
This  force,  oper-
ating inside the device, pushes charge from
in an “uphill” direction against
Thus  maintains the potential difference between the ter-
the electric force
minals. If  were not present, charge would ﬂow between the terminals until the
potential difference was zero. The origin of the additional inﬂuence
depends
on the kind of source. In a generator it results from magnetic-ﬁeld forces on mov-
ing charges. In a battery or fuel cell it is associated with diffusion processes and
varying electrolyte concentrations resulting from chemical reactions. In an elec-
trostatic machine such as a Van de Graaff generator (see Fig. 22.26), an actual
mechanical force is applied by a moving belt or wheel.

S
e.
F

S
F
n

S
F
n

S
F
n

to

q

a

b

b

q

to

is moved from

If a positive charge
S
F
n

a
does a positive amount of work

qVab,
is the (positive) potential of point  with respect to point

inside the source, the nonelectro-
Wn = qE
on the charge. This dis-
static force
S
F
e,
so  the  potential  energy
placement  is  opposite to  the  electrostatic  force
where
associated  with  the  charge  increases by  an  amount  equal  to
Vab = Va - Vb
b
. For
the ideal source of emf that we’ve described,
are equal in magnitude
but opposite in direction, so the total work done on the charge
is zero; there is
an increase in potential energy but no change in the kinetic energy of the charge.
It’s  like  lifting  a  book  from  the  ﬂoor  to  a  high  shelf  at  constant  speed.  The
increase  in  potential  energy  is  just  equal  to  the  nonelectrostatic  work
so
qE = qVab,

a
and

Wn,

S
F
n

S
F
e

or

q

Vab = E

(ideal source of emf)

(25.13)

to
Now let’s make a complete circuit by connecting a wire with resistance
the terminals of a source (Fig. 25.14). The potential difference between terminals
a
b
and  sets up an electric ﬁeld within the wire; this causes current to ﬂow around
the loop from
, from higher to lower potential. Where the wire bends,
equal amounts of positive and negative charge persist on the “inside” and “outside”

toward

R

a

b

25.13 Schematic diagram of a source of
emf in an “open-circuit” situation. The
S
e (cid:2) qE
electric-ﬁeld force
F
S
F
nonelectrostatic force
n
positive charge

and the
are shown for a

.q

S

Ideal emf
source

Terminal at higher
potential

Va

+

a

5 E

Vab

S
E

Vb

Nonelectrostatic
force tending to
move charge to
higher potential

Force due to
electric field

S

5 qE

S
Fn
q
S
Fe

b

Terminal at lower
potential

When the emf source is not part of a closed
5 Fe and there is no net motion of
circuit, Fn
charge between the terminals.

PhET: Battery Voltage
PhET: Signal Circuit
ActivPhysics 12.1: DC Series Circuits
(Qualitative)

830

CHAPTER 25 Current, Resistance, and Electromotive Force

S

25.14 Schematic diagram of an ideal
source of emf in a complete circuit. The
S
e (cid:2) qE
and the non-
electric-ﬁeld force
F
S
are shown for a posi-
F
electrostatic force
n
tive charge
a
direction from
a
and from

to  within the source.

. The current is in the

in the external circuit

to

b

q

b

Potential across terminals creates electric
field in circuit, causing charges to move.

Ideal emf
source

Va

+

a

I

S
E

5 E

Vab

S
E

Vb

S
Fn

S
Fe

b

S
E

I

S
E

When a real
(as opposed
to ideal) emf source
is connected to a circuit, Vab and thus Fe fall, so
. Fe and Fn does work on the charges.
that Fn

S

I

Application Danger: Electric Ray!
Electric rays deliver electric shocks to stun
their prey and to discourage predators. (In
ancient Rome, physicians practiced a primitive
form of electroconvulsive therapy by placing
electric rays on their patients to cure
headaches and gout.) The shocks are pro-
duced by specialized ﬂattened cells called elec-
troplaques. Such a cell moves ions across
membranes to produce an emf of about
0.05 V. Thousands of electroplaques are
stacked on top of each other, so their emfs
add to a total of as much as 200 V. These
stacks make up more than half of an electric
ray’s body mass. A ray can use these to
deliver an impressive current of up to 30 A for
a few milliseconds.

Vab = IR.
E = Vab = IR

of the bend. These charges exert the forces that cause the current to follow the
bends in the wire.

From  Eq.  (25.11) the  potential  difference  between  the  ends  of  the  wire  in

Fig. 25.14 is given by

Combining with Eq. (25.13), we have

(ideal source of emf)

(25.14)

That is, when a positive charge  ﬂows around the circuit, the potential rise
as
it  passes  through  the  ideal  source  is  numerically  equal  to  the  potential  drop
Vab = IR
are
known, this relationship determines the current in the circuit.

as  it  passes  through  the  remainder  of  the  circuit.  Once

and

R

E

q

E

CAUTION Current is not “used up” in a circuit It’s a common misconception that
in a closed circuit, current is something that squirts out of the positive terminal of a
battery and is consumed or “used up” by the time it reaches the negative terminal. In fact
the current is the same at every point in a simple loop circuit like that in Fig. 25.14, even if
the  thickness  of  the  wires  is  different  at  different  points  in  the  circuit.  This  happens
because charge is conserved (that is, it can be neither created nor destroyed) and because
charge cannot accumulate in the circuit devices we have described. If charge did accumu-
late,  the  potential  differences  would  change  with  time.  It’s  like  the  ﬂow  of  water  in  an
ornamental fountain; water ﬂows out of the top of the fountain at the same rate at which it
reaches the bottom, no matter what the dimensions of the fountain. None of the water is
“used up” along the way! ❙

?

Internal Resistance
Real  sources  of  emf  in  a  circuit  don’t  behave  in  exactly  the  way  we  have
described; the potential difference across a real source in a circuit is not equal to
the emf as in Eq. (25.14). The reason is that charge moving through the material
of any real source encounters resistance. We call this the internal resistance of
r
the source, denoted by  . If this resistance behaves according to Ohm’s law,
is
,  it
r
constant  and  independent  of  the  current
. As  the  current  moves  through
Ir
. Thus, when a current is
experiences an associated drop in potential equal to
b
a
ﬂowing through a source from the negative terminal
,
to the positive terminal
Vab
the potential difference

between the terminals is

r

I

Vab = E - Ir

(terminal voltage, source
with internal resistance)

(25.15)

E

a

q

Ir

A

S
n,
F

qVab
qE

Vab,
representing  the  potential  drop  across  the  internal  resistance

called the terminal voltage, is less than the emf  because of
r
.
as a charge  moves
done by the nonelec-
since  some  potential  energy  is  lost  in  traversing  the  internal

The potential
the  term
Expressed another way, the increase in potential energy
b
from
to  within the source is now less than the work
trostatic  force
resistance.
1.5-V
of the battery
I = 0
is  equal  to
in
Eq. (25.15). If the battery is part of a complete circuit through which current is
For a real source of emf, the
ﬂowing, the terminal voltage will be less than
terminal voltage equals the emf only if no current is ﬂowing through the source
(Fig. 25.15). Thus we can describe the behavior of a source in terms of two prop-
erties:  an  emf  which  supplies  a  constant  potential  difference  independent  of
r
current, in series with an internal resistance  .

only  if  no  current  is  ﬂowing  through  it  so  that

battery has an emf of
1.5 V

but the terminal voltage

1.5 V.

1.5 V,

Vab

E,

The current in the external circuit connected to the source terminals  and

a

b

is

still determined by

Vab = IR.

Combining this with Eq. (25.15), we ﬁnd

E - Ir = IR

or

I =

E
R + r

(current, source with
internal resistance)

(25.16)

25.4 Electromotive Force and Circuits

831

That is, the current equals the source emf divided by the total circuit resistance
1R + r2.

CAUTION A battery is not a “current source” You might have thought that a battery or
other source of emf always produces the same current, no matter what circuit it’s used in.
Equation (25.16) shows that this isn’t so! The greater the resistance R of the external cir-
cuit, the less current the source will produce. It’s analogous to pushing an object through a
thick, viscous liquid such as oil or molasses; if you exert a certain steady push (emf), you
can  move  a  small  object  at  high  speed  (small
large  )  or  a  large  object  at  low  speed
(large

, small  ). ❙

R,

R

I

I

25.15 The emf of this battery—that is,
the terminal voltage when it’s not connected
to anything—is
battery has internal resistance, the terminal
voltage of the battery is less than
when it is supplying current to a light bulb.

But because the

12 V.

12 V

Symbols for Circuit Diagrams
An important part of analyzing any electric circuit is drawing a schematic circuit
diagram. Table 25.4 shows the usual symbols used in circuit diagrams. We will
use  these  symbols  extensively  in  this  chapter  and  the  next. We  usually  assume
that  the  wires  that  connect  the  various  elements  of  the  circuit  have  negligible
resistance; from Eq. (25.11),
the potential difference between the ends
of such a wire is zero.

V = IR,

Table 25.4 includes two meters that are used to measure the properties of cir-
cuits. Idealized meters do not disturb the circuit in which they are connected. A
voltmeter, introduced in Section 23.2, measures the potential difference between
its terminals; an idealized voltmeter has inﬁnitely large resistance and measures
potential difference without having any current diverted through it. An ammeter
measures the current passing through it; an idealized ammeter has zero resist-
ance and has no potential difference between its terminals. Because meters act as
part of the circuit in which they are connected, these properties are important to
remember.

Table 25.4 Symbols for Circuit Diagrams

or

R

+ E

+E

+ E

V

A

Conductor with negligible resistance

Resistor

Source of emf (longer vertical line always represents the positive
terminal, usually the terminal with higher potential)

Source of emf with internal resistance  ( can be placed on either
side)

rr

Voltmeter (measures potential difference between its terminals)

Ammeter (measures current through it)

Conceptual Example 25.4 A source in an open circuit

E = 12 V

r

Figure 25.16 shows a source (a battery) with emf
and
internal resistance  (cid:4)
2 Æ.
(For comparison, the internal resist-
ance of a commercial
lead storage battery is only a few thou-
sandths of an ohm.) The wires to the left of  and to the right of the
are not connected to anything. Determine the respec-
ammeter
tive readings
and the ideal-
ized ammeter

and I of the idealized voltmeter

Vab
.A

12-V

A

V

a

25.16 A source of emf in an open circuit.

Vab

V

+

a

r 5 2 V, E 5 12 V

A

b

Continued

832

CHAPTER 25 Current, Resistance, and Electromotive Force

SOLUTION

There  is  zero current  because  there  is  no  complete  circuit.  (Our
idealized voltmeter has an inﬁnitely large resistance, so no current
ﬂows through it.) Hence the ammeter reads
Because there is
no current through the battery, there is no potential difference across

I = 0.

Example 25.5

A source in a complete circuit

Vab

its internal resistance. From Eq. (25.15) with
the potential
difference
across the battery terminals is equal to the emf. So
The  terminal  voltage  of  a
the  voltmeter  reads
real,  nonideal  source  equals  the  emf  only if  there  is  no  current
ﬂowing through the source, as in this example.

Vab = E = 12 V.

I = 0,

4-Æ

We add a
resistor to the battery in Conceptual Example 25.4,
forming  a  complete  circuit  (Fig.  25.17).  What  are  the  voltmeter
and ammeter readings

and I now?

Vab

SOLUTION

IDENTIFY  and SET  UP: Our  target  variables  are  the  current
through the circuit
ﬁnd  using Eq. (25.16). To ﬁnd
or Eq. (25.15).

I
. We ﬁrst
we can use either Eq. (25.11)

and the potential difference

aa¿b¿b

Vab,

Vab

I

25.17 A source of emf in a complete circuit.

Vab

5 Va(cid:2)b(cid:2)

V

a

+

b

I

r 5 2 V, E 5 12 V

A

I

a(cid:2)

R 5 4 V

b(cid:2)

Conceptual Example 25.6 Using voltmeters and ammeters

We move the voltmeter and ammeter in Example 25.5 to different
positions  in  the  circuit.  What  are  the  readings  of  the  ideal  volt-
meter and ammeter in the situations shown in (a) Fig. 25.18a and
(b) Fig. 25.18b?

SOLUTION

(a) The voltmeter now measures the potential difference between
Vab = Va¿b¿,
points
so the voltmeter
and  As in Example 25.5,
reads the same as in Example 25.5: Va¿b¿ = 8 V.

b¿.

a¿

25.18 Different placements of a voltmeter and an ammeter in a
complete circuit.

(a)

(b)

a

+

b

a

+

b

I

A

r 5 2 V, E 5 12 V

I

A

r 5 2 V, E 5 12 V

V

a(cid:2)

R 5 4 V

b(cid:2)

a(cid:2)

R 5 4 V

b(cid:2)

Vbb(cid:2)

V

Va(cid:2)b(cid:2)

EXECUTE: The  ideal  ammeter  has  zero  resistance,  so  the  total
From Eq. (25.16), the
resistance external to the source is
aa¿b¿b
current through the circuit

R = 4 Æ.
is then

I =

E
R + r

=

12 V
4 Æ + 2 Æ

= 2 A

Our idealized conducting wires and the idealized ammeter have
zero resistance, so there is no potential difference between points
a
b¿;
and
Vab
by considering  and  as the terminals of the resistor: From Ohm’s
a
law, Eq. (25.11), we then have

or between points  and

Vab = Va¿b¿.

We ﬁnd

that is,

a¿

b

b

Va¿b¿ = IR = 12 A214 Æ2 = 8 V

Alternatively,  we  can  consider  a and b as  the  terminals  of  the
source. Then, from Eq. (25.15),

Vab = E - Ir = 12 V - 12 A212 Æ2 = 8 V

Either way, we see that the voltmeter reading is 8 V.

EVALUATE:  With current ﬂowing through the source, the terminal
.E
is less than the emf  The smaller the internal resist-
voltage
Vab
ance  , the less the difference between

and

Vab

.E

r

CAUTION Current in a simple loop As charges move through a
resistor, there is a decrease in electric potential energy, but there is
no change in the current. The current in a simple loop is the same
at every point; it is not “used up” as it moves through a resistor.
Hence the ammeter in Fig. 25.17 (“downstream” of the
resis-
tor)  and  the  ammeter  in  Fig.  25.18b  (“upstream”  of  the  resistor)
both read

I = 2 A.

4-Æ

❙

(b)  There  is  no  current  through  the  ideal  voltmeter  because  it
has inﬁnitely large resistance. Since the voltmeter is now part of
the circuit, there is no current at all in the circuit, and the ammeter
reads

I = 0.

b

b¿.

Vbb¿

Since

and
Va¿b¿ = IR = 0,
a¿

The  voltmeter  measures  the  potential  difference
I = 0,

between
points
the  potential  difference  across  the
resistor is
and the potential difference between the
ends  and
is equal
a
the terminal voltage of the source. As in Conceptual Exam-
to
Vab,
ple 25.4, there is no current, so the terminal voltage equals the emf,
and the voltmeter reading is

of the idealized ammeter is also zero. So

Vab = E = 12 V.

Vbb¿

This example shows that ammeters and voltmeters are circuit ele-
ments, too. Moving the voltmeter from the position in Fig. 25.18a to
that in Fig. 25.18b makes large changes in the current and potential
differences in the circuit. If you want to measure the potential differ-
ence between two points in a circuit without disturbing the circuit,
use a voltmeter as in Fig. 25.17 or 25.18a, not as in Fig. 25.18b.

Example 25.7

A source with a short circuit

25.4 Electromotive Force and Circuits

833

In the circuit of Example 25.5 we replace the
zero-resistance conductor. What are the meter readings now?

resistor with a

4-Æ

SOLUTION

IDENTIFY  and SET  UP:  Figure  25.19 shows  the  new  circuit.  Our
I
Vab.
target variables are again  and
There is now a zero-resistance
path between points a and
, through the lower loop, so the poten-
tial difference between these points must be zero.

b

25.19 Our sketch for this problem.

Vab = IR = I102 = 0,

EXECUTE: We  must  have
the current. We can therefore ﬁnd the current  from Eq. (25.15):
Vab = E - Ir = 0
= 12 V
2 Æ

= 6 A

I =

E

r

I

no  matter  what

EVALUATE:  The  current  has  a  different  value  than  in  Example
25.5, even though the same battery is used; the current depends
on both the internal resistance  and the resistance of the external
circuit.

r

The situation here is called a short circuit. The external-circuit
resistance is zero, because terminals of the battery are connected
directly to each other. The short-circuit current is equal to the emf
E
divided by the internal resistance  . Warning: Short circuits can
be  dangerous! An  automobile  battery  or  a  household  power  line
has very small internal resistance (much less than in these exam-
ples), and the short-circuit current can be great enough to melt a
small wire or cause a storage battery to explode.

r

Potential Changes Around a Circuit
The net change in potential energy for a charge  making a round trip around a
complete circuit must be zero. Hence the net change in potential around the cir-
cuit must also be zero; in other words, the algebraic sum of the potential differ-
ences and emfs around the loop is zero. We can see this by rewriting Eq. (25.16)
in the form

q

E - Ir - IR = 0

E

Ir

is associated with the emf, and potential drops of

IR
A potential gain of
are associated with the internal resistance of the source and the external circuit,
respectively. Figure 25.20 is a graph showing how the potential varies as we go
around the complete circuit of Fig. 25.17. The horizontal axis doesn’t necessar-
ily represent actual distances, but rather various points in the loop. If we take
the potential to be zero at the negative terminal of the battery, then we have a
rise
in  the  external
resistor, and as we finish our trip around the loop, the potential is back where it
started.

in  the  battery  and  an  additional  drop

and  a  drop

and

IR

Ir

E

25.20 Potential rises and drops in a
circuit.

2 A

2 A

+

2 A

12 V

2 V

2 A

4 V

In this section we have considered only situations in which the resistances are
ohmic. If the circuit includes a nonlinear device such as a diode (see Fig. 25.10b),
Eq.  (25.16) is  still  valid  but  cannot  be  solved  algebraically  because
is  not  a
I
constant. In such a situation, the current  can be found by using numerical tech-
niques.

R

Finally, we remark that Eq. (25.15) is not always an adequate representation
of  the  behavior  of  a  source.  The  emf  may  not  be  constant,  and  what  we  have
described as an internal resistance may actually be a more complex voltage–current
relationship that doesn’t obey Ohm’s law. Nevertheless, the concept of internal
resistance  frequently  provides  an  adequate  description  of  batteries,  generators,
and other energy converters. The principal difference between a fresh ﬂashlight
battery and an old one is not in the emf, which decreases only slightly with use,
but in the internal resistance, which may increase from less than an ohm when the
battery is fresh to as much as
or more after long use. Similarly, a car bat-
tery can deliver less current to the starter motor on a cold morning than when the
battery is warm, not because the emf is appreciably less but because the internal
resistance increases with decreasing temperature.

1000 Æ

V

12 V

8 V

O

Ir 5 4 V

E 5 12 V

IR 5 8 V
