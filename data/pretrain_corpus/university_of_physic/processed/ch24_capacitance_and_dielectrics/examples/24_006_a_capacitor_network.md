Example 24.6
A capacitor network
Find the equivalent capacitance of the five-capacitor network
shown in Fig. 24.10a.
SOLUTION
IDENTIFY and SET UP: These capacitors are neither all in series
nor all in parallel. We can, however, identify portions of the
arrangement that are either in series or parallel. We combine these
as described in Problem-Solving Strategy 24.1 to find the net
equivalent capacitance, using Eq. (24.5) for series connections and
Eq. (24.7) for parallel connections.
EXECUTE: The caption of Fig. 24.10 outlines our procedure. We
first use Eq. (24.5) to replace the 
and 
series combina-
tion by its equivalent capacitance 
1
C¿ =
1
12 mF +
1
6 mF     C¿ = 4 mF
C¿:
6-mF
12-mF
This gives us the equivalent combination of Fig. 24.10b. Now we
see three capacitors in parallel, and we use Eq. (24.7) to replace
them with their equivalent capacitance 
This gives us the equivalent combination of Fig. 24.10c, which has
two capacitors in series. We use Eq. (24.5) to replace them with
their equivalent capacitance 
, which is our target variable 
(Fig. 24.10d):
EVALUATE: If the potential difference across the entire network in
Fig. 24.10a is 
= 9.0 V, the net charge on the network is
. Can you find the charge
on, and the voltage across, each of the five individual capacitors?
Q = CeqVab = 16 mF219.0 V2 = 54 mC
Vab
1
Ceq
=
1
18 mF +
1
9 mF     Ceq = 6 mF
Ceq
C- = 3 mF + 11 mF + 4 mF = 18 mF
C-:
a
b
(a)
a
b
(b)
a
b
(c)
a
b
(d)
3 mF
3 mF
6 mF
9 mF
9 mF
12 mF
11 mF
11 mF
4 mF
18 mF
9 mF
6 mF
... replace these series
capacitors by an equivalent
capacitor.
... replace these
parallel capacitors by
an equivalent capacitor ...
Replace these series capacitors
by an equivalent capacitor ...
24.10 (a) A capacitor network between points 
and 
(b) The 
and 
capacitors in series in (a) are replaced by an equiva-
lent 
capacitor. (c) The 
and 
capacitors in parallel in (b) are replaced by an equivalent 
capacitor. 
(d) Finally, the 
and 
capacitors in series in (c) are replaced by an equivalent 
capacitor.
6-mF
9-mF
18-mF
18-mF
4-mF
11-mF,
3-mF,
4-mF
6-mF
12-mF
b.
a
Test Your Understanding of Section 24.2
You want to connect a
capacitor and an 
capacitor. (a) With which type of connection will the
capacitor have a greater potential difference across it than the 
capaci-
tor? (i) series; (ii) parallel; (iii) either series or parallel; (iv) neither series nor parallel. 
(b) With which type of connection will the 
capacitor have a greater charge than the
capacitor? (i) series; (ii) parallel; (iii) either series or parallel; (iv) neither series nor
parallel.
❙
8-mF
4-mF
8-mF
4-mF
8-mF
4-mF

