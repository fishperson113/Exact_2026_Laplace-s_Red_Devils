Example 31.3
A resistor and a capacitor in an ac circuit
A
resistor is connected in series with a 
capacitor.
The voltage across the resistor is 
(Fig. 31.10). (a) Derive an expression for the circuit current. 
(b) Determine the capacitive reactance of the capacitor. (c) Derive
an expression for the voltage across the capacitor.
SOLUTION
IDENTIFY and SET UP: Since this is a series circuit, the current is
the same through the capacitor as through the resistor. Our target
variables are the current 
the capacitive reactance 
and the
capacitor voltage 
We use Eq. (31.6) to find an expression for 
in terms of the angular frequency 
, Eq. (31.18) to
find 
Eq. (31.19) to find the capacitor voltage amplitude 
and
Eq. (31.16) to write an expression for vC.
VC,
XC,
v = 2500 rad>s
i
vC.
XC,
i,
12500 rad>s2t
vR = 11.20 V2cos
5.0-mF
200-Æ
EXECUTE: (a) From Eq. (31.6), 
we find
(b) From Eq. (31.18), the capacitive reactance at 
is
(c) From Eq. (31.19), the capacitor voltage amplitude is
(The 
reactance of the capacitor is 40% of the resistor’s 
resistance, so 
is 40% of 
) The instantaneous capacitor volt-
age is given by Eq. (31.16):
EVALUATE: Although the same current passes through both the
capacitor and the resistor, the voltages across them are different in
both amplitude and phase. Note that in the expression for 
we
converted the 
to 
rad so that all the angular quantities have
the same units. In ac circuit analysis, phase angles are often given
in degrees, so be careful to convert to radians when necessary.
p>2
90°
vC
= 10.48 V2cos312500 rad>s2t - p>2 rad4
vC = VC cos1vt - 90°2
VR.
VC
200-Æ
80-Æ
VC = IXC = 16.0 * 10-3 A2180 Æ2 = 0.48 V
XC =
1
vC =
1
12500 rad>s215.0 * 10-6 F2
= 80 Æ
2500 rad>s
v =
= 16.0 * 10-3 A2cos12500 rad>s2t
i = vR
R =
11.20 V2cos12500 rad>s2t
200 Æ
vR = iR,
31.10 Our sketch for this problem.
Table 31.1 Circuit Elements with Alternating Current
Circuit Element
Amplitude Relationship
Circuit Quantity
Phase of 
Resistor
In phase with 
Inductor
Leads by 
Capacitor
Lags by 90°
i
XC = 1>vC
VC = IXC
90°
i
XL = vL
VL = IXL
i
R
VR = IR
v
XC
O
R
R, X
XL
v
31.11 Graphs of 
and 
as
functions of angular frequency v.
XC
XL,
R,

