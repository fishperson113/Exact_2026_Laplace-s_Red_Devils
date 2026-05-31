Example 31.7
Power in an L-R-C series circuit
For the L-R-C series circuit of Example 31.4, (a) calculate the
power factor and (b) calculate the average power delivered to the
entire circuit and to each circuit element.
SOLUTION
IDENTIFY and SET UP: We can use the results of Example 31.4.
The power factor is the cosine of the phase angle 
and we use
Eq. (31.31) to find the average power delivered in terms of 
and
the amplitudes of voltage and current.
f
f,
EXECUTE: (a) The power factor is 
(b) From Eq. (31.31),
EVALUATE: Although 
is the average power delivered to the 
L-R-C combination, all of this power is dissipated in the resistor.
As Figs. 31.16b and 31.16c show, the average power delivered to a
pure inductor or pure capacitor is always zero.
Pav
Pav = 1
2 VIcosf = 1
2 150 V210.10 A210.602 = 1.5 W
cosf = cos53° = 0.60.
Test Your Understanding of Section 31.4
Figure 31.16d shows that
during part of a cycle of oscillation, the instantaneous power delivered to the cir-
cuit is negative. This means that energy is being extracted from the circuit. 
(a) Where is the energy extracted from? (i) the resistor; (ii) the inductor; (iii) the 
capacitor; (iv) the ac source; (v) more than one of these. (b) Where does the energy go?
(i) the resistor; (ii) the inductor; (iii) the capacitor; (iv) the ac source; (v) more than one
of these.
❙
?
ActivPhysics 14.3: AC Circuits: The Driven
Oscillator (Questions 8, 9, and 11)

