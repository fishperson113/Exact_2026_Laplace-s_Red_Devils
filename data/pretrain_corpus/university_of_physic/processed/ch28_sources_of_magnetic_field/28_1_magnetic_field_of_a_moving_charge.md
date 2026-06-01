SOURCES OF
MAGNETIC FIELD

? The immense cylinder in this photograph is actually a current-carrying coil,

or solenoid, that generates a uniform magnetic ﬁeld in its interior as part
of an experiment at CERN, the European Organization for Nuclear Research.
If two such solenoids were joined end to end, how much stronger would the
magnetic ﬁeld become?

In Chapter 27 we studied the forces exerted on moving charges and on current-

carrying conductors in a magnetic ﬁeld. We didn’t worry about how the mag-
netic ﬁeld got there; we simply took its existence as a given fact. But how are
magnetic ﬁelds created? We know that both permanent magnets and electric cur-
rents in electromagnets create magnetic ﬁelds. In this chapter we will study these
sources of magnetic ﬁeld in detail.

We’ve learned that a charge creates an electric ﬁeld and that an electric ﬁeld
exerts a force on a charge. But a magnetic ﬁeld exerts a force only on a moving
charge. Is it also true that a charge creates a magnetic ﬁeld only when the charge
is moving? In a word, yes.

Our  analysis  will  begin  with  the  magnetic  ﬁeld  created  by  a  single  moving
point charge. We can use this analysis to determine the ﬁeld created by a small
segment of a current-carrying conductor. Once we can do that, we can in princi-
ple ﬁnd the magnetic ﬁeld produced by any shape of conductor.

Then we will introduce Ampere’s law, which plays a role in magnetism analo-
gous  to  the  role  of  Gauss’s  law  in  electrostatics. Ampere’s  law  lets  us  exploit
symmetry properties in relating magnetic ﬁelds to their sources.

Moving  charged  particles  within  atoms  respond  to  magnetic  ﬁelds  and  can
also act as sources of magnetic ﬁeld. We’ll use these ideas to understand how cer-
tain magnetic materials can be used to intensify magnetic ﬁelds as well as why
some materials such as iron act as permanent magnets.

28.1 Magnetic Field of a Moving Charge

Let’s start with the basics, the magnetic ﬁeld of a single point charge q moving
with a constant velocity
In practical applications, such as the solenoid shown
in the photo that opens this chapter, magnetic ﬁelds are produced by tremendous

S
v

.

28

LEARNING GOALS

By studying this chapter, you will

learn:

• The nature of the magnetic field

produced by a single moving

charged particle.

• How to describe the magnetic

field produced by an element of a

current-carrying conductor.

• How to calculate the magnetic

field produced by a long, straight,

current-carrying wire.

• Why wires carrying current in the

same direction attract, while wires

carrying opposing currents repel.

• How to calculate the magnetic field

produced by a current-carrying wire

bent into a circle.

• What Ampere’s law is, and what it

tells us about magnetic fields.

• How to use Ampere’s law to

calculate the magnetic field of

symmetric current distributions.

923

924

CHAPTER 28 Sources of Magnetic Field

numbers of charged particles moving together in a current. But once we under-
stand how to calculate the magnetic ﬁeld due to a single point charge, it’s a small
leap to calculate the ﬁeld due to a current-carrying wire or collection of wires.

28.1 (a) Magnetic-ﬁeld vectors due to
a moving positive point charge q. At each
S
S
point,
is perpendicular to the plane of
B
r
S
v
and its magnitude is proportional to
and
,
the sine of the angle between them. (b)
Magnetic ﬁeld lines in a plane containing
a moving positive charge.

(a) Perspective view

Right-hand rule for the magnetic field due to
a positive charge moving at constant velocity:
Point the thumb of your right hand in the
direction of the velocity. Your fingers now curl
around the charge in the direction of the
magnetic field lines. (If the charge is negative,
the field lines are in the opposite direction.)

S

S
For these field points, r and v
both lie in the beige plane, and
S
B is perpendicular to this plane.

P

S
B

rS

B 5 0

S
B

S
v

^
r

f

q

S
v

S
B

S
B

B 5 0

S
B

S
For these field points, r and v both lie in the
gold plane, and B is perpendicular to this plane.

S

S
B
S

(b) View from behind the charge

The 3 symbol
indicates that the
charge is moving into
the plane of the page
(away from you).

S
B

ƒqƒ

and to

S
E
and the direction of

As we did for electric ﬁelds, we call the location of the moving charge at a
given instant the source point and the point P where we want to ﬁnd the ﬁeld the
ﬁeld point. In Section 21.4 we found that at a ﬁeld point a distance r from a point
caused by the charge is propor-
charge q, the magnitude of the electric ﬁeld
S
1/r 2,
E
tional to the charge magnitude
(for positive q)
is along the line from source point to ﬁeld point. The corresponding relationship
for the magnetic ﬁeld
of a point charge q moving with constant velocity has
some similarities and some interesting differences.
Experiments show that the magnitude of

and to
1>r 2.
is not along the line from source point to ﬁeld point.
Instead,
is  perpendicular  to  the  plane  containing  this  line  and  the  particle’s
as shown in Fig. 28.1. Furthermore, the ﬁeld magnitude B is
velocity vector
v
also proportional to the particle’s speed  and to the sine of the angle  Thus the
magnetic ﬁeld magnitude at point P is given by

is also proportional to

But the direction of

f.

S
v
,

S
B

S
B

S
B

S
B

ƒqƒ

B =

m0
4p

ƒqƒv sin f
r 2
m0

(28.1)

