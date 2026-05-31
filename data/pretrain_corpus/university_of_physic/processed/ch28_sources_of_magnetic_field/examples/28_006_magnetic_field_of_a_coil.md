Example 28.6
Magnetic field of a coil
A coil consisting of 100 circular loops with radius 0.60 m carries a
5.0-A current. (a) Find the magnetic field at a point along the axis
of the coil, 0.80 m from the center. (b) Along the axis, at what dis-
tance from the center of the coil is the field magnitude as great as
it is at the center?
SOLUTION
IDENTIFY and SET UP: This problem concerns the magnetic field
magnitude B along the axis of a current-carrying coil, so we can
use the ideas of this section, and in particular Eq. (28.16). We are
given 
and 
In part (a) our target
variable is 
at a given value of x. In part (b) the target variable is
the value of x at which the field has of the magnitude that it has at
the origin.
EXECUTE: (a) Using 
from Eq. (28.16) we have
= 1.1 * 10-4 T
Bx =
14p * 10-7 T # m/A21100215.0 A210.60 m22
2310.80 m22 + 10.60 m2243>2
x = 0.80 m,
1
8
Bx
a = 0.60 m.
I = 5.0 A,
N = 100,
1
8
(b) Considering Eq. (28.16), we want to find a value of x such
that
To solve this for x, we take the reciprocal of the whole thing and
then take the 
power of both sides; the result is
EVALUATE: We check our answer in part (a) by finding the coil’s
magnetic moment and substituting the result into Eq. (28.18):
The magnetic moment 
is relatively large, yet it produces a rather
small field, comparable to that of the earth. This illustrates how
difficult it is to produce strong fields of 1 T or more.
m
Bx =
14p * 10-7 T # m>A215.7 * 102 A # m22
2p310.80 m22 + 10.60 m2243>2
= 1.1 * 10-4 T
m = NIpa2 = 1100215.0 A2p10.60 m22 = 5.7 * 102 A # m2
x = 23a = 1.04 m
2>3
1
1x2 + a223>2 = 1
8
1
102 + a223>2
z
x
x
P
y
I
O
B
S
28.15 Magnetic field lines produced by
the current in a circular loop. At points on
the axis the 
field has the same direction
as the magnetic moment of the loop.
B
S
Application Magnetic Fields for MRI
The diagnostic technique called MRI, or mag-
netic resonance imaging (see Section 27.7),
requires a magnetic field of about 1.5 T. In a
typical MRI scan, the patient lies inside a coil
that produces the intense field. The currents
required are very high, so the coils are bathed
in liquid helium at a temperature of 4.2 K to
keep them from overheating.