31.3 The L-R-C Series Circuit
Many ac circuits used in practical electronic systems involve resistance, induc-
tive reactance, and capacitive reactance. Figure 31.13a shows a simple example:
A series circuit containing a resistor, an inductor, a capacitor, and an ac source.
(In Section 30.6 we considered the behavior of the current in an L-R-C series cir-
cuit without a source.)
To analyze this and similar circuits, we will use a phasor diagram that includes
the voltage and current phasors for each of the components. In this circuit,
because of Kirchhoff’s loop rule, the instantaneous total voltage 
across all
three components is equal to the source voltage at that instant. We will show that
the phasor representing this total voltage is the vector sum of the phasors for the
individual voltages.
Figures 31.13b and 31.13c show complete phasor diagrams for the circuit of
Fig. 31.13a. We assume that the source supplies a current given by 
Because the circuit elements are connected in series, the current at any instant is
the same at every point in the circuit. Thus a single phasor I, with length propor-
tional to the current amplitude, represents the current in all circuit elements.
As in Section 31.2, we use the symbols 
and 
for the instantaneous
voltages across 
and 
and the symbols 
and 
for the maximum
voltages. We denote the instantaneous and maximum source voltages by and 
Then, in Fig. 31.13a, 
and 
We have shown that the potential difference between the terminals of a resis-
tor is in phase with the current in the resistor and that its maximum value 
is
given by Eq. (31.7):
VR = IR
VR
vC = vcd.
vL = vbc,
vR = vab,
v = vad,
V.
v
VC
VL,
VR,
C,
L,
R,
vC
vL,
vR,
i = Icosvt.
i
vad
1030
CHAPTER 31 Alternating Current
Test Your Understanding of Section 31.2
An oscillating voltage of
fixed amplitude is applied across a circuit element. If the frequency of this voltage
is increased, will the amplitude of the current through the element (i) increase, 
(ii) decrease, or (iii) remain the same if it is (a) a resistor, (b) an inductor, or 
(c) a capacitor?
❙
output. The capacitor in the tweeter branch blocks the low-frequency components
of sound but passes the higher frequencies; the inductor in the woofer branch
does the opposite.
The inductor and capacitor feed low
frequencies mainly to the woofer and
high frequencies mainly to the tweeter.
(a) A crossover network in a loudspeaker system
Tweeter
Woofer
From
amplifier
V
B
A
R
L
R
C
O
(b) Graphs of rms current as functions of
frequency for a given amplifier voltage
f
Irms
Crossover
point
Tweeter
Woofer
31.12 (a) The two speakers in this loud-
speaker system are connected in parallel to
the amplifier. (b) Graphs of current ampli-
tude in the tweeter and woofer as functions
of frequency for a given amplifier voltage
amplitude.
(b) Phasor diagram for the case XL . XC
V 5 IZ
I
VR 5 IR
VC 5 IXC
VL 5 IXL
VL 2 VC
O
f
vt
(c) Phasor diagram for the case XL , XC
V 5 IZ
I
O
VC 5 IXC
VL 2 VC
VR 5 IR
VL 5 IXL
f
vt
(a) L-R-C series circuit
a
b
d
c
R
L
C
2q
q
i
Source voltage phasor is the vector
sum of the VR, VL, and VC phasors.
Inductor voltage
phasor leads
current
phasor
by 90°.
Capacitor voltage
phasor lags
current phasor
by 90°. It is thus always
antiparallel to the VL phasor.
If XL , XC, the source voltage phasor lags the
current phasor, X , 0, and f is a negative angle
between 0 and 290°.
Resistor voltage
phasor is in
phase with
current phasor.
All circuit
elements have
the same
current phasor.
31.13 An L-R-C series circuit with an ac source.

