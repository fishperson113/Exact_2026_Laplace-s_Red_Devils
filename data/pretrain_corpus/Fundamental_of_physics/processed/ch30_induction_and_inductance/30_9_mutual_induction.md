890

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

Checkpoint 7

The table lists the number of turns per unit length, current, and cross-sectional area
for three solenoids. Rank the solenoids according to the magnetic energy density
within them, greatest first.

Solenoid

Turns per
Unit Length

Current

Area

a
b
c

2n1
n1
n1

i1
2i1
i1

2A1
A1
6A1

30-9 MUTUAL INDUCTION

Learning Objectives
After reading this module, you should be able to . . .

30.39 Describe the mutual induction of two coils and sketch

the arrangement.

30.40 Calculate the mutual inductance of one coil with respect
to a second coil (or some second current that is changing).

30.41 Calculate the emf induced in one coil by a second coil
in terms of the mutual inductance and the rate of change
of the current in the second coil.

Key Idea
● If coils 1 and 2 are near each other, a changing current in either coil can induce an emf in the other. This mutual induction is
described by

and

# 2 ! %M

# 1 ! %M

where M (measured in henries) is the mutual inductance.

di1
dt
di2
dt

,

Mutual Induction
In this section we return to the case of two interacting coils, which we first dis-
cussed in Module 30-1, and we treat it in a somewhat more formal manner. We
saw earlier that if two coils are close together as in Fig. 30-2, a steady current i in
one coil will set up a magnetic flux 0 through the other coil (linking the other
coil). If we change i with time, an emf # given by Faraday’s law appears in the sec-
ond coil; we called this process induction. We could better have called it mutual
induction, to suggest the mutual interaction of the two coils and to distinguish it
from self-induction, in which only one coil is involved.

Let  us  look  a  little  more  quantitatively  at  mutual  induction. Figure  30-19a
shows  two  circular  close-packed  coils  near  each  other  and  sharing  a  common
central axis. With the variable resistor set at a particular resistance R, the battery
produces a steady current i1 in coil 1. This current creates a magnetic field repre-
sented by the lines of
in the figure. Coil 2 is connected to a sensitive meter but
contains no battery; a magnetic flux 021 (the flux through coil 2 associated with
the current in coil 1) links the N2 turns of coil 2.

:
B
1

We define the mutual inductance M21 of coil 2 with respect to coil 1 as

M21 !

N2 021
i1

,

(30-57)

30-9 M UTUAL  I N DUCTION

891

:
B
1

Figure 30-19 Mutual induction. (a) The mag-
produced by current i1 in coil
netic field
1 extends through coil 2. If i1 is varied (by
varying resistance R), an emf is induced in
coil 2 and current registers on the meter
connected to coil 2. (b) The roles of the
coils interchanged.

B1

R

N 1

B1

N 2       2 1  Φ

N 1       1 2Φ

B2

N 2

i 1

+  –

Coil 1

(a )

0

0

Coil 2

Coil 1

i 2

+ –

Coil 2
(b )

which has the same form as Eq. 30-28,

L ! N0/i,

the definition of inductance. We can recast Eq. 30-57 as

If we cause i1 to vary with time by varying R, we have

M21i1 ! N2021.

M21

di1
dt

! N2

d021
dt

.

B2

R

(30-58)

(30-59)

(30-60)

The right side of this equation is, according to Faraday’s law, just the magnitude
of the emf #2 appearing in coil 2 due to the changing current in coil 1. Thus, with a
minus sign to indicate direction,

# 2 ! %M21

di1
dt

,

(30-61)

which you should compare with Eq. 30-35 for self-induction (# ! %L di/dt).

Interchange. Let us now interchange the roles of coils 1 and 2, as in Fig. 30-19b;
that is, we set up a current i2 in coil 2 by means of a battery, and this produces a
magnetic flux 012 that links coil 1. If we change i2 with time by varying R, we then
have, by the argument given above,

# 1 ! %M12

di2
dt

.

(30-62)

Thus, we see that the emf induced in either coil is proportional to the rate of
change  of  current  in  the  other  coil. The  proportionality  constants  M21 and M12
seem to be different. However, they turn out to be the same, although we cannot
prove that fact here. Thus, we have

M21 ! M12 ! M,

(30-63)

and we can rewrite Eqs. 30-61 and 30-62 as

and

# 2 ! %M

# 1 ! %M

di1
dt

di2
dt

.

(30-64)

(30-65)

892

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

Sample Problem 30.08 Mutual inductance of two parallel coils

Figure  30-20  shows  two  circular  close-packed  coils, the
smaller  (radius  R2, with  N2 turns)  being  coaxial  with  the
larger (radius R1, with N1 turns) and in the same plane.

(a)  Derive  an  expression  for  the  mutual  inductance  M for
this arrangement of these two coils, assuming that R1 / R2.

KEY IDEA

The mutual inductance M for these coils is the ratio of the
flux  linkage  (N0)  through  one  coil  to  the  current  i in  the
other coil, which produces that flux linkage. Thus, we need
to  assume  that  currents  exist  in  the  coils; then  we  need  to
calculate the flux linkage in one of the coils.

Calculations: The  magnetic  field  through  the  larger  coil
due to the smaller coil is nonuniform in both magnitude and
direction; so  the  flux  through  the  larger  coil  due  to  the
smaller  coil  is  nonuniform  and  difficult  to  calculate.
However, the smaller coil is small enough for us to assume
that the magnetic field through it due to the larger coil is ap-
proximately  uniform. Thus, the  flux  through  it  due  to  the
larger coil is also approximately uniform. Hence, to find M
we shall assume a current i1 in the larger coil and calculate
the flux linkage N2021 in the smaller coil:

R1

R2

i1

+  –

Figure 30-20 A small coil is located at the center of a large coil. The
mutual inductance of the coils can be determined by sending
current i1 through the large coil.

Substituting Eq. 30-68 for B1 and

2
p R2

for A2 in Eq. 30-67

yields

M !

N2 021
i1

.

(30-66)

N2 021 !

pm0 N1N2 R2
2R1

2 i1

.

The  flux  021 through  each  turn  of  the  smaller  coil  is,

Substituting this result into Eq. 30-66, we find

from Eq. 30-2,

021 ! B1A2,

where B1 is  the  magnitude  of  the  magnetic  field  at  points
is
within the small coil due to the larger coil and
the area enclosed by the turn. Thus, the flux linkage in the
smaller coil (with its N2 turns) is

2)
A2 (! p R2

N2021 ! N2B1A2.

(30-67)

To find B1 at points within the smaller coil, we can use

Eq. 29-26,

B(z) !

m0 iR2
2(R2 & z2 )3/2 ,

with z set to 0 because the smaller coil is in the plane of the
larger coil. That equation tells us that each turn of the larger
coil  produces  a  magnetic  field  of  magnitude  m0i1/2R1 at
points within the smaller coil. Thus, the larger coil (with its
N1 turns) produces a total magnetic field of magnitude

B1 ! N1

m0 i1
2R1

(30-68)

at points within the smaller coil.

M !

N2 021
i1

!

2
pm0 N1N2R2
2R1

.

(Answer)

(30-69)

(b)  What  is  the  value  of  M for N1 ! N2 ! 1200  turns,
R2 ! 1.1 cm, and R1 ! 15 cm?

Calculations: Equation 30-69 yields

M !

(p)(4p $ 10 %7 H/m)(1200)(1200)(0.011 m)2
(2)(0.15 m)

! 2.29 $ 10 %3 H % 2.3 mH.

(Answer)

Consider the situation if we reverse the roles of the two
coils — that is, if we produce a current i2 in the smaller coil
and try to calculate M from Eq. 30-57 in the form

M !

N1012
i2

.

The calculation of 012 (the nonuniform flux of the smaller
coil’s magnetic field encompassed by the larger coil) is not
simple. If  we  were  to  do  the  calculation  numerically  using
a computer, we would find M to be 2.3 mH, as above! This
emphasizes that Eq. 30-63 (M21 ! M12 ! M) is not obvious.

Additional examples, video, and practice available at WileyPLUS

Review & Summary

QU ESTIONS

893

Magnetic  Flux The magnetic flux
magnetic field

is defined as

:
B

0

B through an area A in a

0B ! " B

:

:
! dA
,

(30-1)

where the integral is taken over the area. The SI unit of magnetic
:
flux is the weber, where 1 Wb ! 1 T )m2. If
B
is perpendicular to
the area and uniform over it, Eq. 30-1 becomes

