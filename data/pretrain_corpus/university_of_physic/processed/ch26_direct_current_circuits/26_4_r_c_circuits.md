864

CHAPTER 26 Direct-Current Circuits

26.18 This digital multimeter can be
used as a voltmeter (red arc), ammeter
(yellow arc), or ohmmeter (green arc).

26.19 A potentiometer.

(a) Potentiometer circuit

I

a

c

E
1

+

I

I

I

b

(cid:2) 0

I2

G

rG

+

E

2, r

(b) Circuit symbol
for potentiometer
(variable resistor)

The principle of the potentiometer is shown schematically in Fig. 26.19a. A
Rab
resistance wire ab of total resistance
is permanently connected to the ter-
E1.
minals of a source of known emf
A sliding contact c is connected through
the  galvanometer  G  to  a  second  source  whose  emf
is  to  be  measured. As
contact c is moved along the resistance wire, the resistance
between points
c and b varies;  if  the  resistance  wire  is  uniform,
is  proportional  to  the
contact  c is
length  of  wire  between  c and b.  To  determine  the  value  of
moved until a position is found at which the galvanometer shows no deflection;
this corresponds to zero current passing through  With
Kirchhoff’s
loop rule gives

I2 = 0,

E2.

E2,

Rcb

Rcb

E2

I2 = 0,

E2 = IRcb
the current I produced by the emf
E2.

E1

With
what  the  value  of  the  emf  We  calibrate  the  device  by  replacing
source of known emf; then any unknown emf
length of wire cb for which
than

has the same value no matter
by  a
can be found by measuring the
. Note that for this to work,  must be greater

I2 = 0

Vab

E2

E2

E2.

The term potentiometer is also used for any variable resistor, usually having a
circular resistance element and a sliding contact controlled by a rotating shaft and
knob. The circuit symbol for a potentiometer is shown in Fig. 26.19b.

2-Æ

resistor shown in

resistor; (ii) ammeter in series with the

Test Your Understanding of Section 26.3 You want to measure the
current through and the potential difference across the
Fig. 26.12 (Example 26.6 in Section 26.2). (a) How should you connect an
ammeter and a voltmeter to do this? (i) ammeter and voltmeter both in series with the
2-Æ
between points b and d; (iii) ammeter connected between points b and d and voltmeter
in series with the
points b and d. (b) What resistances should these meters have? (i) Ammeter and volt-
meter resistances should both be much greater than
2 Æ
be much greater than
ammeter resistance should be much less than
much greater than
less than

and voltmeter resistance should be
(iv) ammeter and voltmeter resistances should both be much

resistor; (iv) ammeter and voltmeter both connected between

(ii) ammeter resistance should
(iii)

and voltmeter resistance should be much less than

resistor and voltmeter connected

2 Æ;

2 Æ;

2 Æ;

2 Æ.

2-Æ

2-Æ

2 Æ

❙

26.4 R-C Circuits

In the circuits we have analyzed up to this point, we have assumed that all the
emfs  and  resistances  are  constant (time  independent)  so  that  all  the  potentials,
currents, and powers are also independent of time. But in the simple act of charg-
ing or discharging a capacitor we ﬁnd a situation in which the currents, voltages,
and powers do change with time.

Many devices incorporate circuits in which a capacitor is alternately charged
and discharged. These include ﬂashing trafﬁc lights, automobile turn signals, and
electronic  ﬂash  units.  Understanding  what  happens  in  such  circuits  is  thus  of
great practical importance.

Charging a Capacitor
Figure 26.20 shows a simple circuit for charging a capacitor. A circuit such as this
that has a resistor and a capacitor in series is called an R-C circuit. We idealize
the battery (or power supply) to have a constant emf
and zero internal resist-
ance

and we neglect the resistance of all the connecting conductors.

1r = 02,

E

t = 0

We  begin  with  the  capacitor  initially  uncharged  (Fig.  26.20a);  then  at  some
initial time
we close the switch, completing the circuit and permitting cur-
rent around the loop to begin charging the capacitor (Fig. 26.20b). For all practi-
cal purposes, the current begins at the same instant in every conducting part of
the circuit, and at each instant the current is the same in every part.

