Ka = 0
EXECUTE: We  have
and
and
and  our  expressions  for
Ua
v.
equation, then solve for  We ﬁnd

Kb = 1
Ub

2 mv2.

We  substitute  these
into  the  energy-conservation

0 + q0Va = 1

2mv2 + q0Vb

v =

2q01Va - Vb2
m

A

We calculate the potentials using Eq. (23.15),

V = q>4pP0r

:

Finally,

Va = 19.0 * 109 N # m2>C22a 3.0 * 10-9 C

0.010 m

+

1-3.0 * 10-9 C2
0.020 m

b

= 1350 V

23.3 Calculating Electric Potential

767

Vb = 19.0 * 109 N # m2>C22a 3.0 * 10-9 C

0.020 m

+

1-3.0 * 10-9 C2
0.010 m

b

= - 1350 V

Va - Vb = 11350 V2 - 1-1350 V2 = 2700 V

v =

212.0 * 10-9 C212700 V2
5.0 * 10-9 kg

A

= 46 m>s

EVALUATE: Our result makes sense: The positive test charge speeds
up as it moves away from the positive charge and toward the nega-
tive charge. To check unit consistency in the ﬁnal line of the calcu-
so the numerator under the radical
lation, note that
has units of  or kg # m2>s2.
J

1 V = 1 J>C,

Test Your Understanding of Section 23.2 If the electric potential at a certain
point is zero, does the electric ﬁeld at that point have to be zero? (Hint: Consider point
in Example 23.4 and Example 21.8.)

c

❙

23.3 Calculating Electric Potential

When  calculating  the  potential  due  to  a  charge  distribution,  we  usually  follow
one of two routes. If we know the charge distribution, we can use Eq. (23.15) or
(23.16). Or if we know how the electric ﬁeld depends on position, we can use Eq.
(23.17), deﬁning the potential to be zero at some convenient place. Some prob-
lems require a combination of these approaches.

As you read through these examples, compare them with the related examples
of calculating electric ﬁeld in Section 21.5. You’ll see how much easier it is to
calculate scalar electric potentials than vector electric ﬁelds. The moral is clear:
Whenever  possible,  solve  problems  using  an  energy  approach  (using  electric
potential and electric potential energy) rather than a dynamics approach (using
electric ﬁelds and electric forces).

Problem-Solving Strategy 23.1

Calculating Electric Potential

IDENTIFY the relevant concepts: Remember that electric potential
is potential energy per unit charge.

SET UP the problem using the following steps:
1. Make  a  drawing  showing  the  locations  and  values  of  the
charges (which may be point charges or a continuous distribu-
tion of charge) and your choice of coordinate axes.

2. Indicate on your drawing the position of the point at which you
. Sometimes this posi-
from the

want to calculate the electric potential
tion will be an arbitrary one (say, a point a distance
center of a charged sphere).

V

r

EXECUTE the solution as follows:
1. To  ﬁnd  the  potential  due  to  a  collection  of  point  charges,  use
Eq. (23.15). If you are given a continuous charge distribution,
devise  a  way  to  divide  it  into  inﬁnitesimal  elements  and  use
Eq. (23.16). Carry out the integration, using appropriate limits
to include the entire charge distribution.

2. If you are given the electric field, or if you can find it using
any of the methods presented in Chapter 21 or 22, it may be

V

easier to find the potential difference between points a and b
using Eq. (23.17) or (23.18). When appropriate, make use of
to  be  zero  at  some  convenient
your  freedom  to  define
place, and choose this place to be point
(For point charges,
this  will  usually  be  at  infinity.  For  other  distributions  of
charge—especially those that themselves extend to infinity—
it may be necessary to define
to be zero at some finite dis-
Vb
tance from the charge distribution.) Then the potential at any
other point, say
, can by found from Eq. (23.17) or (23.18)
Vb = 0.
with

b.

a

3. Although potential V is a scalar quantity, you may have to use
and  when you use Eq. (23.17)

S
d l

S
E

components of the vectors
or (23.18) to calculate V.

