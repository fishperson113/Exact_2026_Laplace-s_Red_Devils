980

CHAPTE R  33 E LECTROMAG N ETIC WAVES

:
B

through the rectangle of Fig. 33-6 is shown at a different instant

Checkpoint 1
The magnetic field
is directed in the xz plane, parallel to the z axis, and its
in part 1 of the figure here;
magnitude is increasing. (a) Complete part 1 by drawing the induced electric fields,
indicating both directions and relative magnitudes (as in Fig. 33-6). (b) For the same
instant, complete part 2 of the figure by drawing the electric field of the electromag-
netic wave. Also draw the induced magnetic fields, indicating both directions and
relative magnitudes (as in Fig. 33-7).

:
B

y

y

B

x

x

z

z

(1)

(2)

33-2 ENERGY TRANSPORT AND THE POYNTING VECTOR

Learning Objectives
After reading this module, you should be able to . . .

33.13 Identify that an electromagnetic wave transports

33.18 Identify an EM wave’s intensity I in terms of energy

energy.

transport.

33.14 For a target, identify that an EM wave’s rate of energy
transport per unit area is given by the Poynting vector
which is related to the cross product of the electric field
:
E

and magnetic field

:
B
.

:
S
,

33.15 Determine the direction of travel (and thus energy
transport) of an electromagnetic wave by applying
the cross product for the corresponding Poynting
vector.

33.16 Calculate the instantaneous rate S of energy flow of
an EM wave in terms of the instantaneous electric field
magnitude E.

33.17 For the electric field component of an electromag-

netic wave, relate the rms value Erms to the amplitude Em.

33.19 Apply the relationships between an EM wave’s

intensity I and the electric field’s rms value Erms and ampli-
tude Em.

33.20 Apply the relationship between average power Pavg,

energy transfer )E, and the time )t taken by that transfer,
and apply the relationship between the instantaneous
power P and the rate of energy transfer dE/dt.

33.21 Identify an isotropic point source of light.
33.22 For an isotropic point source of light, apply the relation-
ship between the emission power P, the distance r to a
point of measurement, and the intensity I at that point.
33.23 In terms of energy conservation, explain why the intensity
from an isotropic point source of light decreases as 1/r2.

Key Ideas
● The rate per unit area at which energy is transported
via an electromagnetic wave is given by the Poynting
vector

:
S
:

the wave:

I !

1
cm0

2
E rms

,

:
S

!

1
m0

:
E

:
& B
.

:
S

The direction of
energy transport) is perpendicular to the directions of both
:
E