and 
are equal and 
is zero. At this frequency the impedance
has its smallest value, equal simply to the resistance 
Circuit Behavior at Resonance
As we vary the angular frequency 
of the source, the current amplitude 
varies as shown in Fig. 31.18b; the maximum value of occurs at the frequency at
which the impedance 
is minimum. This peaking of the current amplitude at a
certain frequency is called resonance. The angular frequency 
at which the
resonance peak occurs is called the resonance angular frequency. This is the
angular frequency at which the inductive and capacitive reactances are equal, so
at resonance,
(L-R-C series circuit 
at resonance)
(31.32)
Note that this is equal to the natural angular frequency of oscillation of an L-C
circuit, which we derived in Section 30.5, Eq. (30.22). The resonance frequency
is 
This is the frequency at which the greatest current appears in the cir-
cuit for a given source voltage amplitude; in other words, 
is the frequency to
which the circuit is “tuned.”
It’s instructive to look at what happens to the voltages in an L-R-C series circuit
at resonance. The current at any instant is the same in 
and 
The voltage across
an inductor always leads the current by 
or cycle, and the voltage across a
capacitor always lags the current by 
Therefore the instantaneous voltages
across and 
always differ in phase by 
or cycle; they have opposite signs
at each instant. At the resonance frequency, and only at the resonance frequency,
and the voltage amplitudes 
and 
are equal; then the
instantaneous voltages across 
and 
add to zero at each instant, and the total
voltage 
across the L-C combination in Fig. 31.13a is exactly zero. The voltage
across the resistor is then equal to the source voltage. So at the resonance fre-
quency the circuit behaves as if the inductor and capacitor weren’t there at all!
The phase of the voltage relative to the current is given by Eq. (31.24). At fre-
quencies below resonance, 
is greater than 
the capacitive reactance domi-
nates, the voltage lags the current, and the phase angle 
is between zero and
Above resonance, the inductive reactance dominates, the voltage leads the
current, and the phase angle 
is between zero and 
Figure 31.18b shows
this variation of 
with angular frequency.
Tailoring an ac Circuit
If we can vary the inductance or the capacitance 
of a circuit, we can also vary
the resonance frequency. This is exactly how a radio or television receiving set is
“tuned” to receive a particular station. In the early days of radio this was accom-
plished by the use of capacitors with movable metal plates whose overlap could
be varied to change 
(This is what is being done with the radio tuning knob
shown in the photograph that opens this chapter.) A more modern approach is to
vary 
by using a coil with a ferrite core that slides in or out.
In an L-R-C series circuit the impedance reaches its minimum value and the
current its maximum value at the resonance frequency. The middle curve in 
Fig. 31.19 is a graph of current as a function of frequency for such a circuit, with
source voltage amplitude 
and
This curve is called a response curve or a resonance curve. The resonance angu-
lar frequency is 
As we expect, the curve has a peak
at this angular frequency.
The resonance frequency is determined by 
and 
what happens when we
change 
Figure 31.19 also shows graphs of 
as a function of 
for 
and for 
The curves are similar for frequencies far away
R = 2000 Æ.
200 Æ
R =
v
I
R?
C;
L
v0 = 1LC2-1>2 = 1000 rad>s.
R = 500 Æ.
C = 0.50 mF,
L = 2.0 H,
V = 100 V,
L
C.
C
L
f
+90°.
f
-90°.
f
XL;
XC
vbd
C
L
VC = IXC
VL = IXL
XL = XC
1
2
180°,
C
L
90°.
1
4
90°,
C.
L
f0
v0>2p.
f0
XL = XC  v0L =
1
v0C  v0 =
1
1LC
v0
Z
I
I = V>Z
v
R.
2R2 + 1XL - XC22
Z =
XL - XC
XC
XL
1038
CHAPTER 31 Alternating Current
Impedance Z is least at the angular
frequency at which XC 5 XL.
Current peaks at the angular frequency
at which impedance is least. This is the
resonance angular frequency v0.
Logarithmic
scale
Logarithmic
scale
R, X, Z
XC
XL
R
log v
XL 2 XC
O
Z 5 R2 1 (XL 2 XC)2
v0
(a) Reactance, resistance, and impedance as
functions of angular frequency
I, Z
I
Z
O
90°
f
f
f
290°
log v
v0
(b) Impedance, current, and phase angle as
functions of angular frequency
31.18 How variations in the angular
frequency of an ac circuit affect (a) reac-
tance, resistance, and impedance, and (b)
impedance, current amplitude, and phase
angle.
The lower a circuit’s
resistance, the higher
and sharper is the
resonance peak in the
current near the
resonance angular
frequency v0.
I (A)
200 V
0.5
0.4
0.3
0.2
0.1
v (rad/s)
500
1000
1500
2000
O
2000 V
500 V
31.19 Graph of current amplitude as a
function of angular frequency 
for an 
L-R-C series circuit with 
and three differ-
ent values of the resistance R.
C = 0.50 mF,
L = 2.0 H,
V = 100 V,
v
I

31.5 Resonance in Alternating-Current Circuits
1039
from resonance, where the impedance is dominated by 
or 
But near reso-
nance, where 
and 
nearly cancel each other, the curve is higher and more
sharply peaked for small values of 
and broader and flatter for large values of 
At resonance, 
and 
so the maximum height of the curve is
inversely proportional to 
The shape of the response curve is important in the design of radio and televi-
sion receiving circuits. The sharply peaked curve is what makes it possible to dis-
criminate between two stations broadcasting on adjacent frequency bands. But if
the peak is too sharp, some of the information in the received signal is lost, such
as the high-frequency sounds in music. The shape of the resonance curve is also
related to the overdamped and underdamped oscillations that we described in
Section 30.6. A sharply peaked resonance curve corresponds to a small value of 
and a lightly damped oscillating system; a broad, flat curve goes with a large
value of 
and a heavily damped system.
In this section we have discussed resonance in an L-R-C series circuit. Reso-
nance can also occur in an ac circuit in which the inductor, resistor, and capacitor
are connected in parallel. We leave the details to you (see Problem 31.57).
Resonance phenomena occur not just in ac circuits, but in all areas of physics.
We discussed examples of resonance in mechanical systems in Sections 13.8 and
16.5. The amplitude of a mechanical oscillation peaks when the driving-force fre-
quency is close to a natural frequency of the system; this is analogous to the
peaking of the current in an L-R-C series circuit. We suggest that you review the
sections on mechanical resonance now, looking for the analogies.
R
R
R.
I = V>R,
Z = R
R.
R
XC
XL
XC.
XL
