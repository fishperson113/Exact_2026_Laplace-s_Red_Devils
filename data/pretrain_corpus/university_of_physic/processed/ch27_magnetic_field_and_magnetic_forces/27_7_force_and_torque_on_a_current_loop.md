Example 27.8 Magnetic force on a curved conductor

27.7 Force and Torque on a Current Loop

901

S
In Fig. 27.30 the magnetic ﬁeld
is uniform and perpendicular to
B
the  plane  of  the  ﬁgure,  pointing  out  of  the  page.  The  conductor,
carrying current I to the left, has three segments: (1) a straight seg-
ment with length L perpendicular to the plane of the ﬁgure, (2) a
,  and  (3)  another  straight  segment  with
semicircle  with  radius
length  parallel to the
Find the total magnetic force on this
conductor.

R
x-axis.

L

SOLUTION

S
B

S
F
3

S
F
1

and

N
(cid:2) Bk
IDENTIFY and SET UP: The magnetic ﬁeld
is uniform, so
on the straight segments (1) and (3)
we ﬁnd the forces
using Eq. (27.19). We divide the curved segment (2) into inﬁnites-
on
imal  straight  segments  and  ﬁnd  the  corresponding  force
each straight segment using Eq. (27.20). We then integrate to ﬁnd
S
(cid:2)
The  total  magnetic  force  on  the  conductor  is  then
2.
F
S
1 (cid:3) F
F

2 (cid:3) F
3.

S
dF
2

S
F

S

S

27.30 What is the total magnetic force on the conductor?

S
B (out)

S
F

I

I

S
L

L

y

R

O

dFy

S
dF

S
dl

dl

u

du

u

dFx

I

x

I (in)

S

S

(cid:2) -Lın,

S
3 (cid:2) IL
F

S
N
(cid:2) -Lk
L
For  segment  (3),
N2 (cid:2) ILB≥n.

EXECUTE: For  segment  (1),
S
S
(cid:2) 0.
: B
1 (cid:2) IL
F
S
(cid:2) I1-Lın2 : 1Bk
B
For  the  curved  segment  (2),  Fig.  27.20 shows  a  segment
u.

.  Hence  from  Eq.  (27.19),
S
:
so
L

S
d l
at angle  The right-hand rule shows that
is radially outward from the center; make
are perpendicular, the
dF2 =
is  just
. The components of the force on this segment

dl = R du,
with length
S
: B
the direction of
d l
sure you can verify this. Because
magnitude
I dl B = I1R du2B
are

of  the  force  on  the  segment

dF2

and

S
d l

S
d l

S
B

S

dF2x = IR du B cos u    dF2y = IR du B sin u

To  ﬁnd  the  components  of  the  total  force,  we  integrate  these
expressions with respect to θ from
to take in the
whole semicircle. The results are
p

u = 0

u = p

to

F2x = IRB

F2y = IRB

L
0

L
0

cos u du = 0

p
sin u du = 2IRB

S
2 (cid:2) 2IRB≥n
F

.  Finally,  adding  the  forces  on  all  three  seg-

Hence
ments, we ﬁnd that the total force is in the positive y-direction:
3 (cid:2) 0 (cid:3) 2IRB≥n (cid:3) ILB≥n (cid:2) IB12R + L2≥n

1 (cid:3) F

2 (cid:3) F

(cid:2) F

S
F

S

S

S

S
F
2

EVALUATE:  We  could  have  predicted  from  symmetry  that  the
x-component of  would be zero: On the right half of the semicircle
the x-component of the force is positive (to the right) and on the
left half it is negative (to the left); the positive and negative contri-
butions to the integral cancel. The result is that
is the force that
would be exerted if we replaced the semicircle with a straight seg-
ment of length 2R along the x-axis. Do you see why?

S
F
2

Test Your Understanding of Section 27.6 The ﬁgure at right shows a top
view of two conducting rails on which a conducting bar can slide. A uniform magnetic
ﬁeld is directed perpendicular to the plane of the ﬁgure as shown. A battery is to be con-
nected to the two rails so that when the switch is closed, current will ﬂow through the bar
and cause a magnetic force to push the bar to the right. In which orientation, A or B,
should the battery be placed in the circuit?

Switch

Conducting
bar

Which
orientation?

A

B

Conducting
rails

S
F

S
B

❙

27.7 Force and Torque on a Current Loop