EVALUATE  your answer: Check whether your answer agrees with
as  a  function  of  position,
your  intuition.  If  your  result  gives
graph the function to see whether it makes sense. If you know the
electric ﬁeld, you can make a rough check of your result for  by
verifying that  decreases if you move in the direction of

S
.E

V

V

V

768

CHAPTER 23 Electric Potential

Example 23.8 A charged conducting sphere

A solid conducting sphere of radius  has a total charge  Find the
electric potential everywhere, both outside and inside the sphere.

q.

R

SOLUTION

IDENTIFY  and SET  UP:  In  Example  22.5  (Section  22.4)  we  used
Gauss’s law to ﬁnd the electric ﬁeld at all points for this charge dis-
tribution.  We  can  use  that  result  to  determine  the  corresponding
potential.

EXECUTE: From Example 22.5, the ﬁeld outside the sphere is the
same as if the sphere were removed and replaced by a point charge
at inﬁnity, as we did for a point charge. Then the
q.
potential at a point outside the sphere at a distance  from its center
is the same as that due to a point charge  at the center:

We take

V = 0

q

r

V =

1
4pP0

q
r

S
E

The potential at the surface of the sphere is

Vsurface = q>4pP0R.

Inside the  sphere,

is  zero  everywhere.  Hence  no  work  is
done on a test charge that moves from any point to any other point
inside  the  sphere.  This  means  that  the  potential  is  the  same  at
at
every point inside the sphere and is equal to its value
the surface.

q>4pP0R

from the sphere. As you move away from the sphere, in the direc-
tion of

decreases (as it should).

S
,
VE

23.16 Electric-ﬁeld magnitude E and potential V at points
inside and outside a positively charged spherical conductor.

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

R

+

+

+

+

+

+

E

E 5 0

O

V

O

E 5

1
4pP
0

q
R2

E 5 1
4pP
0

q
r 2

V 5 1
4pP

0

q
R
V 5 1
4pP
0

r

q
r

r

EVALUATE:  Figure 23.16 shows the ﬁeld and potential for a posi-
In  this  case  the  electric  ﬁeld  points  radially  away
tive  charge

q.

Ionization and Corona Discharge
The results of Example 23.8 have numerous practical consequences. One conse-
quence  relates  to  the  maximum  potential  to  which  a  conductor  in  air  can  be
raised. This  potential  is  limited  because  air  molecules  become  ionized, and  air
3 * 106 V>m.
becomes  a  conductor,  at  an  electric-ﬁeld  magnitude  of  about
Assume for the moment that q is positive. When we compare the expressions in
at the surface
Example 23.8 for the potential
Em
of a charged conducting sphere, we note that
rep-
resents the electric-ﬁeld magnitude at which air becomes conductive (known as
to which a spheri-
the dielectric strength of air), then the maximum potential
cal conductor can be raised is

Vsurface = EsurfaceR.

and ﬁeld magnitude

Thus, if

Esurface

Vsurface

Vm

Vm = REm

1 cm

in radius in air,

Vm = 110-2 m213 *

106 V>m2 =
For a conducting sphere
30,000 V.
No  amount  of  “charging”  could  raise  the  potential  of  a  conducting
sphere  of  this  size  in  air  higher  than  about
attempting  to  raise  the
potential  further  by  adding  extra  charge  would  cause  the  surrounding  air  to
become  ionized  and  conductive,  and  the  extra  added  charge  would  leak  into
the air.

30,000 V;

To attain even higher potentials, high-voltage machines such as Van de Graaff
generators use spherical terminals with very large radii (see Fig. 22.26 and the
R = 2 m
photograph that opens Chapter 22). For example, a terminal of radius
Vm = 12 m213 * 106 V>m2 = 6 * 106 V = 6 MV.
has a maximum potential
Our result in Example 23.8 also explains what happens with a charged con-
ductor with a very small radius of curvature, such as a sharp point or thin wire.
Because  the  maximum  potential  is  proportional  to  the  radius,  even  relatively

23.3 Calculating Electric Potential

769

23.17 The metal mast at the top of the
Empire State Building acts as a lightning
rod. It is struck by lightning as many as
500 times each year.

