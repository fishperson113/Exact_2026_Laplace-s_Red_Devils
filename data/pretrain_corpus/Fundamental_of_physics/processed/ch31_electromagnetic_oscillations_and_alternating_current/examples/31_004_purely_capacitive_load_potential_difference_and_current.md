Sample Problem 31.04
Purely capacitive load: potential difference and current 
In Fig. 31-10, capacitance C is 15.0 mF and the sinusoidal 
alternating emf device operates at amplitude #m ! 36.0 V
and frequency fd ! 60.0 Hz.
(a) What are the potential difference vC(t) across the 
capacitance and the amplitude VC of vC(t)?
KEY IDEA
In a circuit with a purely capacitive load, the potential dif-
ference vC(t) across the capacitance is always equal to the
potential difference #(t) across the emf device.
Calculations: Here we have vC(t) ! #(t) and VC ! #m.
Since #m is given, we have
VC ! #m ! 36.0 V.
(Answer)
To find vC(t), we use Eq. 31-28 to write
vC(t) ! #(t) ! #m sin vdt.
(31-43)
Then, substituting #m ! 36.0 V and vd ! 2pfd ! 120p into
Eq. 31-43, we have
vC ! (36.0 V) sin(120pt).
(Answer)
(b) What are the current iC(t) in the circuit as a function of
time and the amplitude IC of iC(t)?
Additional examples, video, and practice available at WileyPLUS
iL vL
L
Figure 31-12 An inductor is connected across
an alternating-current generator.
This relation between iC and vC is illustrated by the phasor diagram of
Fig. 31-11b.As the phasors representing these two quantities rotate counterclock-
wise together, the phasor labeled IC does indeed lead that labeled VC, and by an
angle of 90°; that is, the phasor IC coincides with the vertical axis one-quarter
cycle before the phasor VC does. Be sure to convince yourself that the phasor
diagram of Fig. 31-11b is consistent with Eqs. 31-36 and 31-40.
Checkpoint 4
The figure shows, in (a), a sine curve S(t) ! sin(vdt) and three
other sinusoidal curves A(t), B(t), and C(t), each of the form
sin(vdt ' f). (a) Rank the three other curves according to the
value of f, most positive first and most negative last. (b) Which
curve corresponds to which phasor in (b) of the figure? (c)
Which curve leads the others?
t
A
B
S
C
(a)
1
2
3
4
(b)

919
31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS
vL, iL
T
iL
vL
0
Instants
represented in (b)
(a)
t
VL
IL
T/2
= +90° = +   /2 rad 
φ 
π 
For an inductive load,
the current lags the
potential difference
by 90º.
iL
vL
VL
IL
  ω
Rotation of
phasors at
rate
d
dt
ω
“Lags” means that the
current peaks at a
later time than the
potential difference.
(b)
Figure 31-13 (a) The current in the inductor
lags the voltage by 90° (! p/2 rad). (b) A
phasor diagram shows the same thing.
where VL is the amplitude of vL. From Eq. 30-35 (#L ! 'L di/dt), we can write
the potential difference across an inductance L in which the current is changing
at the rate diL/dt as
(31-46)
If we combine Eqs. 31-45 and 31-46, we have
(31-47)
Our concern, however, is with the current, so we integrate:
(31-48)
We now modify this equation in two ways. First, for reasons of symmetry of
notation, we introduce the quantity XL, called the inductive reactance of an
inductor, which is defined as
XL ! vdL
(inductive reactance).
(31-49)
The value of XL depends on the driving angular frequency vd. The unit of the
inductive time constant tL indicates that the SI unit of XL is the ohm, just as it is
for XC and for R.
Second, we replace 'cos vdt in Eq. 31-48 with a phase-shifted sine:
'cos vdt ! sin(vdt ' 90°).
You can verify this identity by shifting a sine curve 90° in the positive direction.
With these two changes, Eq. 31-48 becomes
(31-50)
From Eq. 31-29, we can also write this current in the inductance as
iL ! IL sin(vdt ' f),
(31-51)
where IL is the amplitude of the current iL. Comparing Eqs. 31-50 and 31-51, we
see that for a purely inductive load the phase constant f for the current is $90°.
We also see that the voltage amplitude and current amplitude are related by
VL ! ILXL
(inductor).
(31-52)
Although we found this relation for the circuit of Fig. 31-12, it applies to any
inductance in any ac circuit.
Comparison of Eqs. 31-45 and 31-50, or inspection of Fig. 31-13a, shows
that the quantities iL and vL are 90° out of phase. In this case, however, iL lags
vL; that is, monitoring the current iL and the potential difference vL in the cir-
cuit of Fig. 31-12 shows that iL reaches its maximum value after vL does, by
one-quarter cycle. The phasor diagram of Fig. 31-13b also contains this informa-
tion. As the phasors rotate counterclockwise in the figure, the phasor labeled IL
does indeed lag that labeled VL, and by an angle of 90°. Be sure to convince your-
self that Fig. 31-13b represents Eqs. 31-45 and 31-50.
iL !#
VL
XL$ sin(vdt ' 90+).
iL !" diL ! VL
L " sin vdt dt ! '#
VL
vdL $ cos vdt.
diL
dt ! VL
L  sin vdt.
vL ! L diL
dt .
Checkpoint 5
If we increase the driving frequency in a circuit with a purely capacitive load, do
(a) amplitude VC and (b) amplitude IC increase, decrease, or remain the same? If,
instead, the circuit has a purely inductive load, do (c) amplitude VL and (d) amplitude
IL increase, decrease, or remain the same?

920
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
(for inductor), and in it the letter I (for current) comes after
the letter E (for emf or voltage). Thus, for an inductor, the
current lags (comes after) the voltage. Similarly, ICE (which
contains a C for capacitor) means that the current leads
(comes before) the voltage.You might also use the modified
mnemonic “ELI positively is the ICE man” to remember
that the phase constant f is positive for an inductor.
If you have difficulty in remembering whether XC is
equal to vdC (wrong) or 1/vdC (right), try remembering that
C is in the “cellar”-that is, in the denominator.
Problem-Solving Tactics
Leading and Lagging in AC Circuits: Table 31-2 summa-
rizes the relations between the current i and the voltage v
for each of the three kinds of circuit elements we have con-
sidered. When an applied alternating voltage produces an
alternating current in these elements, the current is always
in phase with the voltage across a resistor, always leads the
voltage across a capacitor, and always lags the voltage
across an inductor.
Many students remember these results with the
mnemonic “ELI the ICE man.” ELI contains the letter L
Table 31-2 Phase and Amplitude Relations for Alternating Currents and Voltages
Circuit 
Resistance 
Phase of 
Phase Constant 
Amplitude
Element
Symbol
or Reactance
the Current
(or Angle) f
Relation
Resistor
R
R
In phase with vR
0+ (! 0 rad)
VR ! IRR
Capacitor
C
XC ! 1/vdC
Leads vC by 90+ (! p/2 rad)
'90+ (! 'p/2 rad)
VC ! ICXC
Inductor
L
XL ! vdL
Lags vL by 90+ (! p/2 rad)
$90+ (! $p/2 rad)
VL ! ILXL
KEY IDEA
In an ac circuit with a purely inductive load, the alternating
current iL(t) in the inductance lags the alternating potential
difference vL(t) by 90°. (In the mnemonic of the problem-
solving tactic, this circuit is “positively an ELI circuit,”
which tells us that the emf E leads the current I and that f is
positive.)
Calculations: Because the phase constant f
for the 
current is $90°, or $p/2 rad, we can write Eq. 31-29 as
iL ! IL sin(vdt ' f) ! IL sin(vdt ' p/2).
(31-54)
We can find the amplitude IL from Eq. 31-52 (VL ! ILXL) if
we first find the inductive reactance XL. From Eq. 31-49 
(XL ! vdL), with vd ! 2pfd, we can write
Then Eq. 31-52 tells us that the current amplitude is
(Answer)
Substituting this and vd ! 2pfd ! 120p into Eq. 31-54, we
have
iL ! (0.415 A) sin(120pt ' p/2).
(Answer)
IL ! VL
XL
! 36.0 V
86.7 " ! 0.415 A.
! 86.7 ".
XL ! 2pfdL ! (2p)(60.0 Hz)(230 & 10'3 H)