28.6 Ampere’s Law
935
28.6 Ampere’s Law
So far our calculations of the magnetic field due to a current have involved find-
ing the infinitesimal field 
due to a current element and then summing all the
’s to find the total field. This approach is directly analogous to our electric-
field calculations in Chapter 21.
For the electric-field problem we found that in situations with a highly sym-
metric charge distribution, it was often easier to use Gauss’s law to find 
There
is likewise a law that allows us to more easily find the magnetic fields caused by
highly symmetric current distributions. But the law that allows us to do this,
called Ampere’s law, is rather different in character from Gauss’s law.
Gauss’s law for electric fields involves the flux of 
through a closed surface;
it states that this flux is equal to the total charge enclosed within the surface,
divided by the constant 
Thus this law relates electric fields and charge distri-
butions. By contrast, Gauss’s law for magnetic fields, Eq. (28.10), is not a rela-
tionship between magnetic fields and current distributions; it states that the flux
of 
through any closed surface is always zero, whether or not there are currents
within the surface. So Gauss’s law for 
can’t be used to determine the magnetic
field produced by a particular current distribution.
Ampere’s law is formulated not in terms of magnetic flux, but rather in terms
of the line integral of 
around a closed path, denoted by
We used line integrals to define work in Chapter 6 and to calculate electric poten-
tial in Chapter 23. To evaluate this integral, we divide the path into infinitesimal
segments 
calculate the scalar product of 
for each segment, and sum
these products. In general, 
varies from point to point, and we must use the
value of 
at the location of each 
An alternative notation is 
where 
is the component of 
parallel to 
at each point. The circle on the integral sign
indicates that this integral is always computed for a closed path, one whose
beginning and end points are the same.
Ampere’s Law for a Long, Straight Conductor
To introduce the basic idea of Ampere’s law, let’s consider again the magnetic
field caused by a long, straight conductor carrying a current I. We found in Sec-
tion 28.3 that the field at a distance r from the conductor has magnitude
The magnetic field lines are circles centered on the conductor. Let’s take the
line integral of 
around one such circle with radius r, as in Fig. 28.16a. At
every point on the circle, 
and 
are parallel, and so 
since r is
constant around the circle, B is constant as well. Alternatively, we can say that
is constant and equal to B at every point on the circle. Hence we can take B
BŒ
B
S # dl
S = B dl;
dl
S
B
S
B
S
B = m0I
2pr
dl
S
B
S
BŒ
A BŒ dl,
dl
S.
B
S
B
S
B
S # dl
S
dl
S,
C
B
S # dl
S
B
S
B
S
B
S
P0.
E
S
E
S.
dB
S
dB
S
Test Your Understanding of Section 28.5
Figure 28.12 shows the
magnetic field 
produced at point P by a segment 
that lies on the positive 
y-axis (at the top of the loop). This field has components 
(a) What are the signs of the components of the field 
produced at P by a segment 
on the negative 
(at the bottom of the loop)? (i) 
(ii) 
(iii) 
(iv) 
(v) none of these. (b) What are the signs of the components of the
field 
produced at P by a segment 
on the negative 
(at the right-hand side 
of the loop)? (i) 
(ii) 
(iii) 
(iv) 
(v) none of 
these.
❙
dBx 6 0, dBy 6 0, dBz = 0;
dBx 6 0, dBy 7 0, dBz = 0;
dBx 7 0, dBy 6 0, dBz = 0;
dBy 7 0, dBz = 0;
dBx 7 0,
z-axis
dl
S
dB
S
dBy 6 0, dBz = 0;
dBx 6 0,
dBx 6 0, dBy 7 0, dBz = 0;
dBy 6 0, dBz = 0;
dBx 7 0,
dBx 7 0, dBy 7 0, dBz = 0;
y-axis
dl
S
dB
S
0.
dBx 7 0, dBy 7 0, dBz =
dl
S
dB
S
28.16 Three integration paths for the
line integral of 
in the vicinity of a long,
straight conductor carrying current I out of
the plane of the page (as indicated by the
circle with a dot). The conductor is seen
end-on.
B
S
(a) Integration path is a circle centered on the
conductor; integration goes around the circle
counterclockwise.
Result: rB # dl 5 m0I
S
S
I
r
B
S
B
S
B
S
B
S
dl
S
dl
S
dl
S
dl
S
r
I
B
S
B
S
B
S
B
S
dl
S
dl
S
dl
S
dl
S
(b) Same integration path as in (a), but
integration goes around the circle clockwise.
Result: rB # dl 5 2m0I
S
S
(c) An integration path that does not enclose the
conductor
Result: rB # dl 5 0
r1
r2
d
b
c
a
B
S
B
S
B
S
B
S
dl
S
dl
S
dl
S
dl
S
u
I

outside of the integral. The remaining integral is just the circumference of the
circle, so
The line integral is thus independent of the radius of the circle and is equal to 
multiplied by the current passing through the area bounded by the circle.
In Fig. 28.16b the situation is the same, but the integration path now goes
around the circle in the opposite direction. Now 
and 
are antiparallel, so
and the line integral equals 
We get the same result if the
integration path is the same as in Fig. 28.16a, but the direction of the current is
reversed. Thus 
equals 
multiplied by the current passing through the
area bounded by the integration path, with a positive or negative sign depending
on the direction of the current relative to the direction of integration.
There’s a simple rule for the sign of the current; you won’t be surprised to
learn that it uses your right hand. Curl the fingers of your right hand around the
integration path so that they curl in the direction of integration (that is, the direc-
tion that you use to evaluate 
Then your right thumb indicates the posi-
tive current direction. Currents that pass through the integration path in this
direction are positive; those in the opposite direction are negative. Using this
rule, you should be able to convince yourself that the current is positive in Fig.
28.16a and negative in Fig. 28.16b. Here’s another way to say the same thing:
Looking at the surface bounded by the integration path, integrate counterclock-
wise around the path as in Fig. 28.16a. Currents moving toward you through the
surface are positive, and those going away from you are negative.
An integration path that does not enclose the conductor is used in Fig. 28.16c.
Along the circular arc ab of radius 
and 
are parallel, and 
along the circular arc cd of radius 
and 
are antiparallel and
The 
field is perpendicular to 
at each point on the
straight sections bc and da, so 
and these sections contribute zero to the
line integral. The total line integral is then
The magnitude of 
is greater on arc cd than on arc ab, but the arc length is less,
so the contributions from the two arcs exactly cancel. Even though there is a
magnetic field everywhere along the integration path, the line integral 
is
zero if there is no current passing through the area bounded by the path.
We can also derive these results for more general integration paths, such as the
one in Fig. 28.17a. At the position of the line element 
the angle between 
and 
is 
and
From the figure, 
where 
is the angle subtended by 
at the
position of the conductor and r is the distance of 
from the conductor. Thus
But 
is just equal to 
the total angle swept out by the radial line from the
conductor to 
during a complete trip around the path. So we get
dl
S
2p,
A du
C
B
S # dl
S =
C
m0I
2pr 1r du2 = m0I
2p C
du
dl
S
dl
S
du
dlcosf = r du,
B
S # dl
S = B dlcosf
f,
B
S
dl
S
dl
S,
A B
S # dl
S
B
S
= m0I
2pr1
1r1u2 + 0 - m0I
2pr2
1r2u2 + 0 = 0
C
B
S # dl
S =
C
BŒdl = B1 L
b
a
dl + 102
L
c
b
dl + 1-B22
L
d
c
dl + 102
L
a
d
dl
BŒ = 0
dl
S
B
S
BŒ = -B2 = -m0I>2pr2.
dl
S
B
S
r2,
m0I>2pr1;
BŒ = B1 =
dl
S
B
S
r1,
A B
S # dl
S).
m0
A B
S # dl
S
-m0I.
B
S # dl
S = -B dl
dl
S
B
S
m0
C
B
S # dl
S =
C
BŒ dl = B
C
dl = m0I
2pr 12pr2 = m0I
936
CHAPTER 28 Sources of Magnetic Field
r du
du
I
r
(a)
B
S
dl
S
f
r du
du
I
r
(b)
B
S
dl
S
28.17 (a) A more general integration
path for the line integral of 
around a long,
straight conductor carrying current I out of
the plane of the page. The conductor is seen
end-on. (b) A more general integration path
that does not enclose the conductor.
B
S

