Example 27.8
Magnetic force on a curved conductor
In Fig. 27.30 the magnetic field 
is uniform and perpendicular to
the plane of the figure, pointing out of the page. The conductor,
carrying current I to the left, has three segments: (1) a straight seg-
ment with length L perpendicular to the plane of the figure, (2) a
semicircle with radius , and (3) another straight segment with
length 
parallel to the 
Find the total magnetic force on this
conductor.
SOLUTION
IDENTIFY and SET UP: The magnetic field 
is uniform, so
we find the forces 
and 
on the straight segments (1) and (3)
using Eq. (27.19). We divide the curved segment (2) into infinites-
imal straight segments and find the corresponding force 
on
each straight segment using Eq. (27.20). We then integrate to find
The total magnetic force on the conductor is then 
F
S
1  F
S
2  F
S
3.
F
S 
F
S
2.
dF
S
2
F
S
3
F
S
1
B
S  BkN
x-axis.
L
R
B
S
EXECUTE: For segment (1), 
. Hence from Eq. (27.19),
For segment (3), 
so 
For the curved segment (2), Fig. 27.20 shows a segment 
with length 
at angle 
The right-hand rule shows that
the direction of 
is radially outward from the center; make
sure you can verify this. Because 
and 
are perpendicular, the
magnitude 
of the force on the segment 
is just 
. The components of the force on this segment
are
To find the components of the total force, we integrate these
expressions with respect to θ from 
to 
to take in the
whole semicircle. The results are
Hence 
. Finally, adding the forces on all three seg-
ments, we find that the total force is in the positive y-direction:
EVALUATE: We could have predicted from symmetry that the 
x-component of 
would be zero: On the right half of the semicircle
the x-component of the force is positive (to the right) and on the
left half it is negative (to the left); the positive and negative contri-
butions to the integral cancel. The result is that 
is the force that
would be exerted if we replaced the semicircle with a straight seg-
ment of length 2R along the x-axis. Do you see why?
F
S
2
F
S
2
F
S  F
S
1  F
S
2  F
S
3  0  2IRB≥n  ILB≥n  IB12R + L2≥n
F
S
2  2IRB≥n
F2y = IRB
L
p
0
sinudu = 2IRB
F2x = IRB
L
p
0
cosudu = 0
u = p
u = 0
dF2x = IRduBcosu  dF2y = IRduBsinu
I dl B = I1R du2B
dF2 =
dl
S
dF2
B
S
dl
S
dl
S : B
S
u.
dl = R du,
dl
S
B
S  I1-Lın2 : 1BkN2  ILB≥n.
F
S
3  IL
S :
L
S  -Lın,
F
S
1  IL
S : B
S  0.
L
S  -LkN
I
L
O
I (in)
R
I
I
dFx
y
x
du
dl
dFy
B (out)
S
F
S
L
S
dl
S
dF
S
u
u
27.30 What is the total magnetic force on the conductor?
Test Your Understanding of Section 27.6
The figure at right shows a top
view of two conducting rails on which a conducting bar can slide. A uniform magnetic
field is directed perpendicular to the plane of the figure as shown. A battery is to be con-
nected to the two rails so that when the switch is closed, current will flow through the bar
and cause a magnetic force to push the bar to the right. In which orientation, A or B,
should the battery be placed in the circuit?
❙
Conducting
bar
Conducting
rails
Which
orientation?
Switch
A
B
F
S
B
S
ActivPhysics 13.6: Magnetic Torque on a
Loop

that the total force on the loop is zero but that there can be a net torque acting on
the loop, with some interesting properties.
Figure 27.31a shows a rectangular loop of wire with side lengths 
and 
A
line perpendicular to the plane of the loop (i.e., a normal to the plane) makes an
angle 
with the direction of the magnetic field 
and the loop carries a current
The wires leading the current into and out of the loop and the source of emf are
omitted to keep the diagram simple.
The force 
on the right side of the loop (length 
is to the right, in the
as shown. On this side, 
is perpendicular to the current direction,
and the force on this side has magnitude
(27.21)
A force 
with the same magnitude but opposite direction acts on the opposite
side of the loop, as shown in the figure.
The sides with length make an angle 
with the direction of 
The
forces on these sides are the vectors 
and 
their magnitude 
is given by
The lines of action of both forces lie along the 
The total force on the loop is zero because the forces on opposite sides cancel
out in pairs.
The net force on a current loop in a uniform magnetic field is zero. However, the
net torque is not in general equal to zero.
(You may find it helpful at this point to review the discussion of torque in Section
10.1.) The two forces 
and 
in Fig. 27.31a lie along the same line and so
give rise to zero net torque with respect to any point. The two forces 
and 
lie along different lines, and each gives rise to a torque about the y-axis. Accord-
ing to the right-hand rule for determining the direction of torques, the vector
torques due to 
and 
are both in the 
hence the net vector
torque 
is in the 
as well. The moment arm for each of these forces
+y-direction
T
S
+y-direction;
F
S
F
S
F
S
F
S
F
S¿
F
S¿
y-axis.
F¿ = IbBsin190° - f2 = IbBcosf
F¿
F
S¿;
F
S¿
B
S.
190° - f2
b
F
S
F = IaB
B
S
+x-direction
a)
F
S
I.
B
S,
f
b.
a
902
CHAPTER 27 Magnetic Field and Magnetic Forces
The two pairs of forces acting on the loop cancel, so no net force acts on the loop.
However, the forces on the a sides of the loop (F and 2F) produce a torque
t 5 (IBa)(b sinf) on the loop.
f is the angle
between a vector
normal to the loop
and the magnetic
field.
The torque is maximal
when f 5 90° (so B is in
the plane of the loop).
The torque is zero when 
f 5 0° (as shown here) or
f 5 180°. In both cases,
B is perpendicular to the
plane of the loop.
The loop is in stable equi-
librium when f 5 0; it is
in unstable equilibrium
when f 5 180°.
z
y
I
I
I
I
a
x
b
f
f
f
2F
S
2F
S
B
S
F
S
B
S
B
S
F
S
90° 2 f
b sin f
(b)
(a)
(c)
I
I
y
y
x (direction normal to loop)
z
2F
S
F
S
B
S
B
S
B
S
I
I
z (direction normal
   to loop)
