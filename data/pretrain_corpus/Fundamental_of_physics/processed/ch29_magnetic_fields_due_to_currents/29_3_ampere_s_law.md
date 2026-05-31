844

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

29-3 AMPERE’S LAW

Learning Objectives
After reading this module, you should be able to . . .

29.13 Apply Ampere’s law to a loop that encircles current.
29.14 With Ampere’s law, use a right-hand rule for determin-

ing the algebraic sign of an encircled current.

29.15 For more than one current within an Amperian loop, de-

termine the net current to be used in Ampere’s law.

29.16 Apply Ampere’s law to a long straight wire with current,
to find the magnetic field magnitude inside and outside the
wire, identifying that only the current encircled by the
Amperian loop matters.

Key Idea
● Ampere’s law states that

:

, B

! ds: ! m 0 ienc

(Ampere’s law).

The line integral in this equation is evaluated around a closed loop called an Amperian loop. The current i on the right side is the
net current encircled by the loop.

Ampere’s Law
We can find the net electric field due to any distribution of charges by first writ-
ing the differential electric field
due to a charge element and then summing
the  contributions  of
from  all  the  elements. However, if  the  distribution  is
complicated, we may have to use a computer. Recall, however, that if the distribu-
tion  has  planar, cylindrical, or  spherical  symmetry, we  can  apply  Gauss’  law  to
find the net electric field with considerably less effort.

:
dE

:
dE

Similarly, we can find the net magnetic field due to any distribution of currents
:
dB
(Eq. 29-3) due to a current-length
by first writing the differential magnetic field
:
dB
element and then summing the contributions of
from all the elements.Again we
may have to use a computer for a complicated distribution. However, if the distri-
bution has some symmetry, we may be able to apply Ampere’s law to find the mag-
netic field with considerably less effort. This law, which can be derived from the
Biot – Savart  law, has  traditionally  been  credited  to  André-Marie  Ampère
(1775 – 1836), for whom the SI unit of current is named. However, the law actually
was advanced by English physicist James Clerk Maxwell. Ampere’s law is

:

, B

! ds: ! m0ienc

(Ampere’s law).

(29-14)

:
B

The loop on the integral sign means that the scalar (dot) product
is to be
integrated around a closed loop, called an Amperian loop. The current ienc is the
net current encircled by that closed loop.

! ds:

! ds:

To see the meaning of the scalar product

and its integral, let us first apply
Ampere’s law to the general situation of Fig. 29-12. The figure shows cross sections
of three long straight wires that carry currents i1, i2, and i3 either directly into
or directly out of the page. An arbitrary Amperian loop lying in the plane of
the page encircles two of the currents but not the third. The counterclockwise
direction marked on the loop indicates the arbitrarily chosen direction of inte-
gration for Eq. 29-14.

:
B

ds:

To apply Ampere’s law, we mentally divide the loop into differential vec-
that are everywhere directed along the tangent to the loop in
tor elements
ds:
the  direction  of  integration. Assume  that  at  the  location  of  the  element
:
B
shown  in  Fig. 29-12, the  net  magnetic  field  due  to  the  three  currents  is
.
Because the wires are perpendicular to the page, we know that the magnetic

29-3 AM PE R E’S  L AW

845

ds:

ds:

due to each current is in the plane of Fig. 29-12; thus, their net mag-
field at
:
B
netic field  at  must also be in that plane. However, we do not know the ori-
:
is arbitrarily drawn at an angle u
B
entation of  within the plane. In Fig. 29-12,
:
ds:
B
to the direction of
on the left side of Eq. 29-14 is
equal to B cos u ds. Thus, Ampere’s law can be written as

. The scalar product

:
B
! ds:

:

, B

! ds: ! , B cos u ds ! m0ienc.

(29-15)

:
as being the product of a length ds
B
We can now interpret the scalar product
of the Amperian loop and the field component B cos u tangent to the loop. Then
we  can  interpret  the  integration  as  being  the  summation  of  all  such  products
around the entire loop.

! ds:

Amperian
loop

i 3

Only the currents
encircled by the
loop are used in
Ampere’s law.

i 2

i 1

ds

θ

B

Direction of
integration

Signs. When  we  can  actually  perform  this  integration, we  do  not  need  to
know the direction of  before integrating. Instead, we arbitrarily assume
to be
generally in the direction of integration (as in Fig. 29-12). Then we use the follow-
ing curled – straight right-hand rule to assign a plus sign or a minus sign to each of
the currents that make up the net encircled current ienc:

:
B

:
B

