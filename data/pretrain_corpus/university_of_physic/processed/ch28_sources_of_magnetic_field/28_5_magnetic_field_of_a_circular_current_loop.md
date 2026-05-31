932

CHAPTER 28 Sources of Magnetic Field

deﬁnition of the coulomb, which is the amount of charge transferred in one sec-
ond by a current of one ampere.

This is an operational deﬁnition; it gives us an actual experimental procedure
for measuring current and deﬁning a unit of current. For high-precision standardiza-
tion of the ampere, coils of wire are used instead of straight wires, and their separa-
tion is only a few centimeters. Even more precise measurements of the standardized
ampere are possible using a version of the Hall effect (see Section 27.9).

Mutual forces of attraction exist not only between wires carrying currents in
the same direction, but also between the longitudinal elements of a single current-
carrying conductor. If the conductor is a liquid or an ionized gas (a plasma), these
forces result in a constriction of the conductor. This is called the pinch effect. The
high temperature produced by the pinch effect in a plasma has been used in one
technique to bring about nuclear fusion.

Example 28.5

Forces between parallel wires

Two straight, parallel, superconducting wires 4.5 mm apart carry
equal currents of 15,000 A in opposite directions. What force, per
unit length, does each wire exert on the other?

SOLUTION

IDENTIFY  and SET  UP: Figure 28.10 shows the situation. We ﬁnd
F L, the magnetic force per unit length of wire, using Eq. (28.11).

>

28.10 Our sketch for this problem.

EXECUTE: The conductors repel each other because the currents are
in opposite directions. From Eq. (28.11) the force per unit length is

=

F
L

m0II¿
2pr

=

14p * 10-7 T # m>A2115,000 A22
12p214.5 * 10-3 m2

= 1.0 * 104 N>m

EVALUATE: This is a large force, more than one ton per meter. Cur-
rents and separations of this magnitude are used in superconduct-
ing electromagnets in particle accelerators, and mechanical stress
analysis is a crucial part of the design process.

I

28.11 This electromagnet contains a
current-carrying coil with numerous turns
of wire. The resulting magnetic ﬁeld can
pick up large quantities of steel bars and
other iron-bearing items.

Test Your Understanding of Section 28.4 A solenoid is a wire wound
into a helical coil. The ﬁgure at left shows a solenoid that carries a current I.
(a) Is the magnetic force that one turn of the coil exerts on an adjacent turn (i)
attractive, (ii) repulsive, or (iii) zero? (b) Is the electric force that one turn of the coil
exerts on an adjacent turn (i) attractive, (ii) repulsive, or (iii) zero? (c) Is the magnetic
force between opposite sides of the same turn of the coil (i) attractive, (ii) repulsive, or
(iii) zero? (d) Is the electric force between opposite sides of the same turn of the
coil (i) attractive, (ii) repulsive, or (iii) zero?

❙

28.5 Magnetic Field of a Circular Current Loop

If you look inside a doorbell, a transformer, an electric motor, or an electromag-
net (Fig. 28.11), you will ﬁnd coils of wire with a large number of turns, spaced
so closely that each turn is very nearly a planar circular loop. A current in such a
coil is used to establish a magnetic ﬁeld. So it is worthwhile to derive an expres-
sion for the magnetic ﬁeld produced by a single circular conducting loop carrying
a current or by N closely spaced circular loops forming a coil. In Section 27.7 we
considered the force and torque on such a current loop placed in an external mag-
netic  ﬁeld  produced  by  other  currents;  we  are  now  about  to  ﬁnd  the  magnetic
ﬁeld produced by the loop itself.

Figure 28.12 shows a circular conductor with radius a. A current I is led into
and out of the loop through two long, straight wires side by side; the currents in
these  straight  wires  are  in  opposite  directions,  and  their  magnetic  ﬁelds  very
nearly cancel each other (see Example 28.4 in Section 28.3).

28.5 Magnetic Field of a Circular Current Loop

933

We can use the law of Biot and Savart, Eq. (28.5) or (28.6), to ﬁnd the mag-
netic ﬁeld at a point P on the axis of the loop, at a distance x from the center. As
S
dB
the  ﬁgure  shows,
r 2 = x 2 + a2,
caused  by  this  particular  element
the magnitude dB of the ﬁeld due to element

and  are  perpendicular,  and  the  direction  of  the  ﬁeld

