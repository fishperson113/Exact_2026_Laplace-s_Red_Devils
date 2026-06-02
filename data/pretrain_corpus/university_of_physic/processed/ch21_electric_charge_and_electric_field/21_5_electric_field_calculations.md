S
E

S
EXECUTE: (a)  Although
F
downward  (because  the  electron’s  charge  is  negative)  and  so
is  negative.  Because
constant:

is
Fy
is  constant,  the  electron’s  acceleration  is

is  upward  (in  the

-direction),

+y

Fy

21.5 Electric-Field Calculations

703

The  velocity  is  downward,  so
tron’s kinetic energy is

vy = - 5.9 * 106 m>s.

The  elec-

K = 1

2 mv2 = 1

2

19.11 * 10-31 kg215.9 * 106 m>s22

ay =

Fy
m

=

-eE
m

=

1-1.60 * 10-19 C211.00 * 104 N>C2
9.11 * 10-31 kg

= - 1.76 * 1015 m>s2

(b)  The  electron  starts  from  rest,  so  its  motion  is  in  the
-direction only (the direction of the acceleration). We can ﬁnd the
y
electron’s speed at any position y using the constant-acceleration
Eq.  (2.13),
and
y0 = 0,
ƒ vy ƒ = 22ayy = 221-1.76 * 1015 m>s221 -1.0 * 10-2 m2

0y + 2ay1y - y02.
y = v 2
v 2
y = - 1.0 cm = - 1.0 * 10-2 m

v0y = 0

We  have

we have

so at

= 5.9 * 106 m>s

= 1.6 * 10-17 J

(c) From Eq. (2.8) for constant acceleration,

vy = v0y + ayt,

t =

vy - v0y
ay

=

1-5.9 * 106 m>s2 - 10 m>s2
-1.76 * 1015 m>s2

= 3.4 * 10-9 s

EVALUATE:  Our  results  show  that  in  problems  concerning  sub-
atomic  particles  such  as  electrons,  many  quantities—including
acceleration, speed, kinetic energy, and time—will have very dif-
ferent values from those typical of everyday objects such as base-
balls and automobiles.

Test Your Understanding of Section 21.4 (a) A negative point charge
moves along a straight-line path directly toward a stationary positive point charge.
Which aspect(s) of the electric force on the negative point charge will remain con-
stant as it moves? (i) magnitude; (ii) direction; (iii) both magnitude and direction;
(iv) neither magnitude nor direction. (b) A negative point charge moves along a circular
orbit around a positive point charge. Which aspect(s) of the electric force on the negative
point charge will remain constant as it moves? (i) magnitude; (ii) direction; (iii) both
magnitude and direction; (iv) neither magnitude nor direction.

❙

21.5 Electric-Field Calculations

Equation  (21.7) gives  the  electric  ﬁeld  caused  by  a  single  point  charge.  But  in
most realistic situations that involve electric ﬁelds and forces, we encounter charge
that is distributed over space. The charged plastic and glass rods in Fig. 21.1 have
electric charge distributed over their surfaces, as does the imaging drum of a laser
printer (Fig. 21.2). In this section we’ll learn to calculate electric ﬁelds caused by
various distributions of electric charge. Calculations of this kind are of tremen-
dous importance for technological applications of electric forces. To determine
the trajectories of atomic nuclei in an accelerator for cancer radiotherapy or of
charged  particles  in  a  semiconductor  electronic  device,  you  have  to  know  the
detailed nature of the electric ﬁeld acting on the charges.

ActivPhysics 11.5: Electric Field Due to a
Dipole
ActivPhysics 11.6: Electric Field: Problems

q1, q2, q3,

The Superposition of Electric Fields
To ﬁnd the ﬁeld caused by a charge distribution, we imagine the distribution to be
made up of many point charges
. . . . (This is actually quite a realistic
description, since we have seen that charge is carried by electrons and protons
each  point
that  are  so  small  as  to  be  almost  pointlike.) At  any  given  point
q0
charge produces its own electric ﬁeld
placed at
S
P
q0 E
from
and so on. From the principle of superposition of forces discussed in
charge
Section 21.3, the total force
is the vec-
tor sum of these individual forces:
S

