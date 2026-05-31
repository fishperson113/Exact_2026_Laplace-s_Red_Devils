Example 31.8
Tuning a radio
The series circuit in Fig. 31.20 is similar to some radio tuning cir-
cuits. It is connected to a variable-frequency ac source with an rms
terminal voltage of 1.0 V. (a) Find the resonance frequency. At the
resonance frequency, find (b) the inductive reactance 
the
capacitive reactance 
and the impedance Z; (c) the rms current
; (d) the rms voltage across each circuit element.
SOLUTION
IDENTIFY and SET UP: Figure 31.20 shows an L-R-C series circuit,
with ideal meters inserted to measure the rms current and voltages,
our target variables. Equations (31.32) include the formula for the
resonance angular frequency 
from which we find the resonance
frequency 
We use Eqs. (31.12) and  (31.18) to find 
and 
,
which are equal at resonance; at resonance, from Eq. (31.23), we
XC
XL
ƒ0.
v0,
Irms
XC,
XL,
have Z
R. We use Eqs. (31.7),  (31.13), and  (31.19) to find the
voltages across the circuit elements.
EXECUTE: (a) The values of 
and 
are
This frequency is in the lower part of the AM radio band.
(b) At this frequency,
Since 
at resonance as stated above, 
(c) From Eq. (31.26) the rms current at resonance is
(d) The rms potential difference across the resistor is
The rms potential differences across the inductor and capacitor are
EVALUATE: The potential differences across the inductor and the
capacitor have equal rms values and amplitudes, but are 
out
of phase and so add to zero at each instant. Note also that at reso-
nance, 
is equal to the source voltage 
while in this
example, 
and 
are both considerably larger than Vrms.
VC-rms
VL-rms
Vrms,
VR-rms
180°
VL-rms = IrmsXL = 10.0020 A212000 Æ2 = 4.0 V
VC-rms = IrmsXC = 10.0020 A212000 Æ2 = 4.0 V
VR-rms = IrmsR = 10.0020 A21500 Æ2 = 1.0 V
Irms = Vrms
Z
= Vrms
R
= 1.0 V
500 Æ = 0.0020 A = 2.0 mA
Z = R = 500 Æ.
XL = XC
XC =
1
vC =
1
15.0 * 106 rad>s21100 * 10-12 F2
= 2000 Æ
XL = vL = 15.0 * 106 rad>s210.40 * 10-3 H2 = 2000 Æ
ƒ0 = 8.0 * 105 Hz = 800 kHz
= 5.0 * 106 rad>s
v0 =
1
2LC
=
1
210.40 * 10-3 H21100 * 10-12 F2
ƒ0
v0
=
2.0
mA
1.0
V
1.0
V
a
b
c
d
C 5 100 pF
R 5 500 V
L 5 0.40 mH
4.0
V
4.0
V
0
V
31.20 A radio tuning circuit at resonance. The circles denote
rms current and voltages.