m0>4p

is a proportionality constant (

where
is read as “mu-nought” or “mu-sub-
zero”).  The  reason  for  writing  the  constant  in  this  particular  way  will  emerge
shortly. We did something similar with Coulomb’s law in Section 21.3.

Moving Charge: Vector Magnetic Field
We can incorporate both the magnitude and direction of
into a single vector
equation using the vector product. To avoid having to say “the direction from the
rn
source q to the ﬁeld point P” over and over, we introduce a unit vector  (“r-hat”)
rn
for the same pur-
that points from the source point to the ﬁeld point. (We used
S
from the source to
r
pose in Section 21.4.) This unit vector is equal to the vector
S
B
Then the  ﬁeld of a moving
the ﬁeld point divided by its magnitude:
point charge is

rn (cid:2) r

S>r.

S
B

S
B

(cid:2)

m0
4p

S : rn
qv
r 2

(magnetic field of a point charge
with constant velocity)

(28.2)

rn
Figure 28.1 shows the relationship of
to P and also shows the magnetic ﬁeld
S
at several points in the vicinity of the charge. At all points along a line through
B
S
v
the charge parallel to the velocity
at all such
,
S
points. At any distance r from q,  has its greatest magnitude at points lying in the
B
plane perpendicular to
If q is negative,
, because there
the directions of

are opposite to those shown in Fig. 28.1.

the ﬁeld is zero because

sin f = 1.

sin f = 0

f = 90°

and

S
B

S
v

Moving Charge: Magnetic Field Lines
A point charge in motion also produces an electric ﬁeld, with ﬁeld lines that radiate
outward from a positive charge. The magnetic ﬁeld lines are completely different.
S
v
,
For a point charge moving with velocity
the magnetic ﬁeld lines are circles cen-
S
v
tered on the line of
and lying in planes perpendicular to this line. The ﬁeld-line
directions for a positive charge are given by the following right-hand rule, one of
several that we will encounter in this chapter: Grasp the velocity vector  with your
your ﬁngers then
right hand so that your right thumb points in the direction of
curl around the line of
in the same sense as the magnetic ﬁeld lines, assuming q is
positive. Figure 28.1a shows parts of a few ﬁeld lines; Fig. 28.1b shows some ﬁeld
lines in a plane through q, perpendicular to
If the point charge is negative, the
directions of the ﬁeld and ﬁeld lines are the opposite of those shown in Fig. 28.1.

S
v
;

S
v
.

S
v

S
v

28.1 Magnetic Field of a Moving Charge

925

S
B

Equations (28.1) and (28.2) describe the  ﬁeld of a point charge moving with
constant velocity. If the charge accelerates, the ﬁeld can be much more compli-
cated. We won’t need these more complicated results for our purposes. (The mov-
ing charged particles that make up a current in a wire accelerate at points where
the wire bends and the direction of
of
the drift velocity in a conductor is typically very small, the centripetal accelera-
tion

is so small that we can ignore its effects.)

changes. But because the magnitude

2>r

vd

S
v

vd

As we discussed in Section 27.2, the unit of B is one tesla (1 T):

1 T = 1 N # s>C # m = 1 N>A # m

Using this with Eq. (28.1) or (28.2), we ﬁnd that the units of the constant

In SI units the numerical value of

1 N # s2>C2 = 1 N>A2 = 1 Wb>A # m = 1 T # m>A
is exactly

4p * 10-7.

Thus

m0 = 4p * 10-7 N # s2>C2 = 4p * 10-7 Wb>A # m

m0

m0

are

(28.3)

= 4p * 10-7 T # m>A
m0

has exactly this numerical value! In fact this is a
It may seem incredible that
deﬁned value  that  arises  from  the  deﬁnition  of  the  ampere,  as  we’ll  discuss  in
Section 28.4.

We mentioned in Section 21.3 that the constant

related to the speed of light c:

1>4pP0

in Coulomb’s law is

k =

1
4pP0

= 110-7 N # s2>C22c2

When we study electromagnetic waves in Chapter 32, we will ﬁnd that their speed
of propagation in vacuum, which is equal to the speed of light

is given by

c,

c2 =

1
P0m0

(28.4)

substitute the resulting expression
If we solve the equation
into Eq. (28.4), and solve for
stated above. This
discussion is a little premature, but it may give you a hint that electric and mag-
netic ﬁelds are intimately related to the nature of light.

we indeed get the value of

k = 1>4pP0
m0,

P0,

for

m0

Example 28.1

Forces between two moving protons

Two  protons  move  parallel  to  the  x-axis  in  opposite  directions
(Fig.  28.2)  at  the  same  speed
(small  compared  to  the  speed  of
light c). At the instant shown, ﬁnd the electric and magnetic forces
on the upper proton and compare their magnitudes.

v

SOLUTION

FE

IDENTIFY and SET UP: Coulomb’s law [Eq. (21.2)] gives the elec-
tric  force
on  the  upper  proton.  The  magnetic  force  law  [Eq.
(27.2)] gives the magnetic force on the upper proton; to use it, we
must ﬁrst use Eq. (28.2) to ﬁnd the magnetic ﬁeld that the lower
proton produces at the position of the upper proton. The unit vector
from the lower proton (the source) to the position of the upper pro-
ton is

rn (cid:2) ≥n.

EXECUTE: From Coulomb’s law, the magnitude of the electric force
on the upper proton is

FE =

1
4p P0

q 2
r 2

28.2 Electric and magnetic forces between two moving protons.

y

S
FE

S

2v

S
FB

q

S
B

r^

S
v

q

z

r

x

Continued
