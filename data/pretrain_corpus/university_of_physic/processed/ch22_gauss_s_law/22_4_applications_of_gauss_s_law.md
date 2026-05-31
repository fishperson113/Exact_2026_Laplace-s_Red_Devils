736

CHAPTER 22 Gauss’s Law

B

surface

A
surface

Fig. 22.15, surface
(shown in red) encloses the positive charge, so
Qencl = + q;
(in  blue)  encloses  the  negative  charge,
Qencl = - q;
so
(in  purple)  encloses  both charges,
C
Qencl = + q + 1-q2 = 0;
so
(in yellow) encloses no
and surface
Qencl = 0.
Hence, without having to do any integration,
charges, so
£ED = 0.
£EA =
£EB = - q>P0,
we  have
and
These  results  depend  only  on  the  charges  enclosed  within  each
Gaussian surface, not on the precise shapes of the surfaces.

£EC =

+q>P0,

D

We can draw similar conclusions by examining the electric ﬁeld
lines. All the ﬁeld lines that cross surface A are directed out of the
surface, so the ﬂux through A must be positive. Similarly, the ﬂux
through B must be negative since all of the ﬁeld lines that cross that
surface point inward. For both surface C and surface D, there are as
many  ﬁeld  lines  pointing  into  the  surface  as  there  are  ﬁeld  lines
pointing outward, so the ﬂux through each of these surfaces is zero.

22.15 The net number of ﬁeld lines leaving a closed surface is
proportional to the total charge enclosed by that surface.

2q

B

1q

C

D

A

S
E

22.16 Five Gaussian surfaces and six
point charges.

S2

S1

15.0 mC

and
—each enclose part of this plane, and Fig. 22.16 shows the intersection of each

Test Your Understanding of Section 22.3 Figure 22.16 shows six point
charges that all lie in the same plane. Five Gaussian surfaces—
S5
surface with the plane. Rank these ﬁve surfaces in order of the electric ﬂux
through them, from most positive to most negative.

S1, S2, S3, S4,

S4

27.0 mC

18.0 mC

19.0 mC

S3

S5

11.0 mC
210.0 mC

❙

22.4 Applications of Gauss’s Law

Gauss’s law is valid for any distribution of charges and for any closed surface.
Gauss’s law can be used in two ways. If we know the charge distribution, and if it
has enough symmetry to let us evaluate the integral in Gauss’s law, we can ﬁnd
the ﬁeld. Or if we know the ﬁeld, we can use Gauss’s law to ﬁnd the charge dis-
tribution, such as charges on conducting surfaces.

In  this  section  we  present  examples  of  both  kinds  of  applications.  As  you
study them, watch for the role played by the symmetry properties of each system.
We will use Gauss’s law to calculate the electric ﬁelds caused by several simple
charge distributions; the results are collected in a table in the chapter summary.

22.17 Under electrostatic conditions
(charges not in motion), any excess charge
on a solid conductor resides entirely on the
conductor’s surface.

Gaussian surface A
inside conductor
(shown in
cross section)

Conductor
(shown in
cross section)

Charge on surface
of conductor

S
E

In practical problems we often encounter situations in which we want to know
the electric ﬁeld caused by a charge distribution on a conductor. These calcula-
tions are aided by the following remarkable fact: When excess charge is placed
on a solid conductor and is at rest, it resides entirely on the surface, not in the
interior of the material. (By excess we mean charges other than the ions and free
electrons that make up the neutral conductor.) Here’s the proof. We know from
Section 21.4 that in an electrostatic situation (with all charges at rest) the electric
ﬁeld
at every point in the interior of a conducting material is zero. If  were
not zero, the excess charges would move. Suppose we construct a Gaussian sur-
face inside the conductor, such as surface
every-
where on this surface, Gauss’s law requires that the net charge inside the surface
is  zero.  Now  imagine  shrinking  the  surface  like  a  collapsing  balloon  until  it
encloses a region so small that we may consider it as a point
then the charge at
that point must be zero. We can do this anywhere inside the conductor, so there
can be no excess charge at any point within a solid conductor; any excess charge
must reside on the conductor’s surface. (This result is for a solid conductor. In the
next  section  we’ll  discuss  what  can  happen  if  the  conductor  has  cavities  in  its
interior.) We will make use of this fact frequently in the examples that follow.

