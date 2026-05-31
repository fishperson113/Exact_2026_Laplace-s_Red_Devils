C H A

P

T

E

R

3

3

Electromagnetic Waves

33-1 ELECTROMAGNETIC WAVES

Learning Objectives
After reading this module, you should be able to . . .

33.01 In the electromagnetic spectrum, identify the relative
wavelengths (longer or shorter) of AM radio, FM radio,
television, infrared light, visible light, ultraviolet light, x rays,
and gamma rays.

33.02 Describe the transmission of an electromagnetic wave

by an LC oscillator and an antenna.

33.03 For a transmitter with an LC oscillator, apply the
relationships between the oscillator’s inductance L,
capacitance C, and angular frequency v, and the
emitted wave’s frequency f and wavelength l.

33.04 Identify the speed of an electromagnetic wave in

vacuum (and approximately in air).

wave’s frequency f, wavelength l, period T, angular
frequency v, and speed c.

33.08 Identify that an electromagnetic wave consists of an
electric component and a magnetic component that are
(a) perpendicular to the direction of travel, (b) perpendicu-
lar to each other, and (c) sinusoidal waves with the same
frequency and phase.

33.09 Apply the sinusoidal equations for the electric and

magnetic components of an EM wave, written as functions
of position and time.

33.10 Apply the relationship between the speed of light c, the

permittivity constant

´0

, and the permeability constant m0.

33.05 Identify that electromagnetic waves do not require a

33.11 For any instant and position, apply the relationship

medium and can travel through vacuum.

33.06 Apply the relationship between the speed of an

electromagnetic wave, the straight-line distance traveled
by the wave, and the time required for the travel.

33.07 Apply the relationships between an electromagnetic

between the electric field magnitude E, the magnetic field
magnitude B, and the speed of light c.

33.12 Describe the derivation of the relationship between the
speed of light c and the ratio of the electric field amplitude
E to the magnetic field amplitude B.

Key Ideas
● An electromagnetic wave consists of oscillating electric
and magnetic fields.

● The various possible frequencies of electromagnetic waves
form a spectrum, a small part of which is visible light.
● An electromagnetic wave traveling along an x axis has an
:
B
and a magnetic field  with magnitudes that
electric field
depend on x and t:

:
E

and

B ! Bm sin(kx ’ vt),
:
E

:
where Em and Bm are the amplitudes of
B
and
field induces the magnetic field and vice versa.
● The speed of any electromagnetic wave in vacuum is c,
which can be written as

. The electric

c !

E
B

!

1
m0´0

,

E ! Em sin(kx ’ vt)

where E and B are the simultaneous magnitudes of the fields.

1

What Is Physics?
The information age in which we live is based almost entirely on the physics of
electromagnetic waves. Like it or not, we are now globally connected by televi-
sion, telephones, and the web. And like it or not, we are constantly immersed in
those signals because of television, radio, and telephone transmitters.

Much  of  this  global  interconnection  of  information  processors  was  not
imagined by even the most visionary engineers of 40 years ago. The challenge for

972

33-1 E LECTROMAG N ETIC WAVES

973

today’s engineers is trying to envision what the global interconnection will be like
40 years from now. The starting point in meeting that challenge is understanding
the  basic  physics  of  electromagnetic  waves, which  come  in  so  many  different
types that they are poetically said to form Maxwell’s rainbow.

Maxwell’s Rainbow
The  crowning  achievement  of  James  Clerk  Maxwell  (see  Chapter  32)  was  to
show that a beam of light is a traveling wave of electric and magnetic fields — an
electromagnetic wave — and thus that optics, the study of visible light, is a branch
of electromagnetism. In this chapter we move from one to the other: we conclude
our  discussion  of  strictly  electrical  and  magnetic  phenomena, and  we  build  a
foundation for optics.

