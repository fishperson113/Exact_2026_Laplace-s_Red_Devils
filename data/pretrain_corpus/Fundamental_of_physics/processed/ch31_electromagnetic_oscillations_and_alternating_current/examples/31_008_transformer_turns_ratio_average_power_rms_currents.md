Sample Problem 31.08
Transformer: turns ratio, average power, rms currents
A transformer on a utility pole operates at Vp
8.5 kV on
the primary side and supplies electrical energy to a number
of nearby houses at Vs ! 120 V, both quantities being rms
values.Assume an ideal step-down transformer,a purely resis-
tive load,and a power factor of unity.
(a) What is the turns ratio Np/Ns of the transformer?
KEY IDEA
The turns ratio Np/Ns is related to the (given) rms primary
and secondary voltages via Eq. 31-79 (Vs ! VpNs/Np).
Calculation: We can write Eq. 31-79 as
(31-83)
(Note that the right side of this equation is the inverse of the
turns ratio.) Inverting both sides of Eq. 31-83 gives us
(Answer)
(b) The average rate of energy consumption (or dissipation) in
the houses served by the transformer is 78 kW.What are the rms
currents in the primary and secondary of the transformer?
KEY IDEA
For a purely resistive load, the power factor cos f is unity; thus,
the average rate at which energy is supplied and dissipated is
given by Eq.31-77 (Pavg ! #I ! IV).
Calculations: In the primary circuit, with Vp
8.5 kV,
!
Np
Ns
!
Vp
Vs
! 8.5 & 10 3 V
120 V
! 70.83 % 71.
Vs
Vp
! Ns
Np
.
!
Additional examples, video, and practice available at WileyPLUS
LC Energy Transfers
In an oscillating LC circuit, energy is
shuttled periodically between the electric field of the capacitor and
the magnetic field of the inductor; instantaneous values of the two
forms of energy are
(31-1, 31-2)
where q is the instantaneous charge on the capacitor and i is the
UE ! q2
2C   and  UB ! Li2
2 ,
Review & Summary
instantaneous current through the inductor. The total energy 
U (! UE $ UB) remains constant.
LC Charge and Current Oscillations
The principle of con-
servation of energy leads to
(LC oscillations)
(31-11)
L d2q
dt2 $ 1
C q ! 0

934
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
as the differential equation of LC oscillations (with no resistance).
The solution of Eq. 31-11 is
q ! Q cos(vt $ f)
(charge),
(31-12)
in which Q is the charge amplitude (maximum charge on the capac-
itor) and the angular frequency v of the oscillations is
(31-4)
The phase constant f in Eq. 31-12 is determined by the initial con-
ditions (at t ! 0) of the system.
The current i in the system at any time t is
i ! 'vQ sin(vt $ f)
(current),
(31-13)
in which vQ is the current amplitude I.
Damped Oscillations
Oscillations in an LC circuit are damped
when a dissipative element R is also present in the circuit.Then
(RLC circuit).
(31-24)
The solution of this differential equation is
q ! Qe'Rt/2L cos(v*t $ f),
(31-25)
where
(31-26)
We consider only situations with small R and thus small damping;
then v* % v.
Alternating Currents; Forced Oscillations
A series RLC
circuit may be set into forced oscillation at a driving angular fre-
quency vd by an external alternating emf
# ! #m sin vdt.
(31-28)
The current driven in the circuit is   
i ! I sin(vdt ' f),
(31-29)
where f is the phase constant of the current.
Resonance
The current amplitude I in a series RLC circuit
driven by a sinusoidal external emf is a maximum (I ! #m/R) when
the driving angular frequency vd equals the natural angular 
frequency v of the circuit (that is, at resonance). Then XC ! XL,
f ! 0, and the current is in phase with the emf.
Single Circuit Elements
The alternating potential difference
across a resistor has amplitude VR ! IR; the current is in phase
with the potential difference.
For a capacitor,VC ! IXC, in which XC ! 1/vdC is the capacitive
reactance; the current here leads the potential difference by 90°
(f ! '90° ! 'p/2 rad).
v* ! 2v2 ' (R/2L)2.
L d 2q
dt2 $ R dq
dt $ 1
C q ! 0
v !
1
1LC
.
For an inductor,VL ! IXL, in which XL ! vdL is the inductive
reactance; the current here lags the potential difference by 90°
(f ! $90° ! $p/2 rad).
Series RLC Circuits
For a series RLC circuit with an alternat-
ing external emf given by Eq. 31-28 and a resulting alternating
current given by Eq. 31-29,
(current amplitude) (31-60, 31-63)
and
(phase constant).
(31-65)
Defining the impedance Z of the circuit as
(impedance)
(31-61)
allows us to write Eq. 31-60 as I ! #m/Z.
Power
In a series RLC circuit, the average power Pavg of the
generator is equal to the production rate of thermal energy in the
resistor:
(31-71, 31-76)
Here rms stands for root-mean-square; the rms quantities are
related to the maximum quantities by 
and 
The term cos f is called the power factor of the
circuit.
Transformers
A transformer (assumed to be ideal) is an iron core
on which are wound a primary coil of Np turns and a secondary coil of
Ns turns. If the primary coil is connected across an alternating-current
generator,the primary and secondary voltages are related by
(transformation of voltage).
(31-79)
The currents through the coils are related by
(transformation of currents),
(31-80)
and the equivalent resistance of the secondary circuit, as seen by
the generator, is
(31-82)
where R is the resistive load in the secondary circuit. The ratio
Np/Ns is called the transformer’s turns ratio.
Req !#
Np
Ns $
2
R,
Is ! Ip
Np
Ns
Vs ! Vp
Ns
Np
erms ! em/12.
V/12,
Irms ! I/12, Vrms !
Pavg ! I 2
rmsR ! #rmsIrms cos f.
Z ! 2R2 $ (XL ' XC)2
tan f ! XL ' XC
R
!
#m
2R2 $ (vdL ' 1/vdC)2
I !
#m
2R2 $ (XL ' XC)2
1
Figure 31-19 shows three oscillating LC circuits with identical
inductors and capacitors. At a particular time, the charges on the
capacitor plates (and thus the electric fields between the plates)
are all at their maximum values. Rank the circuits according to the
time taken to fully discharge the capacitors during the oscillations,
greatest first.
Questions
Figure 31-19 Question 1.
(a) 
(b) 
(c)

3
A charged capacitor and an inductor are connected at time 
t ! 0. In terms of the period T of the resulting oscillations, what is
the first later time at which the following reach a maximum: (a)
UB, (b) the magnetic flux through the inductor, (c) di/dt, and (d)
the emf of the inductor?
4
What values of phase constant f in Eq. 31-12 allow situations
(a), (c), (e), and (g) of Fig. 31-1 to occur at t ! 0?
5
Curve a in Fig. 31-21 gives the
impedance Z of a driven RC circuit
versus the driving angular fre-
quency vd.The other two curves are
similar but for different values of
resistance R and capacitance C.
Rank the three curves according to
the corresponding value of R, great-
est first.
6
Charges on the capacitors in
three oscillating LC circuits vary as:
(1) q ! 2 cos 4t, (2) q ! 4 cos t, (3) q ! 3 cos 4t (with q in coulombs
and t in seconds). Rank the circuits according to (a) the current
amplitude and (b) the period, greatest first.
7
An alternating emf source with a
certain emf amplitude is connected,
in turn, to a resistor, a capacitor, and
then an inductor. Once connected to
one of the devices, the driving fre-
quency fd is varied and the ampli-
tude
I
of the resulting current
through the device is measured and
plotted. Which of the three plots in
Fig. 31-22 corresponds to which of the three devices?
935
PROBLEMS
8
The values of the phase constant f for four sinusoidally driven
series RLC circuits are (1) '15°, (2) $35°, (3) p/3 rad, and
(4) 'p/6 rad. (a) In which is the load primarily capacitive? (b) In
which does the current lag the alternating emf?
9
Figure 31-23 shows the current i
and driving emf # for a series RLC
circuit. (a) Is the phase constant posi-
tive or negative? (b) To increase the
rate at which energy is transferred
to the resistive load, should L be in-
creased or decreased? (c) Should, in-
stead, C be increased or decreased?
10
Figure 31-24 shows three situations like those of Fig. 31-15. Is
the driving angular frequency greater than, less than, or equal to
the resonant angular frequency of the circuit in (a) situation 1, (b)
situation 2, and (c) situation 3?
2
Figure 31-20 shows graphs of capacitor voltage vC for LC
circuits 1 and 2, which contain identical capacitances and have the
same maximum charge Q. Are (a) the inductance L and (b) the
maximum current I in circuit 1 greater than, less than, or the same
as those in circuit 2?
Figure 31-20 Question 2.
vC
1
2
t
Figure 31-21 Question 5.
Z
ω d
c
b
a
Figure 31-22 Question 7.
I
fd
c
b
a
, i
i
t
Figure 31-23 Question 9.
Figure 31-24 Question 10.
m
m
m
I 
I 
I 
(1) 
(2) 
(3) 
11
Figure 31-25 shows the current
i and driving emf # for a series RLC
circuit. Relative to the emf curve,
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
12
Figure 31-25 shows the current i and driving emf # for a series
RLC circuit. (a) Does the current lead or lag the emf? (b) Is the
circuit’s load mainly capacitive or mainly inductive? (c) Is the an-
gular frequency vd of the emf greater than or
less than the natural angular frequency v?
13
Does the phasor diagram of Fig. 31-26 corre-
spond to an alternating emf source connected to a
resistor, a capacitor, or an inductor? (b) If the an-
gular speed of the phasors is increased, does the
length of the current phasor increase or decrease
when the scale of the diagram is maintained?
vd
V
I
Figure 31-26
Question 13.
Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign
SSM
Worked-out solution available in Student Solutions Manual      
• - •••
Number of dots indicates level of problem difficulty
Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com
WWW Worked-out solution is at
ILW
Interactive solution is at 
http://www.wiley.com/college/halliday
Problems
Module 31-1
LC Oscillations
•1
An oscillating LC circuit consists of a 75.0 mH inductor and a
3.60 mF capacitor. If the maximum charge on the capacitor is
2.90 mC, what are (a) the total energy in the circuit and (b) the
maximum current?
•2
The frequency of oscillation of a certain LC circuit is 200 kHz.At
time t ! 0, plate A of the capacitor has maximum positive charge.At
what earliest time t - 0 will (a) plate A again have maximum positive
charge, (b) the other plate of the capacitor have maximum positive
charge,and (c) the inductor have maximum magnetic field?

936
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
•3
In a certain oscillating LC circuit, the total energy is converted
from electrical energy in the capacitor to magnetic energy in the
inductor in 1.50 ms. What are (a) the period of oscillation and
(b) the frequency of oscillation? (c) How long after the magnetic
energy is a maximum will it be a maximum again?
•4
What is the capacitance of an oscillating LC circuit if the maxi-
mum charge on the capacitor is 1.60 mC and the total energy is
140 mJ?
•5
In an oscillating LC circuit, L ! 1.10 mH and C ! 4.00 mF.
The maximum charge on the capacitor is 3.00 mC. Find the maxi-
mum current.
•6
A 0.50 kg body oscillates in SHM on a spring that, when ex-
tended 2.0 mm from its equilibrium position, has an 8.0 N restoring
force.What are (a) the angular frequency of oscillation, (b) the pe-
riod of oscillation, and (c) the capacitance of an LC circuit with the
same period if L is 5.0 H?
•7
The energy in an oscillating LC circuit containing a
1.25 H inductor is 5.70 mJ.The maximum charge on the capacitor is
175 mC. For a mechanical system with the same period, find the
(a) mass, (b) spring constant, (c) maximum displacement, and
(d) maximum speed.
•8
A single loop consists of inductors (L1, L2, . . .), capacitors (C1,
C2, . . .), and resistors (R1, R2, . . .) connected in series as shown, for
example, in Fig. 31-27a. Show that regardless of the sequence of
these circuit elements in the loop, the behavior of this circuit is
identical to that of the simple LC circuit shown in Fig. 31-27b.
(Hint: Consider the loop rule and see Problem 47 in Chapter 30.)
SSM
••13
In an oscillating LC circuit, L ! 3.00 mH and C ! 2.70 mF.
At t ! 0 the charge on the capacitor is zero and the current is 2.00 A.
(a) What is the maximum charge that will appear on the capacitor?
(b) At what earliest time t - 0 is the rate at which energy is stored
in the capacitor greatest, and (c) what is that greatest rate?
••14
To construct an oscillating LC system, you can choose from
a 10 mH inductor, a 5.0 mF capacitor, and a 2.0 mF capacitor.What
are the (a) smallest, (b) second smallest, (c) second largest, and (d)
largest oscillation frequency that can be set up by these elements in
various combinations?
••15
An oscillating LC circuit consisting of a 1.0 nF capacitor
and a 3.0 mH coil has a maximum voltage of 3.0 V.What are (a) the
maximum charge on the capacitor, (b) the maximum current
through the circuit, and (c) the maximum energy stored in the
magnetic field of the coil?
••16
An inductor is connected across a capacitor whose
capacitance can be varied by turning a knob. We wish to make the
frequency of oscillation of this LC circuit vary linearly with the an-
gle of rotation of the knob, going from 2 & 105 to 4 & 105 Hz as the
knob turns through 180°. If L ! 1.0 mH, plot the required capaci-
tance C as a function of the angle of rotation of the knob.
••17
In Fig. 31-28, R ! 14.0
, C
6.20 mF, and L
54.0 mH,
and the ideal battery has emf # !
34.0 V. The switch is kept at a for a
long time and then thrown to posi-
tion b. What are the (a) frequency
and (b) current amplitude of the
resulting oscillations?
••18
An oscillating LC circuit has a
current amplitude of 7.50 mA, a potential amplitude of 250 mV,
and a capacitance of 220 nF.What are (a) the period of oscillation,
(b) the maximum energy stored in the capacitor, (c) the maximum
energy stored in the inductor, (d) the maximum rate at which the
current changes, and (e) the maximum rate at which the inductor
gains energy?
••19
Using the loop rule, derive the differential equation for an
LC circuit (Eq. 31-11).
••20
In an oscillating LC circuit in which C ! 4.00 mF, the
maximum potential difference across the capacitor during the
oscillations is 1.50 V and the maximum current through the inductor
is 50.0 mA. What are (a) the inductance L and (b) the frequency of
the oscillations? (c) How much time is required for the charge on
the capacitor to rise from zero to its maximum value?
••21
In an oscillating LC circuit with C ! 64.0 mF, the current
is given by i
(1.60) sin(2500t
0.680), where t is in seconds, i in
amperes, and the phase constant in radians. (a) How soon after t ! 0
will the current reach its maximum value? What are (b) the induc-
tance L and (c) the total energy?
••22
A series circuit containing inductance L1 and capacitance
C1 oscillates at angular frequency v. A second series circuit, con-
taining inductance L2 and capacitance C2, oscillates at the same
angular frequency. In terms of v, what is the angular frequency of
oscillation of a series circuit containing all four of these elements?
Neglect resistance. (Hint: Use the formulas for equivalent capaci-
tance and equivalent inductance; see Module 25-3 and Problem 47
in Chapter 30.)
$
!
ILW
!
!
"
ILW
ILW
Figure 31-27 Problem 8.
L
C
R
(b)
(a)
L 2
C 1
L 1
C 2
R 2
R 1
•9
In an oscillating LC circuit with L ! 50 mH and C !
4.0 mF, the current is initially a maximum. How long will it take
before the capacitor is fully charged for the first time?
•10
LC oscillators have been used in circuits connected to loud-
speakers to create some of the sounds of electronic music. What
inductance must be used with a 6.7 mF capacitor to produce a fre-
quency of 10 kHz, which is near the middle of the audible range of
frequencies?
••11
A variable capacitor with a range from 10 to
365 pF is used with a coil to form a variable-frequency LC circuit
to tune the input to a radio. (a) What is the ratio of maximum fre-
quency to minimum frequency that can be obtained with such a
capacitor? If this circuit is to obtain frequencies from 0.54 MHz
to 1.60 MHz, the ratio computed in (a) is too large. By adding a
capacitor in parallel to the variable capacitor, this range can be
adjusted. To obtain the desired frequency range, (b) what capaci-
tance should be added and (c) what inductance should the coil
have?
••12
In an oscillating LC circuit, when 75.0% of the total energy
is stored in the inductor’s magnetic field, (a) what multiple of the
maximum charge is on the capacitor and (b) what multiple of the
maximum current is in the inductor?
WWW
SSM
ILW
Figure 31-28 Problem 17.
a
C
R
L
b

937
PROBLEMS
the value of the capacitance, inductance, or resistance, as the case
may be?
••34
An ac generator with emf # ! #m sin vdt, where #m !
25.0 V and vd
377 rad/s, is connected to a 4.15 mF capacitor.
(a) What is the maximum value of the current? (b) When the cur-
rent is a maximum, what is the emf of the generator? (c) When the
emf of the generator is '12.5 V and increasing in magnitude, what
is the current?
Module 31-4
The Series RLC Circuit
•35
A coil of inductance 88 mH and unknown resistance and
a 0.94 mF capacitor are connected in series with an alternating emf
of frequency 930 Hz. If the phase constant between the applied
voltage and the current is 75°, what is the resistance of the coil?
•36
An alternating source with a variable frequency, a capacitor
with capacitance C, and a resistor with resistance R are connected
in series. Figure 31-29 gives the impedance Z of the circuit versus
the driving angular frequency vd; the curve reaches an asymptote
of 500 ", and the horizontal scale is set by vds ! 300 rad/s.The fig-
ure also gives the reactance XC for the capacitor versus vd. What
are (a) R and (b) C?
ILW
!
••23
In an oscillating LC circuit, L ! 25.0 mH and C !
7.80 mF. At time t
0 the current is 9.20 mA, the charge on the
capacitor is 3.80 mC, and the capacitor is charging.What are (a) the
total energy in the circuit, (b) the maximum charge on the capaci-
tor, and (c) the maximum current? (d) If the charge on the capaci-
tor is given by q ! Q cos(vt $ f), what is the phase angle f?
(e) Suppose the data are the same, except that the capacitor is
discharging at t ! 0.What then is f?
Module 31-2
Damped Oscillations in an RLC Circuit
••24
A single-loop circuit consists of a 7.20 " resistor, a 12.0 H
inductor, and a 3.20 mF capacitor. Initially the capacitor has a
charge of 6.20 mC and the current is zero. Calculate the charge on
the capacitor N complete cycles later for (a) N ! 5, (b) N ! 10, and
(c) N ! 100.
••25
What resistance R should be connected in series with an
inductance L
220 mH and capacitance C
12.0 mF for the
maximum charge on the capacitor to decay to 99.0% of its initial
value in 50.0 cycles? (Assume v* % v.)
••26
In an oscillating series RLC circuit, find the time required
for the maximum energy present in the capacitor during an oscilla-
tion to fall to half its initial value.Assume q ! Q at t ! 0.
•••27
In an oscillating series RLC circuit, show that )U/U,
the fraction of the energy lost per cycle of oscillation, is given to a
close approximation by 2pR/vL.The quantity vL/R is often called
the Q of the circuit (for quality). A high-Q circuit has low resis-
tance and a low fractional energy loss (! 2p/Q) per cycle.
Module 31-3
Forced Oscillations of Three Simple Circuits
•28
A 1.50 mF capacitor is connected as in Fig. 31-10 to an ac gen-
erator with #m ! 30.0 V. What is the amplitude of the resulting
alternating current if the frequency of the emf is (a) 1.00 kHz and
(b) 8.00 kHz?
•29
A 50.0 mH inductor is connected as in Fig. 31-12 to an ac
generator with 
30.0 V.What is the amplitude of the resulting
alternating current if the frequency of the emf is (a) 1.00 kHz and
(b) 8.00 kHz?
•30
A 50.0 " resistor is connected as in Fig. 31-8 to an ac genera-
tor with 
30.0 V. What is the amplitude of the resulting alter-
nating current if the frequency of the emf is (a) 1.00 kHz and
(b) 8.00 kHz?
•31
(a) At what frequency would a 6.0 mH inductor and a 10 mF
capacitor have the same reactance? (b) What would the reactance
be? (c) Show that this frequency would be the natural frequency of
an oscillating circuit with the same L and C.
••32
An ac generator has emf # ! #m sin vdt, with #m ! 25.0 V
and 
377 rad/s. It is connected to a 12.7 H inductor. (a) What is
the maximum value of the current? (b) When the current is a maxi-
mum, what is the emf of the generator? (c) When the emf of
the generator is '12.5 V and increasing in magnitude, what is the
current?
••33
An ac generator has emf # ! #m sin(vdt ' p/4), where
30.0 V and 
350 rad/s. The current produced in a con-
nected circuit is i(t)
I sin(
t
3p/4), where I
620 mA. At
what time after t
0 does (a) the generator emf first reach a
maximum and (b) the current first reach a maximum? (c) The cir-
cuit contains a single element other than the generator. Is it a ca-
pacitor, an inductor, or a resistor? Justify your answer. (d) What is
!
!
'
0d
!
0d !
#m !
SSM
0d !
#m !
#m !
ILW
SSM
!
!
ILW
!
Z, XC (Ω)
400
0
d (rad/s) 
800
XC
Z
ω d (rad/s) 
ω 
ds
ω 
Figure 31-29 Problem 36.
•37
An electric motor has an effective resistance of 32.0 " and an
inductive reactance of 45.0 " when working under load. The
voltage amplitude across the alternating source is 420 V. Calculate
the current amplitude.
•38
The current amplitude I versus
driving angular frequency vd for a
driven RLC circuit is given in Fig.
31-30, where the vertical axis scale is
set by Is ! 4.00 A. The inductance
is 200 mH, and the emf amplitude is
8.0 V.What are (a) C and (b) R?
•39
Remove the inductor from
the circuit in Fig. 31-7 and set R !
200 ", C ! 15.0 mF, fd ! 60.0 Hz, and #m ! 36.0 V. What are (a) Z,
(b) f, and (c) I? (d) Draw a phasor diagram.
•40
An alternating source drives a series RLC circuit with an emf
amplitude of 6.00 V, at a phase angle of $30.0°.When the potential
difference across the capacitor reaches its maximum positive value
of 
5.00 V, what is the potential difference across the inductor
(sign included)?
•41
In Fig. 31-7, set R ! 200 ", C ! 70.0 mF, L ! 230 mH,
fd
60.0 Hz, and 
36.0 V. What are (a) Z, (b) f, and (c) I?
(d) Draw a phasor diagram.
•42
An alternating source with a variable frequency, an inductor
#m !
!
SSM
$
I (A) 
Is
010 
30 
d (1000 rad/s) 
50
d (1000 rad/s) 
ω 
Figure 31-30 Problem 38.

938
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
••49
In Fig. 31-33, a genera-
tor with an adjustable frequency
of oscillation is connected to re-
sistance R
100 
, inductances
L1 ! 1.70 mH and L2 ! 2.30
mH, and capacitances C1 ! 4.00
mF, C2 ! 2.50 mF, and C3 ! 3.50
mF. (a) What is the resonant fre-
quency of the circuit? (Hint: See Problem 47 in Chapter 30.) What
happens to the resonant frequency if (b) R is increased, (c) L1 is in-
creased, and (d) C3 is removed from the circuit?
••50 An alternating emf source with a variable frequency fd is con-
nected in series with an 80.0 " resistor and a 40.0 mH inductor.The
emf amplitude is 6.00 V. (a) Draw a phasor diagram for phasor VR
(the potential across the resistor) and phasor VL (the potential
across the inductor). (b) At what driving frequency fd do the two
phasors have the same length? At that driving frequency, what are
(c) the phase angle in degrees, (d) the angular speed at which the
phasors rotate, and (e) the current amplitude?
••51
The fractional half-width )vd of a resonance curve,
such as the ones in Fig. 31-16, is the width of the curve at half the
maximum value of I. Show that )vd/v ! R(3C/L)1/2, where v is the
angular frequency at resonance. Note that the ratio )vd/v in-
creases with R, as Fig. 31-16 shows.
Module 31-5
Power in Alternating-Current Circuits
•52
An ac voltmeter with large impedance is connected in turn
across the inductor, the capacitor, and the resistor in a series circuit
having an alternating emf of 100 V (rms); the meter gives the same
reading in volts in each case.What is this reading?
•53
An air conditioner connected to a 120 V rms ac line is
equivalent to a 12.0 
resistance and a 1.30 
inductive reactance
in series. Calculate (a) the impedance of the air conditioner and
(b) the average rate at which energy is supplied to the appliance.
•54
What is the maximum value of an ac voltage whose rms value
is 100 V?
•55
What direct current will produce the same amount of ther-
mal energy, in a particular resistor, as an alternating current that
has a maximum value of 2.60 A?
••56
A typical light dimmer used to
dim the stage lights in a theater con-
sists of a variable inductor L (whose
inductance is adjustable between
zero and Lmax) connected in series
with a lightbulb B, as shown in
Fig. 31-34. The electrical supply is
120 V (rms) at 60.0 Hz; the lightbulb is rated at 120 V, 1000 W.
(a) What Lmax is required if the rate of energy dissipation in
the lightbulb is to be varied by a factor of 5 from its upper limit of
1000 W? Assume that the resistance of the lightbulb is indepen-
dent of its temperature. (b) Could one use a variable resistor
(adjustable between zero and Rmax) instead of an inductor? (c) If
so, what Rmax is required? (d) Why isn’t this done?
••57
In an RLC circuit such as that of Fig. 31-7 assume that R !
5.00 ", L ! 60.0 mH, fd ! 60.0 Hz, and #m ! 30.0 V. For what val-
ues of the capacitance would the average rate at which energy is
dissipated in the resistance be (a) a maximum and (b) a minimum?
What are (c) the maximum dissipation rate and the corresponding
"
"
SSM
SSM
"
!
with inductance L, and a resistor
with resistance R are connected in
series. Figure 31-31 gives the imped-
ance Z of the circuit versus the driv-
ing angular frequency vd, with the
horizontal axis scale set by vds !
1600 rad/s. The figure also gives the
reactance XL for the inductor versus
vd.What are (a) R and (b) L?
•43
Remove the capacitor from
the circuit in Fig. 31-7 and set R !
200 ", L ! 230 mH, fd ! 60.0 Hz, and #m ! 36.0 V.What are (a) Z,
(b) f, and (c) I? (d) Draw a phasor diagram.
••44
An ac generator with emf amplitude #m ! 220 V and op-
erating at frequency 400 Hz causes oscillations in a series RLC cir-
cuit having R
220 ", L ! 150 mH, and C ! 24.0 mF. Find (a) the
capacitive reactance XC, (b) the impedance Z, and (c) the current
amplitude I. A second capacitor of the same capacitance is then
connected in series with the other components. Determine
whether the values of (d) XC, (e) Z, and (f) I increase, decrease, or
remain the same.
••45
(a) In an RLC circuit, can the amplitude of the volt-
age across an inductor be greater than the amplitude of the gener-
ator emf? (b) Consider an RLC circuit with emf amplitude #m !
10 V, resistance R ! 10 ", inductance L ! 1.0 H, and capacitance
C ! 1.0 mF. Find the amplitude of the voltage across the inductor
at resonance.
••46
An alternating emf source with a variable frequency fd is
connected in series with a 50.0 
resistor and a 20.0 mF capacitor.
The emf amplitude is 12.0 V. (a) Draw a phasor diagram for phasor
VR (the potential across the resistor) and phasor VC (the potential
across the capacitor). (b) At what driving frequency fd do the two
phasors have the same length? At that driving frequency, what are
(c) the phase angle in degrees, (d) the angular speed at which the
phasors rotate, and (e) the current amplitude?
••47
An RLC circuit such as that of Fig. 31-7 has 
R
5.00
, C
20.0 mF, L
1.00 H, and 
30.0 V. (a) At
what angular frequency vd will the current amplitude have its max-
imum value, as in the resonance curves of Fig. 31-16? (b) What is
this maximum value? At what (c) lower angular frequency vd1 and
(d) higher angular frequency vd2 will the current amplitude be half
this maximum value? (e) For the resonance curve for this circuit,
what is the fractional half-width (vd1 ' vd2)/v?
••48
Figure 31-32 shows a driven RLC circuit that contains two
identical capacitors and two switches. The emf amplitude is set at
12.0 V, and the driving frequency is set at 60.0 Hz. With both
switches open, the current leads the emf by 30.9°. With switch S1
closed and switch S2 still open, the emf leads the current by 15.0°.
With both switches closed, the current amplitude is 447 mA. What
are (a) R, (b) C, and (c) L?
#m !
!
!
"
!
WWW
SSM
"
ILW
!
ds
ω 
Z, XL (Ω)
120
80
40
0
d (rad/s) 
ω 
Z
XL
Figure 31-31 Problem 42.
Figure 31-32 Problem 48.
S2
S1
R
C
C
L
Figure 31-33 Problem 49.
G
C 1
C 2
C 3
L 1
R
L 2
To energy 
supply
L
B
Figure 31-34 Problem 56.

75.0 V and frequency 550 Hz. (a) What is the rms current? What is
the rms voltage across (b) R, (c) C, (d) L, (e) C and L together, and
(f) R, C, and L together? At what average rate is energy dissipated
by (g) R, (h) C, and (i) L?
••60
In a series oscillating RLC circuit, R
16.0 ", C 5
31.2
F, L
9.20 mH, and 
sin vdt with 
45.0 V and 
3000 rad/s. For time t
0.442 ms find (a) the rate Pg
at which energy is being supplied by the generator, (b) the rate PC
at which the energy in the capacitor is changing, (c) the rate PL at
which the energy in the inductor is changing, and (d) the rate PR at
which energy is being dissipated in the resistor. (e) Is the sum
of PC, PL, and PR greater than, less than, or equal to Pg?
••61
Figure 31-36
shows an ac generator connected to a
“black box” through a pair of termi-
nals. The box contains an RLC cir-
cuit, possibly even a multiloop cir-
cuit, whose elements and connections
we do not know. Measurements out-
side the box reveal that
#(t) ! (75.0 V) sin vdt
and
i(t) ! (1.20 A) sin(vdt $ 42.0°).
(a) What is the power factor? (b) Does the current lead or lag the
emf? (c) Is the circuit in the box largely inductive or largely
capacitive? (d) Is the circuit in the box in resonance? (e) Must
there be a capacitor in the box? (f) An inductor? (g) A resistor?
(h) At what average rate is energy delivered to the box by the
generator? (i) Why don’t you need to know vd to answer all these
questions?
Module 31-6
Transformers
•62
A generator supplies 100 V to a transformer’s primary coil,
which has 50 turns. If the secondary coil has 500 turns, what is the
secondary voltage?
•63
A transformer has 500 primary turns and 10 sec-
ondary turns. (a) If Vp is 120 V (rms), what is Vs with an open
circuit? If the secondary now has a resistive
load of 15 ", what is the current in the (b)
primary and (c) secondary?
•64
Figure 31-37 shows an “autotrans-
former.” It consists of a single coil (with an
iron core). Three taps Ti are provided.
Between taps T1 and T2 there are 200 turns,
and between taps T2 and T3 there are 800
turns.Any two taps can be chosen as the pri-
mary terminals, and any two taps can be
chosen as the secondary terminals. For
ILW
SSM
WWW
SSM
!
vd !
#m !
#m ! #m
!
1
!
939
PROBLEMS
choices producing a step-up transformer, what are the (a) smallest,
(b) second smallest, and (c) largest values of the ratio Vs/Vp? For
a step-down transformer, what are the (d) smallest, (e) second
smallest, and (f) largest values of Vs/Vp?
••65
An ac generator provides emf to a resistive load in a remote
factory over a two-cable transmission line. At the factory a step-
down transformer reduces the voltage from its (rms) transmission
value Vt to a much lower value that is safe and convenient for use
in the factory. The transmission line resistance is 0.30 "/cable, and
the power of the generator is 250 kW. If Vt ! 80 kV, what are
(a) the voltage decrease )V along the transmission line and (b) the
rate Pd at which energy is dissipated in the line as thermal energy?
If Vt ! 8.0 kV, what are (c) )V and (d) Pd? If Vt ! 0.80 kV, what
are (e) )V and (f) Pd?
Additional Problems
66
In Fig. 31-35, let the rectangular box on the left represent the
(high-impedance) output of an audio amplifier, with r ! 1000 ".
Let R ! 10 " represent the (low-impedance) coil of a loud-
speaker. For maximum transfer of energy to the load R we must
have R ! r, and that is not true in this case. However, a trans-
former can be used to “transform” resistances, making them be-
have electrically as if they were larger or smaller than they actu-
ally are. (a) Sketch the primary and secondary coils of a
transformer that can be introduced between the amplifier and
the speaker in Fig. 31-35 to match the impedances. (b) What must
be the turns ratio?
67
An ac generator produces emf # ! #m sin(vdt ' p/4),
where
m
30.0 V and vd
350 rad/s. The current in the circuit
attached to the generator is i(t) ! I sin(vdt $ p/4), where I !
620 mA. (a) At what time after t ! 0 does the generator emf first
reach a maximum? (b) At what time after t ! 0 does the current
first reach a maximum? (c) The circuit contains a single element
other than the generator. Is it a capacitor, an inductor, or a resis-
tor? Justify your answer. (d) What is the value of the capacitance,
inductance, or resistance, as the case may be?
68
A series RLC circuit is driven by a generator at a frequency
of 2000 Hz and an emf amplitude of 170 V. The inductance is
60.0 mH, the capacitance is 0.400 mF, and the resistance is 200 ".
(a) What is the phase constant in radians? (b) What is the current
amplitude?
69
A generator of frequency 3000 Hz drives a series RLC circuit
with an emf amplitude of 120 V.The resistance is 40.0 ", the capac-
itance is 1.60 mF, and the inductance is 850 mH. What are (a) the
phase constant in radians and (b) the current amplitude? (c) Is the
circuit capacitive, inductive, or in resonance?
70
A 45.0 mH inductor has a reactance of 1.30 k". (a) What is its
operating frequency? (b) What is the capacitance of a capacitor with
the same reactance at that frequency? If the frequency is doubled,
what is the new reactance of (c) the inductor and (d) the capacitor?
71
An RLC circuit is driven by a generator with an emf
amplitude of 80.0 V and a current amplitude of 1.25 A. The
current leads the emf by 0.650 rad. What are the (a) impedance
and (b) resistance of the circuit? (c) Is the circuit inductive, capaci-
tive, or in resonance?
72
A series RLC circuit is driven in such a way that the maxi-
mum voltage across the inductor is 1.50 times the maximum volt-
age across the capacitor and 2.00 times the maximum voltage
across the resistor. (a) What is f for the circuit? (b) Is the circuit
!
!
#
(d) phase angle and (e) power factor? What are (f) the minimum
dissipation rate and the corresponding (g) phase angle and
(h) power factor?
r
R
Figure 31-35 Problems 58 
and 66.
(t)
i(t)
?
Figure 31-36 Problem 61.
••58
For Fig. 31-35, show that the av-
erage rate at which energy is dissipated
in resistance R is a maximum when R is
equal to the internal resistance r of the
ac generator. (In the text discussion we
tacitly assumed that r ! 0.)
••59
In Fig. 31-7, R ! 15.0 ", C !
4.70 mF, and L ! 25.0 mH. The gener-
ator provides an emf with rms voltage
T3
T2
T1
Figure 31-37
Problem 64.

