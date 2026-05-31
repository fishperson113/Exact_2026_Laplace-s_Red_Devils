S
dB

produced at point P by a segment

Test Your Understanding of Section 28.5 Figure 28.12 shows the
S
magnetic ﬁeld
that lies on the positive
d l
dBx 7 0, dBy 7 0, dBz =
y-axis (at the top of the loop). This ﬁeld has components
S
produced at P by a segment
(a) What are the signs of the components of the ﬁeld
dB
0.
S
dBx 7 0, dBy 7 0, dBz = 0;
on the negative
d l
dBx 7 0,
(iv)
(ii)
dBy 6 0, dBz = 0;
ﬁeld
of the loop)? (i)
(iii)
these.

dBx 6 0, dBy 7 0, dBz = 0;
(v) none of these. (b) What are the signs of the components of the
(at the right-hand side

dBx 7 0, dBy 6 0, dBz = 0;
(v) none of

dBy 7 0, dBz = 0;
(iv)

y-axis
dBy 6 0, dBz = 0;

dBx 6 0, dBy 7 0, dBz = 0;

dBx 6 0, dBy 6 0, dBz = 0;

on the negative
(ii)

(at the bottom of the loop)? (i)

produced at P by a segment

dBx 7 0,

dBx 6 0,

z-axis

S
dB

(iii)

S
d l

28.6 Ampere’s Law

935

❙

28.6 Ampere’s Law

So far our calculations of the magnetic ﬁeld due to a current have involved ﬁnd-
ing the inﬁnitesimal ﬁeld
due to a current element and then summing all the
S
dB
’s to ﬁnd the total ﬁeld. This approach is directly analogous to our  electric-
ﬁeld calculations in Chapter 21.

S
dB

For the electric-ﬁeld problem we found that in situations with a highly sym-
metric charge distribution, it was often easier to use Gauss’s law to ﬁnd  There
is likewise a law that allows us to more easily ﬁnd the magnetic ﬁelds caused by
highly  symmetric  current distributions.  But  the  law  that  allows  us  to  do  this,
called Ampere’s law, is rather different in character from Gauss’s law.

S
.
E

P0.

Gauss’s law for electric ﬁelds involves the ﬂux of

through a closed surface;
it  states  that  this  ﬂux  is  equal  to  the  total  charge  enclosed  within  the  surface,
divided by the constant
Thus this law relates electric ﬁelds and charge distri-
butions. By contrast, Gauss’s law for magnetic ﬁelds, Eq. (28.10), is not a rela-
tionship between magnetic ﬁelds and current distributions; it states that the ﬂux
through any closed surface is always zero, whether or not there are currents
of
within the surface. So Gauss’s law for
can’t be used to determine the magnetic
ﬁeld produced by a particular current distribution.

S
B

S
B

Ampere’s law is formulated not in terms of magnetic ﬂux, but rather in terms
around a closed path, denoted by

of the line integral of

S
B

S # d l

B

S

C

S
E

S
B

28.16 Three integration paths for the
line integral of
in the vicinity of a long,
straight conductor carrying current I out of
the plane of the page (as indicated by the
circle with a dot). The conductor is seen
end-on.

(a) Integration path is a circle centered on the
conductor; integration goes around the circle
counterclockwise.
Result: rB # dl 5 m
0I
S
B

S S

S
B

S
B

S
dl

I
S
dl

S
dl

r

S
dl

S
B

(b) Same integration path as in (a), but
integration goes around the circle clockwise.
Result: rB # dl 5 2m
0I

S

S

calculate the scalar product of
S
B

We used line integrals to deﬁne work in Chapter 6 and to calculate electric poten-
tial in Chapter 23. To evaluate this integral, we divide the path into inﬁnitesimal
S
,
segments
for each segment, and sum
d l
these  products.  In  general,
varies  from  point  to  point,  and  we  must  use  the
BŒ
at the location of each
An alternative notation is
value of
S
at each point. The circle on the integral sign
B
is the component of  parallel to
indicates  that  this  integral  is  always  computed  for  a  closed path,  one  whose
beginning and end points are the same.

S # d l

S
.
d l
S
d l

A BŒ dl,

where

S
B

B

S

S
dl

S
B

S
B

S
dl

S
B

S
dl

r

I

S
dl

S
B

Ampere’s Law for a Long, Straight Conductor
To  introduce  the  basic  idea  of Ampere’s  law,  let’s  consider  again  the  magnetic
ﬁeld caused by a long, straight conductor carrying a current I. We found in Sec-
tion 28.3 that the ﬁeld at a distance r from the conductor has magnitude

(c) An integration path that does not enclose the
conductor
Result: rB # dl 5 0

B =

m0I
2pr

S
B

The  magnetic  field  lines  are  circles  centered  on  the  conductor.  Let’s  take  the
around  one  such  circle  with  radius  r,  as  in  Fig.  28.16a. At
line  integral  of
every point on the circle,
since r is
constant around the circle, B is constant as well. Alternatively, we can say that
BŒ
is constant and equal to B at every point on the circle. Hence we can take B

are parallel, and so

S # d l

= B dl;

and

S
d l

S
B

B

S

S
B

b

S
dl

c

S
B

r2

S
B

u

S
dl

S
dl

r1

d

I

S
B

S
dl

a

936

CHAPTER 28 Sources of Magnetic Field

outside of the integral. The remaining integral  is just the circumference of the
circle, so

S # d l

B

S

C

=

C

BŒ dl = B

dl =

C

m0I
2pr

12pr2 = m0I

The line integral is thus independent of the radius of the circle and is equal to
multiplied by the current passing through the area bounded by the circle.

m0

S

= - B dl

S # d l

and the line integral equals

In  Fig.  28.16b  the  situation  is  the  same,  but  the  integration  path  now  goes
S
B
around  the  circle  in  the  opposite  direction.  Now
are  antiparallel,  so
-m0I.
We get the same result if the
B
integration path is the same as in Fig. 28.16a, but the direction of the current is
reversed. Thus
equals  multiplied by the current passing through the
area bounded by the integration path, with a positive or negative sign depending
on the direction of the current relative to the direction of integration.

S # d l

A B

and

S
d l

m0

S

S

A B

S # d l

There’s  a  simple  rule  for  the  sign  of  the  current;  you  won’t  be  surprised  to
learn that it uses your right hand. Curl the ﬁngers of your right hand around the
integration path so that they curl in the direction of integration (that is, the direc-
Then your right thumb indicates the posi-
tion that you use to evaluate
tive  current  direction.  Currents  that  pass  through  the  integration  path  in  this
direction  are  positive;  those  in  the  opposite  direction  are  negative.  Using  this
rule, you should be able to convince yourself that the current is positive in Fig.
28.16a and negative in Fig. 28.16b. Here’s another way to say the same thing:
Looking at the surface bounded by the integration path, integrate counterclock-
wise around the path as in Fig. 28.16a. Currents moving toward you through the
surface are positive, and those going away from you are negative.

).

An integration path that does not enclose the conductor is used in Fig. 28.16c.
S
BŒ = B1 =
B
S
are antiparallel and
d l
S
at each point on the
d l
and these sections contribute zero to the

are  parallel,  and
and
The  ﬁeld is perpendicular to

Along  the  circular  arc  ab of  radius
m0I>2pr1;
BŒ = - B2 = - m0I>2pr2.
straight sections bc and da, so
line integral. The total line integral is then

along the circular arc cd of radius

S
B
BŒ = 0

S
d l
r2,

and

r1,

S
B

S # d l

B

S

C

=

=

BŒ dl = B1 L
C
m0I
2pr1

1r1u2 + 0 -

a

m0I
2pr2

1r2u2 + 0 = 0

b

dl + 102

c

L
b

dl + 1-B22

d

L
c

dl + 102

a

dl

L
d

S
B

is greater on arc cd than on arc ab, but the arc length is less,
The magnitude of
so  the  contributions  from  the  two  arcs  exactly  cancel.  Even  though  there  is  a
magnetic ﬁeld everywhere along the integration path, the line integral
is
zero if there is no current passing through the area bounded by the path.

S # d l

A B

S

We can also derive these results for more general integration paths, such as the
S
d l

the angle between

one in Fig. 28.17a. At the position of the line element
and

S
,
d l

and

f,

S
B

is

S # d l

B

S

= B dl cos f

dl cos f = r du,
From the ﬁgure,
position of the conductor and r is the distance of

where

du

S
d l

is the angle subtended by

S
d l

at the

from the conductor. Thus

S # d l

B

S

C

=

C

m0I
2pr

1r du2 =

m0I
2p C

du

A du
But
conductor to

S
d l

is just equal to

2p,

the total angle swept out by the radial line from the

during a complete trip around the path. So we get

S
B

28.17 (a) A more general integration
path for the line integral of
straight conductor carrying current I out of
the plane of the page. The conductor is seen
end-on. (b) A more general integration path
that does not enclose the conductor.

around a long,

(a)

(b)

f

S
dl

S
B

r du

du

r

I

S
dl

S
B

r du

du

r

I

28.6 Ampere’s Law

937

= m0I

(28.19)

S # d l

B

S

C

This result doesn’t depend on the shape of the path or on the position of the wire
inside it. If the current in the wire is opposite to that shown, the integral has the
opposite sign. But if the path doesn’t enclose the wire (Fig. 28.17b), then the net
is  zero
during  the  trip  around  the  integration  path  is  zero;
change  in
and the line integral is zero.
instead of

u
2p

A du

Ampere’s Law: General Statement
Equation (28.19) is almost, but not quite, the general statement of Ampere’s law.
To  generalize  it  even  further,  suppose  several long,  straight  conductors  pass
through the surface bounded by the integration path. The total magnetic ﬁeld
at
any point on the path is the vector sum of the ﬁelds produced by the individual
times  the  algebraic
conductors. Thus  the  line  integral  of  the  total
sum of  the  currents.  In  calculating  this  sum,  we  use  the  sign  rule  for  currents
described  above.  If  the  integration  path  does  not  enclose  a  particular  wire,  the
u
line integral of the  ﬁeld of that wire is zero, because the angle
for that wire
during the integration. Any
sweeps through a net change of zero rather than
conductors present that are not enclosed by a particular path may still contribute
to the value of
at every point, but the line integrals of their ﬁelds around the
path are zero.

equals

2p

m0

S
B

S
B

S
B

S
B

Thus we can replace I in Eq. (28.19) with

the algebraic sum of the cur-
rents enclosed or linked by  the  integration  path,  with  the  sum  evaluated  by
using the sign rule just described (Fig. 28.18). Our statement of Ampere’s law
is then

Iencl,

S # d l

B

S

C

= m0Iencl

(Ampere’s law)

(28.20)

I1

S # d l

S

= 0,

While we have derived Ampere’s law only for the special case of the ﬁeld of sev-
eral long, straight, parallel conductors, Eq. (28.20) is in fact valid for conductors
and paths of any shape. The general derivation is no different in principle from
what we have presented, but the geometry is more complicated.

If

AB

it  does  not necessarily  mean  that

everywhere  along
the path, only that the total current through an area bounded by the path is zero. In
Figs. 28.16c and 28.17b, the integration paths enclose no current at all; in Fig. 28.19
there  are  positive  and  negative  currents  of  equal  magnitude  through  the  area
Iencl = 0
enclosed by the path. In both cases,

and the line integral is zero.

S
B

(cid:2) 0

28.18 Ampere’s law.

Perspective view

I2

I1

I3

S
dl

S
B

Curl the fingers of
your right hand around
the integration path:
Your thumb points
in the direction of
positive current.

Arbitrary closed
curve around
conductors

Top view

Plane of
curve

I2

Iencl

 5 I1

2 I2

1 I3

I3

S
dl

S
B

Ampere’s law:  If we calculate the line integral
of the magnetic field around a closed curve, the
result equals m
0 times the total enclosed current:
rB # dl 5 m

S

S

0 Iencl.

S

S
E
S
F

CAUTION Line integrals of electric and magnetic ﬁelds In Chapter 23 we saw that the
around any closed path is equal to zero; this is a
line integral of the electrostatic ﬁeld
(cid:2) qE
statement that the electrostatic force
on a point charge q is conservative, so this
force does zero work on a charge that moves around a closed path that returns to the start-
ing point. You might think that the value of the line integral
is similarly related to
the  question  of  whether  the  magnetic force  is  conservative.  This  isn’t  the  case  at  all.
S : B
Remember that the magnetic force
on a moving charged particle is always
S
perpendicular to
is not related to the work done by the magnetic force; as
B
stated in Ampere’s law, this integral is related only to the total current through a surface
bounded by the integration path. In fact, the magnetic force on a moving charged particle
is not conservative. A conservative  force  depends  only  on  the  position  of  the  body  on
which  the  force  is  exerted,  but  the  magnetic  force  on  a  moving  charged  particle  also
depends on the velocity of the particle. ❙

S # d l

S # d l

(cid:2) qv

A B

A B

so

S
F

S

S

S

,

Equation (28.20) turns out to be valid only if the currents are steady and if no
magnetic materials or time-varying electric ﬁelds are present. In Chapter 29 we
will see how to generalize Ampere’s law for time-varying ﬁelds.

28.19 Two long, straight conductors
carrying equal currents in opposite direc-
tions. The conductors are seen end-on, and
the integration path is counterclockwise.
A B
The line integral
gets zero contri-
bution from the upper and lower segments,
a positive contribution from the left seg-
ment, and a negative contribution from the
right segment; the net integral is zero.

S # d l

S

S
dl

S
B

S
dl

S
B

S
B
S
dl

S
B

S
dl

S
dl

(cid:3)I
S
dl

S
B

S
B

S
B

S
dl

(cid:5)I

S
dl

S
B

S
dl

S
B

S
B

S
dl
