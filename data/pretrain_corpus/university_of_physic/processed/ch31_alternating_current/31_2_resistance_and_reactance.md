1024

CHAPTER 31 Alternating Current

31.5 This wall socket delivers a root-
mean-square voltage of 120 V. Sixty
times per second, the instantaneous
voltage across its terminals varies from
11221120 V2 = 170 V to  -170 V
and
back again.

In the same way, the root-mean-square value of a sinusoidal voltage with ampli-
tude (maximum value)

is

V

Vrms = V
22

    (root-mean-square value of a sinusoidal voltage)

(31.5)

We can convert a rectifying ammeter into a voltmeter by adding a series resistor,
just as for the dc case discussed in Section 26.3. Meters used for ac voltage and cur-
rent measurements are nearly always calibrated to read rms values, not maximum
or rectiﬁed average. Voltages and currents in power distribution systems are always
described  in  terms  of  their  rms  values.  The  usual  household  power  supply,
“120-volt ac,” has an rms voltage of 120 V (Fig. 31.5). The voltage amplitude is

V = 22 Vrms = 22 1120 V2 = 170 V

Example 31.1

Current in a personal computer

The  plate  on  the  back  of  a  personal  computer  says  that  it  draws
2.7 A from a 120-V, 60-Hz line. For this computer, what are (a) the
average current, (b) the average of the square of the current, and
(c) the current amplitude?

SOLUTION

31.6 Our graphs of the current  and the square of the current
versus time t.

i

i 2

IDENTIFY  and SET  UP: This example is about alternating current.
In part (a) we ﬁnd the average, over a complete cycle, of the alter-
nating current. In part (b) we recognize that the 2.7-A current draw
of the computer is the rms value  —that is, the square root of
the mean (average) of the square of the current,
. In part (c)
we use Eq. (31.4) to relate

1i 22av
to the current amplitude.

Irms

Irms

EXECUTE: (a)  The  average  of  any sinusoidally  varying  quantity,
over any whole number of cycles, is zero.

(b)  We  are  given

Irms = 2.7 A

.  From  the  deﬁnition  of  rms

value,

Irms = 21i 22av so 1i 22av = 1Irms22 = 12.7 A22 = 7.3 A2

(c) From Eq. (31.4), the current amplitude

I

is

I = 12Irms = 1212.7 A2 = 3.8 A

Figure 31.6 shows graphs of  and

i

i 2

versus time t.

EVALUATE:  Why  would  we  be  interested  in  the  average  of  the
square of the current? Recall that the rate at which energy is dissi-
i 2R.
This  rate  varies  if  the  current
pated  in  a  resistor
1i 22avR =
is alternating, so it is best described by its average value
I rms

We’ll use this idea in Section 31.4.

equals

2R.

R

B

A

I

I

v

Test Your Understanding of Section 31.1 The ﬁgure at left shows four dif-
ferent current phasors with the same angular frequency  At the time shown, which pha-
sor corresponds to (a) a positive current that is becoming more positive; (b) a positive
current that is decreasing toward zero; (c) a negative current that is becoming more nega-
tive; (d) a negative current that is decreasing in magnitude toward zero?

v.

C

I

I

D

❙

31.2 Resistance and Reactance

In this section we will derive voltage–current relationships for individual circuit
elements  carrying  a  sinusoidal  current.  We’ll  consider  resistors,  inductors,  and
capacitors.

Resistor in an ac Circuit
R
through which there is a sinusoidal
First let’s consider a resistor with resistance
i = I cos vt.
The  positive  direction  of  current  is
current  given  by  Eq.  (31.2):
counterclockwise  around  the  circuit,  as  in  Fig.  31.7a.  The  current  amplitude
(maximum current) is  From Ohm’s law the instantaneous potential
of point
a
(that is, the instantaneous voltage across the resistor) is

I.
with respect to point
b

vR

31.2 Resistance and Reactance

1025

R
31.7 Resistance  connected
across an ac source.

(a) Circuit with ac source and resistor

The maximum voltage
function:

VR,

vR = iR = 1IR2 cos vt
the voltage amplitude, is the coefﬁcient of the cosine

(31.6)

VR = IR    (amplitude of voltage across a resistor, ac circuit)

(31.7)

i

R
vR

b

a

(b) Graphs of current and voltage versus time

Hence we can also write

vR = VR cos vt
are both proportional to

i
The current  and voltage
so the current is in
phase with the voltage. Equation (31.7) shows that the current and voltage ampli-
tudes are related in the same way as in a dc circuit.

vR

cos vt,

i, v

I

VR

O

(31.8)

