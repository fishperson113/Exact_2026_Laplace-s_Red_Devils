928

CHAPTER 28 Sources of Magnetic Field

Example 28.2 Magnetic field of a current segment

A copper wire carries a steady 125-A current to an electroplating
tank (Fig. 28.4). Find the magnetic ﬁeld due to a 1.0-cm segment
of this wire at a point 1.2 m away from it, if the point is (a) point
in the
P1,
xy-plane and on a line at

straight out to the side of the segment, and (b) point

to the segment.

30°

P2,

SOLUTION

IDENTIFY and SET UP: Although Eqs. (28.5) and (28.6) apply only
to inﬁnitesimal current elements, we may use either of them here
because the segment length is much less than the distance to the
ﬁeld point. The current element is shown in red in Fig. 28.4 and
(cid:2)
points in the
(the direction of the current), so
dl1- ın2.
for  each  ﬁeld  point  is  directed  from
for
the  current  element  toward  that  point:
for point P2.
point

-x-direction
rn
The  unit  vector

is  in  the
-x-direction

rn
above the

and at an angle of

+y-direction

S
d l

30°

P1

EXECUTE: (a) At point

S
B

rn (cid:2) ≥n,

P1,
: rn

so
I dl1- ın2 : ≥n
r 2

S
I d l

(cid:2)

(cid:2)

m0
4p

m0
m0
4p
4p
r 2
1125 A211.0 * 10-2 m2
(cid:2) -110-7 T # m>A2
11.2 m22

(cid:2) -

n
 k

N
k

I dl
r 2

N
(cid:2) -18.7 * 10-8 T2k

The direction of

is into the xy-plane of Fig. 28.4.

S
B

at

P1
,  the  unit  vector  is

rn (cid:2) 1- cos 30°2ın (cid:3) 1sin 30°2≥n

.

(b)  At

P2

From Eq. (28.6),

S
B

(cid:2)

m0
4p

(cid:2) -

m0I
4p

S
I d l

: rn

(cid:2)

r 2
dl sin 30°
r 2

m0
4p

I dl1- ın2 : 1-cos 30°ın (cid:3) sin 30°≥n2
r 2

N
k

28.4 Finding the magnetic ﬁeld at two points due to a 1.0-cm
segment of current-carrying wire (not shown to scale).

y

P1

P2

1.2 m

125 A

1.2 m
30°

125 A

x

z

1.0 cm

(cid:2) -110-7 T # m>A2

1125 A211.0 * 10-2 m21sin 30°2
11.2 m22

N
 k

N
(cid:2) -14.3 * 10-8 T2k

The direction of

S
B

at

P2

is also into the xy-plane of Fig. 28.4.

EVALUATE:  We  can  check  our  results  for  the  direction  of
by
comparing them with Fig. 28.3. The xy-plane in Fig. 28.4 corre-
sponds to the beige plane in Fig. 28.3, but here the direction of the
is the reverse of that shown in Fig. 28.3.
current and hence of
Hence  the  direction  of  the  magnetic  ﬁeld  is  reversed  as  well.
Hence the ﬁeld at points in the  xy-plane in Fig. 28.4 must point
into, not out of, that plane. This is just what we concluded above.

S
d l

S
B

Test Your Understanding of Section 28.2 An inﬁnitesimal current
1x = y = z = 02
element located at the origin
carries current I in the positive
y-direction. Rank the following locations in order of the strength of the magnetic
ﬁeld that the current element produces at that location, from largest to smallest value.
(i)
(iv)

x = L,
y = 0,
x = L> 12 ,

z = 0;
(ii)
y = L> 12 ,

x = 0,
z = 0.

y = L,

z = L;

y = 0,

x = 0,

z = 0;

(iii)

❙

28.3 Magnetic Field of a Straight
Current-Carrying Conductor

Let’s  use  the  law  of  Biot  and  Savart  to  ﬁnd  the  magnetic  ﬁeld  produced  by  a
straight current-carrying conductor. This result is useful because straight conduct-
ing wires are found in essentially all electric and electronic devices. Figure 28.5
at a
shows such a conductor with length 2a carrying a current I. We will ﬁnd
point a distance x from the conductor on its perpendicular bisector.

S
B

We ﬁrst use the law of Biot and Savart, Eq. (28.5), to ﬁnd the ﬁeld

caused by
dl = dy
the element of conductor of length
shown in Fig. 28.5. From the ﬁgure,
sin f = sin1p - f2 = x> 2x 2 + y2 .
r = 2x 2 + y2
and
The  right-hand  rule
S
S
d l
dB
for the vector product
is into the plane of
’s
the  ﬁgure,  perpendicular  to  the  plane;  furthermore,  the  directions  of  the
from all elements of the conductor are the same. Thus in integrating Eq. (28.7),
S
dB
we can just add the magnitudes of the

shows that the direction of

a signiﬁcant simpliﬁcation.

: rn

S
dB

’s,

S
dB

