Example 28.10
Field of a toroidal solenoid
Figure 28.25a shows a doughnut-shaped toroidal solenoid, tightly
wound with N turns of wire carrying a current I. (In a practical
solenoid the turns would be much more closely spaced than they
are in the figure.) Find the magnetic field at all points.
SOLUTION
IDENTIFY and SET UP: Ignoring the slight pitch of the helical wind-
ings, we can consider each turn of a tightly wound toroidal solenoid
as a loop lying in a plane perpendicular to the large, circular axis of
the toroid. The symmetry of the situation then tells us that the mag-
netic field lines must be circles concentric with the toroid axis. There-
fore we choose circular integration paths (of which Fig. 28.25b
shows three) for use with Ampere’s law, so that the field 
(if any) is
tangent to each path at all points along the path.
EXECUTE: Along each path, 
equals the product of B and
the path circumference 
. The total current enclosed by
path 1 is zero, so from Ampere’s law the field 
everywhere
on this path.
Each turn of the winding passes twice through the area bounded
by path 3, carrying equal currents in opposite directions. The net
B
S  0
l = 2pr
AB
S # dl
S
B
S
O
Path 1
Path 2
Path 3
(a)
(b)
I
I
r
B
r
The magnetic field is confined almost entirely
to the space enclosed by the windings (in blue).
28.25 (a) A toroidal solenoid. For clarity, only a few turns of
the winding are shown. (b) Integration paths (black circles) used
to compute the magnetic field
set up by the current (shown as
dots and crosses).
B
S
current enclosed is therefore zero, and hence 
at all points
on this path as well. We conclude that the field of an ideal toroidal
B
S  0
?

28.8 Magnetic Materials
941
28.8 Magnetic Materials
In discussing how currents cause magnetic fields, we have assumed that the con-
ductors are surrounded by vacuum. But the coils in transformers, motors, genera-
tors, and electromagnets nearly always have iron cores to increase the magnetic
field and confine it to desired regions. Permanent magnets, magnetic recording
tapes, and computer disks depend directly on the magnetic properties of materi-
als; when you store information on a computer disk, you are actually setting up
an array of microscopic permanent magnets on the disk. So it is worthwhile to
examine some aspects of the magnetic properties of materials. After describing
the atomic origins of magnetic properties, we will discuss three broad classes of
magnetic behavior that occur in materials; these are called paramagnetism, dia-
magnetism, and ferromagnetism.
The Bohr Magneton
As we discussed briefly in Section 27.7, the atoms that make up all matter con-
tain moving electrons, and these electrons form microscopic current loops that
produce magnetic fields of their own. In many materials these currents are ran-
domly oriented and cause no net magnetic field. But in some materials an exter-
nal field (a field produced by currents outside the material) can cause these loops
to become oriented preferentially with the field, so their magnetic fields add to
the external field. We then say that the material is magnetized.
Let’s look at how these microscopic currents come about. Figure 28.26 shows
a primitive model of an electron in an atom. We picture the electron (mass m,
charge 
as moving in a circular orbit with radius r and speed 
This moving
charge is equivalent to a current loop. In Section 27.7 we found that a current
loop with area A and current I has a magnetic dipole moment 
given by 
for the orbiting electron the area of the loop is 
To find the current
A = pr 2.
m = IA;
m
v.
-e)
solenoid is confined to the space enclosed by the windings. We can
think of such a solenoid as a tightly wound, straight solenoid that
has been bent into a circle.
For path 2, we have 
Each turn of the wind-
ing passes once through the area bounded by this path, so
We note that 
is positive for the clockwise direction
of integration in Fig. 28.25b, so 
is in the direction shown.
Ampere’s law then says that 
, so
(toroidal solenoid)
(28.24)
EVALUATE: Equation (28.24) indicates that B is not uniform over
the interior of the core, because different points in the interior are
difference distances r from the toroid axis. However, if the radial
extent of the core is small in comparison to r, the variation is
slight. In that case, considering that 
is the circumferential
2pr
B = m0NI
2pr
2prB = m0NI
B
S
Iencl
Iencl = NI.
2prB.
AB
S # dl
S =
length of the toroid and that 
is the number of turns per unit
length n, the field may be written as 
, just as it is at the
center of a long, straight solenoid.
In a real toroidal solenoid the turns are not precisely circular
loops but rather segments of a bent helix. As a result, the external
field is not exactly zero. To estimate its magnitude, we imagine
Fig. 28.25a as being very roughly equivalent, for points outside the
torus, to a single-turn circular loop with radius r. At the center of
such a loop, Eq. (28.17) gives 
this is smaller than the
field inside the solenoid by the factor 
The equations we have derived for the field in a closely wound
straight or toroidal solenoid are strictly correct only for windings
in vacuum. For most practical purposes, however, they can be used
for windings in air or on a core of any nonmagnetic, nonsupercon-
ducting material. In the next section we will show how these equa-
tions are modified if the core is a magnetic material.
N>p.
B = m0I>2r;
B = m0nI
N>2pr
Test Your Understanding of Section 28.7
Consider a conducting wire that
runs along the central axis of a hollow conducting cylinder. Such an arrangement, called a
coaxial cable, has many applications in telecommunications. (The cable that connects a
television set to a local cable provider is an example of a coaxial cable.) In such a cable 
a current I runs in one direction along the hollow conducting cylinder and is spread uni-
formly over the cylinder’s cross-sectional area. An equal current runs in the opposite
direction along the central wire. How does the magnitude B of the magnetic field 
outside such a cable depend on the distance r from the central axis of the cable? (i) B is
proportional to 
(ii) B is proportional to 
(iii) B is zero at all points outside the
cable.
❙
1>r 2;
1>r;
Hollow conducting cylinder
Central wire
Insulator
r
I
I
I
2e
A
L
m
S
v
S
S
28.26 An electron moving with speed 
in a circular orbit of radius r has an angu-
lar momentum 
and an oppositely
directed orbital magnetic dipole moment
It also has a spin angular momentum
and an oppositely directed spin magnetic
dipole moment.
M
S.
L
S
v