28.6 Ampere’s Law
937
(28.19)
This result doesn’t depend on the shape of the path or on the position of the wire
inside it. If the current in the wire is opposite to that shown, the integral has the
opposite sign. But if the path doesn’t enclose the wire (Fig. 28.17b), then the net
change in 
during the trip around the integration path is zero; 
is zero
instead of 
and the line integral is zero.
Ampere’s Law: General Statement
Equation (28.19) is almost, but not quite, the general statement of Ampere’s law.
To generalize it even further, suppose several long, straight conductors pass
through the surface bounded by the integration path. The total magnetic field 
at
any point on the path is the vector sum of the fields produced by the individual
conductors. Thus the line integral of the total 
equals 
times the algebraic
sum of the currents. In calculating this sum, we use the sign rule for currents
described above. If the integration path does not enclose a particular wire, the
line integral of the 
field of that wire is zero, because the angle 
for that wire
sweeps through a net change of zero rather than 
during the integration. Any
conductors present that are not enclosed by a particular path may still contribute
to the value of 
at every point, but the line integrals of their fields around the
path are zero.
Thus we can replace I in Eq. (28.19) with 
the algebraic sum of the cur-
rents enclosed or linked by the integration path, with the sum evaluated by
using the sign rule just described (Fig. 28.18). Our statement of Ampere’s law
is then
(Ampere’s law)
(28.20)
While we have derived Ampere’s law only for the special case of the field of sev-
eral long, straight, parallel conductors, Eq. (28.20) is in fact valid for conductors
and paths of any shape. The general derivation is no different in principle from
what we have presented, but the geometry is more complicated.
If 
it does not necessarily mean that 
everywhere along
the path, only that the total current through an area bounded by the path is zero. In
Figs. 28.16c and 28.17b, the integration paths enclose no current at all; in Fig. 28.19
there are positive and negative currents of equal magnitude through the area
enclosed by the path. In both cases, 
and the line integral is zero.
CAUTION
Line integrals of electric and magnetic fields In Chapter 23 we saw that the
line integral of the electrostatic field 
around any closed path is equal to zero; this is a
statement that the electrostatic force 
on a point charge q is conservative, so this
force does zero work on a charge that moves around a closed path that returns to the start-
ing point. You might think that the value of the line integral 
is similarly related to
the question of whether the magnetic force is conservative. This isn’t the case at all.
Remember that the magnetic force 
on a moving charged particle is always
perpendicular to 
so 
is not related to the work done by the magnetic force; as
stated in Ampere’s law, this integral is related only to the total current through a surface
bounded by the integration path. In fact, the magnetic force on a moving charged particle
is not conservative. A conservative force depends only on the position of the body on
which the force is exerted, but the magnetic force on a moving charged particle also
depends on the velocity of the particle. ❙
Equation (28.20) turns out to be valid only if the currents are steady and if no
magnetic materials or time-varying electric fields are present. In Chapter 29 we
will see how to generalize Ampere’s law for time-varying fields.
A B
S # dl
S
B
S,
F
S  qv
S : B
S
A B
S # dl
S
F
S  qE
S
E
S
Iencl = 0
B
S  0
AB
S # dl
S = 0,
C
B
S # dl
S = m0Iencl
Iencl,
B
S
2p
u
B
S
m0
B
S
B
S
2p
A du
u
C
B
S # dl
S = m0I
Perspective view
Top view
Plane of
curve
B
S
Iencl 5 I1 2 I2 1 I3
B
S
Ampere’s law:  If we calculate the line integral 
of the magnetic field around a closed curve, the
result equals m0 times the total enclosed current:
rB # dl 5 m0 Iencl.
S
S
Arbitrary closed
curve around
conductors
Curl the fingers of
your right hand around
the integration path:
Your thumb points
in the direction of 
positive current.
I2
I1
I3
I2
I1
I3
dl
S
dl
S
28.18 Ampere’s law.
I
I
B
S
B
S
B
S
B
S
B
S
B
S
B
S
B
S
B
S
B
S
dl
S
dl
S
dl
S
dl
S
dl
S
dl
S
dl
S
dl
S
dl
S
dl
S
28.19 Two long, straight conductors
carrying equal currents in opposite direc-
tions. The conductors are seen end-on, and
the integration path is counterclockwise.
The line integral 
gets zero contri-
bution from the upper and lower segments,
a positive contribution from the left seg-
ment, and a negative contribution from the
right segment; the net integral is zero.
A B
S # dl
S

