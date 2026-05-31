Example 31.5
An L-R-C series circuit II
For the L-R-C series circuit of Example 31.4, find expressions for
the time dependence of the instantaneous current i and the instan-
taneous voltages across the resistor (
), inductor (
), capacitor
(
), and ac source ( ).
SOLUTION
IDENTIFY and SET UP: We describe the current using Eq. (31.2),
which assumes that the current is maximum at 
. The voltages
are then given by Eq. (31.8) for the resistor, Eq. (31.10) for the induc-
tor, Eq. (31.16) for the capacitor, and Eq. (31.25) for the source.
EXECUTE: The current and the voltages all oscillate with the same
angular frequency, 
and hence with the same
period,
From Eq. (31.2), the current is
The resistor voltage is in phase with the current, so
The inductor voltage leads the current by 
so
The capacitor voltage lags the current by 
so
We found in Example 31.4 that the source voltage (equal to the
voltage across the entire combination of resistor, inductor, and
capacitor) leads the current by 
so
f = 53°,
= 120 V2sin110,000 rad>s2t
vC = VC cos1vt - 90°2 = VC sinvt
90°,
= -160 V2 sin110,000 rad>s2t
vL = VL cos1vt + 90°2 = -VL sin vt
90°,
vR = VR cosvt = 130 V2 cos110,000 rad>s2t
i = Icosvt = 10.10 A2 cos110,000 rad>s2t
= 6.3 * 10-4 s = 0.63 ms.
2p>v = 2p>110,000 rad>s2
v = 10,000 rad>s,
t = 0
v
vC
vL
vR
EVALUATE: Figure 31.15 graphs the four voltages versus time. The
inductor voltage has a larger amplitude than the capacitor voltage
because 
The instantaneous source voltage 
is always
equal to the sum of the instantaneous voltages 
and 
You
should verify this by measuring the values of the voltages shown
in the graph at different values of the time t.
vC.
vL,
vR,
v
XL 7 XC.
= 150 V2cos3110,000 rad>s2t + 0.93 rad4
= 150 V2cosc110,000 rad>s2t + a 2p rad
360° b153°2d
v = V cos1vt + f2
KEY:
v
vL
vR
v (V)
t (ms)
vC
60
-20
-40
-60
-0.2
0
20
40
0.2
0.6
VL 5 60 V
V 5 50 V
VR 5 30 V
VC 5 20 V
0.4
31.15 Graphs of the source voltage 
resistor voltage 
inductor voltage 
and capacitor voltage 
as functions of time
for the situation of Example 31.4. The current, which is not
shown, is in phase with the resistor voltage.
vC
vL,
vR,
v,
Test Your Understanding of Section 31.3
Rank the following ac
circuits in order of their current amplitude, from highest to lowest value. (i) the
circuit in Example 31.4; (ii) the circuit in Example 31.4 with the capacitor and
inductor both removed; (iii) the circuit in Example 31.4 with the resistor and capacitor
both removed; (iv) the circuit in Example 31.4 with the resistor and inductor both
removed.
❙

31.4 Power in Alternating-Current Circuits
1035
heights of the graphs of and in Fig. 31.7b at each instant. This graph is shown
by the black curve in Fig. 31.16a. The product 
is always positive because 
and are always either both positive or both negative. Hence energy is supplied
to the resistor at every instant for both directions of 
although the power is not
constant.
The power curve for a pure resistor is symmetrical about a value equal to one-
half its maximum value VI, so the average power
is
(31.27)
An equivalent expression is
(31.28)
Also, 
so we can express 
by any of the equivalent forms
(31.29)
Note that the expressions in Eq. (31.29) have the same form as the corresponding
relationships for a dc circuit, Eq. (25.18). Also note that they are valid only for
pure resistors, not for more complicated combinations of circuit elements.
Power in an Inductor
Next we connect the source to a pure inductor 
as in Fig. 31.8a. The voltage
leads the current by 
When we multiply the curves of 
and 
the
product 
is negative during the half of the cycle when 
and have opposite
signs. The power curve, shown in Fig. 31.16b, is symmetrical about the horizon-
tal axis; it is positive half the time and negative the other half, and the average
power is zero. When is positive, energy is being supplied to set up the magnetic
field in the inductor; when is negative, the field is collapsing and the inductor is
returning energy to the source. The net energy transfer over one cycle is zero.
Power in a Capacitor
Finally, we connect the source to a pure capacitor 
as in Fig. 31.9a. The voltage
lags the current by 
Figure 31.16c shows the power curve; the aver-
age power is again zero. Energy is supplied to charge the capacitor and is returned
90°.
i
v = vC
C,
p
p
i
v
vi
i,
v
90°.
i
v = vL
L,
Pav = I rms
2R = Vrms
2
R
= VrmsIrms  (for a pure resistor)
Pav
Vrms = IrmsR,
Pav =
V
12
I
12 = VrmsIrms  (for a pure resistor)
Pav = 1
2 VI  1for a pure resistor)
Pav
i,
i
v
vi
i
v
For an inductor or capacitor, p  vi  is alternately
positive and negative, and the average power is zero.
For a resistor, p  vi is always positive
because v and i are either both positive
or both negative at any instant.
For an arbitrary combination of
resistors, inductors, and capacitors,
the average power is positive.
KEY: Instantaneous current, i
Instantaneous voltage across device, v
Instantaneous power input to device, p
(a) Pure resistor
VI
O
V
I
v, i, p
p
i
v
t
Pav  VI
1
2
(b) Pure inductor
O
v, i, p
p
i
v
t
(c) Pure capacitor
O
, i, p
p
i
v
t
v, i, p
(d) Arbitrary ac circuit
Pav 5 VI cos f
t
v
i
p
1
2
v
O
31.16 Graphs of current, voltage, and power as functions of time for (a) a pure resistor, (b) a pure inductor, (c) a pure capacitor, and
(d) an arbitrary ac circuit that can have resistance, inductance, and capacitance.

