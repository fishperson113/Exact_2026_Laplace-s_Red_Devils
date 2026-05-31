912

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

Sample Problem 31.02 Damped RLC circuit: charge amplitude

A  series  RLC circuit  has  inductance  L 12 mH, capaci-
tance C ! 1.6 mF, and  resistance  R ! 1.5 " and  begins  to
oscillate at time t ! 0.

!

Solving for t and then substituting given data yield

t ! ’

2L
R

 ln 0.50 ! ’

(2)(12 & 10’3 H)(ln 0.50)
1.5 "

(a) At what time t will the amplitude of the charge oscilla-
tions in the circuit be 50% of its initial value?  (Note that we
do not know that initial value.)

! 0.0111 s % 11 ms.

(Answer)

(b) How many oscillations are completed within this time?

KEY IDEA

KEY IDEA

The  amplitude  of  the  charge  oscillations  decreases  expo-
nentially  with  time  t: According  to  Eq. 31-25, the  charge
amplitude at any time t is Qe’Rt/2L, in which Q is the ampli-
tude at time t ! 0.

Calculations: We want the time when the charge amplitude
has decreased to 0.50Q— that is, when

Qe’Rt/2L ! 0.50Q.

We can now cancel Q (which also means that we can answer
the question without knowing the initial charge). Taking the
natural logarithms of both sides (to eliminate the exponen-
tial function), we have

’

Rt
2L

! ln 0.50.

The  time  for  one  complete  oscillation  is  the  period  T !
2p/v, where  the  angular  frequency  for  LC oscillations  is
LC)
given by Eq. 31-4

(v ! 1/

.

Calculation: In the time interval )t ! 0.0111 s, the number
of complete oscillations is

1

)t
T

!

)t

2p
0.0111 s
1
2p[(12 & 10’3 H)(1.6 & 10’6 F)]1/2 % 13.

LC

!

Thus, the  amplitude  decays  by  50%  in  about  13  complete
oscillations. This damping is less severe than that shown in
Fig. 31-3, where the amplitude decays by a little more than
50% in one oscillation.

(Answer)

Additional examples, video, and practice available at WileyPLUS

31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .

31.19 Distinguish alternating current from direct current.
31.20 For an ac generator, write the emf as a function of
time, identifying the emf amplitude and driving angular
frequency.

31.21 For an ac generator, write the current as a function of
time, identifying its amplitude and its phase constant with
respect to the emf.

31.22 Draw a schematic diagram of a (series) RLC circuit

that is driven by a generator.

31.23 Distinguish driving angular frequency vd from natural

angular frequency v.

31.24 In a driven (series) RLC circuit, identify the conditions
for resonance and the effect of resonance on the current
amplitude.

31.25 For each of the three basic circuits (purely resistive
load, purely capacitive load, and purely inductive load),

draw the circuit and sketch graphs and phasor diagrams
for voltage v(t) and current i(t).

31.26 For the three basic circuits, apply equations for voltage

v(t) and current i(t).

31.27 On a phasor diagram for each of the basic circuits,

identify angular speed, amplitude, projection on the verti-
cal axis, and rotation angle.

31.28 For each basic circuit, identify the phase constant, and
interpret it in terms of the relative orientations of the cur-
rent phasor and voltage phasor and also in terms of lead-
ing and lagging.

31.29 Apply the mnemonic “ELI positively is the ICE man.”
31.30 For each basic circuit, apply the relationships between

the voltage amplitude V and the current amplitude I.
31.31 Calculate capacitive reactance XC and inductive

reactance XL.

31-3 FORCE D  OSCI LL ATIONS  OF  TH R E E  SI M PLE  CI RCU ITS

913

Key Ideas
● A series RLC circuit may be set into forced oscillation at a
driving angular frequency vd by an external alternating emf

● The current driven in the circuit is

# ! #m sin vdt.

i ! I sin(vdt ’ f),

where f is the phase constant of the current.
● The alternating potential difference across a resistor has

!

IR; the current is in phase with the potential

amplitude VR
difference.
● For a capacitor, VC ! IXC, in which XC ! 1/vdC is the
capacitive reactance; the current here leads the potential
difference by 90+ (f ! ’90+ ! ’p/2 rad).
● For an inductor, VL ! IXL, in which XL ! vdL is the
inductive reactance; the current here lags the potential
difference by 90+ (f ! $90+ ! $p/2 rad).

