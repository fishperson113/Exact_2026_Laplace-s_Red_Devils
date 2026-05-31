Example 26.1
Equivalent resistance
Find the equivalent resistance of the network in Fig. 26.3a and the
current in each resistor. The source of emf has negligible internal
resistance.
SOLUTION
IDENTIFY and SET UP: This network of three resistors is a combination
of series and parallel resistances, as in Fig. 26.1c. We determine
(a)
+
a
c
b
E  18 V, r  0
6 V
3 V
4 V
(b)
(c)
(f)
(e)
(d)
26.3 Steps in reducing a combination of resistors to a single equivalent resistor and finding the current in each resistor.
Continued

the equivalent resistance of the parallel 
and 
resistors, and
then that of their series combination with the 
resistor: This is
the equivalent resistance 
of the network as a whole. We then
find the current in the emf, which is the same as that in the 
resistor. The potential difference is the same across each of the par-
allel 
and 
resistors; we use this to determine how the cur-
rent is divided between these.
EXECUTE: Figures 26.3b and 26.3c show successive steps in 
reducing the network to a single equivalent resistance 
From 
Eq. (26.2), the 
and 
resistors in parallel in Fig. 26.3a are
equivalent to the single 
resistor in Fig. 26.3b:
[Equation (26.3) gives the same result.] From Eq. (26.1) the series
combination of this 
resistor with the 
resistor is equiva-
lent to the single 
resistor in Fig. 26.3c.
6-Æ
4-Æ
2-Æ
1
R6 Æ+3 Æ
=
1
6 Æ +
1
3 Æ =
1
2 Æ
2-Æ
3-Æ
6-Æ
Req.
3-Æ
6-Æ
4-Æ
Req
4-Æ
3-Æ
6-Æ
854
CHAPTER 26 Direct-Current Circuits
We reverse these steps to find the current in each resistor of the
original network. In the circuit shown in Fig. 26.3d (identical to
Fig. 26.3c), the current is 
So
the current in the 
and 
resistors in Fig. 26.3e (identical to
Fig. 26.3b) is also 3 A. The potential difference 
across the 
resistor is therefore 
This
potential difference must also be 6 V in Fig. 26.3f (identical to 
Fig. 26.3a). From 
the currents in the 
and 
resistors in Fig. 26.3f are respectively 
and
.
EVALUATE: Note that for the two resistors in parallel between
points c and b in Fig. 26.3f, there is twice as much current
through the 
resistor as through the 
resistor; more cur-
rent goes through the path of least resistance, in accordance with
Eq. (26.4). Note also that the total current through these two
resistors is 3 A, the same as it is through the 
resistor between
points a and c.
4-Æ
6-Æ
3-Æ
16 V2>13 Æ2 = 2 A
16 V2>16 Æ2 = 1 A
3-Æ
6-Æ
I = Vcb>R,
Vcb = IR = 13 A212 Æ2 = 6 V.
2-Æ
Vcb
2-Æ
4-Æ
I = Vab>R = 118 V2>16 Æ2 = 3 A.
Example 26.2
Series versus parallel combinations
Two identical light bulbs, each with resistance 
are
connected to a source with 
and negligible internal
resistance. Find the current through each bulb, the potential 
difference across each bulb, and the power delivered to each
bulb and to the entire network if the bulbs are connected (a) in
series and (b) in parallel. (c) Suppose one of the bulbs burns out;
that is, its filament breaks and current can no longer flow
through it. What happens to the other bulb in the series case? In
the parallel case?
SOLUTION
IDENTIFY and SET UP: The light bulbs are just resistors in simple
series and parallel connections (Figs. 26.4a and 26.4b). Once we
find the current I through each bulb, we can find the power deliv-
ered to each bulb using Eq. (25.18), 
EXECUTE: (a) From Eq. (26.1) the equivalent resistance of the two
bulbs between points a and c in Fig. 26.4a is 
. In series, the current is the same through each bulb:
Since the bulbs have the same resistance, the potential difference is
the same across each bulb:
From Eq. (25.18), the power delivered to each bulb is
The total power delivered to both bulbs is 
(b) If the bulbs are in parallel, as in Fig. 26.4b, the potential differ-
ence
across each bulb is the same and equal to 8 V, the terminal
voltage of the source. Hence the current through each light bulb is
Vde
Ptot = 2P = 16 W.
P = Vab
2
R
= Vbc
2
R
=
14 V22
2 Æ
= 8 W
P = I 2R = 12 A2212 Æ2 = 8 W  or
Vab = Vbc = IR = 12 A212 Æ2 = 4 V
I = Vac
Req
= 8 V
4 Æ = 2 A
4 Æ
Req = 2R = 212 Æ2 =
P = I 2R = V2>R.
E = 8 V
R = 2 Æ,
(a) Light bulbs in series
(b) Light bulbs in parallel
26.4 Our sketches for this problem.
and the power delivered to each bulb is
Both the potential difference across each bulb and the current
through each bulb are twice as great as in the series case. Hence
the power delivered to each bulb is four times greater, and each
bulb is brighter.
The total power delivered to the parallel network is 
four times greater than in the series case. The
2P = 64 W,
Ptotal =
P = Vde
2
R
=
18 V22
2 Æ
= 32 W
P = I 2R = 14 A2212 Æ2 = 32 W  or
I = Vde
R = 8 V
2 Æ = 4 A