CAUTION Lowercase means time-varying Up to this point we have been working with
constant potential differences (voltages), currents, and charges, and we have used capital
letters V, I, and Q, respectively, to denote these quantities. To distinguish between quanti-
ties that vary with time and those that are constant, we will use lowercase letters
i, and q
for time-varying voltages, currents, and charges, respectively. We suggest that you follow
this same convention in your own work. ❙

v,

26.20 Charging a capacitor. (a) Just
before the switch is closed, the charge q is
t = 0
zero. (b) When the switch closes (at
E>R.
As
the current jumps from zero to
and the
time passes, q approaches
current i approaches zero.

Qf

),

26.4 R-C Circuits

865

across it is zero at
vab

Because the capacitor in Fig. 26.20 is initially uncharged, the potential differ-
At this time, from Kirchhoff’s loop law, the
1t = 02
is  given  by  Ohm’s  law:

vbc
ence
voltage
current  through  the  resistor,  which  we  will  call
I0 = vab>R = E>R.

across the resistor R is equal to the battery emf  The initial

t = 0.

I0,

E.

vbc
As the capacitor charges, its voltage
increases and the potential difference
vab
across the resistor decreases, corresponding to a decrease in current. The sum
of these two voltages is constant and equal to  After a long time the capacitor
becomes fully charged, the current decreases to zero, and the potential difference
vab
across the resistor becomes zero. Then the entire battery emf  appears across
the capacitor and

E.

E

vbc = E.

Let q represent the charge on the capacitor and i the current in the circuit at
some time t after the switch has been closed. We choose the positive direction
for  the  current  to  correspond  to  positive  charge  flowing  onto  the  left-hand
vab
capacitor plate, as in Fig. 26.20b. The instantaneous potential differences
and

are

vbc

vab = iR    vbc =

q
C

Using these in Kirchhoff’s loop rule, we ﬁnd

E - iR -

q
C

= 0

The potential drops by an amount iR as we travel from a to b and by
travel from b to c. Solving Eq. (26.9) for i, we ﬁnd

i =

E

R

-

q
RC

(26.9)

q>C

as we

(26.10)

t = 0,
Substituting
I0 = E>R,

At time
when the switch is ﬁrst closed, the capacitor is uncharged, and so
q = 0.
q = 0
is
as we have already noted. If the capacitor were not in the cir-
given by
cuit, the last term in Eq. (26.10) would not be present; then the current would be
constant and equal to

into Eq. (26.10), we ﬁnd that the initial current

E>R.

I0

As  the  charge  q increases,  the  term

q>RC

charge approaches its ﬁnal value, which we will call
and eventually becomes zero. When

Eq. (26.10) gives

Qf.

becomes  larger  and  the  capacitor
The current decreases

i = 0,
    Qf = CE

E

R

=

Qf
RC

(a) Capacitor initially uncharged

Switch
open

E

+

i 5 0

q 5 0

a

R

b

c

C

(b) Charging the capacitor

E

+

Switch
closed

i

1q 2q

b

c

C

i

R

a

When the switch is
closed, the charge
on the capacitor
increases over
time while the
current decreases.

26.21 Current i and capacitor charge q
as functions of time for the circuit of Fig.
26.20. The initial current is
and the ini-
tial capacitor charge is zero. The current
asymptotically approaches zero, and the
capacitor charge asymptotically approaches
a ﬁnal value of Qf.

I0

(a) Graph of current versus time for a charging
capacitor
i

I0

I0/2
I0/e

O

The current decreases
      exponentially with time as
             the capacitor charges.

RC

t

(26.11)

(b) Graph of capacitor charge versus time for a
charging capacitor
q

Note that the ﬁnal charge

Qf

does not depend on R.

Figure 26.21 shows the current and capacitor charge as functions of time. At
the current jumps from zero to its initial
the instant the switch is closed
value
after  that,  it  gradually  approaches  zero.  The  capacitor  charge
starts  at  zero  and  gradually  approaches  the  ﬁnal  value  given  by  Eq.  (26.11),
Qf = CE.

I0 = E>R;

1t = 02,

Qf

Qf/2

Qf/e

