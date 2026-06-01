27.9 The Hall Effect

909

(b) The power delivered to the motor from the source is

Pinput = VabI = 1120 V214.00 A2 = 480 W

(c) The power dissipated in the resistance

r

is

Pdissipated = I 2r = 14.00 A2212.00 Æ2 = 32 W

(d)  The  mechanical  power  output  is  the  electric  power  input
minus  the  rate  of  dissipation  of  energy  in  the  motor’s  resistance
(assuming that there are no other power losses):

Poutput = Pinput - Pdissipated = 480 W - 32 W = 448 W

(e) The efﬁciency

e

is the ratio of mechanical power output to

electric power input:

e =

Poutput
Pinput

= 448 W
480 W

= 0.93 = 93%

(f) With the rotor stalled, the back emf

(which is proportional
to rotor speed) goes to zero. From Eq. (27.29) the current becomes

E

I =

Vab
r

= 120 V
2.00 Æ

= 60 A

and the power dissipated in the resistance  becomes

r

Pdissipated = I 2r = 160 A2212.00 Æ2 = 7200 W

EVALUATE:  If this massive overload doesn’t blow a fuse or trip a
circuit breaker, the coils will quickly melt. When the motor is ﬁrst
turned  on,  there’s  a  momentary  surge  of  current  until  the  motor
picks up speed. This surge causes greater-than-usual voltage drops
1V = IR2
in the power lines supplying the current. Similar effects
are  responsible  for  the  momentary  dimming  of  lights  in  a  house
when an air conditioner or dishwasher motor starts.

Test Your Understanding of Section 27.8 In the circuit shown in Fig. 27.39,
you add a switch in series with the source of emf so that the current can be turned on and
off. When you close the switch and allow current to ﬂow, will the rotor begin to turn no
matter what its original orientation?

❙

27.9 The Hall Effect

The reality of the forces acting on the moving charges in a conductor in a magnetic
ﬁeld is strikingly demonstrated by the Hall effect, an effect analogous to the trans-
verse deﬂection of an electron beam in a magnetic ﬁeld in vacuum. (The effect was
discovered by the American physicist Edwin Hall in 1879 while he was still a grad-
uate student.) To describe this effect, let’s consider a conductor in the form of a ﬂat
strip,  as  shown  in  Fig.  27.41. The  current  is  in  the  direction  of  the
and
S
B
there is a uniform magnetic ﬁeld
perpendicular to the plane of the strip, in the
+y-direction.
has
The drift velocity of the moving charges (charge magnitude
vd.
Figure 27.41a shows the case of negative charges, such as electrons
magnitude
in  a  metal,  and  Fig.  27.41b  shows  positive  charges.  In  both  cases  the  magnetic
force is upward, just as the magnetic force on a conductor is the same whether the
moving charges are positive or negative. In either case a moving charge is driven
toward the upper edge of the strip by the magnetic force

+x-axis

Fz = ƒqƒvdB.

ƒqƒ)

e

S
E

that is equal and opposite to the magnetic force (magnitude

If  the  charge  carriers  are  electrons,  as  in  Fig.  27.41a,  an  excess  negative
charge  accumulates  at  the  upper  edge  of  the  strip,  leaving  an  excess  positive
charge  at  its  lower  edge. This  accumulation  continues  until  the  resulting  trans-
becomes  large  enough  to  cause  a  force  (magnitude
verse  electrostatic  ﬁeld
ƒqƒEe)
After
that,  there  is  no  longer  any  net  transverse  force  to  deﬂect  the  moving  charges.
This electric ﬁeld causes a transverse potential difference between opposite edges
of  the  strip,  called  the  Hall  voltage or  the  Hall  emf. The  polarity  depends  on
whether the moving charges are positive or negative. Experiments show that for
metals the upper edge of the strip in Fig. 27.41a does become negatively charged,
showing that the charge carriers in a metal are indeed negative electrons.

ƒqƒvdB).

However,  if  the  charge  carriers  are  positive, as  in  Fig.  27.41b,  then  positive
charge accumulates at the upper edge, and the potential difference is opposite to
the situation with negative charges. Soon after the discovery of the Hall effect in
1879,  it  was  observed  that  some  materials,  particularly  some  semiconductors,
show a Hall emf opposite to that of the metals, as if their charge carriers were
positively  charged.  We  now  know  that  these  materials  conduct  by  a  process
known  as  hole  conduction. Within  such  a  material  there  are  locations,  called
holes, that would normally be occupied by an electron but are actually empty. A
missing  negative  charge  is  equivalent  to  a  positive  charge.  When  an  electron
moves in one direction to ﬁll a hole, it leaves another hole behind it. The hole
migrates in the direction opposite to that of the electron.

