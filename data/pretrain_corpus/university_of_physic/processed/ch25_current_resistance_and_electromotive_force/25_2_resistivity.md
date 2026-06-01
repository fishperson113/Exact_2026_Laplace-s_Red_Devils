822

CHAPTER 25 Current, Resistance, and Electromotive Force

closed loop, called a complete circuit. In such a steady situation, the total charge
in every segment of the conductor is constant. Hence the rate of ﬂow of charge
out at one end of a segment at any instant equals the rate of ﬂow of charge in at
the other end of the segment, and the current is the same at all cross sections of
the circuit. We’ll make use of this observation when we analyze electric circuits
later in this chapter.

In  many  simple  circuits,  such  as  ﬂashlights  or  cordless  electric  drills,  the
direction of the current is always the same; this is called direct current. But home
appliances such as toasters, refrigerators, and televisions use alternating current,
in  which  the  current  continuously  changes  direction.  In  this  chapter  we’ll  con-
sider direct current only. Alternating current has many special features worthy of
detailed study, which we’ll examine in Chapter 31.

Example 25.1

Current density and drift velocity in a wire

An 18-gauge copper wire (the size usually used for lamp cords),
with a diameter of
1.67 A
to  a  200-W lamp.  The  free-electron  density  in  the  wire  is
8.5 * 1028
per cubic meter. Find (a) the current density and (b) the
drift speed.

carries a constant current of

1.02 mm,

SOLUTION

IDENTIFY and SET UP: This problem uses the relationships among
. We are given I and
current I, current density J, and drift speed
the  wire  diameter  d,  so  we  use  Eq.  (25.3) to  ﬁnd
.  We  use  Eq.
(25.3) again to ﬁnd

from  and the known electron density n.

vd

J

J

vd

EXECUTE: (a) The cross-sectional area is
p11.02 * 10-3 m22
4

pd 2
4

A =

=

= 8.17 * 10-7 m2

The magnitude of the current density is then

J = I
A

=

1.67 A
8.17 * 10-7 m2

= 2.04 * 106 A>m2

(b) From Eq. (25.3) for the drift velocity magnitude

vd

, we ﬁnd

vd = J
nƒqƒ

=

2.04 * 106 A>m2
18.5 * 1028 m-32ƒ -1.60 * 10-19 Cƒ

= 1.5 * 10-4 m>s = 0.15 mm>s

EVALUATE: At this speed an electron would require
(almost
2 h) to travel 1 m along this wire. The speeds of random motion of
106 m>s,
the  electrons  are  roughly
times  the  drift
speed. Picture the electrons as bouncing around frantically, with a
very slow drift!

around

6700 s

1010

Test Your Understanding of Section 25.1 Suppose we replaced the
wire in Example 25.1 with 12-gauge copper wire, which has twice the diameter of
18-gauge wire. If the current remains the same, what effect would this have on the
(i) none— would be unchanged; (ii)  would
magnitude of the drift velocity
vd
be twice as great; (iii)  would be four times greater; (iv)  would be half as great;
(v)  would be one-fourth as great.

vd?

vd

vd

vd

vd

❙

25.2 Resistivity

S
J

S
E

,

E

S
E

S
J
J

and the ratio of the magnitudes of

in a conductor depends on the electric ﬁeld

and on the
The current density
properties of the material. In general, this dependence can be quite complex. But
is nearly directly
for some materials, especially metals, at a given temperature,
proportional to
is constant. This
and
relationship, called Ohm’s law, was discovered in 1826 by the German physicist
Georg Simon Ohm (1787–1854). The word “law” should actually be in quotation
marks,  since  Ohm’s  law, like  the  ideal-gas  equation  and  Hooke’s  law,  is  an
idealized model that describes the behavior of some materials quite well but is
not a general description of all matter. In the following discussion we’ll assume
that Ohm’s law is valid, even though there are many situations in which it is not.
The situation is comparable to our representation of the behavior of the static and
kinetic friction forces; we treated these friction forces as being directly propor-
tional to the normal force, even though we knew that this was at best an approxi-
mate description.

Table 25.1 Resistivities at Room Temperature (20 C)

°

Substance

R 1æ # m2

Conductors
Metals

Alloys

Silver
Copper
Gold
Aluminum
Tungsten
Steel
Lead
Mercury
Manganin (Cu 84%, Mn 12%, Ni 4%)
Constantan (Cu 60%, Ni 40%)
Nichrome