Alternating Current
The  oscillations  in  an RLC circuit  will  not  damp  out  if  an  external  emf  device
supplies enough energy to make up for the energy dissipated as thermal energy
in the resistance R. Circuits in homes, offices, and factories, including countless
RLC circuits, receive such energy from local power companies. In most countries
the energy is supplied via oscillating emfs and currents — the current is said to be
an alternating current, or ac for short. (The nonoscillating current from a battery
is said to be a direct current, or dc.) These oscillating emfs and currents vary si-
nusoidally with time, reversing direction (in North America) 120 times per sec-
ond and thus having frequency f ! 60 Hz.

Electron Oscillations. At first sight this may seem to be a strange arrange-
ment. We have seen that the drift speed of the conduction electrons in household
1
wiring may typically be 4 & 10’5 m/s. If we now reverse their direction every
120 s
,
10’7 m in a half-cycle. At this rate, a typi-
&
such electrons can move only about 3
cal electron can drift past no more than about 10 atoms in the wiring before it is
required to reverse its direction. How, you may wonder, can the electron ever get
anywhere?

Although this question may be worrisome, it is a needless concern. The con-
duction electrons do not have to “get anywhere.” When we say that the current in
a  wire  is  one  ampere, we  mean  that  charge  passes  through  any  plane  cutting
across that wire at the rate of one coulomb per second. The speed at which the
charge carriers cross that plane does not matter directly; one ampere may corre-
spond  to  many  charge  carriers  moving  very  slowly  or  to  a  few  moving  very
rapidly. Furthermore, the  signal  to  the  electrons  to  reverse  directions — which
originates in the alternating emf provided by the power company’s generator —
is propagated along the conductor at a speed close to that of light. All electrons,
no  matter  where  they  are  located, get  their  reversal  instructions  at  about  the
same instant. Finally, we note that for many devices, such as lightbulbs and toast-
ers, the direction of motion is unimportant as long as the electrons do move so as
to transfer energy to the device via collisions with atoms in the device.

Why ac? The basic advantage of alternating current is this: As the current
alternates, so does the magnetic field that surrounds the conductor. This makes
possible  the  use  of  Faraday’s  law  of  induction, which, among  other  things,
means that we can step up (increase) or step down (decrease) the magnitude of
an alternating potential difference at will, using a device called a transformer,
as we shall discuss later. Moreover, alternating current is more readily adapt-
able to rotating machinery such as generators and motors than is (nonalternat-
ing) direct current.

Emf and Current. Figure 31-6 shows a simple model of an ac generator. As
, a

the conducting loop is forced to rotate through the external magnetic field
sinusoidally oscillating emf # is induced in the loop:

:
B

# ! #m sin vdt.

(31-28)

B

i

i

i

Slip rings

i

Metal
brush

Figure 31-6 The basic mechanism of an
alternating-current generator is a conduct-
ing loop rotated in an external magnetic
field. In practice, the alternating emf
induced in a coil of many turns of wire is
made accessible by means of slip rings
attached to the rotating loop. Each ring is
connected to one end of the loop wire and
is electrically connected to the rest of the
generator circuit by a conducting brush
against which the ring slips as the loop
(and it) rotates.

914

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

The angular frequency vd of the emf is equal to the angular speed with which the
loop rotates in the magnetic field, the phase of the emf is vdt, and the amplitude of
the emf is #m (where the subscript stands for maximum). When the rotating loop
is part of a closed conducting path, this emf produces (drives) a sinusoidal (alter-
nating) current along the path with the same angular frequency vd, which then is
called the driving angular frequency. We can write the current as

i ! I sin(vdt ’ f),

(31-29)

in which I is the amplitude of the driven current. (The phase vdt ’ f of the cur-
rent is traditionally written with a minus sign instead of as vdt $ f.) We include
a phase constant f in Eq. 31-29 because the current i may not be in phase with
the emf #. (As you will see, the phase constant depends on the circuit to which
the  generator  is  connected.)  We  can  also  write  the  current  i in  terms  of  the
driving frequency fd of the emf, by substituting 2pfd for vd in Eq. 31-29.

Forced Oscillations
We have seen that once started, the charge, potential difference, and current in
both  undamped  LC circuits  and  damped  RLC circuits  (with  small  enough  R)
. Such oscillations are said to be free
oscillate at angular frequency
oscillations (free of any external emf), and the angular frequency v is said to be
the circuit’s natural angular frequency.