i 5 I cos vt

vR

5 IR cos vt 5 VR cos vt

i

Figure 31.7b shows graphs of  and

vR
as functions of time. The vertical scales
for current and voltage are different, so the relative heights of the two curves are
not signiﬁcant. The corresponding phasor diagram is given in Fig. 31.7c. Because
are in phase and have the same frequency, the current and voltage pha-
i
sors rotate together; they are parallel at each instant. Their projections on the hor-
izontal axis represent the instantaneous current and voltage, respectively.

and

vR

Amplitudes are in the
same relationship as for
a dc circuit: VR

5 IR.

(c) Phasor diagram

t

Current is in phase
with voltage: crests and
troughs occur together.

Inductor in an ac Circuit
Next, we replace the resistor in Fig. 31.7 with a pure inductor with self-inductance
i =
L
and  zero  resistance  (Fig.  31.8a).  Again  we  assume  that  the  current  is
I cos vt,
with the positive direction of current taken as counterclockwise around
the circuit.

a

b

vL

Although there is no resistance, there is a potential difference

between the
inductor terminals  and  because the current varies with time, giving rise to a
self-induced emf. The induced emf in the direction of
is given by Eq. (30.7),
E = - L di>dt;
vL
To  see  why,
however,  the  voltage
notice  that  if  the  current  in  the  inductor  is  in  the  positive  (counterclockwise)
direction from a to b and is increasing, then
is positive and the induced emf
is directed to the left to oppose the increase in current; hence point a is at higher
potential than is point b. Thus the potential of point a with respect to point b is
the negative of the induced emf. (You
positive and is given by

is  not simply  equal  to

vL = + L di>dt,

di>dt

E.

i

Voltage
phasor

Current
phasor

VR

vR

I

Current and voltage
phasors are in phase:
they rotate together.

vt

i

O

Instantaneous
voltage

Instantaneous
current

31.8 Inductance  connected across an ac source.

L

(a) Circuit with ac source and inductor

(b) Graphs of current and voltage versus time

(c) Phasor diagram

i

L
vL

b

a

i, v

I

VL

O

i 5 I cos vt

5 IvL cos 1vt 1 90°2

vL

Voltage phasor leads current phasor
by f 5 p/2 rad 5 90°.

I

t

Voltage
phasor

Phase
angle f

1
4 T,

p
2
Voltage curve leads current curve by a quarter-
cycle (corresponding to f 5 p/2 rad 5 90°).

rad 5 90°

Current
phasor

i

vt

VL
vL
O

1026

CHAPTER 31 Alternating Current

ActivPhysics 14.3: AC Circuits: The Driven
Oscillator (Questions 1–5)

should  convince  yourself  that  this  expression  gives  the  correct  sign  of
in  all
cases,  including  counterclockwise  and  decreasing,  clockwise  and  increasing,
and  clockwise and decreasing; you should also review Section 30.2.) So we have

vL

i

i

i

vL = L

di
dt

= L

d
dt

1I cos vt2 = - IvL sin vt

(31.9)

vL

across  the  inductor  at  any  instant  is  proportional  to  the  rate  of
The  voltage
change of the current. The points of maximum voltage on the graph correspond
to maximum steepness of the current curve, and the points of zero voltage are the
points  where  the  current  curve  instantaneously  levels  off  at  its  maximum  and
minimum values (Fig. 31.8b). The voltage and current are “out of step” or out of
phase by  a  quarter-cycle.  Since  the  voltage  peaks  occur  a  quarter-cycle  earlier
than the current peaks, we say that the voltage leads the current by
The pha-
sor diagram in Fig. 31.8c also shows this relationship; the voltage phasor is ahead
of the current phasor by

90°.

90°.

We can also obtain this phase relationship by rewriting Eq. (31.9) using the

identity

cos1A + 90°2 = - sin A:

vL = IvL cos1vt + 90°2

(31.10)

This  result  shows  that  the  voltage  can  be  viewed  as  a  cosine  function  with  a
“head start” of

relative to the current.

90°

As  we  have  done  in  Eq.  (31.10),  we  will  usually  describe  the  phase  of  the
voltage relative to the current, not the reverse. Thus if the current  in a circuit is

i

i = I cos vt

and the voltage  of one point with respect to another is

v

v = V cos1vt + f2

f

we  call
current. For a pure resistor,

the  phase  angle; it  gives  the  phase  of  the  voltage relative  to  the

f = 0,

and for a pure inductor,

f = 90°.

From Eq. (31.9) or  (31.10) the amplitude
VL = IvL
XL

We deﬁne the inductive reactance

of an inductor as