P,
. . . , so a test charge
S
2 (cid:2)
a  force
F

S
S
2, E
E
from  charge

that the charge distribution exerts on

experiences  a  force

S
1 (cid:2) q0 E
F

S
1, E

S
F
0

q1,

q2,

q0

3,

S

S

S

S

S

S

2

1

S
0 (cid:2) F
F

1 (cid:4) F

2 (cid:4) F

3 (cid:4) Á (cid:2) q0 E

1 (cid:4) q0 E

2 (cid:4) q0 E

3 (cid:4) Á

The combined effect of all the charges in the distribution is described by the total
. From the deﬁnition of electric ﬁeld, Eq. (21.3), this is
electric ﬁeld

at point

S
E

P

S
E

(cid:2)

S
F
0
q0

S

(cid:2) E

S

1 (cid:4) E

S

2 (cid:4) E

3 (cid:4) Á

704

CHAPTER 21 Electric Charge and Electric Field

21.21 Illustrating the principle of
superposition of electric ﬁelds.

q1

Electric field
at P due to q2

P

Electric field
at P due to q1

q2

S
E2

S
E

S
E1

The total electric field E at point
S
P is the vector sum of E1 and E2.

S

S

The total electric ﬁeld at

is the vector sum of the ﬁelds at  due to each point
charge in the charge distribution (Fig. 21.21). This is the principle of superposi-
tion of electric ﬁelds.

P

P

l

When charge is distributed along a line, over a surface, or through a volume, a
few  additional  terms  are  useful.  For  a  line  charge  distribution  (such  as  a  long,
thin,  charged  plastic  rod),  we  use
(the  Greek  letter  lambda)  to  represent  the
When charge
linear charge density (charge per unit length, measured in
is distributed over a surface (such as the surface of the imaging drum of a laser
(sigma)  to  represent  the  surface  charge  density (charge
printer),  we  use
per  unit  area,  measured  in
).  And  when  charge  is  distributed  through  a
(rho) to represent the volume charge density (charge per unit
volume, we use
).
volume,

C>m).

C>m2

C>m3

s

r

Some of the calculations in the following examples may look fairly intricate.
After you’ve worked through the examples one step at a time, the process will
seem less formidable. We will use many of the calculational techniques in these
examples  in  Chapter  28 to  calculate  the  magnetic ﬁelds  caused  by  charges  in
motion.

Problem-Solving Strategy 21.2

Electric-Field Calculations

IDENTIFY the relevant concepts: Use the principle of superposition
to calculate the electric ﬁeld due to a discrete or continuous charge
distribution.

SET UP the problem using the following steps:
1. Make a drawing showing the locations of the charges and your

choice of coordinate axes.

2. On your drawing, indicate the position of the ﬁeld point P (the

point at which you want to calculate the electric ﬁeld

S
E

).

EXECUTE the solution as follows:
1. Use  consistent  units.  Distances  must  be  in  meters  and  charge
must  be  in  coulombs.  If  you  are  given  centimeters  or  nano-
coulombs, don’t forget to convert.

2. Distinguish between the source point S and the ﬁeld point P. The
ﬁeld produced by a point charge always points from S to P if the
charge is positive, and from P to S if the charge is negative.
3. Use vector addition when applying the principle of superposi-
tion;  review  the  treatment  of  vector  addition  in  Chapter  1 if
necessary.

Example 21.8

Field of an electric dipole

q1

+12 nC

and (cid:3)
Point charges  (cid:3)
q2
are 0.100 m apart
(Fig.  21.22).  (Such  pairs  of  point  charges  with  equal  magnitude
and opposite sign are called electric dipoles.) Compute the electric
ﬁeld caused by
and the total ﬁeld (a) at
point
a;

the ﬁeld caused by
q2,
and (c) at point
c.
b;

q1,
(b) at point

-12 nC

SOLUTION

IDENTIFY and SET UP: We must ﬁnd the total electric ﬁeld at vari-
ous points due to two point charges. We use the principle of super-
1 (cid:4) E
Figure  21.22 shows  the  coordinate
position:
system and the locations of the ﬁeld points

(cid:2) E

S
E

