774

CHAPTER 23 Electric Potential

23.5 Potential Gradient

ActivPhysics 11.12.3: Electrical Potential,
Field, and Force

Electric  ﬁeld  and  potential  are  closely  related.  Equation  (23.17),  restated  here,
expresses one aspect of that relationship:

Va - Vb =

b

L
a

S # d l

E

S

S
E

If we know
at various points, we can use this equation to calculate potential
differences. In this section we show how to turn this around; if we know the poten-
tial V at various points, we can use it to determine  Regarding V as a function of
S
E
the coordinates
are related to the partial derivatives of V with respect to

S
.
E
of a point in space, we will show that the components of

1x, y, z2

and

x, y,

z.

In  Eq.  (23.17),

Va - Vb

is  the  potential  of  a with  respect  to  b—that  is,  the

change of potential encountered on a trip from b to  We can write this as

a.

Va - Vb =

a

L
b

dV = -

b

dV

L
a

where
element

SdV
d l

is the inﬁnitesimal change of potential accompanying an inﬁnitesimal

of the path from b to  Comparing to Eq. (23.17), we have

a.

b

dV =

b

L
a

-

L
a

S # d l

E

S

These two integrals must be equal for any pair of limits a and
true the integrands must be equal. Thus, for any inﬁnitesimal displacement

and for this to be

S
,
d l

b,

-dV = E

S # d l

S

S
d l

S
E

To  interpret  this  expression,  we  write
S
E

N
(cid:2) ıN Ex (cid:4) ≥N Ey (cid:4) k

S
d l

Ez

and
N
(cid:2) ıN dx (cid:4) ≥N dy (cid:4) k
dz.
and
-dV = Ex dx + Ey dy + Ez dz

in  terms  of  their  components:

Then we have

Application Potential Gradient
Across a Cell Membrane
The interior of a human cell is at a lower elec-
tric potential V than the exterior. (The potential
difference when the cell is inactive is about
–70 mV in neurons and about –95 mV in skele-
tal muscle cells.) Hence there is a potential
gradient
exterior of the cell membrane, and an electric
that points from the exterior to
ﬁeld
the interior. This ﬁeld affects how ions ﬂow into
or out of the cell through special channels in
the membrane.

that points from the interior to the

S
(cid:2) - §

S
E

S
§

V

V

or

Suppose  the  displacement  is  parallel  to  the  x-axis,  so
-dV = Ex dx
Ex = - 1dV>dx2y, z constant,
only x varies in the derivative; recall that V is in general a function of
this is just what is meant by the partial derivative
S
E

Then
where the subscript reminds us that
x, y,
z.
and  But
The y- and z-components of
are related to the corresponding derivatives of V in the same way, so we have

0V>0x.

dy = dz = 0.

Ex = -

    Ey = -

0V
0x

    Ez = -

0V
0y

0V
0z

(components of
in terms of V)

S
E

(23.19)

This is consistent with the units of electric ﬁeld being
tors we can write

S
E

as

V>m.

In terms of unit vec-

S
E

(cid:2) (cid:3) a ıN

0V
0x

(cid:4) ≥N

0V
0y

(cid:4) k

N 0V
0z

b    1E

S

 in terms of V2

(23.20)

In vector notation the following operation is called the gradient of the func-
tion

ƒ:

S
f (cid:2) a ıN
§

0
0x

(cid:4) ≥N

0
0y

(cid:4) k

N 0
0z

bƒ

(23.21)

The operator denoted by the symbol
notation,

S
§

is called “grad” or “del.” Thus in vector

This is read “
V.” The quantity

is the negative of the gradient of V” or “
S
§
is called the potential gradient.

V

S
E

S
E

S
(cid:2) (cid:3) §

V

(23.22)

S
E

equals negative grad

S
E

At  each  point,  the  potential  gradient  points  in  the  direction  in  which  V
increases most rapidly with a change in position. Hence at each point the direc-
tion of
is the direction in which V decreases most rapidly and is always perpen-
dicular  to  the  equipotential  surface  through  the  point.  This  agrees  with  our
observation  in  Section  23.2  that  moving  in  the  direction  of  the  electric  ﬁeld
means moving in the direction of decreasing potential.

23.5 Potential Gradient

775

Equation (23.22) doesn’t depend on the particular choice of the zero point for
V. If we were to change the zero point, the effect would be to change V at every
point by the same amount; the derivatives of V would be the same.

is radial with respect to a point or an axis and r is the distance from the

S
E

If

point or the axis, the relationship corresponding to Eqs. (23.19) is

Er = -

0V
0r

    1radial electric field2

(23.23)

S
E