27.41 Forces on charge carriers in a
conductor in a magnetic ﬁeld.

(a) Negative charge carriers (electrons)

The charge carriers are pushed toward the top
of the strip ...

z

Jx

By

b

vd

Fz

– – – – – – – – – –
+ + + + + + + + + +

Ee

By

q

a

y

Jx

x

... so point a is at a higher potential than point b.

(b) Positive charge carriers

The charge carriers are again pushed toward the
top of the strip ...

z

Jx

By

b

Ee

q

Fz

+ + + + + + + + + +
– – – – – – – – – –

By

vd

a

y

Jx

x

... so the polarity of the potential difference is
opposite to that for negative charge carriers.

910

CHAPTER 27 Magnetic Field and Magnetic Forces

In terms of the coordinate axes in Fig. 27.41b, the electrostatic ﬁeld

+y-direction,

positive-q case is in the
netic ﬁeld is in the
+z-direction)
is
steady state, when the forces
in direction,

qvdBy.

-z-direction;

its z-component

and we write it as

S
E

e

for the
Ez
is negative. The mag-
The magnetic force (in the
+x-direction.
In  the
are equal in magnitude and opposite

By.
is  in  the

Jx

The  current  density
and

qEz

qvdBy
qEz + qvdBy = 0    or    Ez = - vdBy
Ez
Jx = nqvd
between these equations, we ﬁnd

is positive,

q

This conﬁrms that when

is negative. The current density

Jx

is

Eliminating

vd

nq =

-JxBy
Ez

(Hall effect)

(27.30)

is positive, and conversely.

q
We can measure

Note that this result (as well as the entire derivation) is valid for both positive and
q.
negative  When

is negative,
Jx,
By,
and
In both
metals and semiconductors,
q
is equal in magnitude to the electron charge, so the
Hall effect permits a direct measurement of
the concentration of current-carrying
charges in the material. The sign of the charges is determined by the polarity of
the Hall emf, as we have described.

so we can compute the product

Ez
Ez,

nq.

n,

The  Hall  effect  can  also  be  used  for  a  direct  measurement  of  electron  drift
vd
in metals. As we saw in Chapter 25, these speeds are very small, often of
speed
the order of
or less. If we move the entire conductor in the opposite direc-
tion to the current with a speed equal to the drift speed, then the electrons are at
rest with respect to the magnetic ﬁeld, and the Hall emf disappears. Thus the con-
ductor speed needed to make the Hall emf vanish is equal to the drift speed.

1 mm>s

Example 27.12

A Hall-effect measurement

You place a strip of copper, 2.0 mm thick and 1.50 cm wide, in a uni-
form 0.40-T magnetic ﬁeld as shown in Fig. 27.41a. When you run a
you ﬁnd that the potential at the
75-A current in the
bottom of the slab is
higher than at the top. From this meas-
urement, determine the concentration of mobile electrons in copper.

+x-direction,
0.81mV

Then, from Eq. (27.30),

n =

-JxBy
qEz

=

-12.5 * 106 A>m2210.40 T2
1-1.60 * 10-19 C215.4 * 10-5 V>m2

= 11.6 * 1028 m-3

SOLUTION

IDENTIFY and SET UP: This problem describes a Hall-effect exper-
iment. We use Eq. (27.30) to determine the mobile electron con-
centration

n.

EXECUTE: First  we  ﬁnd  the  current  density
ﬁeld
Ez:
Jx = I
A

75 A
12.0 * 10-3 m211.50 * 10-2 m2
= 0.81 * 10-6 V
1.5 * 10-2 m

Ez = V
d

= 5.4 * 10-5 V>m

=

Jx

and  the  electric

= 2.5 * 106 A>m2

for  copper  is

8.5 * 1028 m-3
EVALUATE:  The  actual  value  of
n
.
The  difference  shows  that  our  simple  model  of  the  Hall  effect,
which  ignores  quantum  effects  and  electron  interactions  with  the
ions, must be used with caution. This example also shows that with
good conductors, the Hall emf is very small even with large cur-
rent  densities.  In  practice,  Hall-effect  devices  for  magnetic-ﬁeld
measurements  use  semiconductor  materials,  for  which  moderate
current densities give much larger Hall emfs.

Test Your Understanding of Section 27.9 A copper wire of square cross sec-
tion is oriented vertically. The four sides of the wire face north, south, east, and west.
There is a uniform magnetic ﬁeld directed from east to west, and the wire carries current
downward. Which side of the wire is at the highest electric potential? (i) north side; (ii)
south side; (iii) east side; (iv) west side.

❙
