930

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

31-6 TRANSFORMERS

Learning Objectives
After reading this module, you should be able to . . .

31.49 For power transmission lines, identify why the

31.55 Apply the relationship between the current and number

transmission should be at low current and high voltage.
31.50 Identify the role of transformers at the two ends of a

of turns on the two sides of a transformer.

31.56 Apply the relationship between the power into and out

transmission line.

of an ideal transformer.

31.51 Calculate the energy dissipation in a transmission line.
31.52 Identify a transformer’s primary and secondary.
31.53 Apply the relationship between the voltage and
number of turns on the two sides of a transformer.

31.57 Identify the equivalent resistance as seen from the

primary side of a transformer.

31.58 Apply the relationship between the equivalent

resistance and the actual resistance.

31.54 Distinguish between a step-down transformer and a

31.59 Explain the role of a transformer in impedance

step-up transformer.

matching.

Key Ideas
● A transformer (assumed to be ideal) is an iron core on
which are wound a primary coil of Np turns and a secondary
coil of Ns turns. If the primary coil is connected across an
alternating-current generator, the primary and secondary
voltages are related by

Vs ! Vp

Ns
Np

(transformation of voltage).

● The currents through the coils are related by

Is ! Ip

Np
Ns

(transformation of currents).

● The equivalent resistance of the secondary circuit, as seen
by the generator, is

2

Req ! # Np
Ns $

R,

where R is the resistive load in the secondary circuit. The
ratio Np/Ns is called the transformer’s turns ratio.

Transformers
Energy Transmission Requirements
When  an  ac  circuit  has  only  a  resistive  load, the  power  factor  in  Eq. 31-76  is
cos 0° ! 1 and the applied rms emf #rms is equal to the rms voltage Vrms across the
load. Thus, with an rms current Irms in the load, energy is supplied and dissipated
at the average rate of

Pavg ! #I ! IV.

(31-77)

(In Eq. 31-77 and the rest of this module, we follow conventional practice and drop
the  subscripts  identifying  rms  quantities. Engineers  and  scientists  assume  that  all
time-varying currents and voltages are reported as rms values; that is what the me-
ters  read.)  Equation  31-77  tells  us  that, to  satisfy  a  given  power  requirement, we
have a range of choices for I and V, provided only that the product IV is as required.
In electrical power distribution systems it is desirable for reasons of safety
and for efficient equipment design to deal with relatively low voltages at both the
generating end (the electrical power plant) and the receiving end (the home or
factory). Nobody wants an electric toaster to operate at, say, 10 kV. However, in
the transmission of electrical energy from the generating plant to the consumer,
we want the lowest practical current (hence the largest practical voltage) to mini-
mize I 2R losses (often called ohmic losses) in the transmission line.

As an example, consider the 735 kV line used to transmit electrical energy
from the La Grande 2 hydroelectric plant in Quebec to Montreal, 1000 km away.
Suppose  that  the  current  is  500 A  and  the  power  factor  is  close  to  unity. Then
from Eq. 31-77, energy is supplied at the average rate

Pavg ! #I ! (7.35 & 10 5 V)(500 A) ! 368 MW.

31-6 TRANSFOR M E RS

931

Φ B

S

Vp

Np

Vs

R

Ns

Primary

Secondary

Figure 31-18 An ideal transformer (two coils
wound on an iron core) in a basic trans-
former circuit. An ac generator produces
current in the coil at the left (the primary).
The coil at the right (the secondary) is con-
nected to the resistive load R when switch S
is closed.

The resistance of the transmission line is about 0.220 "/km; thus, there is a total
resistance of about 220 " for the 1000 km stretch. Energy is dissipated due to that
resistance at a rate of about