26.2 Kirchhoff’s Rules
855
increased power compared to the series case isn’t obtained “for
free”; energy is extracted from the source four times more rapidly
in the parallel case than in the series case. If the source is a battery,
it will be used up four times as fast.
(c) In the series case the same current flows through both bulbs.
If one bulb burns out, there will be no current in the circuit, and
neither bulb will glow.
In the parallel case the potential difference across either bulb is
unchanged if a bulb burns out. The current through the functional
bulb and the power delivered to it are unchanged.
EVALUATE: Our calculation isn’t completely accurate, because the
resistance 
of real light bulbs depends on the potential dif-
ference V across the bulb. That’s because the filament resistance
increases with increasing operating temperature and therefore with
increasing V. But bulbs connected in series across a source do in
fact glow less brightly than when connected in parallel across the
same source (Fig. 26.5).
R = V>I
26.5 When connected to the same source, two light bulbs in
series (shown at top) draw less power and glow less brightly than
when they are in parallel (shown at bottom).
26.2 Kirchhoff’s Rules
Many practical resistor networks cannot be reduced to simple series-parallel
combinations. Figure 26.6a shows a dc power supply with emf 
charging a bat-
tery with a smaller emf 
and feeding current to a light bulb with resistance R.
Figure 26.6b is a “bridge” circuit, used in many different types of measurement
and control systems. (Problem 26.81 describes one important application of a
“bridge” circuit.) To compute the currents in these networks, we’ll use the 
techniques developed by the German physicist Gustav Robert Kirchhoff
(1824-1887).
First, here are two terms that we will use often. A junction in a circuit is 
a point where three or more conductors meet. A loop is any closed conducting
path. In Fig. 26.6a points a and b are junctions, but points c and d are not; 
in Fig. 26.6b the points a, b, c, and d are junctions, but points e and f are not.
The blue lines in Figs. 26.6a and 26.6b show some possible loops in these 
circuits.
Kirchhoff’s rules are the following two statements:
Kirchhoff’s junction rule: The algebraic sum of the currents into any junction
is zero. That is,
(junction rule, valid at any junction)
(26.5)
Kirchhoff’s loop rule: The algebraic sum of the potential differences in any
loop, including those associated with emfs and those of resistive elements, must
equal zero. That is,
(loop rule, valid for any closed loop)
(26.6)
a V = 0  
a I = 0  
E2
E1
Test Your Understanding of Section 26.1
Suppose all three of the
resistors shown in Fig. 26.1 have the same resistance, so 
Rank the four arrangements shown in parts (a)-(d) of Fig. 26.1 in order of their
equivalent resistance, from highest to lowest.
❙
R1 = R2 = R3 = R.
Junction
Not a 
junction
Not a 
junction
Junction
Loop 2
Loop 1
(1)
(2)
(3)
(4)
Loop 3
(a)
(b)
R
b
c
d
a
r2
E2
r1
E1
r
E
c
f
e
a
d
b
R1
R2
R3
R4
Rm
+
+
+
26.6 Two networks that cannot be
reduced to simple series-parallel combina-
tions of resistors.