in Fig. 22.17. Because

(cid:2) 0

S
E

S
E

P;

A

Problem-Solving Strategy 22.1

Gauss’s Law

22.4 Applications of Gauss’s Law

737

IDENTIFY the relevant concepts: Gauss’s law is most useful when
the charge distribution has spherical, cylindrical, or planar symme-
try. In these cases the symmetry determines the direction of
. Then
if we are given the charge
Gauss’s law yields the magnitude of
distribution,  and  vice  versa.  In  either  case,  begin  the  analysis  by
asking the question: What is the symmetry?

S
E

S
E

SET UP the problem using the following steps:
1. List the known and unknown quantities and identify the target

variable.

2. Select the appropriate closed, imaginary Gaussian surface. For
spherical  symmetry,  use  a  concentric  spherical  surface.  For
cylindrical symmetry, use a coaxial cylindrical surface with ﬂat
ends perpendicular to the axis of symmetry (like a soup can).
For planar symmetry, use a cylindrical surface (like a tuna can)
with its ﬂat ends parallel to the plane.

EXECUTE the solution as follows:
1. Determine the appropriate size and placement of your Gaussian
surface.  To  evaluate  the  ﬁeld  magnitude  at  a  particular  point,
the surface must include that point. It may help to place one end
of a can-shaped surface within a conductor, where
and there-
£
are zero, or to place its ends equidistant from a charged
fore
plane.

S
E

2. Evaluate the integral

AE(cid:2) dA

in Eq. (22.9). In this equation

E(cid:2)
is the perpendicular component of the total electric ﬁeld at each
point on the Gaussian surface. A well-chosen Gaussian surface
should  make  integration  trivial  or  unnecessary.  If  the  surface
comprises several separate surfaces, such as the sides and ends

Example 22.5

Field of a charged conducting sphere

We  place  a  total  positive  charge
S
E
with radius
sphere.

(Fig. 22.18). Find

R

on  a  solid  conducting  sphere
q
at any point inside or outside the

22.18 Calculating the electric ﬁeld of a conducting sphere with
positive charge q. Outside the sphere, the ﬁeld is the same as if all
of the charge were concentrated at the center of the sphere.

+
+
+

+

+ +

R

+

+ +
E

+

+

E1R2 5

1
4pP
0

q
R2

Inside the sphere, the
electric field is zero:
E 5 0.
E1R2/4
E1R2/9
O

Gaussian surfaces
at r 5 2R and r 5 3R

Outside the sphere, the magnitude
of the electric field decreases with
the square of the radial distance
from the center of the sphere:
E 5

1
4pP
0

q
r 2

R

2R

3R

r

3. If

of  a  cylinder,  the  integral
face is the sum of the integrals
1E(cid:2) dA
faces. Consider points 3–6 as you work.

AE(cid:2) dA

over  the  entire  closed  sur-
over the separate sur-

S
E

(If

and
is inward, then

S
is perpendicular (normal) at every point to a surface with
E
area
if it points outward from the interior of the surface, and
A,
if it has the same magnitude at every point on the surface, then
E(cid:2) = E = constant,
over that surface is equal to
1E(cid:2) dA
E(cid:2) = - E
1E(cid:2) dA = - EA.
) This
and
EA.
S
should be the case for part or all of your Gaussian surface. If
E
and the inte-
is tangent to a surface at every point, then
gral over that surface is zero. This may be the case for parts of a
cylindrical Gaussian surface. If
at every point on a sur-
face, the integral is zero.

E(cid:2) = 0

(cid:2) 0

S
E

4. Even  when  there  is  no charge  within  a  Gaussian  surface,  the
ﬁeld at any given point on the surface is not necessarily zero. In
that case, however, the total electric ﬂux through the surface is
always zero.
5. The  ﬂux  integral

can  be  approximated  as  the  differ-
ence between the numbers of electric lines of force leaving and
entering the Gaussian surface. In this sense the ﬂux gives the
sign of the enclosed charge, but is only proportional to it; zero
ﬂux corresponds to zero enclosed charge.

AE(cid:2) dA

6. Once you have evaluated

AE(cid:2) dA,

use Eq. (22.9) to solve for

your target variable.

EVALUATE  your answer: If your result is a function that describes
how the magnitude of the electric ﬁeld varies with position, ensure
that it makes sense.

SOLUTION