Current-carrying conductors usually form closed loops, so it is worthwhile to use
the results of Section 27.6 to ﬁnd the total magnetic force and torque on a con-
ductor in the form of a loop. Many practical devices make use of the magnetic
force or torque on a conducting loop, including loudspeakers (see Fig. 27.28) and
galvanometers (see Section 26.3). Hence the results of this section are of substan-
tial practical importance. These results will also help us understand the behavior
of bar magnets described in Section 27.1.

As an example, let’s look at a rectangular current loop in a uniform magnetic
ﬁeld. We can represent the loop as a series of straight line segments. We will ﬁnd

ActivPhysics 13.6: Magnetic Torque on a
Loop

902

CHAPTER 27 Magnetic Field and Magnetic Forces

27.31 Finding the torque on a current-carrying loop in a uniform magnetic ﬁeld.

(a)

(b)

The two pairs of forces acting on the loop cancel, so no net force acts on the loop.

However, the forces on the a sides of the loop (F and 2F) produce a torque
z
t 5 (IBa)(b sin f) on the loop.

S

S

y

f is the angle
between a vector
normal to the loop
and the magnetic
field.

S

F(cid:3)

I

S
B

I

mS

S
B
f

90° 2 f

f

S
B

a

S

2F

f

I

S
F

b sin f

I

S

2F(cid:3)

b

The torque is maximal
when f 5 90° (so B is in
the plane of the loop).

S

x (direction normal to loop)

z

S
B

S
B

S
B

S
F

I

y

I

x

mS

y

S

F(cid:3)

(c)

S
B

S

2F

S

2F

mS

S
B

z (direction normal
   to loop)

S
B

I

I

S
F

x

S

2F(cid:3)

The torque is zero when
f 5 0° (as shown here) or
f 5 180°. In both cases,
S
B is perpendicular to the
plane of the loop.

The loop is in stable equi-
librium when f 5 0; it is
in unstable equilibrium
when f 5 180°.

that the total force on the loop is zero but that there can be a net torque acting on
the loop, with some interesting properties.

Figure 27.31a shows a rectangular loop of wire with side lengths

b.
and  A
line perpendicular to the plane of the loop (i.e., a normal to the plane) makes an
angle  with the direction of the magnetic ﬁeld
and the loop carries a current
I.
The wires leading the current into and out of the loop and the source of emf are
omitted to keep the diagram simple.

S
B

f

a

,

The  force
S
+x-direction
B
and the force on this side has magnitude

S
F
as shown. On this side,

on  the  right  side  of  the  loop  (length

is  to  the  right,  in  the
is perpendicular to the current direction,

a)

F = IaB

(27.21)

with the same magnitude but opposite direction acts on the opposite

S

(cid:4)F

A force
side of the loop, as shown in the ﬁgure.

The sides with length  make an angle

b

forces on these sides are the vectors

190° - f2
(cid:4)F

S
with the direction of  The
.
B
F¿
is given by

their magnitude

¿;

S

S
F

¿

and
F¿ = IbB sin190° - f2 = IbB cos f

The lines of action of both forces lie along the

y-axis.

The total force on the loop is zero because the forces on opposite sides cancel

out in pairs.

The net force on a current loop in a uniform magnetic ﬁeld is zero. However, the
net torque is not in general equal to zero.

¿

S

S
F

and

(cid:4)F

(You may ﬁnd it helpful at this point to review the discussion of torque in Section
¿
in Fig. 27.31a lie along the same line and so
10.1.) The two forces
S
(cid:4)F
give rise to zero net torque with respect to any point. The two forces
lie along different lines, and each gives rise to a torque about the y-axis. Accord-
ing  to  the  right-hand  rule  for  determining  the  direction  of  torques,  the  vector
torques  due  to
hence  the  net  vector
TS
as well. The moment arm for each of these forces
torque

(cid:4)F
and
+y-direction

S
F
is in the

are  both  in  the

+y-direction;

and

S
F

S

27.7 Force and Torque on a Current Loop

903

(equal to the perpendicular distance from the rotation axis to the line of action of
so  the  torque  due  to  each  force  has  magnitude
the  force)  is
F1b>22 sin f.

1b>22 sin f,
If we use Eq. (27.21) for

the magnitude of the net torque is

F,
t = 2F1b>22 sin f = 1IBa21b sin f2

(27.22)

S

or

180°

f = 0°

f = 90°,
S B
B

(Fig. 27.31b). The torque is zero when

