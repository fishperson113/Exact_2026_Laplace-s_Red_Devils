Example 21.10
Field of a charged line segment
Positive charge 
is distributed uniformly along the 
-axis
between 
and 
Find the electric field at point 
on
the -axis at a distance from the origin.
SOLUTION
IDENTIFY and SET UP: Figure 21.24 shows the situation. As in
Example 21.9, we must find the electric field due to a continuous
distribution of charge. Our target variable is an expression for the
electric field at 
as a function of . The -axis is a perpendicular
bisector of the segment, so we can use a symmetry argument.
EXECUTE: We divide the line charge of length 2a into infinitesimal
segments of length dy. The linear charge density is 
and
the charge in a segment is 
. The distance r
from a segment at height y to the field point P is 
,
so the magnitude of the field at P due to the segment at height y is
Figure 21.24 shows that the x- and y-components of this field are
and 
, where cos a  x r and
sin
y r. Hence
To find the total field at P, we must sum the fields from all seg-
ments along the line-that is, we must integrate from 
to
You should work out the details of the integration (a table
of integrals will help). The results are
or, in vector form,
(21.9)
E
S 
1
4pP0
Q
x2x2 + a2 ın
Ey =
1
4pP0
Q
2a L
+a
-a
ydy
1x2 + y223>2 = 0
Ex =
1
4pP0
Q
2a L
+a
-a
xdy
1x2 + y223>2 =
Q
4pP0
1
x2x2 + a2
y = +a.
y = -a
dEy =
1
4pP0
Q
2a
ydy
1x2 + y223>2
dEx =
1
4pP0
Q
2a
xdy
1x2 + y223>2
>
a =
>
dEy = -dE sin a
dEx = dE cos a
dE =
1
4pP0
dQ
r 2 =
1
4pP0
Q
2a
dy
1x2 + y22
r = 1x2 + y221>2
dQ = ldy = 1Q>2a2dy
l = Q>2a,
x
x
P
x
x
P
y = +a.
y = -a
y
Q
points away from the line of charge if 
is positive and toward
the line of charge if 
is negative.
EVALUATE: Using a symmetry argument as in Example 21.9, we
could have guessed that 
would be zero; if we place a positive
test charge at , the upper half of the line of charge pushes down-
ward on it, and the lower half pushes up with equal magnitude.
Symmetry also tells us that the upper and lower halves of the seg-
ment contribute equally to the total field at P.
If the segment is very short (or the field point is very far from
the segment) so that 
we can neglect 
in the denominator
of Eq. (21.9). Then the field becomes that of a point charge, just as
in Example 21.9:
To see what happens if the segment is very long (or the field point
is very close to it) so that 
we first rewrite Eq. (21.9)
slightly:
(21.10)
In the limit 
we can neglect 
in the denominator of 
Eq. (21.10), so
E
S 
l
2pP0x ın
x2>a2
a W x
E
S 
1
2pP0
l
x21x2>a22 + 1
ın
a W x,
E
S 
1
4pP0
Q
x2 ın
a
x W a,
P
Ey
l
l
E
S
21.24 Our sketch for this problem.

21.5 Electric-Field Calculations
707
This is the field of an infinitely long line of charge. At any point 
at a perpendicular distance from the line in any direction, 
has
magnitude
(infinite line of charge)
Note that this field is proportional to 
rather than to 
as for
a point charge.
1>r 2
1>r
E =
l
2pP0r
E
S
r
P
There’s really no such thing in nature as an infinite line of
charge. But when the field point is close enough to the line,
there’s very little difference between the result for an infinite
line and the real-life finite case. For example, if the distance of
the field point from the center of the line is 1% of the length of
the line, the value of 
differs from the infinite-length value by
less than 0.02%.
E
r