0B ! BA

: " A, B
(B

:

uniform).

(30-2)

Faraday’s Law of Induction If the magnetic flux  B through an
area bounded by a closed conducting loop changes with time, a current
and an emf are produced in the loop; this process is called induction.
The induced emf is

0

# ! %

d 0B
dt

(Faraday’s law).

(30-4)

If the loop is replaced by a closely packed coil of N turns, the induced
emf is

# ! %N

.

(30-5)

d 0B
dt

Lenz’s  Law An  induced  current  has  a  direction  such  that
the magnetic  field  due  to  the  current opposes  the  change  in  the
magnetic  flux  that  induces  the  current. The  induced  emf  has  the
same direction as the induced current.

Emf and the Induced Electric Field An emf is induced by
a changing magnetic flux even if the loop through which the flux is
changing  is  not  a  physical  conductor  but  an  imaginary  line. The
changing magnetic field induces an electric field
at every point
of such a loop; the induced emf is related to  by

:
E

:
E

# ! , E

:

! ds:,

(30-19)

where the integration is taken around the loop. From Eq. 30-19 we
can write Faraday’s law in its most general form,

:

, E

! ds: ! %

d 0B
dt

(Faraday’s law).

(30-20)

:
A changing magnetic field induces an electric field .
E

!
The SI unit of inductance is the henry (H), where 1 henry
1 T )m2/A. The inductance per unit length near the middle of a long
solenoid of cross-sectional area A and n turns per unit length is

1 H

!

L
l

! m0 n2A

(solenoid).

(30-31)

Self-Induction If a current i in a coil changes with time, an emf
is induced in the coil. This self-induced emf is

#L ! %L

di
dt

.

(30-35)

The direction of #L is found from Lenz’s law: The self-induced emf
acts to oppose the change that produces it.

Series RL Circuits If a constant emf # is introduced into a sin-
gle-loop circuit containing a resistance R and an inductance L, the
current rises to an equilibrium value of #/R:

i !

#
R

 (1 % e%t/tL)

(rise of current).

(30-41)

Here tL (! L/R) is the inductive time constant. When the source of
constant  emf  is  removed, the  current  decays  from  a value  i0
according to

i ! i0 e%t/tL

(decay of current).

(30-45)

Magnetic  Energy If  an  inductor  L carries  a  current  i, the
inductor’s magnetic field stores an energy given by

UB ! 1

2Li2

(magnetic energy).

(30-49)

If B is  the  magnitude  of  a  magnetic  field  at  any  point  (in  an
inductor or anywhere else), the density of stored magnetic energy
at that point is

uB !

B2
2m0

(magnetic energy density).

(30-55)

Mutual Induction If coils 1 and 2 are near each other, a chang-
ing current in either coil can induce an emf in the other. This mu-
tual induction is described by

Inductors An inductor is a device that can be used to produce a
known magnetic field in a specified region. If a current i is estab-
lished through each of the N windings of an inductor, a magnetic
flux 0B links those windings. The inductance L of the inductor is

and

# 2 ! %M

# 1 ! %M

di1
dt
di2
dt

,

(30-64)

(30-65)

(inductance defined).

(30-28)

where M (measured in henries) is the mutual inductance.

L !

N 0B
i

Questions

1 If  the  circular  conductor  in  Fig. 30-21  undergoes  thermal
expansion  while  it  is  in  a  uniform  mag-
netic field, a current is induced clockwise
around  it. Is  the  magnetic  field  directed
into or out of the page?

y

Bz

2

x

1

4

3

5

6

t

2 The wire loop in Fig. 30-22a is sub-
jected, in turn, to six uniform magnetic
fields, each  directed  parallel  to  the  z

Figure 30-21 Question 1.

Figure 30-22 Question 2.

(a)

(b)

894

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

axis, which is directed out of the plane of the figure. Figure 30-
22b gives the z components Bz of the fields versus time t. (Plots 1
and 3 are parallel; so are plots 4 and 6. Plots 2 and 5 are parallel
to the time axis.) Rank the six plots according to the emf induced
in  the  loop, greatest  clockwise  emf  first, greatest  counterclock-
wise emf last.

tion, rank the choices according to (a)
the  work  done  per  unit  charge  in  set-
ting up the induced current and (b) that
induced  current, greatest  first. (c)  For
each choice, what is the direction of the
induced current in the figure?

y

c

b

x

3 In Fig. 30-23, a long straight wire with current i passes (without
touching) three rectangular wire loops with edge lengths L, 1.5L,
and 2L. The loops are widely spaced (so as not to affect one an-
other). Loops 1 and 3 are symmetric about the long wire. Rank the
loops according to the size of the current induced in them if cur-
rent i is (a) constant and (b) increasing, greatest first.

2

1

Figure 30-23 Question 3.

i

3

4 Figure 30-24 shows two circuits in which a conducting bar is slid
at the same speed v through the same uniform magnetic field and
along a U-shaped wire. The parallel lengths of the wire are sepa-
rated by 2L in circuit 1 and by L in circuit 2. The current induced in
circuit 1 is counterclockwise. (a) Is the magnetic field into or out of
the page? (b) Is the current induced in circuit 2 clockwise or coun-
terclockwise? (c) Is the emf induced in circuit 1 larger than, smaller
than, or the same as that in circuit 2?

v

(1)

(2)

v

Figure 30-24 Question 4.

5 Figure 30-25 shows a circular region in which a decreasing uni-
form magnetic field is directed out of the page, as well as four con-
centric circular paths. Rank the paths according to the magnitude
of

evaluated along them, greatest first.

! ds:

:
- E

a

b

c

d

a

z

7 Figure  30-27  shows  a  circuit  with
two identical resistors and an ideal in-
ductor. Is the current through the cen-
tral resistor more than, less than, or the same as that through the
other resistor (a) just after the closing of switch S, (b) a long time
after that, (c) just after S is reopened a long time later, and (d) a
long time after that?

Figure 30-26 Question 6.

+
–

S

Figure 30-27 Question 7.

8 The  switch  in  the  circuit  of
Fig. 30-15 has been closed on a for a
very  long  time  when  it  is  then
thrown  to  b. The  resulting  current
through the inductor is indicated in
Fig. 30-28 for four sets of values for
the resistance R and inductance L:
(1) R0 and L0, (2) 2R0 and L0, (3) R0
and 2L0, (4) 2R0 and 2L0. Which set
goes with which curve?

d

c

i

b

a

9 Figure 30-29 shows three circuits
with  identical  batteries, inductors,
and  resistors. Rank  the  circuits,
greatest first, according to the current through the resistor labeled
R (a) long  after  the  switch  is  closed, (b)  just  after  the  switch  is
reopened a long time later, and (c) long after it is reopened.

Figure 30-28 Question 8.

t

+
–

R

+
–

+
–

R

R

(2)

(3)

Figure 30-29 Question 9.

Figure 30-25 Question 5.

(1)

6 In Fig. 30-26, a wire loop has been bent so that it has three seg-
ments: segment bc (a quarter-circle), ac (a square corner), and ab
(straight). Here are three choices for a magnetic field through the
loop:

(1)

(2)

(3)

:
B
:
B
:
B

1 ! 3ˆi & 7ˆj % 5t ˆk
,
2 ! 5tˆi % 4ˆj % 15 ˆk
,
3 ! 2ˆi % 5tˆj % 12 ˆk
:
B

,

where

is in milliteslas and t is in seconds. Without written calcula-

10 Figure 30-30 gives the variation
with time of the potential difference
VR across a resistor in three circuits
wired as shown in Fig. 30-16. The cir-
cuits  contain  the  same  resistance  R
and  emf  # but  differ  in  the  induc-
tance L. Rank the circuits according
to the value of L, greatest first.

