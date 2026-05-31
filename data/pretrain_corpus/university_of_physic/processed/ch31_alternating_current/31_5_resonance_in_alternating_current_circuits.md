SOLUTION

Our  target  variables  are  the  resistance

IDENTIFY  and SET  UP:  We  are  given
120 V.
Irms,
We solve Eq. (31.29) to ﬁnd R, Eq. (31.28) to ﬁnd
and

and the maximum value

, and Eq. (31.30) to ﬁnd

p max

R,

p max .

Pav

Pav = 1500 W

Vrms =
and
the  rms  current
p.
Vrms

from

Irms

of the instantaneous power

EXECUTE: (a) From Eq. (31.29), the resistance is

R =

V  2
rms
Pav

=

1120 V22
1500 W

= 9.6 Æ

(b) From Eq. (31.28),

Irms =

Pav
Vrms

= 1500 W
120 V

= 12.5 A

Example 31.7

Power in an L-R-C series circuit

For  the  L-R-C series  circuit  of  Example  31.4,  (a)  calculate  the
power factor and (b) calculate the average power delivered to the
entire circuit and to each circuit element.

SOLUTION

IDENTIFY  and SET  UP:  We  can  use  the  results  of  Example  31.4.
and we use
The power factor is the cosine of the phase angle
f
Eq. (31.31) to ﬁnd the average power delivered in terms of
and
the amplitudes of voltage and current.

f,

31.5 Resonance in Alternating-Current Circuits

1037

the  phase  angle
neous  power  is
power  is
power
Pav,

(c) For a pure resistor, the voltage and current are in phase and
is  zero.  Hence  from  Eq.  (31.30),  the  instanta-
and  the  maximum  instantaneous
From  Eq.  (31.27),  this  is  twice  the  average

f
p = VI cos2vt

pmax = VI.
so
pmax = VI = 2Pav = 211500 W2 = 3000 W

EVALUATE:  We  can  conﬁrm  our  result  in  part  (b)  by  using  Eq.
(31.7):
12.5  A.  Note  that
some  unscrupulous  manufacturers  of  stereo  ampliﬁers  advertise
the peak power output rather than the lower average value.

1120 V2>19.6 Æ2 =

Vrms>R

Irms

(cid:3)

(cid:3)

EXECUTE: (a) The power factor is

cos f = cos 53° = 0.60.

(b) From Eq. (31.31),

Pav = 1

2 VI cos f = 1

2

150 V210.10 A210.602 = 1.5 W

Pav

EVALUATE:  Although
is  the  average  power  delivered  to  the
L-R-C combination, all of this power is dissipated in the resistor.
As Figs. 31.16b and 31.16c show, the average power delivered to a
pure inductor or pure capacitor is always zero.

Test Your Understanding of Section 31.4 Figure 31.16d shows that
during part of a cycle of oscillation, the instantaneous power delivered to the cir-
cuit is negative. This means that energy is being extracted from the circuit.
(a) Where is the energy extracted from? (i) the resistor; (ii) the inductor; (iii) the
capacitor; (iv) the ac source; (v) more than one of these. (b) Where does the energy go?
(i) the resistor; (ii) the inductor; (iii) the capacitor; (iv) the ac source; (v) more than one
of these.

❙

31.5 Resonance in Alternating-Current Circuits

Much of the practical importance of L-R-C series circuits arises from the way
v.
in which such circuits respond to sources of different angular frequency
For example, one type of tuning circuit used in radio receivers is simply an L-R-C
series  circuit. A radio  signal  of  any  given  frequency  produces  a  current  of  the
same frequency in the receiver circuit, but the amplitude of the current is greatest
if the signal frequency equals the particular frequency to which the receiver cir-
cuit is “tuned.” This effect is called resonance. The circuit is designed so that sig-
nals at other than the tuned frequency produce currents that are too small to make
an audible sound come out of the radio’s speakers.

? ActivPhysics 14.3: AC Circuits: The Driven

Oscillator (Questions 8, 9, and 11)

V

v

To see how an L-R-C series circuit can be used in this way, suppose we con-
nect an ac source with constant voltage amplitude
but adjustable angular fre-
across an L-R-C series circuit. The current that appears in the circuit
quency
I = V>Z,
has the same angular frequency as the source and a current amplitude
where
is the impedance of the L-R-C series circuit. This impedance depends on
XC,
the frequency, as Eq. (31.23) shows. Figure 31.18a shows graphs of
as functions of  We have used a logarithmic angular frequency scale
and
so that we can cover a wide range of frequencies. As the frequency increases,
decreases; hence there is always one frequency at which
XL

increases and

XL,

XC

v.

R,

Z

Z

1038

CHAPTER 31 Alternating Current

31.18 How variations in the angular
frequency of an ac circuit affect (a) reac-
tance, resistance, and impedance, and (b)
impedance, current amplitude, and phase
angle.