v ! 1/

LC

1

When  the  external  alternating  emf  of  Eq. 31-28  is  connected  to  an  RLC
circuit, the oscillations of charge, potential difference, and current are said to be
driven  oscillations or forced  oscillations. These  oscillations  always  occur  at  the
driving angular frequency vd:

Whatever the natural angular frequency v of a circuit may be, forced oscillations
of charge, current, and potential difference in the circuit always occur at the driv-
ing angular frequency vd.

However, as you will see in Module 31-4, the amplitudes of the oscillations very much
depend on how close vd is to v. When the two angular frequencies match—a condi-
tion known as resonance—the amplitude I of the current in the circuit is maximum.

Three Simple Circuits
Later  in  this  chapter, we  shall  connect  an  external  alternating  emf  device  to
a  series  RLC circuit  as  in  Fig. 31-7. We  shall  then  find  expressions  for  the
amplitude I and  phase  constant  f of  the  sinusoidally  oscillating  current  in
terms of the amplitude #m and angular frequency vd of the external emf. First,
let’s consider three simpler circuits, each having an external emf and only one
other circuit element: R, C, or L. We start with a resistive element (a purely re-
sistive load).

A Resistive Load
Figure  31-8  shows  a  circuit  containing  a  resistance  element  of  value  R and  an
ac generator with the alternating emf of Eq. 31-28. By the loop rule, we have

i

R

L

i

C

i

Figure 31-7 A single-loop circuit containing a
resistor, a capacitor, and an inductor. A
generator, represented by a sine wave in a
circle, produces an alternating emf that es-
tablishes an alternating current; the direc-
tions of the emf and current are indicated
here at only one instant.

R

iR

vR

With Eq. 31-28, this gives us

# ’ vR ! 0.

vR ! #m sin vdt.

Figure 31-8 A resistor is connected across an
alternating-current generator.

Because  the  amplitude  VR of  the  alternating  potential  difference  (or  voltage)
across the resistance is equal to the amplitude #m of the alternating emf, we can

31-3 FORCE D  OSCI LL ATIONS  OF  TH R E E  SI M PLE  CI RCU ITS

915

write this as

vR ! VR sin vdt.

(31-30)

From the definition of resistance (R ! V/i), we can now write the current iR in the
resistance as

iR !

vR
R

!

VR
R

 sin vdt.

From Eq. 31-29, we can also write this current as

iR ! IR sin(vdt ’ f),

(31-31)

(31-32)

where IR is  the  amplitude  of  the  current  iR in  the  resistance. Comparing  Eqs.
31-31 and 31-32, we see that for a purely resistive load the phase constant f ! 0°.
We also see that the voltage amplitude and current amplitude are related by

VR ! IRR (resistor).

(31-33)

Although  we  found  this  relation  for  the  circuit  of  Fig. 31-8, it  applies  to  any
resistance in any ac circuit.

By comparing Eqs. 31-30 and 31-31, we see that the time-varying quantities
vR and iR are both functions of sin vdt with f ! 0°. Thus, these two quantities are
in phase, which means that their corresponding maxima (and minima) occur at
the same times. Figure 31-9a, which is a plot of vR(t) and iR(t), illustrates this fact.
Note that vR and iR do not decay here because the generator supplies energy to
the circuit to make up for the energy dissipated in R.

The time-varying quantities vR and iR can also be represented geometrically
by phasors. Recall from Module 16-6 that phasors are vectors that rotate around
an origin. Those that represent the voltage across and current in the resistor of
Fig. 31-8  are  shown  in  Fig. 31-9b at  an  arbitrary  time  t. Such  phasors  have  the
following properties:

Angular  speed: Both phasors rotate counterclockwise about the origin with an

angular speed equal to the angular frequency vd of vR and iR.

Length: The  length  of  each  phasor  represents  the  amplitude  of  the  alternating

quantity: VR for the voltage and IR for the current.

Projection: The  projection  of  each  phasor  on  the  vertical axis  represents  the
value  of  the  alternating  quantity  at  time  t: vR for  the  voltage  and  iR for
the current.

Rotation angle: The rotation angle of each phasor is equal to the phase of the

For a resistive load,
the current and potential
difference are in phase.

φ

 = 0° = 0 rad

vR, iR
IR

VR

iR

vR

0

T/2

t

T

Rotation of
phasors at
rate d
ω

IR

iR

