C H A

P

T

E

R

2

9

Magnetic Fields Due to Currents

29-1 MAGNETIC FIELD DUE TO A CURRENT

Learning Objectives
After reading this module, you should be able to . . .

29.01 Sketch a current-length element in a wire and indicate
the direction of the magnetic field that it sets up at a given
point near the wire.

29.02 For a given point near a wire and a given current-element
in the wire, determine the magnitude and direction of the
magnetic field due to that element.

29.03 Identify the magnitude of the magnetic field set up by a
current-length element at a point in line with the direction
of that element.

29.04 For a point to one side of a long straight wire carrying
current, apply the relationship between the magnetic field
magnitude, the current, and the distance to the point.
29.05 For a point to one side of a long straight wire carrying

Key Ideas
● The magnetic field set up by a current-carrying conductor can
be found from the Biot–Savart law. This law asserts that the
contribution
ment
ment is

at a point P located a distance r from the current ele-

to the field produced by a current-length ele-

:
dB

i ds:

:
dB

!

m0
4p

i ds: $ rˆ
r2

(Biot – Savart law).

is a unit vector that points from the element toward P.

rˆ
Here
The quantity m0, called the permeability constant, has the value

4p $ 10 %7 T )m/A % 1.26 $ 10 %6 T )m/A.

current, use a right-hand rule to determine the direction of
the field vector.

29.06 Identify that around a long straight wire carrying cur-

rent, the magnetic field lines form circles.

29.07 For a point to one side of the end of a semi-infinite wire

carrying current, apply the relationship between the magnetic
field magnitude, the current, and the distance to the point.
29.08 For the center of curvature of a circular arc of wire car-
rying current, apply the relationship between the magnetic
field magnitude, the current, the radius of curvature, and
the angle subtended by the arc (in radians).

29.09 For a point to one side of a short straight wire carrying
current, integrate the Biot–Savart law to find the magnetic
field set up at the point by the current.

● For a long straight wire carrying a current i, the Biot–Savart
law gives, for the magnitude of the magnetic field at a perpen-
dicular distance R from the wire,

B !

m 0 i
2pR

(long straight wire).

● The magnitude of the magnetic field at the center of a circular
arc, of radius R and central angle f (in radians), carrying current
i, is

B !

m 0 if
4pR

(at center of circular arc).

What Is Physics?
One  basic  observation  of  physics  is  that  a  moving  charged  particle  produces  a
magnetic field around itself. Thus a current of moving charged particles produces
a magnetic field around the current. This feature of  electromagnetism, which is
the  combined  study  of  electric  and  magnetic  effects, came  as  a  surprise  to  the
people who discovered it. Surprise or not, this feature has become enormously
important  in  everyday  life  because  it  is  the  basis  of  countless  electromagnetic
devices. For  example, a  magnetic  field  is  produced  in  maglev  trains  and  other
devices used to lift heavy loads.

Our first step in this chapter is to find the magnetic field due to the current in
a  very  small  section  of  current-carrying  wire. Then  we  shall  find  the  magnetic
field due to the entire wire for several different arrangements of the wire.

836

29-1 MAG N ETIC  FI E LD  DU E  TO  A  CU R R E NT

837

:
B

Calculating the Magnetic Field Due to a Current
Figure 29-1 shows a wire of arbitrary shape carrying a current i. We want to find
at a nearby point P. We first mentally divide the wire into
the magnetic field
differential elements ds and then define for each element a length vector
that
has length ds and whose direction is the direction of the current in ds. We can
then define a differential current-length element to be i
; we wish to calculate
produced at P by a typical current-length element. From experiment
the field
we find that magnetic fields, like electric fields, can be superimposed to find a net
at P by summing, via integration, the
field. Thus, we can calculate the net field
from all the current-length elements. However, this summation
contributions
is  more  challenging  than  the  process  associated  with  electric  fields  because  of
a complexity; whereas a charge element dq producing an electric field is a scalar,
a current-length element i
producing a magnetic field is a vector, being the
product of a scalar and a vector.

:
dB

