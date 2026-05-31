Example 28.1
Forces between two moving protons
Two protons move parallel to the x-axis in opposite directions 
(Fig. 28.2) at the same speed 
(small compared to the speed of
light c). At the instant shown, find the electric and magnetic forces
on the upper proton and compare their magnitudes.
SOLUTION
IDENTIFY and SET UP: Coulomb’s law [Eq. (21.2)] gives the elec-
tric force 
on the upper proton. The magnetic force law [Eq.
(27.2)] gives the magnetic force on the upper proton; to use it, we
must first use Eq. (28.2) to find the magnetic field that the lower
proton produces at the position of the upper proton. The unit vector
from the lower proton (the source) to the position of the upper pro-
ton is 
EXECUTE: From Coulomb’s law, the magnitude of the electric force
on the upper proton is
FE =
1
4pP0
q2
r 2
rn  ≥n.
FE
v
28.2 Electric and magnetic forces between two moving protons.
y
q
q
z
x
r
B
S
v
S
2v
S
FE
S
FB
S
r^
Continued

926
CHAPTER 28 Sources of Magnetic Field
The forces are repulsive, and the force on the upper proton is verti-
cally upward (in the 
The velocity of the lower proton is 
. From the right-
hand rule for the cross product 
in Eq. (28.2), the 
due
to the lower proton at the position of the upper proton is in the
(see Fig. 28.2). From Eq. (28.2), the field is
The velocity of the upper proton is 
, so the magnetic
force on it is
The magnetic interaction in this situation is also repulsive. The
ratio of the force magnitudes is
 m0
4p
q2v2
r 2 ≥n
kN
m0
4p
qv
r 2
F
S
B  q1-v
S2 : B
S  q1-vın2 :
-v
S  -vın
B
S  m0
4p
q1vın2 : ≥n
r 2
 m0
4p
qv
r 2 kN
+z-direction
B
S field
v
S : rn
v
S  vın
+y-direction).
Test Your Understanding of Section 28.1
(a) If two protons are traveling
parallel to each other in the same direction and at the same speed, is the magnetic force
between them (i) attractive or (ii) repulsive? (b) Is the net force between them (i) attrac-
tive, (ii) repulsive, or (iii) zero? (Assume that the protons’ speed is much slower than the
speed of light.)
❙
With the relationship 
Eq. (28.4), this becomes
When 
is small in comparison to the speed of light, the magnetic
force is much smaller than the electric force.
EVALUATE: We have described the velocities, fields, and forces as
they are measured by an observer who is stationary in the coordinate
system of Fig. 28.2. In a coordinate system that moves with one of
the charges, one of the velocities would be zero, so there would be
no magnetic force. The explanation of this apparent paradox pro-
vided one of the paths that led to the special theory of relativity.
v
FB
FE
= v2
c2
P0m0 = 1>c2,
FB
FE
= m0q2v2>4pr 2
q2>4pP0r 2
= m0v2
1>P0
= P0m0v2
28.2 Magnetic Field of a Current Element
Just as for the electric field, there is a principle of superposition of magnetic
fields:
The total magnetic field caused by several moving charges is the vector sum of
the fields caused by the individual charges.
We can use this principle with the results of Section 28.1 to find the magnetic
field produced by a current in a conductor.
We begin by calculating the magnetic field caused by a short segment 
of a
current-carrying conductor, as shown in Fig. 28.3a. The volume of the segment is
A dl, where A is the cross-sectional area of the conductor. If there are n moving
charged particles per unit volume, each of charge q, the total moving charge dQ
in the segment is
The moving charges in this segment are equivalent to a single charge dQ, trav-
eling with a velocity equal to the drift velocity 
(Magnetic fields due to the
random motions of the charges will, on average, cancel out at every point.) From
Eq. (28.1) the magnitude of the resulting field 
at any field point P is
But from Eq. (25.2), 
equals the current I in the element. So
(28.5)
Current Element: Vector Magnetic Field
In vector form, using the unit vector as in Section 28.1, we have
(magnetic field of a current element)
(28.6)
dB
S  m0
4p
I dl
S : rn
r 2
rn
dB = m0
4p
I dlsinf
r 2
nƒqƒvd A
dB = m0
4p
ƒdQƒvdsinf
r 2
= m0
4p
nƒqƒvd A dlsinf
r 2
dB
S
v
S
d.
dQ = nqA dl
dl
S
P
dB 5 0
I
dB 5 0
dB
S
dB
S
dB
S
dB
S
dB
S
dB
S
dl
S
^
rS
(a) Perspective view
Right-hand rule for the magnetic field due to
a current element: Point the thumb of your
right hand in the direction of the current. Your
fingers now curl around the current element in
the direction of the magnetic field lines.
For these field points, r and dl both lie in the
beige plane, and dB is perpendicular to this
plane.
S
S
S
For these field points, r and dl both lie in the
gold plane, and dB is perpendicular to this plane.
S
S
S
Axis of dl
S
I
r
f
dB
S
Current directed into
the plane of the page
(b) View along the axis of the current
element
28.3 (a) Magnetic-field vectors due to 
a current element 
(b) Magnetic field
lines in a plane containing the current ele-
ment 
Compare this figure to Fig. 28.1
for the field of a moving point charge.
dl
S.
dl
S.

