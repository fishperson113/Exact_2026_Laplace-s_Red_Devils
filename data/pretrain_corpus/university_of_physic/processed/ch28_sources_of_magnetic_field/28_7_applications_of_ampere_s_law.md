938

CHAPTER 28 Sources of Magnetic Field

SSS

NNN

S
B

Test Your Understanding of Section 28.6 The ﬁgure at left shows magnetic
ﬁeld lines through the center of a permanent magnet. The magnet is not connected to a
source of emf. One of the ﬁeld lines is colored red. What can you conclude about the cur-
rents inside the permanent magnet within the region enclosed by this ﬁeld line? (i) There
are no currents inside the magnet; (ii) there are currents directed out of the plane of the
page; (iii) there are currents directed into the plane of the page; (iv) not enough informa-
tion is given to decide.

❙

28.7 Applications of Ampere’s Law

Ampere’s law is useful when we can exploit the symmetry of a situation to eval-
uate the line integral of
Several examples are given below. Problem-Solving
Strategy  28.2  is  directly  analogous  to  Problem-Solving  Strategy  22.1  (Section
22.4) for applications of Gauss’s law; we suggest you review that strategy now
and compare the two methods.

S
.
B

Problem-Solving Strategy 28.2

Ampere’s Law

S # d l
AB

IDENTIFY the relevant concepts: Like Gauss’s law, Ampere’s law
is most useful when the magnetic ﬁeld is highly symmetric. In the
form
as a func-
tion of position if we are given the magnitude and direction of the
ﬁeld-generating electric current.

it can yield the magnitude of

m0Iencl,

S
B

=

S

SET UP the problem using the following steps:
1. Determine the target variable(s). Usually one will be the mag-

nitude of the  ﬁeld as a function of position.

S
B

2. Select the integration path you will use with Ampere’s law. If
you want to determine the magnetic ﬁeld at a certain point, then
the  path  must  pass  through  that  point.  The  integration  path
doesn’t have to be any actual physical boundary. Usually it is a
purely geometric curve; it may be in empty space, embedded in
a solid body, or some of each. The integration path has to have
enough symmetry to  make  evaluation  of  the  integral  possible.
in regions of interest; else-
Ideally the path will be tangent to
where  the  path  should  be  perpendicular  to
or  should  run
through regions in which

= 0.

S
B

S
B

S
B

2. In  the  integral

is always zero.
3. Determine the current

magnitude B at every point, then its line integral is the product
S
of B and the length of that portion of the path. If
is perpendi-
B
= 0,
cular  to  some  portion  of  the  path,  or  if
that  portion
makes no contribution to the integral.
S # d l
AB

is  the  total magnetic  ﬁeld  at  each
point on the path; it can be caused by currents enclosed or not
enclosed by the path. If no net current is enclosed by the path,
the ﬁeld at points on the path need not be zero, but the integral
S # d l
AB

S
,

S
B

S
B

S

Iencl

enclosed by the integration path. A
right-hand rule gives the sign of this current: If you curl the ﬁn-
gers of your right hand so that they follow the path in the direc-
tion of integration, then your right thumb points in the direction
is tangent to the path everywhere and
of positive current. If
is the same as the direction of
Iencl
integration.  If  instead
is  in  the  direction
opposite to that of the integration.
= m0I

Iencl
S # d l
AB

to solve for the target variable.

is positive, the direction of

is  negative,

S
B

S
B

S
B

S

4. Use Ampere’s law

EXECUTE the solution as follows:
S # d l
S
1. Carry  out  the  integral
AB

is
tangent  to  all  or  some  portion  of  the  path  and  has  the  same

along  the  chosen  path.  If

S
B

EVALUATE your answer: If your result is an expression for the ﬁeld
magnitude as a function of position, check it by examining how the
expression behaves in different limits.

Example 28.7

Field of a long, straight, current-carrying conductor

In Section 28.6 we derived Ampere’s law using Eq. (28.9) for the
ﬁeld  of a long, straight, current-carrying conductor. Reverse this
process, and use Ampere’s law to ﬁnd

for this situation.

S
B

S
B

SOLUTION

IDENTIFY and SET UP: The situation has cylindrical symmetry, so
in Ampere’s  law  we  take  our  integration  path  to  be  a  circle  with
radius r centered on the conductor and lying in a plane perpendicu-
is everywhere tangent to this
lar to it, as in Fig. 28.16a. The ﬁeld
circle and has the same magnitude B everywhere on the circle.

S
B

EXECUTE: With our choice of integration path, Ampere’s law [Eq.
(28.20)] becomes

S # d l
B

S

=

C

C

BŒ dl = B12pr2 = m0I

S
B

follows immediately.

Equation (28.9),

B = m0I>2pr,
Ampere’s law determines the direction of