:
dB

ds:

ds:

ds:

:
B

Magnitude. The magnitude of the field

produced at point P at distance r

by a current-length element i

ds:

:
dB
turns out to be

This element of current creates a
magnetic field at P, into the page.

ids

ds

θ

ˆr

r

d B (into
page)

P

i

Current
distribution

Figure 29-1 A current-length element i
produces a differential magnetic field
$
point P. The green
at the dot for point P indicates that
directed into the page there.

at
(the tail of an arrow)

ds:
:
dB

:
dB

is

dB !

m 0
4p

i ds sin u
r2

,

(29-1)

where u is the angle between the directions of
and  , a unit vector that points
from ds toward P. Symbol  m 0 is  a  constant, called  the  permeability  constant,
whose value is defined to be exactly

ds:

rˆ

m 0 ! 4p $ 10 %7 T )m/A % 1.26 $ 10 %6 T )m/A.

(29-2)

Direction. The direction of
ds: $ rˆ

that of the cross product

:
dB
, shown as being into the page in Fig. 29-1, is
. We can therefore write Eq. 29-1 in vector form as

:
dB

!

m 0
4p

i ds: $ rˆ
r2

(Biot – Savart law).

(29-3)

This vector equation and its scalar form, Eq. 29-1, are known as the law of Biot
and  Savart (rhymes  with “Leo  and  bazaar”). The  law, which  is  experimentally
deduced, is  an  inverse-square  law. We  shall  use  this  law  to  calculate  the  net
magnetic field  produced at a point by various distributions of current.

:
B

Here is one easy distribution: If current in a wire is either directly toward or
directly away from a point P of measurement, can you see from Eq. 29-1 that the
magnetic field at P from the current is simply zero (the angle u is either 0" for to-
ward or 180° for away, and both result in sin u ! 0)?

Magnetic Field Due to a Current in a Long Straight Wire
Shortly we shall use the law of Biot and Savart to prove that the magnitude of the
magnetic field at a perpendicular distance R from a long (infinite) straight wire
carrying a current i is given by

The magnetic field vector
at any point is tangent to
a circle.

Wire with current
into the page

B !

m 0 i
2pR

(long straight wire).

(29-4)

The field magnitude B in Eq. 29-4 depends only on the current and the per-
pendicular distance R of the point from the wire. We shall show in our derivation
form concentric circles around the wire, as Fig. 29-2 shows
that the field lines of

:
B

B

B

Figure 29-2 The magnetic field lines produced by a current in a long straight wire form
concentric circles around the wire. Here the current is into the page, as indicated by the $.

838

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

Courtesy Education Development Center

Figure 29-3 Iron filings that have been sprinkled onto cardboard collect in concentric circles
when current is sent through the central wire.The alignment, which is along magnetic field
lines, is caused by the magnetic field produced by the current.

B

r

Figure 29-4 The magnetic field vector
perpendicular to the radial line extending
from a long straight wire with current, but
which of the two perpendicular vectors is it?

is

:
B

:
B

Figure 29-5 A right-hand rule gives the direc-
tion of the magnetic field due to a current in
a wire. (a) The situation of Fig. 29-2, seen
from the side.The magnetic field  at any
point to the left of the wire is perpendicular
to the dashed radial line and directed into
the page, in the direction of the fingertips, as
indicated by the $. (b) If the current is re-
versed,
at any point to the left is still per-
pendicular to the dashed radial line but now
is directed out of the page, as indicated by
the dot.

:
B

and as the iron filings in Fig. 29-3 suggest. The increase in the spacing of the lines
in Fig. 29-2 with increasing distance from the wire represents the 1/R decrease in
the magnitude of  predicted by Eq. 29-4. The lengths of the two vectors
in the
figure also show the 1/R decrease.

:
B

:
B

:
B

