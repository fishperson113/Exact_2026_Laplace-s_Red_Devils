29-5 A  CU R R E NT-CAR RYI NG  COI L  AS  A  MAG N ETIC  DI POLE

851

Sample Problem 29.04 The field inside a solenoid (a long coil of current)

A  solenoid  has  length  L ! 1.23 m  and  inner  diameter
d ! 3.55 cm, and it carries a current i ! 5.57 A. It consists of
five close-packed layers, each with 850 turns along length L.
What is B at its center?

KEY IDEA

The magnitude B of the magnetic field along the solenoid’s
central axis is related to the solenoid’s current i and number
of turns per unit length n by Eq. 29-23 (B ! m0 in).

Calculation: Because B does not depend on the diameter of
the windings, the value of n for five identical layers is simply
five times the value for each layer. Equation 29-23 then tells us

B ! m0 in ! (4p $ 10 %7 T )m /A)(5.57 A)

5 $ 850 turns
1.23 m

! 2.42 $ 10 %2 T ! 24.2 mT.

(Answer)

To a good approximation, this is the field magnitude through-
out most of the solenoid.

Additional examples, video, and practice available at WileyPLUS

29-5 A CURRENT-CARRYING COIL AS A MAGNETIC DIPOLE

Learning Objectives

After reading this module, you should be able to . . .

29.22 Sketch the magnetic field lines of a flat coil that is

current i, number of turns N, and area per turn A.

carrying current.

29.23 For a current-carrying coil, apply the relationship be-
tween the dipole moment magnitude m and the coil’s

29.24 For a point along the central axis, apply the relationship
between the magnetic field magnitude B, the magnetic
moment m, and the distance z from the center of the coil.

Key Idea
● The magnetic field produced by a current-carrying coil, which is a magnetic dipole, at a point P located a distance z along the
coil’s perpendicular central axis is parallel to the axis and is given by

where

m:

is the dipole moment of the coil. This equation applies only when z is much greater than the dimensions of the coil.

:
B

(z) !

m 0
2p

m:
z3 ,

A Current-Carrying Coil as a Magnetic Dipole
So  far  we  have  examined  the  magnetic  fields  produced  by  current  in  a  long
straight  wire, a  solenoid, and  a  toroid. We  turn  our  attention  here  to  the  field
produced by a coil carrying a current. You saw in Module 28-8 that such a coil
:
B
behaves as a magnetic dipole in that, if we place it in an external magnetic field
,
t:
a torque  given by

:
t: ! m: $ B

(29-25)

m:

acts on it. Here
is the magnetic dipole moment of the coil and has the magni-
tude NiA, where N is the number of turns, i is the current in each turn, and A is
the  area  enclosed  by  each  turn. (Caution: Don’t  confuse  the  magnetic  dipole
moment  with the permeability constant m0.)

m:

Recall that the direction of

is given by a curled – straight right-hand rule:
Grasp the coil so that the fingers of your right hand curl around it in the direction
of  the  current; your  extended  thumb  then  points  in  the  direction  of  the  dipole
moment

.m:

m:

852

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

i

N

µµ

S

i

B

Figure 29-22 A current loop produces a magnetic field like that of a bar magnet and thus has
associated north and south poles.The magnetic dipole moment  of the loop, its direction
given by a curled – straight right-hand rule, points from the south pole to the north pole, in
the direction of the field  within the loop.

:
B

m:

Magnetic Field of a Coil
We turn now to the other aspect of a current-carrying coil as a magnetic dipole.
What magnetic field does it produce at a point in the surrounding space? The
problem does not have enough symmetry to make Ampere’s law useful; so we
must turn to the law of Biot and Savart. For simplicity, we first consider only a
coil with a single circular loop and only points on its perpendicular central axis,
which we take to be a z axis. We shall show that the magnitude of the magnetic
field at such points is

B(z) !

m 0 iR2
2(R2 & z2)3/2 ,

(29-26)

in which R is the radius of the circular loop and z is the distance of the point in
question  from  the  center  of  the  loop. Furthermore, the  direction  of  the  mag-
netic field
is the same as the direction of the magnetic dipole moment  of
the loop.

:
B

m:

Large z. For axial points far from the loop, we have z R in Eq. 29-26. With

/

that approximation, the equation reduces to

B(z) %

m 0iR2
2z3

.

Recalling that pR2 is the area A of the loop and extending our result to include
a coil of N turns, we can write this equation as

B(z) !

m 0
2p

NiA
z3

.

Further, because
vector form, substituting from the identity

and  have the same direction, we can write the equation in
NiA:

m !

m:

:
B

:
B

(z) !

m0
2p

m:
z3

(current-carrying coil).

(29-27)

Thus, we have two ways in which we can regard a current-carrying coil as a
magnetic  dipole: (1)  it  experiences  a  torque  when  we  place  it  in  an  external
magnetic field; (2) it generates its own intrinsic magnetic field, given, for dis-
tant points along its axis, by Eq. 29-27. Figure 29-22 shows the magnetic field of
a current loop; one side of the loop acts as a north pole (in the direction of  )m:

29-5 A  CU R R E NT-CAR RYI NG  COI L  AS  A  MAG N ETIC  DI POLE

853

and the other side as a south pole, as suggested by the lightly drawn magnet in
the figure. If we were to place a current-carrying coil in an external magnetic
field, it would tend to rotate just like a bar magnet would.

Checkpoint 3

The figure here shows four arrangements of circular loops of radius r or 2r, centered
on vertical axes (perpendicular to the loops) and carrying identical currents in the di-
rections indicated. Rank the arrangements according to the magnitude of the net
magnetic field at the dot, midway between the loops on the central axis, greatest first.

(a)

(b)

(c)

(d)

d B

d B

⊥

d B<

α

P

r

z

The perpendicular
components
just cancel. We add
only the parallel
components.

ˆr

α

ds

R

Figure 29-23 Cross section through a current
loop of radius R. The plane of the loop is
perpendicular to the page, and only the
back half of the loop is shown. We use the
law of Biot and Savart to find the magnetic
field at point P on the central perpendicu-
lar axis of the loop.

Proof of Equation 29-26
Figure 29-23 shows the back half of a circular loop of radius R carrying a current
i. Consider a point P on the central axis of the loop, a distance z from its plane.
Let us apply the law of Biot and Savart to a differential element ds of the loop,
for this element points
located at the left side of the loop. The length vector
rˆ
perpendicularly out of the page. The angle u between
and
in Fig. 29-23 is 90°;
the plane formed by these two vectors is perpendicular to the plane of the page
ds:.
and contains both  and
From the law of Biot and Savart (and the right-hand
:
produced at point P by the current in this element
dB
rule), the differential field
is  perpendicular  to  this  plane  and  thus  is  directed  in  the  plane  of  the  figure,
perpendicular to  , as indicated in Fig. 29-23.
:
dB

rˆ
into two components: dB, along the axis of the loop and
Let us resolve
perpendicular to this axis. From the symmetry, the vector sum of all the per-
due to all the loop elements ds is zero. This leaves

dB"
dB"
pendicular components
only the axial (parallel) components dB, and we have

ds:
ds:

rˆ

B ! " dB,.

For the element

ds:

in Fig. 29-23, the law of Biot and Savart (Eq. 29-1) tells us