Curl your right hand around the Amperian loop, with the fingers pointing in the
direction of integration. A current through the loop in the general direction of your
outstretched thumb is assigned a plus sign, and a current generally in the opposite
direction is assigned a minus sign.

Finally, we solve Eq. 29-15 for the magnitude of
the direction we assumed for
minus sign and redraw

in the opposite direction.

:
B

:
B

. If B turns out positive, then
is correct. If it turns out negative, we neglect the

:
B

Figure 29-12 Ampere’s law applied to an
arbitrary Amperian loop that encircles two
long straight wires but excludes a third
wire. Note the directions of the currents.

This is how to assign a
sign to a current used in
Ampere’s law.

+i 1

–i 2

Direction of
integration

Net Current. In Fig. 29-13 we apply the curled – straight right-hand rule for
Ampere’s law to the situation of Fig. 29-12. With the indicated counterclockwise
direction of integration, the net current encircled by the loop is

(Current i3 is not encircled by the loop.) We can then rewrite Eq. 29-15 as

ienc ! i1 % i2.

, B cos u ds ! m0(i1 % i2).

Figure 29-13 A right-hand rule for Ampere’s
law, to determine the signs for currents
encircled by an Amperian loop. The situa-
tion is that of Fig. 29-12.

(29-16)

You  might  wonder  why, since  current  i3 contributes  to  the  magnetic-field  mag-
nitude B on the left side of Eq. 29-16, it is not needed on the right side. The answer
is that the contributions of current i3 to the magnetic field cancel out because the
integration in Eq. 29-16 is made around the full loop. In contrast, the contributions
of an encircled current to the magnetic field do not cancel out.

We cannot solve Eq. 29-16 for the magnitude B of the magnetic field because for
the situation of Fig. 29-12 we do not have enough information to simplify and solve
the integral. However, we do know the outcome of the integration; it must be equal to
m0(i1 % i2), the value of which is set by the net current passing through the loop.

We shall now apply Ampere’s law to two situations in which symmetry does

allow us to simplify and solve the integral, hence to find the magnetic field.

Magnetic Field Outside a Long Straight Wire with Current
Figure  29-14  shows  a  long  straight  wire  that  carries  current  i directly  out  of  the
page. Equation 29-4 tells us that the magnetic field  produced by the current has
the same magnitude at all points that are the same distance r from the wire; that is,
the field  has cylindrical symmetry about the wire. We can take advantage of that
symmetry to simplify the integral in Ampere’s law (Eqs. 29-14 and 29-15) if we en-
circle the wire with a concentric circular Amperian loop of radius r, as in Fig. 29-14.
The magnetic field  then has the same magnitude B at every point on the loop. We
ds:
shall integrate counterclockwise, so that

has the direction shown in Fig. 29-14.

:
B

:
B

All of the current is
encircled and thus all
is used in Ampere’s law.

Wire
surface

r

i

Amperian
loop

B

(   = 0)
θ

ds

Figure 29-14 Using Ampere’s law to find the
magnetic field that a current i produces
outside a long straight wire of circular cross
section. The Amperian loop is a concentric
circle that lies outside the wire.

846

CHAPTE R  29 MAG N ETIC  FI E LDS  DU E  TO  CU R R E NTS

We can further simplify the quantity B cos u in Eq. 29-15 by noting that
ds:

:
B
is
are
tangent  to  the  loop  at  every  point  along  the  loop, as  is
either parallel or antiparallel at each point of the loop, and we shall arbitrarily
assume the former. Then at every point the angle u between
is 0°, so
cos u ! cos 0° ! 1. The integral in Eq. 29-15 then becomes

. Thus,

and

and

ds:

ds:

:
B

:
B

:

, B

! ds: ! , B cos u ds ! B, ds ! B(2pr).

Note  that  - ds is  the  summation  of  all  the  line  segment  lengths  ds around  the
circular loop; that is, it simply gives the circumference 2pr of the loop.

Our right-hand rule gives us a plus sign for the current of Fig. 29-14. The right

side of Ampere’s law becomes &m0i, and we then have

B(2pr) ! m0i

or

B !

m0i
2pr

(outside straight wire).

(29-17)

With a slight change in notation, this is Eq. 29-4, which we derived earlier — with
considerably more effort — using the law of Biot and Savart. In addition, because
:
B
the  magnitude  B turned  out  positive, we  know  that  the  correct  direction  of
must be the one shown in Fig. 29-14.

