28.8 Magnetic Materials

941

solenoid is conﬁned to the space enclosed by the windings. We can
think of such a solenoid as a tightly wound, straight solenoid that
has been bent into a circle.
For path 2, we have

Each turn of the wind-
ing  passes  once through  the  area  bounded  by  this  path,  so
Iencl = NI.
is positive for the clockwise direction
We note that
is  in  the  direction  shown.
of  integration  in  Fig.  28.25b,  so
Ampere’s law then says that

S
B
2prB = m0NI

S # d l
AB

2prB.

Iencl

, so

=

S

B =

m0NI
2pr

(toroidal solenoid)

(28.24)

EVALUATE:  Equation (28.24) indicates that B is not uniform over
the interior of the core, because different points in the interior are
difference distances r from the toroid axis. However, if the radial
extent  of  the  core  is  small  in  comparison  to  r,  the  variation  is
is  the  circumferential
slight.  In  that  case,  considering  that

2pr

length of the toroid and that
length n, the ﬁeld may be written as
center of a long, straight solenoid.

N>2pr

is the number of turns per unit
B = m0nI
, just as it is at the

In  a  real  toroidal  solenoid  the  turns  are  not  precisely  circular
loops but rather segments of a bent helix. As a result, the external
ﬁeld  is  not  exactly  zero.  To  estimate  its  magnitude,  we  imagine
Fig. 28.25a as being very roughly equivalent, for points outside the
torus, to a single-turn circular loop with radius r. At the center of
such a loop, Eq. (28.17) gives
this is smaller than the
ﬁeld inside the solenoid by the factor

B = m0I>2r;
N>p.

The equations we have derived for the ﬁeld in a closely wound
straight or toroidal solenoid are strictly correct only for windings
in vacuum. For most practical purposes, however, they can be used
for windings in air or on a core of any nonmagnetic, nonsupercon-
ducting material. In the next section we will show how these equa-
tions are modiﬁed if the core is a magnetic material.

Test Your Understanding of Section 28.7 Consider a conducting wire that
runs along the central axis of a hollow conducting cylinder. Such an arrangement, called a
coaxial cable, has many applications in telecommunications. (The cable that connects a
television set to a local cable provider is an example of a coaxial cable.) In such a cable
a current I runs in one direction along the hollow conducting cylinder and is spread uni-
formly over the cylinder’s cross-sectional area. An equal current runs in the opposite
direction along the central wire. How does the magnitude B of the magnetic ﬁeld
outside such a cable depend on the distance r from the central axis of the cable? (i) B is
proportional to
(iii) B is zero at all points outside the
cable.

(ii) B is proportional to

1>r 2;

1>r ;

❙

Hollow conducting cylinder

Insulator

Central wire

28.8 Magnetic Materials

In discussing how currents cause magnetic ﬁelds, we have assumed that the con-
ductors are surrounded by vacuum. But the coils in transformers, motors, genera-
tors, and electromagnets nearly always have iron cores to increase the magnetic
ﬁeld and conﬁne it to desired regions. Permanent magnets, magnetic recording
tapes, and computer disks depend directly on the magnetic properties of materi-
als; when you store information on a computer disk, you are actually setting up
an array of microscopic permanent magnets on the disk. So it is worthwhile to
examine some aspects of the magnetic properties of materials. After describing
the atomic origins of magnetic properties, we will discuss three broad classes of
magnetic behavior that occur in materials; these are called paramagnetism, dia-
magnetism, and ferromagnetism.

The Bohr Magneton
As we discussed brieﬂy in Section 27.7, the atoms that make up all matter con-
tain  moving  electrons,  and  these  electrons  form  microscopic  current  loops  that
produce magnetic ﬁelds of their own. In many materials these currents are ran-
domly oriented and cause no net magnetic ﬁeld. But in some materials an exter-
nal ﬁeld (a ﬁeld produced by currents outside the material) can cause these loops
to become oriented preferentially with the ﬁeld, so their magnetic ﬁelds add to
the external ﬁeld. We then say that the material is magnetized.