a

b

c

R
V

t

Figure 30-30 Question 10.

PROB LE M S

895

11 Figure 30-31 shows three situations in which a wire loop lies
partially in a magnetic field. The magnitude of the field is either in-
creasing or decreasing, as indicated. In each situation, a battery is
part of the loop. In which situations are the induced emf and the
battery emf in the same direction along the loop?

page) at the same constant speed. The loops have edge lengths of
either L or 2L, as drawn. Rank the situations according to (a) the
magnitude of the force required of us and (b) the rate at which
energy  is  transferred  from  us  to  thermal  energy  of  the  loop,
greatest first.

" #

B ! 0

# "

B ! 0

# "

B ! 0

B increasing

B decreasing

B decreasing

B

B

B

B

(a )

(b )

(c )

Figure 30-31 Question 11.

12 Figure 30-32 gives four situations in which we pull rectangu-
lar wire loops out of identical magnetic fields (directed into the

(1 )

(2)

(3)

(4)

Figure 30-32 Question 12.

Problems

Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign

SSM Worked-out solution available in Student Solutions Manual
• – ••• Number of dots indicates level of problem difficulty

WWW Worked-out solution is at

ILW Interactive solution is at

http://www.wiley.com/college/halliday

Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com

:
N

Module 30-1 Faraday’s Law and
Lenz’s Law
•1 In Fig. 30-33, a circular loop of wire 10 cm
in  diameter  (seen  edge-on)  is  placed  with  its
at an angle u ! 30° with the direction
normal
of  magnitude
of  a  uniform  magnetic  field
ro-
0.50 T. The loop is then rotated such that
tates in a cone about the field direction at the
rate  100 rev/min; angle  u remains  unchanged
during the process. What is the emf induced in
the loop?

:
N

:
B

B

N

θ

Loop

Figure 30-33
Problem 1.

•5 In  Fig. 30-36, a  wire  forms  a  closed  circular  loop, of  radius
R ! 2.0 m and resistance 4.0 1. The circle is centered on a long
straight wire; at time t ! 0, the current in the long straight wire
is 5.0 A rightward. Thereafter, the current changes according to
i ! 5.0 A % (2.0 A /s2)t2. (The straight wire is insulated; so there
is  no  electrical  contact  between  it  and  the  wire  of  the  loop.)
What  is  the  magnitude  of  the  current  induced  in  the  loop  at
times t , 0?

•2 A certain elastic conducting material is stretched into a cir-
cular loop of 12.0 cm radius. It is placed with its plane perpendi-
cular to a uniform 0.800 T magnetic field. When released, the ra-
dius  of  the  loop  starts  to  shrink  at  an  instantaneous  rate  of
75.0 cm/s. What emf is induced in the loop at that instant?

SSM

WWW

In Fig. 30-34, a 120-
•3
turn coil of radius 1.8 cm and resist-
ance 5.3 1 is coaxial with a solenoid
of 220 turns/cm and diameter 3.2 cm.
The  solenoid  current  drops  from
1.5 A  to  zero  in  time  interval  ’t !
25 ms. What current is induced in the
coil during ’t?

Coil

Solenoid

Figure 30-34 Problem 3.

Bs

:
B

)
T
(
B

•4 A wire loop of radius 12 cm and re-
sistance  8.5  1 is  located  in  a  uniform
magnetic  field
that  changes  in  magni-
tude  as  given  in  Fig. 30-35. The  vertical
axis  scale  is  set  by  Bs ! 0.50 T, and  the
horizontal axis scale is set by ts ! 6.00 s.
:
B
The  loop’s  plane  is  perpendicular  to
.
What emf is induced in the loop during time intervals (a) 0 to 2.0 s,
(b) 2.0 s to 4.0 s, and (c) 4.0 s to 6.0 s?

Figure 30-35 Problem 4.

t (s)

ts

0

R

Figure 30-36 Problem 5.

•6 Figure  30-37a shows  a  circuit  consisting  of  an  ideal  battery
with emf # ! 6.00 mV, a resistance R, and a small wire loop of area
5.0 cm2. For the time interval t ! 10 s to t ! 20 s, an external mag-
netic  field  is  set  up  throughout  the  loop. The  field  is  uniform, its
direction is into the page in Fig. 30-37a, and the field magnitude is
given  by  B ! at, where  B is  in  teslas, a is  a constant, and  t is  in
seconds. Figure 30-37b gives the current i in the circuit before, dur-
ing, and after the external field is set up. The vertical axis scale is
set by is ! 2.0 mA. Find the constant a in the equation for the field
magnitude.

R

)
A
m
(

i

is

0

30

(a )

(b )

t (s)

Figure 30-37 Problem 6.

896

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

•7 In  Fig. 30-38,
the  magnetic  flux
through  the  loop  increases  according  to
the relation 0B ! 6.0t2 & 7.0t, where 0B is
in milliwebers and t is in seconds. (a) What
is the magnitude of the emf induced in the
loop when t
2.0 s? (b) Is the direction of
the current through R to the right or left?

!

B

:
B

•8 A  uniform  magnetic  field
is  per-
pendicular to the plane of a circular loop
of  diameter  10 cm  formed  from  wire  of
diameter  2.5 mm  and  resistivity  1.69  $
10 %8 1)m. At  what  rate  must  the  magni-
tude of

:
B

change to induce a 10 A current in the loop?

R

Figure 30-38 Problem 7.

•9 A small loop of area 6.8 mm2 is placed inside a long solenoid
that has 854 turns/cm and carries a sinusoidally varying current i of
amplitude 1.28 A and angular frequency 212 rad/s. The central axes
of the loop and solenoid coincide. What is the amplitude of the emf
induced in the loop?

Magnetic
field

••10 Figure  30-39  shows  a  closed
loop of wire that consists of a pair of
equal  semicircles, of  radius  3.7  cm,
lying
in  mutually  perpendicular
planes. The loop was formed by fold-
ing a flat circular loop along a diam-
eter  until  the  two  halves  became
perpendicular  to  each  other. A  uni-
form magnetic field
of magnitude
76 mT  is  directed  perpendicular  to
the  fold  diameter  and  makes  equal
angles (of 45°) with the planes of the
semicircles. The magnetic field is reduced to zero at a uniform rate
during  a  time  interval  of  4.5 ms. During  this  interval, what  are
the (a)  magnitude  and  (b)  direction  (clockwise  or  counterclock-
wise when viewed along the direction of
) of the emf induced in
the loop?

Figure 30-39 Problem 10.

:
B

:
B

••11 A rectangular coil of N turns and of length a and width b is
rotated at frequency f in a uniform magnetic field
, as indicated in
Fig. 30-40. The  coil  is  connected  to  co-rotating  cylinders, against
which metal brushes slide to make contact. (a) Show that the emf
induced in the coil is given (as a function of time t) by

:
B

# ! 2pfNabB sin(2pft) ! #0 sin(2pft).

This is the principle of the commercial alternating-current gen-
erator. (b)  What  value  of  Nab gives  an  emf  with  #0 ! 150  V
when the loop is rotated at 60.0 rev/s in a uniform magnetic field
of 0.500 T?

Sliding contacts

B

b

R

a

Figure 30-40 Problem 11.

••12 In Fig. 30-41, a wire loop of lengths L ! 40.0 cm and W
:
B
25.0 cm lies in a magnetic field
(b) direction (clockwise or counterclockwise — or “none” if

!
. What are the (a) magnitude  and
0)

#
# !

#

What  are  (c)
:
! (6.00 $ 10 %2 T/s)t ˆk?
B

of the emf induced in the loop if
10 %2 T/m)y ˆk?
direction  if
#
are (e)
10 %2 T/m)s)yt ˆk?
direction if
#
are  (i)
10 %2 T/m)s)ytˆi?

and (f) the direction if
#

and  (j)  the  direction  if

What  are  (g)

