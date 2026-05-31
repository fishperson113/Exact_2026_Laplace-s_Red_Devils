Example 29.10

The Faraday disk dynamo

29.5 Induced Electric Fields

971

Figure 29.16 shows a conducting disk with radius R that lies in the
xy-plane  and  rotates  with  constant  angular  velocity
about  the
z-axis. The disk is in a uniform, constant  ﬁeld in the z-direction.
Find the induced emf between the center and the rim of the disk.

S
B

v

SOLUTION

IDENTIFY  and SET  UP:  A motional  emf  arises  because  the  con-
. The complication is that different
ducting disk moves relative to

S
B

v

29.16 A conducting disk with radius R rotating at an angular
speed
in a magnetic ﬁeld  The emf is induced along radial
lines of the disk and is applied to an external circuit through the
two sliding contacts labeled b.

S
B

.

v,

parts  of  the  disk  move  at  different  speeds
depending  on  their
distance from the rotation axis. We’ll address this by considering
small  segments  of  the  disk  and  integrating  their  contributions  to
determine our target variable, the emf between the center and the
rim.  Consider  the  small  segment  of  the  disk  shown  in  red  in
Fig. 29.16 and labeled by its velocity vector  The magnetic force
S : B
v
per unit charge on this segment is
which points radially out-
,
ward from the center of the disk. Hence the induced emf tends to
make a current ﬂow radially outward, which tells us that the mov-
ing conducting path to think about here is a straight line from the
center to the rim. We can ﬁnd the emf from each small disk seg-
dE = 1v
ment along this line using
and then integrate
to ﬁnd the total emf.

2 # d l

S : B

S
v
.

S

S

S

y

R

r

dr
S
B

b

S
B

S
B

v

z b

S
B

S
v

x

Speed of small radial segment
of length dr at radius r is v (cid:4) vr.

Emf induced across this segment is
dE (cid:4) vB dr (cid:4) vBr dr.

I

S
EXECUTE: The length vector
d l
segment points radially outward, in the same direction as
The vectors
v = vr.
emf  is  the  integral  of
1r = R2

(of length dr) associated with the
S
S : B
v
.
S
v
is
. The total
to  the  rim

The emf from the segment is then
dE

are perpendicular, and the magnitude of

dE = vBr dr
1r = 02

from  the  center

and

S
B

S
v

:

R
vBr dr = 1
2

vBR2

E =

L
0

EVALUATE: We can use this device as a source of emf in a circuit by
completing the circuit through two stationary brushes (labeled b in
the ﬁgure) that contact the disk and its conducting shaft as shown.
Such a disk is called a Faraday disk dynamo or a homopolar gen-
erator. Unlike  the  alternator  in  Example  29.3,  the  Faraday  disk
dynamo  is  a  direct-current  generator;  it  produces  an  emf  that  is
constant  in  time.  Can  you  use  Lenz’s  law  to  show  that  for  the
direction of rotation in Fig. 29.16, the current in the external circuit
must be in the direction shown?

Test Your Understanding of Section 29.4 The earth’s magnetic ﬁeld
points toward (magnetic) north. For simplicity, assume that the ﬁeld has no verti-
cal component (as is the case near the earth’s equator). (a) If you hold a metal rod
in your hand and walk toward the east, how should you orient the rod to get the maxi-
mum motional emf between its ends? (i) east-west; (ii) north-south; (iii) up-down; (iv)
you get the same motional emf with all of these orientations. (b) How should you hold it
to get zero emf as you walk toward the east? (i) east-west; (ii) north-south; (iii) up-down;
(iv) none of these. (c) In which direction should you travel so that the motional emf
across the rod is zero no matter how the rod is oriented? (i) west; (ii) north;
(iii) south; (iv) straight up; (v) straight down.

❙

29.5 Induced Electric Fields

When a conductor moves in a magnetic ﬁeld, we can understand the induced emf
on the basis of magnetic forces on charges in the conductor, as described in Sec-
tion 29.4. But an induced emf also occurs when there is a changing ﬂux through a
stationary conductor. What is it that pushes the charges around the circuit in this
type of situation?