Pavg ! I 2R ! (500 A)2(220 ") ! 55.0 MW,

which is nearly 15% of the supply rate.

Imagine what would happen if we doubled the current and halved the volt-
age. Energy would be supplied by the plant at the same average rate of 368 MW
as previously, but now energy would be dissipated at the rate of about

Pavg ! I 2R ! (1000 A)2(220 ") ! 220 MW,
which is almost 60% of the supply rate. Hence the general energy transmission
rule: Transmit at the highest possible voltage and the lowest possible current.

The Ideal Transformer
The transmission rule leads to a fundamental mismatch between the requirement
for efficient high-voltage transmission and the need for safe low-voltage gener-
ation  and  consumption. We  need  a  device  with  which  we  can  raise  (for  trans-
mission)  and  lower  (for  use)  the  ac  voltage  in  a  circuit, keeping  the  product
current
voltage  essentially  constant. The  transformer is  such  a  device. It  has
no moving  parts, operates  by  Faraday’s  law  of  induction, and  has  no  simple
direct-current counterpart.

&

The ideal transformer in Fig. 31-18 consists of two coils, with different num-
bers of turns, wound around an iron core. (The coils are insulated from the core.)
In use, the primary winding, of Np turns, is connected to an alternating-current
generator whose emf # at any time t is given by

# ! #m sin vt.

(31-78)

The  secondary  winding, of  Ns turns, is  connected  to  load  resistance  R, but  its
circuit  is  an  open  circuit  as  long  as  switch  S  is  open  (which  we  assume  for  the
present). Thus, there can be no current through the secondary coil. We assume
further for this ideal transformer that the resistances of the primary and second-
ary windings are negligible. Well-designed, high-capacity transformers can have
energy losses as low as 1%; so our assumptions are reasonable.

For  the  assumed  conditions, the  primary  winding  (or  primary)  is  a  pure
inductance and the primary circuit is like that in Fig. 31-12. Thus, the (very small)
primary current, also called the magnetizing current Imag, lags the primary voltage
Vp by 90°; the primary’s power factor (! cos f in Eq. 31-76) is zero; so no power
is delivered from the generator to the transformer.

However, the  small  sinusoidally  changing  primary  current  Imag produces  a
sinusoidally  changing  magnetic  flux  #B in  the  iron  core. The  core  acts  to
strengthen the flux and to bring it through the secondary winding (or secondary).
Because #B varies, it  induces  an  emf  #turn (! d#B/dt)  in  each  turn  of  the
secondary. In  fact, this  emf  per  turn  #turn is  the  same  in  the  primary  and  the
secondary. Across the primary, the voltage Vp is the product of #turn and the num-
ber of turns Np; that is, Vp ! #turnNp. Similarly, across the secondary the voltage is
Vs ! #turnNs. Thus, we can write

#turn !

Vp
Np

!

Vs
Ns

,

or

Vs ! Vp

Ns
Np

(transformation of voltage).

(31-79)

If Ns - Np, the device is a step-up transformer because it steps the primary’s voltage
Vp up to a higher voltage Vs. Similarly, if Ns / Np, it is a step-down transformer.

932

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

With switch S open, no energy is transferred from the generator to the rest of
the circuit, but when we close S to connect the secondary to the resistive load R,
energy is transferred. (In  general, the  load  would  also  contain  inductive  and
capacitive elements, but here we consider just resistance R.) Here is the process:

1. An alternating current Is appears in the secondary circuit, with corresponding

energy dissipation rate

2R (! V s
I s

2/R)

in the resistive load.

2. This current produces its own alternating magnetic flux in the iron core, and

this flux induces an opposing emf in the primary windings.

3. The  voltage  Vp of  the  primary, however, cannot  change  in  response  to  this
opposing emf because it must always be equal to the emf # that is provided by
the generator; closing switch S cannot change this fact.

4. To maintain Vp, the generator now produces (in addition to Imag) an alternat-
ing  current  Ip in  the  primary  circuit; the  magnitude  and  phase  constant  of
Ip are just those required for the emf induced by Ip in the primary to exactly
cancel the emf induced there by Is. Because the phase constant of Ip is not 90°
like that of Imag, this current Ip can transfer energy to the primary.

Energy Transfers. We want to relate Is to Ip. However, rather than analyze the
foregoing complex process in detail, let us just apply the principle of conservation
of energy. The rate at which the generator transfers energy to the primary is equal
to IpVp. The rate at which the primary then transfers energy to the secondary (via
the  alternating  magnetic  field  linking  the  two  coils)  is  IsVs. Because  we  assume
that no energy is lost along the way, conservation of energy requires that

Substituting for Vs from Eq. 31-79, we find that

IpVp ! IsVs.

Is ! Ip

Np
Ns

(transformation of currents).

(31-80)

This  equation  tells  us  that  the  current  Is in  the  secondary  can  differ  from  the
current Ip in the primary, depending on the turns ratio Np/Ns.

Current Ip appears in the primary circuit because of the resistive load R in
the secondary circuit. To find Ip, we substitute Is ! Vs/R into Eq. 31-80 and then
we substitute for Vs from Eq. 31-79. We find

Ip !

2

1

R # Ns
Np $

Vp.

(31-81)

This equation has the form Ip ! Vp/Req, where equivalent resistance Req is

2

Req ! # Np
Ns $
This Req is the value of the load resistance as “seen” by the generator; the genera-
tor produces the current Ip and voltage Vp as if the generator were connected to a
resistance Req.

(31-82)

R.

Impedance Matching
Equation 31-82 suggests still another function for the transformer. For maximum
transfer of energy from an emf device to a resistive load, the resistance of the emf
device  must  equal  the  resistance  of  the  load. The  same  relation  holds  for  ac
circuits except that the impedance (rather than just the resistance) of the genera-
tor must equal that of the load. Often this condition is not met. For example, in
a music-playing system, the amplifier has high impedance and the speaker set has
low  impedance. We  can  match  the  impedances  of  the  two  devices  by  coupling
them through a transformer that has a suitable turns ratio Np/Ns.

Checkpoint 8

An alternating-current emf device in a certain circuit has a smaller resistance than that
of the resistive load in the circuit; to increase the transfer of energy from the device to
the load, a transformer will be connected between the two. (a) Should Ns be greater
than or less than Np? (b) Will that make it a step-up or step-down transformer?

R EVI EW  &  SU M MARY

933

Sample Problem 31.08 Transformer: turns ratio, average power, rms currents

A transformer on a utility pole operates at Vp
8.5 kV on
the primary side and supplies electrical energy to a number
of  nearby  houses  at  Vs ! 120 V, both  quantities  being  rms
values.Assume an ideal step-down transformer, a purely resis-
tive load, and a power factor of unity.

!

(a) What is the turns ratio Np/Ns of the transformer?

KEY IDEA

The turns ratio Np/Ns is related to the (given) rms primary
and secondary voltages via Eq. 31-79 (Vs ! VpNs/Np).

Calculation: We can write Eq. 31-79 as

Eq. 31-77 yields

Ip !

Pavg
Vp

!

78 & 10 3 W
8.5 & 10 3 V

! 9.176 A % 9.2 A.

(Answer)

Similarly, in the secondary circuit,

Is !

Pavg
Vs

!

78 & 10 3 W
120 V

! 650 A.

(Answer)

You can check that Is ! Ip(Np/Ns) as required by Eq. 31-80.

(c) What is the resistive load Rs in the secondary circuit? What
is the corresponding resistive load Rp in the primary circuit?

Vs
Vp

!

Ns
Np

.

(31-83)

One way: We can use V ! IR to relate the resistive load to the
rms voltage and current. For the secondary circuit, we find

(Note that the right side of this equation is the inverse of the
turns ratio.) Inverting both sides of Eq. 31-83 gives us

Np
Ns

!

Vp
Vs

!

8.5 & 10 3 V
120 V

! 70.83 % 71.

(Answer)

(b) The average rate of energy consumption (or dissipation) in
the houses served by the transformer is 78 kW.What are the rms
currents in the primary and secondary of the transformer?

KEY IDEA

For a purely resistive load, the power factor cos f is unity; thus,
the  average  rate  at  which  energy  is  supplied  and  dissipated  is
given by Eq.31-77 (Pavg ! #I ! IV).

Calculations: In  the  primary  circuit, with  Vp

!

8.5 kV,

Rs !

Vs
Is

!

120 V
650 A

! 0.1846 " % 0.18 ".

(Answer)

Similarly, for the primary circuit we find

Rp !

Vp
Ip

!

8.5 & 10 3 V
9.176 A

! 926 " % 930 ".

(Answer)

Second way: We use the fact that Rp equals the equivalent re-
sistive load “seen” from the primary side of the transformer,
which is a resistance modified by the turns ratio and given by
Eq. 31-82 (Req ! (Np/Ns)2R). If we substitute Rp for Req and Rs
for R, that equation yields

2

Rp ! # Np
Ns $

Rs ! (70.83)2(0.1846 ")

! 926 " % 930 ".

(Answer)

Additional examples, video, and practice available at WileyPLUS

Review & Summary

LC Energy  Transfers In  an  oscillating  LC circuit, energy  is
shuttled periodically between the electric field of the capacitor and
the magnetic field of the inductor; instantaneous values of the two
forms of energy are

UE !

q2
2C

    and    UB !

Li2
2

,

(31-1, 31-2)

where q is the instantaneous charge on the capacitor and i is the

instantaneous  current  through  the  inductor. The  total  energy
U (! UE $ UB) remains constant.

LC Charge and Current Oscillations The principle of con-
servation of energy leads to

L

d 2q
dt 2 $

1
C

q ! 0

(LC oscillations)

(31-11)

934

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

as the differential equation of LC oscillations (with no resistance).
The solution of Eq. 31-11 is

q ! Q cos(vt $ f)

(charge),

(31-12)

in which Q is the charge amplitude (maximum charge on the capac-
itor) and the angular frequency v of the oscillations is

v !

1
LC

.

(31-4)

The phase constant f in Eq. 31-12 is determined by the initial con-
ditions (at t ! 0) of the system.

1

The current i in the system at any time t is

i ! ’vQ sin(vt $ f)

(current),

(31-13)

in which vQ is the current amplitude I.

Damped Oscillations Oscillations in an LC circuit are damped
when a dissipative element R is also present in the circuit.Then

For an inductor, VL ! IXL, in which XL ! vdL is the inductive
reactance; the  current  here  lags  the  potential  difference  by  90°
(f ! $90° ! $p/2 rad).

Series RLC Circuits For a series RLC circuit with an alternat-
ing  external  emf  given  by  Eq. 31-28  and  a  resulting  alternating
current given by Eq. 31-29,

I !

!

and

#m
R2 $ (XL ’ XC)2

2

2

#m
R2 $ (vdL ’ 1/vdC)2
XL ’ XC
R

tan f !

(current amplitude) (31-60, 31-63)

(phase constant).

(31-65)

Defining the impedance Z of the circuit as

Z !

R2 $ (XL ’ XC)2

(impedance)

(31-61)

L

d 2q
dt 2 $ R

dq
dt

$

1
C

q ! 0

(RLC circuit).

(31-24)

allows us to write Eq. 31-60 as I ! #m/Z.

2

The solution of this differential equation is

q ! Qe’Rt/2L cos(v*t $ f),

where

v* !

v2 ’ (R/2L)2.

Power
In  a  series  RLC circuit, the  average  power Pavg of  the
generator is equal to the production rate of thermal energy in the
resistor:

Pavg ! I 2

rmsR ! #rmsIrms cos f.

(31-71, 31-76)

(31-25)

(31-26)

We consider only situations with small R and thus small damping;
then v* % v.

2

Alternating Currents; Forced Oscillations A series RLC
circuit may be set into forced oscillation at a driving angular fre-
quency vd by an external alternating emf

# ! #m sin vdt.

The current driven in the circuit is

i ! I sin(vdt ’ f),

where f is the phase constant of the current.

(31-28)

(31-29)

Resonance The  current  amplitude  I in  a  series  RLC circuit
driven by a sinusoidal external emf is a maximum (I ! #m/R) when
the  driving  angular  frequency  vd equals  the  natural  angular
frequency  v of  the  circuit  (that  is, at  resonance). Then  XC ! XL,
f ! 0, and the current is in phase with the emf.

Single Circuit Elements The alternating potential difference
across  a  resistor  has  amplitude  VR ! IR; the  current  is  in phase
with the potential difference.

For a capacitor, VC ! IXC, in which XC ! 1/vdC is the capacitive
reactance; the  current  here  leads  the  potential  difference  by  90°
(f ! ’90° ! ’p/2 rad).

Questions

1 Figure 31-19 shows three oscillating LC circuits with identical
inductors and capacitors. At a particular time, the charges on the
capacitor  plates  (and  thus  the  electric  fields  between  the  plates)
are all at their maximum values. Rank the circuits according to the
time taken to fully discharge the capacitors during the oscillations,
greatest first.

Here  rms  stands  for  root-mean-square; the  rms  quantities  are
related  to  the  maximum  quantities  by
2,
The term cos f is called the power factor of the
and
circuit.

erms ! em /

2, Vrms !

Irms ! I/

V/

1

1

2.

1

Transformers A transformer (assumed to be ideal) is an iron core
on which are wound a primary coil of Np turns and a secondary coil of
Ns turns. If the primary coil is connected across an alternating-current
generator, the primary and secondary voltages are related by

Vs ! Vp

Ns
Np

(transformation of voltage).

(31-79)

The currents through the coils are related by

Is ! Ip

Np
Ns

(transformation of currents),

(31-80)

and the equivalent resistance of the secondary circuit, as seen by
the generator, is

Req ! # Np
Ns $

2
R,

(31-82)

where R is  the  resistive  load  in  the  secondary  circuit. The  ratio
Np/Ns is called the transformer’s turns ratio.

(a)

(b)

(c)

Figure 31-19 Question 1.

2 Figure  31-20  shows  graphs  of  capacitor  voltage  vC for LC
circuits 1 and 2, which contain identical capacitances and have the
same  maximum  charge  Q. Are  (a)  the  inductance  L and  (b)  the
maximum current I in circuit 1 greater than, less than, or the same
as those in circuit 2?

vC

t

2

1

Figure 31-20 Question 2.

3 A  charged  capacitor  and  an  inductor  are  connected  at  time
t ! 0. In terms of the period T of the resulting oscillations, what is
the  first  later  time  at  which  the  following  reach  a maximum: (a)
UB, (b)  the  magnetic  flux  through  the  inductor, (c) di/dt, and  (d)
the emf of the inductor?

4 What values of phase constant f in Eq. 31-12 allow situations
(a), (c), (e), and (g) of Fig. 31-1 to occur at t ! 0?

Z

5 Curve a in  Fig. 31-21  gives  the
impedance Z of a driven RC circuit
versus  the  driving  angular  fre-
quency vd. The other two curves are
similar  but  for  different  values  of
resistance R and  capacitance  C.
Rank the three curves according to
the corresponding value of R, great-
est first.

c

b

a

ω d

6 Charges  on  the  capacitors  in
three oscillating LC circuits vary as:
(1) q ! 2 cos 4t, (2) q ! 4 cos t, (3) q ! 3 cos 4t (with q in coulombs
and t in  seconds). Rank  the  circuits  according  to  (a)  the  current
amplitude and (b) the period, greatest first.

Figure 31-21 Question 5.

a

7 An alternating emf source with a
certain emf amplitude is connected,
in turn, to a resistor, a capacitor, and
then an inductor. Once connected to
one  of  the  devices, the  driving  fre-
quency  fd is  varied  and  the  ampli-
tude I of  the  resulting  current
through the device is measured and
plotted. Which of the three plots in
Fig. 31-22 corresponds to which of the three devices?

b

I

c

fd

Figure 31-22 Question 7.

PROB LE M S

935

8 The values of the phase constant f for four sinusoidally driven
series RLC circuits  are  (1)  ’15°, (2) $35°, (3)  p/3  rad, and
(4) ’p/6 rad. (a) In which is the load primarily capacitive? (b) In
which does the current lag the alternating emf?

9 Figure  31-23  shows  the  current  i
and  driving  emf  # for  a series  RLC
circuit. (a) Is the phase constant posi-
tive or negative? (b) To increase the
rate  at  which  energy  is  transferred
to the resistive load, should L be in-
creased or decreased? (c) Should, in-
stead, C be  increased  or  decreased?

, i

i

t

Figure 31-23 Question 9.

10 Figure 31-24 shows three situations like those of Fig. 31-15. Is
the driving angular frequency greater than, less than, or equal to
the resonant angular frequency of the circuit in (a) situation 1, (b)
situation 2, and (c) situation 3?

I

m

(1)

(2)

I

m

I

m

(3)

Figure 31-24 Question 10.

11 Figure 31-25 shows the current
i and driving emf # for a series RLC
circuit. Relative  to  the  emf  curve,
does the current curve shift leftward
or rightward and does the amplitude
of that curve increase or decrease if
we slightly increase (a) L, (b) C, and
(c) vd?

, i

i

t

Figure 31-25 Questions 11
and 12.

12 Figure 31-25 shows the current i and driving emf # for a series
RLC circuit. (a) Does the current lead or lag the emf? (b) Is the
circuit’s load mainly capacitive or mainly inductive? (c) Is the an-
gular  frequency  vd of  the  emf  greater  than  or
less than the natural angular frequency v?

13 Does the phasor diagram of Fig. 31-26 corre-
spond to an alternating emf source connected to a
resistor, a capacitor, or an inductor? (b) If the an-
gular  speed  of  the  phasors  is  increased, does  the
length of the current phasor increase or decrease
when the scale of the diagram is maintained?

I

vd

V

Figure 31-26
Question 13.

Problems

Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign

SSM Worked-out solution available in Student Solutions Manual
• – ••• Number of dots indicates level of problem difficulty

WWW Worked-out solution is at

ILW Interactive solution is at

http://www.wiley.com/college/halliday

Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com

LC Oscillations

Module 31-1
•1 An oscillating LC circuit consists of a 75.0 mH inductor and a
3.60 mF  capacitor. If  the  maximum  charge  on  the  capacitor  is
2.90 mC, what  are  (a)  the  total  energy  in  the  circuit  and  (b)  the
maximum current?

•2 The frequency of oscillation of a certain LC circuit is 200 kHz. At
time t ! 0, plate A of the capacitor has maximum positive charge. At
what earliest time t - 0 will (a) plate A again have maximum positive
charge, (b) the other plate of the capacitor have maximum positive
charge, and (c) the inductor have maximum magnetic field?

936

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

•3 In a certain oscillating LC circuit, the total energy is converted
from electrical energy in the capacitor to magnetic energy in the
inductor  in  1.50 ms. What  are  (a)  the  period  of  oscillation  and
(b) the frequency of oscillation? (c) How long after the magnetic
energy is a maximum will it be a maximum again?

•4 What is the capacitance of an oscillating LC circuit if the maxi-
mum  charge  on  the  capacitor  is  1.60 mC  and  the  total  energy  is
140 mJ?

•5 In  an  oscillating  LC circuit, L ! 1.10 mH  and  C ! 4.00 mF.
The maximum charge on the capacitor is 3.00 mC. Find the maxi-
mum current.

•6 A 0.50 kg body oscillates in SHM on a spring that, when ex-
tended 2.0 mm from its equilibrium position, has an 8.0 N restoring
force. What are (a) the angular frequency of oscillation, (b) the pe-
riod of oscillation, and (c) the capacitance of an LC circuit with the
same period if L is 5.0 H?

SSM

The  energy  in  an  oscillating  LC circuit  containing  a
•7
1.25 H inductor is 5.70 mJ. The maximum charge on the capacitor is
175 mC. For  a  mechanical  system  with  the  same  period, find  the
(a) mass, (b)  spring  constant, (c)  maximum  displacement, and
(d) maximum speed.

•8 A single loop consists of inductors (L1, L2, . . .), capacitors (C1,
C2, . . .), and resistors (R1, R2, . . .) connected in series as shown, for
example, in  Fig. 31-27a. Show  that  regardless  of  the  sequence  of
these  circuit  elements  in  the  loop, the  behavior  of  this  circuit  is
identical  to  that  of  the  simple  LC circuit  shown  in  Fig. 31-27b.
(Hint: Consider the loop rule and see Problem 47 in Chapter 30.)

L 1

C 1

L 2

R 1

C 2

R 2

L

C

R

(a )

(b )

Figure 31-27 Problem 8.

ILW

In  an  oscillating  LC circuit  with  L ! 50 mH  and  C !
•9
4.0 mF, the  current  is  initially  a  maximum. How  long  will  it  take
before the capacitor is fully charged for the first time?

•10 LC oscillators have been used in circuits connected to loud-
speakers  to  create  some  of  the  sounds  of  electronic  music. What
inductance must be used with a 6.7 mF capacitor to produce a fre-
quency of 10 kHz, which is near the middle of the audible range of
frequencies?

SSM

WWW

A  variable  capacitor  with  a  range  from  10  to
••11
365 pF is used with a coil to form a variable-frequency LC circuit
to tune the input to a radio. (a) What is the ratio of maximum fre-
quency  to  minimum  frequency  that  can  be  obtained  with  such  a
capacitor?  If  this  circuit  is  to  obtain  frequencies  from  0.54 MHz
to 1.60 MHz, the  ratio  computed  in  (a)  is  too  large. By  adding  a
capacitor  in  parallel  to  the  variable  capacitor, this  range  can  be
adjusted. To obtain the desired frequency range, (b) what capaci-
tance  should  be  added  and  (c)  what  inductance  should  the  coil
have?

••12 In an oscillating LC circuit, when 75.0% of the total energy
is stored in the inductor’s magnetic field, (a) what multiple of the
maximum charge is on the capacitor and (b) what multiple of the
maximum current is in the inductor?

••13 In an oscillating LC circuit, L ! 3.00 mH and C ! 2.70 mF.
At t ! 0 the charge on the capacitor is zero and the current is 2.00 A.
(a) What is the maximum charge that will appear on the capacitor?
(b) At what earliest time t - 0 is the rate at which energy is stored
in the capacitor greatest, and (c) what is that greatest rate?

••14 To construct an oscillating LC system, you can choose from
a 10 mH inductor, a 5.0 mF capacitor, and a 2.0 mF capacitor. What
are the (a) smallest, (b) second smallest, (c) second largest, and (d)
largest oscillation frequency that can be set up by these elements in
various combinations?

ILW

An oscillating LC circuit consisting of a 1.0 nF capacitor
••15
and a 3.0 mH coil has a maximum voltage of 3.0 V. What are (a) the
maximum  charge  on  the  capacitor, (b)  the  maximum  current
through  the  circuit, and  (c)  the  maximum  energy  stored  in  the
magnetic field of the coil?

inductor

••16 An
is  connected  across  a  capacitor  whose
capacitance can be varied by turning a knob. We wish to make the
frequency of oscillation of this LC circuit vary linearly with the an-
gle of rotation of the knob, going from 2 & 105 to 4 & 105 Hz as the
knob turns through 180°. If L ! 1.0 mH, plot the required capaci-
tance C as a function of the angle of rotation of the knob.

!

ILW

In Fig. 31-28, R ! 14.0
••17
, C 6.20 mF, and  L 54.0 mH,
"
!
and  the  ideal  battery  has  emf  # !
34.0 V. The  switch  is  kept  at  a for  a
long  time  and  then  thrown  to  posi-
tion b. What  are  the  (a)  frequency
and  (b)  current  amplitude  of  the
resulting oscillations?

R

a
b

C
L

Figure 31-28 Problem 17.

••18 An oscillating LC circuit has a
current  amplitude  of  7.50 mA, a  potential  amplitude  of  250 mV,
and a capacitance of 220 nF. What are (a) the period of oscillation,
(b) the maximum energy stored in the capacitor, (c) the maximum
energy stored in the inductor, (d) the maximum rate at which the
current changes, and (e) the maximum rate at which the inductor
gains energy?

••19 Using the loop rule, derive the differential equation for an
LC circuit (Eq. 31-11).

In  an  oscillating  LC circuit  in  which  C ! 4.00 mF, the
••20
maximum  potential  difference  across  the  capacitor  during  the
oscillations is 1.50 V and the maximum current through the inductor
is 50.0 mA. What are (a) the inductance L and (b) the frequency of
the oscillations? (c) How much time is required for the charge on
the capacitor to rise from zero to its maximum value?

!

(1.60) sin(2500t

In an oscillating LC circuit with C ! 64.0 mF, the current
••21
ILW
$
is given by i
0.680), where t is in seconds, i in
amperes, and the phase constant in radians. (a) How soon after t ! 0
will the current reach its maximum value? What are (b) the induc-
tance L and (c) the total energy?

••22 A  series  circuit  containing  inductance  L1 and  capacitance
C1 oscillates at angular frequency v. A second series circuit, con-
taining  inductance  L2 and  capacitance  C2, oscillates  at  the  same
angular frequency. In terms of v, what is the angular frequency of
oscillation of a series circuit containing all four of these elements?
Neglect resistance. (Hint: Use the formulas for equivalent capaci-
tance and equivalent inductance; see Module 25-3 and Problem 47
in Chapter 30.)

!

In  an  oscillating  LC circuit, L ! 25.0 mH  and  C !
••23
7.80 mF. At  time  t
0  the  current  is  9.20 mA, the  charge  on  the
capacitor is 3.80 mC, and the capacitor is charging. What are (a) the
total energy in the circuit, (b) the maximum charge on the capaci-
tor, and (c) the maximum current? (d) If the charge on the capaci-
tor  is  given  by  q ! Q cos(vt $ f), what  is  the  phase  angle  f?
(e) Suppose  the  data  are  the  same, except  that  the  capacitor  is
discharging at t ! 0. What then is f?

Module 31-2 Damped Oscillations in an RLC Circuit
A single-loop circuit consists of a 7.20 " resistor, a 12.0 H
••24
inductor, and  a  3.20 mF  capacitor. Initially  the  capacitor  has  a
charge of 6.20 mC and the current is zero. Calculate the charge on
the capacitor N complete cycles later for (a) N ! 5, (b) N ! 10, and
(c) N ! 100.

ILW

What resistance R should be connected in series with an
••25
inductance L 220 mH  and  capacitance  C 12.0 mF  for  the
maximum charge on the capacitor to decay to 99.0% of its initial
value in 50.0 cycles? (Assume v* % v.)

!

!

In an oscillating series RLC circuit, find the time required
••26
for the maximum energy present in the capacitor during an oscilla-
tion to fall to half its initial value. Assume q ! Q at t ! 0.

SSM

In an oscillating series RLC circuit, show that )U/U,
•••27
the fraction of the energy lost per cycle of oscillation, is given to a
close approximation by 2pR/vL. The quantity vL/R is often called
the Q of  the  circuit  (for  quality). A  high-Q circuit  has  low  resis-
tance and a low fractional energy loss (! 2p/Q) per cycle.

Module  31-3 Forced  Oscillations  of  Three  Simple  Circuits
•28 A 1.50 mF capacitor is connected as in Fig. 31-10 to an ac gen-
erator  with  #m ! 30.0 V. What  is  the  amplitude  of  the  resulting
alternating current if the frequency of the emf is (a) 1.00 kHz and
(b) 8.00 kHz?

ILW

A 50.0 mH inductor is connected as in Fig. 31-12 to an ac
•29
generator with
30.0 V. What is the amplitude of the resulting
alternating current if the frequency of the emf is (a) 1.00 kHz and
(b) 8.00 kHz?

#m !

•30 A 50.0 " resistor is connected as in Fig. 31-8 to an ac genera-
tor with
30.0 V. What is the amplitude of the resulting alter-
nating  current  if  the  frequency  of  the  emf  is  (a) 1.00 kHz  and
(b) 8.00 kHz?

#m !

•31 (a) At what frequency would a 6.0 mH inductor and a 10 mF
capacitor have the same reactance? (b) What would the reactance
be? (c) Show that this frequency would be the natural frequency of
an oscillating circuit with the same L and C.

0d !

An ac generator has emf # ! #m sin vdt, with #m ! 25.0 V
••32
and
377 rad/s. It is connected to a 12.7 H inductor. (a) What is
the maximum value of the current? (b) When the current is a maxi-
mum, what  is  the  emf  of  the  generator?  (c)  When  the  emf  of
the generator is ’12.5 V and increasing in magnitude, what is the
current?

SSM
30.0 V and

An ac generator has emf # ! #m sin(vdt ’ p/4), where
••33
#m !
0d !
350 rad/s. The  current  produced  in  a  con-
3p/4), where  I
!
I sin(
nected  circuit  is  i(t)
620 mA. At
!
what  time  after  t
0  does  (a)  the  generator  emf  first  reach  a
maximum and (b) the current first reach a maximum? (c) The cir-
cuit contains a single element other than the generator. Is it a ca-
pacitor, an inductor, or a resistor? Justify your answer. (d) What is

’0d
t

!

PROB LE M S

937

the value of the capacitance, inductance, or resistance, as the case
may be?

!

An  ac  generator  with  emf  # ! #m sin vdt, where  #m !
••34
25.0 V  and  vd
377 rad/s, is  connected  to  a  4.15 mF  capacitor.
(a) What is the maximum value of the current? (b) When the cur-
rent is a maximum, what is the emf of the generator? (c) When the
emf of the generator is ’12.5 V and increasing in magnitude, what
is the current?

The Series RLC Circuit

Module 31-4
A coil of inductance 88 mH and unknown resistance and
•35
ILW
a 0.94 mF capacitor are connected in series with an alternating emf
of  frequency  930 Hz. If  the  phase  constant  between  the  applied
voltage and the current is 75°, what is the resistance of the coil?

•36 An alternating source with a variable frequency, a capacitor
with capacitance C, and a resistor with resistance R are connected
in series. Figure 31-29 gives the impedance Z of the circuit versus
the driving angular frequency vd; the curve reaches an asymptote
of 500 ", and the horizontal scale is set by vds ! 300 rad/s. The fig-
ure also gives the reactance XC for the capacitor versus vd. What
are (a) R and (b) C?

)
Ω
(

C
X

,

Z

800

400

0

Z

XC

ω d (rad/s)
d (rad/s)
ω

Figure 31-29 Problem 36.

dsω

•37 An electric motor has an effective resistance of 32.0 " and an
inductive  reactance  of  45.0  " when  working  under  load. The
voltage amplitude across the alternating source is 420 V. Calculate
the current amplitude.

Is

•38 The current amplitude I versus
driving  angular  frequency  vd for  a
driven RLC circuit  is  given  in  Fig.
31-30, where the vertical axis scale is
set  by  Is !  4.00  A. The  inductance
is 200 mH, and the emf amplitude is
8.0 V.What are (a) C and (b) R?

)
A
(

I

0
10

30

50

ω

d (1000 rad/s)
d (1000 rad/s)

inductor  from
•39 Remove  the
the circuit  in  Fig. 31-7  and  set  R !
200 ", C ! 15.0 mF, fd ! 60.0 Hz, and #m ! 36.0 V. What are (a) Z,
(b) f, and (c) I? (d) Draw a phasor diagram.

Figure 31-30 Problem 38.

•40 An alternating source drives a series RLC circuit with an emf
amplitude of 6.00 V, at a phase angle of $30.0°. When the potential
difference across the capacitor reaches its maximum positive value
of
5.00 V, what  is  the  potential  difference  across  the  inductor
(sign included)?

$

SSM
60.0 Hz, and

•41
!
fd
(d) Draw a phasor diagram.

#m !

In  Fig. 31-7, set  R ! 200 ", C ! 70.0 mF, L ! 230 mH,
36.0 V. What  are  (a)  Z, (b)  f, and  (c)  I?

•42 An alternating source with a variable frequency, an inductor

938

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

with  inductance  L, and  a  resistor
with  resistance  R are  connected  in
series. Figure 31-31 gives the imped-
ance Z of the circuit versus the driv-
ing  angular  frequency  vd, with  the
horizontal  axis  scale  set  by  vds !
1600 rad/s. The figure also gives the
reactance XL for the inductor versus
vd. What are (a) R and (b) L?

)
Ω
(

L
X

,

Z

120

80

40

0

Z

XL

dsω

ω

d (rad/s)

Figure 31-31 Problem 42.

•43 Remove  the  capacitor  from
the  circuit  in  Fig. 31-7  and  set  R !
200 ", L ! 230 mH, fd ! 60.0 Hz, and #m ! 36.0 V. What are (a) Z,
(b) f, and (c) I? (d) Draw a phasor diagram.

!

An ac generator with emf amplitude #m ! 220 V and op-
••44
erating at frequency 400 Hz causes oscillations in a series RLC cir-
cuit having R 220 ", L ! 150 mH, and C ! 24.0 mF. Find (a) the
capacitive reactance XC, (b) the impedance Z, and (c) the current
amplitude I. A  second  capacitor  of  the  same  capacitance  is  then
connected  in  series  with  the  other  components. Determine
whether the values of (d) XC, (e) Z, and (f) I increase, decrease, or
remain the same.

ILW

(a) In an RLC circuit, can the amplitude of the volt-
••45
age across an inductor be greater than the amplitude of the gener-
ator emf? (b) Consider an RLC circuit with emf amplitude #m !
10 V, resistance R ! 10 ", inductance L ! 1.0 H, and capacitance
C ! 1.0 mF. Find the amplitude of the voltage across the inductor
at resonance.

An alternating emf source with a variable frequency fd is
••46
resistor and a 20.0 mF capacitor.
"
connected in series with a 50.0
The emf amplitude is 12.0 V. (a) Draw a phasor diagram for phasor
VR (the potential across the resistor) and phasor VC (the potential
across the capacitor). (b) At what driving frequency fd do the two
phasors have the same length? At that driving frequency, what are
(c) the phase angle in degrees, (d) the angular speed at which the
phasors rotate, and (e) the current amplitude?

"

!

WWW
, C 20.0 mF, L 1.00 H, and
!

An RLC circuit  such  as  that  of  Fig. 31-7  has
••47
SSM
!
R 5.00
30.0 V. (a)  At
what angular frequency vd will the current amplitude have its max-
imum value, as in the resonance curves of Fig. 31-16? (b) What is
this maximum value? At what (c) lower angular frequency vd1 and
(d) higher angular frequency vd2 will the current amplitude be half
this maximum value? (e) For the resonance curve for this circuit,
what is the fractional half-width (vd1 ’ vd2)/v?

#m !

Figure 31-32 shows a driven RLC circuit that contains two
••48
identical capacitors and two switches. The emf amplitude is set at
12.0 V, and  the  driving  frequency  is  set  at  60.0 Hz. With  both
switches open, the current leads the emf by 30.9°. With switch S1
closed and switch S2 still open, the emf leads the current by 15.0°.
With both switches closed, the current amplitude is 447 mA. What
are (a) R, (b) C, and (c) L?

R

G

"

!

L 1

In Fig. 31-33, a genera-
••49
tor with an adjustable frequency
of oscillation is connected to re-
sistance R 100
, inductances
L1 ! 1.70 mH  and  L2 ! 2.30
mH, and capacitances C1 ! 4.00
mF, C2 ! 2.50 mF, and  C3 ! 3.50
mF. (a) What is the resonant fre-
quency of the circuit? (Hint: See Problem 47 in Chapter 30.) What
happens to the resonant frequency if (b) R is increased, (c) L1 is in-
creased, and (d) C3 is removed from the circuit?

Figure 31-33 Problem 49.

C 3

C 2

C 1

L 2

••50 An alternating emf source with a variable frequency fd is con-
nected in series with an 80.0 " resistor and a 40.0 mH inductor. The
emf amplitude is 6.00 V. (a) Draw a phasor diagram for phasor VR
(the  potential  across  the  resistor)  and  phasor  VL (the  potential
across the inductor). (b) At what driving frequency fd do the two
phasors have the same length? At that driving frequency, what are
(c) the phase angle in degrees, (d) the angular speed at which the
phasors rotate, and (e) the current amplitude?

SSM

The  fractional  half-width  )vd of  a  resonance  curve,
••51
such as the ones in Fig. 31-16, is the width of the curve at half the
maximum value of I. Show that )vd/v ! R(3C/L)1/2, where v is the
angular  frequency  at  resonance. Note  that  the  ratio  )vd/v in-
creases with R, as Fig. 31-16 shows.

Module 31-5 Power in Alternating-Current Circuits
•52 An ac voltmeter with large impedance is connected in turn
across the inductor, the capacitor, and the resistor in a series circuit
having an alternating emf of 100 V (rms); the meter gives the same
reading in volts in each case. What is this reading?

SSM

An air conditioner connected to a 120 V rms ac line is
•53
equivalent to a 12.0
inductive reactance
resistance and a 1.30
in  series. Calculate  (a)  the  impedance  of  the  air  conditioner  and
(b) the average rate at which energy is supplied to the appliance.

"

"

•54 What is the maximum value of an ac voltage whose rms value
is 100 V?

•55 What direct current will produce the same amount of ther-
mal energy, in a particular resistor, as an alternating current that
has a maximum value of 2.60 A?

L

B

To energy
supply

••56 A typical light dimmer used to
dim the stage lights in a theater con-
sists of a variable inductor L (whose
inductance  is  adjustable  between
zero  and  Lmax)  connected  in  series
with  a  lightbulb  B, as  shown  in
Fig. 31-34. The  electrical  supply  is
120 V  (rms)  at  60.0 Hz; the  lightbulb  is  rated  at  120 V, 1000 W.
(a) What  Lmax is  required  if  the  rate  of  energy  dissipation  in
the lightbulb is to be varied by a factor of 5 from its upper limit of
1000 W? Assume  that  the  resistance  of  the  lightbulb  is  indepen-
dent  of  its  temperature. (b)  Could  one  use  a  variable  resistor
(adjustable between zero and Rmax) instead of an inductor? (c) If
so, what Rmax is required? (d) Why isn’t this done?

Figure 31-34 Problem 56.

S1

C

R

S2

L

C

Figure 31-32 Problem 48.

••57 In an RLC circuit such as that of Fig. 31-7 assume that R !
5.00 ", L ! 60.0 mH, fd ! 60.0 Hz, and #m ! 30.0 V. For what val-
ues of the capacitance would the average rate at which energy is
dissipated in the resistance be (a) a maximum and (b) a minimum?
What are (c) the maximum dissipation rate and the corresponding

(d) phase angle and (e) power factor? What are (f) the minimum
dissipation  rate  and  the  corresponding  (g)  phase  angle  and
(h) power factor?

••58 For Fig. 31-35, show that the av-
erage rate at which energy is dissipated
in resistance R is a maximum when R is
equal to the internal resistance r of the
ac generator. (In the text discussion we
tacitly assumed that r ! 0.)

r

R

In Fig. 31-7, R ! 15.0 ", C !
••59
4.70 mF, and L ! 25.0 mH. The gener-
ator provides an emf with rms voltage
75.0 V and frequency 550 Hz. (a) What is the rms current? What is
the rms voltage across (b) R, (c) C, (d) L, (e) C and L together, and
(f) R, C, and L together? At what average rate is energy dissipated
by (g) R, (h) C, and (i) L?

Figure 31-35 Problems 58
and 66.

1

!
#m !

sin vdt with

#m ! #m
!

3000 rad/s. For  time  t

In  a  series  oscillating  RLC circuit, R 16.0 ", C 5
••60
!
31.2 F, L 9.20 mH, and
45.0 V and
vd !
0.442 ms  find  (a)  the  rate  Pg
at which energy is being supplied by the generator, (b) the rate PC
at which the energy in the capacitor is changing, (c) the rate PL at
which the energy in the inductor is changing, and (d) the rate PR at
which  energy  is  being  dissipated  in  the  resistor. (e)  Is  the  sum
of PC, PL, and PR greater than, less than, or equal to Pg?

SSM

WWW

Figure  31-36
••61
shows an ac generator connected to a
“black box” through a pair of termi-
nals. The  box  contains  an  RLC cir-
cuit, possibly  even  a  multiloop  cir-
cuit, whose elements and connections
we do not know. Measurements out-
side the box reveal that

i(t)

(t)

?

Figure 31-36 Problem 61.

and

#(t) ! (75.0 V) sin vdt
i(t) ! (1.20 A) sin(vdt $ 42.0°).

(a) What is the power factor? (b) Does the current lead or lag the
emf?  (c)  Is  the  circuit  in  the  box  largely  inductive  or  largely
capacitive?  (d)  Is  the  circuit  in  the  box  in  resonance?  (e)  Must
there be a capacitor in the box? (f) An inductor? (g) A resistor?
(h) At  what  average  rate  is  energy  delivered  to  the  box  by  the
generator? (i) Why don’t you need to know vd to answer all these
questions?

Transformers

Module 31-6
•62 A generator supplies 100 V to a transformer’s primary coil,
which has 50 turns. If the secondary coil has 500 turns, what is the
secondary voltage?

ILW

SSM

A transformer has 500 primary turns and 10 sec-
•63
ondary  turns. (a)  If  Vp is  120 V  (rms), what  is  Vs with  an  open
circuit? If the secondary now has a resistive
load of 15 ", what is the current in the (b)
primary and (c) secondary?

T3

•64 Figure  31-37  shows  an  “autotrans-
former.” It consists of a single coil (with an
iron  core). Three  taps  Ti are  provided.
Between taps T1 and T2 there are 200 turns,
and  between  taps  T2 and T3 there  are  800
turns. Any two taps can be chosen as the pri-
mary  terminals, and  any  two  taps  can  be
chosen  as  the  secondary  terminals. For

T2

T1

Figure 31-37
Problem 64.

PROB LE M S

939

choices producing a step-up transformer, what are the (a) smallest,
(b) second smallest, and (c) largest values of the ratio Vs/Vp? For
a step-down  transformer, what  are  the  (d) smallest, (e)  second
smallest, and (f) largest values of Vs/Vp?

••65 An ac generator provides emf to a resistive load in a remote
factory  over  a  two-cable  transmission  line. At  the  factory  a  step-
down transformer reduces the voltage from its (rms) transmission
value Vt to a much lower value that is safe and convenient for use
in the factory. The transmission line resistance is 0.30 "/cable, and
the  power  of  the  generator  is  250 kW. If  Vt ! 80 kV, what  are
(a) the voltage decrease )V along the transmission line and (b) the
rate Pd at which energy is dissipated in the line as thermal energy?
If Vt ! 8.0 kV, what are (c) )V and (d) Pd? If Vt ! 0.80 kV, what
are (e) )V and (f) Pd?

