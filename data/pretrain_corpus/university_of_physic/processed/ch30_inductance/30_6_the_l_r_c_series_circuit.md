the left-hand plate of the capacitor) and the current i to be negative
as well (that is, current will ﬂow counterclockwise).

To ﬁnd the value of q, we use Eq. (30.21),

The charge is maximum at
so
10-6 F21300 V2 = 7.5 * 10-3 C.

t = 0,

q = Q cos1vt + f2
.
Q = CE = 125 *
and

f = 0
Hence Eq. (30.21) becomes

q = 17.5 * 10-3 C2 cos vt

30.5 The L-R-C Series Circuit

1009

vt = 12.0 * 103 rad>s211.2 * 10-3 s2 = 2.4 rad
q = 17.5 * 10-3 C2 cos12.4 rad2 = - 5.5 * 10-3 C

From Eq. (30.23), the current i at any time is
t = 1.2 * 10-3 s,
i = - 12.0 * 103 rad>s217.5 * 10-3 C2 sin12.4 rad2 = - 10 A

i = - vQ sin vt

. At

At time t = 1.2 * 10-3 s,

EVALUATE: The signs of q and i are both negative, as predicted.

Example 30.9

Energy in an oscillating circuit

For the L-C circuit of Example 30.8, ﬁnd the magnetic and electric
energies (a) at

t = 1.2 ms.

and (b) at

t = 0

SOLUTION

UE

IDENTIFY and SET UP: We must calculate the magnetic energy
UB
(stored  in  the
(stored  in  the  inductor)  and  the  electric  energy
capacitor)  at  two  times  during  the  L-C circuit  oscillation.  From
Example 30.8 we know the values of the capacitor charge q and cir-
2 Li 2
cuit current i for both times. We use them to calculate
and

UE = q 2>2C.
EXECUTE: (a) At
Hence there
is  no  magnetic  energy,  and  all  the  energy  in  the  circuit  is  in  the
form of electric energy in the capacitor:

there is no current and

UB = 1

q = Q.

t = 0

(b) From Example 30.8, at t (cid:3) 1.2 ms we have

i = - 10 A

and

. Hence

q = - 5.5 * 10-3 C
2 Li 2 = 1
UB = 1
q 2
2C

UE =

=

110 * 10-3 H21 -10 A22 = 0.5 J

2
1-5.5 * 10-3 C22
2125 * 10-6 F2

= 0.6 J

EVALUATE:  The  magnetic  and  electric  energies  are  the  same  at
t = 3T>8 = 0.375T,
halfway between the situations in Figs. 30.14b
and 30.14c. We saw in Example 30.8 that the time considered in
part (b), t (cid:3) 1.2 ms, equals 0.38T; this is slightly later than 0.375T,
E =
so
UB
UB + UE
has the same value, 1.1 J. An L-C circuit without resist-
ance is a conservative system; no energy is dissipated.

. At  all times  the  total energy

is  slightly  less  than

UE

UB = 1

2 Li 2 = 0  UE =

Q2
2C

=

17.5 * 10-3 C22
2125 * 10-6 F2

= 1.1 J

Test Your Understanding of Section 30.5 One way to think about the energy
stored in an L-C circuit is to say that the circuit elements do positive or negative work on
the charges that move back and forth through the circuit. (a) Between stages (a) and
(b) in Fig. 30.14, does the capacitor do positive work or negative work on the charges?
(b) What kind of force (electric or magnetic) does the capacitor exert on the charges to do
this work? (c) During this process, does the inductor do positive or negative work on the
charges? (d) What kind of force (electric or magnetic) does the inductor exert on the
charges?

❙

30.6 The L-R-C Series Circuit

In our discussion of the L-C circuit we assumed that there was no resistance in
the circuit. This is an idealization, of course; every real inductor has resistance in
its windings, and there may also be resistance in the connecting wires. Because
of  resistance,  the  electromagnetic  energy  in  the  circuit  is  dissipated  and  con-
verted to other forms, such as internal energy of the circuit materials. Resistance
in an electric circuit is analogous to friction in a mechanical system.