is in the plane of the loop, and the nor-
The torque is greatest when
mal to this plane is perpendicular to
is
and the normal to the loop is parallel or antiparallel to the ﬁeld (Fig.
0°
27.31c). The value
is a stable equilibrium position because the torque is
zero there, and when the loop is rotated slightly from this position, the resulting
is  an
torque  tends  to  rotate  it  back  toward
unstable equilibrium  position;  if  displaced  slightly  from  this  position,  the  loop
f = 180°.
tends to move farther away from
Figure 27.31 shows rotation about
the y-axis, but because the net force on the loop is zero, Eq. (27.22) for the torque
is valid for any choice of axis.

The  position

f = 180°

f = 0°.

f

The area  of the loop is equal to

A

ab,

so we can rewrite Eq. (27.22) as

t = IBA sin f

(magnitude of torque on a current loop)

(27.23)

The product
the loop, for which we use the symbol

IA

m

is called the magnetic dipole moment or magnetic moment of

(the Greek letter mu):

m = IA

(27.24)

It is analogous to the electric dipole moment introduced in Section 21.7. In terms
of

the magnitude of the torque on a current loop is

m,

t = mB sin f

(27.25)

S
.
B

f
is the angle between the normal to the loop (the direction of the vector
where
S
2
A
area
The torque tends to rotate the loop in the direction of decreasing
and
f
—that  is,  toward  its  stable  equilibrium  position  in  which  the  loop  lies  in  the
xy-plane
(Fig.  27.31c). A current
loop, or any other body that experiences a magnetic torque given by Eq. (27.25),
is also called a magnetic dipole.

perpendicular  to  the  direction  of  the  ﬁeld

S
B

MS

Magnetic Torque: Vector Form
This is shown
We can also deﬁne a vector magnetic moment  with magnitude
MS
in Fig. 27.31. The direction of
is deﬁned to be perpendicular to the plane of the
loop, with a sense determined by a right-hand rule, as shown in Fig. 27.32. Wrap
the ﬁngers of your right hand around the perimeter of the loop in the direction of
the current. Then extend your thumb so that it is perpendicular to the plane of the
(and of the vector area  of the loop). The
loop; its direction is the direction of
torque is greatest when
are perpendicular and is zero when they are par-
allel or antiparallel. In the stable equilibrium position,

and

and

IA:

S
A

S
B

S
B

MS

MS

MS

Finally, we can express this interaction in terms of the torque vector  which
we  used  for  electric-dipole  interactions  in  Section  21.7.  From  Eq.  (27.25) the
magnitude of
and reference to Fig. 27.31
shows that the directions are also the same. So we have

is equal to the magnitude of

MS : B
,

TS

S

are parallel.
TS
,

TS (cid:2) MS : B

S

(vector torque on a current loop)

(27.26)

This  result  is  directly  analogous  to  the  result  we  found  in  Section  21.7  for  the
S
p
.
torque exerted by an electric ﬁeld  on an electric dipole with dipole moment

S
E

Potential Energy for a Magnetic Dipole
When a magnetic dipole changes orientation in a magnetic ﬁeld, the ﬁeld does
is given by
work on it. In an inﬁnitesimal angular displacement

, the work

df

dW

27.32 The right-hand rule determines
the direction of the magnetic moment of a
current-carrying loop. This is also the
S
direction of the loop’s area vector
;
A
MS (cid:2) IA

is a vector equation.

S

I

mS

I

S
A

I

I

904

CHAPTER 27 Magnetic Field and Magnetic Forces

MS

t df,
and there is a corresponding change in potential energy. As the above dis-
cussion  suggests,  the  potential  energy  is  least  when
are  parallel  and
greatest when they are antiparallel. To ﬁnd an expression for the potential energy
U
as  a  function  of  orientation,  we  can  make  use  of  the  beautiful  symmetry
between the electric and magnetic dipole interactions. The torque on an electric
S : E
TS (cid:2) p
S # E
;
we found in Section 21.7 that the corre-
dipole in an electric ﬁeld is
S
U = (cid:4) p
.
sponding potential energy is
The torque on a magnetic dipole in a
S
MS : B
,
magnetic ﬁeld  is
so  we  can  conclude  immediately  that  the  corre-
sponding potential energy is

TS (cid:2)

and

S
B

S

U = - MS # B

S

= - mB cos f

(potential energy for a magnetic dipole)

(27.27)

U
With this deﬁnition,
to the magnetic ﬁeld.

is zero when the magnetic dipole moment is perpendicular

27.33 The collection of rectangles
exactly matches the irregular plane loop in
the limit as the number of rectangles
approaches inﬁnity and the width of each
rectangle approaches zero.

I

A planar current loop
  of any shape can be
    approximated by a
      set of rectangular
         loops.

I

I

I

S

TS (cid:2) MS : B

27.34 The torque
solenoid in a uniform magnetic ﬁeld is
directed straight into the page. An actual
solenoid has many more turns, wrapped
closely together.

on this

mS

f

I

tS

I

S
B

The torque tends to make the solenoid rotate
clockwise in the plane of the page, aligning
magnetic moment m with field B.

S

S

Magnetic Torque: Loops and Coils
Although we have derived Eqs. (27.21) through (27.27) for a rectangular current
loop, all these relationships are valid for a plane loop of any shape at all. Any pla-
nar loop may be approximated as closely as we wish by a very large number of
rectangular loops, as shown in Fig. 27.33. If these loops all carry equal currents
in the same clockwise sense, then the forces and torques on the sides of two loops
adjacent to each other cancel, and the only forces and torques that do not cancel
are  due  to  currents  around  the  boundary.  Thus  all  the  above  relationships  are
valid for a plane current loop of any shape, with the magnetic moment
given
by

MS (cid:2) IA
.
We can also generalize this whole formulation to a coil consisting of  planar
loops  close  together;  the  effect  is  simply  to  multiply  each  force,  the  magnetic
moment, the torque, and the potential energy by a factor of

N.

MS

N

S

An  arrangement  of  particular  interest  is  the  solenoid, a  helical  winding  of
wire, such as a coil wound on a circular cylinder (Fig. 27.34). If the windings are
closely spaced, the solenoid can be approximated by a number of circular loops
lying in planes at right angles to its long axis. The total torque on a solenoid in a
magnetic ﬁeld is simply the sum of the torques on the individual turns. For a sole-
noid with

the magnetic moment is

turns in a uniform ﬁeld

m = NIA

and

B,

N

t = NIAB sin f

(27.28)

f

is  the  angle  between  the  axis  of  the  solenoid  and  the  direction  of  the
where
ﬁeld. The magnetic moment vector
is along the solenoid axis. The torque is
greatest when the solenoid axis is perpendicular to the magnetic ﬁeld and zero
when they are parallel. The effect of this torque is to tend to rotate the solenoid
into a position where its axis is parallel to the ﬁeld. Solenoids are also useful as
sources of magnetic ﬁeld, as we’ll discuss in Chapter 28.

MS

The d’Arsonval galvanometer, described in Section 26.3, makes use of a mag-
netic torque on a coil carrying a current. As Fig. 26.14 shows, the magnetic ﬁeld
is not uniform but is radial, so the side thrusts on the coil are always perpendicu-
lar to its plane. Thus the angle
and the magnetic
torque is directly proportional to the current, no matter what the orientation of the
coil. A restoring  torque  proportional  to  the  angular  displacement  of  the  coil  is
provided by two hairsprings, which also serve as current leads to the coil. When
current is supplied to the coil, it rotates along with its attached pointer until the
restoring  spring  torque  just  balances  the  magnetic  torque.  Thus  the  pointer
deﬂection is proportional to the current.

in Eq. (27.28) is always

90°,

f

An important medical application of the torque on a magnetic dipole is
magnetic resonance imaging (MRI). A patient is placed in a magnetic ﬁeld
of about 1.5 T, more than
times stronger than the earth’s ﬁeld. The nucleus of
each hydrogen atom in the tissue to be imaged has a magnetic dipole moment,

104

?

27.7 Force and Torque on a Current Loop

905

which experiences a torque that aligns it with the applied ﬁeld. The tissue is then
illuminated  with  radio  waves  of  just  the  right  frequency  to  ﬂip  these  magnetic
moments out of alignment. The extent to which these radio waves are absorbed in
the  tissue  is  proportional  to  the  amount  of  hydrogen  present.  Hence  hydrogen-
rich soft tissue looks quite different from hydrogen-deﬁcient bone, which makes
MRI ideal for analyzing details in soft tissue that cannot be seen in x-ray images
(see the image that opens this chapter).

Example 27.9 Magnetic torque on a circular coil

A circular coil 0.0500 m in radius, with 30 turns of wire, lies in a
horizontal  plane.  It  carries  a  counterclockwise  (as  viewed  from
above) current of 5.00 A. The coil is in a uniform 1.20-T magnetic
ﬁeld  directed  toward  the  right.  Find  the  magnitudes  of  the  mag-
netic moment and the torque on the coil.

SOLUTION

IDENTIFY  and SET  UP: This problem uses the deﬁnition of mag-
netic  moment  and  the  expression  for  the  torque  on  a  magnetic
dipole  in  a  magnetic  ﬁeld.  Figure  27.35 shows  the  situation.
Equation (27.24) gives the magnitude
of the magnetic moment
of  a  single  turn  of  wire;  for  N turns,  the  magnetic  moment  is  N
of  the
times  greater.  Equation  (27.25) gives  the  magnitude
torque.

m

t

f

The angle

between the direction of
(which is along the normal to the plane of the coil) is
Eq. (27.25), the torque on the coil is

and the direction of

MS
From

90°.

S
B

t = mtotalB sin f = 11.18 A # m2211.20 T21sin 90°2
= 1.41 N # m

EVALUATE:  The  torque  tends  to  rotate  the  right  side  of  the  coil
down and the left side up, into a position where the normal to its
S
plane is parallel to B

.

27.35 Our sketch for this problem.

EXECUTE: The area of the coil is
total magnetic moment of all 30 turns is

A = pr 2

. From Eq. (27.24), the

mtotal = NIA = 3015.00 A2p10.0500 m22 = 1.18 A # m2

Example 27.10

Potential energy for a coil in a magnetic field

If the coil in Example 27.9 rotates from its initial orientation to one
MS
in  which  its  magnetic  moment
what  is  the
change in potential energy?

is  parallel  to

S
B

,

SOLUTION

IDENTIFY and SET UP: Equation (27.27) gives the potential energy
for each orientation. The initial position is as shown in Fig. 27.35,
f1 = 90°.
with
In  the  ﬁnal  orientation,  the  coil  has  been  rotated
MS
clockwise so that
are parallel, so the angle between
90°
these vectors is f2 = 0.

and

S
B

EXECUTE: From Eq. (27.27), the potential energy change is
¢U = U2 - U1 = - mB cos f2 - 1-mB cos f12

= - mB1cos f2 - cos f12
= - 11.18 A # m2211.20 T21cos 0° - cos 90°2 = - 1.41 J

EVALUATE: The potential energy decreases because the rotation is in
the direction of the magnetic torque that we found in Example 27.9.

S
B

Magnetic Dipole in a Nonuniform Magnetic Field
We have seen that a current loop (that is, a magnetic dipole) experiences zero net
force in a uniform magnetic ﬁeld. Figure 27.36 shows two current loops in the
nonuniform ﬁeld of a bar magnet; in both cases the net force on the loop is not
zero. In Fig. 27.36a the magnetic moment
is in the direction opposite to the
S
dF
ﬁeld, and the force
on a segment of the loop has both a radial
component and a component to the right. When these forces are summed to ﬁnd
the net force
on the loop, the radial components cancel so that the net force is
to the right, away from the magnet. Note that in this case the force is toward the
B
region where the ﬁeld lines are farther apart and the ﬁeld magnitude
is less. The
S
are  parallel;
B
polarity  of  the  bar  magnet  is  reversed  in  Fig.  27.36b,  so

(cid:2) I d l

: B

and

S
F

MS

MS

S

S

906

CHAPTER 27 Magnetic Field and Magnetic Forces

S
B

27.36 Forces on current loops in a
nonuniform  ﬁeld. In each case the axis
of the bar magnet is perpendicular to the
plane of the loop and passes through the
center of the loop.

(a) Net force on this coil is away from north
pole of magnet.

S
net F

S

N

mS

S
dF

S
dF

S
dF
SI
dF

(b) Net force on same coil is toward south
pole of magnet.

S
net F

S
dF

S
B

S
B

N

S

mS

S
dF

S
dF

I

S
dF

27.37 (a) An unmagnetized piece of
iron. (Only a few representative atomic
moments are shown.) (b) A magnetized
piece of iron (bar magnet). The net mag-
netic moment of the bar magnet points
from its south pole to its north pole.
(c) A bar magnet in a magnetic ﬁeld.

(a) Unmagnetized iron: magnetic moments
are oriented randomly.

S
m

atom

(b) In a bar magnet, the magnetic moments
are aligned.

mS

N

S

(c) A magnetic field creates a torque on the
bar magnet that tends to align its dipole
S
moment with the B field.

N

S
B

tS

S

mS

now the net force on the loop is to the left, toward the region of greater ﬁeld mag-
nitude  near  the  magnet.  Later  in  this  section  we’ll  use  these  observations  to
explain why bar magnets can pick up unmagnetized iron objects.

S
B

Magnetic Dipoles and How Magnets Work
The behavior of a solenoid in a magnetic ﬁeld (see Fig. 27.34) resembles that of a
bar magnet or compass needle; if free to turn, both the solenoid and the magnet ori-
ent themselves with their axes parallel to the  ﬁeld. In both cases this is due to the
interaction of moving electric charges with a magnetic ﬁeld; the difference is that
in a bar magnet the motion of charge occurs on the microscopic scale of the atom.
Think of an electron as being like a spinning ball of charge. In this analogy the
circulation of charge around the spin axis is like a current loop, and so the elec-
tron has a net magnetic moment. (This analogy, while helpful, is inexact; an elec-
tron isn’t really a spinning sphere. A full explanation of the origin of an electron’s
magnetic  moment  involves  quantum  mechanics,  which  is  beyond  our  scope
here.)  In  an  iron  atom  a  substantial  fraction  of  the  electron  magnetic  moments
align with each other, and the atom has a nonzero magnetic moment. (By con-
trast, the atoms of most elements have little or no net magnetic moment.) In an
unmagnetized  piece  of  iron  there  is  no  overall  alignment  of  the  magnetic
moments of the atoms; their vector sum is zero, and the net magnetic moment is
zero (Fig. 27.37a). But in an iron bar magnet the magnetic moments of many of
the  atoms  are  parallel,  and  there  is  a  substantial  net  magnetic  moment
(Fig.
S
the ﬁeld exerts a torque
27.37b). If the magnet is placed in a magnetic ﬁeld
B
(Fig. 27.37c). A bar magnet
given by Eq. (27.26) that tends to align  with
tends to align with a  ﬁeld so that a line from the south pole to the north pole of
the magnet is in the direction of
hence the real signiﬁcance of a magnet’s north
and south poles is that they represent the head and tail, respectively, of the mag-
net’s dipole moment

S
;
B

S
B

S
B

MS

MS

MS

,

.

The  torque  experienced  by  a  current  loop  in  a  magnetic  ﬁeld  also  explains
how an unmagnetized iron object like that in Fig. 27.37a becomes magnetized. If
an unmagnetized iron paper clip is placed next to a powerful magnet, the mag-
netic moments of the paper clip’s atoms tend to align with the  ﬁeld of the mag-
net. When the paper clip is removed, its atomic dipoles tend to remain aligned,
and the paper clip has a net magnetic moment. The paper clip can be demagnet-
ized by being dropped on the ﬂoor or heated; the added internal energy jostles
and re-randomizes the atomic dipoles.

S
B

The magnetic-dipole picture of a bar magnet explains the attractive and repul-
sive forces between bar magnets shown in Fig. 27.1. The magnetic moment
of
a bar magnet points from its south pole to its north pole, so the current loops in
Figs. 27.36a and 27.36b are both equivalent to a magnet with its north pole on the
left. Hence the situation in Fig. 27.36a is equivalent to two bar magnets with their
north  poles  next  to  each  other;  the  resultant  force  is  repulsive,  just  as  in  Fig.
27.1b.  In  Fig.  27.36b  we  again  have  the  equivalent  of  two  bar  magnets  end  to
end, but with the south pole of the left-hand magnet next to the north pole of the
right-hand magnet. The resultant force is attractive, as in Fig. 27.1a.

MS

MS

S
B

Finally, we can explain how a magnet can attract an unmagnetized iron object
(see Fig. 27.2). It’s a two-step process. First, the atomic magnetic moments of the
iron tend to align with the  ﬁeld of the magnet, so the iron acquires a net mag-
netic dipole moment
parallel to the ﬁeld. Second, the nonuniform ﬁeld of the
magnet attracts the magnetic dipole. Figure 27.38a shows an example. The north
pole of the magnet is closer to the nail (which contains iron), and the magnetic
dipole produced in the nail is equivalent to a loop with a current that circulates in a
direction opposite to that shown in Fig. 27.36a. Hence the net magnetic force on
the nail is opposite to the force on the loop in Fig. 27.36a, and the nail is attracted
toward  the  magnet.  Changing  the  polarity  of  the  magnet,  as  in  Fig.  27.38b,
MS
.
The situation is now equivalent to that
reverses the directions of both

and

S
B
