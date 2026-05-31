868

CHAPTER 26 Direct-Current Circuits

Example 26.12

Charging a capacitor

10-MÆ

resistor is connected in series with a

A
capacitor
and a battery with emf 12.0 V. Before the switch is closed at time
t = 0,
the capacitor is uncharged. (a) What is the time constant?
is  on  the  capacitor  at
(b)  What  fraction  of  the  ﬁnal  charge
t = 46 s?
is still ﬂowing
at

(c) What fraction of the initial current

t = 46 s?

Qf

I0

1.0-mF

SOLUTION

C = 1.0 mF,

R = 10 MÆ,

IDENTIFY  and SET  UP: This is the same situation as shown in Fig.
26.20,  with
The
charge q and current i vary with time as shown in Fig. 26.21. Our tar-
get variables are (a) the time constant
s,
i>I0
For  a
and  (c)  the  ratio
capacitor being charged, Eq. (26.12) gives q and Eq. (26.13) gives i.

(b) the ratio
at
s.  Equation  (26.14) gives

t = 46
t.

E = 12.0 V.

t = 46

q>Qf

and

at

t,

Example 26.13

Discharging a capacitor

The  resistor  and  capacitor  of  Example  26.12  are  reconnected  as
5.0 mC
shown in Fig. 26.22. The capacitor has an initial charge of
and is discharged by closing the switch at
(a) At what time will
(b) What is the current at this time?
the charge be equal to

0.50 mC?

t = 0.

SOLUTION

IDENTIFY and SET UP: Now the capacitor is being discharged, so q
Q0 = 5.0 * 10-6 C .
and i vary with time as in Fig. 26.23, with
Again  we  have  RC (cid:2)
Our  target  variables  are  (a)  the
and  (b)  the  value  of  i at  this
value  of  t at  which
time. We first solve Eq. (26.16) for t, and then solve Eq. (26.17)
for i.

t = 10 s.
q = 0.50 mC

EXECUTE: (a) From Eq. (26.14),

t = RC = 110 * 106 Æ211.0 * 10-6 F2 = 10 s

(b) From Eq. (26.12),

q
Qf

= 1 - e-t>RC = 1 - e-146 s2>110 s2 = 0.99

(c) From Eq. (26.13),

= e-t>RC = e-146 s2>110 s2 = 0.010

i
I0

EVALUATE:  After 4.6 time constants the capacitor is 99% charged
and the charging current has decreased to 1.0% of its initial value.
The circuit would charge more rapidly if we reduced the time con-
stant by using a smaller resistance.

EXECUTE: (a) Solving Eq. (26.16) for the time t gives

t = - RC ln

q
Q0

= - 110 s2 ln

0.50 mC
5.0 mC

= 23 s = 2.3t

(b) From Eq. (26.17), with

Q0 = 5.0 mC = 5.0 * 10-6 C,

i = -

Q0
RC

e-t>RC = - 5.0 * 10-6 C

10 s

e-2.3 = - 5.0 * 10-8 A

EVALUATE:  The  current  in  part  (b)  is  negative  because  i has  the
opposite  sign  when  the  capacitor  is  discharging  than  when  it  is
by
charging.  Note  that  we  could  have  avoided  evaluating
noticing that at the time in question,
from Eq. (26.16)
this means that e-t>RC = 0.10.

q = 0.10Q0;

e-t>RC

Test Your Understanding of Section 26.4 The energy stored in a
When a capacitor is discharged, what fraction of
capacitor is equal to
the initial energy remains after an elapsed time of one time constant? (i)
1/e;
(ii)
was stored initially.

(v) answer depends on how much energy

11 - 1/e22;

1 - 1/e;

q 2/2C.

1/e2;

(iii)

(iv)

❙

26.5 Power Distribution Systems

We conclude this chapter with a brief discussion of practical household and auto-
motive electric-power distribution systems. Automobiles use direct-current (dc)
systems,  while  nearly  all  household,  commercial,  and  industrial  systems  use
alternating current (ac) because of the ease of stepping voltage up and down with
transformers. Most of the same basic wiring concepts apply to both. We’ll talk
about alternating-current circuits in greater detail in Chapter 31.