24.3 Energy Storage in Capacitors and Electric-Field Energy
797
We can calculate the potential energy 
of a charged capacitor by calculating the
work 
required to charge it. Suppose that when we are done charging the capac-
itor, the final charge is 
and the final potential difference is 
From Eq. (24.1)
these quantities are related by
Let 
and 
be the charge and potential difference, respectively, at an intermedi-
ate stage during the charging process; then 
At this stage the work 
required to transfer an additional element of charge 
is
The total work 
needed to increase the capacitor charge 
from zero to a final
value 
is
(work to charge a capacitor) (24.8)
This is also equal to the total work done by the electric field on the charge when
the capacitor discharges. Then q decreases from an initial value 
to zero as the
elements of charge 
“fall” through potential differences 
that vary from 
down to zero.
If we define the potential energy of an uncharged capacitor to be zero, then 
in Eq. (24.8) is equal to the potential energy 
of the charged capacitor. The final
stored charge is 
so we can express 
(which is equal to 
) as
(potential energy stored 
in a capacitor)
(24.9)
When 
is in coulombs, 
in farads (coulombs per volt), and 
in volts (joules
per coulomb), 
is in joules.
The last form of Eq. (24.9), 
shows that the total work 
required
to charge the capacitor is equal to the total charge 
multiplied by the average
potential difference 
during the charging process.
The expression 
in Eq. (24.9) shows that a charged capacitor is
the electrical analog of a stretched spring with elastic potential energy 
The charge 
is analogous to the elongation 
and the reciprocal of the capacitance,
is analogous to the force constant 
The energy supplied to a capacitor in the
charging process is analogous to the work we do on a spring when we stretch it.
Equations (24.8) and (24.9) tell us that capacitance measures the ability of a
capacitor to store both energy and charge. If a capacitor is charged by connecting
it to a battery or other source that provides a fixed potential difference 
then
increasing the value of 
gives a greater charge 
and a greater amount of
stored energy 
If instead the goal is to transfer a given quantity of
charge 
from one conductor to another, Eq. (24.8) shows that the work 
required is inversely proportional to 
the greater the capacitance, the easier it is
to give a capacitor a fixed amount of charge.
Applications of Capacitors: Energy Storage
Most practical applications of capacitors take advantage of their ability to
store and release energy. In electronic flash units used by photographers, the
energy stored in a capacitor (see Fig. 24.4) is released by depressing the camera’s
shutter button. This provides a conducting path from one capacitor plate to the
other through the flash tube. Once this path is established, the stored energy is rap-
idly converted into a brief but intense flash of light. An extreme example of the
same principle is the Z machine at Sandia National Laboratories in New Mexico,
C;
W
Q
U = 1
2 CV2.
Q = CV
C
V,
k.
1>C,
x,
Q
U = 1
2 kx2.
U = 1
21Q2>C2
1
2 V
Q
W
U = 1
2 QV,
U
V
C
Q
U = Q2
2C = 1
2 CV2 = 1
2 QV
W
U
Q = CV,
U
W
V
v
dq
Q
W =
L
W
0
dW = 1
C L
Q
0
q dq = Q2
2C
Q
q
W
dW = v dq = q dq
C
dq
dW
v = q>C.
v
q
V = Q
C
V.
Q
W
U
?

which is used in experiments in controlled nuclear fusion (Fig. 24.11). A bank of
charged capacitors releases more than a million joules of energy in just a few bil-
lionths of a second. For that brief space of time, the power output of the Z
machine is 
W, or about 80 times the power output of all the electric
power plants on earth combined!
In other applications, the energy is released more slowly. Springs in the sus-
pension of an automobile help smooth out the ride by absorbing the energy from
sudden jolts and releasing that energy gradually; in an analogous way, a capacitor
in an electronic circuit can smooth out unwanted variations in voltage due to
power surges. We’ll discuss these circuits in detail in Chapter 26.
Electric-Field Energy
We can charge a capacitor by moving electrons directly from one plate to another.
This requires doing work against the electric field between the plates. Thus we can
think of the energy as being stored in the field in the region between the plates. To
develop this relationship, let’s find the energy per unit volume in the space
between the plates of a parallel-plate capacitor with plate area 
and separation 
We call this the energy density, denoted by 
From Eq. (24.9) the total stored
potential energy is 
and the volume between the plates is just 
hence the
energy density is
(24.10)
From Eq. (24.2) the capacitance 
is given by 
The potential differ-
ence 
is related to the electric-field magnitude 
by 
If we use these
expressions in Eq. (24.10), the geometric factors 
and cancel, and we find
(electric energy density in a vacuum)
(24.11)
Although we have derived this relationship only for a parallel-plate capacitor, it
turns out to be valid for any capacitor in vacuum and indeed for any electric field
configuration in vacuum. This result has an interesting implication. We think of
vacuum as space with no matter in it, but vacuum can nevertheless have electric
fields and therefore energy. Thus “empty” space need not be truly empty after all.
We will use this idea and Eq. (24.11) in Chapter 32 in connection with the energy
transported by electromagnetic waves.
CAUTION
Electric-field energy is electric potential energy It’s a common misconception
that electric-field energy is a new kind of energy, different from the electric potential
energy described before. This is not the case; it is simply a different way of interpreting
electric potential energy. We can regard the energy of a given system of charges as being a
shared property of all the charges, or we can think of the energy as being a property of the
electric field that the charges create. Either interpretation leads to the same value of the
potential energy. ❙
u = 1
2 P0E2  
d
A
V = Ed.
E
V
C = P0A>d.
C
u = Energy density =
1
2 CV2
Ad
Ad;
1
2 CV2
u.
d.
A
2.9 * 1014
798
CHAPTER 24 Capacitance and Dielectrics
24.11 The Z machine uses a large
number of capacitors in parallel to give a
tremendous equivalent capacitance 
(see
Section 24.2). Hence a large amount of
energy 
can be stored with even
a modest potential difference 
The arcs
shown here are produced when the capaci-
tors discharge their energy into a target,
which is no larger than a spool of thread.
This heats the target to a temperature
higher than 
K.
2 * 109
V.
U = 1
2CV2
C
