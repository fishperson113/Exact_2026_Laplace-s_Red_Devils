1040

CHAPTER 31 Alternating Current

31.21 Schematic diagram of an ideal-
ized step-up transformer. The primary is
connected to an ac source; the secondary is
connected to a device with resistance R.

The induced emf per turn is the same in both
coils, so we adjust the ratio of terminal voltages
by adjusting the ratio of turns:

V2
V1

5 N2
N1

Source of alternating
current

I1

Iron core

V1
N1

Primary
winding

F

B

N2

V2

R

Secondary
winding

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

Test Your Understanding of Section 31.5 How does the resonance fre-
quency of an L-R-C series circuit change if the plates of the capacitor are brought closer
together? (i) It increases; (ii) it decreases; (iii) it is unaffected.

❙

31.6 Transformers

i 2R

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
former  are  two  coils  or  windings, electrically  insulated  from  each  other  but
wound on the same core. The core is typically made of a material, such as iron,
This keeps the magnetic ﬁeld lines
with a very large relative permeability
due to a current in one winding almost completely within the core. Hence almost
all  of  these  ﬁeld  lines  pass  through  the  other  winding,  maximizing  the  mutual
inductance of the two windings (see Section 30.1). The winding to which power
is supplied is called the primary; the winding from which power is delivered is
called  the  secondary. The  circuit  symbol  for  a  transformer  with  an  iron  core,
such as those used in power distribution systems, is

Km.

Here’s how a transformer works. The ac source causes an alternating current
in the primary, which sets up an alternating ﬂux in the core; this induces an emf
in each winding, in accordance with Faraday’s law. The induced emf in the sec-
ondary  gives  rise  to  an  alternating  current  in  the  secondary,  and  this  delivers
energy to the device to which the secondary is connected. All currents and emfs
have the same frequency as the ac source.

Let’s see how the voltage across the secondary can be made larger or smaller
in amplitude than the voltage across the primary. We neglect the resistance of the
windings  and  assume  that  all  the  magnetic  ﬁeld  lines  are  conﬁned  to  the  iron
is the same in each turn of the pri-
core, so at any instant the magnetic ﬂux
turns and the second-
mary and secondary windings. The primary winding has
ary winding has
turns. When the magnetic ﬂux changes because of changing
currents in the two coils, the resulting induced emfs are

£B

N1

N2

E1 = - N1

  and  E2 = - N2

d£B
dt

d£B
dt

(31.33)

£B

The ﬂux per turn

is the same in both the primary and the secondary, so
Eqs. (31.33) show that the induced emf per turn is the same in each. The ratio of
E1
is therefore equal at any instant to the
the secondary emf
ratio of secondary to primary turns:

to the primary emf

E2

E2
E1

=

N2
N1

(31.34)

E1

E2

both  oscillate  with  the  same  frequency  as  the  ac  source,
Since
Eq. (31.34) also gives the ratio of the amplitudes or of the rms values of the induced

and

31.6 Transformers

1041

31.22 The cylindrical can near the top
of this power pole is a step-down trans-
former. It converts the high-voltage ac in
the power lines to low-voltage (120 V) ac,
which is then distributed to the surround-
ing homes and businesses.

emfs. If the windings have zero resistance, the induced emfs
the terminal voltages across the primary and the secondary, respectively; hence

and

are equal to

E1

E2

V2
V1

=

N2
N1

(terminal voltages of transformer
primary and secondary)

(31.35)

V1

V2

and

V2 7 V1

are either the amplitudes or the rms values of the terminal volt-
where
N2>N1,
we may obtain any desired
ages. By choosing the appropriate turns ratio
N2 7 N1,
as in Fig. 31.21,
secondary voltage from a given primary voltage. If
N2 6 N1,
V2 6 V1
then
and
then
and we have a step-up transformer; if
we have a step-down transformer. At a power generating station, step-up trans-
formers are used; the primary is connected to the power source and the secondary
is connected to the transmission lines, giving the desired high voltage for trans-
mission. Near the consumer, step-down transformers lower the voltage to a value
suitable for use in home or industry (Fig. 31.22).

Even  the  relatively  low  voltage  provided  by  a  household  wall  socket  is  too
high  for  many  electronic  devices,  so  a  further  step-down  transformer  is  neces-
sary. This is the role of an “ac adapter” such as those used to recharge a mobile
phone or laptop computer from line voltage. Such adapters contain a step-down
transformer that converts line voltage to a lower value, typically 3 to 12 volts, as
well as diodes to convert alternating current to the direct current that small elec-
tronic devices require (Fig. 31.23).

31.23 An ac adapter like this one con-
verts household ac into low-voltage dc for
use in electronic devices. It contains a
step-down transformer to lower the voltage
and diodes to rectify the output current
(see Fig. 31.3).

Energy Considerations for Transformers
then the amplitude or rms
If the secondary circuit is completed by a resistance
value of the current in the secondary circuit is
From energy consider-
ations, the power delivered to the primary equals that taken out of the secondary
(since there is no resistance in the windings), so

R,
I2 = V2>R.

V1I1 = V2I2    (currents in transformer primary and secondary)

(31.36)

We can combine Eqs. (31.35) and (31.36) and the relationship
inate

and  we obtain

V2

I2;

=

V1
I1

R
1N2>N122

I2 = V2>R

to elim-

(31.37)

R

R,
This shows that when the secondary circuit is completed through a resistance
the result is the same as if the source had been connected directly to a resistance
equal to  divided by the square of the turns ratio,
In other words, the
transformer “transforms” not only voltages and currents, but resistances as well.
More generally, we can regard a transformer as “transforming” the impedance of
the network to which the secondary circuit is completed.