As an example, let’s consider the situation shown in Fig. 29.17. A long, thin
n
turns per unit length is encircled at its
solenoid with cross-sectional area A and
center by a circular conducting loop. The galvanometer G measures the current in
S
B
the loop. A current I in the winding of the solenoid sets up a magnetic ﬁeld
along the solenoid axis, as shown, with magnitude  B as calculated in Example
n
is the number of turns per unit length.
28.9 (Section 28.7):

where

B = m0nI,

972

CHAPTER 29 Electromagnetic Induction

dI/dt.

The magnetic ﬂux in the sole-

29.17 (a) The windings of a long sole-
noid carry a current I that is increasing at a
rate
noid is increasing at a rate
changing ﬂux passes through a wire loop.
An emf
loop, inducing a current
that is measured
by the galvanometer G. (b) Cross-sectional
view.

is induced in the
I¿

E = - d£B/dt

d£B/dt,

and this

(a)

A

(b)

I, dI
dt

Galvanometer

Wire loop

I'

Solenoid

I, dI
dt

G

S
B

Blue cylinder shows region
S
with magnetic field B.

I

S
E

S
E

G

r

S
B

S
E

If we neglect the small ﬁeld outside the solenoid and take the area vector
point in the same direction as

S
A
through the loop is

S
B

to

£B

,
then the magnetic ﬂux
£B = BA = m0nIA

When  the  solenoid  current  I changes  with  time,  the  magnetic  ﬂux
also
changes, and according to Faraday’s law the induced emf in the loop is given by

£B

E = -

d£B
dt

= - m0nA

dI
dt

(29.8)

If the total resistance of the loop is R, the induced current in the loop, which we
may call

I¿ = E/R.

I¿,

is

But what force makes the charges move around the wire loop? It can’t be a
magnetic force because the loop isn’t even in a magnetic ﬁeld. We are forced to
conclude that there has to be an induced electric ﬁeld in the conductor caused by
the  changing  magnetic  ﬂux. This  may  be  a  little  jarring;  we  are  accustomed  to
thinking about electric ﬁeld as being caused by electric charges, and now we are
saying that a changing magnetic ﬁeld somehow acts as a source of electric ﬁeld.
Furthermore,  it’s  a  strange  sort  of  electric  ﬁeld.  When  a  charge  q goes  once
around the loop, the total work done on it by the electric ﬁeld must be equal to q
times the emf  That is, the electric ﬁeld in the loop is not conservative, as we
around a closed path is
used the term in Chapter 23, because the line integral of
S
not zero. Indeed, this line integral, representing the work done by the induced
E
ﬁeld per unit charge, is equal to the induced emf

S
E

E:

E.

S # d l

E

S

C

= E

(29.9)

From Faraday’s law the emf
netic ﬂux through the loop. Thus for this case we can restate Faraday’s law as

is also the negative of the rate of change of mag-

E

S # d l

E

S

C

= -

d£B
dt

    (stationary integration path)

(29.10)

Note that Faraday’s law is always true in the form
in Eq. (29.10) is valid only if the path around which we integrate is stationary.

the form given

E = - d£B/dt;

As an example of a situation to which Eq. (29.10) can be applied, consider the
stationary circular loop in Fig. 29.17b, which we take to have radius r. Because
of  cylindrical  symmetry,  the  electric  ﬁeld
has  the  same  magnitude  at  every
point on the circle and is tangent to it at each point. (Symmetry would also permit
the ﬁeld to be radial, but then Gauss’s law would require the presence of a net
charge  inside  the  circle,  and  there  is  none.)  The  line  integral  in  Eq.  (29.10)
becomes  simply  the  magnitude  E times  the  circumference
of  the  loop,
AE

and Eq. (29.10) gives

S # d l

= 2prE,

2pr

S
E

S

E = 1
2pr

`

d£B
dt

`

(29.11)

S
E

S

S # d l

The directions of
S
S
E
B
has to have the direction shown when
d£B>dt
AE
has to be negative when
used  to  ﬁnd  the  induced  electric  ﬁeld  inside the  solenoid  when  the  solenoid
ﬁeld is changing; we leave the details to you (see Exercise 29.35).

at points on the loop are shown in Fig. 29.17b. We know that
in the solenoid is increasing, because
is positive. The same approach can be
S
B

Nonelectrostatic Electric Fields
Now let’s summarize what we’ve learned. Faraday’s law, Eq. (29.3), is valid for
two rather different situations. In one, an emf is induced by magnetic forces on
charges  when  a  conductor  moves  through  a  magnetic  ﬁeld.  In  the  other,  a