The various lamps, motors, and other appliances to be operated are always con-
nected  in  parallel to  the  power  source  (the  wires  from  the  power  company  for
houses, or from the battery and alternator for a car). If appliances were connected in
series, shutting one appliance off would shut them all off (see Example 26.2 in Sec-
tion 26.1). Figure 26.24 shows the basic idea of house wiring. One side of the “line,”
as the pair of conductors is called, is called the neutral side; it is always connected to

26.24 Schematic diagram of part of a house wiring system. Only two branch circuits are shown; an actual system might have four to
thirty branch circuits. Lamps and appliances may be plugged into the outlets. The grounding wires, which normally carry no current, are
not shown.

26.5 Power Distribution Systems

869

From power
company

Main
fuse

Fuse

Outlets

Fuse

Light

Switch

Hot
line

Neutral
line

Outlets

Switch

Hot
line

Light

Neutral
line

Meter

Ground

“ground” at the entrance panel. For houses, ground is an actual electrode driven into
the earth (which is usually a good conductor) or sometimes connected to the house-
hold water pipes. Electricians speak of the “hot” side and the “neutral” side of the
line. Most modern house wiring systems have two hot lines with opposite polarity
with respect to the neutral. We’ll return to this detail later.

Household  voltage  is  nominally  120 V in  the  United  States  and  Canada,  and
often  240  V in  Europe.  (For  alternating  current,  which  varies  sinusoidally  with
time, these numbers represent the root-mean-square voltage, which is
times
the peak voltage. We’ll discuss this further in Section 31.1.) The amount of current
I drawn by a given device is determined by its power input P, given by Eq. (25.17):
P = VI.

For example, the current in a 100-W light bulb is

I = P>V.

1> 12

Hence

I = P
V

= 100 W
120 V

= 0.83 A

The  power  input  to  this  bulb  is  actually  determined  by  its  resistance  R.  Using
Eq.  (25.18),  which  states  that
for  a  resistor,  the  resist-
ance of this bulb at operating temperature is

P = VI = I 2R = V 2>R

R = V
I

= 120 V
0.83 A

= 144 Æ    or    R = V 2

P

=

1120 V22
100 W

= 144 Æ

11500 W2>1120 V2 = 12.5 A
Similarly, a 1500-W wafﬂe iron draws a current of
Because of the temperature
and has a resistance, at operating temperature, of
dependence  of  resistivity,  the  resistances  of  these  devices  are  considerably  less
when they are cold. If you measure the resistance of a 100-W light bulb with an
ohmmeter (whose small current causes very little temperature rise), you will prob-
ably get a value of about
When a light bulb is turned on, this low resistance
causes  an  initial  surge  of  current  until  the  ﬁlament  heats  up. That’s  why  a  light
bulb that’s ready to burn out nearly always does so just when you turn it on.

9.6 Æ.

10 Æ.

Circuit Overloads and Short Circuits
The maximum current available from an individual circuit is limited by the resist-
ance of the wires. As we discussed in Section 25.5, the
power loss in the wires
causes them to become hot, and in extreme cases this can cause a ﬁre or melt the
wires. Ordinary lighting and outlet wiring in houses usually uses 12-gauge wire.
This has a diameter of 2.05 mm and can carry a maximum current of 20 A safely
(without overheating). Larger-diameter wires of the same length have lower resist-
ance [see Eq. (25.10)]. Hence 8-gauge (3.26 mm) or 6-gauge (4.11 mm) are used
for  high-current  appliances  such  as  clothes  dryers,  and  2-gauge  (6.54  mm)  or
larger is used for the main power lines entering a house.

I 2R

870

CHAPTER 26 Direct-Current Circuits

26.25 (a) Excess current will melt the
thin wire of lead–tin alloy that runs along
the length of a fuse, inside the transparent
housing. (b) The switch on this circuit
breaker will ﬂip if the maximum allowable
current is exceeded.

(a)

(b)

