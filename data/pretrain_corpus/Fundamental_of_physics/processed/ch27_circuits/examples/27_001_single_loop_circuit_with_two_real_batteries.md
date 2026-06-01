Sample Problem 27.01
Single-loop circuit with two real batteries
The emfs and resistances in the circuit of Fig. 27-8a have the
following values:
#1 ! 4.4 V,
#2 ! 2.1 V,
r1 ! 2.3 0,
r2 ! 1.8 0,
R ! 5.5 0.
(a) What is the current i in the circuit?
KEY IDEA
We can get an expression involving the current i in this
single-loop circuit by applying the loop rule, in which we
sum the potential changes around the full loop.
Calculations: Although knowing the direction of i is not
necessary, we can easily determine it from the emfs of the
Additional examples, video, and practice available at WileyPLUS
Figure 27-8 (a) A single-loop circuit containing two real batteries
and a resistor.The batteries oppose each other; that is, they tend to
send current in opposite directions through the resistor. (b) A
graph of the potentials, counterclockwise from point a, with the
potential at a arbitrarily taken to be zero. (To better link the circuit
with the graph, mentally cut the circuit at a and then unfold the left
side of the circuit toward the left and the right side of the circuit
toward the right.)
R
Battery 1
r1
i
(a)
a
Battery 2
1
b
c
2
r2
i
a
b
c
a
r2
R
r1
i
1
2
Battery 1
Battery 2
Resistor
Va
0
-1
-2
-3
-4
-5
1 = 4.4 V
ir1
iR
ir2
2 = 2.1 V
Vb
Va
Vc
Potential (V)
(b)

Multiloop Circuits
Figure 27-9 shows a circuit containing more than one loop. For simplicity, we
assume the batteries are ideal. There are two junctions in this circuit, at b and d,
and there are three branches connecting these junctions.The branches are the left
branch (bad), the right branch (bcd), and the central branch (bd). What are the
currents in the three branches?
We arbitrarily label the currents, using a different subscript for each branch.
Current i1 has the same value everywhere in branch bad, i2 has the same value
everywhere in branch bcd, and i3 is the current through branch bd.The directions
of the currents are assumed arbitrarily.
Consider junction d for a moment: Charge comes into that junction via
incoming currents i1 and i3, and it leaves via outgoing current i2. Because there is
no variation in the charge at the junction, the total incoming current must equal
the total outgoing current:
i1 % i3 ! i2.
(27-18)
You can easily check that applying this condition to junction b leads to exactly
the same equation. Equation 27-18 thus suggests a general principle:
781
27-2 MULTILOOP CIRCUITS
27-2 MULTILOOP CIRCUITS
After reading this module, you should be able to . . .
27.17 Apply the junction rule.
27.18 Draw a schematic diagram for a battery and three
parallel resistors and distinguish it from a diagram with a
battery and three series resistors.
27.19 Identify that resistors in parallel have the same potential
difference, which is the same value that their equivalent
resistor has.
27.20 Calculate the resistance of the equivalent resistor of
several resistors in parallel.
27.21 Identify that the total current through parallel resistors
is the sum of the currents through the individual resistors.
27.22 For a circuit with a battery and some resistors in parallel
and some in series, simplify the circuit in steps by finding
equivalent resistors, until the current through the battery
can be determined, and then reverse the steps to find
the currents and potential differences of the individual
resistors.
27.23 If a circuit cannot be simplified by using equivalent
resistors, identify the several loops in the circuit, choose
names and directions for the currents in the branches, set
up loop equations for the various loops, and solve these
simultaneous equations for the unknown currents.
27.24 In a circuit with identical real batteries in series, replace
them with a single ideal battery and a single resistor.
27.25 In a circuit with identical real batteries in parallel, re-
place them with a single ideal battery and a single resistor.
Learning Objectives
●When resistances are in parallel, they have the same potential difference. The equivalent resistance that can replace a parallel
combination of resistances is given by
(n resistances in parallel).
1
Req
! '
n
j!1
1
Rj
Key Idea
Figure 27-9 A multiloop circuit consisting of
three branches: left-hand branch bad, right-
hand branch bcd, and central branch bd.
The circuit also consists of three loops: left-
hand loop badb, right-hand loop bcdb, and
big loop badcb.
R 2
R3
R1
a
b 
c 
d
 i 1
 i 3
 i 2
+ - 
1 
2 
- + 
The current into the junction
must equal the current out
(charge is conserved).
JUNCTION RULE: The sum of the currents entering any junction must be
equal to the sum of the currents leaving that junction.
This rule is often called Kirchhoff’s junction rule (or Kirchhoff’s current law). It is
simply a statement of the conservation of charge for a steady flow of charge-
there is neither a buildup nor a depletion of charge at a junction. Thus, our basic
tools for solving complex circuits are the loop rule (based on the conservation of
energy) and the junction rule (based on the conservation of charge).