that the magnetic field at distance r is

We also have

dB !

m 0
4p

i ds sin 90"
r2

.

dB, ! dB cos a.

Combining these two relations, we obtain

dB, !

m 0 i cos a ds
4pr2

.

(29-28)

Figure 29-23 shows that r and a are related to each other. Let us express each in
terms of the variable z, the distance between point P and the center of the loop.
The relations are

r !

R2 & z2

2

(29-29)

854

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

and

cos a !

R
r

!

R
R2 & z2

.

(29-30)

Substituting Eqs. 29-29 and 29-30 into Eq. 29-28, we find

1

dB, !

m 0iR
4p(R2 & z2)3/2 ds.

Note that i, R, and z have the same values for all elements ds around the loop; so
when we integrate this equation, we find that

B ! " dB,

!

m 0 iR

4p(R2 & z2)3/2 " ds

or, because

" ds

is simply the circumference 2pR of the loop,

B(z) !

m 0iR2
2(R2 & z2)3/2 .

This is Eq. 29-26, the relation we sought to prove.

Review & Summary

The Biot–Savart Law The magnetic field set up by a current-
carrying  conductor  can  be  found  from  the  Biot – Savart  law. This
to  the  field  produced  by  a
law  asserts  that  the  contribution
at a point P located a distance r from
current-length element
the current element is

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

(29-3)

rˆ

is a unit vector that points from the element toward P. The

Here
quantity m0, called the permeability constant, has the value

4p $ 10 %7 T )m/A % 1.26 $ 10 %6 T )m/A.

Magnetic  Field  of  a  Long  Straight  Wire For  a  long
straight wire carrying a current i, the Biot – Savart law gives, for the
magnitude  of  the  magnetic  field  at  a  perpendicular  distance  R
from the wire,

B !

m 0 i
2pR

(long straight wire).

(29-4)

Magnetic  Field  of  a  Circular  Arc The  magnitude  of  the
magnetic field at the center of a circular arc, of radius R and central
angle f (in radians), carrying current i, is

B !

m 0 if
4pR

(at center of circular arc).

(29-9)

Ampere’s Law Ampere’s law states that

:

, B

! ds: ! m 0 ienc

(Ampere’s law).

(29-14)

The line integral in this equation is evaluated around a closed loop
called an Amperian loop. The current i on the right side is the net
current  encircled  by  the  loop. For  some  current  distributions,
Eq. 29-14 is easier to use than Eq. 29-3 to calculate the magnetic
field due to the currents.

Fields of a Solenoid and a Toroid Inside a long solenoid
carrying current i, at points not near its ends, the magnitude B of
the magnetic field is

B ! m 0in

(ideal solenoid),

(29-23)

where n is the number of turns per unit length. Thus the internal
magnetic field is uniform. Outside the solenoid, the magnetic field
is approximately zero.

At  a  point  inside  a  toroid, the  magnitude  B of  the  magnetic

field is

B !

m 0 iN
2p

1
r

(toroid),

(29-24)

where r is the distance from the center of the toroid to the point.

Force  Between  Parallel  Currents Parallel  wires  carrying
currents in the same direction attract each other, whereas parallel
wires carrying currents in opposite directions repel each other. The
magnitude of the force on a length L of either wire is

Field of a Magnetic Dipole The magnetic field produced by
a current-carrying coil, which is a magnetic dipole, at a point P lo-
cated a distance z along the coil’s perpendicular central axis is par-
allel to the axis and is given by

Fba ! ibLBa sin 90" !

m 0Liaib
2pd

,

(29-13)

where d is the wire separation, and ia and ib are the currents in the
wires.

m:
z3 ,
is  the  dipole  moment  of  the  coil. This  equation  applies

where
only when z is much greater than the dimensions of the coil.

(29-27)

m 0
2p

(z) !

:
B

m:

Questions

1 Figure 29-24 shows three circuits, each consisting of two radial
lengths  and  two  concentric  circular  arcs, one  of  radius  r and  the
other of radius R , r. The circuits have the same current through
them and the same angle between the two radial lengths. Rank the
circuits according to the magnitude of the net magnetic field at the
center, greatest first.

(a)

(b)

(c)

Figure 29-24 Question 1.

2 Figure  29-25  represents  a  snap-
shot  of  the  velocity  vectors  of  four
electrons  near  a  wire  carrying  cur-
rent i. The  four  velocities  have  the
same  magnitude; velocity
is  di-
rected into the page. Electrons 1 and
2 are at the same distance from the
wire, as are electrons 3 and 4. Rank
the electrons according to the mag-
nitudes  of  the  magnetic  forces  on
them due to current i, greatest first.

n:

2

i

v1

v2

v3

v4

Figure 29-25 Question 2.

3 Figure 29-26 shows four arrangements in which long parallel wires
carry equal currents directly into or out of the page at the corners of
identical squares. Rank the arrangements according to the magnitude
of the net magnetic field at the center of the square, greatest first.

(a)

(b)

(c)

(d)

Figure 29-26 Question 3.

4 Figure 29-27 shows cross sections
of  two  long  straight  wires; the  left-
hand  wire  carries  current  i1 directly
out  of  the page. If  the  net  magnetic
field due to the two currents is to be zero at point P, (a) should the
direction of current i2 in the right-hand wire be directly into or out of
the page and (b) should i2 be greater than, less than, or equal to i1?

Figure 29-27 Question 4.

P

i1

i2

5 Figure 29-28 shows three circuits consisting of straight radial
lengths and concentric circular arcs (either half- or quarter-circles

(a)

(b)

(c)

Figure 29-28 Question 5.

QU ESTIONS

855

of  radii  r, 2r, and  3r). The  circuits  carry  the  same  current. Rank
them according to the magnitude of the magnetic field produced at
the center of curvature (the dot), greatest first.

6 Figure 29-29 gives, as a function of radial distance r, the magni-
tude B of the magnetic field inside and outside four wires (a, b, c, and
d), each of which carries a current that is uniformly distributed across
the  wire’s  cross  section. Overlapping  portions  of  the  plots  (drawn
slightly separated) are indicated by double labels. Rank the wires ac-
cording to (a) radius, (b) the magnitude of the magnetic field on the
surface, and (c) the value of the current, greatest first. (d) Is the mag-
nitude of the current density in wire a greater than, less than, or equal
to that in wire c?

B

a, b

c, d

a

b

c

r

a, c

b, d

Figure 29-29 Question 6.

7 Figure  29-30  shows  four  circular
Amperian  loops  (a, b, c, d )  concentric
with  a  wire  whose  current  is  directed
out of the page. The current is uniform
across  the  wire’s  circular  cross  section
(the shaded region). Rank the loops ac-
! ds:
cording  to  the  magnitude  of
around each, greatest first.

:
- B

a

b

c

d

Figure 29-30 Question 7.

8 Figure 29-31 shows four arrangements in which long, parallel,
equally spaced wires carry equal currents directly into or out of the
page. Rank  the  arrangements  according  to  the  magnitude  of  the
net force on the central wire due to the currents in the other wires,
greatest first.

(a)

(b)

(c)

(d)

Figure 29-31 Question 8.