lies  in  the  xy-plane.  Since

S
d l

S
d l

S
d l

is

rN

The components of the vector

dB =

S
dB

m0I
4p
are
m0I
4p
m0I
4p

dl
1x 2 + a22

dl
1x 2 + a22

dl
1x 2 + a22

(28.12)

(28.13)

(28.14)

a
1x 2 + a221>2
x
1x 2 + a221>2

dBx = dB cos u =

dBy = dB sin u =

S
B

The total ﬁeld

at P has only an x-component (it is perpendicular to the plane
of the loop). Here’s why: For every element
there is a corresponding element
on the opposite side of the loop, with opposite direction. These two elements give
equal contributions to the x-component of
given by Eq. (28.13), but opposite
components perpendicular to the x-axis. Thus all the perpendicular components
cancel and only the x-components survive.

S
,
dB

S
d l

To  obtain  the  x-component  of  the  total  ﬁeld

we  integrate  Eq.  (28.13),
’s around the loop. Everything in this expression except dl is

including all the
constant and can be taken outside the integral, and we have

S
d l

S
,
B

Bx =

m0I
4p

L

a dl
1x 2 + a223>2

=

m0Ia
4p1x 2 + a223>2 L

dl

The  integral  of  dl is  just  the  circumference  of  the  circle,
ﬁnally get

1 dl = 2pa,

and  we

Bx =

m0Ia2
21x 2 + a223>2

(on the axis of a circular loop)

(28.15)

The direction of the magnetic ﬁeld on the axis of a current-carrying loop is
given by a right-hand rule. If you curl the ﬁngers of your right hand around the
loop in the direction of the current, your right thumb points in the direction of the
ﬁeld (Fig. 28.13).

Magnetic Field on the Axis of a Coil
Now suppose that instead of the single loop in Fig. 28.12 we have a coil consist-
ing of N loops, all with the same radius. The loops are closely spaced so that the
plane of each loop is essentially the same distance x from the ﬁeld point P. Then
the total ﬁeld is N times the ﬁeld of a single loop:
m0NIa2
21x 2 + a223>2

(on the axis of N circular loops)

Bx =

(28.16)

The factor N in Eq. (28.16) is the reason coils of wire, not single loops, are used
to produce strong magnetic ﬁelds; for a desired ﬁeld strength, using a single loop
might require a current I so great as to exceed the rating of the loop’s wire.
Bx
the center of the loop or coil:

as a function of x. The maximum value of

Figure 28.14 shows a graph of

the ﬁeld is at

x = 0,

,

causes the ﬁeld

28.12 Magnetic ﬁeld on the axis of a
circular loop. The current in the segment
S
S
which lies in the
d l
dB
S
xy-plane. The currents in other
’s cause
d l
S
’s with different components perpendi-
dB
cular to the x-axis; these components add
to zero. The x-components of the
combine to give the total  ﬁeld at point P.

S
dB

S
B

’s

y

S
dl

a

O

I

z

I

I

r^

u

S
r

2 u

p
2
dBy

S
dB

u

x

dBx

x

p
2

2 u

P

PhET: Faraday’s Electromagnetic Lab
PhET: Magnets and Electromagnets
ActivPhysics 13.2: Magnetic Field of a Loop

28.13 The right-hand rule for the
direction of the magnetic ﬁeld produced
on the axis of a current-carrying coil.

S
B

Right-hand rule for the
magnetic field produced by
a current in a loop:

I

II

I

When the fingers of your right
hand curl in the direction of I,
your right thumb points in the
S
direction of B.

S
B

28.14 Graph of the magnetic ﬁeld along
the axis of a circular coil with N turns. When
x is much larger than a, the ﬁeld magnitude
decreases approximately as 1/x 3.

Bx

Bmax 5

m

0NI
2a

1
2

Bmax

Bx =

m0NI
2a

(at the center of N circular loops)

(28.17)

As we go out along the axis, the ﬁeld decreases in magnitude.

(cid:5)3a

(cid:5)2a

(cid:5)a

O

a

2a

3a

x

934

CHAPTER 28 Sources of Magnetic Field

Application Magnetic Fields for MRI
The diagnostic technique called MRI, or mag-
netic resonance imaging (see Section 27.7),
requires a magnetic ﬁeld of about 1.5 T. In a
typical MRI scan, the patient lies inside a coil
that produces the intense ﬁeld. The currents
required are very high, so the coils are bathed
in liquid helium at a temperature of 4.2 K to
keep them from overheating.