In Maxwell’s time (the mid 1800s), the visible, infrared, and ultraviolet forms
of light were the only electromagnetic waves known. Spurred on by Maxwell’s
work, however, Heinrich  Hertz  discovered  what  we  now  call  radio  waves  and
verified that they move through the laboratory at the same speed as visible light,
indicating that they have the same basic nature as visible light.

As Fig. 33-1 shows, we now know a wide spectrum (or range) of electromag-
netic waves: Maxwell’s rainbow. Consider the extent to which we are immersed in
electromagnetic  waves  throughout  this  spectrum. The  Sun, whose  radiations
define  the  environment  in  which  we  as  a  species  have  evolved  and  adapted, is
the dominant  source. We  are  also  crisscrossed  by  radio  and  television  signals.
Microwaves from radar systems and from telephone relay systems may reach us.
There are electromagnetic waves from lightbulbs, from the heated engine blocks
of  automobiles, from  x-ray  machines, from  lightning  flashes, and  from  buried
radioactive  materials. Beyond  this, radiation  reaches  us  from  stars  and  other
objects in our galaxy and from other galaxies. Electromagnetic waves also travel
in  the  other  direction. Television  signals, transmitted  from  Earth  since  about
1950, have now taken news about us (along with episodes of I Love Lucy, albeit
very faintly) to whatever technically sophisticated inhabitants there may be on
whatever planets may encircle the nearest 400 or so stars.

Wavelength (nm)

700

600

500

400

d
e
R

e
g
n
a
r
O

w
o

l
l
e
Y

n
e
e
r
G

e
u
B

l

t
e
l

i

o
V

Visible spectrum

Wavelength (m)

108 107 106 105 104 103 102

10

1  10–1 10–2 10–3 10–4 10–5 10–6 10–7 10–8 10–9 10–10 10–11 10–12 10–13 10–14 10–15 10–16

Long waves

Radio waves

Infrared

Ultraviolet

X rays

Gamma rays

10  102 103 104 105 106 107 108 109 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019 1020 1021 1022 1023 1024
Frequency (Hz)

Maritime and
aeronautical uses

AM
radio

104

105

106

Figure 33-1 The electromagnetic spectrum.

FM radio

Maritime,
aeronautical,
and mobile radio

TV channels

6

-

2

3
1

-

7

9
6

-

4
1

Maritime, aeronautical,
citizens band,
and mobile radio

107

108

Frequency (Hz)

109

1010

1011

974

CHAPTE R  33 E LECTROMAG N ETIC WAVES

100

y
t
i
v
i
t
i
s
n
e
s

e
v
i
t
a
l
e
R

80

60

40

20

0
400

450

500

550
650
Wavelength (nm)

600

700

Figure 33-2 The relative sensitivity of the av-
erage human eye to electromagnetic waves
at different wavelengths. This portion of the
electromagnetic spectrum to which the eye
is sensitive is called visible light.

In  the  wavelength  scale  in  Fig. 33-1  (and  similarly  the  corresponding
frequency  scale), each  scale  marker  represents  a  change  in  wavelength  (and
correspondingly  in  frequency)  by  a  factor  of  10. The  scale  is  open-ended; the
wavelengths of electromagnetic waves have no inherent upper or lower bound.

Certain regions of the electromagnetic spectrum in Fig. 33-1 are identified by
familiar labels, such as x rays and radio waves. These labels denote roughly defined
wavelength ranges within which certain kinds of sources and detectors of electro-
magnetic  waves  are  in  common  use. Other  regions  of  Fig. 33-1, such  as  those
labeled TV channels and AM radio, represent specific wavelength bands assigned
by law for certain commercial or other purposes. There are no gaps in the electro-
magnetic spectrum — and all electromagnetic waves, no matter where they lie in
the spectrum, travel through free space (vacuum) with the same speed c.

The  visible  region  of  the  spectrum  is  of  course  of  particular  interest  to  us.
Figure  33-2  shows  the  relative  sensitivity  of  the  human  eye  to  light  of  various
wavelengths. The center of the visible region is about 555 nm, which produces the
sensation that we call yellow-green.

