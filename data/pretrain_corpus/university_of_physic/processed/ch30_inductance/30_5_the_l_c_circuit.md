Example 30.7

Energy in an R-L circuit

When the current in an R-L circuit is decaying, what fraction of the
original energy stored in the inductor has been dissipated after 2.3
time constants?

SOLUTION

IDENTIFY and SET UP: This problem concerns current decay in an
R-L circuit  as  well  as  the  relationship  between  the  current  in  an
inductor and the amount of stored energy. The current  at any time
is  given  by  Eq.  (30.18);  the  stored  energy  associated  with  this
t
U = 1
current is given by Eq. (30.9),

i

EXECUTE: From Eq. (30.18), the current  at any time  is

t

2 Li 2.
i

i = I0e-1R>L2t
2 Li 2

U = 1

We  substitute  this  into
stored energy at any time:
2 LI 2

U = 1

0 e-21R>L2t = U0e-21R>L2t

to  obtain  an  expression  for  the

30.5 The L-C Circuit

1005

U0 = 1
2 LI 2
where
0
t = 2.3t = 2.3L>R,

is  the  energy  at  the  initial  time
we have

t = 0.

When

U = U0e-212.32 = U0e-4.6 = 0.010U0
That  is,  only  0.010  or  1.0%  of  the  energy  initially  stored  in  the
inductor remains, so 99.0% has been dissipated in the resistor.

and

L = 69 mH

is  dissipated  in

t
U0 = 1
we  have
Of  this,  99.0%  or

EVALUATE:  To get a sense of what this result means, consider the
= 390 ms.
R-L circuit we analyzed in Example 30.6, for which
I0 = 36 mA,
0 =
2 LI 2
With
10.069 H210.036 A22 = 4.5 * 10-5 J.
1
4.4 *
2
10-5 J
s = 0.90 ms.
In other words, this circuit can be almost completely powered off
(or powered on) in 0.90 ms, so the minimum time for a complete
on–off cycle is 1.8 ms. Even shorter cycle times are required for
many purposes, such as in fast switching networks for telecom-
munications.  In  such  cases  a  smaller  time  constant
is
needed.

2.31390 ms2 = 9.0 * 10-4

t = L>R

Test Your Understanding of Section 30.4 (a) In Fig. 30.11, what are the
is closed and
algebraic signs of the potential differences
switch
(iv)
and
closed, and current is ﬂowing in the direction shown? (i)
(ii)

when switch
vbc 6 0;
(iii)
vbc
when
S1
vab 7 0,
vbc 7 0;

vab 7 0,
vbc 7 0;
(b) What are the signs of

S1
vab 6 0,
is open,

vbc
and
vab 7 0,
vab

is open? (i)
vbc 6 0.

S2
vab 6 0,

vab
(ii)

vbc 7 0;
is
S2

(iii)

(iv)

vab 6 0,

vab 7 0,

vab 6 0,

vbc 6 0;

vbc 7 0;

vbc 6 0.

❙

30.5 The L-C Circuit

A circuit containing an inductor and a capacitor shows an entirely new mode of
behavior, characterized by oscillating current and charge. This is in sharp con-
trast  to  the  exponential approach  to  a  steady-state  situation  that  we  have  seen
with both R-C and R-L circuits. In the L-C circuit in Fig. 30.14a we charge the
capacitor to a potential difference
on its left-hand
plate and then close the switch. What happens?

and initial charge

Q = CVm

Vm

ActivPhysics 14.2: AC Circuits: The RLC
Oscillator (Questions 1–6)

The  capacitor  begins  to  discharge  through  the  inductor.  Because  of  the
induced emf in the inductor, the current cannot change instantaneously; it starts at
zero and eventually builds up to a maximum value
During this buildup the
capacitor  is  discharging.  At  each  instant  the  capacitor  potential  equals  the
induced  emf,  so  as  the  capacitor  discharges,  the  rate  of  change of  current
decreases. When  the  capacitor  potential  becomes  zero,  the  induced  emf  is  also
zero,  and  the  current  has  leveled  off  at  its  maximum  value
Figure  30.14b
shows this situation; the capacitor has completely discharged. The potential dif-
ference between its terminals (and those of the inductor) has decreased to zero,
and the current has reached its maximum value