x
2F
S
2F
S
F
S
B
S
B
S
B
S
F
S
S
S
S
S
m
S
m
S
m
S
27.31 Finding the torque on a current-carrying loop in a uniform magnetic field.

27.7 Force and Torque on a Current Loop
903
(equal to the perpendicular distance from the rotation axis to the line of action of
the force) is 
so the torque due to each force has magnitude
If we use Eq. (27.21) for 
the magnitude of the net torque is
(27.22)
The torque is greatest when 
is in the plane of the loop, and the nor-
mal to this plane is perpendicular to 
(Fig. 27.31b). The torque is zero when 
is
or 
and the normal to the loop is parallel or antiparallel to the field (Fig.
27.31c). The value 
is a stable equilibrium position because the torque is
zero there, and when the loop is rotated slightly from this position, the resulting
torque tends to rotate it back toward 
The position 
is an
unstable equilibrium position; if displaced slightly from this position, the loop
tends to move farther away from 
Figure 27.31 shows rotation about
the y-axis, but because the net force on the loop is zero, Eq. (27.22) for the torque
is valid for any choice of axis.
The area 
of the loop is equal to 
so we can rewrite Eq. (27.22) as
(magnitude of torque on a current loop)
(27.23)
The product 
is called the magnetic dipole moment or magnetic moment of
the loop, for which we use the symbol 
(the Greek letter mu):
(27.24)
It is analogous to the electric dipole moment introduced in Section 21.7. In terms
of 
the magnitude of the torque on a current loop is
(27.25)
where 
is the angle between the normal to the loop (the direction of the vector
area 
and 
The torque tends to rotate the loop in the direction of decreasing
-that is, toward its stable equilibrium position in which the loop lies in the
perpendicular to the direction of the field 
(Fig. 27.31c). A current
loop, or any other body that experiences a magnetic torque given by Eq. (27.25),
is also called a magnetic dipole.
Magnetic Torque: Vector Form
We can also define a vector magnetic moment 
with magnitude 
This is shown
in Fig. 27.31. The direction of 
is defined to be perpendicular to the plane of the
loop, with a sense determined by a right-hand rule, as shown in Fig. 27.32. Wrap
the fingers of your right hand around the perimeter of the loop in the direction of
the current. Then extend your thumb so that it is perpendicular to the plane of the
loop; its direction is the direction of 
(and of the vector area 
of the loop). The
torque is greatest when 
and 
are perpendicular and is zero when they are par-
allel or antiparallel. In the stable equilibrium position, 
and 
are parallel.
Finally, we can express this interaction in terms of the torque vector 
which
we used for electric-dipole interactions in Section 21.7. From Eq. (27.25) the
magnitude of 
is equal to the magnitude of 
and reference to Fig. 27.31
shows that the directions are also the same. So we have
(vector torque on a current loop)
(27.26)
This result is directly analogous to the result we found in Section 21.7 for the
torque exerted by an electric field 
on an electric dipole with dipole moment 
Potential Energy for a Magnetic Dipole
When a magnetic dipole changes orientation in a magnetic field, the field does
work on it. In an infinitesimal angular displacement 
, the work 
is given by
dW
df
p
S.
E
S
T
S  M
S : B
S
M
S : B
S,
T
S
T
S,
B
S
M
S
B
S
M
S
A
S
M
S
M
S
IA:
M
S
B
S
xy-plane
f
B
S.
A
S2
f
t = mBsinf
m,
m = IA
m
IA
t = IBAsinf
ab,
A
f = 180°.
f = 180°
f = 0°.
f = 0°
180°
0°
f
B
S B
S
f = 90°,
t = 2F1b>22sinf = 1IBa21bsinf2
F,
F1b>22sinf.
1b>22sinf,
I
I
I
I
A
S
m
S
27.32 The right-hand rule determines
the direction of the magnetic moment of a
current-carrying loop. This is also the
direction of the loop’s area vector 
is a vector equation.
M
S  IA
S
A
S;

and there is a corresponding change in potential energy. As the above dis-
cussion suggests, the potential energy is least when 
and 
are parallel and
greatest when they are antiparallel. To find an expression for the potential energy
as a function of orientation, we can make use of the beautiful symmetry
between the electric and magnetic dipole interactions. The torque on an electric
dipole in an electric field is 
we found in Section 21.7 that the corre-
sponding potential energy is 
The torque on a magnetic dipole in a
magnetic field is 
so we can conclude immediately that the corre-
sponding potential energy is
(potential energy for a magnetic dipole)
(27.27)
With this definition, 
is zero when the magnetic dipole moment is perpendicular
to the magnetic field.
Magnetic Torque: Loops and Coils
Although we have derived Eqs. (27.21) through (27.27) for a rectangular current
loop, all these relationships are valid for a plane loop of any shape at all. Any pla-
nar loop may be approximated as closely as we wish by a very large number of
rectangular loops, as shown in Fig. 27.33. If these loops all carry equal currents
in the same clockwise sense, then the forces and torques on the sides of two loops
adjacent to each other cancel, and the only forces and torques that do not cancel
are due to currents around the boundary. Thus all the above relationships are
valid for a plane current loop of any shape, with the magnetic moment 
given
by
We can also generalize this whole formulation to a coil consisting of 
planar
loops close together; the effect is simply to multiply each force, the magnetic
moment, the torque, and the potential energy by a factor of 
An arrangement of particular interest is the solenoid, a helical winding of
wire, such as a coil wound on a circular cylinder (Fig. 27.34). If the windings are
closely spaced, the solenoid can be approximated by a number of circular loops
lying in planes at right angles to its long axis. The total torque on a solenoid in a
magnetic field is simply the sum of the torques on the individual turns. For a sole-
noid with 
turns in a uniform field 
the magnetic moment is 
and
(27.28)
where 
is the angle between the axis of the solenoid and the direction of the
field. The magnetic moment vector 
is along the solenoid axis. The torque is
greatest when the solenoid axis is perpendicular to the magnetic field and zero
when they are parallel. The effect of this torque is to tend to rotate the solenoid
into a position where its axis is parallel to the field. Solenoids are also useful as
sources of magnetic field, as we’ll discuss in Chapter 28.
The d’Arsonval galvanometer, described in Section 26.3, makes use of a mag-
netic torque on a coil carrying a current. As Fig. 26.14 shows, the magnetic field
is not uniform but is radial, so the side thrusts on the coil are always perpendicu-
lar to its plane. Thus the angle 
in Eq. (27.28) is always 
and the magnetic
torque is directly proportional to the current, no matter what the orientation of the
coil. A restoring torque proportional to the angular displacement of the coil is
provided by two hairsprings, which also serve as current leads to the coil. When
current is supplied to the coil, it rotates along with its attached pointer until the
restoring spring torque just balances the magnetic torque. Thus the pointer
deflection is proportional to the current.
An important medical application of the torque on a magnetic dipole is
magnetic resonance imaging (MRI). A patient is placed in a magnetic field
of about 1.5 T, more than 
times stronger than the earth’s field. The nucleus of
each hydrogen atom in the tissue to be imaged has a magnetic dipole moment,
104
90°,
f
M
S
f
t = NIABsinf
m = NIA
B,
N
N.
N
M
S  IA
S.
M
S
U
U = -M
S # B
S = -mBcosf
M
S : B
S,
T
S 
U = p
S# E
S.
T
S  p
S : E
S;
U
B
S
M
S
tdf,
904
CHAPTER 27 Magnetic Field and Magnetic Forces
The torque tends to make the solenoid rotate
clockwise in the plane of the page, aligning
magnetic moment m with field B.
S
S
I
I
B
S
m
S
t
S
f
27.34 The torque 
on this
solenoid in a uniform magnetic field is
directed straight into the page. An actual
solenoid has many more turns, wrapped
closely together.
T
S  M
S : B
S
I
I
I
I
A planar current loop
  of any shape can be
    approximated by a
      set of rectangular
         loops.
27.33 The collection of rectangles
exactly matches the irregular plane loop in
the limit as the number of rectangles
approaches infinity and the width of each
rectangle approaches zero.
?

27.7 Force and Torque on a Current Loop
905
which experiences a torque that aligns it with the applied field. The tissue is then
illuminated with radio waves of just the right frequency to flip these magnetic
moments out of alignment. The extent to which these radio waves are absorbed in
the tissue is proportional to the amount of hydrogen present. Hence hydrogen-
rich soft tissue looks quite different from hydrogen-deficient bone, which makes
MRI ideal for analyzing details in soft tissue that cannot be seen in x-ray images
(see the image that opens this chapter).
