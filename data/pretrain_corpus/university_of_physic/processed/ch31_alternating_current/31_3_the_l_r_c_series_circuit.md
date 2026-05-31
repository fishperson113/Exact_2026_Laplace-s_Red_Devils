1030

CHAPTER 31 Alternating Current

31.12 (a) The two speakers in this loud-
speaker system are connected in parallel to
the ampliﬁer. (b) Graphs of current ampli-
tude in the tweeter and woofer as functions
of frequency for a given ampliﬁer voltage
amplitude.

(a) A crossover network in a loudspeaker system

From
amplifier

V

A

B

C

R

R

L

Tweeter

Woofer

(b) Graphs of rms current as functions of
frequency for a given amplifier voltage

Irms

The inductor and capacitor feed low
frequencies mainly to the woofer and
high frequencies mainly to the tweeter.

Tweeter

Woofer

f

Crossover
point

O

output. The capacitor in the tweeter branch blocks the low-frequency components
of  sound  but  passes  the  higher  frequencies;  the  inductor  in  the  woofer  branch
does the opposite.

Test Your Understanding of Section 31.2 An oscillating voltage of
ﬁxed amplitude is applied across a circuit element. If the frequency of this voltage
is increased, will the amplitude of the current through the element (i) increase,
(ii) decrease, or (iii) remain the same if it is (a) a resistor, (b) an inductor, or
(c) a capacitor?

❙

31.3 The L-R-C Series Circuit

Many ac circuits used in practical electronic systems involve resistance, induc-
tive reactance, and capacitive reactance. Figure 31.13a shows a simple example:
A series circuit containing a resistor, an inductor, a capacitor, and an ac source.
(In Section 30.6 we considered the behavior of the current in an L-R-C series cir-
cuit without a source.)

To analyze this and similar circuits, we will use a phasor diagram that includes
the  voltage  and  current  phasors  for  each  of  the  components.  In  this  circuit,
because  of  Kirchhoff’s  loop  rule,  the  instantaneous  total voltage
across  all
three components is equal to the source voltage at that instant. We will show that
the phasor representing this total voltage is the vector sum of the phasors for the
individual voltages.

vad

Figures 31.13b and 31.13c show complete phasor diagrams for the circuit of
i = I cos vt.
Fig. 31.13a. We assume that the source supplies a current  given by
Because the circuit elements are connected in series, the current at any instant is
the same at every point in the circuit. Thus a single phasor I, with length propor-
tional to the current amplitude, represents the current in all circuit elements.

i

As in Section 31.2, we use the symbols
and

vR,
and the symbols
voltages across
voltages. We denote the instantaneous and maximum source voltages by  and
Then, in Fig. 31.13a,

for the instantaneous
VC
for the maximum
v
V.

and
VL,

vC
and

vL,
VR,

L,R,

and

C,

vR = vab,

vC = vcd.

vL = vbc,

v = vad,

We have shown that the potential difference between the terminals of a resis-
is

tor is in phase with the current in the resistor and that its maximum value
given by Eq. (31.7):

VR

31.13 An L-R-C series circuit with an ac source.

(a) L-R-C series circuit

(b) Phasor diagram for the case XL

. XC

(c) Phasor diagram for the case XL

, XC

VR = IR

i

a

R

b

L

2q

q

d

c

C

Source voltage phasor is the vector
sum of the VR, VL, and VC phasors.

Inductor voltage
phasor leads
current
phasor
by 90°.

VL

5 IXL

All circuit
elements have
the same
current phasor.

V 5 IZ

VL

2 VC

I

f

5 IR

VR

vt

O

Capacitor voltage
phasor lags
current phasor
by 90°. It is thus always
antiparallel to the VL phasor.

5 IXC

VC

Resistor voltage
phasor is in
phase with
current phasor.

, XC, the source voltage phasor lags the

If XL
current phasor, X , 0, and f is a negative angle
between 0 and 290°.

I

VR

5 IR

f

V 5 IZ

VL

5 IXL

vt

2 VC

O

VL
5 IXC

VC

31.3 The L-R-C Series Circuit

1031

