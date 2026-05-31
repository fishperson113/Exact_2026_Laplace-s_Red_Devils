Example 25.7
A source with a short circuit
In the circuit of Example 25.5 we replace the 
resistor with a
zero-resistance conductor. What are the meter readings now?
SOLUTION
IDENTIFY and SET UP: Figure 25.19 shows the new circuit. Our
target variables are again and 
There is now a zero-resistance
path between points a and , through the lower loop, so the poten-
tial difference between these points must be zero.
b
Vab.
I
4-Æ
EXECUTE: We must have 
no matter what
the current. We can therefore find the current from Eq. (25.15):
EVALUATE: The current has a different value than in Example
25.5, even though the same battery is used; the current depends
on both the internal resistance and the resistance of the external
circuit.
The situation here is called a short circuit. The external-circuit
resistance is zero, because terminals of the battery are connected
directly to each other. The short-circuit current is equal to the emf
divided by the internal resistance . Warning: Short circuits can
be dangerous! An automobile battery or a household power line
has very small internal resistance (much less than in these exam-
ples), and the short-circuit current can be great enough to melt a
small wire or cause a storage battery to explode.
r
E
r
I = E
r = 12 V
2 Æ = 6 A
Vab = E - Ir = 0
I
Vab = IR = I102 = 0,
25.19 Our sketch for this problem.
O
V
12 V
2 A
4 V
2 V
12 V
Ir 5 4 V
IR 5 8 V
E 5 12 V
2 A
2 A
2 A
8 V
+
25.20 Potential rises and drops in a
circuit.

25.5 Energy and Power in Electric Circuits
Let’s now look at some energy and power relationships in electric circuits. The
box in Fig. 25.21 represents a circuit element with potential difference
between its terminals and current passing through it in the direc-
tion from 
toward . This element might be a resistor, a battery, or something
else; the details don’t matter. As charge passes through the circuit element, the
electric field does work on the charge. In a source of emf, additional work is done
by the force 
that we mentioned in Section 25.4.
As an amount of charge passes through the circuit element, there is a change
in potential energy equal to 
For example, if 
and 
is
positive, potential energy decreases as the charge “falls” from potential 
to
lower potential 
The moving charges don’t gain kinetic energy, because the
current (the rate of charge flow) out of the circuit element must be the same as the
current into the element. Instead, the quantity 
represents energy transferred
into the circuit element. This situation occurs in the coils of a toaster or electric
oven, in which electrical energy is converted to thermal energy.
If the potential at a is lower than at b, then 
is negative and there is a net
transfer of energy out of the circuit element. The element then acts as a source,
delivering electrical energy into the circuit to which it is attached. This is the
usual situation for a battery, which converts chemical energy into electrical
energy and delivers it to the external circuit. Thus 
can denote either a quan-
tity of energy delivered to a circuit element or a quantity of energy extracted from
that element.
In electric circuits we are most often interested in the rate at which energy is
either delivered to or extracted from a circuit element. If the current through the
element is , then in a time interval 
an amount of charge 
passes
through the element. The potential energy change for this amount of charge is
Dividing this expression by 
, we obtain the rate at which
energy is transferred either into or out of the circuit element. The time rate of
energy transfer is power, denoted by , so we write
(rate at which energy is delivered to 
(25.17)
or extracted from a circuit element)
The unit of 
is one volt, or one joule per coulomb, and the unit of is one
ampere, or one coulomb per second. Hence the unit of 
is one watt, as it
should be:
Let’s consider a few special cases.
Power Input to a Pure Resistance
If the circuit element in Fig. 25.21 is a resistor, the potential difference is
From Eq. (25.17) the electrical power delivered to the resistor by the
circuit is
(25.18)
(power delivered to a resistor)
P = VabI = I 2R = Vab
2
R
Vab = IR.
11 J>C211 C>s2 = 1 J>s = 1 W
P = VabI
I
Vab
P = VabI
P
dt
Vab dQ = Vab I dt.
dQ = I dt
dt
I
qVab
Vab
qVab
Vb.
Va
Vab = Va - Vb
q 7 0
qVab.
q
F
S
n
b
a
I
Va - Vb = Vab
834
CHAPTER 25 Current, Resistance, and Electromotive Force
Test Your Understanding of Section 25.4
Rank the following circuits
in order from highest to lowest current. (i) a 
resistor connected to a 
battery that has an internal resistance of 
(ii) a 
resistor connected to
a 
battery that has a terminal voltage of 
but an unknown internal resistance;
(iii) an unknown resistor connected to a 
battery that has an internal resistance of
and a terminal voltage of 
❙
11.0 V.
0.20 Æ
12.0-V
3.6 V
4.0-V
1.8-Æ
0.10 Æ;
1.5-V
1.4-Æ
I
I
a
b
Va
Vb
Circuit
element
25.21 The power input to the circuit
element between and is 
VabI.
Vb2I =
P = 1Va -
b
a
PhET: Battery-Resistor Circuit
PhET: Circuit Construction Kit (AC+DC)
PhET: Circuit Construction Kit (DC Only)
PhET: Ohm’s Law