associated with the electron, we note that the orbital period T (the time for the
electron to make one complete orbit) is the orbit circumference divided by the
electron speed: 
The equivalent current I is the total charge passing
any point on the orbit per unit time, which is just the magnitude e of the electron
charge divided by the orbital period T:
The magnetic moment 
is then
(28.25)
It is useful to express 
in terms of the angular momentum L of the electron. For
a particle moving in a circular path, the magnitude of angular momentum equals
the magnitude of momentum 
multiplied by the radius r-that is, 
(see Section 10.5). Comparing this with Eq. (28.25), we can write
(28.26)
Equation (28.26) is useful in this discussion because atomic angular momen-
tum is quantized; its component in a particular direction is always an integer
multiple of 
where h is a fundamental physical constant called Planck’s
constant. The numerical value of h is
The quantity 
thus represents a fundamental unit of angular momentum in
atomic systems, just as e is a fundamental unit of charge. Associated with the
quantization of 
is a fundamental uncertainty in the direction of 
and therefore
of 
In the following discussion, when we speak of the magnitude of a magnetic
moment, a more precise statement would be “maximum component in a given
direction.” Thus, to say that a magnetic moment 
is aligned with a magnetic
field 
really means that 
has its maximum possible component in the direction
of 
such components are always quantized.
Equation (28.26) shows that associated with the fundamental unit of angular
momentum is a corresponding fundamental unit of magnetic moment. If 
then
(28.27)
This quantity is called the Bohr magneton, denoted by 
Its numerical value is
You should verify that these two sets of units are consistent. The second set is
useful when we compute the potential energy 
for a magnetic
moment in a magnetic field.
Electrons also have an intrinsic angular momentum, called spin, that is not
related to orbital motion but that can be pictured in a classical model as spinning
on an axis. This angular momentum also has an associated magnetic moment,
and its magnitude turns out to be almost exactly one Bohr magneton. (Effects
having to do with quantization of the electromagnetic field cause the spin mag-
netic moment to be about 
Paramagnetism
In an atom, most of the various orbital and spin magnetic moments of the elec-
trons add up to zero. However, in some cases the atom has a net magnetic
moment that is of the order of 
When such a material is placed in a magnetic
mB.
1.001 mB.)
U = -M
S # B
S
mB = 9.274 * 10-24 A # m2 = 9.274 * 10-24 J>T
mB.
m =
e
2m a h
2p b =
eh
4pm
h>2p,
L =
B
S;
M
S
B
S
M
S
M
S.
L
S
L
S
h>2p
h = 6.626 * 10-34 J # s
h>2p,
m =
e
2m L
L = mvr
mv
m
m =
ev
2pr 1pr 22 = evr
2
m = IA
I = e
T =
ev
2pr
T = 2pr>v.
942
CHAPTER 28 Sources of Magnetic Field