PhET: Circuit Construction Kit (AC+DC)
PhET: Faraday’s Electromagnetic Lab
ActivPhysics 14.3: AC Circuits: The Driven
Oscillator (Questions 6, 7, and 10)

31.14 This gas-ﬁlled glass sphere has
an alternating voltage between its surface
and the electrode at its center. The glowing
streamers show the resulting alternating
current that passes through the gas. When
you touch the outside of the sphere, your
ﬁngertips and the inner surface of the
sphere act as the plates of a capacitor, and
the sphere and your body together form an
L-R-C series circuit. The current (which is
low enough to be harmless) is drawn to
your ﬁngers because the path through your
body has a low impedance.

VR

The phasor
represents the
in Fig. 31.13b, in phase with the current phasor
voltage across the resistor. Its projection onto the horizontal axis at any instant
gives the instantaneous potential difference

I,

vR.

The voltage across an inductor leads the current by

90°.

Its voltage amplitude

is given by Eq. (31.13):

VL = IXL

in Fig. 31.13b represents the voltage across the inductor, and its

VL

The phasor
projection onto the horizontal axis at any instant equals
The voltage across a capacitor lags the current by
90°.

vL.

Its voltage amplitude is

given by Eq. (31.19):

VC = IXC

The phasor
projection onto the horizontal axis at any instant equals

in Fig. 31.13b represents the voltage across the capacitor, and its

VC

vC.

v
The instantaneous potential difference  between terminals a and d is equal at
vC.
every instant to the (algebraic) sum of the potential differences
and
That is, it equals the sum of the projections of the phasors
But the
VL,
sum of the projections of these phasors is equal to the projection of their vector
v
sum. So the vector sum  must be the phasor that represents the source voltage
and the instantaneous total voltage

across the series of elements.

vR,
and

vL,
VC.

VR,

V

vad

To form this vector sum, we ﬁrst subtract the phasor

VL.
(These  two  phasors  always  lie  along  the  same  line,  with  opposite  directions.)
This gives the phasor
so
from the Pythagorean theorem the magnitude of the phasor

This is always at right angles to the phasor

from the phasor

VL - VC.

VR,

VC

is

V

2 + 1VL - VC22 = 21IR22 + 1IXL - IXC22  or

V = 2V R
V = I 2R2 + 1XL - XC22

(31.20)

We deﬁne the impedance

of an ac circuit as the ratio of the voltage ampli-
tude across the circuit to the current amplitude in the circuit. From Eq. (31.20)
the impedance of the L-R-C series circuit is

Z

Z = 2R2 + 1XL - XC22

(31.21)

so we can rewrite Eq. (31.20) as

V = IZ    (amplitude of voltage across an ac circuit)

(31.22)

While Eq. (31.21) is valid only for an L-R-C series circuit, we can use Eq. (31.22)
to deﬁne the impedance of any network of resistors, inductors, and capacitors as
the ratio of the amplitude of the voltage across the network to the current ampli-
tude. The SI unit of impedance is the ohm.

V = IR,

The Meaning of Impedance and Phase Angle
in an ac circuit
with impedance
Equation (31.22) has a form similar to
playing the role of resistance
in a dc circuit. Just as direct current tends to fol-
low the path of least resistance, so alternating current tends to follow the path of
lowest impedance (Fig. 31.14). Note, however, that impedance is actually a func-
as well as of the angular frequency  We can see this by sub-
tion of
XC
stituting Eq. (31.12) for
into Eq. (31.21), giving the
following complete expression for

and Eq. (31.18) for

for a series circuit:

L,R,

and

XL

v.

C,

R

Z

Z

Z = 2R2 + 1XL - XC22

= 2R2 + 3vL - 11>vC242

(impedance of an L-R-C
series circuit)

(31.23)

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

Hence for a given amplitude
I = V>Z
amplitude
cies. We’ll explore this frequency dependence in detail in Section 31.5.

of the source voltage applied to the circuit, the
of the resulting current will be different at different frequen-

V

In the phasor diagram shown in Fig. 31.13b, the angle  between the voltage
and current phasors is the phase angle of the source voltage  with respect to the
i;
current
that  is,  it  is  the  angle  by  which  the  source  voltage  leads  the  current.
From the diagram,

v

f

tan f =

VL - VC
VR

=