(and thus of the wave’s travel and the

and

:
B
.

in which

Erms ! Em/

 2
.

1

● A point source of electromagnetic waves emits the waves
isotropically—that is, with equal intensity in all directions. The
intensity of the waves at distance r from a point source of
power Ps is

● The time-averaged rate per unit area at which energy
is transported is Savg, which is called the intensity I of

I !

Ps
4pr2  .

33-2 E N E RGY  TRANSPORT  AN D  TH E  POYNTI NG  VECTOR

981

Energy Transport and the Poynting Vector
All  sunbathers  know  that  an  electromagnetic  wave  can  transport  energy  and
deliver it to a body on which the wave falls. The rate of energy transport per unit
area in such a wave is described by a vector
, called the Poynting vector after
physicist  John  Henry  Poynting  (1852 – 1914), who  first  discussed  its  properties.
This vector is defined as

:
S

:
S

!

1
m0

:
E

:
& B

(Poynting vector).

(33-19)

Its magnitude S is related to the rate at which energy is transported by a wave
across a unit area at any instant (inst):

S ! # energy/time

area

$inst

! # power

area $inst

.

(33-20)

From this we can see that the SI unit for

:
S

is the watt per square meter (W/m2).

:
S
The direction of the Poynting vector  of an electromagnetic wave at any
point gives the wave’s direction of travel and the direction of energy transport
at that point.

Because

:
B
wave, the magnitude of

and

:
E

are  perpendicular  to  each  other  in  an  electromagnetic
:
E

is EB. Then the magnitude of

:
& B

:
S

is

S !

1
m0

EB,

(33-21)

in which S, E, and B are instantaneous values. The magnitudes E and B are so
closely  coupled  to  each  other  that  we  need  to  deal  with  only  one  of  them; we
choose E, largely because most instruments for detecting electromagnetic waves
deal with the electric component of the wave rather than the magnetic compo-
nent. Using B ! E/c from Eq. 33-5, we can rewrite Eq. 33-21 in terms of just the
electric component as

S !

1
cm0

E 2

(instantaneous energy flow rate).

(33-22)

Intensity. By substituting E ! Em sin(kx ’ vt) into Eq. 33-22, we could ob-
tain an equation for the energy transport rate as a function of time. More useful
in  practice, however, is  the  average  energy  transported  over  time; for  that,
we need  to  find  the  time-averaged  value  of  S, written  Savg and  also  called  the
intensity I of the wave. Thus from Eq. 33-20, the intensity I is

I ! Savg ! # energy/time

area

$avg

! # power

area $avg

.

(33-23)

From Eq. 33-22, we find

I ! Savg !

1
cm0

 [E 2]avg !

1
cm0

 [E 2

m sin2(kx ’ vt)]avg.

(33-24)

Over a full cycle, the average value of sin2 u, for any angular variable u, is  (see
Fig. 31-17). In  addition, we  define  a  new  quantity  Erms, the  root-mean-square
value of the electric field, as

1
2

Erms !

 .

Em
2
1

(33-25)

982

CHAPTE R  33 E LECTROMAG N ETIC WAVES

The energy emitted by light
source S must pass through
the sphere of radius r.

We can then rewrite Eq. 33-24 as

I !

1
cm0

E 2

rms

.

(33-26)

r

S

Figure 33-8 A point source S emits electro-
magnetic waves uniformly in all directions.
The spherical wavefronts pass through an
imaginary sphere of radius r that is
centered on S.

Because E ! cB and c is such a very large number, you might conclude that
the energy associated with the electric field is much greater than that associated
with the magnetic field. That conclusion is incorrect; the two energies are exactly
equal. To  show  this, we  start  with  Eq. 25-25, which  gives  the  energy  density
u ( ! 1

within an electric field, and substitute cB for E; then we can write

2´0E 2)

uE ! 1

2´0E 2 ! 1

2´0(cB)2.

If we now substitute for c with Eq. 33-3, we get

uE ! 1

2´0

1
m0´0

B2 !

B2
2m0

.

However, Eq. 30-55  tells  us  that  B2/2m0 is  the  energy  density  uB of  a  magnetic
; so we see that uE ! uB everywhere along an electromagnetic wave.
field

:
B

Variation of Intensity with Distance
How intensity varies with distance from a real source of electromagnetic radia-
tion  is  often  complex — especially  when  the  source  (like  a  searchlight  at  a
movie premier) beams the radiation in a particular direction. However, in some
situations  we  can  assume  that  the  source  is  a  point  source that  emits  the  light
isotropically — that is, with equal intensity in all directions. The spherical wave-
fronts spreading from such an isotropic point source S at a particular instant are
shown in cross section in Fig. 33-8.

Let us assume that the energy of the waves is conserved as they spread from this
source. Let us also center an imaginary sphere of radius r on the source, as shown in
Fig. 33-8.All the energy emitted by the source must pass through the sphere.Thus, the
rate at which energy passes through the sphere via the radiation must equal the rate
at which energy is emitted by the source—that is, the source power Ps.The intensity I
(power per unit area) measured at the sphere must then be, from Eq. 33-23,

I !

power
area

!

Ps
4pr 2 ,

(33-27)

where 4pr2 is the area of the sphere. Equation 33-27 tells us that the intensity of
the electromagnetic radiation from an isotropic point source decreases with the
square of the distance r from the source.

Checkpoint 2

The figure here gives the electric field of an electromagnetic wave at
a certain point and a certain instant. The wave is transporting energy
in the negative z direction. What is the direction of the magnetic field
of the wave at that point and instant?

y

E

z

x

Sample Problem 33.01 Light wave: rms values of the electric and magnetic fields

When  you  look  at  the  North  Star  (Polaris), you  intercept
light from a star at a distance of 431 ly and emitting energy
at  a  rate  of  2.2 & 103 times  that  of  our  Sun  (Psun ! 3.90 &

1026 W)
. Neglecting  any  atmospheric  absorption, find  the
rms  values  of  the  electric  and  magnetic  fields  when  the
starlight reaches you.