The  limits  of  this  visible  spectrum  are  not  well  defined  because  the  eye
sensitivity curve approaches the zero-sensitivity line asymptotically at both long
and  short  wavelengths. If  we  take  the  limits, arbitrarily, as  the  wavelengths  at
which eye sensitivity has dropped to 1% of its maximum value, these limits are
about 430 and 690 nm; however, the eye can detect electromagnetic waves some-
what beyond these limits if they are intense enough.

The Traveling Electromagnetic Wave, Qualitatively
Some  electromagnetic  waves, including  x  rays, gamma  rays, and  visible  light,
are radiated (emitted)  from  sources  that  are  of  atomic  or  nuclear  size, where
quantum  physics  rules. Here  we  discuss  how  other  electromagnetic  waves  are
generated. To simplify matters, we restrict ourselves to that region of the spec-
trum  (wavelength  l % 1 m)  in  which  the  source  of  the  radiation (the  emitted
waves) is both macroscopic and of manageable dimensions.

Figure 33-3 shows, in broad outline, the generation of such waves. At its heart
is  an  LC  oscillator, which  establishes  an  angular  frequency
LC).
Charges  and  currents  in  this  circuit  vary  sinusoidally  at  this  frequency, as  de-
picted  in  Fig. 31-1. An  external  source — possibly  an  ac  generator — must  be
included  to  supply  energy  to  compensate  both  for  thermal  losses  in  the  circuit
and for energy carried away by the radiated electromagnetic wave.