as well as its mag-
nitude. Since we chose to go counterclockwise around the integra-
tion  path,  the  positive  direction  for  current  is  out  of  the  plane  of
Fig. 28.16a; this is the same as the actual current direction in the
ﬁgure,  so  I is  positive  and  the  integral
is  also  positive.
’s  run  counterclockwise,  the  direction  of  must  be
Since  the
counterclockwise as well, as shown in Fig. 28.16a.

S # d l
AB

S
d l

S
B

S

EVALUATE: Our results are consistent with those in Section 28.6.

Example 28.8

Field of a long cylindrical conductor

A cylindrical conductor with radius R carries a current I (Fig. 28.20).
The current is uniformly distributed over the cross-sectional area of
the conductor. Find the magnetic ﬁeld as a function of the distance
r from the conductor axis for points both inside
and out-
side

the conductor.

1r 6 R2

1r 7 R2

SOLUTION

IDENTIFY and SET UP: As in Example 28.7, the current distribu-
tion has cylindrical symmetry, and the magnetic field lines must
be  circles  concentric  with  the  conductor  axis. To  find  the  mag-
netic  field  inside  and  outside  the  conductor,  we  choose  circular
r 6 R
integration  paths  with  radii
,  respectively  (see
Fig. 28.20).

r 7 R

and

S
B

EXECUTE: In  either  case  the  ﬁeld
has  the  same  magnitude  at
every  point  on  the  circular  integration  path  and  is  tangent  to  the
path. Thus the magnitude of the line integral is simply
To
enclosed by a circular integration path inside
ﬁnd the current
, note that the current density (current per unit
the conductor
Iencl = J1pr 22 = Ir 2>R2.
area) is
Hence Ampere’s
law gives

Iencl
1r 6 R,2
so
B12pr2 = m0Ir 2>R2

J = I>pR2,

B12pr2.

, or

28.20 To ﬁnd the magnetic ﬁeld at radius
Ampere’s law to the circle enclosing the gray area. The current
through the red area is
r 7 R,
radius
entire conductor.

we apply Ampere’s law to the circle enclosing the

To ﬁnd the magnetic ﬁeld at

1r 2>R22I.

we apply

r 6 R,

I

r .R

r ,R

S
B

S
B

R

S
B

S
B

I

Example 28.9

Field of a solenoid

S
B

A solenoid consists of a helical winding of wire on a cylinder, usu-
ally  circular  in  cross  section.  There  can  be  thousands  of  closely
spaced  turns  (often  in  several  layers),  each  of  which  can  be
regarded as a circular loop. For simplicity, Fig. 28.22 shows a sole-
noid with only a few turns. All turns carry the same current I, and
the total  ﬁeld at every point is the vector sum of the ﬁelds caused
by the individual turns. The ﬁgure shows ﬁeld lines in the xy- and
xz-planes. We draw ﬁeld lines that are uniformly spaced at the cen-
ter of the solenoid. Exact calculations show that for a long, closely
wound solenoid, half of these ﬁeld lines emerge from the ends and
half  “leak  out”  through  the  windings  between  the  center  and  the
end, as the ﬁgure suggests.

If  the  solenoid  is  long  in  comparison  with  its  cross-sectional
diameter and the coils are tightly wound, the ﬁeld inside the solenoid
near its midpoint is very nearly uniform over the cross section and
parallel to the axis; the external ﬁeld near the midpoint is very small.

28.7 Applications of Ampere’s Law

939

B =

m0I
2p

r
R2

(inside the conductor,
r 6 R)

(28.21)

A circular  integration  path  outside  the  conductor  encloses  the
. Applying Ampere’s law
total current in the conductor, so
gives the same equation as in Example 28.7, with the same result
for B:

Iencl = I

B =

m0I
2pr

(outside the conductor,
r 7 R)

(28.22)

Outside the conductor, the magnetic ﬁeld is the same as that of a
long,  straight  conductor  carrying  current  I,  independent  of  the
radius R over which the current is distributed. Indeed, the magnetic
ﬁeld outside any cylindrically symmetric current distribution is the
same  as  if  the  entire  current  were  concentrated  along  the  axis  of
the distribution. This is analogous to the results of Examples 22.5
and 22.9 (Section 22.4), in which we found that the electric ﬁeld
outside  a  spherically  symmetric  charged body  is  the  same  as
though the entire charge were concentrated at the center.

EVALUATE: Note that at the surface of the conductor
Eqs.
(28.21) and  (28.22) agree,  as  they  must.  Figure  28.21 shows  a
graph of B as a function of r.

1r = R2,

28.21 Magnitude of the magnetic ﬁeld inside and outside a long,
straight cylindrical conductor with radius R carrying a current I.

B

m
0I
2p

r
R2

m
0I
2pR
B 5

1
2

m
0I
2pR

B 5

m
0I
2pr