-e)

Let’s look at how these microscopic currents come about. Figure 28.26 shows
a  primitive  model  of  an  electron  in  an  atom. We  picture  the  electron  (mass  m,
charge
as moving in a circular orbit with radius r and speed  This moving
charge  is  equivalent  to  a  current  loop.  In  Section  27.7  we  found  that  a  current
m
m = IA;
loop with area A and current I has a magnetic dipole moment  given by
To  ﬁnd  the  current
for  the  orbiting  electron  the  area  of  the  loop  is

A = pr 2.

v.

S
L

v
28.26 An electron moving with speed
in a circular orbit of radius r has an angu-
lar momentum  and an oppositely
directed orbital magnetic dipole moment
MS
It also has a spin angular momentum
and an oppositely directed spin magnetic
dipole moment.

.

S
L

mS

I

2e

r

S
v

I

A

I

942

CHAPTER 28 Sources of Magnetic Field

associated with the electron, we note that the orbital period T (the time for the
electron to make one complete orbit) is the orbit circumference divided by the
electron speed:
The equivalent current I is the total charge passing
any point on the orbit per unit time, which is just the magnitude e of the electron
charge divided by the orbital period T:

T = 2pr>v.

I = e
T

= ev
2pr

The magnetic moment

m = IA

is then

m = ev
2pr

1pr 22 = evr
2

(28.25)

m

It is useful to express
in terms of the angular momentum L of the electron. For
a particle moving in a circular path, the magnitude of angular momentum equals
L = mvr
mv
the  magnitude  of  momentum
(see Section 10.5). Comparing this with Eq. (28.25), we can write

multiplied  by  the  radius  r—that  is,

m = e
2m

L

(28.26)

Equation (28.26) is useful in this discussion because atomic angular momen-
tum  is  quantized; its  component  in  a  particular  direction  is  always  an  integer
multiple  of
where  h is  a  fundamental  physical  constant  called  Planck’s
constant. The numerical value of h is

h>2p,

h = 6.626 * 10-34 J # s

h>2p

.

MS

S
L

The quantity
thus represents a fundamental unit of angular momentum in
atomic  systems,  just  as  e is  a  fundamental  unit  of  charge. Associated  with  the
quantization of
and therefore
is a fundamental uncertainty in the direction of
of
In the following discussion, when we speak of the magnitude of a magnetic
moment,  a  more  precise  statement  would  be  “maximum  component  in  a  given
is  aligned  with  a  magnetic
direction.” Thus,  to  say  that  a  magnetic  moment
S
MS
B
ﬁeld
has its maximum possible component in the direction
S
such components are always quantized.
;
B
of
Equation (28.26) shows that associated with the fundamental unit of angular
L =

momentum  is  a  corresponding  fundamental  unit  of  magnetic  moment.  If
h>2p,

really means that

then

S
L

MS

m = e
2m

a h
2p

b = eh
4pm

(28.27)

This quantity is called the Bohr magneton, denoted by

Its numerical value is

mB.

mB = 9.274 * 10-24 A # m2 = 9.274 * 10-24 J>T

You should verify that these two sets of units are consistent. The second set is
for  a  magnetic
useful  when  we  compute  the  potential  energy
moment in a magnetic ﬁeld.

U = - MS # B

S

Electrons  also  have  an  intrinsic  angular  momentum,  called  spin, that  is  not
related to orbital motion but that can be pictured in a classical model as spinning
on  an  axis.  This  angular  momentum  also  has  an  associated  magnetic  moment,
and  its  magnitude  turns  out  to  be  almost  exactly  one  Bohr  magneton.  (Effects
having to do with quantization of the electromagnetic ﬁeld cause the spin mag-
netic moment to be about

1.001 mB.)

Paramagnetism
In an atom, most of the various orbital and spin magnetic moments of the elec-
trons  add  up  to  zero.  However,  in  some  cases  the  atom  has  a  net  magnetic
moment that is of the order of  When such a material is placed in a magnetic

mB.

S

ﬁeld, the ﬁeld exerts a torque on each magnetic moment, as given by Eq. (27.26):
TS (cid:2) MS : B
.
These torques tend to align the magnetic moments with the ﬁeld, as
we discussed in Section 27.7. In this position, the directions of the current loops
are such as to add to the externally applied magnetic ﬁeld.

We saw in Section 28.5 that the

ﬁeld produced by a current loop is propor-
S
B
tional to the loop’s magnetic dipole moment. In the same way, the additional
ﬁeld produced by microscopic electron current loops is proportional to the total
magnetic  moment
per  unit  volume  V in  the  material. We  call  this  vector
quantity the magnetization of the material, denoted by

S
:
M

total

MS

S
B

S
M

(cid:2)

MS

total
V

(28.28)

The additional magnetic ﬁeld due to magnetization of the material turns out to
be equal simply to
is the same constant that appears in the law of
Biot and Savart and Ampere’s law. When such a material completely surrounds a
current-carrying conductor, the total magnetic ﬁeld

in the material is

m0 M
,

where

m0

S
B

S

S
B

S

(cid:2) B

S

0 (cid:3) m0M

(28.29)

where

S
B

0

is the ﬁeld caused by the current in the conductor.

S
M
1A # m22,
rent times area
From Section 28.1, the units of the constant
are the same as the units of

To check that the units in Eq. (28.29) are consistent, note that magnetization
is magnetic moment per unit volume. The units of magnetic moment are cur-
1A # m22>m3 = A>m.
so the units of magnetization are
T # m>A.
m0M
So the units of
1T # m>A21A>m2 = T.
A material showing the behavior just described is said to be paramagnetic.
The result is that the magnetic ﬁeld at any point in such a material is greater by a
called the relative permeability of the material, than it
dimensionless factor
would be if the material were replaced by vacuum. The value of
is different
for different materials; for common paramagnetic solids and liquids at room tem-
perature,

typically ranges from 1.00001 to 1.003.

Km,

Km

are

S
:
B

m0

S

Km

All of the equations in this chapter that relate magnetic ﬁelds to their sources
can be adapted to the situation in which the current-carrying conductor is embed-
Kmm0.
ded in a paramagnetic material. All that need be done is to replace
This  product  is  usually  denoted  as
and  is  called  the  permeability of  the
material:

m0

by

m

m = Kmm0

(28.30)

M
CAUTION Two meanings of the symbol
Equation (28.30) involves some really dan-
m
gerous notation because we have also used
for magnetic dipole moment. It’s customary
to use
for both quantities, but beware: From now on, every time you see a  make sure
you know whether it is permeability or magnetic moment. You can usually tell from the
context. ❙

m,

m

The amount by which the relative permeability differs from unity is called the

magnetic susceptibility, denoted by

xm:
xm = Km - 1

(28.31)

xm

Km

and

are dimensionless quantities. Table 28.1 lists values of magnetic
Both
xm = 2.2 * 10-5
susceptibility for several materials. For example, for aluminum,
The ﬁrst group of materials in the table are paramagnetic;
and
we’ll discuss the second group of materials, which are called diamagnetic, very
shortly.

Km = 1.000022.

The  tendency  of  atomic  magnetic  moments  to  align  themselves  parallel  to
the magnetic field (where the potential energy is minimum) is opposed by ran-
dom thermal motion, which tends to randomize their orientations. For this rea-
son, paramagnetic susceptibility always decreases with increasing temperature.

28.8 Magnetic Materials

943

Table 28.1 Magnetic
Susceptibilities of Paramagnetic
and Diamagnetic Materials at
T (cid:2) 20°C

Material

Paramagnetic

Xm (cid:2) Km (cid:4) 1 1 * 10-52

Iron ammonium alum

Uranium

Platinum

Aluminum

Sodium

Oxygen gas

Diamagnetic

Bismuth

Mercury

Silver

Carbon (diamond)

Lead

Sodium chloride

Copper

66

40

26

2.2

0.72

0.19

-

16.6

-

-

-

-

-

2.9

2.6

2.1

1.8

1.4

1.0-

944

CHAPTER 28 Sources of Magnetic Field

In many cases it is inversely proportional to the absolute temperature T, and the
magnetization M can be expressed as

M = C

B
T

(28.32)

This  relationship  is  called  Curie’s  law, after  its  discoverer,  Pierre  Curie
(1859–1906). The quantity C is a constant, different for different materials, called
the Curie constant.

As  we  described  in  Section  27.7,  a  body  with  atomic  magnetic  dipoles  is
attracted to the poles of a magnet. In most paramagnetic substances this attraction
is very weak due to thermal randomization of the atomic magnetic moments. But
at  very  low  temperatures  the  thermal  effects  are  reduced,  the  magnetization
increases in accordance with Curie’s law, and the attractive forces are greater.

Example 28.11 Magnetic dipoles in a paramagnetic material

1NO2

Nitric  oxide
is  a  paramagnetic  compound.  The  magnetic
moment of each NO molecule has a maximum component in any
direction  of  about  one  Bohr  magneton.  Compare  the  interaction
energy of such magnetic moments in a 1.5-T magnetic ﬁeld with
the average translational kinetic energy of molecules at 300 K.

SOLUTION

IDENTIFY  and SET  UP:  This  problem  involves  the  energy  of  a
magnetic  moment  in  a  magnetic  ﬁeld  and  the  average  thermal
U = - MS # B
, for the interac-
kinetic energy. We have Eq. (27.27),
S
MS
with  a
tion  energy  of  a  magnetic  moment
ﬁeld,  and  Eq.
B
(18.16),
for the average translational kinetic energy of a
molecule at temperature T.

K = 3

2 kT,

S

ƒUƒ max L mBB = 19.27 * 10-24 J>T211.5 T2

= 1.4 * 10-23 J = 8.7 * 10-5 eV

The average translational kinetic energy K is
2 kT = 3

11.38 * 10-23 J>K21300 K2

K = 3

2

= 6.2 * 10-21 J = 0.039 eV

EVALUATE: At 300 K the magnetic interaction energy is only about
0.2%  of  the  thermal  kinetic  energy,  so  we  expect  only  a  slight
degree of alignment. This is why paramagnetic susceptibilities at
ordinary temperature are usually very small.

U = - mŒB,
EXECUTE: We can write
MS
the  magnetic  moment
mŒ
is about
maximum value of

in  the  direction  of  the
so

where

mŒ

mB,

is the component of
ﬁeld.  Here  the

S
B

Diamagnetism
In some materials the total magnetic moment of all the atomic current loops is
zero when no magnetic ﬁeld is present. But even these materials have magnetic
effects because an external ﬁeld alters electron motions within the atoms, causing
additional current loops and induced magnetic dipoles comparable to the induced
electric dipoles we studied in Section 28.5. In this case the additional ﬁeld caused
by these current loops is always opposite in direction to that of the external ﬁeld.
(This behavior is explained by Faraday’s law of induction, which we will study in
Chapter  29.  An  induced  current  always  tends  to  cancel  the  ﬁeld  change  that
caused it.)

Such materials are said to be diamagnetic. They always have negative sus-
slightly less than
ceptibility, as shown in Table 28.1, and relative permeability
unity, typically of the order of 0.99990 to 0.99999 for solids and liquids. Diamag-
netic susceptibilities are very nearly temperature independent.

Km

Ferromagnetism
There is a third class of materials, called ferromagnetic materials, that includes
iron, nickel, cobalt, and many alloys containing these elements. In these materials,
strong interactions between atomic magnetic moments cause them to line up par-
allel to each other in regions called  magnetic domains, even when no external

ﬁeld  is  present.  Figure  28.27 shows  an  example  of  magnetic  domain  structure.
Within each domain, nearly all of the atomic magnetic moments are parallel.

0

S
B

When there is no externally applied ﬁeld, the domain magnetizations are ran-
domly oriented. But when a ﬁeld
(caused by external currents) is present, the
domains tend to orient themselves parallel to the ﬁeld. The domain boundaries
also shift; the domains that are magnetized in the ﬁeld direction grow, and those
that  are  magnetized  in  other  directions  shrink.  Because  the  total  magnetic
moment  of  a  domain  may  be  many  thousands  of  Bohr  magnetons,  the  torques
that tend to align the domains with an external ﬁeld are much stronger than occur
with  paramagnetic  materials. The  relative  permeability
is  much larger  than
unity, typically of the order of 1000 to 100,000. As a result, an object made of a
ferromagnetic  material  such  as  iron  is  strongly  magnetized  by  the  ﬁeld  from  a
permanent magnet and is attracted to the magnet (see Fig. 27.38). A paramagnetic
material such as aluminum is also attracted to a permanent magnet, but
for
paramagnetic materials is so much smaller for such a material than for ferromag-
netic materials that the attraction is very weak. Thus a magnet can pick up iron
nails, but not aluminum cans.

Km

Km

28.8 Magnetic Materials

945

28.27 In this drawing adapted from a
magniﬁed photo, the arrows show the
directions of magnetization in the domains
of a single crystal of nickel. Domains that
are magnetized in the direction of an
applied magnetic ﬁeld grow larger.

(a) No field

(b) Weak field

As the external ﬁeld is increased, a point is eventually reached at which nearly
all the magnetic moments in the ferromagnetic material are aligned parallel to the
external  ﬁeld.  This  condition  is  called  saturation  magnetization; after  it  is
reached, further increase in the external ﬁeld causes no increase in magnetization
or in the additional ﬁeld caused by the magnetization.

S
B

(c) Stronger field

B0

B0,

Km

Figure 28.28 shows a “magnetization curve,” a graph of magnetization M as a
for soft iron. An alternative description of
function of external magnetic ﬁeld
this behavior is that
increases. (Paramag-
is not constant but decreases as
netic materials also show saturation at sufﬁciently strong ﬁelds. But the magnetic
ﬁelds required are so large that departures from a linear relationship between M and
B0
in these materials can be observed only at very low temperatures, 1 K or so.)
For many ferromagnetic materials the relationship of magnetization to exter-
nal magnetic ﬁeld is different when the external ﬁeld is increasing from when it is
decreasing. Figure 28.29a shows this relationship for such a material. When the
material is magnetized to saturation and then the external ﬁeld is reduced to zero,
some magnetization remains. This behavior is characteristic of permanent mag-
nets, which retain most of their saturation magnetization when the magnetizing
ﬁeld is removed. To reduce the magnetization to zero requires a magnetic ﬁeld in
the reverse direction.

This  behavior  is  called  hysteresis, and  the  curves  in  Fig.  28.29 are  called
hysteresis  loops. Magnetizing  and  demagnetizing  a  material  that  has  hysteresis
involve the dissipation of energy, and the temperature of the material increases
during such a process.

S
B

28.28 A magnetization curve for a fer-
romagnetic material. The magnetization M
approaches its saturation value
as the
B0
magnetic ﬁeld
(caused by external cur-
rents) becomes large.

Msat

M

Msat

O

B0

28.29 Hysteresis loops. The materials of both (a) and (b) remain strongly magnetized when
hard to demagnetize, it would be good for permanent magnets. Since (b) magnetizes and demagnetizes more easily, it could be used as a
computer memory material. The material of (c) would be useful for transformers and other alternating-current devices where zero
hysteresis would be optimal.

is reduced to zero. Since (a) is also

B0

(a)

3

A large external field in the
opposite direction is needed to
reduce the magnetization to zero.

Magnetization
M

2

External field is reduced to
zero; magnetization remains.

(b)

M

1

Material is magnetized
to saturation by an external field.

4

Further increasing the
reversed external field gives
the material a magnetization
in the reverse direction.

5

This magnetization remains if
the external field is reduced to zero.

Applied external
field B0

6

Increasing the external field
in the original direction
again reduces the
magnetization to zero.

(c)

M

These materials can
be magnetized to
saturation and
demagnetized by
smaller external
fields than in (a).

B0

B0

946

CHAPTER 28 Sources of Magnetic Field

Application Magnetic Nanoparticles
for Cancer Therapy
The violet blobs in this microscope image are
cancer cells that have broken away from a
tumor and threaten to spread throughout a
patient’s body. An experimental technique for
ﬁghting these cells uses particles of a mag-
netic material (shown in brown) injected into
the body. These particles are coated with a
chemical that preferentially attaches to cancer
cells. A magnet outside the patient is then
used to “steer” the particles out of the body,
taking the cancer cells with them. (Photo
courtesy of cancer researcher Dr. Kenneth
Scarberry.)

Ferromagnetic materials are widely used in electromagnets, transformer cores,
and motors and generators, in which it is desirable to have as large a magnetic
ﬁeld as possible for a given current. Because hysteresis dissipates energy, materi-
als that are used in these applications should usually have as narrow a hysteresis
loop as possible. Soft iron is often used; it has high permeability without appre-
ciable hysteresis. For permanent magnets a broad hysteresis loop is usually desir-
able,  with  large  zero-ﬁeld  magnetization  and  large  reverse  ﬁeld  needed  to
demagnetize.  Many  kinds  of  steel  and  many  alloys,  such  as Alnico,  are  com-
monly  used  for  permanent  magnets.  The  remaining  magnetic  ﬁeld  in  such  a
material, after it has been magnetized to near saturation, is typically of the order
of  about
of  1  T,  corresponding  to  a  remaining  magnetization
800,000 A>m.

M = B>m0

Example 28.12

A ferromagnetic material

A cube-shaped  permanent  magnet  is  made  of  a  ferromagnetic
The side
material with a magnetization M of about
length is 2 cm. (a) Find the magnetic dipole moment of the magnet.
(b) Estimate the magnetic ﬁeld due to the magnet at a point 10 cm
from the magnet along its axis.

8 * 105 A>m.

SOLUTION

IDENTIFY and SET UP: This problem uses the relationship between
and  the  idea
magnetization M and  magnetic  dipole  moment
mtotal
that a magnetic dipole produces a magnetic ﬁeld. We ﬁnd
using
Eq. (28.28). To estimate the ﬁeld, we approximate the magnet as a
current loop with this same magnetic moment and use Eq. (28.18).

mtotal

EXECUTE: (a) From Eq. (28.28),

mtotal = MV = 18 * 105 A>m212 * 10-2 m23 = 6 A # m2

loop with magnetic moment

(b) From Eq. (28.18), the magnetic ﬁeld on the axis of a current
is
m0mtotal
2p1x 2 + a223>2

mtotal

B =

where x is the distance from the loop and a is its radius. We can use
this expression here if we take a to refer to the size of the perma-
nent magnet. Strictly speaking, there are complications because our
magnet does not have the same geometry as a circular current loop.
is  fairly  large  in  comparison  to  the  2-cm
But  because
x 2
size of the magnet, the term
and can be ignored. So

is negligible in comparison to

x = 10 cm

a2

B L

m0mtotal
2px 3

=

14p * 10-7 T # m>A216 A # m22
2p10.1 m23

= 1 * 10-3 T = 10 G

which is about ten times stronger than the earth’s magnetic ﬁeld.

EVALUATE:  We calculated B at a point outside the magnetic mate-
of the magnetic
rial and therefore used
m
material, in our calculation. You would substitute permeability
m0
if you were calculating B inside a material with relative per-
for
meability

not the permeability

for which m = Kmm0.

Km,

m0,

m

Test Your Understanding of Section 28.8 Which of the following materials
are attracted to a magnet? (i) sodium; (ii) bismuth; (iii) lead; (iv) uranium.

❙