1N2>N122.

Equation  (31.37) has  many  practical  consequences.  The  power  supplied  by  a
source to a resistor depends on the resistances of both the resistor and the source. It
can be shown that the power transfer is greatest when the two resistances are equal.
The same principle applies in both dc and ac circuits. When a high-impedance ac
source must be connected to a low-impedance circuit, such as an audio ampliﬁer
connected to a loudspeaker, the source impedance can be matched to that of the
circuit by the use of a transformer with an appropriate turns ratio

N2>N1.

Real transformers always have some energy losses. (That’s why an ac adapter
like the one shown in Fig. 31.23 feels warm to the touch after it’s been in use for
a while; the transformer is heated by the dissipated energy.) The windings have
some  resistance,  leading  to
losses.  There  are  also  energy  losses  through
hysteresis in the core (see Section 28.8). Hysteresis losses are minimized by the
use of soft iron with a narrow hysteresis loop.

i 2R

Another  important  mechanism  for  energy  loss  in  a  transformer  core  involves
eddy currents (see Section 29.6). Consider a section AA through an iron transformer
core (Fig. 31.24a). Since iron is a conductor, any such section can be pictured as

1042

CHAPTER 31 Alternating Current

31.24 (a) Primary and secondary windings in a transformer. (b) Eddy currents in the iron core, shown in the cross section at AA.
(c) Using a laminated core reduces the eddy currents.

(a) Schematic transformer

(b) Large eddy currents in solid core

(c) Smaller eddy currents in laminated core

A

A

Primary
winding

Solid
core

Laminated
core

Secondary
winding

Eddy
currents
Section at AA

Eddy
currents

Section at AA

several conducting circuits, one within the other (Fig. 31.24b). The ﬂux through
each of these circuits is continually changing, so eddy currents circulate in the
entire volume of the core, with lines of ﬂow that form planes perpendicular to the
i 2R
ﬂux. These  eddy  currents  are  very  undesirable;  they  waste  energy  through
heating and themselves set up an opposing ﬂux.

The effects of eddy currents can be minimized by the use of a laminated core—
that is, one built up of thin sheets or laminae. The large electrical surface resist-
ance of each lamina, due either to a natural coating of oxide or to an insulating
varnish, effectively conﬁnes the eddy currents to individual laminae (Fig. 31.24c).
The  possible  eddy-current  paths  are  narrower,  the  induced  emf  in  each  path  is
smaller, and the eddy currents are greatly reduced. The alternating magnetic ﬁeld
exerts forces on the current-carrying laminae that cause them to vibrate back and
forth; this vibration causes the characteristic “hum” of an operating transformer.
You can hear this same “hum” from the magnetic ballast of a ﬂuorescent light ﬁx-
ture (see Section 30.2).

Thanks to the use of soft iron cores and lamination, transformer efﬁciencies

are usually well over 90%; in large installations they may reach 99%.

Example 31.9

“Wake up and smell the (transformer)!”

A friend  returns  to  the  United  States  from  Europe  with  a  960-W
coffeemaker, designed to operate from a 240-V line. (a) What can
she do to operate it at the USA-standard 120 V? (b) What current
will  the  coffeemaker  draw  from  the  120-V line?  (c)  What  is  the
resistance of the coffeemaker? (The voltages are rms values.)

SOLUTION

IDENTIFY  and SET  UP: Our friend needs a step-up transformer to
convert  120-V ac  to  the  240-V ac  that  the  coffeemaker  requires.
N2>N1,
We use Eq. (31.35) to determine the transformer turns ratio
Pav = VrmsIrms
for a resistor to ﬁnd the current draw, and Eq. (31.37)
to calculate the resistance.

V2 = 240 V

EXECUTE: (a)  To  get
the  required
N2>N1 = V2>V1 = 1240 V2>1120 V2 = 2.
That is, the
turns ratio is
secondary coil (connected to the coffeemaker) should have twice as
many turns as the primary coil (connected to the 120-V line).

from

V1 = 120 V,

I1

Pav

where

(b) We ﬁnd the rms current

in the 120-V primary by using
Pav = V1I1,
is  the  average  power  drawn  by  the  cof-
feemaker and hence the power supplied by the 120-V line. (We’re
assuming  that  no  energy  is  lost  in  the  transformer.)  Hence
=
Pav>V1
8.0  A.  The  secondary  current  is
then

1960 W2>1240 V2

I1

= 4.0 A.
and

I1 = 8.0 A,

N2>N1 = 2,

so

I2 =
Pav>V2
(c) We have

= 1960 W2>1120 V2 =
=
V1 = 120 V,
V1
I1

= 120 V
8.0 A

= 15 Æ

From Eq. (31.37),

R = 22115 Æ2 = 60 Æ

V2>R = 1240 V2>160 Æ2 = 4.0 A = I2,
EVALUATE:  As  a  check,
the same value obtained previously. You can also check this result
Pav = V 2
for R by using the expression
for the power drawn by
the coffeemaker.

2 >R

Test Your Understanding of Section 31.6 Each of the following four trans-
formers has 1000 turns in its primary coil. Rank the transformers from largest to smallest
number of turns in the secondary coil. (i) converts 120-V ac into 6.0-V ac; (ii) converts
120-V ac into 240-V ac; (iii) converts 240-V ac into 6.0-V ac; (iv) converts 240-V ac into
❙
120-V ac.