Directions. Plugging values into Eq. 29-4 to find the field magnitude B at a
given radius is easy. What is difficult for many students is finding the direction of
a field vector  at a given point. The field lines form circles around a long straight
wire, and the field vector at any point on a circle must be tangent to the circle.
That means it must be perpendicular to a radial line extending to the point from
the wire. But there are two possible directions for that perpendicular vector, as
shown in Fig. 29-4. One is correct for current into the figure, and the other is cor-
rect for current out of the figure. How can you tell which is which? Here is a sim-
ple right-hand rule for telling which vector is correct:

Curled–straight right-hand rule: Grasp the element in your right hand with your ex-
tended thumb pointing in the direction of the current. Your fingers will then natu-
rally curl around in the direction of the magnetic field lines due to that element.

:
B

The result of applying this right-hand rule to the current in the straight wire
of Fig. 29-2 is shown in a side view in Fig. 29-5a. To determine the direction of the
set up at any particular point by this current, mentally wrap your
magnetic field
right hand around the wire with your thumb in the direction of the current. Let
your fingertips pass through the point; their direction is then the direction of the
at any point is tangent to
magnetic field at that point. In the view of Fig. 29-2,
a magnetic field line; in the view of Fig. 29-5, it is perpendicular to a dashed radial
line connecting the point and the current.

:
B

B

(a )

i

B

(b )

i

The thumb is in the
current’s direction.
The fingers reveal
the field vector’s
direction, which is
tangent to a circle.

29-1 MAG N ETIC  FI E LD  DU E  TO  A  CU R R E NT

839

The direction of
into the page.

:
dB

Proof of Equation 29-4
Figure 29-6, which is just like Fig. 29-1 except that now the wire is straight and of
at point P, a per-
infinite length, illustrates the task at hand. We seek the field
pendicular distance R from the wire. The magnitude of the differential magnetic
field produced at P by the current-length element i
located a distance r from P
is given by Eq. 29-1:

ds:

:
B

dB !

m 0
4p

i ds sin u
r2

.

:
dB

in Fig. 29-6 is that of the vector

ds: $ rˆ

— namely, directly

Note  that

at  point  P has  this  same  direction  for  all  the  current-length
elements into which the wire can be divided. Thus, we can find the magnitude of
the magnetic field produced at P by the current-length elements in the upper half
of the infinitely long wire by integrating dB in Eq. 29-1 from 0 to ..

ds:

Now consider a current-length element in the lower half of the wire, one that
is as far below P as
is above P. By Eq. 29-3, the magnetic field produced at P
by this current-length element has the same magnitude and direction as that from
element i
in Fig. 29-6. Further, the magnetic field produced by the lower half
of the wire is exactly the same as that produced by the upper half. To find the
magnitude of the total magnetic field
at P, we need only multiply the result of
our integration by 2. We get

ds:

:
B

B ! 2".

0

dB !

m 0 i

2p ".

0

sin u ds
r2

.

(29-5)

The variables u, s, and r in this equation are not independent; Fig. 29-6 shows

that they are related by

and

sin u ! sin(p % u) !

r !

s2 & R2

2

R
s2 & R2

.

With these substitutions and integral 19 in Appendix E, Eq. 29-5 becomes

1

B !

!

m 0i

2p ".
m 0i
2pR (

0

R ds
(s2 & R2)3/2
s

(s2 & R2)1/2 )0

.

!

m 0i
2pR

,

(29-6)

as we wanted. Note that the magnetic field at P due to either the lower half or the
upper half of the infinite wire in Fig. 29-6 is half this value; that is,

B !

m 0i
4pR

(semi-infinite straight wire).

(29-7)

Magnetic Field Due to a Current in a Circular Arc of Wire
To find the magnetic field produced at a point by a current in a curved wire, we
would again use Eq. 29-1 to write the magnitude of the field produced by a single
current-length  element, and  we  would  again  integrate  to  find  the  net  field
produced  by  all  the  current-length  elements. That  integration  can  be  difficult,
depending on the shape of the wire; it is fairly straightforward, however, when the
wire is a circular arc and the point is the center of curvature.

Figure 29-7a shows such an arc-shaped wire with central angle f, radius R,
and center C, carrying current i. At C, each current-length element i
of the
wire produces a magnetic field of magnitude dB given by Eq. 29-1. Moreover, as
Fig. 29-7b shows, no matter where the element is located on the wire, the angle u