25.5 Energy and Power in Electric Circuits
835
In this case the potential at 
(where the current enters the resistor) is always
higher than that at (where the current exits). Current enters the higher-potential
terminal of the device, and Eq. (25.18) represents the rate of transfer of electric
potential energy into the circuit element.
What becomes of this energy? The moving charges collide with atoms in the
resistor and transfer some of their energy to these atoms, increasing the internal
energy of the material. Either the temperature of the resistor increases or there is
a flow of heat out of it, or both. In any of these cases we say that energy is
dissipated in the resistor at a rate 
Every resistor has a power rating, the max-
imum power the device can dissipate without becoming overheated and dam-
aged. Some devices, such as electric heaters, are designed to get hot and transfer
heat to their surroundings. But if the power rating is exceeded, even such a
device may melt or even explode.
Power Output of a Source
The upper rectangle in Fig. 25.22a represents a source with emf 
and internal
resistance , connected by ideal (resistanceless) conductors to an external circuit
represented by the lower box. This could describe a car battery connected to one
of the car’s headlights (Fig. 25.22b). Point is at higher potential than point , so
and 
is positive. Note that the current is leaving the source at the
higher-potential terminal (rather than entering there). Energy is being delivered
to the external circuit, at a rate given by Eq. (25.17):
For a source that can be described by an emf 
and an internal resistance , we
may use Eq. (25.15):
Multiplying this equation by , we find
(25.19)
What do the terms 
and 
mean? In Section 25.4 we defined the emf 
as
the work per unit charge performed on the charges by the nonelectrostatic force
as the charges are pushed “uphill” from to in the source. In a time , a charge
flows through the source; the work done on it by this nonelectrostatic
force is 
Thus 
is the rate at which work is done on the circulat-
ing charges by whatever agency causes the nonelectrostatic force in the source.
This term represents the rate of conversion of nonelectrical energy to electrical
energy within the source. The term 
is the rate at which electrical energy is
dissipated in the internal resistance of the source. The difference 
is the
net electrical power output of the source-that is, the rate at which the source
delivers electrical energy to the remainder of the circuit.
Power Input to a Source
Suppose that the lower rectangle in Fig. 25.22a is itself a source, with an emf
larger than that of the upper source and with its emf opposite to that of the
upper source. Figure 25.23 shows a practical example, an automobile battery
(the upper circuit element) being charged by the car’s alternator (the lower ele-
ment). The current in the circuit is then opposite to that shown in Fig. 25.22;
the lower source is pushing current backward through the upper source.
Because of this reversal of current, instead of Eq. (25.15) we have for the upper
source
and instead of Eq. (25.19), we have
(25.20)
P = VabI = EI + I 2r
Vab = E + Ir
I
EI - I 2r
I 2r
EI
E dQ = EI dt.
dQ = I dt
dt
a
b
E
I 2r
EI
P = VabI = EI - I 2r
I
Vab = E - Ir
r
E
P = VabI
I
Vab
Va 7 Vb
b
a
r
E
I 2R.
b
a
+
+
+
+
Headlight
S
S
S
• The emf source converts nonelectrical to
 