2.

S

S

EXECUTE: At each ﬁeld point,
ﬁrst calculate the magnitudes
the magnitude of the ﬁeld

S
E

1a

S
depends on
E
and
E1
E2
caused by

S
E

a, b, and c.
S
E
at each ﬁeld point. At
isq1

there; we
a

and

2

1

4. Simplify your calculations by exploiting any symmetries in the

charge distribution.

5. If the charge distribution is continuous, deﬁne a small element
of charge that can be considered as a point, ﬁnd its electric ﬁeld
at P, and ﬁnd a way to add the ﬁelds of all the charge elements
by  doing  an  integral.  Usually  it  is  easiest  to  do  this  for  each
separately, so you may need to evaluate more
component of
than  one  integral.  Ensure  that  the  limits  on  your  integrals  are
correct;  especially  when  the  situation  has  symmetry,  don’t
count a charge twice.

S
E

S
EVALUATE your answer: Check that the direction of
E
is reason-
is a function
E
able. If your result for the electric-ﬁeld magnitude
x
of position (say, the coordinate  ), check your result in any limits
for which you know what the magnitude should be. When possi-
ble, check your answer by calculating it in a different way.

E1a =

1
4pP0

ƒ q1 ƒ
r 2

= 19.0 * 109 N # m2>C22 12 * 10-9 C
10.060 m22

= 3.0 * 104 N>C

We  calculate  the  other  ﬁeld  magnitudes  in  a  similar  way.  The
results are

E1a = 3.0 * 104 N>C
E1c = 6.39 * 103 N>C

E1b = 6.8 * 104 N>C

E2a = 6.8 * 104 N>C
E2c = E1c = 6.39 * 103 N>C

E2b = 0.55 * 104 N>C

The directions of  the  corresponding  ﬁelds  are  in  all  cases  away
from the positive charge

and toward the negative charge

.q2

q1

21.22 Electric ﬁeld at three points,
charges

c
and  which form an electric dipole.

a, b,

q2,

q1

and  , set up by

y

S
E1

c

S
E2

a

a

S
Ec

13.0 cm

13.0 cm

S
Eb

b

a

q1

+

4.0
cm

6.0
cm

q2
–

x

a

S
Ea

4.0
cm

(a) At a,

S
E

S
E

S
E

2a

and

are both directed to the right, so

1a
a (cid:2) E1aın (cid:4) E2aın (cid:2) 19.8 * 104 N>C2ın

(b) At b,

S
E

1b

right, so

is directed to the left and

S
E

2b

is directed to the

21.5 Electric-Field Calculations

705

(c) Figure 21.22 shows the directions of
x

vectors have the same  -component:

S
E

1

and

S
E

2

at c. Both

E1cx = E2cx = E1c cos a = 16.39 * 103 N>C2A 5

13

B

= 2.46 * 103 N>C

From symmetry,
is zero. Hence

E1y

and

E2y

are equal and opposite, so their sum

S
E

c (cid:2) 212.46 * 103 N>C2ın (cid:2) 14.9 * 103 N>C2ın

S
E

c

S

c

q2

q1

S
r
1

to  point

rN
1 (cid:2) r

using Eq. (21.7) for the ﬁeld of a
is
from
.  Hence  the  unit  vector  that  points  from
1>r (cid:2) cos a ın + sin a ≥n
.  By  symmetry,  the
to  point  c has  the  opposite  x-
2 (cid:2) -cos a ın (cid:4) sin a ≥n
.
and
in
2c
and the distance

EVALUATE:  We can also ﬁnd
point  charge.  The  displacement  vector
S
1 (cid:2) r cos a ın (cid:4) r sin a ≥n
r
to  point  c is
q1
unit  vector  that  points  from
component  but  the  same  y-component:
We can now use Eq. (21.7) to write the ﬁelds
vector form, then ﬁnd their sum. Since
r to c is the same for both charges,
q1
r 2
22 (cid:2)

2c (cid:2) 1
4pP0
1 (cid:4) q2rN

q2
1 (cid:4) 1
rN
4pP0
r 2
q1
1rN
1 (cid:3) rN
4pP0r 2

S
E
1c
q2 = - q1