1.47 * 10-8
1.72 * 10-8
2.44 * 10-8
2.75 * 10-8
5.25 * 10-8
20 * 10-8
22 * 10-8
95 * 10-8
44 * 10-8
49 * 10-8
100 * 10-8

25.2 Resistivity

823

Substance

Semiconductors

Pure carbon (graphite)
Pure germanium
Pure silicon

Insulators

Amber
Glass
Lucite
Mica
Quartz (fused)
Sulfur
Teﬂon
Wood

R 1æ # m2

3.5 * 10-5
0.60
2300

5 * 1014
1010–1014
71013
1011–1015
75 * 1016
1015
71013
108–1011

r
We deﬁne the resistivity
tric ﬁeld and current density:

of a material as the ratio of the magnitudes of elec-

r = E
J

(deﬁnition of resistivity)

(25.5)

r
is called one ohm (

1V>m2>1A>m22 = V # m>A.
1 Æ;

The  greater  the  resistivity,  the  greater  the  ﬁeld  needed  to  cause  a  given  current
density, or the smaller the current density caused by a given ﬁeld. From Eq. (25.5)
As we will discuss in the next sec-
the units of  are
1 V>A
tion,
or omega, which
is alliterative with “ohm”). So the SI units for  are
(ohm-meters). Table 25.1
lists  some  representative  values  of  resistivity. A perfect  conductor  would  have
zero resistivity, and a perfect insulator would have an inﬁnite resistivity. Metals
and alloys have the smallest resistivities and are the best conductors. The resistiv-
ities of insulators are greater than those of the metals by an enormous factor, on
the order of

we use the Greek letter

Æ # m

1022.

Æ,

r

The  reciprocal  of  resistivity  is  conductivity. Its  units  are

Good
conductors of electricity have larger conductivity than insulators. Conductivity is
the direct electrical analog of thermal conductivity. Comparing Table 25.1 with
Table  17.5 (Thermal  Conductivities),  we  note  that  good  electrical  conductors,
such as metals, are usually also good conductors of heat. Poor electrical conduc-
tors, such as ceramic and plastic materials, are also poor thermal conductors. In a
metal the free electrons that carry charge in electrical conduction also provide the
principal  mechanism  for  heat  conduction,  so  we  should  expect  a  correlation
between electrical and thermal conductivity. Because of the enormous difference
in conductivity between electrical conductors and insulators, it is easy to conﬁne
electric  currents  to  well-deﬁned  paths  or  circuits  (Fig.  25.5).  The  variation  in
thermal conductivity  is  much  less,  only  a  factor  of
or  so,  and  it  is  usually
impossible to conﬁne heat currents to that extent.

103

1Æ # m2-1.

Semiconductors have  resistivities  intermediate  between  those  of  metals  and
those of insulators. These materials are important because of the way their resis-
tivities are affected by temperature and by small amounts of impurities.

r

E

E

A material that obeys Ohm’s law reasonably well is called an ohmic conductor
is a constant
or a linear conductor. For such materials, at a given temperature,
that does not depend on the value of
. Many materials show substantial depar-
tures from Ohm’s-law behavior; they are nonohmic, or nonlinear. In these materi-
als,  depends on

J
Analogies with ﬂuid ﬂow can be a big help in developing intuition about elec-
tric current and circuits. For example, in the making of wine or maple syrup, the
product  is  sometimes  ﬁltered  to  remove  sediments.  A pump  forces  the  ﬂuid
through the ﬁlter under pressure; if the ﬂow rate (analogous to  ) is proportional
to  the  pressure  difference  between  the  upstream  and  downstream  sides  (analo-
gous to E), the behavior is analogous to Ohm’s law.

in a more complicated manner.

J

25.5 The copper “wires,” or traces, on
this circuit board are printed directly onto
the surface of the dark-colored insulating
board. Even though the traces are very
close to each other (only about a millimeter
apart), the board has such a high resistivity
(and low conductivity) that no current can
ﬂow between the traces.

Conducting paths
(traces)

824

CHAPTER 25 Current, Resistance, and Electromotive Force

10 - 6

Application Resistivity and Nerve
Conduction
This false-color image from an electron micro-
scope shows a cross section through a nerve
ﬁber about 1 μm (
m) in diameter. A layer
of an insulating fatty substance called myelin is
wrapped around the conductive material of the
axon. The resistivity of myelin is much greater
than that of the axon, so an electric signal
traveling along the nerve ﬁber remains con-
ﬁned to the axon. This makes it possible for a
signal to travel much more rapidly than if the
myelin were absent.

