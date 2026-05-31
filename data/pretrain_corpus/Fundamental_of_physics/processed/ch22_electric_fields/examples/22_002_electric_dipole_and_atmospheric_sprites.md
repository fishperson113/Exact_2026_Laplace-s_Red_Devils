Sample Problem 22.02
Electric dipole and atmospheric sprites
Sprites (Fig. 22-10a) are huge flashes that occur far above a
large thunderstorm. They were seen for decades by pilots
flying at night, but they were so brief and dim that most pi-
lots figured they were just illusions.Then in the 1990s sprites
were captured on video. They are still  not well understood
but are believed to be produced when especially powerful
lightning occurs between the ground and storm clouds, par-
ticularly when the lightning transfers a huge amount of neg-
ative charge %q from the ground to the base of the clouds
(Fig. 22-10b).
Just after such a transfer, the ground has a complicated
distribution of positive charge. However, we can model the
electric field due to the charges in the clouds and the ground
by assuming a vertical electric dipole that has charge %q at
cloud height h and charge #q at below-ground depth h
(Fig. 22-10c). If q ! 200 C and h ! 6.0 km, what is the magni-
tude of the dipole’s electric field at altitude z1 ! 30 km some-
what above the clouds and altitude z2 ! 60 km somewhat
above the stratosphere?
(a)
Figure 22-10 (a) Photograph of a sprite. (b) Lightning in which a large amount of negative charge is transferred from ground to cloud base.
(c) The cloud-ground system modeled as a vertical electric dipole.
Charge
transfer
Ground
Cloud
- - - - - - 
(b)
(c)
h
h
z
-q
+q
Courtesy NASA

The Electric Field Due to a Line of Charge
So far we have dealt with only charged particles, a single particle or a simple col-
lection of them. We now turn to a much more challenging situation in which a
thin (approximately one-dimensional) object such as a rod or ring is charged with
a huge number of particles, more than we could ever even count. In the next
module, we consider two-dimensional objects, such as a disk with charge spread
over a surface. In the next chapter we tackle three-dimensional objects, such as a
sphere with charge spread through a volume.
Heads Up. Many students consider this module to be the most difficult in
the book for a variety of reasons. There are lots of steps to take, a lot of vector
features to keep track of, and after all that, we set up and then solve an integral.
The worst part, however, is that the procedure can be different for different
arrangements of the charge. Here, as we focus on a particular arrangement (a
charged ring), be aware of the general approach, so that you can tackle other
arrangements in the homework (such as rods and partial circles).
Figure 22-11 shows a thin ring of radius R with a uniform distribution of posi-
tive charge along its circumference. It is made of plastic, which means that the
charge is fixed in place.The ring is surrounded by a pattern of electric field lines,
but here we restrict our interest to an arbitrary point P on the central axis (the
axis through the ring’s center and perpendicular to the plane of the ring), at dis-
tance z from the center point.
The charge of an extended object is often conveyed in terms of a charge
density rather than the total charge. For a line of charge, we use the linear charge
638
CHAPTER 22
ELECTRIC FIELDS
22-4 THE ELECTRIC FIELD DUE TO A LINE OF CHARGE
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
22.18 Explain how symmetry can be used to simplify the
calculation of the electric field at a point near a line of
uniformly distributed charge.
dE
:
●The equation for the electric field set up by a particle does
not apply to an extended object with charge (said to have a
continuous charge distribution).
●To find the electric field of an extended object at a point, we
first consider the electric field set up by a charge element dq in
the object, where the element is small enough for us to apply
the equation for a particle. Then we sum, via integration, com-
ponents of the electric fields 
from all the charge elements.
●Because the individual electric fields 
have different
magnitudes and point in different directions, we first see if
symmetry allows us to cancel out any of the components of
the fields, to simplify the integration.
dE
:
dE
:
Learning Objectives
Key Ideas
an electric field exceeds a certain critical value Ec, the
field can pull electrons out of atoms (ionize the atoms),
and then the freed electrons can run into other atoms,
causing those atoms to emit light. The value of Ec depends
on the density of the air in which the electric field exists.
At altitude z2 ! 60 km the density of the air is so low that
E ! 2.0 $ 102 N/C exceeds Ec, and thus light is emitted by
the atoms in the air. That light forms sprites. Lower down,
just above the clouds at z1 ! 30 km, the density of the air
is much  higher, E ! 1.6 $ 103 N/C does not exceed Ec,
and no light is emitted. Hence, sprites occur only far
above storm clouds.
Additional examples, video, and practice available at WileyPLUS