We can derive general expressions for the charge q and current i as functions
of  time.  With  our  choice  of  the  positive  direction  for  current  (Fig.  26.20b),
i equals  the  rate  at  which  positive  charge  arrives  at  the  left-hand  (positive)

O

RC

The charge on the
capacitor increases
exponentially with
time toward the
final value Qf.
t

866

CHAPTER 26 Direct-Current Circuits

plate  of  the  capacitor,  so
we have

i = dq>dt.

Making  this  substitution  in  Eq.  (26.10),

We can rearrange this to

dq
dt

=

E

R

-

q
RC

= - 1
RC

1q - CE2

dq
q - CE

= - dt
RC

and  then  integrate  both  sides. We  change  the  integration  variables  to
so that we can use q and t for the upper limits. The lower limits are
t¿ = 0:

q¿
q¿ = 0

and

t¿
and

q

dq¿
q¿ - CE

L
0

= -

t

dt¿
RC

L
0

When we carry out the integration, we get

ln a

q - CE
-CE

b = - t
RC

Exponentiating both sides (that is, taking the inverse logarithm) and solving for
q, we ﬁnd

q - CE
-CE

= e-t/RC

q = CE11 - e-t/RC2 = Qf11 - e-t/RC2

(R-C circuit, charging
capacitor)

(26.12)

The instantaneous current i is just the time derivative of Eq. (26.12):

i =

dq
dt

=

E

R

e-t/RC = I0e-t/RC

(R-C circuit, charging
capacitor)

(26.13)

The charge and current are both exponential functions of time. Figure 26.21a is a
graph of Eq. (26.13) and Fig. 26.21b is a graph of Eq. (26.12).

Time Constant
1>e
After  a  time  equal  to  RC,  the  current  in  the  R-C circuit  has  decreased  to
(about 0.368) of its initial value. At this time, the capacitor charge has reached
11 - 1>e2 = 0.632
The  product  RC is  therefore  a
measure of how quickly the capacitor charges. We call RC the time constant, or
the relaxation time, of the circuit, denoted by

of  its  ﬁnal  value

Qf = CE.

t:

t = RC    (time constant for R-C circuit)

(26.14)

t

is  small,  the  capacitor  charges  quickly;  when  it  is  larger,  the  charging
When
takes more time. If the resistance is small, it’s easier for current to ﬂow, and the
capacitor charges more quickly. If R is in ohms and C in farads,

is in seconds.

t

In Fig. 26.21a the horizontal axis is an asymptote for the curve. Strictly speak-
ing, i never becomes exactly zero. But the longer we wait, the closer it gets. After
a time equal to 10RC, the current has decreased to 0.000045 of its initial value.
Similarly, the curve in Fig. 26.21b approaches the horizontal dashed line labeled
Qf
as an asymptote. The charge q never attains exactly this value, but after a time
equal to 10RC, the difference between q and
is only 0.000045 of  We invite
you to verify that the product RC has units of time.

Qf.

Qf

PhET: Circuit Construction Kit (AC+DC)
PhET: Circuit Construction Kit (DC Only)
ActivPhysics 12.6: Capacitance
ActivPhysics 12.7: Series and Parallel
Capacitors
ActivPhysics 12.8: Circuit Time Constants

Application Pacemakers
and Capacitors
This x-ray image shows a pacemaker
implanted in a patient with a malfunctioning
sinoatrial node, the part of the heart that gen-
erates the electrical signal to trigger heart-
beats. The pacemaker circuit contains a
battery, a capacitor, and a computer-controlled
switch. To maintain regular beating, once per
second the switch discharges the capacitor
and sends an electrical pulse along the lead to
the heart. The switch then ﬂips to allow the
capacitor to recharge for the next pulse.

Pacemaker

Electrical lead

Lung

Lung

Heart

Discharging a Capacitor
we
Now suppose that after the capacitor in Fig. 26.21b has acquired a charge
remove the battery from our R-C circuit and connect points a and c to an open
switch (Fig. 26.22a). We then close the switch and at the same instant reset our
stopwatch to
The capacitor then discharges through
at that time,
the resistor, and its charge eventually decreases to zero.

q = Q0.

t = 0;

Q0,