I1XL - XC2
IR

=

XL - XC
R

tan f =

vL - 1>vC
R

     (phase angle of an L-R-C series circuit2

(31.24)

If the current is

i = I cos vt,

then the source voltage

v

is

v = V cos1vt + f2

(31.25)

XL 7 XC.
Figure
Figure  31.13b  shows  the  behavior  of  a  circuit  in  which
lies on the oppo-
31.13c shows the behavior when
V
the voltage phasor
I
site  side  of  the  current  phasor  and  the  voltage  lags the  current.  In  this  case,
XL - XC
is a negative angle between 0 and
-90°.
f
depends on fre-
quency as well. We’ll examine the consequences of this in Section 31.5.

depend on frequency, the phase angle

is negative, tan
and

is negative, and

XL 6 XC;

Since

XC

XL

f

f

All of the expressions that we’ve developed for an L-R-C series circuit are still
valid if one of the circuit elements is missing. If the resistor is missing, we set
R = 0;
But if the capacitor is missing,
if the inductor is missing, we set
C = q,
corresponding  to  the  absence  of  any  potential  difference
we  set
1vC = q>C = 02
or any capacitive reactance

1XC = 1>vC = 02.

L = 0.

In this entire discussion we have described magnitudes of voltages and cur-
rents in terms of their maximum values, the voltage and current amplitudes. But
we remarked at the end of Section 31.1 that these quantities are usually described
in terms of rms values, not amplitudes. For any sinusoidally varying quantity, the
rms  value  is  always
times  the  amplitude. All  the  relationships  between
voltage and current that we have derived in this and the preceding sections are
still valid if we use rms quantities throughout instead of amplitudes. For exam-
we get
ple, if we divide Eq. (31.22) by

1> 12

12 ,

which we can rewrite as

V
12

= I
12

Z

Vrms = IrmsZ

(31.26)

We can translate Eqs. (31.7),  (31.13), and  (31.19) in exactly the same way.

We  have  considered  only  ac  circuits  in  which  an  inductor,  a  resistor,  and  a
capacitor are in series. You can do a similar analysis for an L-R-C parallel circuit;
see Problem 31.56.

Finally,  we  remark  that  in  this  section  we  have  been  describing  the  steady-
state condition  of  a  circuit,  the  state  that  exists  after  the  circuit  has  been  con-
nected  to  the  source  for  a  long  time. When  the  source  is  ﬁrst  connected,  there
may be additional voltages and currents, called transients, whose nature depends
on the time in the cycle when the circuit is initially completed. A detailed analysis
of transients is beyond our scope. They always die out after a sufﬁciently long
time, and they do not affect the steady-state behavior of the circuit. But they can
cause dangerous and damaging surges in power lines, which is why delicate elec-
tronic  systems  such  as  computers  are  often  provided  with  power-line  surge
protectors.

Problem-Solving Strategy 31.1

Alternating-Current Circuits

31.3 The L-R-C Series Circuit

1033

IDENTIFY the relevant concepts: In analyzing ac circuits, we can
apply  all  of  the  concepts  used  to  analyze  direct-current  circuits,
particularly  those  in  Problem-Solving  Strategies  26.1  and  26.2.
But now we must distinguish between the amplitudes of alternating
currents  and  voltages  and  their  instantaneous  values,  and  among
resistance  (for  resistors),  reactance  (for  inductors  or  capacitors),
and impedance (for composite circuits).

SET UP the problem using the following steps:
1. Draw a diagram of the circuit and label all known and unknown

quantities.

2. Identify the target variables.

EXECUTE the solution as follows:
1. Use the relationships derived in Sections 31.2 and 31.3 to solve

for the target variables, using the following hints.

2. It’s  almost  always  easiest  to  work  with  angular  frequency

v = 2pƒ

rather than ordinary frequency

ƒ.

3. Keep in mind the following phase relationships: For a resistor,
voltage and current are in phase, so the corresponding phasors
always point in the same direction. For an inductor, the voltage
f = + 90°
= p>2
90°
leads the  current  by
radians),  so
the  voltage  phasor  points
counterclockwise  from  the  cur-
90°
rent phasor. For a capacitor, the voltage lags the current by
radians), so the voltage phasor points
(i.e.,
90°

f = - 90° =
-p>2
clockwise from the current phasor.

(i.e.,
90°

Example 31.4

An L-R-C series circuit I

4. Kirchhoff’s rules hold at each instant. For example, in a series
circuit, the instantaneous current is the same in all circuit ele-
ments;  in  a  parallel  circuit,  the  instantaneous  potential  differ-
ence is the same across all circuit elements.

I

V

to current amplitude

5. Inductive  reactance,  capacitive  reactance,  and  impedance  are
analogous  to  resistance;  each  represents  the  ratio  of  voltage
amplitude
in a circuit element or com-
bination of elements. However, phase relationships are crucial.
In  applying  Kirchhoff’s  loop  rule,  you  must  combine  the
effects of resistance and reactance by vector addition of the cor-
responding  voltage  phasors,  as  in  Figs.  31.13b  and  31.13c.
When you have several circuit elements in series, for example,
you  can’t  just  add all  the  numerical  values  of  resistance  and
reactance  to  get  the  impedance;  that  would  ignore  the  phase
relationships.

EVALUATE  your answer: When working with an L-R-C series cir-
cuit,  you  can  check  your  results  by  comparing  the  values  of  the
inductive  and  capacitive  reactances
then
the voltage amplitude across the inductor is greater than that across
f
the capacitor and the phase angle
).
then the voltage amplitude across the inductor is less
If
is  negative
than  that  across  the  capacitor  and  the  phase  angle
(between 0 and

is positive (between 0 and

XL 7 XC,

XL 6 XC,

-90°

and

XC.

90°

XL

If

f

).

In  the  series  circuit  of  Fig.  31.13a,  suppose
L = 60 mH,
Find the reactances
tude
circuit element.

v = 10,000 rad>s.
the current ampli-
XC,
Z,
and the voltage amplitude across each

C = 0.50 mF,
and
XL
f,

V = 50 V,
and
the impedance

R = 300 Æ, With source voltage amplitude
and phase angle
I = V
Z

the phase angle

are

f

I,

V = 50 V

, the current amplitude I

= 0.10 A

= 50 V
500 Æ
XL - XC
R

= arctan

400 Æ
300 Æ

= 53°

f = arctan

SOLUTION

IDENTIFY  and SET  UP: This problem uses the ideas developed in
Section 31.2 and this section about the behavior of circuit elements
in an ac circuit. We use Eqs. (31.12) and  (31.18) to determine
XL
and
and Eq. (31.23) to ﬁnd Z. We then use Eq. (31.22) to ﬁnd
the current amplitude and Eq. (31.24) to ﬁnd the phase angle. The
relationships in Table 31.1 then yield the voltage amplitudes.

XC,

EXECUTE: The inductive and capacitive reactances are

XL = vL = 110,000 rad>s2160 mH2 = 600 Æ
XC = 1
vC

1
110,000 rad>s210.50 * 10-6 F2

=

= 200 Æ

The impedance  of the circuit is then

Z

Z = 2R2 + 1XL - XC22 = 21300 Æ22 + 1600 Æ - 200 Æ22

= 500 Æ

From Table 31.1, the voltage amplitudes
VL,
resistor, inductor, and capacitor, respectively, are

VR,

and

VC

across the

VR = IR = 10.10 A21300 Æ2 = 30 V
VL = IXL = 10.10 A21600 Æ2 = 60 V
VC = IXC = 10.10 A21200 Æ2 = 20 V

EVALUATE:  As in Fig. 31.13b,
; hence the voltage ampli-
tude  across  the  inductor  is  greater  than  that  across  the  capacitor
f = 53°
and
means that the voltage leads
the current by

is positive. The value
53°.

f

XL 7 XC

V = 50 V

Note that the source voltage amplitude

is not equal
to the sum of the voltage amplitudes across the separate circuit ele-
ments:
Instead, V is the vector sum
phasors. If you draw the phasor diagram like
of the
Fig.  31.13b  for  this  particular  situation,  you’ll  see  that
VR,
VL - VC,

50 V Z 30 V + 60 V + 20 V.
VR,

and  constitute a 3-4-5 right triangle.

and

VL,

VC

V