9 Figure  29-32  shows  four  circu-
lar Amperian loops (a, b, c, d) and,
in  cross  section, four  long  circular
conductors  (the  shaded  regions),
all  of  which  are  concentric. Three
of the conductors are hollow cylin-
ders; the  central  conductor  is  a
solid  cylinder. The  currents  in  the
conductors  are,
smallest
radius to largest radius, 4 A out of

from

a

b

c

d

Figure 29-32 Question 9.

856

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

the page, 9 A into the page, 5 A out of the page, and 3 A into the
page. Rank  the  Amperian  loops  according  to  the  magnitude  of
:
- B

around each, greatest first.

! ds:

10 Figure 29-33 shows four identical currents i and five Amperian
paths (a through e) encircling them. Rank the paths according to the
value of

taken in the directions shown, most positive first.

! ds:

:
- B

i

i

i

(a)

(b)

(c)

(d)

(e)

i

Figure 29-33 Question 10.

Problems

11 Figure 29-34 shows three arrangements of three long straight
wires  carrying  equal  currents  directly  into  or  out  of  the  page.
(a) Rank the arrangements according to the magnitude of the net
force on wire A due to the currents in the other wires, greatest first.
(b) In arrangement 3, is the angle between the net force on wire A
and the dashed line equal to, less than, or more than 45°?

D

d

A

d

D

A

(1)

(2)

A

d

D

(3)

Figure 29-34 Question 11.

Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign

SSM Worked-out solution available in Student Solutions Manual
• – ••• Number of dots indicates level of problem difficulty

WWW Worked-out solution is at

ILW Interactive solution is at

http://www.wiley.com/college/halliday

Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com

Module 29-1 Magnetic Field Due to a Current
•1 A surveyor is using a magnetic
compass  6.1 m  below  a power  line
in which there is a steady current of
100  A. (a) What  is  the  magnetic
field at the site of the compass due
to the power line? (b) Will this field
interfere  seriously  with  the com-
pass reading? The horizontal com-
ponent of Earth’s magnetic field at
the site is 20 mT.

θ

ds

dBs

Wire

(a)

0

π

π

(b)

