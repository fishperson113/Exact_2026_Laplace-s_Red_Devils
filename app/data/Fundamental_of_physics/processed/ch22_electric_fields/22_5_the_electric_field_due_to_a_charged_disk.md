22-5 TH E  E LECTR IC  FI E LD  DU E  TO  A  CHARG E D  DISK

643

Straight  line, with  point  P at  perpendicular  dis-
tance y from  the  line  of  charge, as  in  Fig. 22-14b. In  the
expression for dE, replace r with an expression involving x
and y. If P is on the perpendicular bisector of the line of
:
dE
charge, find an expression for the adding component of
.
That will introduce either sin u or cos u. Reduce the result-
ing  two  variables  x and u to  one, x, by  replacing  the
trigonometric function with an expression (its definition)
involving x and y. Integrate over x from end to end of the
line of charge. If P is not on a line of symmetry, as in
Fig. 22-14c, set up an integral to sum the components dEx,
and integrate  over  x to  find  Ex. Also  set  up  an  integral
to sum the components dEy, and integrate over x again to
find Ey. Use the components Ex and Ey in the usual way to
find the magnitude E and the orientation of

:
E
.

Step  6. One  arrangement  of  the  integration  limits  gives  a
positive result.The reverse gives the same result with a mi-

nus sign; discard the minus sign. If the result is to be stated
in terms of the total charge Q of the distribution, replace l
with Q/L, in which L is the length of the distribution.

P

P

y

+  +  +  +  +  +  +  +  +

x

(a)

P

y

+  +  +  +  +  +  +  +  +

x

+  +  +  +  +  +  +  +  +

x

(b)

(c)

Figure 22-14 (a) Point P is on an extension of the line of charge.
(b) P is on a line of symmetry of the line of charge, at perpendicu-
lar distance y from that line. (c) Same as (b) except that P is not on
a line of symmetry.

Additional examples, video, and practice available at WileyPLUS

Checkpoint 2

The figure here shows three nonconducting rods, one circular and
two straight. Each has a uniform charge of magnitude Q along its top
half and another along its bottom half. For each rod, what is the
direction of the net electric field at point P?

–Q

+Q

(a)

y

+Q

y

P

x

+Q

(b)

y

+Q

P

x

P

x

–Q

(c)

22-5 THE ELECTRIC FIELD DUE TO A CHARGED DISK

Learning Objectives
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

Key Idea
● On the central axis through a uniformly charged disk,

E !

s

2´0 #1 %

z

z2 # R2 $

2

gives the electric field magnitude. Here z is the distance
along the axis from the center of the disk, R is the radius of
the disk, and s is the surface charge density.

The Electric Field Due to a Charged Disk
Now we switch from a line of charge to a surface of charge by examining the elec-
tric field of a circular plastic disk, with a radius R and a uniform surface charge
density s (charge per unit area, Table 22-1) on its top surface. The disk sets up a

644

CHAPTE R  22 E LECTR IC  FI E LDS

dE

P

z

dr

r

R

Figure 22-15 A disk of radius R and uniform
positive charge. The ring shown has radius r
and radial width dr. It sets up a differential
electric field
axis.

at point P on its central

:
dE

pattern of electric field lines around it, but here we restrict our attention to the
electric field at an arbitrary point P on the central axis, at distance z from the cen-
ter of the disk, as indicated in Fig. 22-15.

We could proceed as in the preceding module but set up a two-dimensional in-
tegral to include all of the field contributions from the two-dimensional distribu-
tion of charge on the top surface. However, we can save a lot of work with a neat
shortcut using our earlier work with the field on the central axis of a thin ring.

We superimpose a ring on the disk as shown in Fig. 22-15, at an arbitrary ra-
r ’ R.
dius
The ring is so thin that we can treat the charge on it as a charge ele-
ment dq. To  find  its  small  contribution  dE to  the  electric  field  at  point  P, we
rewrite Eq. 22-16 in terms of the ring’s charge dq and radius r:

dE !

dq z
4p´0(z2 # r2)3/2 .

(22-22)

The ring’s field points in the positive direction of the z axis.

To find the total field at P, we are going to integrate Eq. 22-22 from the cen-
ter of the disk at r ! 0 out to the rim at r ! R so that we sum all the dE contribu-
tions (by sweeping our arbitrary ring over the entire disk surface). However, that
means we want to integrate with respect to a variable radius r of the ring.

We get dr into the expression by substituting for dq in Eq. 22-22. Because the ring
is so thin, call its thickness dr. Then its surface area dA is the product of its circumfer-
ence 2pr and thickness dr. So, in terms of the surface charge density s, we have

dq ! s dA ! s (2pr dr).

(22-23)

After substituting this into Eq. 22-22 and simplifying slightly, we can sum all the
dE contributions with

E ! " dE !

sz

4´0 "R

0

(z2 # r2)%3/2(2r) dr,

(22-24)

where we have pulled the constants (including  z) out of the integral. To solve
m ! %3
" Xm dX
this  integral, we  cast  it  in  the  form
,
2
and dX ! (2r) dr. For the recast integral we have

by  setting  X ! (z2 # r 2),

and so Eq. 22-24 becomes

" Xm dX !

Xm#1
m # 1

,

E !

sz

4´0 ( (z2 # r2)%1/2

%1
2

R

)

0

.

(22-25)

Taking the limits in Eq. 22-25 and rearranging, we find

E !

s

2´0 #1 %

z

z2 # R2 $

(charged disk)

(22-26)

as the magnitude of the electric field produced by a flat, circular, charged disk at
points on its central axis. (In carrying out the integration, we assumed that z - 0.)
If we let R : ` while keeping z finite, the second term in the parentheses in

2

Eq. 22-26 approaches zero, and this equation reduces to

E !

s
2´0

(infinite sheet).

(22-27)

This is the electric field produced by an infinite sheet of uniform charge located
on  one  side  of  a  nonconductor  such  as  plastic. The  electric  field  lines  for  such
a situation are shown in Fig. 22-4.

We also get Eq. 22-27 if we let z : 0 in Eq. 22-26 while keeping R finite. This
shows that at points very close to the disk, the electric field set up by the disk is
the same as if the disk were infinite in extent.