(cid:2) 1

1c (cid:4) E

c (cid:2) E

1q1rN

rN
2

22

S
E

S
E

at

rN

c

S

S

4pP0r 2
q1
r2

4pP0

(cid:2) 1

12 cosa ın2

(cid:2) 219.0 * 109 N # m2>C22 12 * 10-9 C
10.13 m22

A 5
13

B ın

(cid:2) 14.9 * 103 N>C2ın

S
E

b (cid:2) -E1bın (cid:4) E2bın (cid:2) 1-6.2 * 104 N>C2ın

This is the same as we calculated in part (c).

Example 21.9

Field of a ring of charge

Q
is  uniformly  distributed  around  a  conducting  ring  of
(Fig. 21.23). Find the electric ﬁeld at a point  on the ring

P

Charge
a
radius
axis at a distance

x

from its center.

SOLUTION

IDENTIFY  and SET  UP:  This is a problem in the superposition of
electric ﬁelds. Each bit of charge around the ring produces an elec-
tric ﬁeld at an arbitrary point on the x-axis; our target variable is
the total ﬁeld at this point due to all such bits of charge.

the  charge  in  a  segment  of  length

EXECUTE: We  divide  the  ring  into  inﬁnitesimal  segments  ds as
shown  in  Fig.  21.23.  In  terms  of  the  linear  charge  density
l = Q>2pa,
dQ = l ds.
Consider  two  identical  segments,  one  as  shown  in  the  ﬁgure  at
y = a
y = - a
.  From
they exert on a point
Example 21.4, we see that the net force
test charge at P, and thus their net ﬁeld
, are directed along the
x-axis. The same is true for any such pair of segments around the
ring, so the net ﬁeld at P is along the x-axis:

and  another  halfway  around  the  ring  at

SdF
dE

S
E

is

ds

S

To calculate

Ex,

gle ring segment to the point
tude of this segment’s contribution

is

P

Sr 2 = x 2 + a2.
dE

note that the square of the distance  from a sin-
Hence the magni-

to the electric ﬁeld at

P

is

(cid:2) Exın.
r

21.23 Calculating the electric ﬁeld on the axis of a ring of
charge. In this ﬁgure, the charge is assumed to be positive.

dE =

dQ

ds

y

a

O

Q

r(cid:3)

x2(cid:5)a2

a

P

x

dEy

dEx
a

x

S
dE

1
4pP0

dQ
x 2 + a2
dEx = dE cos a

The x-component of this ﬁeld is
l
ds and Fig. 21.23 shows that

cos a

= x>r = x>1x 2 + a221>2,

. We know dQ (cid:3)
so

dEx = dE cos a =

1
4pP0
lx
1x 2 + a223>2

=

1
4pP0

dQ
x 2 + a2

x
2x 2 + a2

ds

Continued

706

CHAPTER 21 Electric Charge and Electric Field

Ex

To ﬁnd  we integrate this expression over the entire ring—that is,
for s from 0 to 2pa (the circumference of the ring). The integrand
has the same value for all points on the ring, so it can be taken out-
side the integral. Hence we get

2pa

lx
1x 2 + a223>2 3
0

ds

12pa2

1
4pP0
lx
1x 2 + a223>2

Ex =

L

dEx =

=

1
4pP0
(cid:2) Exın (cid:2) 1
4pP0

S
E

S
E

(cid:2) 0

2

1

EVALUATE:  Equation (21.8) shows that
at the center of the
ring x (cid:3) 0 . This makes sense; charges on opposite sides of the
ring push in opposite directions on a test charge at the center, and
the vector sum of each such pair of forces is zero. When the ﬁeld
is  much  farther  from  the  ring  than  the  ring’s  radius,  we
point
P
x W a
have
and the denominator in Eq. (21.8) becomes approxi-
mately equal to

. In this limit the electric ﬁeld at P is

x 3

S
E

(cid:2) 1

4pP0

ın

Q
x 2

Qx
1x 2 + a223>2

ın

(21.8)

That is, when the ring is so far away that its radius is negligible in
comparison to the distance  , its ﬁeld is the same as that of a point
charge.

x

Example 21.10