XL = vL    (inductive reactance)

VL

of the inductor voltage is

(31.11)

(31.12)

we can write Eq. (31.11) in a form similar to Eq. (31.7) for a resistor

XL,
Using
1VR = IR2:
VL = IXL    (amplitude of voltage across an inductor, ac circuit)

(31.13)

Because
as for resistance.

XL

is the ratio of a voltage and a current, its SI unit is the ohm, the same

CAUTION Inductor voltage and current are not in phase Keep in mind that Eq. (31.13)
is  a  relationship  between  the  amplitudes of  the  oscillating  voltage  and  current  for  the
inductor in Fig. 31.8a. It does not say that the voltage at any instant is equal to the current
at that instant multiplied by  As Fig. 31.8b shows, the voltage and current are
out of
phase. Voltage and current are in phase only for resistors, as in Eq. (31.6). ❙

XL.

90°

XL

The Meaning of Inductive Reactance
The  inductive  reactance
is  really  a  description  of  the  self-induced  emf  that
opposes any change in the current through the inductor. From Eq. (31.13), for a
across the inductor and the
given current amplitude
self-induced emf
that is directly propor-
tional to
According to Eq. (31.12), the inductive reactance and self-induced
emf increase with more rapid variation in current (that is, increasing angular fre-
quency

vL = + L di>dt
both have an amplitude

I
E = - L di>dt

) and increasing inductance L.

the voltage

XL.

VL

v

31.2 Resistance and Reactance

1027

VL

XL

Since

If an oscillating voltage of a given amplitude

is applied across the inductor
terminals, the resulting current will have a smaller amplitude  for larger values of
is proportional to frequency, a high-frequency voltage applied to the
XL.
inductor gives only a small current, while a lower-frequency voltage of the same
amplitude gives rise to a larger current. Inductors are used in some circuit applica-
tions, such as power supplies and radio-interference ﬁlters, to block high frequen-
cies while permitting lower frequencies or dc to pass through. A circuit device that
uses an inductor for this purpose is called a low-pass ﬁlter (see Problem 31.52).

I

Example 31.2

An inductor in an ac circuit

The current amplitude in a pure inductor in a radio receiver is to be
250 mA
when  the  voltage  amplitude  is  3.60 V at  a  frequency  of
1.60 MHz (at the upper end of the AM broadcast band). (a) What
inductive reactance is needed? What inductance? (b) If the voltage
amplitude  is  kept  constant,  what  will  be  the  current  amplitude
through this inductor at 16.0 MHz? At 160 kHz?

SOLUTION

IDENTIFY and SET UP: There may be other elements of this circuit,
but in this example we don’t care: All they do is provide the induc-
tor  with  an  oscillating  voltage,  so  the  other  elements  are  lumped
into  the  ac  source  shown  in  Fig.  31.8a.  We  are  given  the  current
amplitude  and the voltage amplitude  Our target variables in part
(a) are the inductive reactance
at 1.60 MHz and the inductance
XL
which we ﬁnd using Eqs. (31.13) and  (31.12). Knowing  we
L,
use these equations in part (b) to ﬁnd

L,
and I at any frequency.

V.

I

XL

From Eq. (31.12), with

v = 2pƒ,

L =

=

XL
2pƒ

1.44 * 104 Æ
2p11.60 * 106 Hz2
= 1.43 * 10-3 H = 1.43 mH

(b) Combining Eqs. (31.12) and  (31.13), we ﬁnd

VL>vL = VL>2pƒL.
portional to the frequency  Since
the  current  amplitudes  at  16.0  MHz
0.160 MHz
125.0 mA2

VL>XL =
Thus  the  current  amplitude  is  inversely  pro-
I = 250 mA
ƒ = 1.60 MHz,
110ƒ2
160 kHz =
and
will  be,  respectively,  one-tenth  as  great

and ten times as great

12500 mA =

2.50 mA2

.

1ƒ>102

I =

at

ƒ.

EVALUATE:  In  general,  the  lower  the  frequency  of  an  oscillating
voltage applied across an inductor, the greater the amplitude of the
resulting oscillating current.

EXECUTE: (a) From Eq. (31.13),

XL =

VL
I

=

3.60 V
250 * 10-6 A

= 1.44 * 104 Æ = 14.4 kÆ

Capacitor in an ac Circuit
Finally, we connect a capacitor with capacitance
i = I cos vt
producing a current
tion of current is counterclockwise around the circuit.

to the source, as in Fig. 31.9a,
through the capacitor. Again, the positive direc-

C