Additional Problems
66 In Fig. 31-35, let the rectangular box on the left represent the
(high-impedance) output of an audio amplifier, with r ! 1000 ".
Let R ! 10 " represent  the  (low-impedance)  coil  of  a loud-
speaker. For maximum transfer of energy to the load R we must
have R ! r, and  that  is  not  true  in  this  case. However, a  trans-
former can be used to “transform” resistances, making them be-
have electrically as if they were larger or smaller than they actu-
ally  are. (a)  Sketch  the  primary  and  secondary  coils  of  a
transformer  that  can  be  introduced  between  the  amplifier  and
the speaker in Fig. 31-35 to match the impedances. (b) What must
be the turns ratio?

!

!#

30.0 V and vd

An  ac  generator  produces  emf  # ! #m sin(vdt ’ p/4),
67
where m
350 rad/s. The current in the circuit
attached  to  the  generator  is  i(t) ! I sin(vdt $ p/4), where  I !
620 mA. (a) At what time after t ! 0 does the generator emf first
reach a maximum? (b) At what time after t ! 0 does the current
first  reach  a  maximum?  (c) The  circuit  contains  a  single  element
other than the generator. Is it a capacitor, an inductor, or a resis-
tor? Justify your answer. (d) What is the value of the capacitance,
inductance, or resistance, as the case may be?