ds:

This element of current
creates a magnetic field
at P, into the page.

θ

ˆr

r

R

ds

s

i

d B

P

Figure 29-6 Calculating the magnetic field
produced by a current i in a long straight
wire. The field
current-length element i
the page, as shown.

at P associated with the

is directed into

:
dB

ds:

ds

r

ˆr

(b)

R

φ

C

i

C

(a)

B

C

i

(c)

The right-hand rule
reveals the field’s
direction at the center.

Figure 29-7 (a) A wire in the shape of a
circular arc with center C carries current i.
(b) For any element of wire along the arc,
the angle between the directions of
rˆ
is 90°. (c) Determining the direction of
the magnetic field at the center C due to the
current in the wire; the field is out of the
page, in the direction of the fingertips, as
indicated by the colored dot at C.

ds:

and

840

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

rˆ
between the vectors
90° for u in Eq. 29-1, we obtain

and

ds:

is 90°; also, r ! R. Thus, by substituting R for r and

dB !

m 0
4p

i ds sin 90"
R2

!

m 0
4p

i ds
R2 .

(29-8)

The field at C due to each current-length element in the arc has this magnitude.

Directions. How about the direction of the differential field

set up by
an element? From above we know that the vector must be perpendicular to a
radial line extending through point C from the element, either into the plane of
Fig. 29-7a or out of it. To tell which direction is correct, we use the right-hand rule
for any of the elements, as shown in Fig. 29-7c. Grasping the wire with the thumb
in the direction of the current and bringing the fingers into the region near C, we
:
dB
see that the vector
due to any of the differential elements is out of the plane
of the figure, not into it.

:
dB

Total Field. To find the total field at C due to all the elements on the arc,
we need to add all the differential field vectors
. However, because the vectors
are all in the same direction, we do not need to find components. We just sum the
magnitudes dB as given by Eq. 29-8. Since we have a vast number of those magni-
tudes, we sum via integration. We want the result to indicate how the total field
depends on the angle f of the arc (rather than the arc length). So, in Eq. 29-8 we
switch from ds to df by using the identity ds ! R df. The summation by integra-
tion then becomes

:
dB

B ! " dB ! "f

0

m 0
4p

iR df
R2 !

Integrating, we find that

m 0i

4pR "f

0

df.

B !

m0if
4pR

(at center of circular arc).

(29-9)

Heads  Up. Note  that  this  equation  gives  us  the  magnetic  field  only at  the
center  of  curvature  of  a  circular  arc  of  current. When  you  insert  data  into  the
equation, you must be careful to express f in radians rather than degrees. For ex-
ample, to find the magnitude of the magnetic field at the center of a full circle of
current, you would substitute 2p rad for f in Eq. 29-9, finding

B !

m 0i(2p)
4pR

!

m 0i
2R

(at center of full circle).

(29-10)

Sample Problem 29.01 Magnetic field at the center of a circular arc of current

The  wire  in  Fig. 29-8a carries  a  current  i and  consists  of  a
circular  arc  of  radius  R and  central  angle  p/2 rad, and  two
straight  sections  whose  extensions  intersect  the  center  C of
:
B
the  arc. What  magnetic  field
(magnitude  and  direction)
does the current produce at C?

KEY IDEAS

:
B

at point C by applying the
We can find the magnetic field
Biot – Savart law of Eq. 29-3 to the wire, point by point along
the  full  length  of  the  wire. However, the  application  of
Eq. 29-3 can be simplified by evaluating
separately for the
three  distinguishable  sections  of  the  wire — namely, (1)  the

:
B

straight section at the left, (2) the straight section at the right,
and (3) the circular arc.

Straight  sections: For  any  current-length  element
section 1, the angle u between
so Eq. 29-1 gives us

in
is zero (Fig. 29-8b);

and

ds:

rˆ

dB1 !

m 0
4p

i ds sin u
r2

!

m 0
4p