31.3 The L-R-C Series Circuit
1031
The phasor 
in Fig. 31.13b, in phase with the current phasor 
represents the
voltage across the resistor. Its projection onto the horizontal axis at any instant
gives the instantaneous potential difference 
The voltage across an inductor leads the current by 
Its voltage amplitude
is given by Eq. (31.13):
The phasor 
in Fig. 31.13b represents the voltage across the inductor, and its
projection onto the horizontal axis at any instant equals 
The voltage across a capacitor lags the current by 
Its voltage amplitude is
given by Eq. (31.19):
The phasor 
in Fig. 31.13b represents the voltage across the capacitor, and its
projection onto the horizontal axis at any instant equals 
The instantaneous potential difference 
between terminals a and d is equal at
every instant to the (algebraic) sum of the potential differences 
and 
That is, it equals the sum of the projections of the phasors 
and 
But the
sum of the projections of these phasors is equal to the projection of their vector
sum. So the vector sum 
must be the phasor that represents the source voltage 
and the instantaneous total voltage 
across the series of elements.
To form this vector sum, we first subtract the phasor 
from the phasor 
(These two phasors always lie along the same line, with opposite directions.)
This gives the phasor 
This is always at right angles to the phasor 
so
from the Pythagorean theorem the magnitude of the phasor 
is
(31.20)
We define the impedance
of an ac circuit as the ratio of the voltage ampli-
tude across the circuit to the current amplitude in the circuit. From Eq. (31.20)
the impedance of the L-R-C series circuit is
(31.21)
so we can rewrite Eq. (31.20) as
(31.22)
While Eq. (31.21) is valid only for an L-R-C series circuit, we can use Eq. (31.22)
to define the impedance of any network of resistors, inductors, and capacitors as
the ratio of the amplitude of the voltage across the network to the current ampli-
tude. The SI unit of impedance is the ohm.
The Meaning of Impedance and Phase Angle
Equation (31.22) has a form similar to 
with impedance 
in an ac circuit
playing the role of resistance 
in a dc circuit. Just as direct current tends to fol-
low the path of least resistance, so alternating current tends to follow the path of
lowest impedance (Fig. 31.14). Note, however, that impedance is actually a func-
tion of 
and 
as well as of the angular frequency 
We can see this by sub-
stituting Eq. (31.12) for 
and Eq. (31.18) for 
into Eq. (31.21), giving the
following complete expression for 
for a series circuit:
(impedance of an L-R-C
series circuit)
(31.23)
= 2R2 + 3vL - 11>vC242
Z = 2R2 + 1XL - XC22
Z
XC
XL
v.
C,
L,
R,
R
Z
V = IR,
V = IZ  (amplitude of voltage across an ac circuit)
Z = 2R2 + 1XL - XC22
Z
V = I 2R2 + 1XL - XC22
V = 2VR
2 + 1VL - VC22 = 21IR22 + 1IXL - IXC22 or
V
VR,
VL - VC.
VL.
VC
vad
v
V
VC.
VL,
VR,
vC.
vL,
vR,
v
vC.
VC
VC = IXC
90°.
vL.
VL
VL = IXL
90°.
vR.
I,
VR
31.14 This gas-filled glass sphere has
an alternating voltage between its surface
and the electrode at its center. The glowing
streamers show the resulting alternating
current that passes through the gas. When
you touch the outside of the sphere, your
fingertips and the inner surface of the
sphere act as the plates of a capacitor, and
the sphere and your body together form an
L-R-C series circuit. The current (which is
low enough to be harmless) is drawn to
your fingers because the path through your
body has a low impedance.
PhET: Circuit Construction Kit (AC+DC)
PhET: Faraday’s Electromagnetic Lab
ActivPhysics 14.3: AC Circuits: The Driven 
Oscillator (Questions 6, 7, and 10)