68 A series RLC circuit is driven by a generator at a frequency
of 2000 Hz  and  an  emf  amplitude  of  170 V. The  inductance  is
60.0 mH, the capacitance is 0.400 mF, and the resistance is 200 ".
(a) What is the phase constant in radians? (b) What is the current
amplitude?

69 A generator of frequency 3000 Hz drives a series RLC circuit
with an emf amplitude of 120 V. The resistance is 40.0 ", the capac-
itance is 1.60 mF, and the inductance is 850 mH. What are (a) the
phase constant in radians and (b) the current amplitude? (c) Is the
circuit capacitive, inductive, or in resonance?

70 A 45.0 mH inductor has a reactance of 1.30 k". (a) What is its
operating frequency? (b) What is the capacitance of a capacitor with
the same reactance at that frequency? If the frequency is doubled,
what is the new reactance of (c) the inductor and (d) the capacitor?

71 An RLC circuit  is  driven  by  a  generator  with  an  emf
amplitude  of  80.0 V  and  a  current  amplitude  of  1.25 A. The
current leads  the  emf  by  0.650 rad. What  are  the  (a)  impedance
and (b) resistance of the circuit? (c) Is the circuit inductive, capaci-
tive, or in resonance?

72 A series RLC circuit is driven in such a way that the maxi-
mum voltage across the inductor is 1.50 times the maximum volt-
age  across  the  capacitor  and  2.00  times  the  maximum  voltage
across the resistor. (a) What is f for the circuit? (b) Is the circuit