Im.

Im.

Im.

During  the  discharge  of  the  capacitor,  the  increasing  current  in  the  inductor
has established a magnetic ﬁeld in the space around it, and the energy that was
initially  stored  in  the  capacitor’s  electric  ﬁeld  is  now  stored  in  the  inductor’s
magnetic ﬁeld.

Although  the  capacitor  is  completely  discharged  in  Fig.  30.14b,  the  current
persists  (it  cannot  change  instantaneously),  and  the  capacitor  begins  to  charge
with  polarity  opposite  to  that  in  the  initial  state. As  the  current  decreases,  the
magnetic ﬁeld also decreases, inducing an emf in the inductor in the same direc-
tion as the current; this slows down the decrease of the current. Eventually, the

1006

CHAPTER 30 Inductance

30.14 In an oscillating L-C circuit, the charge on the capacitor and the current through the inductor both vary sinusoidally with time.
Energy is transferred between magnetic energy in the inductor
motion, the total energy

remains constant. (Compare Fig. 14.14 in Section 14.3.)

and electric energy in the capacitor

As in simple harmonic

1UE2.

1UB2

E

Capacitor polarity reverses.

Current direction reverses.

Capacitor fully charged;
zero current
Vm

Capacitor fully
discharged;
current maximal

Capacitor fully charged;
zero current
–Vm

Capacitor fully
discharged;
current maximal

+Qm

+
+
+
+
+
+
+

Em

C
L

z
e
r
o

E 5 UB

1 UE

Circuit’s energy all
stored in electric field

(a) t 5 0 and t 5 T
(close switch at t 5 0)

–Qm

Capacitor
discharging;
I increasing

–Qm

Capacitor
charging;
I decreasing

+Qm

+
+
+
+
+
+
+

Capacitor
discharging;
I increasing

Im

Bm

Im

z
e
r
o

E 5 UB

1 UE

Circuit’s energy all
stored in magnetic field

(b) t 5 T

1
4

Em

z
e
r
o

E 5 UB

1 UE

Circuit’s energy all
stored in electric field

(c) t 5 T

1
2

Im

Bm

Im

z
e
r
o

E 5 UB

1 UE

Circuit’s energy all
stored in magnetic field

(d) t 5 T

3
4

Capacitor charging; I decreasing

current and the magnetic ﬁeld reach zero, and the capacitor has been charged in
the  sense  opposite to  its  initial  polarity  (Fig.  30.14c),  with  potential  difference
-Vm

on its left-hand plate.

and charge

-Q

The  process  now  repeats  in  the  reverse  direction;  a  little  later,  the  capacitor
has again discharged, and there is a current in the inductor in the opposite direc-
tion  (Fig.  30.14d).  Still  later,  the  capacitor  charge  returns  to  its  original  value
(Fig.  30.14a),  and  the  whole  process  repeats.  If  there  are  no  energy  losses,  the
charges  on  the  capacitor  continue  to  oscillate  back  and  forth  indeﬁnitely.  This
process is called an electrical oscillation.

From  an  energy  standpoint  the  oscillations  of  an  electrical  circuit  transfer
energy  from  the  capacitor’s  electric  ﬁeld  to  the  inductor’s  magnetic  ﬁeld  and
back. The total energy associated with the circuit is constant. This is analogous to
the transfer of energy in an oscillating mechanical system from potential energy
to kinetic energy and back, with constant total energy. As we will see, this anal-
ogy goes much further.

Electrical Oscillations in an L-C Circuit
To study the ﬂow of charge in detail, we proceed just as we did for the R-L cir-
cuit. Figure 30.15 shows our deﬁnitions of q and i.

CAUTION Positive current in an L-C circuit After  examining  Fig.  30.14,  the  positive
direction  for  current  in  Fig.  30.15 may  seem  backward  to  you.  In  fact  we’ve  chosen
this  direction  to  simplify  the  relationship  between  current  and  capacitor  charge.  We
define the current at each instant to be
the rate of change of the charge on
the left-hand capacitor plate. Hence if the capacitor is initially charged and begins to
discharge as in Figs. 30.14a and 30.14b, then
and the initial current i is neg-
ative; the direction of the current is then opposite to the (positive) direction shown in
Fig. 30.15. ❙