i ds sin 0
r2

! 0.

Thus, the current along the entire length of straight section 1
contributes no magnetic field at C:

B1 ! 0.

29-1 MAG N ETIC  FI E LD  DU E  TO  A  CU R R E NT

841

Current directly toward or
away from C does not
create any field there.

i

1

i

3

R

i

2

d s

ˆr

r

(a )

C

(b )

C

(c )

C

i

B3

Figure 29-8 (a) A wire consists of two straight sections
(1 and 2) and a circular arc (3), and carries current i.
(b) For a current-length element in section 1, the an-
and  is zero. (c) Determining the di-
gle between
at C due to the current in
rection of magnetic field
the circular arc; the field is into the page there.

:
B
3

ds:

rˆ

The same situation prevails in straight section 2, where
and  for any current-length element

ds:

rˆ

the angle u between
is 180°. Thus,

B2 ! 0.

Circular arc: Application of the Biot – Savart law to evalu-
ate the magnetic field at the center of a circular arc leads to
Eq. 29-9 (B ! m0if/4pR). Here the central angle f of the arc
is p/2 rad.Thus from Eq. 29-9, the magnitude of the magnetic
field

at the arc’s center C is

:
B

3

B3 !

m 0i(p/2)
4pR

!

m 0i
8R

.

To find the direction of

:
B
, we apply the right-hand rule
3
displayed  in  Fig. 29-5. Mentally  grasp  the  circular  arc  with
your  right  hand  as  in  Fig. 29-8c, with  your  thumb  in  the

direction of the current. The direction in which your fingers
curl around the wire indicates the direction of the magnetic
field  lines  around  the  wire. They  form  circles  around  the
wire, coming out of the page above the arc and going into
the page inside the arc. In the region of point C (inside the
:
arc), your fingertips point into the plane of the page. Thus,
B
is directed into that plane.

3

Net field: Generally, we combine multiple magnetic fields as
vectors. Here, however, only  the  circular  arc  produces  a
magnetic field at point C. Thus, we can write the magnitude
of the net field  as

:
B

B ! B1 & B2 & B3 ! 0 & 0 &

m 0i
8R

!

m 0i
8R

.

(Answer)

The direction of
plane of Fig. 29-8.

:
B

:
B
is the direction of  — namely, into the
3

Sample Problem 29.02 Magnetic field off to the side of two long straight currents

Figure 29-9a shows two long parallel wires carrying currents
i1 and i2 in opposite directions. What are the magnitude and
direction of the net magnetic field at point P? Assume the
following values: i1 ! 15 A, i2 ! 32 A, and d ! 5.3 cm.

KEY IDEAS

:
B

at point P is the vector sum of
(1) The net magnetic field
the magnetic fields due to the currents in the two wires. (2)
We can find the magnetic field due to any current by apply-
ing the Biot – Savart law to the current. For points near the
current in a long straight wire, that law leads to Eq. 29-4.

P

d

(a)

R

i2

R

i1

The two currents create
magnetic fields that must
be added as vectors to get
the net field.

y

B

B1

φ

45°

45°

P

d

(b)

i2

i1

B2

x

Finding  the  vectors: In  Fig. 29-9a, point  P is  distance  R
from  both  currents  i1 and i2. Thus, Eq. 29-4  tells  us  that  at
:
point P those  currents  produce  magnetic  fields
B
2
with magnitudes

and

:
B
1

Figure 29-9 (a) Two wires carry currents i1 and i2 in opposite directions
(out of and into the page). Note the right angle at P. (b) The separate
fields

are combined vectorially to yield the net field

and

:
.B

:
B
1

:
B
2

B1 !

m 0i1
2pR

    and    B2 !

m 0i2
2pR

.

cos 45° ! R/d and replace R with d cos 45°. Then the field
magnitudes B1 and B2 become

In the right triangle of Fig. 29-9a, note that the base angles
(between sides R and d) are both 45°. This allows us to write

B1 !

m 0i1
2pd cos 45"

    and    B2 !

m 0i2
2pd cos 45"

.