940

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

inductive, capacitive, or  in  resonance? The  resistance  is  49.9  ",
and the current amplitude is 200 mA. (c) What is the amplitude
of the driving emf?

73 A  capacitor  of  capacitance  158 mF  and  an  inductor  form  an
LC circuit that oscillates at 8.15 kHz, with a current amplitude of
4.21 mA. What are (a) the inductance, (b) the total energy in the
circuit, and (c) the maximum charge on the capacitor?

74 An oscillating LC circuit has an inductance of 3.00 mH and a
capacitance  of  10.0 mF. Calculate  the  (a)  angular  frequency  and
(b) period  of  the  oscillation. (c)  At  time  t ! 0, the  capacitor  is
charged  to  200 mC  and  the  current  is  zero. Roughly  sketch  the
charge on the capacitor as a function of time.

75 For a certain driven series RLC circuit, the maximum genera-
tor emf is 125 V and the maximum current is 3.20 A. If the current
leads the generator emf by 0.982 rad, what are the (a) impedance
and (b) resistance of the circuit? (c) Is the circuit predominantly
capacitive or inductive?

76 A  1.50 mF  capacitor  has  a  capacitive  reactance  of  12.0  ".
(a) What  must  be  its  operating  frequency?  (b) What  will  be  the
capacitive reactance if the frequency is doubled?