IDENTIFY and SET UP: As we discussed earlier in this section, all
of the charge must be on the surface of the sphere. The charge is
free to move on the conductor, and there is no preferred position
on  the  surface;  the  charge  is  therefore  distributed  uniformly over
the  surface,  and  the  system  is  spherically  symmetric.  To  exploit
this symmetry, we take as our Gaussian surface a sphere of radius
r
centered on the conductor. We can calculate the ﬁeld inside or out-
,  respectively.  In
side  the  conductor  by  taking
either case, the point at which we want to calculate
lies on the
Gaussian surface.

r 6 R

r 7 R

or

S
E

EXECUTE: The spherical symmetry means that the direction of the
electric  ﬁeld  must  be  radial;  that’s  because  there  is  no  preferred
direction parallel to the surface, so
can have no component par-
allel  to  the  surface.  There  is  also  no  preferred  orientation  of  the
sphere, so the ﬁeld magnitude
can depend only on the distance
r
from the center and must have the same value at all points on the
Gaussian surface.

S
E

E

r 7 R

For

the entire conductor is within the Gaussian surface,
The  area  of  the  Gaussian  surface  is
is uniform over the surface and perpendicular to it at
and

is  then  just

E14pr 22,

AE(cid:2) dA

q.

S
E

, and

so  the  enclosed  charge  is
4pr 2
each  point.  The  ﬂux  integral
Eq. (22.8) gives

Continued

738

CHAPTER 22 Gauss’s Law

E14pr 22 =

E =

  and

q
P0
1
4pP0

q
r 2

(outside a charged
conducting sphere)

This expression is the same as that for a point charge; outside the
charged  sphere,  its  ﬁeld  is  the  same  as  though  the  entire  charge
were  concentrated  at  its  center.  Just  outside  the  surface  of  the
sphere, where

(at the surface of a charged conducting sphere)

r = R,
q
R2

E =

1
4pP0

q

CAUTION Flux  can  be  positive  or  negative Remember  that  we
have chosen the charge
to be positive. If the charge is negative,
the electric ﬁeld is radially inward instead of radially outward, and
the  electric  ﬂux  through  the  Gaussian  surface  is  negative.  The
electric-ﬁeld  magnitudes  outside  and  at  the  surface  of  the  sphere
are given by the same expressions as above, except that  denotes
the magnitude (absolute value) of the charge. ❙

q

For

r 6 R

But  now  our
Gaussian  surface  (which  lies  entirely  within  the  conductor)

we  again  have

E14pr 22 = Qencl>P0.

Example 22.6

Field of a uniform line charge

Electric  charge  is  distributed  uniformly  along  an  inﬁnitely  long,
thin wire. The charge per unit length is
(assumed positive). Find
the electric ﬁeld using Gauss’s law.

l

SOLUTION

l

S
E

is positive and radially inward if

IDENTIFY and SET UP: We found in Example 21.10 (Section 21.5)
that the ﬁeld  of a uniformly charged, inﬁnite wire is radially out-
ward if
is negative, and that
the ﬁeld magnitude E depends only on the radial distance from the
wire. This suggests that we use a cylindrical Gaussian surface, of
coaxial with the wire and with its
radius  and arbitrary length
ends perpendicular to the wire (Fig. 22.19).

l

l,

r

