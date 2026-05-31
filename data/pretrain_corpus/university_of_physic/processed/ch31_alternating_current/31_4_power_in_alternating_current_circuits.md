1034

CHAPTER 31 Alternating Current

Example 31.5

An L-R-C series circuit II

For the L-R-C series circuit of Example 31.4, ﬁnd expressions for
the time dependence of the instantaneous current i and the instan-
taneous  voltages  across  the  resistor  (
),  capacitor
vC
(

), and ac source ( ).

),  inductor  (

vR

vL

v

SOLUTION

IDENTIFY  and SET  UP:  We  describe  the  current  using  Eq.  (31.2),
which assumes that the current is maximum at
. The voltages
are then given by Eq. (31.8) for the resistor, Eq. (31.10) for the induc-
tor, Eq. (31.16) for the capacitor, and Eq. (31.25) for the source.

t = 0

EXECUTE: The current and the voltages all oscillate with the same
angular  frequency,
and  hence  with  the  same
= 6.3 * 10-4 s = 0.63 ms.
period,
From Eq. (31.2), the current is

2p>v = 2p>110,000 rad>s2

v = 10,000 rad>s,

i = I cos vt = 10.10 A2 cos110,000 rad>s2t

The resistor voltage is in phase with the current, so

vR = VR cos vt = 130 V2 cos110,000 rad>s2t

The inductor voltage leads the current by

90°,

so

vL = VL cos1vt + 90°2 = - VL sin vt
= - 160 V2 sin110,000 rad>s2t

The capacitor voltage lags the current by

90°,

so

vC = VC cos1vt - 90°2 = VC sin vt
= 120 V2 sin110,000 rad>s2t

We  found  in  Example  31.4  that  the  source  voltage  (equal  to  the
voltage  across  the  entire  combination  of  resistor,  inductor,  and
capacitor) leads the current by

f = 53°,

so

v = V cos1vt + f2

= 150 V2 cos c110,000 rad>s2t + a 2p rad
360°
= 150 V2 cos3110,000 rad>s2t + 0.93 rad4

b153°2 d

XL 7 XC.

EVALUATE: Figure 31.15 graphs the four voltages versus time. The
inductor voltage has a larger amplitude than the capacitor voltage
is  always
because
equal to the sum of the instantaneous voltages
You
should verify this by measuring the values of the voltages shown
in the graph at different values of the time t.

The  instantaneous source  voltage
vL,

v
and

vC.

vR,

31.15 Graphs of the source voltage
vL,
inductor voltage
for the situation of Example 31.4. The current, which is not
shown, is in phase with the resistor voltage.

resistor voltage
vC

and capacitor voltage

v,

vR,

as functions of time

5 60 V
VL
V 5 50 V
5 30 V

VR

VC

5 20 V

0.2

0.4

0.6

t (ms)

v (V)

60

40

20

0
–20

–40

–60

–0.2

KEY: v

vR

vL

vC

Test Your Understanding of Section 31.3 Rank the following ac
circuits in order of their current amplitude, from highest to lowest value. (i) the
circuit in Example 31.4; (ii) the circuit in Example 31.4 with the capacitor and
inductor both removed; (iii) the circuit in Example 31.4 with the resistor and capacitor
both removed; (iv) the circuit in Example 31.4 with the resistor and inductor both
removed.

❙

31.4 Power in Alternating-Current Circuits

Alternating  currents  play  a  central  role  in  systems  for  distributing,  converting,
and using electrical energy, so it’s important to look at power relationships in ac
I,
circuits.  For  an  ac  circuit  with  instantaneous  current  and  current  amplitude
we’ll consider an element of that circuit across which the instantaneous potential
V.
difference is  with voltage amplitude  The instantaneous power  delivered to
this circuit element is

v

p

i

Let’s ﬁrst see what this means for individual circuit elements. We’ll assume in
each case that

i = I cos vt.

p = vi

Power in a Resistor
Suppose ﬁrst that the circuit element is a pure resistor
v = vR

as in Fig. 31.7a; then
and  are in phase. We obtain the graph representing  by multiplying the

R,

p

i

31.4 Power in Alternating-Current Circuits

1035

i

v
heights of the graphs of  and  in Fig. 31.7b at each instant. This graph is shown
v
by the black curve in Fig. 31.16a. The product
and  are always either both positive or both negative. Hence energy is supplied
to the resistor at every instant for both directions of  although the power is not
constant.

is always positive because

vi

i,

i

The power curve for a pure resistor is symmetrical about a value equal to one-

half its maximum value VI, so the average power

Pav

is

Pav = 1

2 VI    1for a pure resistor)

(31.27)

An equivalent expression is

Pav = V
12

I
12

= VrmsIrms    (for a pure resistor)

(31.28)

Also,

Vrms = IrmsR,

so we can express

Pav

by any of the equivalent forms

Pav = I rms

2R =

2
V rms
R

= VrmsIrms    (for a pure resistor)

(31.29)

Note that the expressions in Eq. (31.29) have the same form as the corresponding
relationships for a dc circuit, Eq. (25.18). Also note that they are valid only for
pure resistors, not for more complicated combinations of circuit elements.

i

L,

90°.

is negative during the half of the cycle when

leads the current  by
vi