where 
is a vector with length dl, in the same direction as the current in the
conductor.
Equations (28.5) and (28.6) are called the law of Biot and Savart (pro-
nounced “Bee-oh” and “Suh-var”). We can use this law to find the total magnetic
field 
at any point in space due to the current in a complete circuit. To do this,
we integrate Eq. (28.6) over all segments 
that carry current; symbolically,
(28.7)
In the following sections we will carry out this vector integration for several
examples.
Current Element: Magnetic Field Lines
As Fig. 28.3 shows, the field vectors 
and the magnetic field lines of a current
element are exactly like those set up by a positive charge dQ moving in the direc-
tion of the drift velocity 
The field lines are circles in planes perpendicular to
and centered on the line of 
Their directions are given by the same right-
hand rule that we introduced for point charges in Section 28.1.
We can’t verify Eq. (28.5) or (28.6) directly because we can never experiment
with an isolated segment of a current-carrying circuit. What we measure experi-
mentally is the total
for a complete circuit. But we can still verify these equations
indirectly by calculating 
for various current configurations using Eq. (28.7) and
comparing the results with experimental measurements.
If matter is present in the space around a current-carrying conductor, the field
at a field point P in its vicinity will have an additional contribution resulting from
the magnetization of the material. We’ll return to this point in Section 28.8. How-
ever, unless the material is iron or some other ferromagnetic material, the addi-
tional field is small and is usually negligible. Additional complications arise if
time-varying electric or magnetic fields are present or if the material is a super-
conductor; we’ll return to these topics later.
B
S
B
S
dl
S.
dl
S
v
S
d.
dB
S
B
S  m0
4p L
I dl
S : rn
r 2
dl
S
B
S
dl
S
28.2 Magnetic Field of a Current Element
927
Problem-Solving Strategy 28.1
Magnetic-Field Calculations
IDENTIFY the relevant concepts: The Biot-Savart law [Eqs. (28.5)
and (28.6)] allows you to calculate the magnetic field at a field
point P due to a current-carrying wire of any shape. The idea is to
calculate the field element 
at P due to a representative current
element in the wire and integrate all such field elements to find the
field 
at P.
SET UP the problem using the following steps:
1. Make a diagram showing a representative current element and
the field point P.
2. Draw the current element 
being careful that it points in the
direction of the current.
3. Draw the unit vector 
directed from the current element (the
source point) to P.
4. Identify the target variable (usually ).
EXECUTE the solution as follows:
1. Use Eq. (28.5) or (28.6) to express the magnetic field 
at P
from the representative current element.
2. Add up all the 
’s to find the total field at point P. In some sit-
uations the
’s at point P have the same direction for all the
current elements; then the magnitude of the total 
field is the
B
S
dB
SdB
S
dB
S
B
S
rn
dl
S,
B
S
dB
S
sum of the magnitudes of the 
’s. But often the 
’s have dif-
ferent directions for different current elements. Then you have
to set up a coordinate system and represent each 
in terms of
its components. The integral for the total 
is then expressed in
terms of an integral for each component.
3. Sometimes you can use the symmetry of the situation to prove
that one component of 
must vanish. Always be alert for ways
to use symmetry to simplify the problem.
4. Look for ways to use the principle of superposition of mag-
netic fields. Later in this chapter we’ll determine the fields pro-
duced by certain simple conductor shapes; if you encounter a
conductor of a complex shape that can be represented as a
combination of these simple shapes, you can use superposition
to find the field of the complex shape. Examples include a rec-
tangular loop and a semicircle with straight line segments on
both sides.
EVALUATE your answer: Often your answer will be a mathemati-
cal expression for 
as a function of the position of the field point.
Check the answer by examining its behavior in as many limits as
you can.
B
S
B
S
B
S
dB
S
dB
S
dB
S

928
CHAPTER 28 Sources of Magnetic Field
28.3 Magnetic Field of a Straight 
Current-Carrying Conductor
Let’s use the law of Biot and Savart to find the magnetic field produced by a
straight current-carrying conductor. This result is useful because straight conduct-
ing wires are found in essentially all electric and electronic devices. Figure 28.5
shows such a conductor with length 2a carrying a current I. We will find 
at a
point a distance x from the conductor on its perpendicular bisector.
We first use the law of Biot and Savart, Eq. (28.5), to find the field 
caused by
the element of conductor of length 
shown in Fig. 28.5. From the figure,
and 
The right-hand rule
for the vector product 
shows that the direction of 
is into the plane of
the figure, perpendicular to the plane; furthermore, the directions of the 
from all elements of the conductor are the same. Thus in integrating Eq. (28.7),
we can just add the magnitudes of the 
a significant simplification.
dB
S’s,
dB
S’s
dB
S
dl
S : rn
sinf = sin1p - f2 = x> 2x2 + y2.
r = 2x2 + y2
dl = dy
dB
S
B
S