dq>dt 6 0

i = dq>dt,

30.15 Applying Kirchhoff’s loop rule to
the L-C circuit. The direction of travel
around the loop in the loop equation is
shown. Just after the circuit is completed
and the capacitor ﬁrst begins to discharge,
as in Fig. 30.14a, the current is negative
(opposite to the direction shown).

C

+q

–q

Travel

i

L

We  apply  Kirchhoff’s  loop  rule  to  the  circuit  in  Fig.  30.15.  Starting  at  the
lower-right corner of the circuit and adding voltages as we go clockwise around
the loop, we obtain

30.5 The L-C Circuit

1007

i = dq>dt,

Since
into the above equation and divide by

it follows that

-L

-

di
dt

= 0

q
C
di>dt = d 2q>dt 2.
to obtain

-L

We substitute this expression

d 2q
dt 2

+ 1
LC

q = 0    1L-C circuit2

(30.20)

Equation  (30.20) has  exactly  the  same  form  as  the  equation  we  derived  for
d 2x>dt 2 =

simple harmonic motion in Section 14.2, Eq. (14.4). That equation is
-1k>m2x,

or

d 2x
dt 2

+ k
m

x = 0

(You  should  review  Section  14.2  before  going  on  with  this  discussion.)  In  the
L-C circuit the capacitor charge q plays the role of the displacement x, and the
current
The induc-
1>C,
tance
is
L
analogous to the force constant k.

i = dq>dt
is analogous to the mass m, and the reciprocal of the capacitance,

is analogous to the particle’s velocity

vx = dx>dt.

Pursuing  this  analogy,  we  recall  that  the  angular  frequency
1k>m21>2,

of  the
and the position is given as a function of

v = 2pf

harmonic oscillator is equal to
time by Eq. (14.13),

x = A cos1vt + f2

where the amplitude
the analogous electrical situation the capacitor charge q is given by

and the phase angle  depend on the initial conditions. In

A

f

v
and the angular frequency  of oscillation is given by

q = Q cos1vt + f2

v =

1
LC

A

(angular frequency of oscillation
in an L-C circuit)

(30.21)

(30.22)

You should verify that Eq. (30.21) satisﬁes the loop equation, Eq. (30.20), when
v
has the value given by Eq. (30.22). In doing this, you will ﬁnd that the instanta-
neous current

i = dq>dt

is given by

i = - vQ sin1vt + f2

(30.23)

Thus the charge and current in an L-C circuit oscillate sinusoidally with time,
C.
with an angular frequency determined by the values of  and  The ordinary fre-
f,
as always. The con-
quency
Q
in  Eqs.  (30.21) and  (30.23) are  determined  by  the  initial
stants
the left-hand capacitor plate in Fig. 30.15 has its max-
conditions. If at time
Q
imum charge
then
If
f = (cid:2)p>2 rad.

the number of cycles per second, is equal to
and

and the current i is zero, then

L
v>2p

f = 0.

t = 0,

q = 0

at time

t = 0

f

Energy in an L-C Circuit
We can also analyze the L-C circuit using an energy approach. The analogy to
simple harmonic motion is equally useful here. In the mechanical problem a body
with mass m is attached to a spring with force constant k. Suppose we displace
the body a distance
from its equilibrium position and release it from rest at time
t = 0.
and its elastic
Because  the  system  is  conservative,  the  sum  of  these
potential  energy  is

The kinetic energy of the system at any later time is

1
2,
2 mvx

A

1

2 kx 2.

1008

CHAPTER 30 Inductance

Table 30.1 Oscillation of a
Mass-Spring System Compared
with Electrical Oscillation in
an L-C Circuit

2
2 mvx
2 kx 2

Mass-Spring System
Kinetic energy = 1
Potential energy = 1
1
2 kx 2 = 1
2 mvx
vx = (cid:2) 2k>m 2A2 - x 2
vx = dx>dt

2 kA2

2 + 1

v =

k
m
x = A cos1vt + f2

A