Protection against overloading and overheating of circuits is provided by fuses
or circuit breakers. A fuse contains a link of lead–tin alloy with a very low melting
temperature; the link melts and breaks the circuit when its rated current is exceeded
(Fig. 26.25a). A circuit breaker is an electromechanical device that performs the
same function, using an electromagnet or a bimetallic strip to “trip” the breaker and
interrupt  the  circuit  when  the  current  exceeds  a  speciﬁed  value  (Fig.  26.25b).
Circuit breakers have the advantage that they can be reset after they are tripped,
while a blown fuse must be replaced.

If your system has fuses and you plug too many high-current appliances into
the same outlet, the fuse blows. Do not replace the fuse with one of larger rating;
if you do, you risk overheating the wires and starting a ﬁre. The only safe solu-
tion is to distribute the appliances among several circuits. Modern kitchens often
have three or four separate 20-A circuits.

Contact  between  the  hot  and  neutral  sides  of  the  line  causes  a  short  circuit.
Such a situation, which can be caused by faulty insulation or by any of a variety
of mechanical malfunctions, provides a very low-resistance current path, permit-
ting a very large current that would quickly melt the wires and ignite their insula-
tion if the current were not interrupted by a fuse or circuit breaker (see Example
25.10 in Section 25.5). An equally dangerous situation is a broken wire that inter-
rupts the current path, creating an open circuit. This is hazardous because of the
sparking that can occur at the point of intermittent contact.

In approved wiring practice, a fuse or breaker is placed only in the hot side of
the  line,  never  in  the  neutral  side.  Otherwise,  if  a  short  circuit  should  develop
because  of  faulty  insulation  or  other  malfunction,  the  ground-side  fuse  could
blow.  The  hot  side  would  still  be  live  and  would  pose  a  shock  hazard  if  you
touched the live conductor and a grounded object such as a water pipe. For simi-
lar reasons the wall switch for a light ﬁxture is always in the hot side of the line,
never the neutral side.

Further  protection  against  shock  hazard  is  provided  by  a  third  conductor
called the grounding wire, included in all present-day wiring. This conductor cor-
responds to the long round or U-shaped prong of the three-prong connector plug
on an appliance or power tool. It is connected to the neutral side of the line at the
entrance panel. The grounding wire normally carries no current, but it connects
the metal case or frame of the device to ground. If a conductor on the hot side of
the  line  accidentally  contacts  the  frame  or  case,  the  grounding  conductor  pro-
vides  a  current  path,  and  the  fuse  blows.  Without  the  ground  wire,  the  frame
could  become  “live”—that  is,  at  a  potential  120  V above  ground.  Then  if  you
touched it and a water pipe (or even a damp basement ﬂoor) at the same time, you
could get a dangerous shock (Fig. 26.26). In some situations, especially outlets
located  outdoors  or  near  a  sink  or  other  water  pipes,  a  special  kind  of  circuit
breaker  called  a  ground-fault  interrupter (GFI  or  GFCI)  is  used.  This  device
senses the difference in current between the hot and neutral conductors (which is
normally  zero)  and  trips  when  this  difference  exceeds  some  very  small  value,
typically 5 mA.

Household and Automotive Wiring
Most modern household wiring systems actually use a slight elaboration of the sys-
tem described above. The power company provides three conductors. One is neu-
tral; the other two are both at 120 V with respect to the neutral but with opposite
polarity, giving a voltage between them of 240 V. The power company calls this a
three-wire line, in contrast to the 120-V two-wire (plus ground wire) line described
above.  With  a  three-wire  line,  120-V lamps  and  appliances  can  be  connected
between neutral and either hot conductor, and high-power devices requiring 240 V,
such as electric ranges and clothes dryers, are connected between the two hot lines.
All of the above discussion can be applied directly to automobile wiring. The
voltage is about 13 V (direct current); the power is supplied by the battery and by

(a) Two-prong plug

(b) Three-prong plug

26.5 Power Distribution Systems

871

26.26 (a) If a malfunctioning electric
drill is connected to a wall socket via a
two-prong plug, a person may receive a
shock. (b) When the drill malfunctions
when connected via a three-prong plug, a
person touching it receives no shock,
because electric charge ﬂows through the
ground wire (shown in green) to the third
prong and into the ground rather than into
the person’s body. If the ground current is
appreciable, the fuse blows.

