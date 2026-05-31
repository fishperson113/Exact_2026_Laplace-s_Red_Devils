Example 31.1
Current in a personal computer
The plate on the back of a personal computer says that it draws 
2.7 A from a 120-V, 60-Hz line. For this computer, what are (a) the
average current, (b) the average of the square of the current, and
(c) the current amplitude?
SOLUTION
IDENTIFY and SET UP: This example is about alternating current.
In part (a) we find the average, over a complete cycle, of the alter-
nating current. In part (b) we recognize that the 2.7-A current draw
of the computer is the rms value 
-that is, the square root of
the mean (average) of the square of the current, 
. In part (c)
we use Eq. (31.4) to relate 
to the current amplitude.
EXECUTE: (a) The average of any sinusoidally varying quantity,
over any whole number of cycles, is zero.
(b) We are given 
. From the definition of rms
value,
(c) From Eq. (31.4), the current amplitude is
Figure 31.6 shows graphs of and 
versus time t.
i2
i
I = 12Irms = 1212.7 A2 = 3.8 A
I
Irms = 21i22av so 1i22av = 1Irms22 = 12.7 A22 = 7.3 A2
Irms = 2.7 A
Irms
1i22av
Irms
EVALUATE: Why would we be interested in the average of the
square of the current? Recall that the rate at which energy is dissi-
pated in a resistor 
equals 
This rate varies if the current 
is alternating, so it is best described by its average value 
We’ll use this idea in Section 31.4.
I rms
2R.
1i22avR =
i2R.
R
31.6 Our graphs of the current and the square of the current 
versus time t.
i2
i
Test Your Understanding of Section 31.1
The figure at left shows four dif-
ferent current phasors with the same angular frequency 
At the time shown, which pha-
sor corresponds to (a) a positive current that is becoming more positive; (b) a positive
current that is decreasing toward zero; (c) a negative current that is becoming more nega-
tive; (d) a negative current that is decreasing in magnitude toward zero?
❙
v.
31.2 Resistance and Reactance
In this section we will derive voltage-current relationships for individual circuit
elements carrying a sinusoidal current. We’ll consider resistors, inductors, and
capacitors.
B
A
D
C
v
I
I
I
I