vR

VR

dtω

“In phase” means
that they peak at
the same time.

(a)

Instants
represented in (b)

(b)

Figure 31-9 (a) The current iR and the potential difference vR across the resistor are plotted
on the same graph, both versus time t. They are in phase and complete one cycle in one
period T. (b) A phasor diagram shows the same thing as (a).

916

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

alternating  quantity  at  time  t. In  Fig. 31-9b, the  voltage  and  current  are  in
phase; so their phasors always have the same phase vdt and the same rotation
angle, and thus they rotate together.

Mentally  follow  the  rotation. Can  you  see  that  when  the  phasors  have
rotated  so  that  vdt ! 90° (they  point  vertically  upward), they  indicate  that  just
then vR ! VR and iR ! IR? Equations 31-30 and 31-32 give the same results.

Checkpoint 3

If we increase the driving frequency in a circuit with a purely resistive load, do
(a) amplitude VR and (b) amplitude IR increase, decrease, or remain the same?

Sample Problem 31.03 Purely resistive load: potential difference and current

In Fig. 31-8, resistance R is 200
and the sinusoidal alter-
nating  emf  device  operates  at  amplitude  #m ! 36.0 V  and
frequency fd ! 60.0 Hz.

"

(a) What is the potential difference vR(t) across the resistance
as a function of time t, and what is the amplitude VR of vR(t)?

We  can  leave  the  argument  of  the  sine  in  this  form  for  con-
venience, or we can write it as (377 rad/s)t or as (377 s’1)t.

(b)  What  are  the  current  iR(t)  in  the  resistance  and  the
amplitude IR of iR(t)?

KEY IDEA

KEY IDEA

In a circuit with a purely resistive load, the potential differ-
ence vR(t) across the resistance is always equal to the potential
difference  (t) across the emf device.

#

In an ac circuit with a purely resistive load, the alternating
current iR(t) in the resistance is in phase with the alternating
potential  difference  vR(t)  across  the  resistance; that  is, the
phase constant f for the current is zero.

Calculations: For our situation, vR(t)
Since #m is given, we can write

!

#(t) and VR

!

#m.

Calculations: Here we can write Eq. 31-29 as

VR ! #m ! 36.0 V.

(Answer)

iR ! IR sin(vdt ’ f) ! IR sin vdt.

(31-35)

To find vR(t), we use Eq. 31-28 to write

From Eq. 31-33, the amplitude IR is

vR(t) ! #(t) ! #m sin vdt

(31-34)

and then substitute #m ! 36.0 V and

vd ! 2pfd ! 2p(60 Hz) ! 120p

to obtain

IR !

VR
R

!

36.0 V
200 "

! 0.180 A.

(Answer)

Substituting  this  and  vd ! 2pfd ! 120p into  Eq. 31-35, we
have

vR ! (36.0 V) sin(120pt).

(Answer)

iR ! (0.180 A) sin(120pt).

(Answer)

Additional examples, video, and practice available at WileyPLUS

A Capacitive Load
Figure  31-10  shows  a  circuit  containing  a  capacitance  and  a  generator  with  the
alternating emf of Eq. 31-28. Using the loop rule and proceeding as we did when
we obtained Eq. 31-30, we find that the potential difference across the capacitor is

vC ! VC sin vdt,

(31-36)

C

iC vC

where VC is the amplitude of the alternating voltage across the capacitor. From
the definition of capacitance we can also write

Figure 31-10 A capacitor is connected across
an alternating-current generator.

Our concern, however, is with the current rather than the charge. Thus, we differ-

qC ! CvC ! CVC sin vdt.

(31-37)

31-3 FORCE D  OSCI LL ATIONS  OF  TH R E E  SI M PLE  CI RCU ITS

917

entiate Eq. 31-37 to find

iC !

dqC
dt

! vdCVC  cos vdt.

(31-38)

We now modify Eq. 31-38 in two ways. First, for reasons of symmetry of nota-
tion, we introduce the quantity XC, called the capacitive reactance of a capacitor,
defined as

XC !

1
vdC

(capacitive reactance).

(31-39)

Its  value  depends  not  only  on  the  capacitance  but  also  on  the  driving  angular
frequency  vd. We  know  from  the  definition  of  the  capacitive  time  constant
(t ! RC) that the SI unit for C can be expressed as seconds per ohm. Applying
this to Eq. 31-39 shows that the SI unit of XC is the ohm, just as for resistance R.