:
dB

)
T
p
(
B
d

/2
θ  (rad)

•2 Figure  29-35a shows  an  ele-
ment  of  length  ds ! 1.00 mm  in  a
very  long  straight  wire  carrying
current. The  current  in  that  ele-
ment  sets  up  a  differential  mag-
netic  field
at  points  in  the
surrounding  space. Figure  29-35b
gives the magnitude dB of the field
for points 2.5 cm from the element,
as a function of angle u between the wire and a straight line to the
point. The vertical scale is set by dBs ! 60.0 pT. What is the magni-
tude of the magnetic field set up by the entire wire at perpendicular
distance 2.5 cm from the wire?
At a certain location in the Philippines, Earth’s magnetic
•3
field  of  39 mT  is  horizontal  and  directed  due  north. Suppose  the
net  field  is  zero  exactly  8.0 cm  above  a  long, straight, horizontal
wire  that  carries  a  constant  current. What  are  the  (a)  magnitude
and (b) direction of the current?

Figure 29-35 Problem 2.

SSM

•4 A straight conductor carrying cur-
rent i ! 5.0 A splits into identical semi-
circular  arcs  as  shown  in  Fig. 29-36.
What is the magnetic field at the center
C of the resulting circular loop?
•5 In Fig. 29-37, a current i ! 10 A
is set up in a long hairpin conductor
formed  by  bending  a  wire  into  a
semicircle of radius R ! 5.0 mm. Point
b is midway between the straight sec-
tions and so distant from the semicir-
cle  that  each  straight  section  can  be
approximated  as  being  an  infinite
wire. What are the (a) magnitude and
(b) direction (into or out of the page)
at  a and  the  (c)  magnitude  and
of
(d) direction of  at b?

:
B

:
B

i

i

C

Figure 29-36 Problem 4.

R
a

i

b

Figure 29-37 Problem 5.

•6 In Fig. 29-38, point P is at perpendicular distance R ! 2.00 cm
from a very long straight wire carrying a current. The magnetic field
:
set up at point P is due to contributions from all the identical cur-
B
along the wire. What is the distance s to the
rent-length elements i

ds:

P

R

s

Wire

Figure 29-38 Problem 6.

element making (a) the greatest contribution to field  and (b) 10.0%
of the greatest contribution?

:
B

current i ! 58.2 mA. (Note  that  the  wire  is  not long.) What  is  the
magnitude of the magnetic field at P1 due to i?

PROB LE M S

857

In  Fig. 29-39, two  circular
•7
arcs have  radii  a ! 13.5 cm  and b !
subtend  angle  u ! 74.0°,
10.7 cm,
carry  current  i ! 0.411  A, and  share
the same center of curvature P. What
are  the  (a)  magnitude  and  (b)  direc-
tion  (into  or  out  of  the  page)  of  the
net magnetic field at P?

•8 In  Fig. 29-40, two  semicircular
arcs  have  radii  R2 ! 7.80 cm  and
R1 ! 3.15 cm, carry current i ! 0.281
A, and have the same center of cur-
vature C. What are the (a) magnitude
and (b) direction (into or out of the
page) of the net magnetic field at C?

a

i

i

b

θ

P

Figure 29-39 Problem 7.

R2

i

i

R1

C

SSM

Two  long  straight  wires
•9
are parallel and 8.0 cm apart. They
are to carry equal currents such that the magnetic field at a point
halfway  between  them  has  magnitude  300 mT. (a) Should  the
currents  be  in  the  same  or  opposite  directions?  (b)  How  much
current is needed?

Figure 29-40 Problem 8.

i

•10 In Fig. 29-41, a wire forms a semi-
circle  of  radius  R ! 9.26 cm  and  two
(radial)  straight  segments  each  of
length L ! 13.1 cm. The  wire  carries
current i ! 34.8 mA. What  are  the  (a)
magnitude  and  (b)  direction  (into  or
out of the page) of the net magnetic field at the semicircle’s cen-
ter of curvature C?

Figure 29-41 Problem 10.

R

C

L

L

i

•11 In  Fig. 29-42, two  long  straight
wires are perpendicular to the page and
separated  by  distance  d1 ! 0.75 cm.
Wire 1 carries 6.5 A into the page. What
are the (a) magnitude and (b) direction
(into or out of the page) of the current
in wire 2 if the net magnetic field due to
the  two  currents  is  zero  at  point  P lo-
cated  at  distance  d2 ! 1.50 cm  from
wire 2?

•12 In  Fig. 29-43, two  long  straight
wires  at  separation d ! 16.0 cm  carry
currents i1 ! 3.61 mA  and  i2 ! 3.00i1
out of the page. (a) Where on the x axis
is the net magnetic field equal to zero?
(b)  If  the  two  currents  are  doubled, is
the zero-field point shifted toward wire
1, shifted toward wire 2, or unchanged?

Wire 1

Wire 2

d1

d2

P

Figure 29-42 Problem 11.

y

i 1

i 2

x

d

Figure 29-43 Problem 12.

••13 In Fig. 29-44, point P1 is at distance R ! 13.1 cm on the per-
pendicular bisector of a straight wire of length L ! 18.0 cm carrying

Figure 29-44 Problems 13 and 17.

P 2

R

P 1

R

L

i

••14 Equation 29-4 gives the magnitude B of the magnetic field
set up by a current in an infinitely long straight wire, at a point P
at perpendicular distance R from the wire. Suppose that point P
is  actually  at  perpendicular  distance  R from  the  midpoint  of  a
wire with a finite length L. Using Eq. 29-4 to calculate B then re-
sults  in  a  certain  percentage  error. What  value  must  the  ratio
L/R exceed if the percentage error is to be less than 1.00%? That
is, what L/R gives

(B from Eq. 29-4) % (B actual)
(B actual)

 (100%) ! 1.00%?

θ

i2

••15 Figure  29-45  shows  two  cur-
rent  segments. The  lower  segment
carries a current of i1 ! 0.40 A and
includes  a  semicircular  arc  with
radius 5.0 cm, angle 180°, and center
point P. The  upper  segment  carries
current i2 ! 2i1 and includes a circu-
lar arc with radius 4.0 cm, angle 120°,
and  the  same  center  point  P. What
:
B
are the (a) magnitude and (b) direction of the net magnetic field
at P for the indicated current directions? What are the (c) magni-
tude and (d) direction of

Figure 29-45 Problem 15.

if i1 is reversed?

:
B

i1

P

In Fig. 29-46, two concen-
••16
tric  circular  loops  of  wire  carrying
current  in  the  same  direction  lie  in
the  same  plane. Loop  1  has  radius
1.50 cm and carries 4.00 mA. Loop 2
has  radius  2.50 cm  and  carries  6.00
mA. Loop 2 is to be rotated about a diameter while the net mag-
netic  field
set  up  by  the  two  loops  at  their  common  center  is
measured. Through what angle must loop 2 be rotated so that the
magnitude of that net field is 100 nT?

Figure 29-46 Problem 16.

:
B

1

2

SSM

In Fig. 29-44, point P2 is at perpendicular distance R !
••17
25.1 cm from one end of a straight wire of length L ! 13.6 cm car-
rying current i ! 0.693 A. (Note that the wire is not long.) What is
the magnitude of the magnetic field at P2?

••18 A  current  is  set  up  in  a  wire
loop consisting of a semicircle of ra-
dius  4.00 cm, a  smaller  concentric
semicircle, and  two  radial  straight
lengths, all in the same plane. Figure
29-47a shows the arrangement but is
not  drawn  to  scale. The  magnitude
of  the  magnetic  field  produced  at
the center of curvature is 47.25 mT. The smaller semicircle is then
flipped over (rotated) until the loop is again entirely in the same
plane (Fig. 29-47b). The magnetic field produced at the (same) cen-
ter of curvature now has magnitude 15.75 mT, and its direction is
reversed from the initial magnetic field. What is the radius of the
smaller semicircle?

Figure 29-47 Problem 18.

(a)

(b)

••19 One long wire lies along an x axis and carries a current of 30
A in the positive x direction. A second long wire is perpendicular to
the xy plane, passes through the point (0, 4.0 m, 0), and carries a cur-
rent of 40 A in the positive z direction. What is the magnitude of the
resulting magnetic field at the point (0, 2.0 m, 0)?

858

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

carrying

••20 In Fig. 29-48, part of a long in-
current
sulated  wire
i ! 5.78 mA  is  bent  into  a  circular
section  of  radius  R ! 1.89 cm. In
unit-vector  notation, what  is  the
magnetic field at the center of curva-
ture C if the circular section (a) lies
in  the  plane  of  the  page  as  shown
and (b) is perpendicular to the plane
of  the  page  after  being  rotated  90°
counterclockwise as indicated?

Figure  29-49  shows  two
••21
very long straight wires (in cross sec-
tion)  that  each  carry  a  current  of
4.00 A  directly  out  of  the page.
Distance d1 ! 6.00 m  and  distance
d2 ! 4.00 m. What  is  the  magnitude
of the net magnetic field at point P,
which lies on a perpendicular bisec-
tor to the wires?

y

i

x

i

i

C

P

Figure 29-48 Problem 20.

d1

d2

P

Figure 29-49 Problem 21.

Figure 29-50a shows, in cross section, two long, parallel
••22
wires carrying current and separated by distance L. The ratio i1/i2
of their currents is 4.00; the directions of the currents are not indi-
cated. Figure 29-50b shows the y component By of their net mag-
netic field along the x axis to the right of wire 2. The vertical scale is
set by Bys ! 4.0 nT, and the horizontal scale is set by xs ! 20.0 cm.
(a) At what value of x , 0 is By maximum? (b) If i2 ! 3 mA, what is
the value of that maximum? What is the direction (into or out of the
page) of (c) i1 and (d) i2?

must you move wire 3 along the x axis to rotate  by 30° back to its
initial orientation?

:
B

SSM

A  wire  with  current
••25
i ! 3.00 A  is  shown  in  Fig. 29-53. Two
semi-infinite straight sections, both tan-
gent  to  the  same  circle, are  connected
by a circular arc that has a central angle
u and runs along the circumference of
the circle. The arc and the two straight
sections all lie in the same plane. If B !
0 at the circle’s center, what is u?

R

θ

i

i

Connecting arc

Figure 29-53
Problem 25.

In Fig. 29-54a, wire 1 consists of a circular arc and two
••26
it  carries  current  i1 ! 0.50 A  in  the  direction
radial  lengths;
indicated. Wire 2, shown in cross section, is long, straight, and per-
pendicular to the plane of the figure. Its distance from the center of
the arc is equal to the radius R of the arc, and it carries a current i2
that can be varied. The two currents set up a net magnetic field
at
the center of the arc. Figure 29-54b gives the square of the field’s
magnitude B2 plotted versus the square of the current
. The verti-
What angle is subtended by
cal scale is set by
the arc?

2 ! 10.0 $ 10%10 T2.

Bs

:
B

2
i2

)
2
T
0
1
–