O

R

2R

3R

r

4R

28.22 Magnetic ﬁeld lines produced by the current in a sole-
noid. For clarity, only a few turns are shown.

y

I

z

I

x

S
B

Continued

940

CHAPTER 28 Sources of Magnetic Field

Use Ampere’s law to ﬁnd the ﬁeld at or near the center of such

a solenoid if it has n turns per unit length and carries current I.

SOLUTION

S
B

IDENTIFY  and SET  UP:  We  assume  that
is  uniform  inside  the
solenoid and zero outside. Figure 28.23 shows the situation and our
chosen integration path, rectangle abcd. Side ab, with length L, is
parallel to the axis of the solenoid. Sides bc and da are taken to be
very long so that side cd is far from the solenoid; then the ﬁeld at
side cd is negligibly small.
S
B

EXECUTE: Along side ab,
is parallel to the path and is constant.
Our Ampere’s-law integration takes us along side ab in the same
direction as

so here

S
B

,

BŒ = + B
and
b
S # d l
B

S

= BL

;  along  side  cd,

Along  sides  bc and da,
S
BŒ = 0
B
closed path, then, we have

L
a
S
is  perpendicular  to  the  path  and  so
B
(cid:2) 0
Around  the  entire
S # d l
AB
In a length L there are nL turns, each of which passes once
?
through abcd carrying  current  I.  Hence  the  total  current
S # d l
enclosed  by  the  rectangle  is
AB

BŒ = 0.
BL.

The  integral

Iencl = nLI.

and  so
S

is

=

S

Iencl
positive, so from Ampere’s law
must be positive as well. This
means that the current passing through the surface bounded by the
integration  path  must  be  in  the  direction  shown  in  Fig.  28.23.
BL = m0nLI
Ampere’s law then gives

, or

B = m0nI

(solenoid)

(28.23)

Side ab need  not  lie  on  the  axis  of  the  solenoid,  so  this  result
demonstrates that the ﬁeld is uniform over the entire cross section
at the center of the solenoid’s length.

EVALUATE: Note that the direction of
same direction as the solenoid’s vector magnetic moment
found in Section 28.5 for a single current-carrying loop.

inside the solenoid is in the
as we

MS

,

S
B

For points along the axis, the ﬁeld is strongest at the center of
the solenoid and drops off near the ends. For a solenoid very long
in  comparison  to  its  diameter,  the  ﬁeld  magnitude  at  each  end  is
exactly half that at the center. This is approximately the case even
for a relatively short solenoid, as Fig. 28.24 shows.

28.24 Magnitude of the magnetic ﬁeld at points along the axis
of a solenoid with length 4a, equal to four times its radius a. The
ﬁeld magnitude at each end is about half its value at the center.
(Compare with Fig. 28.14 for the ﬁeld of N circular loops.)

28.23 Our sketch for this problem.

I

5

S

2a

4a

B

m

0nI

1
2

m

0nI

24a

23a

22a

2a

O a

2a

3a

4a

x

Example 28.10

Field of a toroidal solenoid

Figure 28.25a shows a doughnut-shaped toroidal solenoid, tightly
wound  with  N turns  of  wire  carrying  a  current  I.  (In  a  practical
solenoid the turns would be much more closely spaced than they
are in the ﬁgure.) Find the magnetic ﬁeld at all points.

28.25 (a) A toroidal solenoid. For clarity, only a few turns of
the winding are shown. (b) Integration paths (black circles) used
to compute the magnetic ﬁeld
dots and crosses).

set up by the current (shown as

S
B

SOLUTION

(a)

(b)

r
B

IDENTIFY and SET UP: Ignoring the slight pitch of the helical wind-
ings, we can consider each turn of a tightly wound toroidal solenoid
as a loop lying in a plane perpendicular to the large, circular axis of
the toroid. The symmetry of the situation then tells us that the mag-
netic ﬁeld lines must be circles concentric with the toroid axis. There-
fore  we  choose  circular  integration  paths  (of  which  Fig.  28.25b
shows three) for use with Ampere’s law, so that the ﬁeld
(if any) is
tangent to each path at all points along the path.

EXECUTE: Along each path,
the  path  circumference
path 1 is zero, so from Ampere’s law the ﬁeld
on this path.

S # d l
equals the product of B and
AB
l = 2pr
.  The  total  current  enclosed  by
everywhere

(cid:2) 0

S
B

S
B

S

Each turn of the winding passes twice through the area bounded
by path 3, carrying equal currents in opposite directions. The net

r

O
Path 1

I

I

Path 2

Path 3

The magnetic field is confined almost entirely
to the space enclosed by the windings (in blue).

current enclosed is therefore zero, and hence
at all points
on this path as well. We conclude that the ﬁeld of an ideal toroidal

S
B

(cid:2) 0