(a) Reactance, resistance, and impedance as
functions of angular frequency

Impedance Z is least at the angular
frequency at which XC

5 XL.

R, X, Z

Z 5 (cid:2)R2 1 (XL

2 XC)2

are equal and

and

XL
XC
2R2 + 1XL - XC22

has its smallest value, equal simply to the resistance

is zero. At this frequency the impedance
R.

XL - XC

Z =

Circuit Behavior at Resonance
v
I = V>Z
As we vary the angular frequency  of the source, the current amplitude
varies as shown in Fig. 31.18b; the maximum value of  occurs at the frequency at
is minimum. This peaking of the current amplitude at a
which the impedance
certain  frequency  is  called  resonance. The  angular  frequency
at  which  the
resonance  peak  occurs  is  called  the  resonance  angular frequency. This  is  the
angular frequency at which the inductive and capacitive reactances are equal, so
at resonance,

v0

Z

I

XL = XC    v0L = 1
v0C

    v0 =

1
1LC

(L-R-C series circuit
at resonance)

(31.32)

R

XC

XL

O

v

0

log v

XL

2 XC

Logarithmic
scale

(b) Impedance, current, and phase angle as
functions of angular frequency

Current peaks at the angular frequency
at which impedance is least. This is the
resonance angular frequency v
I, Z

0.

I

Z

f
90°

O

290°
f

v
0

f

log v

Logarithmic
scale

31.19 Graph of current amplitude  as a
function of angular frequency
L-R-C series circuit with
L = 2.0 H,
C = 0.50 mF,
ent values of the resistance R.

v
V = 100 V,
and three differ-

I
for an

I (A)

0.5

0.4

0.3

0.2

0.1

200 V

500 V

2000 V

The lower a circuit’s
resistance, the higher
and sharper is the
resonance peak in the
current near the
resonance angular
frequency v

0.

O

500

1000

1500

2000

v (rad/s)

Note that this is equal to the natural angular frequency of oscillation of an L-C
circuit, which we derived in Section 30.5, Eq. (30.22). The resonance frequency
f0
This is the frequency at which the greatest current appears in the cir-
is the frequency to
cuit for a given source voltage amplitude; in other words,
which the circuit is “tuned.”

v0>2p.

is

f0

1
4

L

L

C

C.

90°,

It’s instructive to look at what happens to the voltages in an L-R-C series circuit
at resonance. The current at any instant is the same in  and  The voltage across
or  cycle, and the voltage across a
an inductor always leads the current by
Therefore  the  instantaneous  voltages
capacitor  always  lags the  current  by
across  and  always differ in phase by
or  cycle; they have opposite signs
at each instant. At the resonance frequency, and only at the resonance frequency,
XL = XC
VL = IXL
are equal; then the
instantaneous voltages across
C
add to zero at each instant, and the total
voltage
across the L-C combination in Fig. 31.13a is exactly zero. The voltage
across  the  resistor  is  then  equal  to  the  source  voltage.  So  at  the  resonance  fre-
quency the circuit behaves as if the inductor and capacitor weren’t there at all!

and the voltage amplitudes
and

VC = IXC

180°,

and

90°.

vbd

L

1
2

The phase of the voltage relative to the current is given by Eq. (31.24). At fre-
the capacitive reactance domi-
is  between  zero  and
Above resonance, the inductive reactance dominates, the voltage leads the
Figure 31.18b shows

XC
quencies below resonance,
nates,  the  voltage  lags the  current,  and  the  phase  angle
-90°.
current, and the phase angle
this variation of  with angular frequency.

is between zero and

is greater than

+90°.

XL;

f

f

f

L

Tailoring an ac Circuit
If we can vary the inductance  or the capacitance  of a circuit, we can also vary
the resonance frequency. This is exactly how a radio or television receiving set is
“tuned” to receive a particular station. In the early days of radio this was accom-
plished by the use of capacitors with movable metal plates whose overlap could
be varied to change
(This is what is being done with the radio tuning knob
shown in the photograph that opens this chapter.) A more modern approach is to
vary  by using a coil with a ferrite core that slides in or out.

C.

C

L

In an L-R-C series circuit the impedance reaches its minimum value and the
current  its  maximum  value  at  the  resonance  frequency.  The  middle  curve  in
Fig. 31.19 is a graph of current as a function of frequency for such a circuit, with
R = 500 Æ.
source voltage amplitude
This curve is called a response curve or a resonance curve. The resonance angu-
As we expect, the curve has a peak
lar frequency is
at this angular frequency.

v0 = 1LC2-1>2 = 1000 rad>s.

C = 0.50 mF,

V = 100 V,

L = 2.0 H,

and

The resonance frequency is determined by

