23

ELECTRIC POTENTIAL

LEARNING GOALS

By studying this chapter, you will

learn:

• How to calculate the electric poten-

tial energy of a collection of charges.

• The meaning and significance of

electric potential.

• How to calculate the electric potential

that a collection of charges produces

at a point in space.

• How to use equipotential surfaces to

visualize how the electric potential

varies in space.

• How to use electric potential to

calculate the electric field.

754

? In one type of welding, electric charge ﬂows between the welding tool and the

metal pieces that are to be joined together. This produces a glowing arc
whose high temperature fuses the pieces together. Why must the tool be held
close to the pieces being welded?

This  chapter  is  about  energy  associated  with  electrical  interactions.  Every

time you turn on a light, listen to an MP3 player, or talk on a mobile phone,
you are using electrical energy, an indispensable ingredient of our techno-
logical  society.  In  Chapters  6 and  7 we  introduced  the  concepts  of  work and
energy in the context of mechanics; now we’ll combine these concepts with what
we’ve learned about electric charge, electric forces, and electric ﬁelds. Just as we
found  for  many  problems  in  mechanics,  using  energy  ideas  makes  it  easier  to
solve a variety of problems in electricity.

When  a  charged  particle  moves  in  an  electric  ﬁeld,  the  ﬁeld  exerts  a  force
that can do work on the particle. This work can always be expressed in terms of
electric  potential  energy.  Just  as  gravitational  potential  energy  depends  on  the
height of a mass above the earth’s surface, electric potential energy depends on
the  position  of  the  charged  particle  in  the  electric  ﬁeld.  We’ll  describe  electric
potential energy using a new concept called electric potential, or simply potential.
In  circuits,  a  difference  in  potential  from  one  point  to  another  is  often  called
voltage. The concepts of potential and voltage are crucial to understanding how
electric circuits work and have equally important applications to electron beams
used in cancer radiotherapy, high-energy particle accelerators, and many other
devices.

23.1 Electric Potential Energy

The concepts of work, potential energy, and conservation of energy proved to
be extremely useful in our study of mechanics. In this section we’ll show that
these  concepts  are  just  as  useful  for  understanding  and  analyzing  electrical
interactions.

Let’s begin by reviewing three essential points from Chapters 6 and 7. First,
acts on a particle that moves from point a to point b, the work

S
F

when a force
WaSb

done by the force is given by a line integral:

WaSb =

b

L
a

S # dl

F

S

=

b

L
a

F cos f dl

(work done by a force)

(23.1)

S
d l
where
angle between

S
F

is an inﬁnitesimal displacement along the particle’s path and

f

is the

S

and

Second, if the force

Sd l
at each point along the path.
F
is conservative, as we deﬁned the term in Section 7.3,
can always be expressed in terms of a potential energy U.
Ua
to a point
and the work

the work done by
When the particle moves from a point where the potential energy is
where it is
the change in potential energy is
WaSb

¢U = Ub - Ua

done by the force is

Ub,

S
F

WaSb = Ua - Ub = - 1Ub - Ua2 = - ¢U

(work done by a
conservative force)

(23.2)

Ua

Ub,

WaSb

is positive,

is greater than

When
is negative, and the potential
energy decreases. That’s what happens when a baseball falls from a high point
(a) to a lower point (b) under the inﬂuence of the earth’s gravity; the force of
gravity  does  positive  work,  and  the  gravitational  potential  energy  decreases
(Fig. 23.1). When a tossed ball is moving upward, the gravitational force does
negative work during the ascent, and the potential energy increases.

¢U

Third,  the  work–energy  theorem  says  that  the  change  in  kinetic  energy
¢K = Kb - Ka
during a displacement equals the total work done on the parti-
cle. If only conservative forces do work, then Eq. (23.2) gives the total work, and
Kb - Ka = - 1Ub - Ua2.

We usually write this as

Ka + Ua = Kb + Ub

(23.3)

That is, the total mechanical energy (kinetic plus potential) is conserved under
these circumstances.