SSM

In Fig. 31-38, a three-phase generator G produces electri-
77
cal power that is transmitted by means of three wires. The electric
potentials  (each  relative  to  a  common  reference  level)  are  V1 !
A sin vdt for  wire  1, V2 ! A sin(vdt ’ 120°)  for  wire  2, and  V3 !
A sin(vdt ’ 240°)  for  wire  3. Some  types  of  industrial  equipment
(for example, motors) have three terminals and are designed to be
connected directly to these three wires. To use a more conventional
two-terminal  device  (for  example, a
lightbulb), one connects it to any two
of the three wires. Show that the po-
tential difference between any two of
the  wires  (a)  oscillates  sinusoidally
with  angular  frequency  vd and  (b)
has an amplitude of

Figure 31-38 Problem 77.

Three-wire transmission line

1
2
3

A

G

78 An electric motor connected to a 120 V, 60.0 Hz ac outlet does
mechanical work at the rate of 0.100 hp (1 hp ! 746 W). (a) If the
motor draws an rms current of 0.650 A, what is its effective resis-
tance, relative to power transfer? (b) Is this the same as the resis-
tance of the motor’s coils, as measured with an ohmmeter with the
motor disconnected from the outlet?

.
3
1

SSM

(a) In an oscillating LC circuit, in terms of the maximum
79
charge Q on  the  capacitor, what  is  the  charge  there  when  the
energy in the electric field is 50.0% of that in the magnetic field?
(b) What fraction of a period must elapse following the time the
capacitor is fully charged for this condition to occur?