28.15 Magnetic ﬁeld lines produced by
the current in a circular loop. At points on
the axis the  ﬁeld has the same direction
as the magnetic moment of the loop.

S
B

z

O

x

P

x

I

S
B

y

In  Section  27.7  we  defined  the  magnetic  dipole  moment

(or magnetic
moment)  of  a  current-carrying  loop  to  be  equal  to  IA,  where  A is  the  cross-
sectional area of the loop. If there are N loops, the total magnetic moment is
so  the  magnetic
NIA.  The  circular  loop  in  Fig.  28.12 has  area
moment  of  a  single  loop  is
Substituting
these results into Eqs. (28.15) and (28.16), we find that both of these expres-
sions can be written as

m = NIpa2.

for  N loops,

m = Ipa2;

A = pa2,

m

Bx =

m0m
2p1x 2 + a223>2

(on the axis of any number
of circular loops)

(28.18)

We described a magnetic dipole in Section 27.7 in terms of its response to a mag-
netic ﬁeld produced by currents outside the dipole. But a magnetic dipole is also
a source of magnetic ﬁeld; Eq. (28.18) describes the magnetic ﬁeld produced by a
magnetic  dipole  for  points  along  the  dipole  axis.  This  ﬁeld  is  directly  propor-
m.
tional to the magnetic dipole moment  Note that the ﬁeld along the x-axis is in
the same direction as the vector magnetic moment
this is true on both the pos-
itive and negative x-axis.

MS

;

CAUTION Magnetic ﬁeld of a coil Equations (28.15), (28.16), and (28.18) are valid only
on the axis of a loop or coil. Don’t attempt to apply these equations at other points! ❙

Figure  28.15 shows  some  of  the  magnetic  ﬁeld  lines  surrounding  a  circular
current loop (magnetic dipole) in planes through the axis. The directions of the
ﬁeld lines are given by the same right-hand rule as for a long, straight conductor.
Grab the conductor with your right hand, with your thumb in the direction of the
current; your ﬁngers curl around in the same direction as the ﬁeld lines. The ﬁeld
lines for the circular current loop are closed curves that encircle the conductor;
they are not circles, however.

Example 28.6 Magnetic field of a coil

A coil consisting of 100 circular loops with radius 0.60 m carries a
5.0-A current. (a) Find the magnetic ﬁeld at a point along the axis
of the coil, 0.80 m from the center. (b) Along the axis, at what dis-
tance from the center of the coil is the ﬁeld magnitude  as great as
it is at the center?

1
8

SOLUTION

IDENTIFY  and SET  UP: This problem concerns the magnetic ﬁeld
magnitude B along the axis of a current-carrying coil, so we can
use the ideas of this section, and in particular Eq. (28.16). We are
a = 0.60 m.
given
In part (a) our target
at a given value of x. In part (b) the target variable is
variable is
the value of x at which the ﬁeld has  of the magnitude that it has at
the origin.

N = 100,
Bx

I = 5.0 A,

and

1
8

EXECUTE: (a) Using

x = 0.80 m,

from Eq. (28.16) we have
14p * 10-7 T # m/A21100215.0 A210.60 m22
2310.80 m22 + 10.60 m2243>2

Bx =

= 1.1 * 10-4 T

(b) Considering Eq. (28.16), we want to ﬁnd a value of x such

that

1
1x 2 + a223>2

= 1
8

1
102 + a223>2

To solve this for x, we take the reciprocal of the whole thing and
power of both sides; the result is
then take the

2>3

x = (cid:6) 23a = (cid:6)1.04 m

EVALUATE:  We check our answer in part (a) by ﬁnding the coil’s
magnetic moment and substituting the result into Eq. (28.18):
m = NIpa2 = 1100215.0 A2p10.60 m22 = 5.7 * 102 A # m2

14p * 10-7 T # m>A215.7 * 102 A # m22
2p310.80 m22 + 10.60 m2243>2

Bx =

= 1.1 * 10-4 T

is relatively large, yet it produces a rather
The magnetic moment
small  ﬁeld,  comparable  to  that  of  the  earth.  This  illustrates  how
difﬁcult it is to produce strong ﬁelds of 1 T or more.

m
