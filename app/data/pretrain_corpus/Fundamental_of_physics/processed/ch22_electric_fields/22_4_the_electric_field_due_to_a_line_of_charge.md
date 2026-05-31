638

CHAPTE R  22 E LECTR IC  FI E LDS

an  electric  field  exceeds  a  certain  critical  value  Ec, the
field  can  pull  electrons  out  of  atoms  (ionize  the  atoms),
and  then  the  freed  electrons  can  run  into  other  atoms,
causing those atoms to emit light. The value of Ec depends
on the density of the air in which the electric field exists.
At altitude z2 ! 60 km the density of the air is so low that

E ! 2.0 $ 102 N/C exceeds Ec, and thus light is emitted by
the atoms in the air. That light forms sprites. Lower down,
just above the clouds at z1 ! 30 km, the density of the air
is  much    higher, E ! 1.6 $ 103 N/C  does  not  exceed  Ec,
and  no  light  is  emitted. Hence, sprites  occur  only  far
above storm clouds.

Additional examples, video, and practice available at WileyPLUS

22-4 THE ELECTRIC FIELD DUE TO A LINE OF CHARGE

Learning Objectives
After reading this module, you should be able to . . .

22.16 For a uniform distribution of charge, find the linear charge
density l for charge along a line, the surface charge density
s for charge on a surface, and the volume charge density r
for charge in a volume.

22.17 For charge that is distributed uniformly along a line, find

the net electric field at a given point near the line by

splitting the distribution up into charge elements dq and
then summing (by integration) the electric field vectors
set up at the point by each element.

:
dE

22.18 Explain how symmetry can be used to simplify the
calculation of the electric field at a point near a line of
uniformly distributed charge.

Key Ideas
● The equation for the electric field set up by a particle does
not apply to an extended object with charge (said to have a
continuous charge distribution).
● To find the electric field of an extended object at a point, we
first consider the electric field set up by a charge element dq in
the object, where the element is small enough for us to apply

the equation for a particle. Then we sum, via integration, com-
:
dE
from all the charge elements.
ponents of the electric fields

● Because the individual electric fields
magnitudes and point in different directions, we first see if
symmetry allows us to cancel out any of the components of
the fields, to simplify the integration.

have different

:
dE

The Electric Field Due to a Line of Charge
So far we have dealt with only charged particles, a single particle or a simple col-
lection of them. We now turn to a much more challenging situation in which a
thin (approximately one-dimensional) object such as a rod or ring is charged with
a  huge  number  of  particles, more  than  we  could  ever  even  count. In  the  next
module, we consider two-dimensional objects, such as a disk with charge spread
over a surface. In the next chapter we tackle three-dimensional objects, such as a
sphere with charge spread through a volume.

Heads  Up. Many students consider this module to be the most difficult in
the book for a variety of reasons. There are lots of steps to take, a lot of vector
features to keep track of, and after all that, we set up and then solve an integral.
The  worst  part, however, is  that  the  procedure  can  be  different  for  different
arrangements  of  the  charge. Here, as  we  focus  on  a  particular  arrangement  (a
charged  ring), be  aware  of  the  general  approach, so  that  you  can  tackle  other
arrangements in the homework (such as rods and partial circles).

Figure 22-11 shows a thin ring of radius R with a uniform distribution of posi-
tive charge along its circumference. It is made of plastic, which means that the
charge is fixed in place. The ring is surrounded by a pattern of electric field lines,
but here we restrict our interest to an arbitrary point P on the central axis (the
axis through the ring’s center and perpendicular to the plane of the ring), at dis-
tance z from the center point.

The  charge  of  an  extended  object  is  often  conveyed  in  terms  of  a  charge
density rather than the total charge. For a line of charge, we use the linear charge

22-4 TH E  E LECTR IC  FI E LD  DU E  TO  A  LI N E  OF  CHARG E

639

density l (the  charge  per  unit  length), with  the  SI  unit  of  coulomb  per  meter.
Table 22-1 shows the other charge densities that we shall be using for charged
surfaces and volumes.

First Big Problem. So far, we have an equation for the electric field of a par-
ticle. (We can combine the field of several particles as we did for the electric di-
pole  to  generate  a  special  equation, but  we  are  still  basically  using  Eq. 22-3).
Now take a look at the ring in Fig. 22-11. That clearly is not a particle and so Eq.
22-3 does not apply. So what do we do?

The answer is to mentally divide the ring into differential elements of charge
that are so small that we can treat them as though they are particles. Then we can
apply Eq. 22-3.

Second Big Problem. We now know to apply Eq. 22-3 to each charge ele-
ment dq (the front d emphasizes that the charge is very small) and can write an
(the front d emphasizes that
expression for its contribution of electric field
the contribution is very small). However, each such contributed field vector at P
is in its own direction. How can we add them to get the net field at P?