Often  we  can  compute  the  electric  ﬁeld  caused  by  a  charge  distribution  in
either of two ways: directly, by adding the  ﬁelds of point charges, or by ﬁrst
calculating the potential and then taking its gradient to ﬁnd the ﬁeld. The second
method is often easier because potential is a scalar quantity, requiring at worst
the integration of a scalar function. Electric ﬁeld is a vector quantity, requiring
computation of components for each element of charge and a separate integra-
tion  for  each  component.  Thus,  quite  apart  from  its  fundamental  signiﬁcance,
potential  offers  a  very  useful  computational  technique  in  ﬁeld  calculations.
Below, we present two examples in which a knowledge of V is used to ﬁnd the
electric ﬁeld.

We stress once more that if we know

as a function of position, we can cal-
culate V using Eq. (23.17) or (23.18), and if we know V as a function of position,
S
we  can  calculate
E
requires integration, and deriving

using  Eq.  (23.19),  (23.20),  or  (23.23).  Deriving  V from

from V requires differentiation.

S
E

S
E

S
E

Example 23.13

Potential and field of a point charge

From Eq. (23.14) the potential at a radial distance
charge
q
expression for

from a point
Find the vector electric ﬁeld from this

V = q>4pP0r.

is

V.

r

SOLUTION

IDENTIFY and SET UP: This problem uses the general relationship
between  the  electric  potential  as  a  function  of  position  and  the
electric-ﬁeld vector. By symmetry, the electric ﬁeld here has only a
radial component  We use Eq. (23.23) to ﬁnd this component.

Er.

EXECUTE: From Eq. (23.23),

Er = -

0V
0r

= -

0
0r

a 1
4pP0

q
r

b =

1
4pP0

q
r 2

so the vector electric ﬁeld is

S
E

(cid:2) rNEr (cid:2) 1
4pP0

rN

q
r 2

EVALUATE: Our result agrees with Eq. (21.7), as it must.

An alternative approach is to ignore the radial symmetry, write
r = 2x 2 + y2 + z2,
and  take  the  deriva-
z

the  radial  distance  as
tives of  with respect to

and  as in Eq. (23.20). We ﬁnd

x, y,

V

q
2x 2 + y2 + z2

b = - 1

4pP0

qx
1x 2 + y2 + z223>2

0V
0x

=

0
0x

= -

a 1
4pP0
qx
4pP0r 3

and similarly

0V
0y

= -

qy
4pP0 r 3

0V
0z

= -

qz
4pP0r 3

Then from Eq. (23.20),

S (cid:2) (cid:3) c ıNa -
E

(cid:2) 1

4pP0

q
r 2

b (cid:4) ≥N a -

qx
4pP0r 3
N
xıN (cid:4) y≥N (cid:4) zk
r

a

b (cid:2) 1

4pP0

rN

q
r 2

qy
4pP0r 3

b (cid:4) k

N a -

qz
4pP0r 3

b d

This  approach  gives  us  the  same  answer,  but  with  more  effort.
Clearly it’s best to exploit the symmetry of the charge distribution
whenever possible.

776

CHAPTER 23 Electric Potential

Example 23.14

Potential and field of a ring of charge

In Example 23.11 (Section 23.3) we found that for a ring of charge
the potential at a point  on the
with radius  and total charge
Q,
from the center is
ring’s symmetry axis a distance
x

P

a

V =

1
4pP0

Q
2x 2 + a2

Find the electric ﬁeld at

P.

SOLUTION

x

V

IDENTIFY  and SET  UP: Figure 23.20 shows the situation. We are
given  as a function of  along the  -axis, and we wish to ﬁnd the
electric  ﬁeld  at  a  point  on  this  axis.  From  the  symmetry  of  the
charge distribution, the electric ﬁeld along the symmetry (x-) axis
of the ring can have only an  -component. We ﬁnd it using the ﬁrst
of Eqs. (23.19).

x

x

EXECUTE: The  -component of the electric ﬁeld is

x

Ex = -

0V
0x

=

1
4pP0

Qx
1x 2 + a223>2

EVALUATE: This agrees with our result in Example 21.9.

CAUTION Don’t  use  expressions  where  they  don’t  apply In  this
example,
is  not  a  function  of
or  on  the  ring  axis,  so  that
V
y
z
0V>0y = 0V>0z = 0
Ey = Ez = 0.
But  that  does  not  mean
and
are  valid
that  it’s  true  everywhere;  our  expressions  for
and
Ex
valid  at  all
only  on  the  ring  axis.  If  we  had  an  expression  for
V
at any
points in space, we could use it to ﬁnd the components of
point using Eqs. (23.19). ❙

S
E

V

V = A + Bx + Cy3 + Dxy,

Test Your Understanding of Section 23.5 In a certain region of space
the potential is given by
A, B, C,
positive constants. Which of these statements about the electric ﬁeld
region of space is correct? (There may be more than one correct answer.) (i) Increasing
the value of  will increase the value of
decrease the value of
zero at the origin

S
at all points; (ii) increasing the value of  will
E
S
E
at all points; (iii)  has no  -component; (iv) the electric ﬁeld is

1x = 0, y = 0, z = 02.

D
in this

and
S
E

where

are

S
E

A

A

z

❙