Electric Potential Energy in a Uniform Field
Let’s look at an electrical example of these basic concepts. In Fig. 23.2 a pair of
charged  parallel  metal  plates  sets  up  a  uniform,  downward  electric  ﬁeld  with
magnitude E. The field exerts a downward force with magnitude
on a
positive test charge  As the charge moves downward a distance d from point
a to point b, the force on the test charge is constant and independent of its loca-
tion. So the work done by the electric field is the product of the force magni-
tude  and  the  component  of  displacement  in  the  (downward)  direction  of  the
force:

F = q0E

q0.

WaSb = Fd = q0Ed

(23.4)

This  work  is  positive,  since  the  force  is  in  the  same  direction  as  the  net
displacement of the test charge.

Fy = - q0E,

The y-component of the electric force,

is constant, and there is no
x- or z-component. This is exactly analogous to the gravitational force on a mass m
Fy = - mg
near the earth’s surface; for this force, there is a constant y-component
and the x- and z-components are zero. Because of this analogy, we can conclude that
by the uniform electric ﬁeld in Fig. 23.2 is conservative, just
the force exerted on
as is the gravitational force. This means that the work
done by the ﬁeld is
independent of the path the particle takes from a to b. We can represent this work
with a potential-energy function U, just as we did for gravitational potential energy

WaSb

q0

23.1 Electric Potential Energy

755

23.1 The work done on a baseball
moving in a uniform gravitational ﬁeld.

Object moving in a uniform gravitational field

S

w 5 mg

S

The work done by
the gravitational
force is the same for
any path from a to b:
Wa S b

5 2DU 5 mgh

h

a

b

23.2 The work done on a point charge
moving in a uniform electric ﬁeld.
Compare with Fig. 23.1.

Point charge moving in
a uniform electric field

y

+

+

S
E

+

+

a

+

q0

S

S

F 5 q0E

d

y

–

–

b

–

–

 O

–

The work done by the electric force
is the same for any path from a to b:

WaSb

5 2DU 5 q0Ed

756

CHAPTER 23 Electric Potential

23.3 A positive charge moving (a) in the direction of the electric ﬁeld
direction opposite

S
.E

S
E

and (b) in the

S
(a) Positive charge moves in the direction of E:
•  Field does positive work on charge.
• U decreases.

y

S
(b) Positive charge moves opposite E:
•  Field does negative work on charge.
• U increases.

y

+

S
E

–

+

+

+

+

S

S

F 5 q0E

a

b

ya

yb

–

O
–

–

–

+

S
E

–

+

+

+

+

b

a

yb

ya

–

O
–

S

S

F 5 q0E
–

–

was

(23.5)

in  Section  7.1.  The  potential  energy  for  the  gravitational  force
U = mgy;

hence the potential energy for the electric force

Fy = - q0E

Fy = - mg
is

U = q0Ey
ya

When the test charge moves from height
charge by the ﬁeld is given by
WaSb = - ¢U = - 1Ub - Ua2 = - 1q0Eyb - q0Eya2 = q0E1ya - yb2

to height

yb,

the work done on the

(23.6)

yb

ya

q0

S
;
E

(cid:2) q0 E

is greater than

(Fig. 23.3a), the positive test charge  moves down-
the displacement is in the same direction as the
so the ﬁeld does positive work and  decreases. [In particular, if
in agreement with
q0
(Fig. 23.3b), the positive test charge  moves
S
;
E
the displacement is opposite the force, the

When
ward, in the same direction as
S
S
,
F
force
ya - yb = d
yb
Eq. (23.4).] When
upward, in the opposite direction to
ﬁeld does negative work, and U increases.
q0

is negative, the potential energy increases when it moves

U
WaSb = q0Ed,

as in Fig. 23.2, Eq. (23.6) gives

If the test charge

is less than

ya

with the ﬁeld and decreases when it moves against the ﬁeld (Fig. 23.4).