L
Figure  31.19 also  shows  graphs  of

and  what happens when we
R =
I
The  curves  are  similar  for  frequencies  far  away

as  a  function  of

R?
and  for

R = 2000 Æ.

change
200 Æ

for

C;

v

31.5 Resonance in Alternating-Current Circuits

1039

XL

and

from resonance, where the impedance is dominated by
nance, where
sharply peaked for small values of  and broader and ﬂatter for large values of
At  resonance,
inversely proportional to

But near reso-
nearly cancel each other, the curve is higher and more
R.
so  the  maximum  height  of  the  curve  is

R
I = V>R,

and
R.

Z = R

XC.

XC

XL

or

The shape of the response curve is important in the design of radio and televi-
sion receiving circuits. The sharply peaked curve is what makes it possible to dis-
criminate between two stations broadcasting on adjacent frequency bands. But if
the peak is too sharp, some of the information in the received signal is lost, such
as the high-frequency sounds in music. The shape of the resonance curve is also
related  to  the  overdamped  and  underdamped  oscillations  that  we  described  in
R
Section 30.6. A sharply peaked resonance curve corresponds to a small value of
and  a  lightly  damped  oscillating  system;  a  broad,  ﬂat  curve  goes  with  a  large
value of  and a heavily damped system.

R

In this section we have discussed resonance in an L-R-C series circuit. Reso-
nance can also occur in an ac circuit in which the inductor, resistor, and capacitor
are connected in parallel. We leave the details to you (see Problem 31.57).

Resonance phenomena occur not just in ac circuits, but in all areas of physics.
We discussed examples of resonance in mechanical systems in Sections 13.8 and
16.5. The amplitude of a mechanical oscillation peaks when the driving-force fre-
quency  is  close  to  a  natural  frequency  of  the  system;  this  is  analogous  to  the
peaking of the current in an L-R-C series circuit. We suggest that you review the
sections on mechanical resonance now, looking for the analogies.

Example 31.8

Tuning a radio

The series circuit in Fig. 31.20 is similar to some radio tuning cir-
cuits. It is connected to a variable-frequency ac source with an rms
terminal voltage of 1.0 V. (a) Find the resonance frequency. At the
resonance  frequency,  ﬁnd  (b)  the  inductive  reactance
the
and the impedance Z; (c) the rms current
capacitive reactance
Irms

; (d) the rms voltage across each circuit element.

XC,

XL,

SOLUTION

IDENTIFY and SET UP: Figure 31.20 shows an L-R-C series circuit,
with ideal meters inserted to measure the rms current and voltages,
our target variables. Equations (31.32) include the formula for the
from which we ﬁnd the resonance
resonance angular frequency
XC
frequency  We use Eqs. (31.12) and  (31.18) to ﬁnd
,
which are equal at resonance; at resonance, from Eq. (31.23), we

v0,

and

ƒ0.

XL

31.20 A radio tuning circuit at resonance. The circles denote
rms current and voltages.

2.0
mA

a

1.0
V

R 5 500 V L 5 0.40 mH

C 5 100 pF

b

c

d

1.0
V

4.0
V

4.0
V

0
V

=

have Z
voltages across the circuit elements.

R. We use Eqs. (31.7),  (31.13), and  (31.19) to ﬁnd the

EXECUTE: (a) The values of
1
2LC

v0 =

=

1
210.40 * 10-3 H21100 * 10-12 F2

v0

and

ƒ0

are

= 5.0 * 106 rad>s

ƒ0 = 8.0 * 105 Hz = 800 kHz

This frequency is in the lower part of the AM radio band.

(b) At this frequency,
XL = vL = 15.0 * 106 rad>s210.40 * 10-3 H2 = 2000 Æ
XC = 1
1
vC
15.0 * 106 rad>s21100 * 10-12 F2
XL = XC
at resonance as stated above,
(c) From Eq. (31.26) the rms current at resonance is

Z = R = 500 Æ.

= 2000 Æ

=

Since

Irms =

Vrms
Z

=

Vrms
R

= 1.0 V
500 Æ

= 0.0020 A = 2.0 mA

(d) The rms potential difference across the resistor is
VR-rms = IrmsR = 10.0020 A21500 Æ2 = 1.0 V
The rms potential differences across the inductor and capacitor are
VL-rms = IrmsXL = 10.0020 A212000 Æ2 = 4.0 V
VC-rms = IrmsXC = 10.0020 A212000 Æ2 = 4.0 V

EVALUATE:  The  potential  differences  across  the  inductor  and  the
capacitor have equal rms values and amplitudes, but are
out
of phase and so add to zero at each instant. Note also that at reso-
while  in  this
nance,
are both considerably larger than Vrms.
example,

is  equal  to  the  source  voltage

VC-rms

VR-rms

VL-rms

Vrms,

180°

and