Second, we replace cos vdt in Eq. 31-38 with a phase-shifted sine:

cos vdt ! sin(vdt $ 90°).

You can verify this identity by shifting a sine curve 90° in the negative direction.

With these two modifications, Eq. 31-38 becomes

iC ! # VC

XC $ sin(vdt $ 90+).

(31-40)

From Eq. 31-29, we can also write the current iC in the capacitor of Fig. 31-10 as

iC ! IC sin(vdt ’ f),

(31-41)

where IC is the amplitude of iC. Comparing Eqs. 31-40 and 31-41, we see that for
a purely  capacitive  load  the  phase  constant  f for  the  current  is  ’90°. We  also
see that the voltage amplitude and current amplitude are related by

VC ! ICXC

(capacitor).

(31-42)

Although  we  found  this  relation  for  the  circuit  of  Fig. 31-10, it  applies  to  any
capacitance in any ac circuit.

Comparison of Eqs. 31-36 and 31-40, or inspection of Fig. 31-11a, shows that
the  quantities  vC and iC are  90°, p/2 rad, or  one-quarter  cycle, out  of  phase.
Furthermore, we  see  that  iC leads  vC, which  means  that, if  you  monitored  the
current iC and the potential difference vC in the circuit of Fig. 31-10, you would
find that iC reaches its maximum before vC does, by one-quarter cycle.

For a capacitive load, the
current leads the potential
difference by 90º.

vC, iC

IC
VC

φ

= –90° = –   /2 rad

π

vC

0

T/2

iC

t

T

Figure 31-11 (a) The current in the capacitor leads
the voltage by 90° (! p/2 rad). (b) A phasor dia-
gram shows the same thing.

Instants
represented in (b)

(a)

IC

iC

vC

Rotation of
phasors at
rate d
ω

VC

dtω

“Leads” means that the
current peaks at an
earlier time than the
potential difference.

(b)

918

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

This  relation  between  iC and vC is  illustrated  by  the  phasor  diagram  of
Fig. 31-11b. As the phasors representing these two quantities rotate counterclock-
wise together, the phasor labeled IC does indeed lead that labeled VC, and by an
angle  of  90°; that  is, the  phasor  IC coincides  with  the  vertical  axis  one-quarter
cycle  before  the  phasor  VC does. Be  sure  to  convince  yourself  that  the  phasor
diagram of Fig. 31-11b is consistent with Eqs. 31-36 and 31-40.

Checkpoint 4

The figure shows, in (a), a sine curve S(t) ! sin(vdt) and three
other sinusoidal curves A(t), B(t), and C(t), each of the form
sin(vdt ’ f). (a) Rank the three other curves according to the
value of f, most positive first and most negative last. (b) Which
curve corresponds to which phasor in (b) of the figure? (c)
Which curve leads the others?

A

B

S

C

2

3

1

4

t

(a)

(b)

Sample Problem 31.04 Purely capacitive load: potential difference and current

In  Fig. 31-10, capacitance  C is  15.0 mF  and  the  sinusoidal
alternating  emf  device  operates  at  amplitude  #m ! 36.0 V
and frequency fd ! 60.0 Hz.

(a)  What  are  the  potential  difference  vC(t)  across  the
capacitance and the amplitude VC of vC(t)?

KEY IDEA

In a circuit with a purely capacitive load, the potential dif-
ference vC(t)  across  the  capacitance  is  always  equal  to  the
potential difference #(t) across the emf device.

Calculations: Here  we  have  vC(t) ! #(t)  and  VC ! #m.
Since #m is given, we have

VC ! #m ! 36.0 V.

(Answer)

To find vC(t), we use Eq. 31-28 to write

vC(t) ! #(t) ! #m sin vdt.

(31-43)

Then, substituting  #m ! 36.0 V  and  vd ! 2pfd ! 120p into
Eq. 31-43, we have

vC ! (36.0 V) sin(120pt).

(Answer)

(b) What are the current iC(t) in the circuit as a function of
time and the amplitude IC of iC(t)?

KEY IDEA

In an ac circuit with a purely capacitive load, the alternating
current iC(t) in the capacitance leads the alternating poten-
tial difference vC(t) by 90+; that is, the phase constant f for
the current is ’90°, or ’p/2 rad.

Calculations: Thus, we can write Eq. 31-29 as

iC ! IC sin(vdt ’ f) ! IC sin(vdt $ p/2).