28.5 Magnetic ﬁeld produced by a
straight current-carrying conductor of
length 2a.

y

a

S
dl

O

2a

f

r^

p 2 f

y

r (cid:2) (cid:2)x2 (cid:3) y2

P

I

x

x

S
dB
S
At point P, the field dB
caused by each element of
the conductor points into the
plane of the page, as does
the total B field.

S

28.3 Magnetic Field of a Straight Current-Carrying Conductor

929

Putting the pieces together, we ﬁnd that the magnitude of the total  ﬁeld is
a

S
B

B =

m0I
4p L
-a

x dy
1x 2 + y223>2

We can integrate this by trigonometric substitution or by using an integral table:

B =

m0I
4p

2a
x2x 2 + a2

(28.8)

When the length 2a of the conductor is very great in comparison to its distance x
from point P, we can consider it to be inﬁnitely long. When a is much larger than
x,
Eq. (28.8)
becomes

is approximately equal to a; hence in the limit

2x 2 + a2

a S q,

B =

m0I
2px

The  physical  situation  has  axial  symmetry  about  the  y-axis.  Hence  must
have the same magnitude at all points on a circle centered on the conductor and
lying in a plane perpendicular to it, and the direction of  must be everywhere
tangent  to  such  a  circle  (Fig.  28.6).  Thus,  at  all  points  on  a  circle  of  radius  r
around the conductor, the magnitude B is

S
B

S
B

B =

m0I
2pr

(near a long, straight, current-carrying conductor) (28.9)

1>r.

The  geometry  of  this  problem  is  similar  to  that  of  Example  21.10  (Section
21.5), in which we solved the problem of the electric ﬁeld caused by an inﬁnite
line of charge. The same integral appears in both problems, and the ﬁeld magni-
S
B
in the magnetic
tudes in both problems are proportional to
in  the  analogous
problem  have  completely  different  shapes  than  the  lines  of
electrical problem. Electric ﬁeld lines radiate outward from a positive line charge
distribution  (inward  for  negative  charges).  By  contrast,  magnetic  ﬁeld  lines
encircle the  current  that  acts  as  their  source.  Electric  ﬁeld  lines  due  to  charges
begin and end at those charges, but magnetic ﬁeld lines always form closed loops
and never have end points, irrespective of the shape of the current-carrying con-
ductor  that  sets  up  the  ﬁeld. As  we  discussed  in  Section  27.3,  this  is  a  conse-
quence of Gauss’s law for magnetism, which states that the total magnetic ﬂux
through any closed surface is always zero:

But the lines of
S
E

S # dA

B

S

C

= 0

(magnetic ﬂux through any closed surface) (28.10)

28.6 Magnetic ﬁeld around a long,
straight, current-carrying conductor. The
ﬁeld lines are circles, with directions
determined by the right-hand rule.

Right-hand rule for the magnetic field
around a current-carrying wire: Point the
thumb of your right hand in the direction of the
current. Your fingers now curl around the wire
in the direction of the magnetic field lines.

S
B

S
B

S
B

I

I

S
B

S
B

S
B

ActivPhysics 13.1: Magnetic Field of a Wire

Any magnetic ﬁeld line that enters a closed surface must also emerge from that
surface.

Example 28.3 Magnetic field of a single wire

A long, straight conductor carries a 1.0-A current. At what distance
from  the  axis  of  the  conductor  does  the  resulting  magnetic  ﬁeld
have magnitude
(about that of the earth’s mag-
netic ﬁeld in Pittsburgh)?

B = 0.5 * 10-4 T

SOLUTION

EXECUTE: We solve Eq. (28.9) for r:

r =

m0I
2pB

=

14p * 10-7 T # m>A211.0 A2
12p210.5 * 10-4 T2

= 4 * 10-3 m = 4 mm

IDENTIFY  and SET  UP:  The length of a “long” conductor is much
greater  than  the  distance  from  the  conductor  to  the  ﬁeld  point.
Hence  we  can  use  the  ideas  of  this  section.  The  geometry  is  the
same as that of Fig. 28.6, so we use Eq. (28.9). All of the quantities
in this equation are known except the target variable, the distance r.

EVALUATE:  As we saw in Example 26.14, currents of an ampere or
more  are  typical  of  those  found  in  the  wiring  of  home  appliances.
This example shows that the magnetic ﬁelds produced by these appli-
ances are very weak even very close to the wire; the ﬁelds are propor-
tional to 1 r, so they become even weaker at greater distances.

>

930

CHAPTER 28 Sources of Magnetic Field

Example 28.4 Magnetic field of two wires

Figure 28.7a is an end-on view of two long, straight, parallel wires
perpendicular  to  the  xy-plane,  each  carrying  a  current  I but  in
opposite directions. (a) Find
(b) Find an
S
expression for
B

P1,
at any point on the x-axis to the right of wire 2.

at points

and

P2,

P3.

S
B

),

S
B