EXECUTE: The ﬂux through the ﬂat ends of our Gaussian surface is
zero because the radial electric ﬁeld is parallel to these ends, and
S # nN = 0.
On  the  cylindrical  part  of  our  surface  we  have
so
E
S # nN = E(cid:2) = E
E
everywhere. (If  were negative, we would have

l

22.19 A coaxial cylindrical Gaussian surface is used to ﬁnd the
electric ﬁeld outside an inﬁnitely long, charged wire.

E' 5 E
S
dA

Gaussian
surface

E' 5 0

r

l

encloses no charge, so
ductor is therefore zero.

Qencl = 0

. The electric ﬁeld inside the con-

S
E

(cid:2) 0

E

as  a  function  of  the  distance

EVALUATE:  We already knew that
inside a solid conductor
(whether spherical or not) when the charges are at rest. Figure 22.18
from  the  center  of  the
shows
sphere. Note that in the limit as
the sphere becomes a point
charge; there is then only an “outside,” and the ﬁeld is everywhere
given  by
Thus  we  have  deduced  Coulomb’s  law
from Gauss’s law. (In Section 22.3 we deduced Gauss’s law from
Coulomb’s law; the two laws are equivalent.)

E = q>4pP0r 2.

R S 0,

r

We can also use this method for a conducting spherical shell (a
spherical  conductor  with  a  concentric  spherical  hole  inside)  if
there is no charge inside the hole. We use a spherical Gaussian sur-
face with radius
less than the radius of the hole. If there were a
ﬁeld  inside  the  hole,  it  would  have  to  be  radial  and  spherically
But  now  there  is  no
symmetric  as  before,  so
enclosed charge, so

E = Qencl>4pP0r 2.

inside the hole.

E = 0

and

Qencl = 0

r

Can you use this same technique to ﬁnd the electric ﬁeld in the
region between a charged sphere and a concentric hollow conduct-
ing sphere that surrounds it?

S # nN = E(cid:2) = - E
E
2prl,
is
the Gaussian surface—is EA
is

Qencl = ll,

so the ﬂux through it—and hence the total ﬂux

everywhere.) The area of the cylindrical surface
through
The total enclosed charge

= 2prlE.

£E

and so from Gauss’s law, Eq. (22.8),

£E = 2prlE =

E =

1
2pP0

l

r

  and

ll
P0
    (field of an infinite line of charge)

We  found  this  same  result  in  Example  21.10  with  much more
effort.
l
If

is directed radially inward, and in the above
as the absolute value of the

is negative,

S
E

l

expression for  we must interpret
charge per unit length.

E

Qencl = ll

EVALUATE: We saw in Example 21.10 that the entire charge on the
wire contributes to the ﬁeld at any point, and yet we consider only
that  part  of  the  charge
within  the  Gaussian  surface
when we apply Gauss’s law. There’s nothing inconsistent here; it
takes the entire charge to give the ﬁeld the properties that allow us
so  easily,  and  Gauss’s  law  always  applies  to  the
to  calculate
enclosed charge only. If the wire is short, the symmetry of the inﬁ-
nite wire is lost, and E is not uniform over a coaxial, cylindrical
Gaussian surface. Gauss’s law then cannot be used to ﬁnd
; we
must solve the problem the hard way, as in Example 21.10.

£E

£E

We can use the Gaussian surface in Fig. 22.19 to show that the
ﬁeld  outside  a  long,  uniformly  charged  cylinder  is  the  same  as
though  all  the  charge  were  concentrated  on  a  line  along  its  axis
(see Problem 22.42). We can also calculate the electric ﬁeld in the
space between a charged cylinder and a coaxial hollow conducting
cylinder surrounding it (see Problem 22.39).

Example 22.7

Field of an infinite plane sheet of charge

22.4 Applications of Gauss’s Law

739

Use Gauss’s law to ﬁnd the electric ﬁeld caused by a thin, ﬂat, inﬁ-
nite sheet with a uniform positive surface charge density

s.

SOLUTION

S
E

IDENTIFY and SET UP: In Example 21.11 (Section 21.5) we found
that the ﬁeld  of a uniformly charged inﬁnite sheet is normal to the
sheet, and that its magnitude is independent of the distance from the
sheet. To  take  advantage  of  these  symmetry  properties,  we  use  a
cylindrical Gaussian surface with ends of area A and with its axis
perpendicular to the sheet of charge (Fig. 22.20).

22.20 A cylindrical Gaussian surface is used to ﬁnd the ﬁeld of
an inﬁnite plane sheet of charge.

EXECUTE: The  ﬂux  through  the  cylindrical  part  of  our  Gaussian
S # nN = 0
everywhere.  The  ﬂux  through
surface  is  zero  because
E
S # nN = E(cid:2) = E
+EA
each  ﬂat  end  of  the  surface  is
E
everywhere,  so  the  total  ﬂux  through  both  ends—and  hence  the
total  ﬂux
The  total
enclosed charge is

+2EA.
and so from Gauss’s law,

through  the  Gaussian  surface—is

because

£E

Qencl = sA,
  and
    (field of an infinite sheet of charge)

2EA =

E =

sA
P0
s
2P0

s

If

In  Example  21.11  we  found  this  same  result  using  a  much  more
complex calculation.
S
is negative,
E

is directed toward the sheet, the ﬂux through
in the expres-
denotes  the  magnitude  (absolute  value)  of  the