Power in an Inductor
Next we connect the source to a pure inductor
as in Fig. 31.8a. The voltage
v = vL
v
the
and  have opposite
product
signs. The power curve, shown in Fig. 31.16b, is symmetrical about the horizon-
tal axis; it is positive half the time and negative the other half, and the average
p
power is zero. When
is positive, energy is being supplied to set up the magnetic
is negative, the ﬁeld is collapsing and the inductor is
ﬁeld in the inductor; when
returning energy to the source. The net energy transfer over one cycle is zero.

When we multiply the curves of

and

i,

v

p

i

Power in a Capacitor
as in Fig. 31.9a. The voltage
Finally, we connect the source to a pure capacitor
v = vC
i
Figure 31.16c shows the power curve; the aver-
age power is again zero. Energy is supplied to charge the capacitor and is returned

lags the current  by

90°.

C,

31.16 Graphs of current, voltage, and power as functions of time for (a) a pure resistor, (b) a pure inductor, (c) a pure capacitor, and
(d) an arbitrary ac circuit that can have resistance, inductance, and capacitance.

(a) Pure resistor

(b) Pure inductor

(c) Pure capacitor

(d) Arbitrary ac circuit

For a resistor, p (cid:3) vi is always positive
because v and i are either both positive
or both negative at any instant.

For an inductor or capacitor, p (cid:3) vi  is alternately
positive and negative, and the average power is zero.

For an arbitrary combination of
resistors, inductors, and capacitors,
the average power is positive.

v, i, p

VI

Pav

(cid:3)  VI1
2

I

V

O

p

v

i

v, i, p

v
, i, p

t

O

p

v

i

t

O

p

v

i

v, i, p
Pav

1
2

5 VI cos f
p

t

O

t

v

i

KEY: Instantaneous current, i

Instantaneous voltage across device, v

Instantaneous power input to device, p

1036

CHAPTER 31 Alternating Current

to  the  source  when  the  capacitor  discharges.  The  net  energy  transfer  over  one
cycle is again zero.

Power in a General ac Circuit
In any ac circuit, with any combination of resistors, capacitors, and inductors, the
voltage  across the entire circuit has some phase angle  with respect to the cur-
rent  Then the instantaneous power

is given by

f

i.

v

p

p = vi = 3V cos1vt + f243I cos vt4

(31.30)

The  instantaneous  power  curve  has  the  form  shown  in  Fig.  31.16d.  The  area
between the positive loops and the horizontal axis is greater than the area between
the negative loops and the horizontal axis, and the average power is positive.
We can derive from Eq. (31.30) an expression for the average power

by

Pav

using the identity for the cosine of the sum of two angles:

p = 3V1cos vt cos f - sin vt sin f243I cos vt4
= VI cos f cos2 vt - VI sin f cos vt sin vt

cos2 vt

From the discussion in Section 31.1 that led to Eq. (31.4), we see that the average
value of
is zero
because this product is equal to
whose average over a cycle is zero. So
the average power

(over one cycle) is  The average value of

1
2 .
2 sin 2vt,

cos vt sin vt

is

1

Pav

31.17 Using phasors to calculate the
average power for an arbitrary ac circuit.

1
Average power 5 I(V cos f), where V cos f
2
is the component of V in phase with I.

I

f

V

V cos f
vt

O

Pav = 1

2 VI cos f = VrmsIrms cos f

(average power into a
general ac circuit)

(31.31)

1

VR

Pav

90°

v
v

f = 0,

The factor
f = 0,

the average power equals

ance,
f = (cid:2) 90°,
is equal to

goes into either of these circuit elements.

f
has a phase angle  with respect to
V cos f,

2 VI = VrmsIrms;
i
When  and  are in phase, so
the average power equals
and  are
out  of  phase,  the  average  power  is  zero.  In  the  general
i
when
1
v
i,
2 I
case, when
multiplied by
the component of the voltage phasor that is in phase with the
current phasor. Figure 31.17 shows the general relationship of the current and volt-
V cos f
age phasors. For the L-R-C series circuit, Figs. 31.13b and 31.13c show that
for the resistor; hence Eq. (31.31) is the average
equals the voltage amplitude
power dissipated in the resistor. On average there is no energy ﬂow into or out of
the inductor or capacitor, so none of
cos f
cos f = 1,

is called the power factor of the circuit. For a pure resist-
For  a  pure  inductor  or  capacitor,
For an L-R-C series circuit the power factor
we leave the proof of this statement to you (see Exercise 31.21).
A low power factor (large angle  of lag or lead) is usually undesirable in power
circuits. The reason is that for a given potential difference, a large current is needed
to supply a given amount of power. This results in large
losses in the transmis-
sion lines. Your electric power company may charge a higher rate to a client with a
low power factor. Many types of ac machinery draw a lagging current; that is, the
current drawn by the machinery lags the applied voltage. Hence the voltage leads
the current, so
The power factor can be corrected toward
the ideal value of 1 by connecting a capacitor in parallel with the load. The current
drawn by the capacitor leads the voltage (that is, the voltage across the capacitor
lags the current), which compensates for the lagging current in the other branch of
the circuit. The capacitor itself absorbs no net power from the line.

cos f = 0,
R>Z;

Pav = VrmsIrms.

cos f 6 1.

Pav = 0.

f 7 0

and

and

and

i 2R

f

Example 31.6

Power in a hair dryer

An  electric  hair  dryer  is  rated  at  1500 W (the  average power)  at
120 V (the rms voltage). Calculate (a) the resistance, (b) the rms

current,  and  (c)  the  maximum  instantaneous  power. Assume  that
the dryer is a pure resistor. (The heating element acts as a resistor.)

Continued