28.7 Applications of Ampere’s Law
Ampere’s law is useful when we can exploit the symmetry of a situation to eval-
uate the line integral of 
Several examples are given below. Problem-Solving
Strategy 28.2 is directly analogous to Problem-Solving Strategy 22.1 (Section
22.4) for applications of Gauss’s law; we suggest you review that strategy now
and compare the two methods.
B
S.
938
CHAPTER 28 Sources of Magnetic Field
Test Your Understanding of Section 28.6
The figure at left shows magnetic
field lines through the center of a permanent magnet. The magnet is not connected to a
source of emf. One of the field lines is colored red. What can you conclude about the cur-
rents inside the permanent magnet within the region enclosed by this field line? (i) There
are no currents inside the magnet; (ii) there are currents directed out of the plane of the
page; (iii) there are currents directed into the plane of the page; (iv) not enough informa-
tion is given to decide.
❙
S
N
B
S
Problem-Solving Strategy 28.2
Ampere’s Law
IDENTIFY the relevant concepts: Like Gauss’s law, Ampere’s law
is most useful when the magnetic field is highly symmetric. In the
form 
it can yield the magnitude of 
as a func-
tion of position if we are given the magnitude and direction of the
field-generating electric current.
SET UP the problem using the following steps:
1. Determine the target variable(s). Usually one will be the mag-
nitude of the 
field as a function of position.
2. Select the integration path you will use with Ampere’s law. If
you want to determine the magnetic field at a certain point, then
the path must pass through that point. The integration path
doesn’t have to be any actual physical boundary. Usually it is a
purely geometric curve; it may be in empty space, embedded in
a solid body, or some of each. The integration path has to have
enough symmetry to make evaluation of the integral possible.
Ideally the path will be tangent to 
in regions of interest; else-
where the path should be perpendicular to 
or should run
through regions in which 
EXECUTE the solution as follows:
1. Carry out the integral 
along the chosen path. If 
is
tangent to all or some portion of the path and has the same
B
S
AB
S # dl
S
B
S = 0.
B
S
B
S
B
S
B
S
m0Iencl,
AB
S # dl
S =
magnitude B at every point, then its line integral is the product
of B and the length of that portion of the path. If 
is perpendi-
cular to some portion of the path, or if 
that portion
makes no contribution to the integral.
2. In the integral 
is the total magnetic field at each
point on the path; it can be caused by currents enclosed or not
enclosed by the path. If no net current is enclosed by the path,
the field at points on the path need not be zero, but the integral
is always zero.
3. Determine the current 
enclosed by the integration path. A
right-hand rule gives the sign of this current: If you curl the fin-
gers of your right hand so that they follow the path in the direc-
tion of integration, then your right thumb points in the direction
of positive current. If 
is tangent to the path everywhere and
is positive, the direction of 
is the same as the direction of
integration. If instead 
is negative, 
is in the direction
opposite to that of the integration.
4. Use Ampere’s law 
to solve for the target variable.
EVALUATE your answer: If your result is an expression for the field
magnitude as a function of position, check it by examining how the
expression behaves in different limits.
AB
S # dl
S = m0I
B
S
Iencl
B
S
Iencl
B
S
Iencl
AB
S # dl
S
B
S
AB
S # dl
S,
B
S = 0,
B
S
