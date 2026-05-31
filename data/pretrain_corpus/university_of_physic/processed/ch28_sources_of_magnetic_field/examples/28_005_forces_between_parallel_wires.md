Example 28.5
Forces between parallel wires
Two straight, parallel, superconducting wires 4.5 mm apart carry
equal currents of 15,000 A in opposite directions. What force, per
unit length, does each wire exert on the other?
SOLUTION
IDENTIFY and SET UP: Figure 28.10 shows the situation. We find
F L, the magnetic force per unit length of wire, using Eq. (28.11).
>
EXECUTE: The conductors repel each other because the currents are
in opposite directions. From Eq. (28.11) the force per unit length is
EVALUATE: This is a large force, more than one ton per meter. Cur-
rents and separations of this magnitude are used in superconduct-
ing electromagnets in particle accelerators, and mechanical stress
analysis is a crucial part of the design process.
= 1.0 * 104 N>m
F
L = m0II¿
2pr =
14p * 10-7 T # m>A2115,000 A22
12p214.5 * 10-3 m2
28.10 Our sketch for this problem.
Test Your Understanding of Section 28.4
A solenoid is a wire wound
into a helical coil. The figure at left shows a solenoid that carries a current I.
(a) Is the magnetic force that one turn of the coil exerts on an adjacent turn (i)
attractive, (ii) repulsive, or (iii) zero? (b) Is the electric force that one turn of the coil
exerts on an adjacent turn (i) attractive, (ii) repulsive, or (iii) zero? (c) Is the magnetic
force between opposite sides of the same turn of the coil (i) attractive, (ii) repulsive, or
(iii) zero? (d) Is the electric force between opposite sides of the same turn of the 
coil (i) attractive, (ii) repulsive, or (iii) zero?
❙
I
28.5 Magnetic Field of a Circular Current Loop
If you look inside a doorbell, a transformer, an electric motor, or an electromag-
net (Fig. 28.11), you will find coils of wire with a large number of turns, spaced
so closely that each turn is very nearly a planar circular loop. A current in such a
coil is used to establish a magnetic field. So it is worthwhile to derive an expres-
sion for the magnetic field produced by a single circular conducting loop carrying
a current or by N closely spaced circular loops forming a coil. In Section 27.7 we
considered the force and torque on such a current loop placed in an external mag-
netic field produced by other currents; we are now about to find the magnetic
field produced by the loop itself.
Figure 28.12 shows a circular conductor with radius a. A current I is led into
and out of the loop through two long, straight wires side by side; the currents in
these straight wires are in opposite directions, and their magnetic fields very
nearly cancel each other (see Example 28.4 in Section 28.3).
28.11 This electromagnet contains a
current-carrying coil with numerous turns
of wire. The resulting magnetic field can
pick up large quantities of steel bars and
other iron-bearing items.