Inductor-Capacitor Circuit
Magnetic energy = 1
2 Li 2
Electric energy = q 2>2C
1
2 Li 2 + q 2>2C = Q2>2C
i = (cid:2) 21>LC 2Q2 - q 2
i = dq>dt

v =

1
LC
q = Q cos1vt + f2

A

energies equals the initial energy of the system,
any position x just as we did in Section 14.3, Eq. (14.22):

1

2 kA2.

We ﬁnd the velocity

vx

at

vx = (cid:2)

k
m

A

2A2 - x 2

(30.24)

The L-C circuit is also a conservative system. Again let

capacitor charge. The magnetic-ﬁeld energy
responds to the kinetic energy
energy
the spring. The sum of these energies equals the total energy
tem:

be the maximum
in the inductor at any time cor-
of the oscillating body, and the electric-ﬁeld
2 kx 2
of
of the sys-

in the capacitor corresponds to the elastic potential energy

Q2>2C

q 2>2C

2 mv2

2 Li 2

Q

1

1

1

1

2 Li 2 +

q 2
2C

=

Q2
2C

(30.25)

The total energy in the L-C circuit is constant; it oscillates between the magnetic
and the electric forms, just as the constant total mechanical energy in simple har-
monic motion is constant and oscillates between the kinetic and potential forms.
Solving Eq. (30.25) for i, we ﬁnd that when the charge on the capacitor is q,

the current i is

i = (cid:2)

1
LC

A

2Q2 - q 2

(30.26)

You  can  verify  this  equation  by  substituting  q from  Eq.  (30.21) and  i from
i = dq>dt
Eq. (30.23). Comparing Eqs. (30.24) and (30.26), we see that current
and position
and charge q are related in the same way as are velocity
x in the mechanical problem.

vx = dx>dt

Table  30.1 summarizes  the  analogies  between  simple  harmonic  motion  and
L-C circuit oscillations. The striking parallels shown there are so close that we can
solve complicated mechanical and acoustical problems by setting up analogous
electric circuits and measuring the currents and voltages that correspond to the
mechanical and acoustical quantities to be determined. This is the basic principle
of many analog computers. This analogy can be extended to damped oscillations,
which we consider in the next section. In Chapter 31 we will extend the analogy
further  to  include  forced electrical  oscillations,  which  occur  in  all  alternating-
current circuits.

Example 30.8

An oscillating circuit

25-mF

A 300-V dc power supply is used to charge a
capacitor. After
the  capacitor  is  fully  charged,  it  is  disconnected  from  the  power
supply  and  connected  across  a  10-mH  inductor. The  resistance  in
the circuit is negligible. (a) Find the frequency and period of oscil-
lation  of  the  circuit.  (b)  Find  the  capacitor  charge  and  the  circuit
current 1.2 ms after the inductor and capacitor are connected.

SOLUTION

ƒ

T

L,

and period

IDENTIFY and SET UP: Our target variables are the oscillation fre-
, as well as the charge q and current i at a
quency
particular  time  t. We  are  given  the  capacitance
and  the  induc-
from  which  we  can  calculate  the  frequency  and  period
tance
using  Eq.  (30.22).  We  ﬁnd  the  charge  and  current  using  Eqs.
(30.21) and (30.23). Initially the capacitor is fully charged and the
current is zero, as in Fig. 30.14a, so the phase angle is
[see
the discussion that follows Eq. (30.23)].

f = 0

C

EXECUTE: (a) The natural angular frequency is

v =

1
LC

A

=

1
110 * 10-3 H2125 * 10-6 F2

B

= 2.0 * 103 rad>s

The frequency  and period T are then

ƒ

ƒ =

v
2p
T = 1
ƒ

=

=

2.0 * 103 rad>s
2p rad>cycle
1
320 Hz

= 320 Hz

= 3.1 * 10-3 s = 3.1 ms

equals

(b)  Since  the  period  of  the  oscillation  is

T = 3.1 ms,
t = 1.2 ms
0.38T;
this corresponds to a situation intermedi-
1t = T>42
1t = T>22.
ate  between  Fig.  30.14b
and  Fig.  30.14c
Comparing those ﬁgures with Fig. 30.15, we expect the capacitor
charge q to be negative (that is, there will be negative charge on