31.6 Transformers
One of the great advantages of ac over dc for electric-power distribution is that it
is much easier to step voltage levels up and down with ac than with dc. For long-
distance power transmission it is desirable to use as high a voltage and as small a
current as possible; this reduces 
losses in the transmission lines, and smaller
wires can be used, saving on material costs. Present-day transmission lines rou-
tinely operate at rms voltages of the order of 500 kV. On the other hand, safety
considerations and insulation requirements dictate relatively low voltages in gen-
erating equipment and in household and industrial power distribution. The stan-
dard voltage for household wiring is 120 V in the United States and Canada and
240 V in many other countries. The necessary voltage conversion is accomplished
by the use of transformers.
How Transformers Work
Figure 31.21 shows an idealized transformer. The key components of the trans-
former are two coils or windings, electrically insulated from each other but
wound on the same core. The core is typically made of a material, such as iron,
with a very large relative permeability 
This keeps the magnetic field lines
due to a current in one winding almost completely within the core. Hence almost
all of these field lines pass through the other winding, maximizing the mutual
inductance of the two windings (see Section 30.1). The winding to which power
is supplied is called the primary; the winding from which power is delivered is
called the secondary. The circuit symbol for a transformer with an iron core,
such as those used in power distribution systems, is
Km.
i2R
1040
CHAPTER 31 Alternating Current
Test Your Understanding of Section 31.5
How does the resonance fre-
quency of an L-R-C series circuit change if the plates of the capacitor are brought closer
together? (i) It increases; (ii) it decreases; (iii) it is unaffected.
❙
Here’s how a transformer works. The ac source causes an alternating current
in the primary, which sets up an alternating flux in the core; this induces an emf
in each winding, in accordance with Faraday’s law. The induced emf in the sec-
ondary gives rise to an alternating current in the secondary, and this delivers
energy to the device to which the secondary is connected. All currents and emfs
have the same frequency as the ac source.
Let’s see how the voltage across the secondary can be made larger or smaller
in amplitude than the voltage across the primary. We neglect the resistance of the
windings and assume that all the magnetic field lines are confined to the iron
core, so at any instant the magnetic flux 
is the same in each turn of the pri-
mary and secondary windings. The primary winding has 
turns and the second-
ary winding has 
turns. When the magnetic flux changes because of changing
currents in the two coils, the resulting induced emfs are
(31.33)
The flux per turn
is the same in both the primary and the secondary, so
Eqs. (31.33) show that the induced emf per turn is the same in each. The ratio of
the secondary emf 
to the primary emf 
is therefore equal at any instant to the
ratio of secondary to primary turns:
(31.34)
Since 
and 
both oscillate with the same frequency as the ac source, 
Eq. (31.34) also gives the ratio of the amplitudes or of the rms values of the induced
E2
E1
E2
E1
= N2
N1
E1
E2
£B
E1 = -N1
d£B
dt  and E2 = -N2
d£B
dt
N2
N1
£B
The induced emf per turn is the same in both
coils, so we adjust the ratio of terminal voltages
by adjusting the ratio of turns:
5 N2
N1
V2
V1
R
N2
V2
N1
I1
Primary
winding
Secondary
winding
Iron core
Source of alternating
current
FB
V1
31.21 Schematic diagram of an ideal-
ized step-up transformer. The primary is
connected to an ac source; the secondary is
connected to a device with resistance R.
Application Dangers of ac Versus
dc Voltages
Alternating current at high voltage (above 
500 V) is more dangerous than direct current
at the same voltage. When a person touches
a high-voltage dc source, it usually causes a
single muscle contraction that can be strong
enough to push the person away from the
source. By contrast, touching a high-voltage
ac source can cause a continuing muscle con-
traction that prevents the victim from letting
go of the source. Lowering the ac voltage with
a transformer reduces the risk of injury.