940
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
82
A 1.50 mH inductor in an oscillating LC circuit stores a maxi-
mum energy of 10.0 mJ.What is the maximum current?
83
A generator with an adjustable frequency of oscillation is
wired in series to an inductor of L ! 2.50 mH and a capacitor of 
C ! 3.00 mF. At what frequency does the generator produce the
largest possible current amplitude in the circuit?
84
A series RLC circuit has a resonant frequency of 6.00 kHz.
When it is driven at 8.00 kHz, it has an impedance of 1.00 k" and a
phase constant of 45°.What are (a) R,(b) L,and (c) C for this circuit?
85
An LC circuit oscillates at a frequency of 10.4 kHz. (a) If
the capacitance is 340 mF, what is the inductance? (b) If the maxi-
mum current is 7.20 mA, what is the total energy in the circuit?
(c) What is the maximum charge on the capacitor?
86
When under load and operating at an rms voltage of 220 V, a
certain electric motor draws an rms current of 3.00 A. It has a re-
sistance of 24.0 " and no capacitive reactance.What is its inductive
reactance?
87
The ac generator in Fig. 31-39
supplies 120 V at 60.0 Hz.With the
switch open as in the diagram, the
current leads the generator emf by
20.0°. With the switch in position 1,
the current lags the generator emf
by 10.0°.When the switch is in posi-
tion 2, the current amplitude is 2.00
A.What are (a) R, (b) L, and (c) C?
88
In an oscillating LC circuit, L ! 8.00 mH and C ! 1.40 mF.At
time t ! 0, the current is maximum at 12.0 mA. (a) What is the
maximum charge on the capacitor during the oscillations? (b) At
what earliest time t - 0 is the rate of change of energy in the capac-
itor maximum? (c) What is that maximum rate of change?
89
For a sinusoidally driven series RLC circuit, show that
over one complete cycle with period T (a) the energy stored in the
capacitor does not change; (b) the energy stored in the inductor
does not change; (c) the driving emf device supplies energy
and (d) the resistor dissipates energy 
.
(e) Show that the quantities found in (c) and (d) are equal.
90
What capacitance would you connect across a 1.30 mH
inductor to make the resulting oscillator resonate at 3.50 kHz?
91
A series circuit with resistor-inductor-capacitor combina-
tion R1, L1, C1 has the same resonant frequency as a second circuit
with a different combination R2, L2, C2. You now connect the two
combinations in series. Show that this new circuit has the same res-
onant frequency as the separate circuits.
92
Consider the circuit shown
in Fig. 31-40. With switch S1
closed and the other two switches
open, the circuit has a time con-
stant tC. With switch S2 closed
and the other two switches open,
the circuit has a time constant tL.
With switch S3 closed and the
other two switches open, the cir-
cuit oscillates with a period T.Show that 
93
When the generator emf in Sample Problem 31.07 is a maxi-
mum, what is the voltage across (a) the generator, (b) the resis-
tance, (c) the capacitance, and (d) the inductance? (e) By summing
these with appropriate signs, verify that the loop rule is satisfied.
T ! 2p 1tCtL.
(1
2T)RI2
(1
2T)# mI cos f;
SSM
SSM
inductive, capacitive, or in resonance? The resistance is 49.9 ",
and the current amplitude is 200 mA. (c) What is the amplitude
of the driving emf?
73
A capacitor of capacitance 158 mF and an inductor form an
LC circuit that oscillates at 8.15 kHz, with a current amplitude of
4.21 mA. What are (a) the inductance, (b) the total energy in the
circuit, and (c) the maximum charge on the capacitor?
74
An oscillating LC circuit has an inductance of 3.00 mH and a
capacitance of 10.0 mF. Calculate the (a) angular frequency and
(b) period of the oscillation. (c) At time t ! 0, the capacitor is
charged to 200 mC and the current is zero. Roughly sketch the
charge on the capacitor as a function of time.
75
For a certain driven series RLC circuit, the maximum genera-
tor emf is 125 V and the maximum current is 3.20 A. If the current
leads the generator emf by 0.982 rad, what are the (a) impedance
and (b) resistance of the circuit? (c) Is the circuit predominantly
capacitive or inductive?
76
A 1.50 mF capacitor has a capacitive reactance of 12.0 ".
(a) What must be its operating frequency? (b) What will be the
capacitive reactance if the frequency is doubled?
77
In Fig. 31-38, a three-phase generator G produces electri-
cal power that is transmitted by means of three wires. The electric
potentials (each relative to a common reference level) are V1 !
A sin vdt for wire 1, V2 ! A sin(vdt ' 120°) for wire 2, and V3 !
A sin(vdt ' 240°) for wire 3. Some types of industrial equipment
(for example, motors) have three terminals and are designed to be
connected directly to these three wires.To use a more conventional
two-terminal device (for example, a
lightbulb), one connects it to any two
of the three wires. Show that the po-
tential difference between any two of
the wires (a) oscillates sinusoidally
with angular frequency vd and (b)
has an amplitude of
.
78
An electric motor connected to a 120 V, 60.0 Hz ac outlet does
mechanical work at the rate of 0.100 hp (1 hp ! 746 W). (a) If the
motor draws an rms current of 0.650 A, what is its effective resis-
tance, relative to power transfer? (b) Is this the same as the resis-
tance of the motor’s coils, as measured with an ohmmeter with the
motor disconnected from the outlet?
79
(a) In an oscillating LC circuit, in terms of the maximum
charge Q on the capacitor, what is the charge there when the
energy in the electric field is 50.0% of that in the magnetic field?
(b) What fraction of a period must elapse following the time the
capacitor is fully charged for this condition to occur? 
80
A series RLC circuit is driven by an alternating source at a
frequency of 400 Hz and an emf amplitude of 90.0 V. The
resistance is 20.0 ", the capacitance is 12.1 mF, and the inductance
is 24.2 mH. What is the rms potential difference across (a) the
resistor, (b) the capacitor, and (c) the inductor? (d) What is 
the average rate at which energy is dissipated?
81
In a certain series RLC circuit being driven at a
frequency of 60.0 Hz, the maximum voltage across the inductor
is 2.00 times the maximum voltage across the resistor and 2.00
times the maximum voltage across the capacitor. (a) By what angle
does the current lag the generator emf? (b) If the maximum gener-
ator emf is 30.0 V, what should be the resistance of the circuit to
obtain a maximum current of 300 mA?
SSM
SSM
A13
SSM
G
1
2
3
Three-wire transmission line 
Figure 31-38 Problem 77.
Figure 31-39 Problem 87.
C
S
1
2
C
R
L
S1
S2
S3
L
C
R
Figure 31-40 Problem 92.
