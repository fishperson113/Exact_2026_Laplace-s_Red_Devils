Example 31.2
An inductor in an ac circuit
The current amplitude in a pure inductor in a radio receiver is to be
when the voltage amplitude is 3.60 V at a frequency of
1.60 MHz (at the upper end of the AM broadcast band). (a) What
inductive reactance is needed? What inductance? (b) If the voltage
amplitude is kept constant, what will be the current amplitude
through this inductor at 16.0 MHz? At 160 kHz?
SOLUTION
IDENTIFY and SET UP: There may be other elements of this circuit,
but in this example we don’t care: All they do is provide the induc-
tor with an oscillating voltage, so the other elements are lumped
into the ac source shown in Fig. 31.8a. We are given the current
amplitude and the voltage amplitude 
Our target variables in part 
(a) are the inductive reactance 
at 1.60 MHz and the inductance
which we find using Eqs. (31.13) and  (31.12). Knowing 
we
use these equations in part (b) to find 
and I at any frequency.
EXECUTE: (a) From Eq. (31.13),
XL = VL
I =
3.60 V
250 * 10-6 A
= 1.44 * 104 Æ = 14.4 kÆ
XL
L,
L,
XL
V.
I
250 mA
From Eq. (31.12), with 
(b) Combining Eqs. (31.12) and  (31.13), we find
Thus the current amplitude is inversely pro-
portional to the frequency 
Since 
at 
the current amplitudes at 16.0 MHz 
and 
will be, respectively, one-tenth as great
and ten times as great 
.
EVALUATE: In general, the lower the frequency of an oscillating
voltage applied across an inductor, the greater the amplitude of the
resulting oscillating current.
2.50 mA2
12500 mA =
125.0 mA2
1ƒ>102
0.160 MHz
160 kHz =
110ƒ2
ƒ = 1.60 MHz,
I = 250 mA
ƒ.
VL>vL = VL>2pƒL.
VL>XL =
I =
= 1.43 * 10-3 H = 1.43 mH
L =
XL
2pƒ =
1.44 * 104 Æ
2p11.60 * 106 Hz2
v = 2pƒ,
Capacitor in an ac Circuit
Finally, we connect a capacitor with capacitance 
to the source, as in Fig. 31.9a,
producing a current 
through the capacitor. Again, the positive direc-
tion of current is counterclockwise around the circuit.
CAUTION
Alternating current through a capacitor You may object that charge can’t
really move through the capacitor because its two plates are insulated from each other.
True enough, but as the capacitor charges and discharges, there is at each instant a current
into one plate, an equal current out of the other plate, and an equal displacement current
between the plates just as though the charge were being conducted through the capacitor.
(You may want to review the discussion of displacement current in Section 29.7.) Thus we
often speak about alternating current through a capacitor. ❙
To find the instantaneous voltage 
across the capacitor-that is, the poten-
tial of point with respect to point -we first let denote the charge on the left-
hand plate of the capacitor in Fig. 31.9a (so 
is the charge on the right-hand
plate). The current is related to by 
with this definition, positive cur-
rent corresponds to an increasing charge on the left-hand capacitor plate. Then
Integrating this, we get
(31.14)
q = I
v sinvt
i = dq
dt = Icosvt
i = dq>dt;
q
i
-q
q
b
a
vC
i
i = Icosvt
C