to the source when the capacitor discharges. The net energy transfer over one
cycle is again zero.
Power in a General ac Circuit
In any ac circuit, with any combination of resistors, capacitors, and inductors, the
voltage across the entire circuit has some phase angle 
with respect to the cur-
rent Then the instantaneous power is given by
(31.30)
The instantaneous power curve has the form shown in Fig. 31.16d. The area
between the positive loops and the horizontal axis is greater than the area between
the negative loops and the horizontal axis, and the average power is positive.
We can derive from Eq. (31.30) an expression for the average power 
by
using the identity for the cosine of the sum of two angles:
From the discussion in Section 31.1 that led to Eq. (31.4), we see that the average
value of 
(over one cycle) is 
The average value of 
is zero
because this product is equal to 
whose average over a cycle is zero. So
the average power 
is
(average power into a 
general ac circuit)
(31.31)
When and are in phase, so 
the average power equals 
when 
and are 
out of phase, the average power is zero. In the general
case, when
has a phase angle 
with respect to 
the average power equals 
multiplied by 
the component of the voltage phasor that is in phase with the
current phasor. Figure 31.17 shows the general relationship of the current and volt-
age phasors. For the L-R-C series circuit, Figs. 31.13b and 31.13c show that 
equals the voltage amplitude 
for the resistor; hence Eq. (31.31) is the average
power dissipated in the resistor. On average there is no energy flow into or out of
the inductor or capacitor, so none of 
goes into either of these circuit elements.
The factor 
is called the power factor of the circuit. For a pure resist-
ance, 
and 
For a pure inductor or capacitor,
and 
For an L-R-C series circuit the power factor
is equal to 
we leave the proof of this statement to you (see Exercise 31.21).
A low power factor (large angle 
of lag or lead) is usually undesirable in power
circuits. The reason is that for a given potential difference, a large current is needed
to supply a given amount of power. This results in large 
losses in the transmis-
sion lines. Your electric power company may charge a higher rate to a client with a
low power factor. Many types of ac machinery draw a lagging current; that is, the
current drawn by the machinery lags the applied voltage. Hence the voltage leads
the current, so 
and 
The power factor can be corrected toward
the ideal value of 1 by connecting a capacitor in parallel with the load. The current
drawn by the capacitor leads the voltage (that is, the voltage across the capacitor
lags the current), which compensates for the lagging current in the other branch of
the circuit. The capacitor itself absorbs no net power from the line.
cosf 6 1.
f 7 0
i2R
f
R>Z;
Pav = 0.
cosf = 0,
f = 90°,
Pav = VrmsIrms.
cosf = 1,
f = 0,
cosf
Pav
VR
Vcosf
Vcosf,
1
2 I
i,
f
v
90°
i
v
1
2 VI = VrmsIrms;
f = 0,
i
v
Pav = 1
2 VIcosf = VrmsIrmscosf
Pav
1
2 sin2vt,
cosvtsinvt
1
2 .
cos2vt
= VIcosfcos2vt - VIsinfcosvtsinvt
p = 3V1cosvtcosf - sinvtsinf243Icosvt4
Pav
p = vi = 3Vcos1vt + f243Icosvt4
p
i.
f
v
1036
CHAPTER 31 Alternating Current
