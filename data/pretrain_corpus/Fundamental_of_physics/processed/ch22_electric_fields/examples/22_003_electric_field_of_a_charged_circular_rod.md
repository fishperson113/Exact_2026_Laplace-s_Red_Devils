Sample Problem 22.03
Electric field of a charged circular rod
60°
60°
P
y
x
r
Plastic rod
of charge -Q
(a)
This negatively charged rod
is obviously not a particle.
P
y
x
(g)
θ
ds
r
d
We use this to 
relate the element’s 
arc length to the 
angle that it subtends.
x
P
y
(e)
θ
θ
ds
dEy
Symmetric
element ds'
dE
dE'
These y components just
cancel, so neglect them.
P
y
x
(b)
ds
But we can treat this
element as a particle.
Here is the field created by 
the symmetric element, same 
size and angle.
P
y
x
(d)
θ
θ
ds
Symmetric
element ds'
dE
dE'
P
y
x
(c)
θ
ds
dE
Here is the field the
element creates.
x
P
y
(f )
θ
θ
ds
dEx
Symmetric
element ds'
dE
dE'
These x components add.
Our job is to add all such
components.
Figure 22-13 Available in
WileyPLUS as an animation
with voiceover.(a) A plastic
rod of charge %Q is a circular
section of radius r and central
angle 120";point P is the center
of curvature of the rod.(b)-(c)
A differential element in the
top half of the rod,at an angle
u to the x axis and of arc length
ds, sets up a differential
electric field 
at P.(d) An el-
ement ds,,symmetric to ds
about the x axis,sets up a field
at P with the same magni-
tude.(e)-(f ) The field compo-
nents.(g) Arc length ds makes
an angle du about point P.
dE
:,
dE
:
A
Figure 22-13a shows a plastic rod with a uniform charge
%Q. It is bent in a 120° circular arc of radius  r and symmet-
rically paced across an x axis with the origin at the center of
curvature P of the rod. In terms of Q and r, what is the elec-
tric field 
due to the rod at point P?
KEY IDEA
Because the rod has a continuous charge distribution,we must
find an expression for the electric fields due to differential ele-
ments of the rod and then sum those fields via calculus.
An element: Consider a differential element having arc
length ds and located at an angle u above the x axis (Figs.
22-13b and c). If we let l represent the linear charge density of
the rod,our element ds has a differential charge of magnitude
dq ! l ds.
(22-18)
The element’s field: Our element produces a differential
electric field 
at point P, which is a distance r from the 
element. Treating the element as a point charge, we can
dE
:
E
:
rewrite Eq. 22-3 to express the magnitude of 
as
(22-19)
The direction of 
is toward ds because charge dq is negative.
Symmetric partner: Our element has a symmetrically 
located (mirror image) element ds, in the bottom half of the
rod. The electric field 
set up at P by ds, also has the
magnitude given by Eq. 22-19, but the field vector points to-
ward 
as shown in Fig. 22-13d. If we resolve the electric
field vectors of ds and 
into x and y components as shown
in Figs. 22-13e and f, we see that their y components cancel
(because they have equal magnitudes and are in opposite
directions). We also see that their x components have equal
magnitudes and are in the same direction.
Summing: Thus, to find the electric field set up by the rod,
we need sum (via integration) only the x components of the
differential electric fields set up by all the differential ele-
ments of the rod. From Fig. 22-13f and Eq. 22-19, we can write
ds,
ds,
dE
:,
dE
:
dE !
1
4p´0
dq
r2 !
1
4p´0
l ds
r2 .
dE
:

642
CHAPTER 22
ELECTRIC FIELDS
duces and resolve it into components. One of the com-
ponents produced by dq is a canceling component; it is
canceled by the corresponding component produced by
dq, and needs no further attention.The other compo-
nent produced by dq is an adding component; it adds to
the corresponding component produced by dq,.Add the
adding components of all the elements via integration.
Step 5.
Here are four general types of uniform charge
distributions, with strategies for the integral of step 4.
Ring, with point P on (central) axis of symmetry, as
in Fig. 22-11. In the expression for dE, replace r 2 with
z2 # R2, as in Eq. 22-12. Express the adding component
of 
in terms of u.That introduces cos u, but u is identi-
cal for all elements and thus is not a variable. Replace
cos u as in Eq. 22-13. Integrate over s, around the cir-
cumference of the ring.
Circular arc, with point P at the center of curva-
ture, as in Fig. 22-13. Express the adding component of
in terms of u. That introduces either sin u or cos u.
Reduce the resulting two variables s and u to one, u, by
replacing ds with r du. Integrate over u from one end
of the arc to the other end.
Straight line, with point P on an extension of the
line, as in Fig. 22-14a. In the expression for dE, replace
r with x. Integrate over x, from end to end of the line of
charge.
dE
:
dE
:
Problem-Solving Tactics
A Field Guide for Lines of Charge
Here is a generic guide for finding the electric field 
pro-
duced at a point P by a line of uniform charge, either circu-
lar or straight.The general strategy is to pick out an element
dq of the charge, find 
due to that element, and integrate
over the entire line of charge.
Step 1.
If the line of charge is circular, let ds be the arc
length of an element of the distribution. If the line is
straight, run an x axis along it and let dx be the length of
an element. Mark the element on a sketch.
Step 2.
Relate the charge dq of the element to the length of
the element with either dq ! l ds or dq ! l dx.Consider
dq and l to be positive,even if the charge is actually nega-
tive.(The sign of the charge is used in the next step.)
Step 3.
Express the field 
produced at P by dq with
Eq.22-3,replacing q in that equation with either l ds or
l dx.If the charge on the line is positive,then at P draw a
vector 
that points directly away from dq.If the charge
is negative,draw the vector pointing directly toward dq.
Step 4.
Always look for any symmetry in the situation. If
P is on an axis of symmetry of the charge distribution,
resolve the field 
produced by dq into components
that are perpendicular and parallel to the axis of symme-
try.Then consider a second element dq, that is located
symmetrically to dq about the line of symmetry.At P
draw the vector 
that this symmetrical element pro-
dE
:,
dE
:
dE
:
dE
:
dE
:
dE
:
E
:
the component dEx set up by ds as
(22-20)
Equation 22-20 has two variables, u and s. Before we can
integrate it, we must eliminate one variable. We do so by
replacing ds, using the relation
ds ! r du,
in which du is the angle at P that includes arc length ds
(Fig. 22-13g). With this replacement, we can integrate
Eq. 22-20 over the angle made by the rod at P,from u ! %60"
to u ! 60"; that will give us the field magnitude at P:
(22-21)
! 1.73l
4p´0r .
!
l
4p´0r  [sin 60" % sin(%60")]
!
l
4p´0r "
60"
%60"
 cos u du !
l
4p´0r (sin u)
60"
%60"
E !" dEx !"
60"
%60"
1
4p´0
l
r2  cos u r du
dEx ! dE cos u !
1
4p´0
l
r2  cos u ds.
(If we had reversed the limits on the integration, we would
have gotten the same result but with a minus sign. Since the
integration gives only the magnitude of 
, we would then
have discarded the minus sign.)
Charge density: To evaluate l, we note that the full rod
subtends an angle of 120" and so is one-third of a full circle.
Its arc length is then 2pr/3, and its linear charge density
must be
Substituting this into Eq. 22-21 and simplifying give us
(Answer)
The direction of 
is toward the rod,along the axis of symmetry
of the charge distribution. We can write 
in unit-vector nota-
tion as
.
E
: ! 0.83Q
4p´0r2  iˆ
E
:
E
:
! 0.83Q
4p´0r2 .
E ! (1.73)(0.477Q)
4p´0r2
l ! charge
length !
Q
2pr/3 ! 0.477Q
r
.
E
:

643
22-5 THE ELECTRIC FIELD DUE TO A CHARGED DISK
Additional examples, video, and practice available at WileyPLUS
x
P
(a)
x
(b)
P
y
x
(c)
P
y
+ + + + + + + + +
+ + + + + + + + + 
+ + + + + + + + + 
Figure 22-14 (a) Point P is on an extension of the line of charge.
(b) P is on a line of symmetry of the line of charge, at perpendicu-
lar distance y from that line. (c) Same as (b) except that P is not on
a line of symmetry.
Checkpoint 2
The figure here shows three nonconducting rods,one circular and
two straight.Each has a uniform charge of magnitude Q along its top
half and another along its bottom half.For each rod,what is the
direction of the net electric field at point P?
x 
x 
x 
y
y
y
-Q
+Q
P
P
+Q
+Q
+Q
-Q
P
(a)
(b)
(c)
Straight line, with point P at perpendicular dis-
tance y from the line of charge, as in Fig. 22-14b. In the
expression for dE, replace r with an expression involving x
and y. If P is on the perpendicular bisector of the line of
charge,find an expression for the adding component of 
That will introduce either sin u or cos u.Reduce the result-
ing two variables x and u to one, x, by replacing the
trigonometric function with an expression (its definition)
involving x and y. Integrate over x from end to end of the
line of charge. If P is not on a line of symmetry, as in
Fig. 22-14c, set up an integral to sum the components dEx,
and integrate over x to find Ex. Also set up an integral
to sum the components dEy, and integrate over x again to
find Ey.Use the components Ex and Ey in the usual way to
find the magnitude E and the orientation of .
Step 6.
One arrangement of the integration limits gives a
positive result.The reverse gives the same result with a mi-
E
:
dE
:.
nus sign; discard the minus sign. If the result is to be stated
in terms of the total charge Q of the distribution,replace l
with Q/L,in which L is the length of the distribution.
22-5 THE ELECTRIC FIELD DUE TO A CHARGED DISK
After reading this module, you should be able to . . .
22.19 Sketch a disk with uniform charge and indicate the di-
rection of the electric field at a point on the central axis if
the charge is positive and if it is negative.
22.20 Explain how the equation for the electric field on the
central axis of a uniformly charged ring can be used to find
the equation for the electric field on the central axis of a
uniformly charged disk.
22.21 For a point on the central axis of a uniformly charged
disk, apply the relationship between the surface charge den-
sity s, the disk radius R, and the distance z to that point.
●On the central axis through a uniformly charged disk,
E !
s
2´0 #1 %
z
2z2 # R2$
gives the electric field magnitude. Here z is the distance
along the axis from the center of the disk, R is the radius of
the disk, and s is the surface charge density.
Learning Objectives
Key Idea
The Electric Field Due to a Charged Disk
Now we switch from a line of charge to a surface of charge by examining the elec-
tric field of a circular plastic disk, with a radius R and a uniform surface charge
density s (charge per unit area, Table 22-1) on its top surface. The disk sets up a