0
1
(

2
B

2
Bs

0

i1

i2

R

(a)

2

1
2 (A2)
i 2

(b)

y

1

2

x

L

(a)

Bys

)
T
n
(

y

B

0

0

–Bys

Figure 29-50 Problem 22.

ILW

Figure  29-51  shows  a  snap-
••23
shot  of  a  proton  moving  at  velocity
(%200 m/s)jˆ
v: !
toward a long straight
wire  with  current  i
350 mA. At  the
instant  shown, the  proton’s  distance
from  the  wire  is  d ! 2.89 cm. In  unit-
vector  notation, what  is  the  magnetic
force on the proton due to the current?

!

xs

Figure 29-54 Problem 26.

x (cm)

(b)

y

d

v

i

x

Figure 29-51 Problem 23.

••27 In Fig. 29-55, two long straight
wires  (shown  in  cross  section)  carry
the  currents  i1 ! 30.0 mA  and  i2 !
40.0 mA  directly  out  of  the  page.
They  are  equal  distances  from  the
origin, where they set up a magnetic
. To what value must current i1
field
be changed in order to rotate
20.0°
clockwise?

:
B

:
B

y

i1

i2

x

Figure 29-55 Problem 27.

••28
wires, each carrying a current. Wire 1 consists of a circular arc of

Figure  29-56a shows  two

i1

Figure 29-52 shows, in cross
••24
section, four thin wires that are paral-
lel, straight, and very long. They carry
identical  currents  in  the  directions  in-
dicated. Initially  all  four  wires  are  at
distance d ! 15.0 cm  from  the  origin
of  the  coordinate  system, where  they
. (a)  To
create  a  net  magnetic  field
what  value  of  x must  you  move  wire  1
:
B
along  the  x axis  in  order  to  rotate
counterclockwise by 30°? (b) With wire
1 in that new position, to what value of x

:
B

y

4

d

d

2

d

1

d

3

x

Figure 29-52
Problem 24.

R

i2

B

0

i 2s

R__
2

(a)

i 2 (A)

(b)

Figure 29-56 Problem 28.

radius R and two radial lengths; it carries current i1 ! 2.0 A in the
direction indicated. Wire 2 is long and straight; it carries a current i2
that can be varied; and it is at distance R/2 from the center of the
arc. The net magnetic field  due to the two currents is measured
at  the  center  of  curvature  of  the  arc. Figure  29-56b is  a  plot  of
the component of
in the direction perpendicular to the figure as
a function of current i2. The horizontal scale is set by i2s ! 1.00 A.
What is the angle subtended by the arc?

:
B

:
B

SSM

In Fig. 29-57, four long straight wires are perpendicular
••29
to the page, and their cross sections form a square of edge length
a ! 20 cm. The currents are out of the page in wires 1 and 4 and
into  the  page  in  wires  2  and  3, and  each  wire  carries  20 A. In
unit-vector  notation, what  is  the  net  magnetic  field  at  the
square’s center?

1

a

y

a

2

a

4

a

3

x

Figure 29-57 Problems 29, 37, and 40.

Two long straight thin wires with current lie against an
•••30
equally long plastic cylinder, at radius R ! 20.0 cm from the cylin-
der’s central axis. Figure 29-58a shows, in cross section, the cylinder
and wire 1 but not wire 2. With wire 2 fixed in place, wire 1 is moved
around the cylinder, from angle u1 ! 0° to angle u1 ! 180°, through
the first and second quadrants of the xy coordinate system. The net
at  the  center  of  the  cylinder  is  measured  as  a
magnetic  field
function of u1. Figure 29-58b gives the x component Bx of that field
as a function of u1 (the vertical scale is set by Bxs ! 6.0 mT), and Fig.
29-58c gives the y component By (the vertical scale is set by Bys ! 4.0
mT). (a) At what angle u2 is wire 2 located? What are the (b) size and
(c) direction (into or out of the page) of the current in wire 1 and the
(d) size and (e) direction of the current in wire 2?

:
B

Wire 1

θ
1

x

y

(a)

Bys

)
T
µ
(

y

B

0

Bxs

)
T
µ
(

x
B

0
0°

90°
θ 1

(b)

180°

–Bys

0°

180°

90°
θ 1

(c)

Figure 29-58 Problem 30.

PROB LE M S

859

•••31 In  Fig. 29-59, length  a is  4.7 cm
(short)  and  current  i is  13 A. What  are
the  (a)  magnitude  and  (b)  direction
(into or out of the page) of the magnetic
field at point P?

a

a

P

i

2a

The  current-carrying  wire
•••32
loop  in  Fig. 29-60a lies  all  in one  plane
and consists of a semicircle of radius 10.0
cm, a smaller  semicircle  with  the  same
center, and  two  radial  lengths. The
smaller semicircle is rotated out of that
plane by angle u, until it is perpendicular
to the plane (Fig. 29-60b). Figure 29-60c gives the magnitude of the
net magnetic field at the center of curvature versus angle u. The
vertical scale is set by Ba ! 10.0 mT and Bb ! 12.0 mT. What is
the radius of the smaller semicircle?

Figure 29-59 Problem 31.

a

y

y

(a)

(b)

z

z

Bb

)
T
µ
(
B

Ba

0

x

x

Figure 29-60 Problem 32.

  /2 π

  /4 π
 (rad)

θ

(c)

ILW

SSM

Figure 29-61 shows
•••33
a cross section of a long thin ribbon
of width w ! 4.91 cm that is carrying
a  uniformly  distributed  total  current
i ! 4.61 mA into the page. In unit-vec-
tor  notation, what  is  the  magnetic
field  at a point P in the plane of the
ribbon at a distance d ! 2.16 cm from
its edge? (Hint: Imagine the ribbon as
being  constructed  from  many  long,
thin, parallel wires.)

:
B

Figure  29-62  shows,

in
•••34
cross  section, two  long  straight  wires
held  against  a  plastic  cylinder  of  ra-
dius  20.0 cm. Wire  1  carries  current
i1 ! 60.0 mA  out  of  the  page  and  is
fixed  in  place  at  the  left  side  of  the
cylinder. Wire  2  carries  current  i2 !
40.0 mA  out  of  the  page  and  can  be
moved  around  the  cylinder. At  what
(positive)  angle  u2 should  wire  2  be
positioned  such  that, at  the  origin,
the net magnetic field due to the two
currents has magnitude 80.0 nT?

Module  29-2 Force  Between
Two Parallel Currents
Figure 29-63 shows wire
•35
1  in  cross  section; the  wire  is  long

SSM

y

P

x

d

w

Figure 29-61 Problem 33.

y

Wire 2

2θ

x

Wire 1

Figure 29-62 Problem 34.

y

1

d1

2

x

d 2

Figure 29-63 Problem 35.

860

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

and straight, carries a current of 4.00 mA out of the page, and is
at distance d1 ! 2.40 cm from a surface. Wire 2, which is parallel
to  wire  1  and  also  long, is  at  horizontal  distance  d2 ! 5.00 cm
from wire 1 and carries a current of 6.80 mA into the page. What
is the x component of the magnetic force per unit length on wire
2 due to wire 1?

z

2

1

••36 In Fig. 29-64, five long parallel
wires in an xy plane are separated by
distance d ! 8.00 cm, have lengths of
10.0 m, and  carry  identical  currents
of 3.00 A out of the page. Each wire
experiences a magnetic force due to
the  currents  in  the  other  wires. In
unit-vector notation, what is the net
magnetic force on (a) wire 1, (b) wire 2, (c) wire 3, (d) wire 4, and (e)
wire 5?

Figure 29-64 Problems 36
and 39.

3

5

4

d

d

d

d

y

In Fig. 29-57, four long straight wires are perpendicular
••37
to the page, and their cross sections form a square of edge length
a ! 13.5 cm. Each wire carries 7.50 A, and the currents are out of
the page in wires 1 and 4 and into the page in wires 2 and 3. In unit-
vector  notation, what  is  the  net  magnetic  force per  meter  of  wire
length on wire 4?

Figure  29-65a shows, in  cross  section, three  current-
••38
carrying wires that are long, straight, and parallel to one another.
Wires  1  and  2  are  fixed  in  place  on  an  x axis, with  separation  d.
Wire 1 has a current of 0.750 A, but the direction of the current is
not given. Wire 3, with a current of 0.250 A out of the page, can be
moved along the x axis to the right of wire 2. As wire 3 is moved,
on wire 2 due to the
the magnitude of the net magnetic force
currents in wires 1 and 3 changes. The x component of that force is
F2x and the value per unit length of wire 2 is F2x/L2. Figure 29-65b
gives F2x/L2 versus the position x of wire 3. The plot has an asymp-
tote F2x/L2 ! %0.627 mN/m as x : .. The horizontal scale is set by
xs ! 12.0 cm. What are the (a) size and (b) direction (into or out of
the page) of the current in wire 2?

:
F
2

y

1

2

3

x

d

(a)

)
m
/
N
µ
(

2
L
/
x
2
F

1.0

0.5

0

0

–0.5

xs

x (cm)

(b)

Figure 29-65 Problem 38.

In Fig. 29-64, five long parallel wires in an xy plane are
••39
separated  by  distance  d ! 50.0 cm. The  currents  into  the  page
are i1 ! 2.00 A,
i5 ! 2.00 A;
the current out of the page is i2 ! 4.00 A. What is the magnitude
of the net force per unit length acting on wire 3 due to the cur-
rents in the other wires?

i4 ! 4.00 A, and

i3 ! 0.250 A,

••40 In  Fig. 29-57, four  long  straight  wires  are  perpendicular  to
the  page, and  their  cross  sections  form  a  square  of  edge  length
a ! 8.50 cm. Each wire carries 15.0 A, and all the currents are out of
the page. In unit-vector notation, what is the net magnetic force per
meter of wire length on wire 1?

ILW

In  Fig. 29-66, a  long
•••41
straight  wire  carries  a  current  i1 !
30.0 A  and  a  rectangular  loop  car-
ries current i2 ! 20.0 A. Take the di-
mensions  to  be  a ! 1.00 cm, b !
8.00 cm, and  L ! 30.0 cm. In  unit-
vector notation, what is the net force
on the loop due to i1?

a

b

i1

y

x

i2

L

Module 29-3 Ampere’s Law
•42 In a particular region there is
a  uniform  current  density  of  15
A /m2 in  the  positive  z direction.
What is the value of
when that line integral is calculated
along  a  closed  path  consisting  of  the  three  straight-line  seg-
ments from (x, y, z) coordinates (4d, 0, 0) to
(4d, 3d, 0) to (0, 0, 0) to (4d, 0, 0), where d !
20 cm?

Figure 29-66 Problem 41.

:
- B

! ds:

a

r

•43 Figure  29-67  shows  a  cross  section
across  a  diameter  of  a  long  cylindrical  con-
ductor of radius a ! 2.00 cm carrying uniform
current 170 A. What is the magnitude of the
current’s magnetic field at radial distance (a)
0, (b)  1.00 cm, (c)  2.00 cm  (wire’s  surface),
and (d) 4.00 cm?
i1

•44 Figure 29-68 shows two closed
paths wrapped around two conduct-
ing loops carrying currents i1 ! 5.0 A
and i2 ! 3.0 A. What is the value of
:
- B
the  integral
for  (a)  path
1 and (b) path 2?

! ds:

Figure 29-67
Problem 43.

i2

1

2

Figure 29-68 Problem 44.

SSM

Each of the eight conductors in Fig. 29-69 carries 2.0 A of
•45
current into or out of the page. Two paths are indicated for the line
:
- B
integral
. What is the value of the integral for (a) path 1 and
(b) path 2?

! ds:

1

2

Figure 29-69 Problem 45.

•46 Eight wires cut the page per-
pendicularly at the points shown in
Fig. 29-70. A wire labeled with the
integer k (k ! 1, 2, . . . , 8)  carries
the current ki, where i ! 4.50 mA.
For those wires with odd k, the cur-
rent  is  out  of  the  page; for  those
with  even  k, it  is  into  the  page.
Evaluate
along  the  closed
path indicated and in the direction
shown.

:
- B

! ds:

3

4

2

6

8

5

7

1

Figure 29-70 Problem 46.

ILW

The current density

••47
side a long, solid, cylindrical wire of radius a
3.1 mm is in the di-
rection  of  the  central  axis, and  its  magnitude  varies  linearly  with
radial  distance  r from  the  axis  according  to  J ! J0r/a, where  J0 !

in-

!

:
J

310 A/m2. Find the magnitude of the mag-
netic  field  at  (a)  r ! 0, (b)  r ! a/2, and
(c) r ! a.

current

••48 In  Fig. 29-71, a  long  circular  pipe
with  outside  radius  R ! 2.6 cm  carries  a
i !
distributed)
(uniformly
8.00 mA into the page. A wire runs parallel
to the pipe at a distance of 3.00R from cen-
ter  to  center. Find  the  (a)  magnitude  and
(b) direction (into or out of the page) of the
current in the wire such that the net mag-
netic field at point P has the same magni-
tude as the net magnetic field at the center
of the pipe but is in the opposite direction.

Wire

P

R

R

R

Pipe

Figure 29-71
Problem 48.

Module 29-4 Solenoids and Toroids
•49 A toroid having a square cross section, 5.00 cm on a side, and
an inner radius of 15.0 cm has 500 turns and carries a current of 0.800
A. (It is made up of a square solenoid — instead of a round one as in
Fig. 29-17—bent into a doughnut shape.) What is the magnetic field
inside the toroid at (a) the inner radius and (b) the outer radius?

•50 A solenoid that is 95.0 cm long has a radius of 2.00 cm and
a winding of 1200 turns; it carries a current of 3.60 A. Calculate
the magnitude of the magnetic field inside the solenoid.

•51 A 200-turn solenoid having a length of 25 cm and a diameter
of 10 cm carries a current of 0.29 A. Calculate the magnitude of the
magnetic field

inside the solenoid.

:
B

•52 A solenoid 1.30 m long and 2.60 cm in diameter carries a cur-
rent  of  18.0 A. The  magnetic  field  inside  the  solenoid  is  23.0 mT.
Find the length of the wire forming the solenoid.

••53 A long solenoid has 100 turns/cm and carries current i. An
electron  moves  within  the  solenoid  in  a  circle  of  radius  2.30 cm
perpendicular  to  the  solenoid  axis. The  speed  of  the  electron  is
0.0460c (c ! speed of light). Find the current i in the solenoid.

••54 An  electron  is  shot  into  one  end  of  a  solenoid. As  it
enters the uniform magnetic field within the solenoid, its speed
is 800 m/s and its velocity vector makes an angle of 30° with the
central  axis  of  the  solenoid. The  solenoid  carries  4.0 A  and  has
8000 turns along its length. How many revolutions does the elec-
tron make along its helical path within the solenoid by the time it
emerges  from  the  solenoid’s  opposite  end?  (In  a  real  solenoid,
where the field is not uniform at the two ends, the number of rev-
olutions would be slightly less than the answer here.)

ILW

SSM

WWW

A long solenoid with 10.0 turns/cm and a
••55
radius  of  7.00 cm  carries  a  current  of  20.0 mA. A  current  of  6.00 A
exists in a straight conductor located along the central axis of the sole-
noid. (a) At what radial distance from the axis will the direction of the
resulting  magnetic  field  be  at  45.0° to
the  axial  direction?  (b)  What  is  the
magnitude of the magnetic field there?

y

i

i

Module  29-5 A  Current-Carrying
Coil as a Magnetic Dipole
•56 Figure  29-72  shows  an  arrange-
ment  known  as  a  Helmholtz  coil. It
consists  of  two  circular  coaxial  coils,
each  of  200
radius
R ! 25.0 cm, separated  by  a  distance

turns  and

x

R

P

s

Figure 29-72
Problem 56.

PROB LE M S

861

s ! R. The two coils carry equal currents i ! 12.2 mA in the same di-
rection. Find the magnitude of the net magnetic field at P, midway
between the coils.

SSM

A  student  makes  a  short  electromagnet  by  winding
•57
300 turns of wire around a wooden cylinder of diameter d ! 5.0 cm.
The coil is connected to a battery producing a current of 4.0 A in
the wire. (a) What is the magnitude of the magnetic dipole moment
d will the magnetic
of this device? (b) At what axial distance
field have the magnitude 5.0 mT (approximately one-tenth that of
Earth’s magnetic field)?

z /

•58 Figure  29-73a shows  a  length  of
wire carrying a current i and bent into
a circular coil of one turn. In Fig. 29-
73b the  same  length  of  wire  has  been
bent to give a coil of two turns, each of
half the original radius. (a) If Ba and Bb
are  the  magnitudes  of  the  magnetic
fields  at  the  centers  of  the  two  coils,
what is the ratio Bb/Ba? (b) What is the
ratio mb/ma of the dipole moment mag-
nitudes of the coils?

i

i

(a)

(b)

Figure 29-73 Problem 58.

•59
m:

SSM

What is the magnitude of the magnetic dipole moment

of the solenoid described in Problem 51?

two  circular

In  Fig. 29-74a,

loops, with  different
••60
currents  but  the  same  radius  of  4.0 cm, are  centered  on  a  y axis.
They are initially separated by distance L ! 3.0 cm, with loop 2 po-
sitioned at the origin of the axis. The currents in the two loops pro-
duce a net magnetic field at the origin, with y component By. That
component is to be measured as loop 2 is gradually moved in the
positive direction of the y axis. Figure 29-74b gives By as a function
of the position y of loop 2. The curve approaches an asymptote of
By ! 7.20 mT as y : .. The horizontal scale is set by ys ! 10.0 cm.
What are (a) current i1 in loop 1 and (b) current i2 in loop 2?

2

1

y

0

(a)

)
T
µ
(

y

B

L

20

0

0

–40

ys

y (cm)

(b)

Figure 29-74 Problem 60.

••61 A circular loop of radius 12 cm carries a current of 15 A. A
flat coil of radius 0.82 cm, having 50 turns and a current of 1.3 A, is
concentric with the loop. The plane of the loop is perpendicular to
the  plane  of  the  coil. Assume  the
loop’s  magnetic  field  is  uniform
across  the  coil. What  is  the  magni-
tude  of  (a)  the  magnetic  field
produced  by  the  loop  at  its  center
and  (b)  the  torque  on  the  coil  due
to the loop?

P

b

i

a

••62 In  Fig. 29-75, current  i !
56.2 mA is set up in a loop having
two radial lengths and two semicir-

Figure 29-75 Problem 62.

862

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

cles of radii a ! 5.72 cm and b ! 9.36 cm with a common center
P. What are the (a) magnitude and (b) direction (into or out of
the  page)  of  the  magnetic  field  at  P and  the  (c)  magnitude  and
(d) direction of the loop’s magnetic dipole moment?

••63 In  Fig. 29-76, a  conductor  car-
ries  6.0 A  along  the  closed  path
abcdefgha running  along  8  of  the  12
edges of a cube of edge length 10 cm.
(a) Taking the path to be a combina-
tion  of  three  square  current  loops
(bcfgb, abgha, and cdefc), find the net
magnetic moment of the path in unit-
vector notation. (b) What is the mag-
nitude of the net magnetic field at the
xyz coordinates of (0, 5.0 m, 0)?

Additional Problems
64 In Fig. 29-77, a closed loop carries
current i ! 200 mA. The  loop  consists
of  two  radial  straight  wires  and  two
concentric circular arcs of radii 2.00 m
and 4.00 m.The angle u is p/4 rad.What
are the (a) magnitude and (b) direction
(into  or  out  of  the  page)  of  the  net
the  center  of
magnetic
curvature P?

field  at

y

g

c

h

d

f

x

e

b

z

a

Figure 29-76 Problem 63.

i

P

θ

65 A cylindrical cable of radius 8.00
mm  carries  a  current  of  25.0 A, uni-
formly spread over its cross-sectional area. At what distance from
the  center  of  the  wire  is  there  a  point  within  the  wire  where  the
magnetic field magnitude is 0.100 mT?

Figure 29-77 Problem 64.

66 Two long wires lie in an xy plane, and each carries a current in
the positive direction of the x axis. Wire 1 is at y ! 10.0 cm and car-
ries 6.00 A; wire 2 is at y ! 5.00 cm and carries 10.0 A. (a) In unit-
vector notation, what is the net magnetic field
at the origin? (b)
! 0
At what value of y does
? (c) If the current in wire 1 is re-
:
versed, at what value of y does
B

! 0

:
B

:
B

?

67 Two  wires, both  of  length L, are  formed  into  a  circle  and  a
square, and each carries current i. Show that the square produces a
greater magnetic field at its center than the circle produces at its
center.

68 A  long  straight  wire  carries  a  current  of  50 A. An  electron,
traveling at 1.0 $ 10 7 m/s, is 5.0 cm from the wire. What is the mag-
nitude of the magnetic force on the electron if the electron velocity
is directed (a) toward the wire, (b) parallel to the wire in the direc-
tion of the current, and (c) perpendicular to the two directions de-
fined by (a) and (b)?

a

69 Three long wires are parallel to
a z axis, and each carries a current of
10 A in the positive z direction. Their
points  of  intersection  with  the  xy
plane  form  an  equilateral  triangle
with sides of 50 cm, as shown in Fig.
29-78. A fourth wire (wire b) passes
through the midpoint of the base of
the  triangle  and  is  parallel  to  the
other three wires. If the net magnetic
force on wire a is zero, what are the
(a) size and (b) direction (&z or %z) of the current in wire b?

b

Figure 29-78 Problem 69.

y

x

i

70 Figure 29-79 shows a closed loop
with current i ! 2.00 A. The loop con-
sists  of  a  half-circle  of  radius  4.00 m,
two quarter-circles each of radius 2.00
m, and  three  radial  straight  wires.
What is the magnitude of the net mag-
netic field at the common center of the
circular sections?

71 A  10-gauge  bare  copper  wire
(2.6 mm in diameter) can carry a current of 50 A without overheat-
ing. For this current, what is the magnitude of the magnetic field at
the surface of the wire?

Figure 29-79 Problem 70.

72 A long vertical wire carries an unknown current. Coaxial with
the wire is a long, thin, cylindrical conducting surface that carries a
current of 30 mA upward. The cylindrical surface has a radius of
3.0 mm. If the magnitude of the magnetic field at a point 5.0 mm
from the wire is 1.0 mT, what are the (a) size and (b) direction of
the current in the wire?

73 Figure  29-80  shows  a  cross  section  of  a
long cylindrical conductor of radius a ! 4.00 cm
containing  a  long  cylindrical  hole  of  radius
b ! 1.50 cm. The central axes of the cylinder
and  hole  are  parallel  and  are  distance  d !
2.00 cm apart; current i ! 5.25 A is uniformly
distributed  over  the  tinted  area. (a) What  is
the  magnitude  of  the  magnetic  field  at  the
center of the hole? (b) Discuss the two spe-
cial cases b ! 0 and d ! 0.

a

b

d

Figure 29-80
Problem 73.

74 The magnitude of the magnetic field at a point 88.0 cm from
the central axis of a long straight wire is 7.30 mT. What is the cur-
rent in the wire?

z

∆s

:
B

SSM

!’
s

Figure  29-81  shows  a  wire
75
segment  of  length
3.0 cm, cen-
tered  at  the  origin, carrying  current
i ! 2.0 A in the positive y direction (as
part of some complete circuit). To cal-
culate  the  magnitude  of  the  magnetic
field
produced  by  the  segment  at  a
point  several  meters  from  the  origin,
we can use B ! (m0/4p)i ’s (sin u)/r2 as
the Biot–Savart law. This is because r
and u are essentially constant over the
(in unit-vector notation) at the (x, y, z) coor-
segment. Calculate
dinates (a) (0, 0, 5.0 m), (b) (0, 6.0 m, 0), (c) (7.0 m, 7.0 m, 0), and (d)
(%3.0 m, %4.0 m, 0).

Figure 29-81 Problem 75.

:
B

x

y

i

Figure  29-82  shows, in  cross  section, two  long  parallel
76
wires spaced by distance d
10.0 cm; each carries 100 A, out of the
page in wire 1. Point P is on a perpendicular bisector of the line con-
necting the wires. In unit-vector notation, what is the net magnetic
field at P if the current in wire 2 is (a) out of the page and (b) into the
page?

!

x

y

1

P

d

2

Figure 29-82 Problem 76.

77 In Fig. 29-83, two infinitely long wires
carry equal currents i. Each follows a 90°
arc on the circumference of the same cir-
cle  of  radius  R. Show  that  the  magnetic
at  the  center  of  the  circle  is  the
field
a distance R below an
same as the field
infinite  straight  wire  carrying  a  current  i
to the left.

:
B

:
B

R

i

i

78 A  long  wire  carrying  100 A  is  per-
pendicular to the magnetic field lines of
a  uniform  magnetic  field  of  magnitude
5.0 mT. At  what  distance  from  the  wire  is  the  net  magnetic  field
equal to zero?

Figure 29-83
Problem 77.

79 A long, hollow, cylindrical conductor (with inner radius 2.0
mm  and  outer  radius  4.0 mm)  carries  a  current  of  24 A  distrib-
uted uniformly across its cross section. A long thin wire that is co-
axial with the cylinder carries a current of 24 A in the opposite
direction. What is the magnitude of the magnetic field (a) 1.0 mm,
(b) 3.0 mm, and (c) 5.0 mm from the central axis of the wire and
cylinder?

80 A long wire is known to have a radius greater than 4.0 mm and
to carry a current that is uniformly distributed over its cross section.
The magnitude of the magnetic field due to that current is 0.28 mT
at a point 4.0 mm from the axis of the wire, and 0.20 mT at a point 10
mm from the axis of the wire.What is the radius of the wire?

B

SSM

Figure 29-84 shows a cross
81
section  of  an  infinite  conducting
sheet  carrying  a  current  per  unit
x-length  of  l; the  current  emerges
perpendicularly  out  of  the  page. (a)
Use  the  Biot – Savart  law  and  sym-
metry  to  show  that  for  all  points  P
above the sheet and all points P( be-
low it, the magnetic field
shown. (b)  Use  Ampere’s  law  to  prove  that
(
points P and P .

:
B

P

B

P'

x

Figure 29-84 Problem 81.

is parallel to the sheet and directed as
at  all

B ! 1

2 m 0 l

PROB LE M S

863

ter wire is 3.2 A (a) in the positive x direction and (b) in the nega-
tive x direction?

SSM

Figure 29-87 shows a cross section
85
of  a  hollow  cylindrical  conductor  of  radii  a
and b, carrying  a  uniformly  distributed  cur-
rent i. (a) Show that the magnetic field magni-
tude B(r) for the radial distance r in the range
b + r + a is given by

B !

m 0 i
2p(a2 % b2)

r2 % b2
r

.

a

b

r

Figure 29-87
Problem 85.

(b) Show that when r ! a, this equation gives
the  magnetic  field  magnitude  B at  the  surface  of  a  long  straight
wire  carrying  current  i; when  r ! b, it  gives  zero  magnetic  field;
and when  b ! 0,
it  gives  the  magnetic  field  inside  a  solid
conductor of radius a carrying current i. (c) Assume that a ! 2.0
cm, b ! 1.8 cm, and  i ! 100 A, and  then  plot  B(r)  for  the  range
0 + r + 6 cm.

86 Show  that  the  magnitude  of  the  magnetic  field  produced  at
the center of a rectangular loop of wire of length L and width W,
carrying a current i, is

B !

2m 0i
p

(L2 & W2)1/2
LW

.

87 Figure  29-88  shows  a  cross  section  of  a
long  conducting  coaxial  cable  and  gives  its
radii (a, b, c). Equal but opposite currents i are
uniformly  distributed  in  the  two  conductors.
Derive  expressions  for  B(r)  with  radial  dis-
tance r in the ranges (a) r + c, (b) c + r + b, (c)
b + r + a, and (d) r , a. (e) Test these expres-
sions for all the special cases that occur to you.
(f)  Assume  that  a ! 2.0 cm, b ! 1.8 cm, c !
0.40 cm, and  i ! 120 A  and  plot  the  function
B(r) over the range 0 + r + 3 cm.

a

b

c

r

Figure 29-88
Problem 87.

82 Figure 29-85 shows, in cross sec-
tion, two long parallel wires that are
separated  by  distance  d ! 18.6 cm.
Each  carries  4.23 A, out of  the  page
in wire 1 and into the page in wire 2.
In  unit-vector  notation, what  is  the
net  magnetic  field  at  point  P at  dis-
tance R ! 34.2 cm, due  to  the  two
currents?

SSM

In  unit-vector  notation,
83
what  is  the  magnetic  field  at  point
P in  Fig. 29-86  if  i ! 10 A  and  a !
8.0 cm?  (Note  that  the  wires  are
not long.)

84 Three long wires all lie in an xy
plane parallel to the x axis. They are
spaced equally, 10 cm apart. The two
outer  wires  each  carry  a  current  of
5.0 A  in  the  positive  x direction.
What  is  the  magnitude  of  the  force
on  a  3.0 m  section  of  either of  the
outer wires if the current in the cen-

y

1

2

d1__
2

1__
2

d

a/4

a/4

P

y

x

a

88 Figure 29-89 is an idealized schematic drawing of a rail gun.
Projectile P sits between two wide rails of circular cross section; a
source of current sends current through the rails and through the
(conducting) projectile (a fuse is not used). (a) Let w be the dis-
tance between the rails, R the radius of each rail, and i the current.
Show that the force on the projectile is directed to the right along
the rails and is given approximately by

P

x

R

Figure 29-85 Problem 82.

F !

i2m 0
2p

 ln

w & R
R

.

(b) If the projectile starts from the left end of the rails at rest, find
the speed v at which it is expelled at the right. Assume that i !
450 kA, w ! 12 mm, R ! 6.7 cm, L ! 4.0 m, and  the  projectile
mass is 10 g.

i

a

Source

L

P

i

i

i

v

R
w

R

Figure 29-86 Problem 83.

Figure 29-89 Problem 88.
