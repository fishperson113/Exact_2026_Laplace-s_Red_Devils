Example 21.11
Field of a uniformly charged disk
A nonconducting disk of radius 
has a uniform positive surface
charge density . Find the electric field at a point along the axis of
the disk a distance from its center. Assume that is positive.
SOLUTION
IDENTIFY and SET UP: Figure 21.25 shows the situation. We rep-
resent the charge distribution as a collection of concentric rings of
charge 
. In Example 21.9 we obtained Eq. (21.8) for the field on
the axis of a single uniformly charged ring, so all we need do here
is integrate the contributions of our rings.
EXECUTE: A typical ring has charge 
, inner radius , and outer
radius 
. Its area is approximately equal to its width dr times
its circumference 2pr, or 
The charge per unit area is
so the charge of the ring is 
We use dQ in place of Q in Eq. (21.8), the expression for the field due
to a ring that we found in Example 21.9, and replace the ring radius 
with . Then the field component 
at point P due to this ring is
dEx =
1
4pP0
2psrx dr
1x2 + r 223>2
dEx
r
a
dQ = sdA = 2psr dr.
s = dQ>dA,
dA = 2pr dr.
r + dr
r
dQ
dQ
x
x
s
R
To find the total field due to all the rings, we integrate 
over 
from 
to 
(not from -R to R):
You can evaluate this integral by making the substitution 
(which yields 
); you can work out the details.
The result is
(21.11)
EVALUATE: If the disk is very large (or if we are very close to it), so
that 
the term 
in Eq. (21.11) is very
much less than 1. Then Eq. (21.11) becomes
(21.12)
Our final result does not contain the distance 
from the plane.
Hence the electric field produced by an infinite plane sheet of charge
is independent of the distance from the sheet. The field direction is
everywhere perpendicular to the sheet, away from it. There is no
such thing as an infinite sheet of charge, but if the dimensions of the
sheet are much larger than the distance 
of the field point 
from
the sheet, the field is very nearly given by Eq. (21.12).
If 
is to the left of the plane 
, the result is the same
except that the direction of 
is to the left instead of the right. If
the surface charge density is negative, the directions of the fields
on both sides of the plane are toward it rather than away from it.
E
S
1x 6 02
P
P
x
x
E =
s
2P0
1> 21R2>x22 + 1
R W x,
=
s
2P0
c1 -
1
21R2>x22 + 1
d
Ex = sx
2P0
c -
1
2x2 + R2 + 1
x d
dt = 2r dr
x2 + r 2
t =
Ex =
L
R
0
1
4pP0
12psr dr2x
1x2 + r 223>2 = sx
4P0 L
R
0
2r dr
1x2 + r 223>2
r = R
r = 0
r
dEx
21.25 Our sketch for this problem.