v (! 1/

1

The LC oscillator of Fig. 33-3 is coupled by a transformer and a transmission
line  to  an  antenna, which  consists  essentially  of  two  thin, solid, conducting  rods.
Through  this  coupling, the  sinusoidally  varying  current  in  the  oscillator  causes
charge  to  oscillate  sinusoidally  along  the  rods  of  the  antenna  at  the
angular frequency v of the LC oscillator. The current in the rods associated with
this movement of charge also varies sinusoidally, in magnitude and direction, at an-
gular frequency v. The antenna has the effect of an electric dipole whose electric
dipole moment varies sinusoidally in magnitude and direction along the antenna.

Figure 33-3 An arrangement for generating a
traveling electromagnetic wave in the
shortwave radio region of the spectrum: an
LC oscillator produces a sinusoidal current
in the antenna, which generates the wave.
P is a distant point at which a detector can
monitor the wave traveling past it.

Energy
source

C

R

L

LC oscillator

Transformer

Traveling wave

P
Distant
point

Transmission
line

Electric
dipole
antenna

33-1 E LECTROMAG N ETIC WAVES

975

B

E

P
(h)

P

(g)

B

P

E
(f)

E

P

B

Greatest
magnitudes
(a)

Zero
magnitudes

B

P

E

Greatest
magnitudes
(e)

B

E

P
(b)

P
(c)

B

P

E
(d)

:
B

:
E

Figure 33-4 (a) – (h) The variation in the
electric field  and the magnetic field  at
the distant point P of Fig. 33-3 as one wave-
length of the electromagnetic wave travels
past it. In this perspective, the wave is
traveling directly out of the page. The two
fields vary sinusoidally in magnitude and
direction. Note that they are always per-
pendicular to each other and to the wave’s
direction of travel.

Because the dipole moment varies in magnitude and direction, the electric
field produced by the dipole varies in magnitude and direction. Also, because the
current  varies, the  magnetic  field  produced  by  the  current  varies  in  magnitude
and  direction. However, the  changes  in  the  electric  and  magnetic  fields  do  not
happen everywhere instantaneously; rather, the changes travel outward from the
antenna at the speed of light c. Together the changing fields form an electromag-
netic wave that travels away from the antenna at speed c. The angular frequency
of this wave is v, the same as that of the LC oscillator.

:
B

Electromagnetic Wave. Figure 33-4 shows how the electric field

and the
change with time as one wavelength of the wave sweeps past the
magnetic field
distant point P of Fig. 33-3; in each part of Fig. 33-4, the wave is traveling directly
out of the page. (We choose a distant point so that the curvature of the waves
suggested in Fig. 33-3 is small enough to neglect. At such points, the wave is said
to be a plane wave, and discussion of the wave is much simplified.) Note several
key features in Fig. 33-4; they are present regardless of how the wave is created:
:
E

are  always  perpendicular  to  the
and
direction in which the wave is traveling. Thus, the wave is a transverse wave, as
discussed in Chapter 16.

1. The  electric  and  magnetic  fields

:
B

:
E

2. The electric field is always perpendicular to the magnetic field.
3. The cross product
always gives the direction in which the wave travels.
4. The  fields  always  vary  sinusoidally, just  like  the  transverse  waves  discussed
in Chapter 16. Moreover, the fields vary with the same frequency and in phase
(in step) with each other.

:
& B

:
E

In keeping with these features, we can assume that the electromagnetic wave
is traveling toward P in the positive direction of an x axis, that the electric field in
Fig. 33-4  is  oscillating  parallel  to  the  y axis, and  that  the  magnetic  field  is  then
oscillating  parallel  to  the  z axis  (using  a  right-handed  coordinate  system, of
course). Then we can write the electric and magnetic fields as sinusoidal functions
of position x (along the path of the wave) and time t:

E ! Em sin(kx ’ vt),

B ! Bm sin(kx ’ vt),

(33-1)

(33-2)

in which Em and Bm are the amplitudes of the fields and, as in Chapter 16, v and k
are  the  angular  frequency  and  angular  wave  number  of  the  wave, respectively.
From these equations, we note that not only do the two fields form the electro-
magnetic wave but each also forms its own wave. Equation 33-1 gives the electric
wave  component of  the  electromagnetic  wave, and  Eq. 33-2  gives  the  magnetic
wave component. As we shall discuss below, these two wave components cannot
exist independently.

Wave  Speed. From  Eq. 16-13, we  know  that  the  speed  of  the  wave  is  v/k.
However, because this is an electromagnetic wave, its speed (in vacuum) is given
the symbol c rather than v. In the next section you will see that c has the value

c !

1
m0´0

(wave speed),

(33-3)

which is about 3.0 & 108 m/s. In other words,

1

All electromagnetic waves, including visible light, have the same speed c in vacuum.

You will also see that the wave speed c and the amplitudes of the electric and

976

CHAPTE R  33 E LECTROMAG N ETIC WAVES

magnetic fields are related by

Em
Bm

! c

(amplitude ratio).

(33-4)

If we divide Eq. 33-1 by Eq. 33-2 and then substitute with Eq. 33-4, we find that
the magnitudes of the fields at every instant and at any point are related by

E
B

! c

(magnitude ratio).

(33-5)

Rays and Wavefronts. We can represent the electromagnetic wave as in Fig. 33-
5a, with a ray (a directed line showing the wave’s direction of travel) or with wave-
fronts (imaginary surfaces over which the wave has the same magnitude of electric
field), or both. The two wavefronts shown in Fig. 33-5a are separated by one wave-
length l (! 2p/k) of the wave. (Waves traveling in approximately the same direction
form a beam, such as a laser beam, which can also be represented with a ray.)

Drawing the Wave. We can also represent the wave as in Fig. 33-5b, which
shows the electric and magnetic field vectors in a “snapshot” of the wave at a
certain  instant. The  curves  through  the  tips  of  the  vectors  represent  the  sinu-
:
B
soidal oscillations given by Eqs. 33-1 and 33-2; the wave components
are  in  phase, perpendicular  to  each  other, and  perpendicular  to  the  wave’s
direction of travel.

and

:
E

Interpretation  of  Fig. 33-5b requires  some  care. The  similar  drawings  for  a
transverse wave on a taut string that we discussed in Chapter 16 represented the
up  and  down  displacement  of  sections  of  the  string  as  the  wave  passed  (some-
thing actually moved ). Figure 33-5b is more abstract. At the instant shown, the
electric  and  magnetic  fields  each  have  a  certain  magnitude  and  direction  (but
always perpendicular to the x axis) at each point along the x axis. We choose to
represent these vector quantities with a pair of arrows for each point, and so we
must draw arrows of different lengths for different points, all directed away from
the x axis, like thorns on a rose stem. However, the arrows represent field values
only at points that are on the x axis. Neither the arrows nor the sinusoidal curves
represent a sideways motion of anything, nor do the arrows connect points on the
x axis with points off the axis.

Feedback. Drawings like Fig. 33-5 help us visualize what is actually a very
complicated situation. First consider the magnetic field. Because it varies sinu-
soidally, it  induces  (via  Faraday’s  law  of  induction)  a  perpendicular  electric
field that also varies sinusoidally. However, because that electric field is vary-
ing  sinusoidally, it  induces  (via  Maxwell’s  law  of  induction)  a  perpendicular
magnetic field that also varies sinusoidally. And so on. The two fields continu-
ously create each other via induction, and the resulting sinusoidal variations
in the fields travel as a wave — the electromagnetic wave. Without this amaz-
ing result, we could not see; indeed, because we need electromagnetic waves

(a)

y

(b)

z

Wavefronts

Ray

λ

dx

c

P

h

x

E

B

B

E

E

B

Electric
component

Magnetic
component

:
B

:
E

Figure 33-5 (a) An electromagnetic wave
represented with a ray and two wavefronts;
the wavefronts are separated by one wave-
length l. (b) The same wave represented in
a “snapshot” of its electric field  and mag-
netic field  at points on the x axis, along
which the wave travels at speed c. As it
travels past point P, the fields vary as
shown in Fig. 33-4. The electric component
of the wave consists of only the electric
fields; the magnetic component consists of
only the magnetic fields. The dashed rec-
tangle at P is used in Fig. 33-6.

33-1 E LECTROMAG N ETIC WAVES

977

from the Sun to maintain Earth’s temperature, without this result we could not
even exist.

A Most Curious Wave
The waves we discussed in Chapters 16 and 17 require a medium (some material)
through which or along which to travel. We had waves traveling along a string,
through Earth, and through the air. However, an electromagnetic wave (let’s use
the term light wave or light) is curiously different in that it requires no medium
for its travel. It can, indeed, travel through a medium such as air or glass, but it
can also travel through the vacuum of space between a star and us.

Once  the  special  theory  of  relativity  became  accepted, long  after  Einstein
published it in 1905, the speed of light waves was realized to be special. One rea-
son  is  that  light  has  the  same  speed  regardless  of  the  frame  of  reference  from
which it is measured. If you send a beam of light along an axis and ask several
observers  to  measure  its  speed  while  they  move  at  different  speeds  along  that
axis, either in the direction of the light or opposite it, they will all measure the
same speed for the light. This result is an amazing one and quite different from
what would have been found if those observers had measured the speed of any
other  type  of  wave; for  other  waves, the  speed  of  the  observers  relative  to  the
wave would have affected their measurements.

The meter has now been defined so that the speed of light (any electromag-

netic wave) in vacuum has the exact value

c ! 299 792 458 m/s,

which can be used as a standard. In fact, if you now measure the travel time of a
pulse of light from one point to another, you are not really measuring the speed
of the light but rather the distance between those two points.

The Traveling Electromagnetic Wave, Quantitatively
We shall now derive Eqs. 33-3 and 33-4 and, even more important, explore the
dual induction of electric and magnetic fields that gives us light.

Equation 33-4 and the Induced Electric Field
The dashed rectangle of dimensions dx and h in Fig. 33-6 is fixed at point P on the
x axis and in the xy plane (it is shown on the right in Fig. 33-5b). As the electro-
magnetic wave moves rightward past the rectangle, the magnetic flux #B through
the rectangle changes and — according to Faraday’s law of induction — induced
and
electric  fields  appear  throughout  the  region  of  the  rectangle. We  take
:
E
to be the induced fields along the two long sides of the rectangle. These
induced  electric  fields  are, in  fact, the  electrical  component  of  the  electro-
magnetic wave.

:
$ dE

:
E

Note the small red portion of the magnetic field component curve far from
the y axis  in  Fig. 33-5b. Let’s  consider  the  induced  electric  fields  at  the  instant
when this red portion of the magnetic component is passing through the rectan-
gle. Just  then, the  magnetic  field  through  the  rectangle  points  in  the  positive  z
direction and is decreasing in magnitude (the magnitude was greater just before
the red section arrived). Because the magnetic field is decreasing, the magnetic
flux #B through the rectangle is also decreasing. According to Faraday’s law, this
change  in  flux  is  opposed  by  induced  electric  fields, which  produce  a  magnetic
field

:
B
According to Lenz’s law, this in turn means that if we imagine the boundary
of  the  rectangle  to  be  a  conducting  loop, a  counterclockwise  induced  current
would  have  to  appear  in  it. There  is, of  course, no  conducting  loop; but  this
are indeed
analysis shows that the induced electric field vectors

in the positive z direction.

:
$ dE

and

:
E

:
E

The oscillating magnetic field
induces an oscillating and
perpendicular electric field.

y

dx

E + dE

x

h

E

B

z

:
B

Figure 33-6 As the electromagnetic wave
travels rightward past point P in Fig. 33-5b,
the sinusoidal variation of the magnetic
through a rectangle centered at P
field
induces electric fields along the rectangle.
At the instant shown,
magnitude and the induced electric field is
therefore greater in magnitude on the right
side of the rectangle than on the left.

is decreasing in

:
B

978

CHAPTE R  33 E LECTROMAG N ETIC WAVES

greater than that of
. Otherwise, the  net  induced  electric  field  would  not  act  counterclockwise

oriented as shown in Fig. 33-6, with the magnitude of
:
E
around the rectangle.

:
E

:
$ dE

Faraday’s Law. Let us now apply Faraday’s law of induction,

:

, E

! ds: ! ’

d#B
dt

 ,

(33-6)

counterclockwise around the rectangle of Fig. 33-6. There is no contribution to
the integral from the top or bottom of the rectangle because
are per-
pendicular to each other there. The integral then has the value

and

ds:

:
E

:

, E

! ds: ! (E $ dE)h ’ Eh ! h dE.

(33-7)

The flux #B through this rectangle is

where B is the average magnitude of  within the rectangle and h dx is the area
of the rectangle. Differentiating Eq. 33-8 with respect to t gives

:
B

#B ! (B)(h dx),

(33-8)

d#B
dt

! h dx

dB
dt

 .

If we substitute Eqs. 33-7 and 33-9 into Eq. 33-6, we find

or

h dE ! ’h dx

dB
dt

dE
dx

! ’

dB
dt

 .

(33-9)

(33-10)

Actually, both B and E are functions of two variables, coordinate x and time t, as
Eqs. 33-1 and 33-2 show. However, in evaluating dE/dx, we must assume that t is
constant  because  Fig. 33-6  is  an  “instantaneous  snapshot.” Also, in  evaluating
dB/dt we must assume that x is constant (a particular value) because we are deal-
ing with the time rate of change of B at a particular place, the point P shown in
Fig. 33-5b. The derivatives under these circumstances are partial derivatives, and
Eq. 33-10 must be written

7E
7x

! ’

7B
7t

 .

(33-11)

The minus sign in this equation is appropriate and necessary because, although
magnitude E is increasing with x at the site of the rectangle in Fig. 33-6, magni-
tude B is decreasing with t.
From Eq. 33-1 we have

7E
7x

7B
7t

! kEm cos(kx ’ vt)

! ’vBm cos(kx ’ vt).

and from Eq. 33-2

Then Eq. 33-11 reduces to

kEm cos(kx ’ vt) ! vBm cos(kx ’ vt).

(33-12)

The ratio v/k for a traveling wave is its speed, which we are calling c. Equation
33-12 then becomes

Em
Bm

! c

(amplitude ratio),

(33-13)

which is just Eq. 33-4.

33-1 E LECTROMAG N ETIC WAVES

979

The oscillating electric field
induces an oscillating and
perpendicular magnetic field.

y

E

x

B + dB

h

B

dx

z

Figure 33-7 The sinusoidal variation of the
electric field through this rectangle, located
(but not shown) at point P in Fig. 33-5b,
induces magnetic fields along the rectangle.
is
The instant shown is that of Fig. 33-6:
decreasing in magnitude, and the magni-
tude of the induced magnetic field is
greater on the right side of the rectangle
than on the left.

:
E

Equation 33-3 and the Induced Magnetic Field
Figure 33-7 shows another dashed rectangle at point P of Fig. 33-5b; this one is
in the  xz plane. As  the  electromagnetic  wave  moves  rightward  past  this  new
rectangle, the electric flux #E through the rectangle changes and — according to
Maxwell’s  law  of  induction — induced  magnetic  fields  appear  throughout  the
region of the rectangle. These induced magnetic fields are, in fact, the magnetic
component of the electromagnetic wave.

We see from Fig. 33-5b that at the instant chosen for the magnetic field repre-
sented in Fig. 33-6, marked in red on the magnetic component curve, the electric field
through the rectangle of Fig. 33-7 is directed as shown. Recall that at the chosen in-
stant, the magnetic field in Fig. 33-6 is decreasing. Because the two fields are in phase,
the electric field in Fig. 33-7 must also be decreasing, and so must the electric flux #E
through the rectangle. By applying the same reasoning we applied to Fig. 33-6, we
:
see  that  the  changing  flux  #E will  induce  a  magnetic  field  with  vectors
B
and
:
:
B
B
is greater than field
.

oriented as shown in Fig. 33-7, where field

:
$ dB

:
$ dB

:
B

Maxwell’s Law. Let us apply Maxwell’s law of induction,

:

, B

!ds: ! m0´0

d#E
dt

 ,

(33-14)

by proceeding counterclockwise around the dashed rectangle of Fig. 33-7. Only
the long sides of the rectangle contribute to the integral because the dot product
along the short sides is zero. Thus, we can write

:

, B

!ds: ! ’(B $ dB)h $ Bh ! ’h dB.

(33-15)

The flux #E through the rectangle is

#E ! (E)(h dx),
:
where E is  the  average  magnitude  of  within  the  rectangle. Differentiating
E
Eq. 33-16 with respect to t gives

(33-16)

d#E
dt

! h dx

dE
dt

 .

If we substitute this and Eq. 33-15 into Eq. 33-14, we find

’h dB ! m0´0 #h dx

dE

dt $

or, changing to partial-derivative notation as we did for Eq. 33-11,

’

7B
7x

! m0´0

7E
7t

.

(33-17)

Again, the minus sign in this equation is necessary because, although B is increas-
ing with x at point P in the rectangle in Fig. 33-7, E is decreasing with t.

Evaluating Eq. 33-17 by using Eqs. 33-1 and 33-2 leads to

’kBm cos(kx ’ vt) ! ’m0´0vEm cos(kx ’ vt),

which we can write as

Em
Bm

!

1
m0´0(v/k)

!

1
m0´0c

 .

Combining this with Eq. 33-13 leads at once to

c !

1
m0´0

(wave speed),

(33-18)

which is exactly Eq. 33-3.

1