:
dE

The  answer  is  to  split  the  vectors  into  components  and  then  separately
sum one set of components and then the other set. However, first we check to
see if one set simply all cancels out. (Canceling out components saves lots of
work.)

Third Big Problem. There is a huge number of dq elements in the ring and
thus a huge number of
components to add up, even if we can cancel out one
set of components. How can we add up more components than we could even
count? The answer is to add them by means of integration.

:
dE

Do It. Let’s do all this (but again, be aware of the general procedure, not just
the fine details). We arbitrarily pick the charge element shown in Fig. 22-11. Let
ds be the arc length of that (or any other) dq element. Then in terms of the linear
density l (the charge per unit length), we have

dq ! l ds.

(22-10)

An  Element’s  Field. This  charge  element  sets  up  the  differential  electric
:
at P, at distance r from the element, as shown in Fig. 22-11. (Yes, we are
dE
field
introducing a new symbol that is not given in the problem statement, but soon we
shall  replace  it  with “legal  symbols.”)  Next  we  rewrite  the  field  equation  for  a
particle (Eq. 22-3) in terms of our new symbols dE and dq, but then we replace dq
using Eq. 22-10. The field magnitude due to the charge element is

dE !

1
4p´0

dq
r2 !

1
4p´0

l ds
r2

.

(22-11)

Notice  that  the  illegal  symbol  r is  the  hypotenuse  of  the  right  triangle  dis-

played in Fig. 22-11. Thus, we can replace r by rewriting Eq. 22-11 as

dE !

1
4p´0