28.8 Magnetic Materials
943
field, the field exerts a torque on each magnetic moment, as given by Eq. (27.26):
These torques tend to align the magnetic moments with the field, as
we discussed in Section 27.7. In this position, the directions of the current loops
are such as to add to the externally applied magnetic field.
We saw in Section 28.5 that the
field produced by a current loop is propor-
tional to the loop’s magnetic dipole moment. In the same way, the additional 
field produced by microscopic electron current loops is proportional to the total
magnetic moment 
per unit volume V in the material. We call this vector
quantity the magnetization of the material, denoted by 
(28.28)
The additional magnetic field due to magnetization of the material turns out to
be equal simply to 
where 
is the same constant that appears in the law of
Biot and Savart and Ampere’s law. When such a material completely surrounds a
current-carrying conductor, the total magnetic field 
in the material is
(28.29)
where 
is the field caused by the current in the conductor.
To check that the units in Eq. (28.29) are consistent, note that magnetization
is magnetic moment per unit volume. The units of magnetic moment are cur-
rent times area 
so the units of magnetization are 
From Section 28.1, the units of the constant 
are 
So the units of 
are the same as the units of 
A material showing the behavior just described is said to be paramagnetic.
The result is that the magnetic field at any point in such a material is greater by a
dimensionless factor 
called the relative permeability of the material, than it
would be if the material were replaced by vacuum. The value of 
is different
for different materials; for common paramagnetic solids and liquids at room tem-
perature, 
typically ranges from 1.00001 to 1.003.
All of the equations in this chapter that relate magnetic fields to their sources
can be adapted to the situation in which the current-carrying conductor is embed-
ded in a paramagnetic material. All that need be done is to replace 
by 
This product is usually denoted as 
and is called the permeability of the
material:
(28.30)
CAUTION
Two meanings of the symbol 
Equation (28.30) involves some really dan-
gerous notation because we have also used 
for magnetic dipole moment. It’s customary
to use 
for both quantities, but beware: From now on, every time you see a 
make sure
you know whether it is permeability or magnetic moment. You can usually tell from the
context. ❙
The amount by which the relative permeability differs from unity is called the
magnetic susceptibility, denoted by 
(28.31)
Both 
and 
are dimensionless quantities. Table 28.1 lists values of magnetic
susceptibility for several materials. For example, for aluminum, 
and 
The first group of materials in the table are paramagnetic;
we’ll discuss the second group of materials, which are called diamagnetic, very
shortly.
The tendency of atomic magnetic moments to align themselves parallel to
the magnetic field (where the potential energy is minimum) is opposed by ran-
dom thermal motion, which tends to randomize their orientations. For this rea-
son, paramagnetic susceptibility always decreases with increasing temperature.
Km = 1.000022.
xm = 2.2 * 10-5
xm
Km
xm = Km - 1
xm:
m,
m
m
M
m = Kmm0
m
Kmm0.
m0
Km
Km
Km,
1T # m>A21A>m2 = T.
B
S:
m0M
S
T # m>A.
m0
1A # m22>m3 = A>m.
1A # m22,
M
S
B
S
0
B
S  B
S
0  m0M
S
B
S
m0
m0M
S ,
M
S  M
S
total
V
M
S :
M
S
total
B
S
B
S
T
S  M
S : B
S.
Table 28.1 Magnetic
Susceptibilities of Paramagnetic
and Diamagnetic Materials at
Material
Paramagnetic
Iron ammonium alum
66
Uranium
40
Platinum
26
Aluminum
2.2
Sodium
0.72
Oxygen gas
0.19
Diamagnetic
Bismuth
16.6
Mercury
2.9
Silver
2.6
Carbon (diamond)
2.1
Lead
1.8
Sodium chloride
1.4
Copper
1.0
-
-
-
-
-
-
-
Xm  Km  1 1* 10-52
T  20°C

In many cases it is inversely proportional to the absolute temperature T, and the
magnetization M can be expressed as
(28.32)
This relationship is called Curie’s law, after its discoverer, Pierre Curie
(1859-1906). The quantity C is a constant, different for different materials, called
the Curie constant.
As we described in Section 27.7, a body with atomic magnetic dipoles is
attracted to the poles of a magnet. In most paramagnetic substances this attraction
is very weak due to thermal randomization of the atomic magnetic moments. But
at very low temperatures the thermal effects are reduced, the magnetization
increases in accordance with Curie’s law, and the attractive forces are greater.
M = C B
T
944
CHAPTER 28 Sources of Magnetic Field