Again let i and q represent the time-varying current and charge at some instant
after the connection is made. In Fig. 26.22b we make the same choice of the pos-
itive direction for current as in Fig. 26.20b. Then Kirchhoff’s loop rule gives Eq.
(26.10) but with

E = 0;

that is,

i =

dq
dt

= -

q
RC

(26.15)

The current i is now negative; this is because positive charge q is leaving the left-
hand capacitor plate in Fig. 26.22b, so the current is in the direction opposite to
t = 0,
that  shown  in  the  ﬁgure.  At  time
the  initial  current  is
I0 = - Q0>RC.

q = Q0,

when

To  ﬁnd  q as  a  function  of  time,  we  rearrange  Eq.  (26.15),  again  change  the
are

and integrate. This time the limits for

and

t¿,

q¿

q¿

names of the variables to
Q0

to q. We get

26.4 R-C Circuits

867

Q0

26.22 Discharging a capacitor.
(a) Before the switch is closed at time
t = 0,
the capacitor charge is
current is zero. (b) At time t after the
switch is closed, the capacitor charge is
q and the current is i. The actual current
direction is opposite to the direction
shown; i is negative. After a long time,
q and i both approach zero.

and the

(a) Capacitor initially charged

Switch
open

i (cid:2) 0

+Q0 –Q0

a

R

b

c

C

(b) Discharging the capacitor

q

L
Q0

dq¿
q¿

= - 1

RC L
0

t

dt¿

 ln

q
Q0

= - t
RC

q = Q0e-t/RC    (R-C circuit, discharging capacitor)

(26.16)

a

Switch
closed

i

i

R

+q –q

b

c

C

When the switch is
closed, the charge
on the capacitor
and the current
both decrease
over time.

The instantaneous current i is the derivative of this with respect to time:

i =

dq
dt

= -

Q0
RC

e-t/RC = I0e-t/RC

(R-C circuit,
discharging capacitor)

(26.17)

We graph the current and the charge in Fig. 26.23; both quantities approach zero
exponentially with time. Comparing these results with Eqs. (26.12) and (26.13),
we note that the expressions for the current are identical, apart from the sign of
I0.
The capacitor charge approaches zero asymptotically in Eq. (26.16), while the
difference between q and Q approaches zero asymptotically in Eq. (26.12).

Energy considerations give us additional insight into the behavior of an R-C
circuit. While the capacitor is charging, the instantaneous rate at which the bat-
P = Ei.
The instantaneous rate at which elec-
tery delivers energy to the circuit is
i 2R
trical energy is dissipated in the resistor is
, and the rate at which energy is
stored in the capacitor is

Multiplying Eq. (26.9) by i, we ﬁnd

ivbc = iq>C.

Ei = i 2R +

iq
C

(26.18)

1i 2R2

is dissipated

supplied by the battery, part

This means that of the power
1iq>C2
in the resistor and part

Ei
is stored in the capacitor.
The total energy  supplied  by  the  battery  during  charging  of  the  capacitor
E
equals  the  battery  emf  multiplied  by  the  total  charge
The  total
Qf E>2.
energy  stored  in  the  capacitor,  from  Eq.  (24.9),  is
Thus,  of  the  energy
supplied by the battery, exactly half is stored in the capacitor, and the other half is
dissipated in the resistor. This half-and-half division of energy doesn’t depend on
C, R, or  You can verify this result by taking the integral over time of each of
the power quantities in Eq. (26.18) (see Problem 26.88).

EQf.

Qf,

or

E.

26.23 Current i and capacitor charge
q as functions of time for the circuit of
Fig. 26.22. The initial current is
initial capacitor charge is
q asymptotically approach zero.

Both i and

Q0.

I0

and the

(a) Graph of current versus time for a
discharging capacitor

i

O

I0/e
I0/2

I0

RC

t

The current
decreases exponen-
tially as the capacitor
discharges. (The current is
negative because its direction
is opposite to that in Fig. 26.22.)

(b) Graph of capacitor charge versus time
for a discharging capacitor

q

Q0

Q0/2
Q0/e

O

The charge on the capacitor
       decreases exponentially as the
                capacitor discharges.

RC

t