Field of a charged line segment

Positive  charge
y = - a
between
the  -axis at a distance
x

Q
and

is  distributed  uniformly  along  the
y = + a.
x

-axis
Find the electric ﬁeld at point  on
P

from the origin.

y

SOLUTION

21.24 Our sketch for this problem.

IDENTIFY  and SET  UP:  Figure  21.24 shows  the  situation.  As  in
Example 21.9, we must ﬁnd the electric ﬁeld due to a continuous
distribution of charge. Our target variable is an expression for the
electric ﬁeld at
. The  -axis is a perpendicular
bisector of the segment, so we can use a symmetry argument.

as a function of

P

x

x

EXECUTE: We divide the line charge of length 2a into inﬁnitesimal
l = Q>2a,
segments of length dy. The linear charge density is
and
dQ = l dy = 1Q>2a2dy
. The distance r
the charge in a segment is
r = 1x 2 + y221>2
from a segment at height y to the ﬁeld point P is
,
so the magnitude of the ﬁeld at P due to the segment at height y is

dE =

1
4pP0

dQ
r 2

=

1
4pP0

Q
2a

dy
1x 2 + y22

Figure 21.24 shows that the x- and y-components of this ﬁeld are
,  where  cos  a (cid:3) x r and
dEx = dE cos a
sin

dEy = - dE sin a

>
y r. Hence

and

a =

>

dEx =

dEy =

1
4pP0

1
4pP0

Q
2a

Q
2a

x dy
1x 2 + y223>2

y dy
1x 2 + y223>2

To  ﬁnd  the  total  ﬁeld  at  P,  we  must  sum  the  ﬁelds  from  all  seg-
ments along the line—that is, we must integrate from
to
y = + a.
You should work out the details of the integration (a table
of integrals will help). The results are

y = - a

Ex =

Ey =

1
4pP0

1
4pP0

+a

Q
2a L
-a

+a

Q
2a L
-a

or, in vector form,

x dy
1x 2 + y223>2

=

Q
4pP0

1
x2x 2 + a2

y dy
1x 2 + y223>2

= 0

points away from the line of charge if

l

is positive and toward

S
E
the line of charge if

l

is negative.

Ey

EVALUATE: Using  a  symmetry  argument  as  in  Example  21.9,  we
could have guessed that  would be zero; if we place a positive
test charge at
, the upper half of the line of charge pushes down-
ward  on  it,  and  the  lower  half  pushes  up  with  equal  magnitude.
Symmetry also tells us that the upper and lower halves of the seg-
ment contribute equally to the total ﬁeld at P.

P

If the segment is very short (or the ﬁeld point is very far from
the segment) so that
in the denominator
of Eq. (21.9). Then the ﬁeld becomes that of a point charge, just as
in Example 21.9:

we can neglect

x W a,

a

(cid:2) 1

S
E

ın

Q
x 2

4pP0
To see what happens if the segment is very long (or the ﬁeld point
a W x,
we  ﬁrst  rewrite  Eq.  (21.9)
is  very  close  to  it)  so  that
slightly:

S
E

(cid:2) 1

2pP0

l

x21x 2>a22 + 1

ın

(21.10)

In  the  limit
Eq. (21.10), so

a W x

we  can  neglect

x 2>a2

in  the  denominator  of

S
E

(cid:2) 1

4pP0

Q
x2x 2 + a2

ın

(21.9)

S
E

(cid:2)

l
2pP0x

ın

This is the ﬁeld of an inﬁnitely long line of charge. At any point
at a perpendicular distance
magnitude

from the line in any direction,

S
E

P
has

r

E =

l
2pP0r

(inﬁnite line of charge)

Note that this ﬁeld is proportional to
a point charge.

1>r

rather than to

1>r 2

as for

Example 21.11

Field of a uniformly charged disk

21.5 Electric-Field Calculations

707

There’s  really  no  such  thing  in  nature  as  an  infinite  line  of
charge.  But  when  the  field  point  is  close  enough  to  the  line,
there’s  very  little  difference  between  the  result  for  an  infinite
line and the real-life finite case. For example, if the distance  of
the field point from the center of the line is 1% of the length of
the line, the value of
differs from the infinite-length value by
less than 0.02%.