639
22-4 THE ELECTRIC FIELD DUE TO A LINE OF CHARGE
Figure 22-11 A ring of uniform positive
charge.A differential element of charge 
occupies a length ds (greatly exaggerated for
clarity).This element sets up an electric field
at point P.
dE
:
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
+
+
+
+ + +
+ + + + ++
+
+
+
+
+
+
+
+
z
ds
R
r
θ 
θ 
P
z
dE
density l (the charge per unit length), with the SI unit of coulomb per meter.
Table 22-1 shows the other charge densities that we shall be using for charged
surfaces and volumes.
First Big Problem. So far, we have an equation for the electric field of a par-
ticle. (We can combine the field of several particles as we did for the electric di-
pole to generate a special equation, but we are still basically using Eq. 22-3).
Now take a look at the ring in Fig. 22-11. That clearly is not a particle and so Eq.
22-3 does not apply. So what do we do?
The answer is to mentally divide the ring into differential elements of charge
that are so small that we can treat them as though they are particles.Then we can
apply Eq. 22-3.
Second Big Problem. We now know to apply Eq. 22-3 to each charge ele-
ment dq (the front d emphasizes that the charge is very small) and can write an
expression for its contribution of electric field 
(the front d emphasizes that
the contribution is very small). However, each such contributed field vector at P
is in its own direction. How can we add them to get the net field at P?
The answer is to split the vectors into components and then separately
sum one set of components and then the other set. However, first we check to
see if one set simply all cancels out. (Canceling out components saves lots of
work.)
Third Big Problem. There is a huge number of dq elements in the ring and
thus a huge number of 
components to add up, even if we can cancel out one
set of components. How can we add up more components than we could even
count? The answer is to add them by means of integration.
Do It. Let’s do all this (but again, be aware of the general procedure, not just
the fine details). We arbitrarily pick the charge element shown in Fig. 22-11. Let
ds be the arc length of that (or any other) dq element.Then in terms of the linear
density l (the charge per unit length), we have
dq ! l ds.
(22-10)
An Element’s Field. This charge element sets up the differential electric
field 
at P, at distance r from the element, as shown in Fig. 22-11. (Yes, we are
introducing a new symbol that is not given in the problem statement, but soon we
shall replace it with “legal symbols.”) Next we rewrite the field equation for a
particle (Eq. 22-3) in terms of our new symbols dE and dq, but then we replace dq
using Eq. 22-10.The field magnitude due to the charge element is
(22-11)
Notice that the illegal symbol r is the hypotenuse of the right triangle dis-
played in Fig. 22-11.Thus, we can replace r by rewriting Eq. 22-11 as
(22-12)
Because every charge element has the same charge and the same distance
from point P, Eq. 22-12 gives the field magnitude contributed by each of them.
Figure 22-11 also tells us that each contributed 
leans at angle u to the cen-
tral axis (the z axis) and thus has components perpendicular and parallel to
that axis.
Canceling Components. Now comes the neat part, where we eliminate one
set of those components. In Fig. 22-11, consider the charge element on the oppo-
site side of the ring. It too contributes the field magnitude dE but the field vector
leans at angle u in the opposite direction from the vector from our first charge
dE
:
dE !
1
4p´0
l ds
(z2 # R2) .
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
dE
:
dE
:
dE
:
Table 22-1 Some Measures of Electric
Charge
Name
Symbol
SI Unit
Charge
q
C
Linear charge 
density
l
C/m
Surface charge 
density
s
C/m2
Volume charge 
density
r
C/m3

element, as indicated in the side view of Fig. 22-12. Thus the two perpendicular
components cancel. All around the ring, this cancelation occurs for every charge
element and its symmetric partner on the opposite side of the ring. So we can neg-
lect all the perpendicular components.
Adding Components. We have another big win here. All the remaining
components are in the positive direction of the z axis, so we can just add them
up as scalars. Thus we can already tell the direction of the net electric field at
P: directly away from the ring. From Fig. 22-12, we see that the parallel com-
ponents each have magnitude dE cos u, but u is another illegal symbol.We can
replace cos u with legal symbols by again using the right triangle in Fig. 22-11
to write
(22-13)
Multiplying Eq. 22-12 by Eq. 22-13 gives us the parallel field component from
each charge element:
(22-14)
Integrating. Because we must sum a huge number of these components, each
small, we set up an integral that moves along the ring, from element to element,
from a starting point (call it s ! 0) through the full circumference (s ! 2pR). Only
the quantity s varies as we go through the elements; the other symbols in Eq. 22-14
remain the same,so we move them outside the integral.We find
(22-15)
This is a fine answer,but we can also switch to the total charge by using l ! q/(2pR):
(charged ring).
(22-16)
If the charge on the ring is negative, instead of positive as we have assumed, the
magnitude of the field at P is still given by Eq. 22-16. However, the electric field
vector then points toward the ring instead of away from it.
Let us check Eq. 22-16 for a point on the central axis that is so far away that 
z ) R. For such a point, the expression z2 # R2 in Eq. 22-16 can be approximated
as z2, and Eq. 22-16 becomes
(charged ring at large distance).
(22-17)
This is a reasonable result because from a large distance, the ring “looks like”
a point charge. If we replace z with r in Eq. 22-17, we indeed do have the magni-
tude of the electric field due to a point charge, as given by Eq. 22-3.
Let us next check Eq. 22-16 for a point at the center of the ring-that is, for 
z ! 0. At that point, Eq. 22-16 tells us that E ! 0. This is a reasonable result
because if we were to place a test charge at the center of the ring, there would
be no net electrostatic force acting on it; the force due to any element of the
ring would be canceled by the force due to the element on the opposite side of
the ring. By Eq. 22-1, if the force at the center of the ring were zero, the electric
field there would also have to be zero.
E !
1
4p´0
q
z2
E !
qz
4p´0(z2 # R2)3/2
!
zl(2pR)
4p´0(z2 # R2)3/2  .
E !"dE cos u !
zl
4p´0(z2 # R2)3/2 "
2pR
0
ds
dE cos u !
1
4p+0
zl
(z2 # R2)3/2 ds.
cos u ! z
r !
z
(z2 # R2)1/2  .
640
CHAPTER 22
ELECTRIC FIELDS
z
dE cos u
u
u
dE
dE
Figure 22-12 The electric fields set up at P
by a charge element and its symmetric
partner (on the opposite side of the ring).
The components perpendicular to the z
axis cancel; the parallel components add.

641
22-4 THE ELECTRIC FIELD DUE TO A LINE OF CHARGE