:
! (4.00 $
B
and  (d)  the
What
:
! (8.00 $
B
and (h)  the
What
! (5.00 $

! (3.00 $ 10%2 T/m)s)xtˆj?

:
B

:
B

y

L

W

x

Figure 30-41
Problem 12.

ILW

One  hundred  turns  of  (insulated)  copper  wire  are
••13
wrapped around a wooden cylindrical core of cross-sectional area
1.20 $ 10 %3 m2. The two ends of the wire are connected to a resis-
tor. The total resistance in the circuit is 13.0 1. If an externally ap-
plied uniform longitudinal magnetic field in the core changes from
1.60 T  in  one  direction  to  1.60 T  in  the  opposite  direction, how
much charge flows through a point in the circuit during the change?

:
B

In  Fig. 30-42a, a  uniform  magnetic  field

increases  in
••14
magnitude with time t as given by Fig. 30-42b, where the vertical
axis scale is set by Bs ! 9.0 mT and the horizontal scale is set by
ts ! 3.0 s. A circular conducting loop of area 8.0 $ 10%4 m2 lies in
the field, in the plane of the page. The amount of charge q passing
point A on the loop is given in Fig. 30-42c as a function of t, with
the vertical axis scale set by qs ! 6.0 mC and the horizontal axis
scale again set by ts ! 3.0 s. What is the loop’s resistance?

)
T
m
(
B

Bs

0

B

A

(a )

ts

t (s)

(b)

)
C
m
(

q

qs

0

Figure 30-42 Problem 14.

A  square  wire  loop  with
••15
2.00 m  sides  is  perpendicular  to  a
uniform magnetic field, with half the
area  of  the  loop  in  the  field  as
shown  in  Fig. 30-43. The  loop  con-
tains an ideal battery with emf # !
20.0 V. If the magnitude of the field
varies  with  time  according  to  B !
0.0420 % 0.870t, with B in teslas and
t in seconds, what are (a) the net emf
in the circuit and (b) the direction of
the  (net)  current  around  the  loop?

ts

t (s)

(c)

B

bat

Figure 30-43 Problem 15.

Figure  30-44a shows  a  wire  that  forms  a  rectangle
••16
(W 20 cm, H 30 cm)  and  has  a  resistance  of  5.0 m . Its1

!

!

y

H

B1

B2

B3

W

(a )

Bs

0

)
T
µ
(

z

B

2

ts

1

3

x

–Bb

t (s)

(b)

Figure 30-44 Problem 16.

:
:
1, B
B
,
interior is split into three equal areas, with magnetic fields
2
:
B
. The fields are uniform within each region and directly out
and
3
of or into the page as indicated. Figure 30-44b gives the change in
the z components Bz of the three fields with time t; the vertical axis
scale is set by Bs ! 4.0 mT and Bb ! %2.5Bs, and the horizontal axis
scale is set by ts ! 2.0 s. What are the (a) magnitude and (b) direc-
tion of the current induced in the wire?

/

by a distance x R. Consequently, the magnetic field due to the
counterclockwise  current  i in  the  larger  loop  is  nearly  uniform
throughout  the  smaller  loop. Suppose  that  x is  increasing  at  the
constant  rate  dx/dt ! v. (a)  Find  an  expression  for  the  magnetic
flux through the area of the smaller loop as a function of x. (Hint:
See Eq. 29-27.) In the smaller loop, find (b) an expression for the
induced emf and (c) the direction of the induced current.

PROB LE M S

897

••17 A small circular loop of area 2.00 cm2 is placed in the plane
of, and concentric with, a large circular loop of radius 1.00 m. The
current in the large loop is changed at a constant rate from 200 A
to %200 A  (a  change  in  direction)  in  a  time  of  1.00 s, starting  at
t ! 0. What is the magnitude of the magnetic field
at the center
of the small loop due to the current in the large loop at (a) t ! 0,
:
(b) t ! 0.500 s, and (c) t ! 1.00 s? (d) From t ! 0 to t ! 1.00 s, is
B
reversed? Because the inner loop is small, assume
is uniform over
its area. (e) What emf is induced in the small loop at t ! 0.500 s?

:
B

:
B

v

••18 In Fig. 30-45, two straight con-
ducting  rails  form  a  right  angle. A
conducting  bar  in  contact  with  the
rails starts at the vertex at time t ! 0
and  moves  with  a  constant  velocity
of 5.20 m/s along them. A magnetic
field  with  B ! 0.350 T  is  directed
out  of  the  page. Calculate  (a)  the
flux through the triangle formed by the rails and bar at t ! 3.00 s
and (b) the emf around the triangle at that time. (c) If the emf is
# ! at n, where a and n are constants, what is the value of n?

Figure 30-45 Problem 18.

B

ILW

An electric generator contains a coil of 100 turns of wire,
••19
each  forming  a  rectangular  loop  50.0 cm  by  30.0 cm. The  coil  is
placed  entirely  in  a  uniform  magnetic  field  with  magnitude  B !
3.50 T and with
initially perpendicular to the coil’s plane. What
is the maximum value of the emf produced when the coil is spun at
:
B
1000 rev/min about an axis perpendicular to  ?

:
B

••20 At  a  certain  place, Earth’s  magnetic  field  has  magnitude
B ! 0.590 gauss and is inclined downward at an angle of 70.0" to
the horizontal. A flat horizontal circular coil of wire with a radius
of 10.0 cm has 1000 turns and a total resistance of 85.0 1. It is con-
nected in series to a meter with 140 1 resistance. The coil is flipped
through a half-revolution about a diameter, so that it is again hori-
zontal. How  much  charge  flows
through the meter during the flip?

••21 In Fig. 30-46, a stiff wire bent
into  a  semicircle  of  radius  a ! 2.0
cm  is  rotated  at  constant  angular
speed  40 rev/s  in  a uniform  20 mT
magnetic field. What are the (a) fre-
quency and (b) amplitude of the emf
induced in the loop?

••22 A  rectangular  loop  (area !
0.15 m2) turns in a uniform magnetic
field, B ! 0.20 T. When the angle be-
tween  the  field  and  the  normal  to
the plane of the loop is p/2 rad and
increasing  at  0.60 rad/s, what  emf  is
induced in the loop?

SSM

Figure  30-47  shows  two
••23
parallel loops of wire having a com-
mon axis. The smaller loop (radius r)
is  above  the  larger  loop  (radius  R)

i

a

B

R

Figure 30-46 Problem 21.

r

x

R

••24 A  wire  is  bent  into  three
circular segments, each of radius r !
10 cm, as  shown  in  Fig. 30-48. Each
segment  is  a quadrant  of  a  circle,
ab lying  in  the  xy plane, bc lying  in
the yz plane, and  ca lying  in  the  zx
plane. (a)  If  a  uniform  magnetic
field  points in the positive x direc-
tion, what  is  the  magnitude  of  the
emf  developed  in  the  wire  when  B
increases  at  the  rate  of  3.0 mT/s?
(b) What  is  the  direction  of  the
current in segment bc?

:
B

z

c

r

r

r

b

y

a

x

Figure 30-48 Problem 24.

Two long, parallel copper wires of diameter 2.5 mm carry
•••25
currents  of  10 A  in  opposite  directions. (a)  Assuming  that  their
central axes are 20 mm apart, calculate the magnetic flux per meter
of wire that exists in the space between those axes. (b) What per-
centage  of  this  flux  lies  inside  the  wires?  (c) Repeat  part  (a)  for
parallel currents.

12.0 cm  and  b

For the wire arrangement
•••26
!
!
in  Fig. 30-49, a
16.0 cm. The  current  in  the  long
straight  wire  is  i ! 4.50t2 % 10.0t,
where i is in amperes and t is in sec-
onds. (a) Find the emf in the square
loop  at  t ! 3.00 s. (b)  What  is  the
direction  of  the  induced  current  in
the loop?

ILW

As  seen  in  Fig. 30-50, a
•••27
square  loop  of  wire  has  sides  of
length 2.0 cm. A magnetic field is di-
rected out of the page; its magnitude
is given by B ! 4.0t2y, where B is in
teslas, t is in seconds, and y is in me-
t ! 2.5 s, what  are  the
ters. At
(a) magnitude  and  (b)  direction  of
the emf induced in the loop?

b

a

i

b

Figure 30-49 Problem 26.

y

B

x

Figure 30-50 Problem 27.

!

2.2 cm, width b

In Fig. 30-51, a rectangular

•••28
loop of wire with length a
0.80 cm, and resist-
ance R ! 0.40 m1 is  placed  near  an  infinitely  long  wire  carrying
current i ! 4.7 A. The loop is then moved away from the wire at
constant  speed  v ! 3.2 mm/s. When  the  center  of  the  loop  is  at
distance r ! 1.5b, what are (a) the magnitude of the magnetic flux
through the loop and (b) the current induced in the loop?

!

v

r

a

i

b

Figure 30-47 Problem 23.

Figure 30-51 Problem 28.

898

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

v

L

v:

Induction and Energy Transfers

Module 30-2
•29 In  Fig. 30-52, a  metal  rod  is
forced to move with constant veloc-
ity
along  two  parallel  metal  rails,
connected  with  a strip  of  metal  at
one end. A magnetic field of magni-
tude B ! 0.350 T  points  out  of  the
page. (a)  If  the  rails  are  separated
by L ! 25.0 cm and the speed of the
rod  is  55.0 cm/s, what  emf  is  gener-
ated? (b) If the rod has a resistance of 18.0 " and the rails and con-
nector  have  negligible  resistance, what  is  the  current  in  the  rod?
(c) At what rate is energy being transferred to thermal energy?

Figure 30-52
Problems 29 and 35.

B

•30 In Fig. 30-53a, a circular loop of wire is concentric with a sole-
noid and lies in a plane perpendicular to the solenoid’s central axis.
The loop has radius 6.00 cm. The solenoid has radius 2.00 cm, con-
sists of 8000 turns/m, and has a current isol varying with time t as
given in Fig. 30-53b, where the vertical axis scale is set by is ! 1.00
A  and  the  horizontal  axis  scale  is  set  by  ts ! 2.0  s. Figure  30-53c
shows, as  a  function  of  time, the  energy  Eth that  is  transferred
to thermal energy of the loop; the vertical axis scale is set by Es !
100.0 nJ. What is the loop’s resistance?

)
A
(

l
o
s

i

is

0

)
J
n
(

h
t

E

Es

0

ts

t (s)

(c)

ts

t (s)

(b)

Figure 30-53 Problem 30.

(a )

ILW

SSM

If 50.0 cm of copper wire (diameter ! 1.00 mm) is
•31
formed into a circular loop and placed perpendicular to a uniform
magnetic field that is increasing at the constant rate of 10.0 mT/s, at
what rate is thermal energy generated in the loop?

•32 A  loop  antenna  of  area  2.00 cm2 and  resistance  5.21 m1 is
perpendicular  to  a  uniform  magnetic  field  of  magnitude  17.0 mT.
The field magnitude drops to zero in 2.96 ms. How much thermal
energy is produced in the loop by the change in field?

i

a

!

Figure 30-54 shows a rod of
••33
!
length L 10.0 cm that is forced to
move at constant speed v
5.00 m/s
along horizontal rails. The rod, rails,
and  connecting  strip  at  the  right
form a conducting loop. The rod has
resistance  0.400  1; the  rest  of  the
loop has negligible resistance. A cur-
i ! 100 A  through  the  long
rent
straight wire at distance a ! 10.0 mm
from the loop sets up a (nonuniform)
magnetic field through the loop. Find
the (a) emf and (b) current induced
in  the  loop. (c) At  what  rate  is  thermal  energy  generated  in  the
rod? (d) What is the magnitude of the force that must be applied to
the rod to make it move at constant speed? (e) At what rate does
this force do work on the rod?

Figure 30-54 Problem 33.

B

L

v

••34 In Fig. 30-55, a long rectangular conducting loop, of width L,
resistance R, and mass m, is hung in a horizontal, uniform magnetic

:
B

field
that is directed into the page
and  that  exists  only  above  line  aa.
The loop is then dropped; during its
fall, it  accelerates  until  it  reaches  a
certain  terminal  speed  vt. Ignoring
air drag, find an expression for vt.

L

B

a

a

v:

mg

••35 The conducting rod shown in
Fig. 30-52 has length L and is being
pulled  along  horizontal, frictionless
conducting rails at a constant veloc-
. The rails are connected at one
ity
end  with  a  metal  strip. A  uniform
:
B
magnetic  field
, directed  out  of
the page, fills the region in which the rod moves. Assume that L !
10 cm, v ! 5.0 m/s, and B ! 1.2 T. What are the (a) magnitude and
(b) direction (up or down the page) of the emf induced in the rod?
What are the (c) size and (d) direction of the current in the con-
ducting loop? Assume that the resistance of the rod is 0.40 1 and
that the resistance of the rails and metal strip is negligibly small.
(e)  At  what  rate  is  thermal  energy  being  generated  in  the  rod?
(f) What external force on the rod is needed to maintain  ? (g) At
what rate does this force do work on the rod?

Figure 30-55 Problem 34.

v:

Induced Electric Fields

Module 30-3
•36 Figure  30-56  shows  two  circu-
lar regions R1 and R2 with radii r1 !
20.0 cm  and  r2 ! 30.0 cm. In  R1
there is a uniform magnetic field of
magnitude B1 ! 50.0 mT  directed
into  the  page, and  in  R2 there  is  a
uniform  magnetic  field  of  magni-
tude B2 ! 75.0 mT  directed  out  of
the  page  (ignore  fringing). Both
fields  are  decreasing  at  the  rate  of
8.50 mT/s. Calculate
for
(a) path 1, (b) path 2, and (c) path 3.

:
- E

! ds:

Path 3

R1

R2

Path 1

Path 2

Figure 30-56 Problem 36.

ILW

SSM

A long solenoid has a diameter of 12.0 cm. When a
•37
current i exists in its windings, a uniform magnetic field of magni-
tude B ! 30.0 mT is produced in its interior. By decreasing i, the
field is caused to decrease at the rate of 6.50 mT/s. Calculate the
magnitude of the induced electric field (a) 2.20 cm and (b) 8.20 cm
from the axis of the solenoid.

0

Es

)
C
/
N
µ
(
E

A circular region in an xy
••38
plane  is  penetrated  by  a  uniform
magnetic field in the positive direc-
tion of the z axis. The field’s magni-
tude B (in  teslas)  increases  with
time t (in seconds) according to B !
at, where a is a constant. The magni-
tude E of the electric field set up by
that increase in the magnetic field is
given by Fig. 30-57 versus radial dis-
tance r; the  vertical  axis  scale  is  set  by  Es ! 300 mN/C, and  the
horizontal axis scale is set by rs ! 4.00 cm. Find a.
••39 The  magnetic  field  of  a  cylindrical  magnet  that  has  a
pole-face  diameter  of  3.3 cm  can  be  varied  sinusoidally  between
29.6 T and 30.0 T at a frequency of 15 Hz. (The current in a wire
wrapped around a permanent magnet is varied to give this varia-
tion  in  the  net  field.) At  a  radial  distance  of  1.6 cm, what  is  the
amplitude of the electric field induced by the variation?

Figure 30-57 Problem 38.

r (cm)

rs

Inductors and Inductance

Module 30-4
•40 The  inductance  of  a  closely  packed  coil  of  400  turns  is
8.0 mH. Calculate  the  magnetic  flux  through  the  coil  when  the
current is 5.0 mA.

••48 Inductors in parallel. Two inductors L1 and L2 are connected
in parallel and separated by a large distance so that the magnetic
field of one cannot affect the other. (a) Show that the equivalent
inductance is given by

PROB LE M S

899

•41 A  circular  coil  has  a  10.0 cm  radius  and  consists  of  30.0
closely  wound  turns  of  wire. An  externally  produced  magnetic
field of magnitude 2.60 mT is perpendicular to the coil. (a) If no
current is in the coil, what magnetic flux links its turns? (b) When
the  current  in  the  coil  is  3.80 A  in  a  certain  direction, the  net
flux through the coil is found to vanish. What is the inductance of
the coil?

••42 Figure  30-58  shows  a  copper  strip  of
width W ! 16.0 cm that has been bent to form
a  shape  that  consists  of  a tube  of  radius
R ! 1.8 cm  plus  two  parallel  flat  extensions.
Current i ! 35 mA  is  distributed  uniformly
across the width so that the tube is effectively
a one-turn solenoid. Assume that the magnetic
field  outside  the  tube  is  negligible  and  the
field inside the tube is uniform. What are (a)
the  magnetic  field  magnitude  inside  the  tube
and (b) the inductance of the tube (excluding
the flat extensions)?

i

i

i

R

W

Two  identical  long  wires  of  radius
1.53 mm  are  parallel  and  carry  identical

••43
!
a
currents in opposite directions. Their center-to-center separation is
d ! 14.2 cm. Neglect the flux within the wires but consider the flux
in  the  region  between  the  wires. What  is  the  inductance  per  unit
length of the wires?

Figure 30-58
Problem 42.

Module 30-5 Self-Induction
•44 A 12 H inductor carries a current of 2.0 A. At what rate must
the current be changed to produce a 60 V emf in the inductor?

•45 At  a  given  instant  the  current
and  self-induced  emf  in an inductor
are directed as indicated in Fig. 30-59.
(a)  Is  the current  increasing  or  de-
creasing?  (b)  The  induced  emf  is
17 V, and  the  rate  of  change  of  the  current  is  25 kA/s; find  the
inductance.

Figure 30-59 Problem 45.

L

i

••46 The current i through a 4.6 H
inductor varies with time t as shown
by the graph of Fig. 30-60, where the
vertical axis scale is set by is ! 8.0 A
and the horizontal axis scale is set by
ts ! 6.0 ms. The inductor has a resist-
ance of 12 ". Find the magnitude of
the induced emf # during time inter-
vals (a) 0 to 2 ms, (b) 2 ms to 5 ms, and
(c) 5 ms to 6 ms. (Ignore the behavior
at the ends of the intervals.)

)
A
(

i

is

0

t (ms)

Figure 30-60 Problem 46.

••47 Inductors in series. Two inductors L1 and L2 are connected in
series and are separated by a large distance so that the magnetic
field of one cannot affect the other. (a) Show that the equivalent
inductance is given by

Leq ! L1 $ L2.
(Hint: Review the derivations for resistors in series and capacitors
in series. Which is similar here?) (b) What is the generalization of
(a) for N inductors in series?

1
Leq

1
L1
(Hint: Review  the  derivations  for  resistors  in  parallel  and
capacitors in parallel. Which is similar here?) (b) What is the gen-
eralization of (a) for N inductors in parallel?

1
L2

!

$

.

••49 The inductor arrangement of
Fig. 30-61, with L1 ! 30.0 mH, L2 !
50.0 mH, L3 ! 20.0 mH, and  L4 !
15.0 mH, is  to  be  connected  to  a
varying current source. What is the
the
equivalent
arrangement?  (First  see  Problems
47 and 48.)

inductance  of

L1

L4

L 2

L 3

Figure 30-61 Problem 49.

Module 30-6 RL Circuits
•50 The  current  in  an  RL circuit  builds  up  to  one-third  of  its
steady-state value in 5.00 s. Find the inductive time constant.

ILW

The current in an RL circuit drops from 1.0 A to 10 mA
•51
in the first second following removal of the battery from the cir-
cuit. If L is 10 H, find the resistance R in the circuit.

•52 The switch in Fig. 30-15 is closed on a at time t ! 0. What is
the ratio #L/# of the inductor’s self-induced emf to the battery’s
emf (a) just after t ! 0 and (b) at t ! 2.00tL? (c) At what multiple
of tL will #L/# ! 0.500?

"

SSM

A  solenoid  having  an  inductance  of  6.30 mH  is  con-
•53
nected  in  series  with  a  1.20 k
resistor. (a)  If  a  14.0 V  battery  is
connected  across  the  pair, how  long  will  it  take  for  the  current
through the resistor to reach 80.0% of its final value? (b) What is
the current through the resistor at time t ! 1.0tL?
•54 In  Fig. 30-62, # ! 100 V, R1 !
10.0 ", R2 ! 20.0 ", R3 ! 30.0 ", and
L ! 2.00 H. Immediately after switch
S is closed, what are (a) i1 and (b) i2?
(Let  currents
indicated
in
directions  have  positive  values  and
currents  in  the  opposite  directions
have  negative  values.)  A  long  time
later, what are (c) i1 and (d) i2? The
switch  is  then  reopened. Just  then,
what are (e) i1 and (f) i2? A long time later, what are (g) i1 and (h) i2?

Figure 30-62 Problem 54.

R1
i2

the

R2

R3

+
–

i1

L

S

ts

A  battery  is  connected  to  a  series  RL circuit  at  time
SSM
0. At what multiple of tL will the current be 0.100% less than

•55
!
t
its equilibrium value?

•56 In Fig. 30-63, the inductor has 25 turns and the ideal battery
has an emf of 16 V. Figure 30-64 gives the magnetic flux # through
each  turn  versus  the  current  i through  the  inductor. The  vertical

R

S

L

2

) Φs
m

•

T
4
–
0
1
(
Φ

0

Figure 30-63 Problems 56,
80, 83, and 93.

is

i (A)

Figure 30-64 Problem 56.

900

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

axis scale is set by #s ! 4.0 & 10’4 T(m2, and the horizontal axis
scale is set by is ! 2.00 A. If switch S is closed at time t ! 0, at what
rate di/dt will the current be changing at t ! 1.5tL?

Fuse

In  Fig. 30-65, R ! 15 ",
••57
!
L 5.0 H,
the  ideal  battery  has
# !
10 V, and the fuse in the upper
branch is an ideal 3.0 A fuse. It has
zero  resistance  as  long  as  the  cur-
rent  through  it  remains  less  than
3.0 A. If  the  current  reaches  3.0 A,
the fuse “blows” and thereafter has
infinite resistance. Switch S is closed
at time t
0. (a) When does the fuse blow? (Hint: Equation 30-41
does not apply. Rethink Eq. 30-39.) (b) Sketch a graph of the cur-
rent i through the inductor as a function of time. Mark the time at
which the fuse blows.

Figure 30-65 Problem 57.

+
–

!

R

L

S

Suppose  the  emf  of  the  battery  in  the  circuit  shown  in
••58
!
Fig. 30-16 varies with time t so that the current is given by i(t)
3.0 $ 5.0t, where i is in amperes and t is in seconds. Take R ! 4.0 "
and L ! 6.0 H, and  find  an  expression  for  the  battery  emf  as  a
function of t. (Hint: Apply the loop rule.)

!

SSM

In  Fig. 30-66,
•••59
WWW
after switch S is closed at time t
0,
the  emf  of  the  source  is  automati-
cally adjusted to maintain a constant
current i through S. (a) Find the cur-
rent through the inductor as a func-
tion of time. (b) At what time is the
current through the resistor equal to
the current through the inductor?

S

R

L

Constant
current
source

Figure 30-66 Problem 59.

•••60 A wooden toroidal core with a square cross section has an
inner radius of 10 cm and an outer radius of 12 cm. It is wound with
one  layer  of  wire  (of  diameter  1.0 mm  and  resistance  per  meter
0.020 "/m). What are (a) the inductance and (b) the inductive time
constant of the resulting toroid? Ignore the thickness of the insula-
tion on the wire.

SSM

Module 30-7 Energy Stored in a Magnetic Field
A coil is connected in series with a 10.0 k" resistor. An
•61
ideal 50.0 V battery is applied across the two devices, and the cur-
rent reaches a value of 2.00 mA after 5.00 ms. (a) Find the induc-
tance of the coil. (b) How much energy is stored in the coil at this
same moment?

•62 A coil with an inductance of 2.0 H and a resistance of 10 " is
suddenly  connected  to  an  ideal  battery  with  # ! 100 V. At  0.10 s
after the connection is made, what is the rate at which (a) energy is
being stored in the magnetic field, (b) thermal energy is appearing
in the resistance, and (c) energy is being delivered by the battery?

ILW

At t ! 0, a battery is connected to a series arrangement
•63
of a resistor and an inductor. If the inductive time constant is 37.0
ms, at what time is the rate at which energy is dissipated in the re-
sistor equal to the rate at which energy is stored in the inductor’s
magnetic field?

•64 At t ! 0, a battery is connected to a series arrangement of a
resistor  and  an  inductor. At  what  multiple  of  the  inductive  time
constant will the energy stored in the inductor’s magnetic field be
0.500 its steady-state value?

••65
6.70

"

For the circuit of Fig. 30-16, assume that # ! 10.0 V, R !
0.!

, and L 5.50 H. The ideal battery is connected at time t

!

(a) How much energy is delivered by the battery during the first
2.00 s? (b) How much of this energy is stored in the magnetic field
of the inductor? (c) How much of this energy is dissipated in the
resistor?

Module 30-8 Energy Density of a Magnetic Field
•66 A circular loop of wire 50 mm in radius carries a current of
100 A. Find the (a) magnetic field strength and (b) energy density
at the center of the loop.

SSM

A  solenoid  that  is  85.0 cm  long  has  a  cross-sectional
•67
area of 17.0 cm2. There are 950 turns of wire carrying a current of
6.60 A. (a) Calculate the energy density of the magnetic field in-
side the solenoid. (b) Find the total energy stored in the magnetic
field there (neglect end effects).

•68 A toroidal inductor with an inductance of 90.0 mH encloses
a volume of 0.0200 m3. If the average energy density in the toroid is
70.0 J/m3, what is the current through the inductor?

ILW

What must be the magnitude of a uniform electric field if
•69
it is to have the same energy density as that possessed by a 0.50 T
magnetic field?

y

x

2

1

2

(a )

)
3
m
/
J
n
(

Figure  30-67a shows, in
••70
cross  section, two  wires  that  are
straight, parallel, and  very  long.
The  ratio  i1/i2 of  the  current  car-
ried  by  wire  1  to  that  carried  by
wire  2  is  1/3. Wire  1  is  fixed  in
place. Wire  2  can  be  moved  along
the positive side of the x axis so as
to  change  the  magnetic  energy
density uB set  up  by  the  two  cur-
rents  at  the  origin. Figure  30-67b
gives uB as  a  function  of  the  posi-
tion x of  wire  2. The  curve  has  an
asymptote  of uB ! 1.96 nJ/m3 as
x : %
, and  the  horizontal  axis
scale is set by xs ! 60.0 cm. What is
the value of (a) i1 and (b) i2?
••71 A length of copper wire carries a current of 10 A uniformly
distributed through its cross section. Calculate the energy density
of (a) the magnetic field and (b) the electric field at the surface of
the wire. The wire diameter is 2.5 mm, and its resistance per unit
length is 3.3 "/km.

Figure 30-67 Problem 70.

x (cm)

(b)

B
u

xs

0

1

Module 30-9 Mutual Induction
•72 Coil 1 has L1 ! 25 mH and N1 ! 100 turns. Coil 2 has L2 !
40 mH and N2 ! 200 turns. The coils are fixed in place; their mu-
tual inductance M is 3.0 mH. A 6.0 mA current in coil 1 is changing
at the rate of 4.0 A/s. (a) What magnetic flux #12 links coil 1, and
(b) what self-induced emf appears in that coil? (c) What magnetic
flux #21 links coil 2, and (d) what mutually induced emf appears in
that coil?

SSM

Two  coils  are  at  fixed  locations. When  coil  1  has  no
•73
current and the current in coil 2 increases at the rate 15.0 A/s, the
emf  in  coil  1  is  25.0 mV. (a)  What  is  their  mutual  inductance?
(b) When coil 2 has no current and coil 1 has a current of 3.60 A,
what is the flux linkage in coil 2?

•74 Two  solenoids  are  part  of  the  spark  coil  of  an  automobile.
When the current in one solenoid falls from 6.0 A to zero in 2.5 ms,
an  emf  of  30 kV  is  induced  in  the  other  solenoid. What  is  the
mutual inductance M of the solenoids?

ILW

A  rectangular  loop  of  N
••75
closely  packed  turns  is  positioned
near a long straight wire as shown in
Fig. 30-68. What is the mutual induc-
tance M for the loop – wire combina-
tion  if  N ! 100, a ! 1.0 cm, b !
8.0 cm, and l ! 30 cm?

••76 A coil C of N turns is placed
around  a  long  solenoid  S  of  radius
R and n turns  per  unit  length, as  in
Fig. 30-69. (a) Show that the mutual
inductance  for  the  coil – solenoid
is  given  by  M !
combination
m0pR2nN. (b)  Explain  why  M does
not depend on the shape, size, or pos-
sible lack of close packing of the coil.

i

N turns

a

b

l

Figure 30-68 Problem 75.

C

S

R

Figure 30-69 Problem 76.

SSM

Two  coils  connected  as

••77
shown in Fig. 30-70 separately have inductances L1 and L2. Their
mutual inductance is M. (a) Show that this combination can be re-
placed by a single coil of equivalent inductance given by

Leq ! L1 $ L2 $ 2M.

(b)  How  could  the  coils  in  Fig. 30-70  be  reconnected  to  yield  an
equivalent inductance of

Leq ! L1 $ L2 ’ 2M?

(This problem is an extension of Problem 47, but the requirement
that the coils be far apart has been removed.)

L1

M

L2

N1

N2

i

i

Figure 30-70 Problem 77.

Additional Problems
78 At  time  t ! 0, a  12.0 V  potential  difference  is  suddenly
applied to the leads of a coil of inductance 23.0 mH and a certain
resistance R. At time t ! 0.150 ms, the current through the induc-
tor is changing at the rate of 280 A/s. Evaluate R.

S

L

i1

i2

!

+
–

R1

5.0

# !

time

t ! 0.

10 V, R1

In Fig. 30-71, the battery is
79
SSM
"
ideal  and
,
R2 ! 10 ", and L ! 5.0 H. Switch S
is  closed  at
Just
afterwards, what  are  (a)  i1, (b)  i2,
(c) the current iS through the switch,
(d)  the  potential  difference  V2
across  resistor  2, (e)  the  potential
difference VL across  the  inductor,
and (f) the rate of change di2/dt? A
long time later, what are (g) i1, (h) i2,
(i) iS, (j) V2, (k) VL, and (l) di2/dt?
80 In  Fig. 30-63, R ! 4.0 k", L ! 8.0 mH, and  the  ideal  battery
has # ! 20 V. How  long  after  switch  S  is  closed  is  the  current
2.0 mA?

Figure 30-71 Problem 79.

R2

i

PROB LE M S

901

1

2

is

D

H

(a )

SSM

Figure  30-72a shows  a
81
rectangular  conducting  loop  of
resistance R ! 0.020 ", height
H ! 1.5 cm, and  length  D ! 2.5
cm being pulled at constant speed
v ! 40 cm/s  through  two  regions
of  uniform  magnetic  field. Figure
30-72b gives the current i induced
in  the  loop  as  a  function  of  the
position x of  the  right  side  of  the
loop. The vertical  axis  scale  is  set
by is ! 3.0 mA. For example, a cur-
rent  equal  to  is is  induced  clock-
wise  as  the  loop  enters  region  1.
What  are  the  (a)  magnitude  and
(b)  direction  (into  or  out  of  the  page)  of  the  magnetic  field  in
region 1? What are the (c) magnitude and (d) direction of the mag-
netic field in region 2?

Figure 30-72 Problem 81.

)
A
µ
0i
(

(b)

x

82 A uniform magnetic field
is perpendicular to the plane of a
circular  wire  loop  of  radius  r. The  magnitude  of  the  field  varies
with time according to B ! B0e’t/t, where B0 and t are constants.
Find an expression for the emf in the loop as a function of time.

:
B

83 Switch  S  in  Fig. 30-63  is  closed  at  time  t ! 0, initiating  the
buildup of current in the 15.0 mH inductor and the 20.0 " resistor.
At what time is the emf across the inductor equal to the potential
difference across the resistor?

:
B
1

:
B
2

regions

Figure  30-73a shows  two
84
concentric  circular
in
which uniform magnetic fields can
change. Region 1, with radius r1 !
1.0 cm, has  an  outward  magnetic
that is increasing in magni-
field
!
tude. Region  2, with  radius  r2
2.0 cm, has  an  outward  magnetic
field
that may also be changing.
Imagine that a conducting ring of
radius R is centered on the two re-
gions  and  then  the  emf  # around
the  ring  is  determined. Figure
30-73b gives emf # as a function of
the square R2 of the ring’s radius,
to the outer edge of region 2. The
vertical  axis  scale  is  set  by  #s !
20.0  nV. What  are  the  rates
(a) dB1/dt and  (b)  dB2/dt?  (c)  Is
the  magnitude  of
increasing,
decreasing, or remaining constant?

:
B
2

:
B

SSM

Figure 30-74 shows a uni-
85
:
B
form magnetic field
confined to
a  cylindrical  volume  of  radius  R.
is  decreasing
The  magnitude  of
at  a  constant  rate  of  10 mT/s. In
unit-vector  notation, what  is  the
initial  acceleration  of  an  electron
released  at  (a)  point  a (radial  dis-
tance r ! 5.0 cm), (b) point b (r !
0), and (c) point c (r ! 5.0 cm)?

r1

r2

(a )

)
V
n
(

(b)

s

0

2
R2 (cm2)

4

Figure 30-73 Problem 84.

y

r

b
r

c

a

R

x

B

In  Fig. 30-75a, switch  S
86
has been closed on A long enough
to  establish  a  steady  current  in  the  inductor  of  inductance

Figure 30-74 Problem 85.

902

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

!

!

25.0

5.00 mH  and  the  resistor  of  resistance  R1

"
L1
.
Similarly, in  Fig. 30-75b, switch  S  has  been  closed  on  A long
enough to establish a steady current in the inductor of inductance
L2 ! 3.00 mH and the resistor of resistance R2 ! 30.0 ". The ra-
tio #02/#01 of  the  magnetic  flux  through  a  turn  in  inductor  2  to
that  in  inductor  1  is  1.50. At  time  t ! 0, the  two  switches  are
closed on B. At what time t is the flux through a turn in the two
inductors equal?

A S

B

(a )

R1

L1

(b)

Figure 30-75 Problem 86.

A S

B

L2

R2

SSM
"

A  square  wire  loop  20 cm  on  a  side, with  resistance
87
20 m , has its plane normal to a uniform magnetic field of magni-
tude B ! 2.0 T. If  you  pull  two  opposite  sides  of  the  loop  away
from  each  other, the  other  two  sides  automatically  draw  toward
each other, reducing the area enclosed by the loop. If the area is re-
duced to zero in time )t ! 0.20 s, what are (a) the average emf and
(b) the average current induced in the loop during )t?

88 A  coil  with  150  turns  has  a  magnetic  flux  of  50.0 nT (m2
through each turn when the current is 2.00 mA. (a) What is the in-
ductance  of  the  coil?  What  are  the  (b)  inductance  and  (c)  flux
through each turn when the current is increased to 4.00 mA? (d)
What  is  the  maximum  emf  # across  the  coil  when  the  current
through it is given by i ! (3.00 mA) cos(377t), with t in seconds?

89 A coil with an inductance of 2.0 H and a resistance of 10 " is
suddenly connected to an ideal battery with # ! 100 V. (a) What is
the  equilibrium  current?  (b)  How  much  energy  is  stored  in  the
magnetic field when this current exists in the coil?

90 How long would it take, following the removal of the battery,
for  the  potential  difference  across  the  resistor  in  an  RL circuit
(with L ! 2.00 H, R ! 3.00 ")  to  decay  to  10.0%  of  its  initial
value?

L

R1

R 2

20

SSM
!

In the circuit of Fig. 30-76,
91
"
!"!
R1
, L 50 mH,
20 k , R2
and  the  ideal  battery  has  # ! 40 V.
Switch  S  has  been  open  for  a  long
time when it is closed at time t ! 0.
Just  after  the  switch  is  closed, what
are  (a)  the  current  ibat through  the
battery  and  (b)  the  rate  dibat/dt?
At t ! 3.0 ms, what  are  (c)  ibat and
(d) dibat/dt? A long time later, what are (e) ibat and (f) dibat/dt?
92 The  flux  linkage  through  a  certain  coil  of  0.75  " resistance
would  be  26 mWb  if  there  were  a  current  of  5.5 A  in  it. (a)
Calculate  the  inductance  of  the  coil. (b)  If  a  6.0 V  ideal  battery
were  suddenly  connected  across  the  coil, how  long  would  it  take
for the current to rise from 0 to 2.5 A?

Figure 30-76 Problem 91.

S

93 In Fig. 30-63, a 12.0 V ideal battery, a 20.0 " resistor, and an
inductor are connected by a switch at time t ! 0. At what rate is the
battery transferring energy to the inductor’s field at t ! 1.61tL?

meter of length? (b) If the current changes at the rate of 13 A/s,
what emf is induced per meter?

95 In Fig. 30-77, R1 ! 8.0 ", R2 ! 10 ", L1 ! 0.30 H, L2 ! 0.20 H,
and the ideal battery has # ! 6.0 V. (a) Just after switch S is closed,
at what rate is the current in inductor 1 changing? (b) When the
circuit is in the steady state, what is the current in inductor 1?

R1

L 1

S

R 2 L 2

Figure 30-77 Problem 95.

96 A  square  loop  of  wire  is  held  in  a  uniform  0.24 T  magnetic
field directed perpendicular to the plane of the loop. The length of
each side of the square is decreasing at a constant rate of 5.0 cm/s.
What emf is induced in the loop when the length is 12 cm?

97 At time t ! 0, a 45 V potential difference is suddenly applied
to  the  leads  of  a  coil  with  inductance  L ! 50 mH  and  resistance
R ! 180 ". At what rate is the current through the coil increasing
at t ! 1.2 ms?

98 The inductance of a closely wound coil is such that an emf of
3.00 mV  is  induced  when  the  current  changes  at  the  rate  of  5.00
A/s. A  steady  current  of  8.00 A  produces  a  magnetic  flux  of  40.0
mWb through each turn. (a) Calculate the inductance of the coil.
(b) How many turns does the coil have?

99 The magnetic field in the interstellar space of our galaxy has a
magnitude  of  about  10’10 T. How  much  energy  is  stored  in  this
field  in  a  cube  10  light-years  on  edge?  (For  scale, note  that  the
nearest star is 4.3 light-years distant and the radius of the galaxy is
about 8 & 104 light-years.)

100 Figure 30-78 shows a wire that has been bent into a circular
arc of radius r ! 24.0 cm, centered at O. A straight wire OP can be
rotated  about  O and  makes  sliding  contact  with  the  arc  at  P.
Another  straight  wire  OQ completes  the  conducting  loop. The
three  wires  have  cross-sectional  area  1.20  mm2 and  resistivity
10’8 " ( m, and  the  apparatus  lies  in  a  uniform  magnetic
1.70
field of magnitude B ! 0.150 T directed out of the figure. Wire OP
begins from rest at angle u ! 0 and has constant angular accelera-
tion  of  12 rad/s2. As  functions  of  u (in  rad), find  (a) the  loop’s
resistance and (b) the magnetic flux through the loop. (c) For what
u is the induced current maximum and (d) what is that maximum?

&

P

B

r

u

O

Q

Figure 30-78 Problem 100.

94 A long cylindrical solenoid with 100 turns/cm has a radius of
1.6 cm. Assume that the magnetic field it produces is parallel to its
axis  and  is  uniform  in  its  interior. (a) What  is  its  inductance  per

101 A toroid has a 5.00 cm square cross section, an inside radius
of 15.0 cm, 500 turns of wire, and a current of 0.800 A. What is the
magnetic flux through the cross section?