80 A  series  RLC circuit  is  driven  by  an  alternating  source  at  a
frequency  of  400 Hz  and  an  emf  amplitude  of  90.0 V. The
resistance is 20.0 ", the capacitance is 12.1 mF, and the inductance
is  24.2 mH. What  is  the  rms  potential  difference  across  (a)  the
resistor, (b)  the  capacitor, and  (c)  the  inductor?  (d)  What  is
the average rate at which energy is dissipated?

SSM

In  a  certain  series  RLC circuit  being  driven  at  a
81
frequency  of  60.0 Hz, the  maximum  voltage  across  the  inductor
is 2.00  times  the  maximum  voltage  across  the  resistor  and  2.00
times the maximum voltage across the capacitor. (a) By what angle
does the current lag the generator emf? (b) If the maximum gener-
ator emf is 30.0 V, what should be the resistance of the circuit to
obtain a maximum current of 300 mA?

82 A 1.50 mH inductor in an oscillating LC circuit stores a maxi-
mum energy of 10.0 mJ. What is the maximum current?

83 A  generator  with  an  adjustable  frequency  of  oscillation  is
wired in series to an inductor of L ! 2.50 mH and a capacitor of
C ! 3.00 mF. At  what  frequency  does  the  generator  produce  the
largest possible current amplitude in the circuit?