(b) At any point on the x-axis to the right of wire 2 (that is, for
x 7 d
. Such a point
are in the same directions as at
is a distance x + d from wire 1 and a distance x – d from wire 2, so
the total ﬁeld is

and

S
B

P3

1

2

SOLUTION

S
B

S

S

total (cid:2) B

1 (cid:3) B

2 (cid:2)

m0I
2p1x + d2

≥n (cid:4)

m0I
2p1x - d2

≥n

1

S

S

S
B

and

S
B
B2

1 (cid:3) B
2.

S
IDENTIFY and SET UP: We can ﬁnd the magnetic ﬁelds
B
2
due to wires 1 and 2 at each point using the ideas of this section.
By the superposition principle, the magnetic ﬁeld at each point is
(cid:2) B
then
B1
of these ﬁelds and the right-hand rule to ﬁnd the correspon-
and
S
ding directions. Figure 28.7a shows
at each
B
point; you should conﬁrm that the directions and relative magni-
tudes shown are correct. Figure 28.7b shows some of the magnetic
ﬁeld lines due to this two-wire system.

We use Eq. (28.9) to ﬁnd the magnitudes

(cid:2) B

and

S
B

S
B

total

1,

2,

S

EXECUTE: (a) Since point
tance  4d from  wire  2,
m0I>2p14d2 = m0I>8pd
the negative y-direction and
m0I
4pd

total (cid:2) B

2 (cid:2) -

1 (cid:3) B

S
B

S

S

S
B

2

P1
B1 = m0I>2p12d2 = m0I>4pd
. The right-hand rule shows that

is a distance 2d from wire 1 and a dis-
B2 =
is in

and
S
B

1

is in the positive y-direction, so
m0I
8pd

m0I
8pd

≥n (cid:2) -

(point

≥n

≥n (cid:3)

P1

)

P2,

a distance d from both wires,

At point
positive y-direction,  and  both  have  the  same  magnitude
B2 = m0I>2pd

are both in the
B1 =

. Hence

and

1

2

S
B

S
B

S
B

S

S

total (cid:2) B

1 (cid:3) B

2 (cid:2)

m0I
2pd

≥n (cid:3)

m0I
2pd

≥n (cid:2)

m0I
pd

≥n

(point

P2

)

the right-hand rule shows that
S
B
2

is in the posi-
Finally, at point
P3
tive y-direction and
is in the negative y-direction. This point is a
distance  3d from  wire  1  and  a  distance  d from  wire  2,  so
B1 = m0I>2p13d2 = m0I>6pd
. The total ﬁeld
and
at

B2 = m0I>2pd

is

P3

S
B
1

S
B

S

S

1 (cid:3) B

total (cid:2) B

m0I
6pd
The same technique can be used to ﬁnd

m0I
2pd

≥n (cid:2) -

2 (cid:2)

≥n (cid:4)

m0I
3pd
S
B

at any point; for
points  off  the  x-axis,  caution  must  be  taken  in  vector  addition,
since

need no longer be simply parallel or antiparallel.

and

S
B

total

S
B

1

2

≥n

(point

P3

)

(cid:2) -

m0Id
p1x 2 - d 22

≥n

where we combined the two terms using a common denominator.

d 2

1>x

; for two wires carrying opposite currents,

EVALUATE:  Consider  our  result  from  part  (b)  at  a  point  very  far
term in
from the wires, so that x is much larger than d. Then the
the denominator can be neglected, and the magnitude of the total
Btotal = m0Id>px 2
ﬁeld  is  approximately
.  For  a  single  wire,  Eq.
(28.9) shows that the magnetic ﬁeld decreases with distance in pro-
S
portion to
B
2
decreases more rapidly, in
partially cancel each other, and so
1>x 2.
proportion to
This effect is used in communication systems
such as telephone or computer networks. The wiring is arranged so
that a conductor carrying a signal in one direction and the conduc-
tor carrying the return signal are side by side, as in Fig. 28.7a, or
twisted  around  each  other  (Fig.  28.8). As  a  result,  the  magnetic
ﬁeld due to these signals outside the conductors is very small, mak-
ing  it  less  likely  to  exert  unwanted  forces  on  other  information-
carrying currents.

Btotal

and

S
B

1

28.8 Computer cables, or cables for audio-video equipment,
create little or no magnetic ﬁeld. This is because within each
cable, closely spaced wires carry current in both directions along
the length of the cable. The magnetic ﬁelds from these opposing
currents cancel each other.

28.7 (a) Two long, straight conductors carrying equal currents in opposite directions. The conductors are seen end-on. (b) Map of the
magnetic ﬁeld produced by the two conductors. The ﬁeld lines are closest together between the conductors, where the ﬁeld is strongest.

(a)

S
B2

S
B1

P1
S
Btotal

(b)

y

S
Btotal

S
B1

S
B2

Wire 1

Wire 2

I

P2

d

d

I

P3

S
Btotal

S
B1

x

2d

S
B2

3d

I

I

S
B