CAUTION Alternating  current  through  a  capacitor You  may  object  that  charge  can’t
really  move  through  the  capacitor  because  its  two  plates  are  insulated  from  each  other.
True enough, but as the capacitor charges and discharges, there is at each instant a current
into one plate, an equal current out of the other plate, and an equal displacement current
i
between the plates just as though the charge were being conducted through the capacitor.
(You may want to review the discussion of displacement current in Section 29.7.) Thus we
often speak about alternating current through a capacitor. ❙

a

To ﬁnd the instantaneous voltage
b

across the capacitor—that is, the poten-
q
tial of point  with respect to point  —we ﬁrst let  denote the charge on the left-
is the charge on the right-hand
hand plate of the capacitor in Fig. 31.9a (so
i
plate). The current  is related to  by
with this deﬁnition, positive cur-
rent corresponds to an increasing charge on the left-hand capacitor plate. Then

-q
i = dq>dt;

vC

q

Integrating this, we get

i =

dq
dt

= I cos vt

q = I

v sin vt

(31.14)

1028

CHAPTER 31 Alternating Current

C
31.9 Capacitor
across an ac source.

connected

(a) Circuit with ac source and capacitor

q (cid:2)q

i

b

i

a

C
vC

(b) Graphs of current and voltage versus time

i, v

I

VC

O

i 5 I cos vt

5

vC

I
vC

cos 1vt (cid:2) 90°2

t

1
4 T,

p
2
Voltage curve lags current curve by a quarter-
cycle (corresponding to f 5(cid:2) p/2 rad 5 (cid:2)90°).

rad 5 90°

(c) Phasor diagram

Current
phasor

I

Phase
angle f

vt

i

O
Voltage
phasor

vC

VC

Voltage phasor lags
current phasor by
f 5(cid:2)p /2 rad 5 (cid:2)90°.

Also, from Eq. (24.1) the charge  equals the voltage  multiplied by the capac-
itance,

q
Using this in Eq. (31.14), we ﬁnd

vC

q = CvC.

vC = I
vC

sin vt

(31.15)

q;

i
The instantaneous current
q = CvC,
i
charge
since
(Compare  to  an  inductor,  for  which  the  situation  is  reversed  and
tional to the rate of change of  ) Figure 31.9b shows
Because
vC
neously levels off at its maximum and minimum values.

of the capacitor
is equal to the rate of change
is also proportional to the rate of change of voltage.
vL
is  propor-
vC
and  as functions of t.
the current has its greatest magnitude when the
curve instanta-

curve is rising or falling most steeply and is zero when the

i.
i = dq>dt = C dvC>dt,

vC

i

dq>dt

The  capacitor  voltage  and  current  are  out  of  phase  by  a  quarter-cycle.  The
peaks of voltage occur a quarter-cycle after the corresponding current peaks, and
we say that the voltage lags the current by
The phasor diagram in Fig. 31.9c
shows this relationship; the voltage phasor is behind the current phasor by a quarter-
cycle, or

90°.

90°.

We  can  also  derive  this  phase  difference  by  rewriting  Eq.  (31.15) using  the

identity

cos1A - 90°2 = sin A:

vC = I
vC

cos1vt - 90°2

(31.16)

This  corresponds  to  a  phase  angle
start” of

compared with the current

90°

i = I cos vt.

f = - 90°.

This  cosine  function  has  a  “late

Equations (31.15) and (31.16) show that the maximum voltage

VC

(the voltage

amplitude) is

VC = I
vC

(13.17)

VR = IR,

we

To put this expression in a form similar to Eq. (31.7) for a resistor,
deﬁne a quantity

XC,

called the capacitive reactance of the capacitor, as
XC = 1
vC

    (capacitive reactance)

(31.18)

Then

VC = IXC    (amplitude of voltage across a capacitor, ac circuit)

(31.19)

The SI unit of
because

XC

XC

is the ohm, the same as for resistance and inductive reactance,

is the ratio of a voltage and a current.

CAUTION Capacitor voltage and current are not in phase Remember that Eq. (31.19) for
a capacitor, like Eq. (31.13) for an inductor, is not a statement about the instantaneous val-
ues  of  voltage  and  current.  The  instantaneous  values  are  actually
out  of  phase,  as
Fig. 31.9b shows. Rather, Eq. (31.19) relates the amplitudes of the voltage and current. ❙

90°

C

The Meaning of Capacitive Reactance
The  capacitive  reactance  of  a  capacitor  is  inversely  proportional  both  to  the
the greater the capacitance and the
and to the angular frequency
capacitance
higher the frequency, the smaller the capacitive reactance
Capacitors tend to
pass high-frequency current and to block low-frequency currents and dc, just the
opposite  of  inductors.  A device  that  preferentially  passes  signals  of  high  fre-
quency is called a high-pass ﬁlter (see Problem 31.51).