electrical energy at a rate EI.
• Its internal resistance dissipates energy at
 
a rate I2r.
• The difference EI 2 I2r is its power output.
(a) Diagrammatic circuit
(b) A real circuit of the type shown in (a)
I
I
a
b
E, r
emf source with
internal resistance r
a
b
q
External
circuit
Fe
v
Fn
b
a
I
I
b
a
Battery
25.22 Energy conversion in a simple
circuit.
+
-
b
a
Battery
(small emf)
+
-
a
b
I
I
Alternator
(large emf)
q
Fe
S
v
r
Fn
S
25.23 When two sources are connected
in a simple loop circuit, the source with the
larger emf delivers energy to the other
source.

Work is being done on, rather than by, the agent that causes the nonelectrostatic
force in the upper source. There is a conversion of electrical energy into nonelec-
trical energy in the upper source at a rate 
The term 
in Eq. (25.20) is again
the rate of dissipation of energy in the internal resistance of the upper source, and
the sum 
is the total electrical power input to the upper source. This is
what happens when a rechargeable battery (a storage battery) is connected to a
charger. The charger supplies electrical energy to the battery; part of it is con-
verted to chemical energy, to be reconverted later, and the remainder is dissipated
(wasted) in the battery’s internal resistance, warming the battery and causing a
heat flow out of it. If you have a power tool or laptop computer with a recharge-
able battery, you may have noticed that it gets warm while it is charging.
EI + I 2r
I 2r
EI.
836
CHAPTER 25 Current, Resistance, and Electromotive Force
Problem-Solving Strategy 25.1
Power and Energy in Circuits
IDENTIFY the relevant concepts: The ideas of electric power input
and output can be applied to any electric circuit. Many problems
will ask you to explicitly consider power or energy.
SET UP the problem using the following steps:
1. Make a drawing of the circuit.
2. Identify the circuit elements, including sources of emf and
resistors. We will introduce other circuit elements later, includ-
ing capacitors (Chapter 26) and inductors (Chapter 30).
3. Identify the target variables. Typically they will be the power
input or output for each circuit element, or the total amount of
energy put into or taken out of a circuit element in a given time.
EXECUTE the solution as follows:
1. A source of emf 
delivers power 
into a circuit when current
flows through the source in the direction from
to 
(For
example, energy is converted from chemical energy in a bat-
tery, or from mechanical energy in a generator.) In this case
there is a positive power output to the circuit or, equivalently, a
negative power input to the source.
2. A source of emf takes power 
from a circuit when current
passes through the source from
to
(This occurs in charg-
ing a storage battery, when electrical energy is converted to
chemical energy.) In this case there is a negative power output
-.
+
I
E
+.
-
I
I
E
E
to the circuit or, equivalently, a positive power input to the
source.
3. There is always a positive power input to a resistor through
which current flows, irrespective of the direction of current
flow. This process removes energy from the circuit, converting
it to heat at the rate 
where 
is the potential
difference across the resistor.
4. Just as in item 3, there always is a positive power input to the
internal resistance 
of a source through which current flows,
irrespective of the direction of current flow. This process like-
wise removes energy from the circuit, converting it into heat at
the rate 
5. If the power into or out of a circuit element is constant, the
energy delivered to or extracted from that element is the product
of power and elapsed time. (In Chapter 26 we will encounter sit-
uations in which the power is not constant. In such cases, calcu-
lating the total energy requires an integral over the relevant
time interval.)
EVALUATE your answer: Check your results; in particular, check
that energy is conserved. This conservation can be expressed in
either of two forms: “
” or “the
algebraic sum of the power inputs to the circuit elements is zero.”
net power input = net power output
I 2r.
r
V
VI = I 2R = V2>R,