Hence for a given amplitude 
of the source voltage applied to the circuit, the
amplitude 
of the resulting current will be different at different frequen-
cies. We’ll explore this frequency dependence in detail in Section 31.5.
In the phasor diagram shown in Fig. 31.13b, the angle 
between the voltage
and current phasors is the phase angle of the source voltage 
with respect to the
current 
that is, it is the angle by which the source voltage leads the current.
From the diagram,
(31.24)
If the current is 
then the source voltage is
(31.25)
Figure 31.13b shows the behavior of a circuit in which 
Figure
31.13c shows the behavior when 
the voltage phasor 
lies on the oppo-
site side of the current phasor 
and the voltage lags the current. In this case,
is negative, tan 
is negative, and 
is a negative angle between 0 and
Since 
and 
depend on frequency, the phase angle 
depends on fre-
quency as well. We’ll examine the consequences of this in Section 31.5.
All of the expressions that we’ve developed for an L-R-C series circuit are still
valid if one of the circuit elements is missing. If the resistor is missing, we set
if the inductor is missing, we set 
But if the capacitor is missing,
we set 
corresponding to the absence of any potential difference
or any capacitive reactance 
In this entire discussion we have described magnitudes of voltages and cur-
rents in terms of their maximum values, the voltage and current amplitudes. But
we remarked at the end of Section 31.1 that these quantities are usually described
in terms of rms values, not amplitudes. For any sinusoidally varying quantity, the
rms value is always 
times the amplitude. All the relationships between
voltage and current that we have derived in this and the preceding sections are
still valid if we use rms quantities throughout instead of amplitudes. For exam-
ple, if we divide Eq. (31.22) by 
we get
which we can rewrite as
(31.26)
We can translate Eqs. (31.7),  (31.13), and  (31.19) in exactly the same way.
We have considered only ac circuits in which an inductor, a resistor, and a
capacitor are in series. You can do a similar analysis for an L-R-C parallel circuit;
see Problem 31.56.
Finally, we remark that in this section we have been describing the steady-
state condition of a circuit, the state that exists after the circuit has been con-
nected to the source for a long time. When the source is first connected, there
may be additional voltages and currents, called transients, whose nature depends
on the time in the cycle when the circuit is initially completed. A detailed analysis
of transients is beyond our scope. They always die out after a sufficiently long
time, and they do not affect the steady-state behavior of the circuit. But they can
cause dangerous and damaging surges in power lines, which is why delicate elec-
tronic systems such as computers are often provided with power-line surge
protectors.
Vrms = IrmsZ
V
12 =
I
12 Z
12,
1> 12
1XC = 1>vC = 02.
1vC = q>C = 02
C = q,
L = 0.
R = 0;
f
XC
XL
-90°.
f
f
XL - XC
I
V
XL 6 XC;
XL 7 XC.
v = Vcos1vt + f2
v
i = Icosvt,
tanf =
vL - 1>vC
R
   (phase angle of an L-R-C series circuit2
tanf = VL - VC
VR
=
I1XL - XC2
IR
= XL - XC
R
i;
v
f
I = V>Z
V
1032
CHAPTER 31 Alternating Current
Application Measuring Body Fat by
Bioelectric Impedance Analysis
The electrodes attached to this overweight
patient’s chest are applying a small ac voltage
of frequency 50 kHz. The attached instrumen-
tation measures the amplitude and phase
angle of the resulting current through the
patient’s body. These depend on the relative
amounts of water and fat along the path fol-
lowed by the current, and so provide a sensi-
tive measure of body composition.

31.3 The L-R-C Series Circuit
1033
Problem-Solving Strategy 31.1
Alternating-Current Circuits
IDENTIFY the relevant concepts: In analyzing ac circuits, we can
apply all of the concepts used to analyze direct-current circuits,
particularly those in Problem-Solving Strategies 26.1 and 26.2.
But now we must distinguish between the amplitudes of alternating
currents and voltages and their instantaneous values, and among
resistance (for resistors), reactance (for inductors or capacitors),
and impedance (for composite circuits).
SET UP the problem using the following steps:
1. Draw a diagram of the circuit and label all known and unknown
quantities.
2. Identify the target variables.
EXECUTE the solution as follows:
1. Use the relationships derived in Sections 31.2 and 31.3 to solve
for the target variables, using the following hints.
2. It’s almost always easiest to work with angular frequency
rather than ordinary frequency 
3. Keep in mind the following phase relationships: For a resistor,
voltage and current are in phase, so the corresponding phasors
always point in the same direction. For an inductor, the voltage
leads the current by 
(i.e., 
radians), so
the voltage phasor points 
counterclockwise from the cur-
rent phasor. For a capacitor, the voltage lags the current by 
(i.e., 
radians), so the voltage phasor points
clockwise from the current phasor.
90°
-p>2
f = -90° =
90°
90°
= p>2
f = +90°
90°
ƒ.
v = 2pƒ
4. Kirchhoff’s rules hold at each instant. For example, in a series
circuit, the instantaneous current is the same in all circuit ele-
ments; in a parallel circuit, the instantaneous potential differ-
ence is the same across all circuit elements.
5. Inductive reactance, capacitive reactance, and impedance are
analogous to resistance; each represents the ratio of voltage
amplitude 
to current amplitude in a circuit element or com-
bination of elements. However, phase relationships are crucial.
In applying Kirchhoff’s loop rule, you must combine the
effects of resistance and reactance by vector addition of the cor-
responding voltage phasors, as in Figs. 31.13b and 31.13c.
When you have several circuit elements in series, for example,
you can’t just add all the numerical values of resistance and
reactance to get the impedance; that would ignore the phase
relationships.
EVALUATE your answer: When working with an L-R-C series cir-
cuit, you can check your results by comparing the values of the
inductive and capacitive reactances 
and 
If 
then
the voltage amplitude across the inductor is greater than that across
the capacitor and the phase angle 
is positive (between 0 and 
).
If 
then the voltage amplitude across the inductor is less
than that across the capacitor and the phase angle 
is negative
(between 0 and 
).
-90°
f
XL 6 XC,
90°
f
XL 7 XC,
XC.
XL
I
V