28.5 Magnetic Field of a Circular Current Loop
933
We can use the law of Biot and Savart, Eq. (28.5) or (28.6), to find the mag-
netic field at a point P on the axis of the loop, at a distance x from the center. As
the figure shows, 
and 
are perpendicular, and the direction of the field 
caused by this particular element 
lies in the xy-plane. Since 
the magnitude dB of the field due to element 
is
(28.12)
The components of the vector 
are
(28.13)
(28.14)
The total field 
at P has only an x-component (it is perpendicular to the plane
of the loop). Here’s why: For every element 
there is a corresponding element
on the opposite side of the loop, with opposite direction. These two elements give
equal contributions to the x-component of 
given by Eq. (28.13), but opposite
components perpendicular to the x-axis. Thus all the perpendicular components
cancel and only the x-components survive.
To obtain the x-component of the total field 
we integrate Eq. (28.13),
including all the 
’s around the loop. Everything in this expression except dl is
constant and can be taken outside the integral, and we have
The integral of dl is just the circumference of the circle, 
and we
finally get
(on the axis of a circular loop)
(28.15)
The direction of the magnetic field on the axis of a current-carrying loop is
given by a right-hand rule. If you curl the fingers of your right hand around the
loop in the direction of the current, your right thumb points in the direction of the
field (Fig. 28.13).
Magnetic Field on the Axis of a Coil
Now suppose that instead of the single loop in Fig. 28.12 we have a coil consist-
ing of N loops, all with the same radius. The loops are closely spaced so that the
plane of each loop is essentially the same distance x from the field point P. Then
the total field is N times the field of a single loop:
(on the axis of N circular loops)
(28.16)
The factor N in Eq. (28.16) is the reason coils of wire, not single loops, are used
to produce strong magnetic fields; for a desired field strength, using a single loop
might require a current I so great as to exceed the rating of the loop’s wire.
Figure 28.14 shows a graph of 
as a function of x. The maximum value of
the field is at 
the center of the loop or coil:
(at the center of N circular loops)
(28.17)
As we go out along the axis, the field decreases in magnitude.
Bx = m0NI
2a
x = 0,
Bx
Bx =
m0NIa2
21x2 + a223>2
Bx =
m0Ia2
21x2 + a223>2
1 dl = 2pa,
Bx =
L
m0I
4p
a dl
1x2 + a223>2 =
m0Ia
4p1x2 + a223>2 L
dl
dl
S
B
S,
dB
S,
dl
S
B
S
dBy = dBsinu = m0I
4p
dl
1x2 + a22
x
1x2 + a221>2
dBx = dBcosu = m0I
4p
dl
1x2 + a22
a
1x2 + a221>2
dB
S
dB = m0I
4p
dl
1x2 + a22
dl
S
r 2 = x2 + a2,
dl
S
dB
S
rN
dl
S
y
O
x
dBy
dBx
I
a
P
x
r
u
u
p
2 2 u
p
2 2 u
dB
S
dl
S
r^
S
z
I
I
28.12 Magnetic field on the axis of a
circular loop. The current in the segment
causes the field 
which lies in the
xy-plane. The currents in other 
’s cause
’s with different components perpendi-
cular to the x-axis; these components add
to zero. The x-components of the 
’s
combine to give the total 
field at point P.
B
S
dB
S
dB
S
dl
S
dB
S,
dl
S
I
I
I
I
Right-hand rule for the
magnetic field produced by
a current in a loop:
When the fingers of your right
hand curl in the direction of I,
your right thumb points in the 
direction of B.
B
S
S
S
B
28.13 The right-hand rule for the
direction of the magnetic field produced 
on the axis of a current-carrying coil.
O
a
2a
x
3a
a
2a
3a
1
2
Bx
Bmax 5
Bmax
m0NI
2a
28.14 Graph of the magnetic field along
the axis of a circular coil with N turns. When
x is much larger than a, the field magnitude
decreases approximately as 1/x3.
PhET: Faraday’s Electromagnetic Lab
PhET: Magnets and Electromagnets
ActivPhysics 13.2: Magnetic Field of a Loop

In Section 27.7 we defined the magnetic dipole moment
(or magnetic
moment) of a current-carrying loop to be equal to IA, where A is the cross-
sectional area of the loop. If there are N loops, the total magnetic moment is
NIA. The circular loop in Fig. 28.12 has area 
so the magnetic
moment of a single loop is 
for N loops, 
Substituting
these results into Eqs. (28.15) and (28.16), we find that both of these expres-
sions can be written as
(28.18)
We described a magnetic dipole in Section 27.7 in terms of its response to a mag-
netic field produced by currents outside the dipole. But a magnetic dipole is also
a source of magnetic field; Eq. (28.18) describes the magnetic field produced by a
magnetic dipole for points along the dipole axis. This field is directly propor-
tional to the magnetic dipole moment 
Note that the field along the x-axis is in
the same direction as the vector magnetic moment 
this is true on both the pos-
itive and negative x-axis.
CAUTION
Magnetic field of a coil Equations (28.15), (28.16), and (28.18) are valid only
on the axis of a loop or coil. Don’t attempt to apply these equations at other points! ❙
Figure 28.15 shows some of the magnetic field lines surrounding a circular
current loop (magnetic dipole) in planes through the axis. The directions of the
field lines are given by the same right-hand rule as for a long, straight conductor.
Grab the conductor with your right hand, with your thumb in the direction of the
current; your fingers curl around in the same direction as the field lines. The field
lines for the circular current loop are closed curves that encircle the conductor;
they are not circles, however.
M
S;
m.
(on the axis of any number
of circular loops)
Bx =
m0m
2p1x2 + a223>2
m = NIpa2.
m = Ipa2;
A = pa2,
m
934
CHAPTER 28 Sources of Magnetic Field