644
CHAPTER 22
ELECTRIC FIELDS
pattern of electric field lines around it, but here we restrict our attention to the
electric field at an arbitrary point P on the central axis, at distance z from the cen-
ter of the disk, as indicated in Fig. 22-15.
We could proceed as in the preceding module but set up a two-dimensional in-
tegral to include all of the field contributions from the two-dimensional distribu-
tion of charge on the top surface. However, we can save a lot of work with a neat
shortcut using our earlier work with the field on the central axis of a thin ring.
We superimpose a ring on the disk as shown in Fig. 22-15, at an arbitrary ra-
dius 
The ring is so thin that we can treat the charge on it as a charge ele-
ment dq. To find its small contribution dE to the electric field at point P, we
rewrite Eq. 22-16 in terms of the ring’s charge dq and radius r:
(22-22)
The ring’s field points in the positive direction of the z axis.
To find the total field at P, we are going to integrate Eq. 22-22 from the cen-
ter of the disk at r ! 0 out to the rim at r ! R so that we sum all the dE contribu-
tions (by sweeping our arbitrary ring over the entire disk surface). However, that
means we want to integrate with respect to a variable radius r of the ring.
We get dr into the expression by substituting for dq in Eq.22-22.Because the ring
is so thin, call its thickness dr.Then its surface area dA is the product of its circumfer-
ence 2pr and thickness dr.So,in terms of the surface charge density s,we have
dq ! s dA ! s (2pr dr).
(22-23)
After substituting this into Eq. 22-22 and simplifying slightly, we can sum all the
dE contributions with
(22-24)
where we have pulled the constants (including z) out of the integral. To solve
this integral, we cast it in the form 
by setting X ! (z2 # r 2),
,
m ! %3
2
" Xm dX
E !" dE ! sz
4´0 "
R
0
(z2 # r2)%3/2(2r) dr,
dE !
dq z
4p´0(z2 # r2)3/2 .
r ' R.
Figure 22-15 A disk of radius R and uniform
positive charge.The ring shown has radius r
and radial width dr. It sets up a differential
electric field 
at point P on its central
axis.
dE
:
R
P
dE
dr
r
z
and dX ! (2r) dr. For the recast integral we have
and so Eq. 22-24 becomes
(22-25)
Taking the limits in Eq. 22-25 and rearranging, we find
(charged disk)
(22-26)
as the magnitude of the electric field produced by a flat, circular, charged disk at
points on its central axis. (In carrying out the integration, we assumed that z - 0.)
If we let R : ` while keeping z finite, the second term in the parentheses in
Eq. 22-26 approaches zero, and this equation reduces to
(infinite sheet).
(22-27)
This is the electric field produced by an infinite sheet of uniform charge located
on one side of a nonconductor such as plastic. The electric field lines for such
a situation are shown in Fig. 22-4.
We also get Eq. 22-27 if we let z : 0 in Eq. 22-26 while keeping R finite.This
shows that at points very close to the disk, the electric field set up by the disk is
the same as if the disk were infinite in extent.
E !
s
2´0
E !
s
2´0 #1 %
z
2z2 # R2$
E ! sz
4´0 (
(z2 # r2)%1/2
%1
2
)
R
0
.
" Xm dX ! Xm#1
m # 1 ,

645
22-6 A POINT CHARGE IN AN ELECTRIC FIELD
22-6 A POINT CHARGE IN AN ELECTRIC FIELD
After reading this module, you should be able to . . .
22.22 For a charged particle placed in an external electric
field (a field due to other charged objects), apply the rela-
tionship between the electric field 
at that point, the parti-
cle’s charge q, and the electrostatic force 
that acts on
the particle, and identify the relative directions of the force
F
:
E
:
and the field when the particle is positively charged and
negatively charged.
22.23 Explain Millikan’s procedure of measuring the elemen-
tary charge.
22.24 Explain the general mechanism of ink-jet printing.
●If a particle with charge q is placed in an external electric
field
, an electrostatic force 
acts on the particle:
.
F
:! qE
:
F
:
E
:
●If charge q is positive, the force vector is in the same direc-
tion as the field vector. If charge q is negative, the force vec-
tor is in the opposite direction (the minus sign in the equation
reverses the force vector from the field vector).
Learning Objectives
Key Ideas
A Point Charge in an Electric Field
In the preceding four modules we worked at the first of our two tasks: given a
charge distribution, to find the electric field it produces in the surrounding space.
Here we begin the second task: to determine what happens to a charged particle
when it is in an electric field set up by other stationary or slowly moving charges.
What happens is that an electrostatic force acts on the particle, as given by
(22-28)
in which q is the charge of the particle (including its sign) and 
is the electric
field that other charges have produced at the location of the particle. (The field is
not the field set up by the particle itself; to distinguish the two fields, the field
acting on the particle in Eq. 22-28 is often called the external field. A charged
particle or object is not affected by its own electric field.) Equation 22-28 tells us
E
:
F
: ! qE
:,
The electrostatic force 
acting on a charged particle located in an external electric
field 
has the direction of 
if the charge q of the particle is positive and has the
opposite direction if q is negative.
E
:
E
:
F
:
Figure 22-16 The Millikan oil-drop apparatus
for measuring the elementary charge e.
When a charged oil drop drifted into cham-
ber C through the hole in plate P1, its mo-
tion could be controlled by closing and
opening switch S and thereby setting up or
eliminating an electric field in chamber C.
The microscope was used to view the drop,
to permit timing of its motion.
Insulating
chamber
wall
+
-
B
S
P2
C
Oil
drop
P1
A
Microscope
Oil
spray
Measuring the Elementary Charge
Equation 22-28 played a role in the measurement of the elementary charge e by
American physicist Robert A. Millikan in 1910-1913. Figure 22-16 is a represen-
tation of his apparatus.When tiny oil drops are sprayed into chamber A, some of
them become charged, either positively or negatively, in the process. Consider a
drop that drifts downward through the small hole in plate P1 and into chamber C.
Let us assume that this drop has a negative charge q.
If switch S in Fig. 22-16 is open as shown, battery B has no electrical effect on
chamber C. If the switch is closed (the connection between chamber C and the
positive terminal of the battery is then complete), the battery causes an excess
positive charge on conducting plate P1 and an excess negative charge on conduct-
ing plate P2. The charged plates set up a downward-directed electric field 
in
chamber C. According to Eq. 22-28, this field exerts an electrostatic force on any
charged drop that happens to be in the chamber and affects its motion. In partic-
ular, our negatively charged drop will tend to drift upward.
By timing the motion of oil drops with the switch opened and with it closed
and thus determining the effect of the charge q, Millikan discovered that the
E
:

646
CHAPTER 22
ELECTRIC FIELDS
Figure 22-18 The metal wires are so charged
that the electric fields they produce in the
surrounding space cause the air there to un-
dergo electrical breakdown.
Adam Hart-Davis/Photo Researchers, Inc.
values of q were always given by
q ! ne,
for n ! 0, .1, .2, .3, . . . ,
(22-29)
in which e turned out to be the fundamental constant we call the elementary
charge, 1.60 $ 10%19 C. Millikan’s experiment is convincing proof that charge is
quantized, and he earned the 1923 Nobel Prize in physics in part for this work.
Modern measurements of the elementary charge rely on a variety of interlocking
experiments, all more precise than the pioneering experiment of Millikan.
Ink-Jet Printing
The need for high-quality, high-speed printing has caused a search for an
alternative to impact printing, such as occurs in a standard typewriter. Building
up letters by squirting tiny drops of ink at the paper is one such alternative.
Figure 22-17 shows a negatively charged drop moving between two conduct-
ing deflecting plates,between which a uniform,downward-directed electric field 
has been set up. The drop is deflected upward according to Eq. 22-28 and then
strikes the paper at a position that is determined by the magnitudes of 
and the
charge q of the drop.
In practice, E is held constant and the position of the drop is determined by
the charge q delivered to the drop in the charging unit, through which the drop
must pass before entering the deflecting system. The charging unit, in turn, is
activated by electronic signals that encode the material to be printed.
Electrical Breakdown and Sparking
If the magnitude of an electric field in air exceeds a certain critical value Ec, the
air undergoes electrical breakdown, a process whereby the field removes elec-
trons from the atoms in the air. The air then begins to conduct electric current
because the freed electrons are propelled into motion by the field. As they
move, they collide with any atoms in their path, causing those atoms to emit
light. We can see the paths, commonly called sparks, taken by the freed elec-
trons because of that emitted light. Figure 22-18 shows sparks above charged
metal wires where the electric fields due to the wires cause electrical break-
down of the air.
E
:
E
:
Checkpoint 3
(a) In the figure, what is the direction of the electro-
static force on the electron due to the external
electric field shown? (b) In which direction will the
electron accelerate if it is moving parallel to the y axis
before it encounters the external field? (c) If, instead,
the electron is initially moving rightward, will its
speed increase, decrease, or remain constant?
x
e
y
E
Input
signals
Deflecting plate 
G 
C 
Deflecting
plate
E
Figure 22-17 Ink-jet printer. Drops shot from generator G receive a charge in charging unit
C.An input signal from a computer controls the charge and thus the effect of field 
on
where the drop lands on the paper.
E
:

647
22-7 A DIPOLE IN AN ELECTRIC FIELD
magnitude QE acts upward on the charged drop. Thus, as the
drop travels parallel to the x axis at constant speed vx, it
accelerates upward with some constant acceleration ay.
Calculations: Applying Newton’s second law (F ! ma) for
components along the y axis, we find that