ActivPhysics 14.2: AC Circuits: The RLC
Oscillator (Questions 7–10)

Suppose an inductor with inductance  and a resistor of resistance

L
are con-
nected  in  series  across  the  terminals  of  a  charged  capacitor,  forming  an  L-R-C
series circuit. As before, the capacitor starts to discharge as soon as the circuit is
completed.  But  because  of
losses  in  the  resistor,  the  magnetic-ﬁeld  energy
acquired by the inductor when the capacitor is completely discharged is less than
the  original  electric-ﬁeld  energy  of  the  capacitor.  In  the  same  way,  the  energy
of the capacitor when the magnetic ﬁeld has decreased to zero is still smaller, and
so on.

i 2R

R

If  the  resistance

is  relatively  small,  the  circuit  still  oscillates,  but  with
damped  harmonic  motion (Fig.  30.16a),  and  we  say  that  the  circuit  is

R

1010

CHAPTER 30 Inductance

30.16 Graphs of capacitor charge as a
function of time in an L-R-C series circuit
with initial charge Q.

(a) Underdamped circuit (small resistance R)

q

Q

O

R,

the oscillations die out more rapidly. When

R
underdamped. If we increase
reaches a certain value, the circuit no longer oscillates; it is critically damped
(Fig.  30.16b).  For  still  larger  values  of
the  circuit  is  overdamped (Fig.
30.16c),  and  the  capacitor  charge  approaches  zero  even  more  slowly. We  used
these same terms to describe the behavior of the analogous mechanical system,
the damped harmonic oscillator, in Section 14.7.

R,

Analyzing an L-R-C Series Circuit
To analyze L-R-C series circuit behavior in detail, we consider the circuit shown
in Fig. 30.17. It is like the L-C circuit of Fig. 30.15 except for the added resistor
R;
we also show the source that charges the capacitor initially. The labeling of the
positive senses of q and i are the same as for the L-C circuit.

t

(b) Critically damped circuit (larger resistance R)

t

t

q

Q

O

(c) Overdamped circuit (very large resistance R)

q

Q

O

30.17 An L-R-C series circuit.

When switch S is in this position,
the emf charges the capacitor.

E

+

C

+q

–q

d

R

c

L

i

S
a

b

When switch S is moved to this
position, the capacitor discharges
through the resistor and inductor.

E

First we close the switch in the upward position, connecting the capacitor to a
for a long enough time to ensure that the capacitor acquires its
source of emf
and  any  initial  oscillations  have  died  out.  Then  at  time
ﬁnal  charge
t = 0
we ﬂip the switch to the downward position, removing the source from the
circuit and placing the capacitor in series with the resistor and inductor. Note that
the initial current is negative, opposite to the direction of i shown in Fig. 30.17.

Q = CE

To ﬁnd how q and i vary with time, we apply Kirchhoff’s loop rule. Starting at
point a and going around the loop in the direction abcda, we obtain the equation

-iR - L

-

di
dt

q
C

= 0

Replacing i with

dq>dt

and rearranging, we get

d 2q
dt 2

+ R
L

dq
dt

+ 1
LC

q = 0

(30.27)

Note that when

R = 0,

this reduces to Eq. (30.20) for an L-C circuit.

There are general methods for obtaining solutions of Eq. (30.27). The form of
R)

and overdamped (large

the solution is different for the underdamped (small
cases. When

is less than

the solution has the form

4L>C,

R2

R)

q = Ae-1R>2L2t cos a

1
LC

B

- R2

4L2 t + fb

(30.28)

f

A

and

are constants. We invite you to take the ﬁrst and second deriva-
where
tives  of  this  function  and  show  by  direct  substitution  that  it  does  satisfy
Eq. (30.27).

This solution corresponds to the underdamped behavior shown in Fig. 30.16a;
the  function  represents  a  sinusoidal  oscillation  with  an  exponentially  decaying
amplitude. (Note that the exponential factor
is not the same as the factor
e-1R>L2t
that we encountered in describing the R-L circuit in Section 30.4.) When
R = 0,
Eq. (30.28) reduces to Eq. (30.21) for the oscillations in an L-C circuit. If
1>1LC21>2
R
because of the term containing  The angular frequency
of the damped oscil-
lations is given by

is  not  zero,  the  angular  frequency  of  the  oscillation  is  less than

e-1R>2L2t

v¿

R.

v¿ =

1
LC

B

- R2
4L2

    1underdamped L-R-C series circuit)