the Gaussian surface in Fig. 22.20 is negative, and
sion
charge density.

E = s>2P0

s

E

Gaussian
surface

EVALUATE:  Again we see that, given favorable symmetry, we can
deduce  electric  ﬁelds  using  Gauss’s  law  much  more  easily  than
using Coulomb’s law.

E' 5 E

+ +

+ + + + +
+ + +
+ + + + +
+ + + + +
+ + + + +
+ + + + +

A

Example 22.8

Field between oppositely charged parallel conducting plates

Two  large  plane  parallel  conducting  plates  are  given  charges  of
equal magnitude and opposite sign; the surface charge densities are
+s
Find the electric ﬁeld in the region between the plates.

-s.

and

SOLUTION

IDENTIFY  and SET  UP:  Figure  22.21a  shows  the  ﬁeld.  Because
opposite charges attract, most of the charge accumulates at the oppos-
ing faces of the plates. A small amount of charge resides on the outer
surfaces of the plates, and there is some spreading or “fringing” of

22.21 Electric ﬁeld between oppositely charged parallel plates.

the ﬁeld at the edges. But if the plates are very large in comparison
to the distance between them, the amount of charge on the outer
surfaces  is  negligibly  small,  and  the  fringing  can  be  neglected
except near the edges. In this case we can assume that the ﬁeld is
uniform in the interior region between the plates, as in Fig. 22.21b,
and  that  the  charges  are  distributed  uniformly  over  the  opposing
surfaces. To exploit this symmetry, we can use the shaded Gauss-
ian  surfaces
These  surfaces  are  cylinders  with
S1,
ﬂat ends of area

S2, S3,
; one end of each surface lies within a plate.
A

and

S4.

(a) Realistic drawing

(b) Idealized model

1

Between the two
plates the electric field
is nearly uniform,
pointing from the
positive plate toward
the negative one.

S
E

++
+
+ +
+
+ +
+
+ +
+
+ +
+
+ +
+
++

–

––
–
––
–
–
–
–
–
–
–
–
–
– –

–

–

–

S
E1

S
E2

a

In the idealized case
we ignore “fringing”
at the plate edges and
treat the field between
the plates as uniform.

Cylindrical Gaussian
surfaces (seen from
the side)

S2

b

S1

+

+

+
+

+

+

+

+

+
+

+
+

+

r
E2

r
E1

c

S
E1
S
E2

S
E

S4

2

–

–

–

–

–

–

–

–

–

–
–

–

–

S3

Continued

740

CHAPTER 22 Gauss’s Law

S1

EXECUTE: The  left-hand  end  of  surface
is  within  the  positive
plate 1. Since the ﬁeld is zero within the volume of any solid con-
ductor  under  electrostatic  conditions,  there  is  no  electric  ﬂux
through this end. The electric ﬁeld between the plates is perpendi-
cular to the right-hand end, so on that end,
and the
is equal to
S
ﬂux is
is directed out of the Gaussian
this is positive, since
E
surface.  There  is  no  ﬂux  through  the  side  walls  of  the  cylinder,
since  these  walls  are  parallel  to
So  the  total  ﬂux  integral  in
sA,
Gauss’s law is
EA.
so Eq. (22.8) yields

The net charge enclosed by the cylinder is
EA = sA>P0;
we then have

EA;

S
.
E

E(cid:2)

E

E =

s
P0

(ﬁeld between oppositely charged conducting plates)

Example 22.9

Field of a uniformly charged sphere

The ﬁeld is uniform and perpendicular to the plates, and its magni-
tude is independent of the distance from either plate. The Gaussian
to
surface
the left of plate 1 and to the right of plate 2, respectively. We leave
these calculations to you (see Exercise 22.29).

yields the same result. Surfaces

E = 0

yield

and

S4

S2

S3

EVALUATE: We obtained the same results in Example 21.11 by using
the principle of superposition of electric ﬁelds. The ﬁelds due to the
S
two sheets of charge (one on each plate) are
and
from Exam-
E
1
s>2P0.
The total electric ﬁeld
ple 22.7, both of these have magnitude
S
(cid:2) E
1 (cid:3) E
at any point is the vector sum
in
At points
2.
a
S
point in opposite directions, and their sum is
Fig. 22.21b,
E
S
zero. At point
are in the same direction; their sum has
E
magnitude