1028
CHAPTER 31 Alternating Current
t
a
C
b
i
i
q
q
I
VC
O
i, v
O
i
vC
VC
I
vt
Current
phasor
Voltage
phasor
Voltage curve lags current curve by a quarter-
cycle (corresponding to f 5 p/2 rad 5 90°).
Voltage phasor lags
current phasor by
f 5 p/2 rad 5 90°.
(c) Phasor diagram
(b) Graphs of current and voltage versus time
vC
(a) Circuit with ac source and capacitor
1
4 T,
rad 5 90°
p
2
I
vC
i 5 Icosvt
vC 5
cos 1vt  90°2
Phase
angle f
31.9 Capacitor 
connected
across an ac source.
C
Also, from Eq. (24.1) the charge equals the voltage 
multiplied by the capac-
itance, 
Using this in Eq. (31.14), we find
(31.15)
The instantaneous current is equal to the rate of change 
of the capacitor
charge 
since 
is also proportional to the rate of change of voltage.
(Compare to an inductor, for which the situation is reversed and 
is propor-
tional to the rate of change of ) Figure 31.9b shows 
and as functions of t.
Because 
the current has its greatest magnitude when the
curve is rising or falling most steeply and is zero when the 
curve instanta-
neously levels off at its maximum and minimum values.
The capacitor voltage and current are out of phase by a quarter-cycle. The
peaks of voltage occur a quarter-cycle after the corresponding current peaks, and
we say that the voltage lags the current by 
The phasor diagram in Fig. 31.9c
shows this relationship; the voltage phasor is behind the current phasor by a quarter-
cycle, or 
We can also derive this phase difference by rewriting Eq. (31.15) using the
identity
(31.16)
This corresponds to a phase angle 
This cosine function has a “late
start” of 
compared with the current 
Equations (31.15) and (31.16) show that the maximum voltage 
(the voltage
amplitude) is
(13.17)
To put this expression in a form similar to Eq. (31.7) for a resistor, 
we
define a quantity 
called the capacitive reactance of the capacitor, as
(31.18)
Then
(31.19)
The SI unit of 
is the ohm, the same as for resistance and inductive reactance,
because 
is the ratio of a voltage and a current.
CAUTION
Capacitor voltage and current are not in phase Remember that Eq. (31.19) for
a capacitor, like Eq. (31.13) for an inductor, is not a statement about the instantaneous val-
ues of voltage and current. The instantaneous values are actually 
out of phase, as 
Fig. 31.9b shows. Rather, Eq. (31.19) relates the amplitudes of the voltage and current. ❙
The Meaning of Capacitive Reactance
The capacitive reactance of a capacitor is inversely proportional both to the
capacitance 
and to the angular frequency 
the greater the capacitance and the
higher the frequency, the smaller the capacitive reactance 
Capacitors tend to
pass high-frequency current and to block low-frequency currents and dc, just the
opposite of inductors. A device that preferentially passes signals of high fre-
quency is called a high-pass filter (see Problem 31.51).
XC.
v;
C
90°
XC
XC
VC = IXC  (amplitude of voltage across a capacitor, ac circuit)
XC =
1
vC  (capacitive reactance)
XC,
VR = IR,
VC =
I
vC
VC
i = Icosvt.
90°
f = -90°.
vC =
I
vC cos1vt - 90°2
cos1A - 90°2 = sinA:
90°.
90°.
vC
vC
i = dq>dt = C dvC>dt,
i
vC
i.
vL
i
q = CvC,
q;
dq>dt
i
vC =
I
vC sinvt
q = CvC.
vC
q

31.2 Resistance and Reactance
1029
Comparing ac Circuit Elements
Table 31.1 summarizes the relationships of voltage and current amplitudes for the
three circuit elements we have discussed. Note again that instantaneous voltage
and current are proportional in a resistor, where there is zero phase difference
between 
and (see Fig. 31.7b). The instantaneous voltage and current are not
proportional in an inductor or capacitor, because there is a 
phase difference
in both cases (see Figs. 31.8b and 31.9b).
Figure 31.11 shows how the resistance of a resistor and the reactances of an
inductor and a capacitor vary with angular frequency 
Resistance 
is inde-
pendent of frequency, while the reactances 
and 
are not. If 
corre-
sponding to a dc circuit, there is no current through a capacitor because 
and there is no inductive effect because 
In the limit 
also
approaches infinity, and the current through an inductor becomes vanishingly
small; recall that the self-induced emf opposes rapid changes in current. In this
same limit, 
and the voltage across a capacitor both approach zero; the current
changes direction so rapidly that no charge can build up on either plate.
Figure 31.12 shows an application of the above discussion to a loudspeaker
system. Low-frequency sounds are produced by the woofer, which is a speaker
with large diameter; the tweeter, a speaker with smaller diameter, produces high-
frequency sounds. In order to route signals of different frequency to the appropri-
ate speaker, the woofer and tweeter are connected in parallel across the amplifier
XC
XL
v S q,
XL = 0.
XC S q,
v = 0,
XC
XL
R
v.
90°
i
vR