(30.29)

R = 0,

v = 11>LC21>2.

this  reduces  to  Eq.  (30.22),

v¿
R
When
the quantity under the radical
becomes smaller and smaller. When
becomes zero; the system no longer oscillates, and the case of critical damping
(Fig. 30.16b) has been reached. For still larger values of
the system behaves as
in Fig. 30.16c. In this case the circuit is overdamped, and q is given as a function
of time by the sum of two decreasing exponential functions.

R2 = 4L>C,

increases,

As

R

In  the  underdamped case  the  phase  constant

in  the  cosine  function  of
Eq. (30.28) provides for the possibility of both an initial charge and an initial cur-
rent at time
analogous to an underdamped harmonic oscillator given both
an initial displacement and an initial velocity (see Exercise 30.40).

t = 0,

f

We emphasize once more that the behavior of the L-R-C series circuit is com-
pletely  analogous  to  that  of  the  damped  harmonic  oscillator  studied  in  Section
14.7. We invite you to verify, for example, that if you start with Eq. (14.41) and
substitute q for x,
for the damping constant b, the result
is Eq. (30.27). Similarly, the cross-over point between underdamping and over-
damping occurs at
for
for the mechanical system and at
the electrical one. Can you ﬁnd still other aspects of this analogy?

R2 = 4L>C

b 2 = 4km

for k, and

for m,

1>C

R

L

The practical applications of the L-R-C series circuit emerge when we include
a sinusoidally varying source of emf in the circuit. This is analogous to the forced
oscillations that we discussed in Section 14.7, and there are analogous resonance
effects. Such a circuit is called an alternating-current (ac) circuit; the analysis of
ac circuits is the principal topic of the next chapter.

Example 30.10

An underdamped L-R-C series circuit

What resistance
to give an L-R-C
is required (in terms of  and
series circuit a frequency that is one-half the undamped frequency?

C )

R

L

30.5 The L-R-C Series Circuit

1011

1
LC

B

- R2
4L2

= 1

2A

1
LC

SOLUTION

We square both sides and solve for

R:

IDENTIFY  and SET  UP:  This  problem  concerns  an  underdamped
L-R-C series circuit (Fig. 30.16a). We want just enough resistance
to  reduce  the  oscillation  frequency  to  one-half  of  the  undamped
value.  Equation  (30.29)  gives  the  angular  frequency
of  an
underdamped L-R-C series  circuit;  Eq.  (30.22) gives  the  angular
frequency
of an undamped L-C circuit. We use these two equa-
tions to solve for

v¿

R.

v

EXECUTE: From  Eqs.  (30.29) and  (30.22),  the  requirement
v¿ = v>2

yields

R =

3L
C

A

For  example,  adding
1L = 10
mH, C
320 Hz to 160 Hz.

35 Æ
= 25 mF2

to  the  circuit  of  Example  30.8
would  reduce  the  frequency  from

EVALUATE: The circuit becomes critically damped with no oscilla-
is smaller than that, as it
Our result for
tions when
should be; we want the circuit to be underdamped.

R = 24L>C.

R

2.0-Æ

resistor. At

Test Your Understanding of Section 30.6 An L-R-C series circuit
includes a
For which of
the following values of the inductance and capacitance will the charge on the
capacitor not oscillate? (i)
(iii)

the capacitor charge is

L = 6.0 mH,

L = 3.0 mH,

L = 3.0 mH,

C = 6.0 mF;

C = 3.0 mF.

2.0 mC.

t = 0

(ii)

C = 3.0 mF;

❙