Equation 27-18 is a single equation involving three unknowns. To solve the
circuit completely (that is, to find all three currents), we need two more equations
involving those same unknowns.We obtain them by applying the loop rule twice.
In the circuit of Fig. 27-9, we have three loops from which to choose: the left-hand
loop (badb), the right-hand loop (bcdb), and the big loop (badcb). Which two
loops we choose does not matter-let’s choose the left-hand loop and the right-
hand loop.
If we traverse the left-hand loop in a counterclockwise direction from point
b, the loop rule gives us
#1 # i1R1 % i3R3 ! 0.
(27-19)
If we traverse the right-hand loop in a counterclockwise direction from point b,
the loop rule gives us
#i3R3 # i2R2 # #2 ! 0.
(27-20)
We now have three equations (Eqs. 27-18, 27-19, and 27-20) in the three unknown
currents, and they can be solved by a variety of techniques.
If we had applied the loop rule to the big loop, we would have obtained
(moving counterclockwise from b) the equation
#1 # i1R1 # i2R2 # #2 ! 0.
However, this is merely the sum of Eqs. 27-19 and 27-20.
Resistances in Parallel
Figure 27-10a shows three resistances connected in parallel to an ideal battery
of emf #. The term “in parallel” means that the resistances are directly wired
together on one side and directly wired together on the other side, and that a
potential difference V is applied across the pair of connected sides.Thus, all three
resistances have the same potential difference V across them, producing a cur-
rent through each. In general,
782
CHAPTER 27
CIRCUITS
Figure 27-10 (a) Three resistors connected in parallel across points a and b. (b) An equiva-
lent circuit, with the three resistors replaced with their equivalent resistance Req.
When a potential difference V is applied across resistances connected in parallel,
the resistances all have that same potential difference V.
In Fig. 27-10a, the applied potential difference V is maintained by the battery. In
Fig. 27-10b, the three parallel resistances have been replaced with an equivalent
resistance Req.
b
i
R eq
(b)
a
i
+
-
i
R3
R1
a
b
 i 1
 i 3
 i 2
+
-
R 2
(a)
i
i
i2 + i3
i2 + i3
Parallel resistors and their
equivalent have the same
potential difference (“par-V”).

783
27-2 MULTILOOP CIRCUITS
Resistances connected in parallel can be replaced with an equivalent resistance
Req that has the same potential difference V and the same total current i as the
actual resistances.
You might remember that Req and all the actual parallel resistances have the
same potential difference V with the nonsense word “par-V.”
To derive an expression for Req in Fig. 27-10b, we first write the current in
each actual resistance in Fig. 27-10a as
where V is the potential difference between a and b. If we apply the junction rule
at point a in Fig. 27-10a and then substitute these values, we find
(27-21)
If we replaced the parallel combination with the equivalent resistance Req
(Fig. 27-10b), we would have
(27-22)
Comparing Eqs. 27-21 and 27-22 leads to
(27-23)
Extending this result to the case of n resistances, we have
(n resistances in parallel).
(27-24)
For the case of two resistances, the equivalent resistance is their product divided
by their sum; that is,
(27-25)
Note that when two or more resistances are connected in parallel,the equivalent
resistance is smaller than any of the combining resistances.Table 27-1 summarizes the
equivalence relations for resistors and capacitors in series and in parallel.
Req !
R1R2
R1 % R2
.
1
Req
! '
n
j!1
1
Rj
1
Req
!
1
R1
%
1
R2
%
1
R3
.
i !
V
Req
.
i ! i1 % i2 % i3 ! V#
1
R1
%
1
R2
%
1
R3$.
i1 ! V
R1
,  i2 ! V
R2
,  and  i3 ! V
R3
,
Table 27-1 Series and Parallel Resistors and Capacitors
Series
Parallel
Series
Parallel
Resistors
Capacitors
Eq. 27-7
Eq. 27-24
Eq. 25-20
Eq. 25-19
Same current through
Same potential difference 
Same charge on all 
Same potential difference 
all resistors
across all resistors
capacitors
across all capacitors
Ceq ! '
n
j!1
Cj
1
Ceq
! '
n
j!1
1
Cj
1
Req
! '
n
j!1
1
Rj
Req ! '
n
j!1
Rj
Checkpoint 4
A battery, with potential V across it, is connected to a combination of two identical re-
sistors and then has current i through it.What are the potential difference across and
the current through either resistor if the resistors are (a) in series and (b) in parallel?

784
CHAPTER 27
CIRCUITS
We can now redraw the circuit as in Fig. 27-11c; note that
the current through R23 must be i1 because charge that
moves through R1 and R4 must also move through R23. For
this simple one-loop circuit, the loop rule (applied clockwise
from point a as in Fig. 27-11d) yields
%# # i1R1 # i1R23 # i1R4 ! 0.
Substituting the given data, we find
12 V # i1(20 0) # i1(12 0) # i1(8.0 0) ! 0,
which gives us
(Answer)
(b) What is the current i2 through R2?
KEY IDEAS
(1) we must now work backward from the equivalent circuit
of Fig. 27-11d, where R23 has replaced R2 and R3. (2) Because
R2 and R3 are in parallel, they both have the same potential
difference across them as R23.
Working backward: We know that the current through R23
is i1 ! 0.30 A. Thus, we can use Eq. 26-8 (R ! V/i) and
Fig. 27-11e to find the potential difference V23 across R23.
Setting R23 ! 12 0 from (a), we write Eq. 26-8 as  
V23 ! i1R23 ! (0.30 A)(12 0) ! 3.6 V.
The potential difference across R2 is thus also 3.6 V 
(Fig. 27-11f), so the current i2 in R2 must be, by Eq. 26-8 and
Fig. 27-11g,
(Answer)
(c) What is the current i3 through R3?
KEY IDEAS
We can answer by using either of two techniques: (1) Apply
Eq. 26-8 as we just did. (2) Use the junction rule, which tells
us that at point b in Fig. 27-11b, the incoming current i1 and
the outgoing currents i2 and i3 are related by
i1 ! i2 % i3.
Calculation: Rearranging this junction-rule result yields
the result displayed in Fig. 27-11g:
i3 ! i1 # i2 ! 0.30 A # 0.18 A
! 0.12 A.
(Answer)
i2 ! V2
R2
! 3.6 V
20 0 ! 0.18 A.
i1 ! 12 V
40 0 ! 0.30 A.