Magnetic Field Inside a Long Straight Wire with Current
Figure  29-15  shows  the  cross  section  of  a  long  straight  wire  of  radius  R that
carries  a  uniformly  distributed  current  i directly  out  of  the  page. Because  the
current  is  uniformly  distributed  over  a  cross  section  of  the  wire, the  magnetic
field  produced by the current must be cylindrically symmetrical. Thus, to find
the magnetic field at points inside the wire, we can again use an Amperian loop of
:
radius r, as shown in Fig. 29-15, where now r + R. Symmetry again suggests that
B
is tangent to the loop, as shown; so the left side of Ampere’s law again yields

:
B

:

, B

! ds: ! B, ds ! B(2pr).

(29-18)

Only the current encircled
by the loop is used in
Ampere’s law.

Wire
surface

ds

B

r

R

i

Amperian
loop

Because the current is uniformly distributed, the current ienc encircled by the loop
is proportional to the area encircled by the loop; that is,

Figure 29-15 Using Ampere’s law to find the
magnetic field that a current i produces in-
side a long straight wire of circular cross
section. The current is uniformly distrib-
uted over the cross section of the wire and
emerges from the page. An Amperian loop
is drawn inside the wire.

ienc ! i

p r2
pR2 .

(29-19)

Our right-hand rule tells us that ienc gets a plus sign. Then Ampere’s law gives us

B(2pr) ! m0i

p r2
pR2

or

B ! # m0i

2pR2 $ r

(inside straight wire).

(29-20)

Thus, inside the wire, the magnitude B of the magnetic field is proportional to r ,
is zero at the center, and is maximum at r ! R (the surface). Note that Eqs. 29-17
and 29-20 give the same value for B at the surface.

Checkpoint 2

The figure here shows three equal currents i (two parallel
and one antiparallel) and four Amperian loops. Rank the
along each,
loops according to the magnitude of
greatest first.

:
- B

! ds:

i

i

a

b

d

c

i

29-3 AM PE R E’S  L AW

847

Sample Problem 29.03 Ampere’s law to find the field inside a long cylinder of current

Figure  29-16a shows  the  cross  section  of  a  long  conducting
cylinder  with  inner  radius  a ! 2.0 cm  and  outer  radius
b ! 4.0 cm. The cylinder carries a current out of the page, and
the  magnitude  of  the  current  density  in  the  cross  section  is
given  by  J ! cr2, with  c ! 3.0 $ 10 6 A/m4 and r in  meters.
:
B
What is the magnetic field  at the dot in Fig. 29-16a, which is
at radius r ! 3.0 cm from the central axis of the cylinder?

Next, we must compute the current ienc that is encircled
by the Amperian loop. However, we cannot set up a propor-
tionality as in Eq. 29-19, because here the current is not uni-
formly  distributed. Instead, we  must  integrate  the  current
density magnitude from the cylinder’s inner radius a to the
loop radius r, using the steps shown in Figs. 29-16c through h.

Calculations: We write the integral as

KEY IDEAS

:
B

The point at which we want to evaluate
is inside the mate-
rial of the conducting cylinder, between its inner and outer
radii. We  note  that  the  current  distribution  has  cylindrical
symmetry (it is the same all around the cross section for any
given radius). Thus, the symmetry allows us to use Ampere’s
at the point. We first draw the Amperian loop
law to find
shown in Fig. 29-16b. The loop is concentric with the cylin-
der and has radius r ! 3.0 cm because we want to evaluate
:
B

at that distance from the cylinder’s central axis.

:
B

ienc ! " J dA ! "r
! 2pc"r

a

a

cr2(2p r dr)

r 3 dr ! 2pc ( r 4
4 )a

r

!

pc(r 4 % a4)
2

.

Note that in these steps we took the differential area dA to
be  the  area  of  the  thin  ring  in  Figs. 29-16d–f and  then

We want the
magnetic field at
the dot at radius r.

So, we put a concentric
Amperian loop through
the dot.

We need to find the
current in the area
encircled by the loop.

r

a

b

Amperian
loop

r

We start with a ring
that is so thin that
we can approximate
the current density as
being uniform within it.

A

(a)

(b)

(c)

(d)

Its area dA is the
product of the ring’s
circumference
and the width dr.

The current within the
ring is the product of
the current density J
and the ring’s area dA.

Our job is to sum
the currents in all
rings from this
smallest one ...

... to this largest
one, which has the
same radius as the
Amperian loop.

dr

dA

( f )

(e)

a

r

(g )

(h)

Figure 29-16 (a)–(b) To find the magnetic field at a point within this conducting cylinder, we use a concentric Amperian
loop through the point.We then need the current encircled by the loop. (c)–(h) Because the current density is nonuni-
form, we start with a thin ring and then sum (via integration) the currents in all such rings in the encircled area.