(31-44)

We can find the amplitude IC from Eq. 31-42 (VC ! ICXC) if
we  first  find  the  capacitive  reactance XC. From  Eq. 31-39
(XC ! 1/vdC), with vd ! 2pfd, we can write

XC !

1
2pfdC
! 177 ".

!

1
(2p)(60.0 Hz)(15.0 & 10’6 F)

Then Eq. 31-42 tells us that the current amplitude is

IC !

VC
XC

!

36.0 V
177 "

! 0.203 A.

(Answer)

Substituting  this  and  vd ! 2pfd ! 120p into  Eq. 31-44, we
have

iC ! (0.203 A) sin(120pt $ p/2).

(Answer)

Additional examples, video, and practice available at WileyPLUS

L

iL vL

Figure 31-12 An inductor is connected across
an alternating-current generator.

An Inductive Load
Figure 31-12 shows a circuit containing an inductance and a generator with the al-
ternating  emf  of  Eq. 31-28. Using  the  loop  rule  and  proceeding  as  we  did  to
obtain Eq. 31-30, we find that the potential difference across the inductance is

vL ! VL sin vdt,

(31-45)

31-3 FORCE D  OSCI LL ATIONS  OF  TH R E E  SI M PLE  CI RCU ITS

919

For an inductive load,
the current lags the
potential difference
by 90º.

vL, iL

VL
IL

(a)

φ

= +90° = +   /2 rad

π

vL

iL

0

T/2

t

T

Instants
represented in (b)

Rotation of
phasors at
rate d
  ω

vL

VL

dtω

“Lags” means that the
current peaks at a
later time than the
potential difference.

iL

IL

(b)

Figure 31-13 (a) The current in the inductor
lags the voltage by 90° (! p/2 rad). (b) A
phasor diagram shows the same thing.