29.5 Induced Electric Fields

973

S

S
E

AE

S # d l

time-varying  magnetic  ﬁeld  induces  an  electric  ﬁeld  in  a  stationary  conductor
and hence induces an emf; in fact, the  ﬁeld is induced even when no conductor
S
E
is present. This  ﬁeld differs from an electrostatic ﬁeld in an important way. It is
nonconservative; the line integral
around a closed path is not zero, and
when a charge moves around a closed path, the ﬁeld does a nonzero amount of
work on it. It follows that for such a ﬁeld the concept of potential has no mean-
ing. We call such a ﬁeld a nonelectrostatic ﬁeld. In contrast, an electrostatic ﬁeld
is always conservative, as we discussed in Section 23.1, and always has an asso-
ciated potential function. Despite this difference, the fundamental effect of any
S
electric ﬁeld is to exert a force
on a charge q. This relationship is valid
is a conservative ﬁeld produced by a charge distribution or a noncon-
whether
servative ﬁeld caused by changing magnetic ﬂux.

(cid:2) qE

S
E

S
F

So a changing magnetic ﬁeld acts as a source of electric ﬁeld of a sort that we
cannot produce with any static charge distribution. This may seem strange, but
it’s the way nature behaves. What’s more, we’ll see in Section 29.7 that a chang-
ing electric ﬁeld acts as a source of magnetic ﬁeld. We’ll explore this symmetry
between the two ﬁelds in greater detail in our study of electromagnetic waves in
Chapter 32.

If any doubt remains in your mind about the reality of magnetically induced
electric  ﬁelds,  consider  a  few  of  the  many  practical  applications  (Fig.  29.18).
Pickups in electric guitars use currents induced in stationary pickup coils by the
vibration of nearby ferromagnetic strings. Alternators in most cars use rotating
magnets to induce currents in stationary coils. Whether we realize it or not, mag-
netically induced electric ﬁelds play an important role in everyday life.

29.18 Applications of induced electric ﬁelds. (a) Data are stored on a computer hard disk in a pattern of magnetized areas on the sur-
face of the disk. To read these data, a coil on a movable arm is placed next to the spinning disk. The coil experiences a changing mag-
netic ﬂux, inducing a current whose characteristics depend on the pattern coded on the disk. (b) This hybrid automobile has both a
gasoline engine and an electric motor. As the car comes to a halt, the spinning wheels run the motor backward so that it acts as a genera-
tor. The resulting induced current is used to recharge the car’s batteries. (c) The rotating crankshaft of a piston-engine airplane spins a
magnet, inducing an emf in an adjacent coil and generating the spark that ignites fuel in the engine cylinders. This keeps the engine run-
ning even if the airplane’s other electrical systems fail.

(a)

(b)

(c)

Example 29.11

Induced electric fields

Suppose the long solenoid in Fig. 29.17a has 500 turns per meter
The  current  in  its  windings  is
and  cross-sectional  area
increasing at
(a) Find the magnitude of the induced emf
in the wire loop outside the solenoid. (b) Find the magnitude of the
induced electric ﬁeld within the loop if its radius is 2.0 cm.

100 A>s.

4.0 cm2.

SOLUTION

IDENTIFY and SET UP: As in Fig. 29.17b, the increasing magnetic
ﬁeld  inside  the  solenoid  causes  a  change  in  the  magnetic  ﬂux
through the wire loop and hence induces an electric ﬁeld
around
E
the  loop.  Our  target  variables  are  the  induced  emf
and  the
electric-ﬁeld magnitude E. We use Eq. (29.8) to determine the emf.

S
E

Determining the ﬁeld magnitude E is simpliﬁed because the loop
and the solenoid share the same central axis. Hence, by symmetry,
the electric ﬁeld is tangent to the loop and has the same magnitude
all  the  way  around  its  circumference.  We  can  therefore  use  Eq.
(29.9) to ﬁnd E.

EXECUTE: (a) From Eq. (29.8), the induced emf is

E = -

d£B
dt

= - m0nA

dI
dt
= - 14p * 10-7 Wb>A # m21500 turns>m2

* 14.0 * 10-4 m221100 A>s2

= - 25 * 10-6 Wb>s = - 25 * 10-6 V = - 25 mV

Continued