Resistivity and Temperature
The  resistivity  of  a  metallic conductor  nearly  always  increases  with  increasing
temperature,  as  shown  in  Fig.  25.6a. As  temperature  increases,  the  ions  of  the
conductor  vibrate  with  greater  amplitude,  making  it  more  likely  that  a  moving
electron will collide with an ion as in Fig. 25.1; this impedes the drift of electrons
through the conductor and hence reduces the current. Over a small temperature
range (up to
or so), the resistivity of a metal can be represented approxi-
mately by the equation

100 C°

r1T2 = r031 + a1T - T024

(temperature dependence
of resistivity)

(25.6)

Myelin

Axon

T

r
for (a) a normal

25.6 Variation of resistivity  with
absolute temperature
metal, (b) a semiconductor, and (c) a
superconductor. In (a) the linear approxi-
mation to  as a function of
is shown as
a green line; the approximation agrees
exactly at

where r = r0.

T

r

T = T0,
r

(a)

r

0

O

(b)

r

O

(c)

r

Metal: Resistivity increases
with increasing temperature.

Slope 5 r

a

0

T

T0

Semiconductor: Resistivity
decreases with increasing
temperature.

T

Superconductor: At
temperatures below Tc,
the resistivity
is zero.

O

Tc

T

r0
and

is  the  resistivity  at  a  reference  temperature
r1T2
is the resistivity at temperature
The factor

where
or
(often  taken  as
20°C2
, which may be higher or lower
is called the temperature coefﬁcient of resistivity. Some
than
T0.
representative  values  are  given  in  Table  25.2. The  resistivity  of  the  alloy  man-
ganin is practically independent of temperature.

0°C

T0

a

T

Table 25.2 Temperature Coefﬁcients of Resistivity
(Approximate Values Near Room Temperature)

Material

Aluminum
Brass
Carbon (graphite)
Constantan
Copper
Iron

A 31°C2(cid:3)14

0.0039
0.0020
-0.0005
0.00001
0.00393
0.0050

Material

Lead
Manganin
Mercury
Nichrome
Silver
Tungsten

A 31°C2(cid:3)14

0.0043
0.00000
0.00088
0.0004
0.0038
0.0045

The  resistivity  of  graphite  (a  nonmetal)  decreases with  increasing  tempera-
ture,  since  at  higher  temperatures,  more  electrons  are  “shaken  loose”  from  the
atoms  and  become  mobile;  hence  the  temperature  coefﬁcient  of  resistivity  of
graphite is negative. This same behavior occurs for semiconductors (Fig. 25.6b).
Measuring the resistivity of a small semiconductor crystal is therefore a sensitive
measure of temperature; this is the principle of a type of thermometer called a
thermistor.

Some materials, including several metallic alloys and oxides, show a phenom-
enon  called  superconductivity. As  the  temperature  decreases,  the  resistivity  at
ﬁrst decreases smoothly, like that of any metal. But then at a certain critical tem-
perature
a phase transition occurs and the resistivity suddenly drops to zero, as
shown in Fig. 25.6c. Once a current has been established in a superconducting
ring, it continues indeﬁnitely without the presence of any driving ﬁeld.

Tc

Superconductivity  was  discovered  in  1911  by  the  Dutch  physicist  Heike
Kamerlingh  Onnes  (1853–1926).  He  discovered  that  at  very  low  temperatures,
4.2 K,
the resistivity of mercury suddenly dropped to zero. For the next
below
75 years, the highest
This meant that superconductivity
occurred only when the material was cooled using expensive liquid helium, with
a boiling-point temperature of
or explosive liquid hydrogen, with a boiling
But in 1986 Karl Müller and Johannes Bednorz discovered an
point of
Tc
and the race
oxide of barium, lanthanum, and copper with a
was on to develop “high-temperature” superconducting materials.

attained was about

of nearly

20.3 K.

4.2 K,

40 K,

20 K.

Tc

Tc

By 1987 a complex oxide of yttrium, copper, and barium had been found that
has a value of  well above the 77 K boiling temperature of liquid nitrogen, a
at
refrigerant that is both inexpensive and safe. The current (2010) record for
atmospheric pressure is 138 K, and materials that are superconductors at room
temperature  may  become  a  reality.  The  implications  of  these  discoveries  for
power-distribution  systems,  computer  design,  and  transportation  are  enormous.
Meanwhile,  superconducting  electromagnets  cooled  by  liquid  helium  are  used
in  particle  accelerators  and  some  experimental  magnetic-levitation  railroads.

Tc