XC.

v;

Example 31.3

A resistor and a capacitor in an ac circuit

31.2 Resistance and Reactance

1029

200-Æ

resistor  is  connected  in  series  with  a

capacitor.
A
12500 rad>s2t
The voltage across the resistor is
(Fig.  31.10).  (a)  Derive  an  expression  for  the  circuit  current.
(b) Determine the capacitive reactance of the capacitor. (c) Derive
an expression for the voltage across the capacitor.

vR = 11.20 V2 cos

5.0-mF

SOLUTION

IDENTIFY  and SET  UP: Since this is a series circuit, the current is
the same through the capacitor as through the resistor. Our target
and  the
variables  are  the  current
capacitor voltage  We use Eq. (31.6) to ﬁnd an expression for
i
, Eq. (31.18) to
in terms of the angular frequency
and
ﬁnd
Eq. (31.16) to write an expression for vC.

Eq. (31.19) to ﬁnd the capacitor voltage amplitude

the  capacitive  reactance

v = 2500 rad>s

XC,

XC,

vC.

VC,

i,

EXECUTE: (a) From Eq. (31.6),

vR = iR,

we ﬁnd

i =

vR
R

=

11.20 V2 cos12500 rad>s2t
200 Æ

= 16.0 * 10-3 A2 cos12500 rad>s2t

(b)  From  Eq.  (31.18),  the  capacitive  reactance  at

v =

2500 rad>s

is
XC = 1
vC

=

1
12500 rad>s215.0 * 10-6 F2

= 80 Æ

(c) From Eq. (31.19), the capacitor voltage amplitude is
VC = IXC = 16.0 * 10-3 A2180 Æ2 = 0.48 V

80-Æ
(The
resistance, so
is 40% of
age is given by Eq. (31.16):

VC

reactance of the capacitor is 40% of the resistor’s

200-Æ
) The instantaneous capacitor volt-

VR.

31.10 Our sketch for this problem.

vC = VC cos1vt - 90°2

= 10.48 V2 cos312500 rad>s2t - p>2 rad4

EVALUATE:  Although  the  same  current passes  through  both  the
capacitor and the resistor, the voltages across them are different in
both amplitude and phase. Note that in the expression for
we
converted the
rad so that all the angular quantities have
the same units. In ac circuit analysis, phase angles are often given
in degrees, so be careful to convert to radians when necessary.

p>2

90°

vC

to

Comparing ac Circuit Elements
Table 31.1 summarizes the relationships of voltage and current amplitudes for the
three circuit elements we have discussed. Note again that instantaneous voltage
and  current  are  proportional  in  a  resistor,  where  there  is  zero  phase  difference
and  (see Fig. 31.7b). The instantaneous voltage and current are not
between
proportional in an inductor or capacitor, because there is a
phase difference
in both cases (see Figs. 31.8b and 31.9b).

90°

vR

i

Figure 31.11 shows how the resistance of a resistor and the reactances of an
inductor  and  a  capacitor  vary  with  angular  frequency
is  inde-
pendent of frequency, while the reactances
corre-
XC
XC S q,
sponding to a dc circuit, there is no current through a capacitor because
v S q,
also
and  there  is  no  inductive  effect  because
XL
approaches  inﬁnity,  and  the  current  through  an  inductor  becomes  vanishingly
small; recall that the self-induced emf opposes rapid changes in current. In this
and the voltage across a capacitor both approach zero; the current
same limit,
changes direction so rapidly that no charge can build up on either plate.

v.
are not. If

R
v = 0,

In  the  limit

Resistance

XL = 0.

and

XC

XL

XC
31.11 Graphs of
functions of angular frequency v.

and

XL,

R,

R, X

XC

XL

Figure 31.12 shows an application of the above discussion to a loudspeaker
system. Low-frequency sounds are produced by the woofer, which is a speaker
with large diameter; the tweeter, a speaker with smaller diameter, produces high-
frequency sounds. In order to route signals of different frequency to the appropri-
ate speaker, the woofer and tweeter are connected in parallel across the ampliﬁer

O

Table 31.1 Circuit Elements with Alternating Current

Circuit Element

Resistor
Inductor
Capacitor

Amplitude Relationship
VR = IR
VL = IXL
VC = IXC

Circuit Quantity

Phase of

v

R
XL = vL
XC = 1>vC

i
In phase with
90°
i
Leads  by
i
Lags  by 90°

as

R

v