31.6 Transformers
1041
emfs. If the windings have zero resistance, the induced emfs 
and 
are equal to
the terminal voltages across the primary and the secondary, respectively; hence
(terminal voltages of transformer
primary and secondary)
(31.35)
where 
and 
are either the amplitudes or the rms values of the terminal volt-
ages. By choosing the appropriate turns ratio 
we may obtain any desired
secondary voltage from a given primary voltage. If 
as in Fig. 31.21,
then 
and we have a step-up transformer; if 
then 
and
we have a step-down transformer. At a power generating station, step-up trans-
formers are used; the primary is connected to the power source and the secondary
is connected to the transmission lines, giving the desired high voltage for trans-
mission. Near the consumer, step-down transformers lower the voltage to a value
suitable for use in home or industry (Fig. 31.22).
Even the relatively low voltage provided by a household wall socket is too
high for many electronic devices, so a further step-down transformer is neces-
sary. This is the role of an “ac adapter” such as those used to recharge a mobile
phone or laptop computer from line voltage. Such adapters contain a step-down
transformer that converts line voltage to a lower value, typically 3 to 12 volts, as
well as diodes to convert alternating current to the direct current that small elec-
tronic devices require (Fig. 31.23).
Energy Considerations for Transformers
If the secondary circuit is completed by a resistance 
then the amplitude or rms
value of the current in the secondary circuit is 
From energy consider-
ations, the power delivered to the primary equals that taken out of the secondary
(since there is no resistance in the windings), so
(31.36)
We can combine Eqs. (31.35) and (31.36) and the relationship 
to elim-
inate 
and 
we obtain
(31.37)
This shows that when the secondary circuit is completed through a resistance 
the result is the same as if the source had been connected directly to a resistance
equal to 
divided by the square of the turns ratio, 
In other words, the
transformer “transforms” not only voltages and currents, but resistances as well.
More generally, we can regard a transformer as “transforming” the impedance of
the network to which the secondary circuit is completed.
Equation (31.37) has many practical consequences. The power supplied by a
source to a resistor depends on the resistances of both the resistor and the source. It
can be shown that the power transfer is greatest when the two resistances are equal.
The same principle applies in both dc and ac circuits. When a high-impedance ac
source must be connected to a low-impedance circuit, such as an audio amplifier
connected to a loudspeaker, the source impedance can be matched to that of the
circuit by the use of a transformer with an appropriate turns ratio 
Real transformers always have some energy losses. (That’s why an ac adapter
like the one shown in Fig. 31.23 feels warm to the touch after it’s been in use for
a while; the transformer is heated by the dissipated energy.) The windings have
some resistance, leading to 
losses. There are also energy losses through
hysteresis in the core (see Section 28.8). Hysteresis losses are minimized by the
use of soft iron with a narrow hysteresis loop.
Another important mechanism for energy loss in a transformer core involves
eddy currents (see Section 29.6). Consider a section AA through an iron transformer
core (Fig. 31.24a). Since iron is a conductor, any such section can be pictured as
i2R
N2>N1.
1N2>N122.
R
R,
V1
I1
=
R
1N2>N122
I2;
V2
I2 = V2>R
V1I1 = V2I2  (currents in transformer primary and secondary)
I2 = V2>R.
R,
V2 6 V1
N2 6 N1,
V2 7 V1
N2 7 N1,
N2>N1,
V2
V1
V2
V1
= N2
N1
E2
E1
31.22 The cylindrical can near the top
of this power pole is a step-down trans-
former. It converts the high-voltage ac in
the power lines to low-voltage (120 V) ac,
which is then distributed to the surround-
ing homes and businesses.
31.23 An ac adapter like this one con-
verts household ac into low-voltage dc for
use in electronic devices. It contains a
step-down transformer to lower the voltage
and diodes to rectify the output current
(see Fig. 31.3).

several conducting circuits, one within the other (Fig. 31.24b). The flux through
each of these circuits is continually changing, so eddy currents circulate in the
entire volume of the core, with lines of flow that form planes perpendicular to the
flux. These eddy currents are very undesirable; they waste energy through 
heating and themselves set up an opposing flux.
The effects of eddy currents can be minimized by the use of a laminated core-
that is, one built up of thin sheets or laminae. The large electrical surface resist-
ance of each lamina, due either to a natural coating of oxide or to an insulating
varnish, effectively confines the eddy currents to individual laminae (Fig. 31.24c).
The possible eddy-current paths are narrower, the induced emf in each path is
smaller, and the eddy currents are greatly reduced. The alternating magnetic field
exerts forces on the current-carrying laminae that cause them to vibrate back and
forth; this vibration causes the characteristic “hum” of an operating transformer.
You can hear this same “hum” from the magnetic ballast of a fluorescent light fix-
ture (see Section 30.2).
Thanks to the use of soft iron cores and lamination, transformer efficiencies
are usually well over 90%; in large installations they may reach 99%.
i2R
1042
CHAPTER 31 Alternating Current
A
A
(a) Schematic transformer
Solid
core
Primary
winding
Secondary
winding
Eddy
currents
Section at AA
(b) Large eddy currents in solid core
Laminated
core
Eddy
currents
Section at AA
(c) Smaller eddy currents in laminated core
31.24 (a) Primary and secondary windings in a transformer. (b) Eddy currents in the iron core, shown in the cross section at AA.
(c) Using a laminated core reduces the eddy currents.