31.2 Resistance and Reactance
1025
Resistor in an ac Circuit
First let’s consider a resistor with resistance 
through which there is a sinusoidal
current given by Eq. (31.2): 
The positive direction of current is
counterclockwise around the circuit, as in Fig. 31.7a. The current amplitude
(maximum current) is 
From Ohm’s law the instantaneous potential 
of point
with respect to point (that is, the instantaneous voltage across the resistor) is
(31.6)
The maximum voltage 
the voltage amplitude, is the coefficient of the cosine
function:
(31.7)
Hence we can also write
(31.8)
The current and voltage 
are both proportional to 
so the current is in
phase with the voltage. Equation (31.7) shows that the current and voltage ampli-
tudes are related in the same way as in a dc circuit.
Figure 31.7b shows graphs of and 
as functions of time. The vertical scales
for current and voltage are different, so the relative heights of the two curves are
not significant. The corresponding phasor diagram is given in Fig. 31.7c. Because
and 
are in phase and have the same frequency, the current and voltage pha-
sors rotate together; they are parallel at each instant. Their projections on the hor-
izontal axis represent the instantaneous current and voltage, respectively.
Inductor in an ac Circuit
Next, we replace the resistor in Fig. 31.7 with a pure inductor with self-inductance
and zero resistance (Fig. 31.8a). Again we assume that the current is 
with the positive direction of current taken as counterclockwise around
the circuit.
Although there is no resistance, there is a potential difference 
between the
inductor terminals 
and 
because the current varies with time, giving rise to a
self-induced emf. The induced emf in the direction of is given by Eq. (30.7),
however, the voltage 
is not simply equal to 
To see why,
notice that if the current in the inductor is in the positive (counterclockwise)
direction from a to b and is increasing, then 
is positive and the induced emf
is directed to the left to oppose the increase in current; hence point a is at higher
potential than is point b. Thus the potential of point a with respect to point b is
positive and is given by 
the negative of the induced emf. (You
vL = +L di>dt,
di>dt
E.
vL
E = -L di>dt;
i
b
a
vL
Icosvt,
i =
L
vR
i
vR
i
cosvt,
vR
i
vR = VRcosvt
VR = IR  (amplitude of voltage across a resistor, ac circuit)
VR,
vR = iR = 1IR2cosvt
b
a
vR
I.
i = Icosvt.
R
Voltage curve leads current curve by a quarter-
cycle (corresponding to f 5 p/2 rad 5 90°).
Voltage phasor leads current phasor
by f 5 p/2 rad 5 90°.
O
i
vL
VL
I
vt
Current
phasor
Phase
angle f
Voltage
phasor
(c) Phasor diagram
I
VL
O
i, v
t
1
4 T,
rad 5 90°
p
2
(b) Graphs of current and voltage versus time
i 5 I cos vt
vL 5 IvLcos 1vt 1 90°2
i
a
L
b
vL
(a) Circuit with ac source and inductor
31.8 Inductance 
connected across an ac source.
L
Amplitudes are in the
same relationship as for
a dc circuit: VR 5 IR.
Current is in phase
with voltage: crests and
troughs occur together.
Current and voltage
phasors are in phase:
they rotate together.
i
a
R
vR
b
(a) Circuit with ac source and resistor
(b) Graphs of current and voltage versus time
I
VR
O
i, v
i 5 I cos vt
vR 5 IR cos vt 5 VR cos vt
t
O
i
vR
VR
I
vt
Current
phasor
Voltage
phasor
Instantaneous
voltage
Instantaneous
current
(c) Phasor diagram
31.7 Resistance 
connected
across an ac source.
R

should convince yourself that this expression gives the correct sign of 
in all
cases, including counterclockwise and decreasing, clockwise and increasing,
and clockwise and decreasing; you should also review Section 30.2.) So we have
(31.9)
The voltage 
across the inductor at any instant is proportional to the rate of
change of the current. The points of maximum voltage on the graph correspond
to maximum steepness of the current curve, and the points of zero voltage are the
points where the current curve instantaneously levels off at its maximum and
minimum values (Fig. 31.8b). The voltage and current are “out of step” or out of
phase by a quarter-cycle. Since the voltage peaks occur a quarter-cycle earlier
than the current peaks, we say that the voltage leads the current by 
The pha-
sor diagram in Fig. 31.8c also shows this relationship; the voltage phasor is ahead
of the current phasor by 
We can also obtain this phase relationship by rewriting Eq. (31.9) using the
identity
(31.10)
This result shows that the voltage can be viewed as a cosine function with a
“head start” of 
relative to the current.
As we have done in Eq. (31.10), we will usually describe the phase of the
voltage relative to the current, not the reverse. Thus if the current in a circuit is
and the voltage of one point with respect to another is
we call 
the phase angle; it gives the phase of the voltage relative to the
current. For a pure resistor, 
and for a pure inductor, 
From Eq. (31.9) or  (31.10) the amplitude 
of the inductor voltage is
(31.11)
We define the inductive reactance
of an inductor as
(31.12)
Using 
we can write Eq. (31.11) in a form similar to Eq. (31.7) for a resistor
(31.13)
Because 
is the ratio of a voltage and a current, its SI unit is the ohm, the same
as for resistance.
CAUTION
Inductor voltage and current are not in phase Keep in mind that Eq. (31.13)
is a relationship between the amplitudes of the oscillating voltage and current for the
inductor in Fig. 31.8a. It does not say that the voltage at any instant is equal to the current
at that instant multiplied by 
As Fig. 31.8b shows, the voltage and current are 
out of
phase. Voltage and current are in phase only for resistors, as in Eq. (31.6). ❙
The Meaning of Inductive Reactance
The inductive reactance 
is really a description of the self-induced emf that
opposes any change in the current through the inductor. From Eq. (31.13), for a
given current amplitude the voltage 
across the inductor and the
self-induced emf 
both have an amplitude 
that is directly propor-
tional to 
According to Eq. (31.12), the inductive reactance and self-induced
emf increase with more rapid variation in current (that is, increasing angular fre-
quency ) and increasing inductance L.
v
XL.
VL
E = -L di>dt
vL = +L di>dt
I
XL
90°
XL.
XL
VL = IXL  (amplitude of voltage across an inductor, ac circuit)
1VR = IR2:
XL,
XL = vL  (inductive reactance)
XL
VL = IvL
VL
f = 90°.
f = 0,
f
v = Vcos1vt + f2
v
i = Icosvt
i
90°
vL = IvLcos1vt + 90°2
cos1A + 90°2 = -sin A:
90°.
90°.
vL
vL = L di
dt = L d
dt 1Icosvt2 = -IvLsinvt
i
i
i
vL
1026
CHAPTER 31 Alternating Current
ActivPhysics 14.3: AC Circuits: The Driven
Oscillator (Questions 1-5)

31.2 Resistance and Reactance
1027
If an oscillating voltage of a given amplitude 
is applied across the inductor
terminals, the resulting current will have a smaller amplitude for larger values of
Since 
is proportional to frequency, a high-frequency voltage applied to the
inductor gives only a small current, while a lower-frequency voltage of the same
amplitude gives rise to a larger current. Inductors are used in some circuit applica-
tions, such as power supplies and radio-interference filters, to block high frequen-
cies while permitting lower frequencies or dc to pass through. A circuit device that
uses an inductor for this purpose is called a low-pass filter (see Problem 31.52).
XL
XL.
I
VL
