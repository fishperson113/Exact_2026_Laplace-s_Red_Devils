29.4 Motional Electromotive Force

969

29.15 A conducting rod moving in a
uniform magnetic ﬁeld. (a) The rod, the
velocity, and the ﬁeld are mutually perpen-
dicular. (b) Direction of induced current in
the circuit.

(a) Isolated moving rod
a
+

S
B

FB

5 qvB

L

q

S
v

Charges in the
moving rod are
acted upon by
a magnetic force
S
FB ...

FE

5 qE

–
b

... and the resulting
charge separation
creates a canceling
electric force FE.

S

(b) Rod connected to stationary conductor

S
B

a

E

S
v

I

I

b
The motional emf E in the moving rod creates
an electric field in the stationary conductor.

ActivPhysics 13.10: Motional EMF

Test Your Understanding of Section 29.3 (a) Suppose the magnet in
Fig. 29.14a were stationary and the loop of wire moved upward. Would the
induced current in the loop be (i) in the same direction as shown in Fig. 29.14a,
(ii) in the direction opposite to that shown in Fig. 29.14a, or (iii) zero? (b) Suppose the
magnet and loop of wire in Fig. 29.14a both moved downward at the same velocity.
Would the induced current in the loop be (i) in the same direction as shown in Fig.
29.14a, (ii) in the direction opposite to that shown in Fig. 29.14a, or (iii) zero?

❙

29.4 Motional Electromotive Force

We’ve seen several situations in which a conductor moves in a magnetic ﬁeld, as
in the generators discussed in Examples 29.3 through 29.6. We can gain additional
insight into the origin of the induced emf in these situations by considering the
magnetic  forces  on  mobile  charges  in  the  conductor.  Figure  29.15a  shows  the
same moving rod that we discussed in Example 29.5, separated for the moment
from the U-shaped conductor. The magnetic ﬁeld
is uniform and directed into
S
.
the page, and we move the rod to the right at a constant velocity  A charged par-
with magnitude
ticle q in the rod then experiences a magnetic force
F = ƒqƒvB.
We’ll assume in the following discussion that q is positive; in that case
the direction of this force is upward along the rod, from b toward a.

Sv
S : B

(cid:2) qv

S
B

S
F

This magnetic force causes the free charges in the rod to move, creating an
excess of positive charge at the upper end a and negative charge at the lower end
S
E
b. This in turn creates an electric ﬁeld  within the rod, in the direction from a
toward b (opposite to the magnetic force). Charge continues to accumulate at the
ends  of  the  rod  until
becomes  large  enough  for  the  downward  electric  force
(with magnitude qE) to cancel exactly the upward magnetic force (with magni-
tude

and the charges are in equilibrium.

Then

S
E

qvB).

qE = qvB
The magnitude of the potential difference

is equal to the electric-
ﬁeld magnitude E multiplied by the length L of the rod. From the above discus-
sion,

E = vB,

Vab = Va - Vb

so

Vab = EL = vBL

(29.5)

with point a at higher potential than point b.

Now suppose the moving rod slides along a stationary  U-shaped conductor,
forming a complete circuit (Fig. 29.15b). No magnetic force acts on the charges
in the stationary U-shaped conductor, but the charge that was near points a and b
redistributes itself along the stationary conductor, creating an electric ﬁeld within
it. This  ﬁeld  establishes  a  current  in  the  direction  shown. The  moving  rod  has
become a source of electromotive force; within it, charge moves from lower to
higher potential, and in the remainder of the circuit, charge moves from higher to
E.
lower potential. We call this emf a motional electromotive force, denoted by
From the above discussion, the magnitude of this emf is

E = vBL

(motional emf; length and velocity
S
B
perpendicular to uniform )

(29.6)

corresponding to a force per unit charge of magnitude
acting for a distance L
along  the  moving  rod.  If  the  total  circuit  resistance  of  the  U-shaped  conductor
vBL = IR.
and the sliding rod is R, the induced current I in the circuit is given by
This  is  the  same  result  we  obtained  in  Section  29.2  using  Faraday’s  law,  and
indeed  motional  emf  is  a  particular  case  of  Faraday’s  law,  one  of  the  several
examples described in Section 29.2.

vB