Whether  the  test  charge  is  positive  or  negative,  the  following  general  rules
apply: U increases if the test charge  moves in the direction opposite the electric
(Figs.  23.3b  and  23.4a);  U  decreases if  moves  in  the  same
force

S
F

q0

S

(cid:2) q0E

q0

23.4 A negative charge moving (a) in the direction of the electric ﬁeld
direction opposite

. Compare with Fig. 23.3.

S
E

S
E

and (b) in the

S
(a) Negative charge moves in the direction of E:
•  Field does negative work on charge.
• U increases.

y

S
(b) Negative charge moves opposite E:
•  Field does positive work on charge.
• U decreases.

y

+

S
E

–

+

+

+

+

S

S

F 5 q0 E

a

b

ya

yb

–

O
–

–

–

+

S
E

–

+

+

+

+

b

a

yb

S

S

F 5 q0 E

ya

–

O
–

–

–

S
F

S

(cid:2) q0E

direction as
(Figs. 23.3a and 23.4b). This is the same behavior as for
gravitational potential energy, which increases if a mass m moves upward (oppo-
site the direction of the gravitational force) and decreases if m moves downward
(in the same direction as the gravitational force).

CAUTION Electric  potential  energy The  relationship  between  electric  potential  energy
change and motion in an electric ﬁeld is an important one that we’ll use often, but that
takes some effort to truly understand. Take the time to carefully study the preceding para-
graph as well as Figs. 23.3 and 23.4. Doing so now will help you tremendously later!

Electric Potential Energy of Two Point Charges
The idea of electric potential energy isn’t restricted to the special case of a uni-
form  electric  ﬁeld.  Indeed,  we  can  apply  this  concept  to  a  point  charge  in  any
electric ﬁeld caused by a static charge distribution. Recall from Chapter 21 that
we can represent any charge distribution as a collection of point charges. There-
fore it’s useful to calculate the work done on a test charge  moving in the elec-
tric ﬁeld caused by a single, stationary point charge

q0

q.

We’ll consider ﬁrst a displacement along the radial line in Fig. 23.5. The force
q0

is given by Coulomb’s law, and its radial component is

on

qq0
r 2

(23.7)

Fr =

1
4pP0
1+ or -2

q0

have the same sign

Fr
is posi-
If q and
the force is repulsive and
tive; if the two charges have opposite signs, the force is attractive and
is neg-
Fr
ative.  The  force  is  not constant  during  the  displacement,  and  we  have  to
by this force as  moves from
integrate to calculate the work
a to b:

done on

WaSb

q0

q0

23.1 Electric Potential Energy

757

q0

23.5 Test charge  moves along a
straight line extending radially from
charge  As it moves from
a
to rb.
distance varies from

to

ra

b,

q.

the

S
E

b

Test charge q0 moves
from a to b along
a radial line
from q.

q0

r

S
E

a

ra

rb

WaSb =

rb
Fr dr =

L
ra

rb

L
ra

1
4pP0

qq0
r 2 dr =

qq0
4pP0

a 1
ra

- 1
rb

b

(23.8)

q

The work done by the electric force for this particular path depends only on the
endpoints.

Now let’s consider a more general displacement (Fig. 23.6) in which a and b
during

do not lie on the same radial line. From Eq. (23.1) the work done on
this displacement is given by

q0

WaSb =

rb
F cos f dl =

L
ra

rb

L
ra

1
4pP0

qq0
r 2 cos f dl

dr

S
d l

cos f dl = dr.
depends  only  on  the  change