E

r

A nonconducting disk of radius
s
charge density
the disk a distance

x

has a uniform positive surface
. Find the electric ﬁeld at a point along the axis of

R

from its center. Assume that

x

is positive.

SOLUTION

IDENTIFY  and SET  UP:  Figure 21.25 shows the situation. We rep-
resent the charge distribution as a collection of concentric rings of
. In Example 21.9 we obtained Eq. (21.8) for the ﬁeld on
charge
the axis of a single uniformly charged ring, so all we need do here
is integrate the contributions of our rings.

dQ

dQ

r + dr

, inner  radius

EXECUTE: A typical  ring  has  charge
, and  outer
r
radius
. Its area is approximately equal to its width dr times
its circumference 2pr, or
The charge per unit area is
s = dQ>dA,
dQ = s dA = 2psr dr.
We use dQ in place of Q in Eq. (21.8), the expression for the ﬁeld due
to a ring that we found in Example 21.9, and replace the ring radius
a
with  . Then the ﬁeld component

so the charge of the ring is

at point P due to this ring is

dA = 2pr dr.

r

dEx

dEx =

1
4pP0

2psrx dr
1x 2 + r 223>2

21.25 Our sketch for this problem.

To ﬁnd the total ﬁeld due to all the rings, we integrate
from

r = 0

to

dEx

over

r

r = R
R

1
4pP0

(not from –R to R):
12psr dr2x
1x 2 + r 223>2

=

Ex =

L
0

sx
4P0 L
0

R

2r dr
1x 2 + r 223>2

You  can  evaluate  this  integral  by  making  the  substitution
x 2 + r 2
The result is

t =
); you can work out the details.

(which yields

dt = 2r dr

Ex =

=

sx
2P0
s
2P0

c -

1
2x 2 + R2

+ 1
x

d

c1 -

1
21R2>x 22 + 1

d

(21.11)

EVALUATE: If the disk is very large (or if we are very close to it), so
1> 21R2>x 22 + 1
that
in  Eq.  (21.11) is  very
much less than 1. Then Eq. (21.11) becomes

R W x,

the  term

E =

s
2P0

(21.12)

x

from  the  plane.
Our  ﬁnal  result  does  not  contain  the  distance
Hence the electric ﬁeld produced by an inﬁnite plane sheet of charge
is independent of the distance from the sheet. The ﬁeld direction is
everywhere  perpendicular  to  the  sheet,  away  from  it.  There  is  no
such thing as an inﬁnite sheet of charge, but if the dimensions of the
from
sheet are much larger than the distance  of the ﬁeld point
the sheet, the ﬁeld is very nearly given by Eq. (21.12).

P

x

P

If

is to the left of the plane

, the result is the same
except that the direction of
is to the left instead of the right. If
the surface charge density is negative, the directions of the ﬁelds
on both sides of the plane are toward it rather than away from it.

S
E

1x 6 02

Example 21.12

Field of two oppositely charged infinite sheets

-s

and

Two  inﬁnite  plane  sheets  with  uniform  surface  charge  densities
+s
d
(Fig. 21.26). Find the electric ﬁeld between the sheets, above the
upper sheet, and below the lower sheet.

are  placed  parallel  to  each  other  with  separation

SOLUTION

IDENTIFY  and SET  UP: Equation  (21.12) gives  the  electric  ﬁeld
due to a single inﬁnite plane sheet of charge. To ﬁnd the ﬁeld due
to two such  sheets,  we  combine  the  ﬁelds  using  the  principle  of
superposition (Fig. 21.26).

21.26 Finding the electric ﬁeld due to two oppositely charged
inﬁnite sheets. The sheets are seen edge-on; only a portion of the
inﬁnite sheets can be shown!

y

d

Sheet 2

2s

Sheet 1

1s

S
E1

S
E1

S
E1

S
E2

S
E2

S
E2

S

S

E (cid:2) E1

S

S

E (cid:2) E1

S

S

E (cid:2) E1

x

S

(cid:4) E2

(cid:2) 0

S

(cid:4) E2

S

(cid:4) E2

(cid:2) 0

Continued