small potentials applied to sharp points in air produce sufﬁciently high ﬁelds just
outside  the  point  to  ionize  the  surrounding  air,  making  it  become  a  conductor.
The resulting current and its associated glow (visible in a dark room) are called
corona. Laser printers and photocopying machines use corona from ﬁne wires to
spray charge on the imaging drum (see Fig. 21.2).

A large-radius conductor is used in situations where it’s important to prevent
corona. An example is the metal ball at the end of a car radio antenna, which pre-
vents the static that would be caused by corona. Another example is the blunt end
of a metal lightning rod (Fig. 23.17). If there is an excess charge in the atmos-
phere, as happens during thunderstorms, a substantial charge of the opposite sign
can build up on this blunt end. As a result, when the atmospheric charge is dis-
charged through a lightning bolt, it tends to be attracted to the charged lightning
rod rather than to other nearby structures that could be damaged. (A conducting
wire connecting the lightning rod to the ground then allows the acquired charge
to dissipate harmlessly.) A lightning rod with a sharp end would allow less charge
buildup and hence would be less effective.

Example 23.9 Oppositely charged parallel plates

Find  the  potential  at  any  height
charged parallel plates discussed in Section 23.1 (Fig. 23.18).

between  the  two  oppositely

y

SOLUTION

IDENTIFY and SET UP: We discussed this situation in Section 23.1.
From Eq. (23.5), we know the electric potential energy
for a test
(We  set  y (cid:4) 0  and  U (cid:4) 0 at  the  bottom
charge
, to ﬁnd the electric potential
plate.) We use Eq. (23.12),
V

as a function of

U = q0Ey.

U = q0V

q0

is

U

y.

EXECUTE: The  potential
energy per unit charge:

V1y2

at  coordinate

y

is  the  potential

V1y2 =

U1y2
q0

=

q0Ey
q0

= Ey

The potential decreases as we move in the direction of
upper to the lower plate. At point  where

and

a,

S
from the
E
V1y2 = Va,

Va - Vb = Ed   and   E =

y = d
Va - Vb
d

=

Vab
d

Vab

where
is  the  potential  of  the  positive  plate  with  respect  to  the
negative plate. That is, the electric ﬁeld equals the potential differ-
ence between the plates divided by the distance between them. For a
the smaller the distance  between the
given potential difference
d
of  the  electric  ﬁeld.  (This
two  plates,  the  greater  the  magnitude
holds only for the planar geometry
relationship between

Vab,

and

E

E

Vab

23.18 The charged parallel plates from Fig. 23.2.

S
E

y

a
q0

b
O

y

d

x

we have described. It does not work for situations such as concen-
tric cylinders or spheres in which the electric ﬁeld is not uniform.)

?

EVALUATE: Our  result  shows  that
y = 0
test charge placed at the bottom plate.

). This is consistent with our choice that

V = 0