l ds
(z2 # R2)

.

(22-12)

Because  every  charge  element  has  the  same  charge  and  the  same  distance
from point P, Eq. 22-12 gives the field magnitude contributed by each of them.
leans at angle u to the cen-
Figure 22-11 also tells us that each contributed
tral  axis  (the  z axis)  and  thus  has  components  perpendicular  and  parallel  to
that axis.

:
dE

Canceling Components. Now comes the neat part, where we eliminate one
set of those components. In Fig. 22-11, consider the charge element on the oppo-
site side of the ring. It too contributes the field magnitude dE but the field vector
leans at angle u in the opposite direction from the vector from our first charge

Table 22-1 Some Measures of Electric
Charge

Name

Symbol

SI Unit

Charge
Linear charge
density
Surface charge
density
Volume charge

density

q

l

s

r

C

C/m

C/m2

C/m3

dE

z

θ

P

θ

z

r

++

+

+ +

+

+

+

+

+

+
+
+
+
+

R

+

+ +

+

++

+

+

+

+

+
+
+
+
+

ds

Figure 22-11 A ring of uniform positive
charge. A differential element of charge
occupies a length ds (greatly exaggerated for
clarity).This element sets up an electric field
:
dE

at point P.

640

CHAPTE R  22 E LECTR IC  FI E LDS

z

dE cos u

dE

dE

u

u

Figure 22-12 The electric fields set up at P
by a charge element and its symmetric
partner (on the opposite side of the ring).
The components perpendicular to the z
axis cancel; the parallel components add.

element, as indicated in the side view of Fig. 22-12. Thus the two perpendicular
components cancel. All around the ring, this cancelation occurs for every charge
element and its symmetric partner on the opposite side of the ring. So we can neg-
lect all the perpendicular components.

Adding  Components. We  have  another  big  win  here. All  the  remaining
components are in the positive direction of the z axis, so we can just add them
up as scalars. Thus we can already tell the direction of the net electric field at
P: directly away from the ring. From Fig. 22-12, we see that the parallel com-
ponents each have magnitude dE cos u, but u is another illegal symbol. We can
replace cos u with legal symbols by again using the right triangle in Fig. 22-11
to write

cos u !

z
r

!

z
(z2 # R2)1/2  .

(22-13)

Multiplying  Eq. 22-12  by  Eq. 22-13  gives  us  the  parallel  field  component  from
each charge element:

dE cos u !

1
4p+0

zl
(z2 # R2)3/2 ds.

(22-14)

Integrating. Because we must sum a huge number of these components, each
small, we  set  up  an  integral  that  moves  along  the  ring, from  element  to  element,
from a starting point (call it s ! 0) through the full circumference (s ! 2pR). Only
the quantity s varies as we go through the elements; the other symbols in Eq. 22-14
remain the same, so we move them outside the integral.We find

E ! "dE cos u !

zl

4p´0(z2 # R2)3/2 "2pR

0

!

zl(2pR)
4p´0(z2 # R2)3/2  .

ds

(22-15)

This is a fine answer, but we can also switch to the total charge by using l ! q/(2pR):

E !

qz
4p´0(z2 # R2)3/2

(charged ring).

(22-16)

If the charge on the ring is negative, instead of positive as we have assumed, the
magnitude of the field at P is still given by Eq. 22-16. However, the electric field
vector then points toward the ring instead of away from it.

Let us check Eq. 22-16 for a point on the central axis that is so far away that
z ) R. For such a point, the expression z2 # R2 in Eq. 22-16 can be approximated
as z2, and Eq. 22-16 becomes

E !

1
4p´0

q
z2

(charged ring at large distance).

(22-17)

This  is  a  reasonable  result  because  from  a  large  distance, the  ring “looks  like”
a point charge. If we replace z with r in Eq. 22-17, we indeed do have the magni-
tude of the electric field due to a point charge, as given by Eq. 22-3.

Let us next check Eq. 22-16 for a point at the center of the ring — that is, for
z ! 0. At  that  point, Eq. 22-16  tells  us  that  E ! 0. This  is  a  reasonable  result
because if we were to place a test charge at the center of the ring, there would
be no net electrostatic force acting on it; the force due to any element of the
ring would be canceled by the force due to the element on the opposite side of
the ring. By Eq. 22-1, if the force at the center of the ring were zero, the electric
field there would also have to be zero.

22-4 TH E  E LECTR IC  FI E LD  DU E  TO  A  LI N E  OF  CHARG E

641

Sample Problem 22.03 Electric field of a charged circular rod

Figure  22-13a shows  a  plastic  rod  with  a  uniform  charge
%Q. It is bent in a 120° circular arc of radius  r and symmet-
rically paced across an x axis with the origin at the center of
curvature P of the rod. In terms of Q and r, what is the elec-
tric field  due to the rod at point P?

:
E

KEY IDEA

Because the rod has a continuous charge distribution, we must
find an expression for the electric fields due to differential ele-
ments of the rod and then sum those fields via calculus.

An  element: Consider  a  differential  element  having  arc
length ds and located at an angle u above the x axis (Figs.
22-13b and c). If we let l represent the linear charge density of
the rod, our element ds has a differential charge of magnitude
dq ! l ds.

(22-18)

The  element’s  field: Our  element  produces  a  differential
at  point P, which  is  a  distance  r from  the
electric  field
element. Treating  the  element as  a  point  charge, we  can

:
dE

rewrite Eq. 22-3 to express the magnitude of

:
dE

as

dE !

dq
r2 !

1
4p´0
:
is toward ds because charge dq is negative.
dE

1
4p´0

l ds
r2

(22-19)

.

The direction of

ds,

:
,
dE

Symmetric  partner: Our  element  has  a  symmetrically
located (mirror image) element ds, in the bottom half of the
set  up  at  P by ds, also  has  the
rod. The  electric  field
magnitude given by Eq. 22-19, but the field vector points to-
as shown in Fig. 22-13d. If we resolve the electric
ward
field vectors of ds and
into x and y components as shown
in Figs. 22-13e and f, we see that their y components cancel
(because  they  have  equal  magnitudes  and  are  in  opposite
directions). We also see that their x components have equal
magnitudes and are in the same direction.

ds,

Summing: Thus, to find the electric field set up by the rod,
we need sum (via integration) only the x components of the
differential  electric  fields  set  up  by  all  the  differential  ele-
ments of the rod. From Fig. 22-13f and Eq. 22-19, we can write

This negatively charged rod
is obviously not a particle.

But we can treat this
element as a particle.

Here is the field the
element creates.

y

Plastic rod
of charge –Q

60°

60°

P

r

x

y

P

ds

x

y

dE

θ

P

ds

x

y

dE

θ
θ

dE'

P

A

ds

x

Symmetric
element ds'

(a)

(b)

(c)

(d)

Figure 22-13 Available in
WileyPLUS as an animation
with voiceover. (a) A plastic
rod of charge %Q is a circular
section of radius r and central
angle 120"; point P is the center
of curvature of the rod. (b)–(c)
A differential element in the
top half of the rod, at an angle
u to the x axis and of arc length
ds, sets up a differential
:
dE
electric field
ement ds,, symmetric to ds
about the x axis, sets up a field
:
,
at P with the same magni-
dE
tude. (e)–(f ) The field compo-
nents. (g) Arc length ds makes
an angle du about point P.

at P. (d) An el-

These y components just
cancel, so neglect them.

These x components add.
Our job is to add all such
components.

y

y

ds

ds

dEy

dE

P

θ
θ

dE'

x

dE

θ
θ

dE'

P

dEx

x

Here is the field created by
the symmetric element, same
size and angle.

We use this to
relate the element’s
arc length to the
angle that it subtends.

ds

d

θ

r

y

P

x

Symmetric
element ds'

Symmetric
element ds'

(e)

( f )

(g )

642

CHAPTE R  22 E LECTR IC  FI E LDS

dEx ! dE cos u !

the component dEx set up by ds as
1
4p´0
Equation  22-20  has  two  variables, u and s. Before  we  can
integrate  it, we  must  eliminate  one  variable. We  do  so  by
replacing ds, using the relation

l
r2  cos u ds.

(22-20)

ds ! r du,

in  which  du is  the  angle  at  P that  includes  arc  length  ds
(Fig. 22-13g). With  this  replacement, we  can  integrate
Eq. 22-20 over the angle made by the rod at P, from u ! %60"
to u ! 60"; that will give us the field magnitude at P:

E ! " dEx ! "60"
4p´0r "60"

%60"

!

l

%60"

1
4p´0

l
r2  cos u r du
l

 cos u du !

4p´0r (sin u)

60"

%60"

(If we had reversed the limits on the integration, we would
have gotten the same result but with a minus sign. Since the
integration  gives  only  the  magnitude  of
, we  would  then
have discarded the minus sign.)

:
E

Charge  density: To  evaluate  l, we  note  that  the  full  rod
subtends an angle of 120" and so is one-third of a full circle.
Its  arc  length  is  then  2pr/3, and  its  linear  charge  density
must be

l !

charge
length

!

Q
2pr/3

!

0.477Q
r

.

Substituting this into Eq. 22-21 and simplifying give us

E !

(1.73)(0.477Q)
4p´0r2

!

0.83Q
4p´0r2 .

(Answer)

!

!

l
4p´0r

 [sin 60" % sin(%60")]

1.73l
4p´0r

.

:
E

The direction of
of the charge distribution. We can write
tion as

is toward the rod, along the axis of symmetry
:
in unit-vector nota-
E

(22-21)

:
E

!

0.83Q

4p´0r2  iˆ

.

Problem-Solving Tactics A Field Guide for Lines of Charge

Here is a generic guide for finding the electric field
pro-
duced at a point P by a line of uniform charge, either circu-
lar or straight. The general strategy is to pick out an element
dq of the charge, find
due to that element, and integrate
:
dE

over the entire line of charge.

:
dE

:
E

Step 1.

If the line of charge is circular, let ds be the arc
length of an element of the distribution. If the line is
straight, run an x axis along it and let dx be the length of
an element. Mark the element on a sketch.

Step 2. Relate the charge dq of the element to the length of
the element with either dq ! l ds or dq ! l dx. Consider
dq and l to be positive, even if the charge is actually nega-
tive. (The sign of the charge is used in the next step.)
:
dE

Step 3. Express the field

produced at P by dq with

Eq. 22-3, replacing q in that equation with either l ds or
l dx. If the charge on the line is positive, then at P draw a
that points directly away from dq. If the charge
vector
is negative, draw the vector pointing directly toward dq.

:
dE

Step 4. Always look for any symmetry in the situation. If
P is on an axis of symmetry of the charge distribution,
produced by dq into components
resolve the field
that are perpendicular and parallel to the axis of symme-
try. Then consider a second element dq, that is located
symmetrically to dq about the line of symmetry. At P
draw the vector

that this symmetrical element pro-

:
,
dE

:
dE

duces and resolve it into components. One of the com-
ponents produced by dq is a canceling component; it is
canceled by the corresponding component produced by
dq, and needs no further attention. The other compo-
nent produced by dq is an adding component; it adds to
the corresponding component produced by dq,. Add the
adding components of all the elements via integration.

Step  5. Here  are  four  general  types  of  uniform  charge
distributions, with strategies for the integral of step 4.

Ring, with point P on (central) axis of symmetry, as
in  Fig. 22-11. In  the  expression  for  dE, replace  r 2 with
z2 # R2, as in Eq. 22-12. Express the adding component
in terms of u. That introduces cos u, but u is identi-
of
cal for all elements and thus is not a variable. Replace
cos u as  in  Eq. 22-13. Integrate  over  s, around  the  cir-
cumference of the ring.

:
dE

Circular  arc, with  point  P at  the  center  of  curva-
ture, as in Fig. 22-13. Express the adding component of
:
in terms of u. That introduces either sin u or cos u.
dE
Reduce the resulting two variables s and u to one, u, by
replacing ds with r du. Integrate over u from one end
of the arc to the other end.

Straight  line, with  point  P on  an  extension  of  the
line, as in Fig. 22-14a. In the expression for dE, replace
r with x. Integrate over x, from end to end of the line of
charge.