just as we found above using Gauss’s law.

and
1
S
,
b
E
E = s>P0,

S
E
2
and

and

S
E

S
E

2;

c

S

1

2

Positive electric charge
ume of an insulating sphere with radius
electric ﬁeld at a point  a distance  from the center of the sphere.

is distributed uniformly throughout the vol-
Find the magnitude of the

R.

Q

P

r

22.22 The magnitude of the electric ﬁeld of a uniformly
charged insulating sphere. Compare this with the ﬁeld for a con-
ducting sphere (see Fig. 22.18).

SOLUTION

IDENTIFY and SET UP: As in Example 22.5, the system is spheri-
cally symmetric. Hence we can use the conclusions of that exam-
ple  about  the  direction  and  magnitude  of
To  make  use  of  the
spherical  symmetry,  we  choose  as  our  Gaussian  surface  a  sphere
concentric with the charge distribution.
with radius

S
.
E

r,

+
+
+

+

+ +
r
+
r
+
+
+
+ +
+
++
+ +
E

+

Spherical insulator

+

+

R

Gaussian
surface

S
E

E(cid:2) = E

is  radial  at  every
and the ﬁeld magnitude
is the same at every point on the surface. Hence the total electric
and the total

EXECUTE: From  symmetry,  the  direction  of
point on the Gaussian surface, so
E
ﬂux through the Gaussian surface is the product of
area of the surface

—that is,
The  amount  of  charge  enclosed  within  the  Gaussian  surface
The
divided by the volume of

depends on  To ﬁnd E inside the sphere, we choose
volume charge density
the entire charged sphere of radius

E
£E = 4pr 2E.

is the charge
R :

A = 4pr 2

r 6 R.

Q

r.

r

r =

Q
4pR3>3

The volume
total charge

Vencl
Qencl

enclosed by the Gaussian surface is
enclosed by that surface is

pr 3,

4
3

so the

Qencl = rVencl = a

Q
4pR3>3
Then Gauss’s law, Eq. (22.8), becomes

b A 4
3

pr 3B = Q

r 3
R3

4pr 2E =

E =

r 3
R3

Q
P0
1
4pP0

  or

Qr
R3

(ﬁeld inside a uniformly
charged sphere)

The  ﬁeld  magnitude  is  proportional  to  the  distance  of  the  ﬁeld
point from the center of the sphere (see the graph of E versus r in
Fig. 22.22).

r

To ﬁnd E outside the sphere, we take
Qencl = Q,

the entire charged sphere, so

This surface encloses

r 7 R.
and Gauss’s law gives

4pr 2E =

E =

  or

Q
P0
1
4pP0

Q
r 2

(ﬁeld outside a uniformly
charged sphere)

E(R) 5

1
4pP
0

Q
R2

E 5

1
4pP
0

Qr
R3

E 5 1
4pP
0

Q
r 2

O

R

r

The ﬁeld outside any spherically symmetric charged body varies as
1>r 2,
as though the entire charge were concentrated at the center.
This is graphed in Fig. 22.22.
S
If the charge is negative,
E

is radially inward and in the expres-

sions for  we interpret

E

Q

as the absolute value of the charge.

r.

r = R
EVALUATE:  Notice that if we set
,
in either expression for
E
E = Q>4pP0R2
for  the  magnitude  of  the
we  get  the  same  result
ﬁeld at the surface of the sphere. This is because the magnitude
E
is a continuous function of  By contrast, for the charged conduct-
ing  sphere  of  Example  22.5  the  electric-ﬁeld  magnitude  is
E = 0
discontinuous at
just inside the sphere
SE = Q>4pP0R2
just outside the sphere). In general, the electric
to
ﬁeld
is discontinuous in magnitude, direction, or both wherever
there is a sheet of charge, such as at the surface of a charged con-
ducting sphere (Example 22.5), at the surface of an inﬁnite charged
sheet  (Example  22.7),  or  at  the  surface  of  a  charged  conducting
plate (Example 22.8).

(it jumps from

r = R

E

The approach used here can be applied to any spherically sym-
metric distribution of charge, even if it is not radially uniform, as it
was here. Such charge distributions occur within many atoms and
atomic  nuclei,  so  Gauss’s  law  is  useful  in  atomic  and  nuclear
physics.