The emf associated with the moving rod in Fig. 29.15 is analogous to that of
a battery with its positive terminal at a and its negative terminal at b, although
the origins of the two emfs are quite different. In each case a nonelectrostatic
force acts on the charges in the device, in the direction from b to a, and the emf
is the work per unit charge done by this force when a charge moves from b to a in
the device. When the device is connected to an external circuit, the direction of

970

CHAPTER 29 Electromagnetic Induction

current is from b to a in the device and from a to b in the external circuit. While
we have discussed motional emf in terms of a closed circuit like that in Fig. 29.15b,
a motional emf is also present in the isolated moving rod in Fig. 29.15a, in the
same way that a battery has an emf even when it’s not part of a circuit.

The direction of the induced emf in Fig. 29.15 can be deduced by using Lenz’s
law, even if (as in Fig. 29.15a) the conductor does not form a complete circuit. In
this case we can mentally complete the circuit between the ends of the conductor
and use Lenz’s law to determine the direction of the current. From this we can
deduce the polarity of the ends of the open-circuit conductor. The direction from
the
within the conductor is the direction the current would
have if the circuit were complete.

- end

+ end

to the

v
in meters per second, B in teslas, and L
You should verify that if we express
1 V = 1 J/C.2
is in volts. (Recall that

in meters, then

E

Motional emf: General Form
We can generalize the concept of motional emf for a conductor with any shape,
moving in any magnetic ﬁeld, uniform or not (assuming that the magnetic ﬁeld at
of the conductor, the contri-
each point does not vary with time). For an element
S
S : B
v
bution
(the magnetic force per unit charge) parallel to

to the emf is the magnitude dl multiplied by the component of

that is,

S
;
d l

S
d l

dE

dE = 1v

S : B

S

2 # d l

S

For any closed conducting loop, the total emf is

S

S : B
1v

2 # d l

S

E =

C

(motional emf; closed conducting loop) (29.7)

E = - d£B>dt.

This  expression  looks  very  different  from  our  original  statement  of  Faraday’s
law, Eq. (29.3), which stated that
In fact, though, the two state-
ments are equivalent. It can be shown that the rate of change of magnetic ﬂux
through a moving conducting loop is always given by the negative of the expres-
sion in Eq. (29.7). Thus this equation gives us an alternative formulation of Fara-
day’s  law.  This  alternative  is  often  more  convenient  than  the  original  one  in
problems with moving conductors. But when we have stationary conductors in
E = - d£B>dt
changing magnetic ﬁelds, Eq. (29.7) cannot be used; in this case,
is the only correct way to express Faraday’s law.

Example 29.9 Motional emf in the slidewire generator

is

2.5 m>s,

Suppose the moving rod in Fig. 29.15b is 0.10 m long, the velocity
v
and B is
0.60 T. Find the motional emf, the induced current, and the force
acting on the rod.

the total resistance of the loop is

0.030 Æ,

SOLUTION

E

IDENTIFY  and SET  UP:  The  ﬁrst  target  variable  is  the  motional
due to the rod’s motion, which we’ll ﬁnd using Eq. (29.6).
emf
and  the  resistance  R.
We’ll  ﬁnd  the  current  from  the  values  of
The force on the rod is a magnetic force, exerted by
on the cur-
rent in the rod; we’ll ﬁnd this force using

S
B
S
: B

S
IL

S
F

(cid:2)

E

.

EXECUTE: From Eq. (29.6) the motional emf is

E = vBL = 12.5 m>s210.60 T210.10 m2 = 0.15 V

The induced current in the loop is

I =

E

R

= 0.15 V
0.030 Æ

= 5.0 A

S
F

(cid:2)

S
IL

S

: B

b

to

In the expression for the magnetic force,
, the vec-
S
tor  points in the same direction as the induced current in the rod
L
(from
in Fig. 29.15). Applying the right-hand rule for vector
products  shows  that  this  force  is  directed  opposite to  the  rod’s
are perpendicular, the magnetic force has
motion. Since
magnitude

and

S
B

S
L

a

F = ILB = 15.0 A210.10 m210.60 T2 = 0.30 N

EVALUATE:  We  can  check  our  answer  for  the  direction  of
by
using  Lenz’s  law.  If  we  take  the  area  vector
to  point  into  the
plane of the loop, the magnetic ﬂux is positive and increasing as
the  rod  moves  to  the  right  and  increases  the  area  of  the  loop.
Lenz’s law tells us that a force appears to oppose this increase in
ﬂux. Hence the force on the rod is to the left, opposite its motion.

S
A

S
F