where VL is the amplitude of vL. From Eq. 30-35 (#L ! ’L di/dt), we can write
the potential difference across an inductance L in which the current is changing
at the rate diL/dt as

vL ! L

.

(31-46)

diL
dt

If we combine Eqs. 31-45 and 31-46, we have

diL
dt

!

VL
L

 sin vdt.

Our concern, however, is with the current, so we integrate:

iL ! " diL !

VL

L " sin vd t dt ! ’# VL

vdL $ cos vdt.

(31-47)

(31-48)

We now modify this equation in two ways. First, for reasons of symmetry of
notation, we  introduce  the  quantity  XL, called  the  inductive  reactance of  an
inductor, which is defined as

XL ! vdL (inductive reactance).

(31-49)

The  value  of  XL depends  on  the  driving  angular  frequency  vd. The  unit  of  the
inductive time constant tL indicates that the SI unit of XL is the ohm, just as it is
for XC and for R.

Second, we replace ’cos vdt in Eq. 31-48 with a phase-shifted sine:

’cos vdt ! sin(vdt ’ 90°).
You can verify this identity by shifting a sine curve 90° in the positive direction.

With these two changes, Eq. 31-48 becomes

iL ! # VL

XL $ sin(vdt ’ 90+).

From Eq. 31-29, we can also write this current in the inductance as

iL ! IL sin(vdt ’ f),

(31-50)

(31-51)

where IL is the amplitude of the current iL. Comparing Eqs. 31-50 and 31-51, we
see that for a purely inductive load the phase constant f for the current is $90°.
We also see that the voltage amplitude and current amplitude are related by

VL ! ILXL

(inductor).

(31-52)

Although  we  found  this  relation  for  the  circuit  of  Fig. 31-12, it  applies  to  any
inductance in any ac circuit.

Comparison  of  Eqs. 31-45  and  31-50, or  inspection  of  Fig. 31-13a, shows
that the quantities iL and vL are 90° out of phase. In this case, however, iL lags
vL; that is, monitoring the current iL and the potential difference vL in the cir-
cuit  of  Fig. 31-12  shows  that  iL reaches  its  maximum  value  after  vL does, by
one-quarter cycle. The phasor diagram of Fig. 31-13b also contains this informa-
tion. As the phasors rotate counterclockwise in the figure, the phasor labeled IL
does indeed lag that labeled VL, and by an angle of 90°. Be sure to convince your-
self that Fig. 31-13b represents Eqs. 31-45 and 31-50.

Checkpoint 5

If we increase the driving frequency in a circuit with a purely capacitive load, do
(a) amplitude VC and (b) amplitude IC increase, decrease, or remain the same? If,
instead, the circuit has a purely inductive load, do (c) amplitude VL and (d) amplitude
IL increase, decrease, or remain the same?

920

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

Problem-Solving Tactics

Leading  and  Lagging  in  AC  Circuits: Table  31-2  summa-
rizes the relations between the current i and the voltage v
for each of the three kinds of circuit elements we have con-
sidered. When  an  applied  alternating  voltage  produces  an
alternating current in these elements, the current is always
in phase with the voltage across a resistor, always leads the
voltage  across  a  capacitor, and  always  lags  the  voltage
across an inductor.

Many  students  remember  these  results  with  the
mnemonic “ELI the ICE man.” ELI contains  the  letter  L

(for inductor), and in it the letter I (for current) comes after
the letter E (for emf or voltage). Thus, for an inductor, the
current lags (comes after) the voltage. Similarly, ICE (which
contains  a  C for  capacitor)  means  that  the  current  leads
(comes before) the voltage. You might also use the modified
mnemonic  “ELI  positively is  the  ICE man” to  remember
that the phase constant f is positive for an inductor.

If  you  have  difficulty  in  remembering  whether  XC is
equal to vdC (wrong) or 1/vdC (right), try remembering that
C is in the “cellar” — that is, in the denominator.

Table 31-2 Phase and Amplitude Relations for Alternating Currents and Voltages

Circuit
Element

Resistor
Capacitor
Inductor

Symbol

R
C
L

Resistance
or Reactance

R
XC ! 1/vdC
XL ! vdL

Phase of
the Current

In phase with vR
Leads vC by 90+ (! p/2 rad)
Lags vL by 90+ (! p/2 rad)

Phase Constant
(or Angle) f

0+ (! 0 rad)
’90+ (! ’p/2 rad)
$90+ (! $p/2 rad)

Amplitude
Relation

VR ! IRR
VC ! ICXC
VL ! ILXL

Sample Problem 31.05 Purely inductive load: potential difference and current

In  Fig. 31-12, inductance  L is  230 mH  and  the  sinusoidal
alternating  emf  device  operates  at  amplitude  #m ! 36.0 V
and frequency fd ! 60.0 Hz.

(a) What are the potential difference vL(t) across the induc-
tance and the amplitude VL of vL(t)?

KEY IDEA

In a circuit with a purely inductive load, the potential differ-
ence vL(t)  across  the  inductance  is  always  equal  to  the
potential difference #(t) across the emf device.

Calculations: Here  we  have  vL(t) ! #(t)  and  VL ! #m.
Since #m is given, we know that

VL ! #m ! 36.0 V.

(Answer)

To find vL(t), we use Eq. 31-28 to write

vL(t) ! #(t) ! #m sin vdt.

(31-53)

Then, substituting  #m ! 36.0 V  and  vd ! 2pfd ! 120p into
Eq. 31-53, we have

vL ! (36.0 V) sin(120pt).

(Answer)

(b) What are the current iL(t) in the circuit as a function of
time and the amplitude IL of iL(t)?

KEY IDEA

In an ac circuit with a purely inductive load, the alternating
current iL(t) in the inductance lags the alternating potential
difference vL(t)  by 90°. (In  the  mnemonic  of  the  problem-
solving  tactic, this  circuit  is  “positively  an  ELI circuit,”
which tells us that the emf E leads the current I and that f is
positive.)

Calculations: Because  the  phase  constant  f for  the
current is $90°, or $p/2 rad, we can write Eq. 31-29 as

iL ! IL sin(vdt ’ f) ! IL sin(vdt ’ p/2).

(31-54)

We can find the amplitude IL from Eq. 31-52 (VL ! ILXL) if
we  first  find  the  inductive  reactance  XL. From  Eq. 31-49
(XL ! vdL), with vd ! 2pfd, we can write

XL ! 2p fdL ! (2p)(60.0 Hz)(230 & 10’3 H)

! 86.7 ".

Then Eq. 31-52 tells us that the current amplitude is

IL !

VL
XL

!

36.0 V
86.7 "

! 0.415 A.

(Answer)

Substituting  this  and  vd ! 2pfd ! 120p into  Eq. 31-54, we
have

iL ! (0.415 A) sin(120pt ’ p/2).

(Answer)

Additional examples, video, and practice available at WileyPLUS