The junction rule is based on conservation of electric charge. No charge
can accumulate at a junction, so the total charge entering the junction per unit
time must equal the total charge leaving per unit time (Fig. 26.7a). Charge per
unit time is current, so if we consider the currents entering a junction to be
positive and those leaving to be negative, the algebraic sum of currents into a
junction must be zero. It’s like a T branch in a water pipe (Fig. 26.7b); if you
have a total of 1 liter per minute coming in the two pipes, you can’t have 
3 liters per minute going out the third pipe. We may as well confess that we
used the junction rule (without saying so) in Section 26.1 in the derivation of
Eq. (26.2) for resistors in parallel.
The loop rule is a statement that the electrostatic force is conservative. Sup-
pose we go around a loop, measuring potential differences across successive cir-
cuit elements as we go. When we return to the starting point, we must find that
the algebraic sum of these differences is zero; otherwise, we could not say that
the potential at this point has a definite value.
Sign Conventions for the Loop Rule
In applying the loop rule, we need some sign conventions. Problem-Solving
Strategy 26.2 describes in detail how to use these, but here’s a quick overview.
We first assume a direction for the current in each branch of the circuit and mark
it on a diagram of the circuit. Then, starting at any point in the circuit, we imag-
ine traveling around a loop, adding emfs and IR terms as we come to them. When
we travel through a source in the direction from 
to 
the emf is considered to
be positive; when we travel from 
to 
the emf is considered to be negative
(Fig. 26.8a). When we travel through a resistor in the same direction as the
assumed current, the IR term is negative because the current goes in the direction
of decreasing potential. When we travel through a resistor in the direction
opposite to the assumed current, the IR term is positive because this represents a
rise of potential (Fig. 26.8b).
Kirchhoff’s two rules are all we need to solve a wide variety of network
problems. Usually, some of the emfs, currents, and resistances are known, 
and others are unknown. We must always obtain from Kirchhoff’s rules a
number of independent equations equal to the number of unknowns so that 
we can solve the equations simultaneously. Often the hardest part of the solu-
tion is not understanding the basic principles but keeping track of algebraic
signs!
-,
+
+,
-
856
CHAPTER 26 Direct-Current Circuits
26.7 Kirchhoff’s junction rule states that
as much current flows into a junction as
flows out of it.
(b) Sign conventions for resistors
(a) Sign conventions for emfs
Travel
Travel
Travel
Travel
R
+
-
E
1E: Travel direction
from - to +:
1IR: Travel opposite
to current direction: 
2IR: Travel in
current direction: 
2E: Travel direction
from + to -:
+
+
-
-
R
+
-
E
I
I
26.8 Use these sign conventions when
you apply Kirchhoff’s loop rule. In each
part of the figure “Travel” is the direction
that we imagine going around the loop,
which is not necessarily the direction of
the current.
The flow rate of 
water leaving the
pipe equals the flow
rate entering it.
The current leaving
a junction equals the
current entering it.
(b) Water-pipe analogy
(a) Kirchhoff’s junction rule
I2
I1  I2
I1
Junction

26.2 Kirchhoff’s Rules
857
Problem-Solving Strategy 26.2
Kirchhoff’s Rules
IDENTIFY the relevant concepts: Kirchhoff’s rules are useful for
analyzing any electric circuit.
SET UP the problem using the following steps:
1. Draw a circuit diagram, leaving room to label all quantities,
known and unknown. Indicate an assumed direction for each
unknown current and emf. (Kirchhoff’s rules will yield the
magnitudes and directions of unknown currents and emfs. If the
actual direction of a quantity is opposite to your assumption,
the resulting quantity will have a negative sign.)
2. As you label currents, it helpful to use Kirchhoff’s junction
rule, as in Fig. 26.9, so as to express the currents in terms of as
few quantities as possible.
3. Identify the target variables.
EXECUTE the solution as follows:
1. Choose any loop in the network and choose a direction (clock-
wise or counterclockwise) to travel around the loop as you
apply Kirchhoff’s loop rule. The direction need not be the same
as any assumed current direction.
2. Travel around the loop in the chosen direction, adding potential
differences algebraically as you cross them. Use the sign con-
ventions of Fig. 26.8.
3. Equate the sum obtained in step 2 to zero in accordance with
the loop rule.
4. If you need more independent equations, choose another loop
and repeat steps 1-3; continue until you have as many inde-
pendent equations as unknowns or until every circuit element
has been included in at least one loop.
5. Solve the equations simultaneously to determine the unknowns.
6. You can use the loop-rule bookkeeping system to find the
potential 
of any point a with respect to any other point b.
Start at b and add the potential changes you encounter in going
from b to a, using the same sign rules as in step 2. The alge-
braic sum of these changes is 
EVALUATE your answer: Check all the steps in your algebra. Apply
steps 1 and 2 to a loop you have not yet considered; if the sum of
potential drops isn’t zero, you’ve made an error somewhere.
Vab = Va - Vb.
Vab
(a) Three unknown currents: I1, I2, I3
(b) Applying the junction rule to point a eliminates I3.
r1
E1
r2
E2
R1
R2
a
R3
I3
I1
I2
I1
I2
r1
E1
r2
E2
R1
R2
a
R3
I1 1 I2
I1
I2
I1
I2
+
+
+
+
26.9 Applying the junction rule to point a reduces the number of unknown currents from three to two.