the alternator, which charges the battery when the engine is running. The neutral
side of each circuit is connected to the body and frame of the vehicle. For this
low voltage a separate grounding conductor is not required for safety. The fuse or
circuit  breaker  arrangement  is  the  same  in  principle  as  in  household  wiring.
Because  of  the  lower  voltage  (less  energy  per  charge),  more  current  (a  greater
number of charges per second) is required for the same power; a 100-W headlight
bulb requires a current of about

1100 W2>113 V2 = 8 A.

Although we spoke of power in the above discussion, what we buy from the
power company is energy. Power is energy transferred per unit time, so energy is
average power multiplied by time. The usual unit of energy sold by the power
company is the kilowatt-hour

11 kW # h2:

1 kW # h = 1103 W213600 s2 = 3.6 * 106 W # s = 3.6 * 106 J
In the United States, one kilowatt-hour typically costs 8 to 27 cents, depending
on the location and quantity of energy purchased. To operate a 1500-W (1.5-kW)
wafﬂe iron continuously for 1 hour requires
of energy; at 10 cents per
kilowatt-hour,  the  energy  cost  is  15  cents.  The  cost  of  operating  any  lamp  or
appliance for a speciﬁed time can be calculated in the same way if the power rat-
ing is known. However, many electric cooking utensils (including wafﬂe irons)
cycle on and off to maintain a constant temperature, so the average power may be
less than the power rating marked on the device.

1.5 kW # h

Example 26.14

A kitchen circuit

An  1800-W toaster,  a  1.3-kW electric  frying  pan,  and  a  100-W
lamp are plugged into the same 20-A, 120-V circuit. (a) What cur-
rent  is  drawn  by  each  device,  and  what  is  the  resistance  of  each
device? (b) Will this combination trip the circuit breaker?

SOLUTION

IDENTIFY  and SET  UP:  When  plugged  into  the  same  circuit,  the
three devices are connected in parallel, so the voltage across each
We  ﬁnd  the  current  I drawn  by  each
appliance  is
P = VI,
device using the relationship
where P is the power input
of the device. To ﬁnd the resistance R of each device we use the
relationship P = V 2>R.

V = 120 V.

EXECUTE: (a) To simplify the calculation of current and resistance,
R = V 2>P.
we note that

Hence

and

I = P>V
Itoaster = 1800 W
120 V
Ifrying pan = 1300 W
120 V
Ilamp = 100 W
120 V

= 15 A

Rtoaster =

= 11 A

Rfrying pan =

= 0.83 A

Rlamp =

1120 V22
1800 W
1120 V22
1300 W
1120 V22
100 W

= 8 Æ

= 11 Æ

= 144 Æ

For constant voltage the device with the least resistance (in this case
the toaster) draws the most current and receives the most power.

Continued

872

CHAPTER 26 Direct-Current Circuits

(b) The total current through the line is the sum of the currents

drawn by the three devices:

I = Itoaster + Ifrying pan + Ilamp

= 15 A + 11 A + 0.83 A = 27 A

This  exceeds  the  20-A rating  of  the  line,  and  the  circuit  breaker
will indeed trip.

I = P>V
EVALUATE:  We could also ﬁnd the total current by using
and dividing the total power P delivered to all three devices by the
voltage:

I =

Ptoaster + Pfrying pan + Plamp
V
= 1800 W + 1300 W + 100 W
120 V

= 27 A

A third way to determine I is to use
equivalent resistance of the three devices in parallel:

I = V>Req

, where

Req

is the

I = V
Req

= 1120 V2a 1
8 Æ

+

1
11 Æ

+

1
144 Æ

b = 27 A

Appliances with such current demands are common, so modern
kitchens have more than one 20-A circuit. To keep currents safely
below 20 A, the toaster and frying pan should be plugged into dif-
ferent circuits.

Test Your Understanding of Section 26.5 To prevent the circuit breaker in
Example 26.14 from blowing, a home electrician replaces the circuit breaker with one
rated at 40 A. Is this a reasonable thing to do?

❙