84 A  series  RLC circuit  has  a  resonant  frequency  of  6.00 kHz.
When it is driven at 8.00 kHz, it has an impedance of 1.00 k" and a
phase constant of 45°.What are (a) R, (b) L, and (c) C for this circuit?

SSM

An LC circuit oscillates at a frequency of 10.4 kHz. (a) If
85
the capacitance is 340 mF, what is the inductance? (b) If the maxi-
mum  current  is  7.20 mA, what  is  the  total  energy  in  the  circuit?
(c) What is the maximum charge on the capacitor?

86 When under load and operating at an rms voltage of 220 V, a
certain electric motor draws an rms current of 3.00 A. It has a re-
sistance of 24.0 " and no capacitive reactance. What is its inductive
reactance?

87 The ac generator in Fig. 31-39
supplies 120 V at 60.0 Hz. With the
switch open as in the diagram, the
current leads the generator emf by
20.0°. With the switch in position 1,
the  current  lags  the  generator  emf
by 10.0°. When the switch is in posi-
tion 2, the current amplitude is 2.00
A. What are (a) R, (b) L, and (c) C?

L

C

S

1

2

C

R

Figure 31-39 Problem 87.

88 In an oscillating LC circuit, L ! 8.00 mH and C ! 1.40 mF. At
time t ! 0, the  current  is  maximum  at  12.0 mA. (a) What  is  the
maximum charge on the capacitor during the oscillations? (b) At
what earliest time t - 0 is the rate of change of energy in the capac-
itor maximum? (c) What is that maximum rate of change?

SSM

For  a  sinusoidally  driven  series  RLC circuit, show  that
89
over one complete cycle with period T (a) the energy stored in the
capacitor  does  not  change; (b)  the  energy  stored  in  the  inductor
does  not  change; (c)  the  driving  emf  device  supplies  energy
(1
(1
2T )RI2
2T )# mI cos f;
and  (d)  the  resistor  dissipates  energy
.
(e) Show that the quantities found in (c) and (d) are equal.

90 What  capacitance  would  you  connect  across  a  1.30 mH
inductor to make the resulting oscillator resonate at 3.50 kHz?

91 A  series  circuit  with  resistor – inductor – capacitor  combina-
tion R1, L1, C1 has the same resonant frequency as a second circuit
with a different combination R2, L2, C2. You now connect the two
combinations in series. Show that this new circuit has the same res-
onant frequency as the separate circuits.

92 Consider  the  circuit  shown
in  Fig. 31-40. With  switch  S1
closed and the other two switches
open, the circuit has a time con-
stant tC. With  switch  S2 closed
and the other two switches open,
the circuit has a time constant tL.
With  switch  S3 closed  and  the
other two switches open, the cir-
cuit oscillates with a period T. Show that

S1

L

S2

C

S3

R

Figure 31-40 Problem 92.

T ! 2p

tCtL.

93 When the generator emf in Sample Problem 31.07 is a maxi-
mum, what  is  the  voltage  across  (a)  the  generator, (b)  the  resis-
tance, (c) the capacitance, and (d) the inductance? (e) By summing
these with appropriate signs, verify that the loop rule is satisfied.

1