That  is,  the  work  done  during  a  small
But  Fig.  23.6 shows  that
displacement
in  the  distance  r between  the
charges, which is the radial component of the displacement. Thus Eq. (23.8) is
q0
by the electric
valid even for this more general displacement; the work done on
S
not on the details of the path.
E
ﬁeld
and
Also, if
returns to its starting point a by a different path, the total work done in
back to
the round-trip displacement is zero (the integral in Eq. (23.8) is from
ra2.
These are the needed characteristics for a conservative force, as we deﬁned it
in Section 7.3. Thus the force on

produced by q depends only on
q0

is a conservative force.

rb,

ra

ra

q0

We  see  that  Eqs.  (23.2) and  (23.8) are  consistent  if  we  deﬁne  the  potential
q0
is  a  distance
from  q,  and  to  be
q0
rb
from q. Thus the potential energy U
is a distance
is at any distance r from charge q is

energy  to  be
Ub = qq0>4pP0rb
when the test charge

Ua = qq0>4pP0ra

when

when
q0

ra

U =

1
4pP0

qq0
r

(electric potential energy of
)
two point charges

q and q0

(23.9)

23.6 The work done on charge
q0
the electric ﬁeld of charge  does not
depend on the path taken, but only on the
distances

by

q

ra

and rb.
Test charge q0 moves from a to b
along an arbitrary path.

S
F

S
E

b

S
dr
q0

S
dl

f

dr

rb

r

q

a

ra

758

CHAPTER 23 Electric Potential

23.7 Graphs of the potential energy  of
two point charges  and
separation r.

versus their

q0

U

q

Equation (23.9) is valid no matter what the signs of the charges
potential energy is positive if the charges q and
and negative if they have opposite signs (Fig. 23.7b).

. The
have the same sign (Fig. 23.7a)

and

q0

q0

q

(a) q and q0 have the same sign.

U

q

q0

q

q0

or

r

r

• U . 0
• As r S 0, U S 1`.
• As r S `, U S 0.

O

r

(b) q and q0 have opposite signs.

U

O

r

q

q0

q

q0

or

r

r
• U , 0
• As r S 0, U S 2`.
• As r S `, U S 0.

CAUTION Electric  potential  energy  vs.  electric  force Don’t  confuse  Eq.  (23.9) for  the
potential  energy  of  two  point  charges  with  the  similar  expression  in  Eq.  (23.7) for  the
radial component of the electric force that one charge exerts on the other. Potential energy
U is proportional to

while the force component

is proportional to

1>r 2.

1>r,

❙

Fr

In Eq. (23.9), U is zero when q and

Potential  energy  is  always  deﬁned  relative  to  some  reference  point  where
r = q.
U = 0.
are inﬁnitely far apart and
Therefore U represents the work that would be done on the test charge
by the
q0
have the
q0
ﬁeld of q if  moved from an initial distance r to inﬁnity. If q and
same sign, the interaction is repulsive, this work is positive, and U is positive at
any ﬁnite separation (Fig. 23.7a). If the charges have opposite signs, the interac-
tion is attractive, the work done is negative, and U is negative (Fig. 23.7b).

q0

q0

the change in potential energy is the same whether q is held ﬁxed and

We  emphasize  that  the  potential  energy  U given  by  Eq.  (23.9) is  a  shared
ra
property of the two charges. If the distance between  and
rb,
is
to
moved  or
is  held  ﬁxed  and  q is  moved.  For  this  reason,  we  never  use  the
phrase “the electric potential energy of a point charge.” (Likewise, if a mass m is
at  a  height  h above  the  earth’s  surface,  the  gravitational  potential  energy  is  a
shared property of the mass m and the earth. We emphasized this in Sections 7.1
and 13.3.)

is changed from
q0

q0

q0

q

Equation (23.9) also holds if the charge

is outside a spherically symmetric
q0
charge distribution with total charge q; the distance r is from
to the center of
the distribution. That’s because Gauss’s law tells us that the electric ﬁeld outside
such a distribution is the same as if all of its charge q were concentrated at its
center (see Example 22.9 in Section 22.4).

q0

Example 23.1 Conservation of energy with electric forces

9.11 * 10-31 kg
A positron (the electron’s antiparticle) has mass
q0 = + e = + 1.60 * 10-19 C.
Suppose  a  positron
and  charge
a
moves  in  the  vicinity  of  an
(alpha)  particle,  which  has  charge
q = + 2e = 3.20 * 10-19 C
6.64 * 10-27 kg.
a
and  mass
particle’s mass is more than 7000 times that of the positron, so we
assume  that  the
particle  remains  at  rest.  When  the  positron  is
1.00 * 10-10 m
particle,  it  is  moving  directly  away
a
from the  particle at
(a) What is the positron’s
apart?  (b) What  is
speed  when  the  particles  are
the  positron’s  speed  when  it  is  very  far  from  the
particle?
(c) Suppose the initial conditions are the same but the moving par-
ticle is an electron (with the same mass as the positron but charge
q0 = - e

). Describe the subsequent motion.

a
from  the

2.00 * 10-10 m

3.00 * 106 m>s.

The

a

a

SOLUTION

r

a

IDENTIFY  and SET  UP: The electric force between a positron (or
particle  is  conservative,  so  mechanical
an  electron)  and  an
energy (kinetic plus potential) is conserved. Equation (23.9) gives the
potential energy U at any separation  : The potential-energy function
for parts (a) and (b) looks like that of Fig. 23.7a, and the function for
part (c) looks like that of Fig. 23.7b. We are given the positron speed
va = 3.00 * 106 m>s
when the separation between the particles is
ra = 1.00 * 10-10 m.
In parts (a) and (b) we use Eqs. (23.3) and
r = rb = 2.00 * 10-10 m
r =
(23.9) to  ﬁnd  the  speed  for
rc S q,
respectively. In part (c) we replace the positron with an
electron and reconsider the problem.

and

EXECUTE: (a) Both particles have positive charge, so the positron
speeds up as it moves away from the  particle. From the energy-
conservation equation, Eq. (23.3), the ﬁnal kinetic energy is

a

Kb = 1

2 mv 2

b = Ka + Ua - Ub

In this expression,

19.11 * 10-31 kg213.00 * 106 m>s22

Ka = 1

2

2 mv 2

a = 1
= 4.10 * 10-18 J
qq0
ra

1
4pP0

Ua =

= 19.0 * 109 N # m2>C22

*

13.20 * 10-19 C211.60 * 10-19 C2
1.00 * 10-10 m

= 4.61 * 10-18 J
qq0
rb

1
4pP0

Ub =

= 2.30 * 10-18 J

Hence  the  positron  kinetic  energy  and  speed  at
10-10 m

are
b = 4.10 * 10-18 J + 4.61 * 10-18 J - 2.30 * 10-18 J

Kb = 1

r = rb = 2.00 *

2 mv 2

= 6.41 * 10-18 J

vb =

2Kb
m

A

=

A

216.41 * 10-18 J2
9.11 * 10-31 kg

= 3.8 * 106 m>s

a

the ﬁnal potential energy

(b) When the positron and  particle are very far apart so that
r = rc S q,
approaches zero. Again
from energy conservation, the ﬁnal kinetic energy and speed of the
positron in this case are
Kc = Ka + Ua - Uc = 4.10 * 10-18 J + 4.61 * 10-18 J - 0

Uc

= 8.71 * 10-18 J

vc =

2Kc
m

A

=

A

218.71 * 10-18 J2
9.11 * 10-31 kg

= 4.4 * 106 m>s

a

(c)  The  electron  and

particle  have  opposite  charges,  so  the
force is attractive and the electron slows down as it moves away.
to  means that the
Changing the moving particle’s sign from
initial  potential  energy  is  now
which
makes the total mechanical energy negative:

Ua = - 4.61 * 10-18 J,

+e

-e

Ka + Ua = 14.10 * 10-18 J2 - 14.61 * 10-18 J2

= - 0.51 * 10-18 J

The  total  mechanical  energy  would  have  to  be  positive  for  the
particle.  Like  a
electron  to  move  inﬁnitely  far  away  from  the
rock thrown upward at low speed from the earth’s surface, it will
r = rd
particle  before
reach  a  maximum  separation
reversing direction. At this point its speed and its kinetic energy
Kd
are zero, so at separation  we have

from  the

a

a

rd

23.1 Electric Potential Energy

759

Ud = Ka + Ua - Kd = 1-0.51 * 10-18 J2 - 0

Ud =

= - 0.51 * 10-18 J

1
4pP0

qq0
rd
qq0
4pP0

rd = 1
Ud
19.0 * 109 N # m2>C22
-0.51 * 10-18 J

=

13.20 * 10-19 C21 -1.60 * 10-19C2

= 9.0 * 10-10 m
rb = 2.00 * 10-10 m

For
electron kinetic energy and speed at this point are

we have

Ub = - 2.30 * 10-18 J,

so the

Kb = 1

2 mv 2

b = 4.10 * 10-18 J + 1-4.61 * 10-18 J2
- 1-2.30 * 10-18 J2 = 1.79 * 10-18 J

vb =

2Kb
m

A

=

A

211.79 * 10-18 J2
9.11 * 10-31 kg

= 2.0 * 106 m>s

a

EVALUATE: Both particles behave as expected as they move away
from the  particle: The positron speeds up, and the electron slows
down and eventually turns around. How fast would an electron have
ra = 1.00 * 10-10 m
to be moving at
to travel inﬁnitely far from
the  particle? (Hint: See Example 13.4 in Section 13.3.)

a

S
E

at distances

q0
r1, r2, r3, Á

Electric Potential Energy with Several Point Charges
Suppose the electric ﬁeld
in which charge  moves is caused by several point
q1, q2, q3, Á
q0,
charges
as in Fig. 23.8. For exam-
q0
ple,
could be a positive ion moving in the presence of other ions (Fig. 23.9). The
total electric ﬁeld at each point is the vector sum of the ﬁelds due to the individ-
q0
ual charges, and the total work done on
during any displacement is the sum of
the contributions from the individual charges. From Eq. (23.9) we conclude that
the potential energy associated with the test charge
at point a in Fig. 23.8 is the
algebraic sum (not a vector sum):

from

q0

U =

q0
4pP0

a

q1
r1

+

+

q2
r2

q3
r3

+ Á b =

q0
4pP0

qi
ri

a
i

q0

(point charge
and collection
)qi
of charges

(23.10)

23.8 The potential energy associated
with a charge
other charges
distances

q0
q1, q2,
and

a
and
q3
r3

from point a.

at point  depends on the

and on their

r1, r2,

q1

r1

a

q0

q2

q3

r2

r3

q0

When

is at a different point

the potential energy is given by the same
b.
to point  The work
expression, but
done on charge  when it moves from a to b along any path is equal to the dif-
ference

r1, r2, Á
q0
Ua - Ub
between the potential energies when

b,
are the distances from

is at a and at

q1, q2, Á

q0

b.

We can represent any charge distribution as a collection of point charges, so
Eq.  (23.10) shows  that  we  can  always  ﬁnd  a  potential-energy  function  for  any
static electric ﬁeld. It follows that for every electric ﬁeld due to a static charge
distribution, the force exerted by that ﬁeld is conservative.

are inﬁnite—that is, when the test charge

Equations  (23.9) and  (23.10) deﬁne  U to  be  zero  when  all  the  distances
r1, r2, Á
is very far away from all
the  charges  that  produce  the  ﬁeld.  As  with  any  potential-energy  function,  the
point where
is arbitrary; we can always add a constant to make U equal
zero  at  any  point  we  choose.  In  electrostatics  problems  it’s  usually  simplest  to
choose this point to be at inﬁnity. When we analyze electric circuits in Chapters
25 and 26, other choices will be more convenient.

U = 0

q0

760

CHAPTER 23 Electric Potential

1Xe+2

23.9 This ion engine for spacecraft uses
electric forces to eject a stream of positive
at speeds in excess of
xenon ions
30 km/s. The thrust produced is very low
(about 0.09 newton) but can be maintained
continuously for days, in contrast to chem-
ical rockets, which produce a large thrust
for a short time (see Fig. 8.33). Such ion
engines have been used for maneuvering
interplanetary spacecraft.

q0

S
E

in the  ﬁeld produced by

Equation (23.10) gives the potential energy associated with the presence of the
But there is also poten-
test charge
tial  energy  involved  in  assembling  these  charges.  If  we  start  with  charges
q1, q2, q3, Á
all separated from each other by inﬁnite distances and then bring
qi
them  together  so  that  the  distance  between
the  total potential
energy  U is  the  sum  of  the  potential  energies  of  interaction  for  each  pair  of
charges. We can write this as

q1, q2, q3, . . . .

and

rij,

is

qj

U =

1
4pP0

a
i 6 j

qiqj
rij

(23.11)

(because  that
This  sum  extends  over  all  pairs of  charges;  we  don’t  let
would be an interaction of a charge with itself ), and we include only terms with
i 6 j
to make sure that we count each pair only once. Thus, to account for the
interaction between
but not a
we include a term with
and
term with

q3
and
j = 3.

j = 4

i = 3

i = 4

and

q4,

i = j

Interpreting Electric Potential Energy
As  a  ﬁnal  comment,  here  are  two  viewpoints  on  electric  potential  energy.  We
have deﬁned it in terms of the work done by the electric ﬁeld on a charged parti-
cle moving in the ﬁeld, just as in Chapter 7 we deﬁned potential energy in terms
of the work done by gravity or by a spring. When a particle moves from point a
to point
Thus the
equals the work that is done by the electric
potential-energy difference
force when the particle moves from a to When
the ﬁeld
does positive work on the particle as it “falls” from a point of higher potential
energy

the work done on it by the electric ﬁeld is
Ua - Ub

to a point of lower potential energy

WaSb = Ua - Ub.

is greater than

Ub,

(b).

(a)

Ua

b.

b,

Ua

to  a  point  a where  it  has  a  greater  value

An  alternative  but  equivalent  viewpoint  is  to  consider  how  much  work  we
would have to do to “raise” a particle from a point b where the potential energy is
Ub
(pushing  two  positive  charges
closer together, for example). To move the particle slowly (so as not to give it any
that is equal
kinetic energy), we need to exert an additional external force
and  opposite  to  the  electric-ﬁeld  force  and  does  positive  work.  The  potential-
energy difference
is then deﬁned as the work that must be done by an
external force to move the particle slowly from b to a against the electric force.
is the negative of the electric-ﬁeld force and the displacement is in
Because
is equiv-
the opposite direction, this deﬁnition of the potential difference
alent to that given above. This alternative viewpoint also works if
is less than
Ub,
corresponding to “lowering” the particle; an example is moving two positive
charges away from each other. In this case,
is again equal to the work
done by the external force, but now this work is negative.

Ua - Ub
Ua

Ua - Ub

Ua - Ub

S
F

S
F

ext

ext

We will use both of these viewpoints in the next section to interpret what is

meant by electric potential, or potential energy per unit charge.

Example 23.2 A system of point charges

at

x = a.

Two point charges are located on the  -axis,
q2 = + e
external force to bring a third point charge
to
charges.

and
(a)  Find  the  work  that  must  be  done  by  an
from inﬁnity
(b) Find the total potential energy of the system of three

q3 = + e

x = 2a.

at

x

q1 = - e

x = 0

x = 2a.
inﬁnity  to
We  do  this  by  using  Eq.  (23.10) to  ﬁnd  the
potential energy associated with
In
q3
part (b) we use Eq. (23.11), the expression for the potential energy
of a collection of point charges, to ﬁnd the total potential energy of
the system.

in the presence of

and

q2.

q1

SOLUTION

23.10 Our sketch of the situation after the third charge has been
brought in from inﬁnity.

IDENTIFY  and SET  UP:  Figure 23.10 shows the ﬁnal arrangement
of the three charges. In part (a) we need to ﬁnd the work W that
in from
must be done on

by an external force

to bring

S
F

q3

q3

ext