at  the  bottom  plate  (at
U = q0V = 0
for a

CAUTION “Zero potential” is arbitrary You might think that if a
conducting body has zero potential, it must necessarily also have
zero net charge. But that just isn’t so! As an example, the plate at
y = 0
but has a nonzero
charge per unit area
There’s nothing particularly special about
the  place  where  potential  is  zero;  we  can  deﬁne this  place  to  be
wherever we want it to be. ❙

in Fig. 23.18 has zero potential
-s.

1V = 02

Example 23.10

An infinite line charge or charged conducting cylinder

Find the potential at a distance
with linear charge density (charge per unit length)

from a very long line of charge
l.

r

SOLUTION

IDENTIFY and SET UP: In both Example 21.10 (Section 21.5) and
Example 22.6 (Section 22.4) we found that the electric field at a

r

radial  distance
Er = l>2pP0r.
has  only  a  radial  component  given  by
this  expression  to  find  the  potential  by  integrating
Eq. (23.17).

from  a  long  straight-line  charge  (Fig.  23.19a)
We  use
S
E
as  in

EXECUTE: Since  the  ﬁeld  has  only  a  radial  component,  we  have
S # d l
E
Hence from Eq. (23.17) the potential of any point a

=

S

Er dr.

Continued

770

CHAPTER 23 Electric Potential

with respect to any other point
the line of charge, is
S # d l
E

Va - Vb =

=

S

b

b

L
a

Er dr =

L
a

b,

at radial distances

ra

and

rb

from

23.19 Electric ﬁeld outside (a) a long, positively charged wire
and (b) a long, positively charged cylinder.

rb

dr
r

=

l
2pP0

ln

rb
ra

(a)

l
2pP0 L
ra
Vb = 0,
from

(b)

Er

r

+ + + + + + + + + + + + +

at  inﬁnity  and  set
ra

is
we  ﬁnd  that
line  charge:
the
. This is not a useful way to deﬁne
for  this  problem!  The  difﬁculty  is  that  the  charge  distribution

b
If  we  take  point
inﬁnite for  any  ﬁnite  distance
Va = 1l>2pP02ln 1q>ra2 = q
V
itself extends to inﬁnity.

Va

Instead, as recommended in Problem-Solving Strategy 23.1, we
Vb = 0
r0.
is given

at  an  arbitrary  but  ﬁnite radial  distance
at point  at a radial distance

at  point

b
V = Va

a

r

set
Then the potential
by

V - 0 = 1l>2pP02 ln 1r0>r2,

or

Er

+

+

r

+

+

+ +

+

+

+ +

+
R
+
+

+ +
+

+

+

V =

l
2pP0

ln

r0
r

l

is  positive,  then

V
increases. This is as it should be:  decreases as we

EVALUATE:  According  to  our  result,  if
decreases as
r
move in the direction of

S
E
From  Example  22.6,  the  expression  for

with  which  we
started also applies outside a long, charged conducting cylinder
with  charge  per  unit  length
(Fig.  23.19b).  Hence  our  result
also gives the potential for such a cylinder, but only for values

Er

V

l

.

Example 23.11

A ring of charge

Electric  charge  Q is  distributed  uniformly  around  a  thin  ring  of
radius
on  the  ring
a
axis at a distance

(Fig.  23.20).  Find  the  potential  at  a  point

from the center of the ring.

P

x

SOLUTION

IDENTIFY  and SET  UP: We divide the ring into inﬁnitesimal seg-
ments  and  use  Eq.  (23.16) to  ﬁnd  All  parts  of  the  ring  (and
therefore  all  elements  of  the  charge  distribution)  are  at  the  same
distance from

P.

V.

EXECUTE: Figure 23.20 shows that the distance from each charge
Hence we can take the factor
element
1>r

outside the integral in Eq. (23.16), and

r = 1x 2 + a2.

to

dq

is

P

V =

1
4pP0 L

dq
r

=

1
4pP0

1
2x 2 + a2 L

dq =

1
4pP0

Q
2x 2 + a2

EVALUATE: When
becomes approximately
distance

is  much  larger  than
V = Q>4pP0x,
Q

V
which is the potential at a
. Very  far  away  from  a  charged

our  expression  for

from  a  point  charge

a,

x

x

(the distance from the cylinder axis) equal to or greater than
to be the cylinder
then at any point for which

of the cylinder. If we choose

r = R,

V = 0

so that

when

r0

R

r

of
the radius
radius
r 7 R,

R,

V =

l
2pP0

ln

R
r

S
E
Inside the cylinder,
the cylinder’s surface.

(cid:2) 0,

and  has the same value (zero) as on

V

23.20 All the charge in a ring of charge Q is the same distance
r from a point P on the ring axis.

r5(cid:2)x21

a2

x

P

a

O

Q

ring, its electric potential looks like that of a point charge. We drew
a similar conclusion about the electric ﬁeld of a ring in Example
21.9 (Section 21.5).

We  know  the  electric  ﬁeld  at  all  points  along  the  -axis  from
along this axis

Example 21.9 (Section 21.5), so we can also ﬁnd
by integrating

as in Eq. (23.17).

S # d l
E

V

x

S

Example 23.12

Potential of a line of charge

Q

2a

is distributed uniformly along a line of
Positive electric charge
y = + a
length
(Fig. 23.21). Find the electric potential at a point  on the x-axis at
a distance

lying  along  the  y-axis  between

y = - a
P

from the origin.

and

x

SOLUTION

IDENTIFY  and SET  UP: This is the same situation as in Example
21.10 (Section 21.5), where we found an expression for the electric
