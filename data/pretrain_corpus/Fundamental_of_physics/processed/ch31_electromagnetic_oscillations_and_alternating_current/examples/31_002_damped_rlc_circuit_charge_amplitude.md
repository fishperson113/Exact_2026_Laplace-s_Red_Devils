Sample Problem 31.02
Damped RLC circuit: charge amplitude
A series RLC circuit has inductance L
12 mH, capaci-
tance C ! 1.6 mF, and resistance R ! 1.5 " and begins to
oscillate at time t ! 0.
(a) At what time t will the amplitude of the charge oscilla-
tions in the circuit be 50% of its initial value?  (Note that we
do not know that initial value.)
KEY IDEA
The amplitude of the charge oscillations decreases expo-
nentially with time t: According to Eq. 31-25, the charge
amplitude at any time t is Qe'Rt/2L, in which Q is the ampli-
tude at time t ! 0.
Calculations: We want the time when the charge amplitude
has decreased to 0.50Q- that is, when
Qe'Rt/2L ! 0.50Q.
We can now cancel Q (which also means that we can answer
the question without knowing the initial charge).Taking the
natural logarithms of both sides (to eliminate the exponen-
tial function), we have
' Rt
2L ! ln 0.50.
!
Additional examples, video, and practice available at WileyPLUS

913
31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS
Alternating Current
The oscillations in an RLC circuit will not damp out if an external emf device
supplies enough energy to make up for the energy dissipated as thermal energy
in the resistance R. Circuits in homes, offices, and factories, including countless
RLC circuits, receive such energy from local power companies. In most countries
the energy is supplied via oscillating emfs and currents-the current is said to be
an alternating current, or ac for short. (The nonoscillating current from a battery
is said to be a direct current, or dc.) These oscillating emfs and currents vary si-
nusoidally with time, reversing direction (in North America) 120 times per sec-
ond and thus having frequency f ! 60 Hz.
Electron Oscillations. At first sight this may seem to be a strange arrange-
ment.We have seen that the drift speed of the conduction electrons in household
wiring may typically be 4 & 10'5 m/s. If we now reverse their direction every 
,
such electrons can move only about 3
10'7 m in a half-cycle.At this rate, a typi-
cal electron can drift past no more than about 10 atoms in the wiring before it is
required to reverse its direction. How, you may wonder, can the electron ever get
anywhere?
Although this question may be worrisome, it is a needless concern. The con-
duction electrons do not have to “get anywhere.” When we say that the current in
a wire is one ampere, we mean that charge passes through any plane cutting
across that wire at the rate of one coulomb per second. The speed at which the
charge carriers cross that plane does not matter directly; one ampere may corre-
spond to many charge carriers moving very slowly or to a few moving very
rapidly. Furthermore, the signal to the electrons to reverse directions-which
originates in the alternating emf provided by the power company’s generator-
is propagated along the conductor at a speed close to that of light. All electrons,
no matter where they are located, get their reversal instructions at about the
same instant. Finally, we note that for many devices, such as lightbulbs and toast-
ers, the direction of motion is unimportant as long as the electrons do move so as
to transfer energy to the device via collisions with atoms in the device.
Why ac? The basic advantage of alternating current is this: As the current
alternates, so does the magnetic field that surrounds the conductor. This makes
possible the use of Faraday’s law of induction, which, among other things,
means that we can step up (increase) or step down (decrease) the magnitude of
an alternating potential difference at will, using a device called a transformer,
as we shall discuss later. Moreover, alternating current is more readily adapt-
able to rotating machinery such as generators and motors than is (nonalternat-
ing) direct current.
Emf and Current. Figure 31-6 shows a simple model of an ac generator. As
the conducting loop is forced to rotate through the external magnetic field 
, a
sinusoidally oscillating emf # is induced in the loop:
# ! #m sin vdt.
(31-28)
B
:
&
1
120 s
●A series RLC circuit may be set into forced oscillation at a
driving angular frequency vd by an external alternating emf
# ! #m sin vdt.
●The current driven in the circuit is   
i ! I sin(vdt ' f),
where f is the phase constant of the current.
●The alternating potential difference across a resistor has
amplitude VR
IR; the current is in phase with the potential
difference.
●For a capacitor, VC ! IXC, in which XC ! 1/vdC is the
capacitive reactance; the current here leads the potential
difference by 90+ (f ! '90+ ! 'p/2 rad).
●For an inductor, VL ! IXL, in which XL ! vdL is the
inductive reactance; the current here lags the potential
difference by 90+ (f ! $90+ ! $p/2 rad).
!
Key Ideas
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
Slip rings 
Metal
brush
i
i
i
i
B

914
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
Figure 31-7 A single-loop circuit containing a
resistor, a capacitor, and an inductor.A
generator, represented by a sine wave in a
circle, produces an alternating emf that es-
tablishes an alternating current; the direc-
tions of the emf and current are indicated
here at only one instant.
i
i
i
C
R
L
Figure 31-8 A resistor is connected across an
alternating-current generator.
iR
R
vR
The angular frequency vd of the emf is equal to the angular speed with which the
loop rotates in the magnetic field, the phase of the emf is vdt, and the amplitude of
the emf is #m (where the subscript stands for maximum).When the rotating loop
is part of a closed conducting path, this emf produces (drives) a sinusoidal (alter-
nating) current along the path with the same angular frequency vd, which then is
called the driving angular frequency. We can write the current as
i ! I sin(vdt ' f),
(31-29)
in which I is the amplitude of the driven current. (The phase vdt ' f of the cur-
rent is traditionally written with a minus sign instead of as vdt $ f.) We include
a phase constant f in Eq. 31-29 because the current i may not be in phase with
the emf #. (As you will see, the phase constant depends on the circuit to which
the generator is connected.) We can also write the current i in terms of the
driving frequency fd of the emf, by substituting 2pfd for vd in Eq. 31-29.
Forced Oscillations
We have seen that once started, the charge, potential difference, and current in
both undamped LC circuits and damped RLC circuits (with small enough R)
oscillate at angular frequency 
. Such oscillations are said to be free
oscillations (free of any external emf), and the angular frequency v is said to be
the circuit’s natural angular frequency.
When the external alternating emf of Eq. 31-28 is connected to an RLC
circuit, the oscillations of charge, potential difference, and current are said to be
driven oscillations or forced oscillations. These oscillations always occur at the
driving angular frequency vd:
v ! 1/1LC
Whatever the natural angular frequency v of a circuit may be, forced oscillations
of charge, current, and potential difference in the circuit always occur at the driv-
ing angular frequency vd.
However,as you will see in Module 31-4,the amplitudes of the oscillations very much
depend on how close vd is to v.When the two angular frequencies match-a condi-
tion known as resonance-the amplitude I of the current in the circuit is maximum.
Three Simple Circuits
Later in this chapter, we shall connect an external alternating emf device to 
a series RLC circuit as in Fig. 31-7. We shall then find expressions for the
amplitude I and phase constant f of the sinusoidally oscillating current in
terms of the amplitude #m and angular frequency vd of the external emf. First,
let’s consider three simpler circuits, each having an external emf and only one
other circuit element: R, C, or L. We start with a resistive element (a purely re-
sistive load).
A Resistive Load
Figure 31-8 shows a circuit containing a resistance element of value R and an
ac generator with the alternating emf of Eq. 31-28. By the loop rule, we have
# ' vR ! 0.
With Eq. 31-28, this gives us
vR ! #m sin vdt.
Because the amplitude VR of the alternating potential difference (or voltage)
across the resistance is equal to the amplitude #m of the alternating emf, we can

915
31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS
write this as
vR ! VR sin vdt.
(31-30)
From the definition of resistance (R ! V/i), we can now write the current iR in the
resistance as
(31-31)
From Eq. 31-29, we can also write this current as
iR ! IR sin(vdt ' f),
(31-32)
where IR is the amplitude of the current iR in the resistance. Comparing Eqs.
31-31 and 31-32, we see that for a purely resistive load the phase constant f ! 0°.
We also see that the voltage amplitude and current amplitude are related by
VR ! IRR
(resistor).
(31-33)
Although we found this relation for the circuit of Fig. 31-8, it applies to any
resistance in any ac circuit.
By comparing Eqs. 31-30 and 31-31, we see that the time-varying quantities
vR and iR are both functions of sin vdt with f ! 0°.Thus, these two quantities are
in phase, which means that their corresponding maxima (and minima) occur at
the same times. Figure 31-9a, which is a plot of vR(t) and iR(t), illustrates this fact.
Note that vR and iR do not decay here because the generator supplies energy to
the circuit to make up for the energy dissipated in R.
The time-varying quantities vR and iR can also be represented geometrically
by phasors. Recall from Module 16-6 that phasors are vectors that rotate around
an origin. Those that represent the voltage across and current in the resistor of
Fig. 31-8 are shown in Fig. 31-9b at an arbitrary time t. Such phasors have the
following properties:
Angular speed: Both phasors rotate counterclockwise about the origin with an
angular speed equal to the angular frequency vd of vR and iR.
Length: The length of each phasor represents the amplitude of the alternating
quantity: VR for the voltage and IR for the current.
Projection: The projection of each phasor on the vertical axis represents the
value of the alternating quantity at time t: vR for the voltage and iR for
the current.
Rotation angle: The rotation angle of each phasor is equal to the phase of the
iR ! vR
R ! VR
R  sin vdt.
vR, iR
T
IR
 = 0° = 0 rad
VR
0
Instants
represented in (b)
(a)
(b)
iR
vR
VR
IR
Rotation of
phasors at
rate
d
t
dt
ω
vR
iR
T/2
ω
φ
For a resistive load,
the current and potential
difference are in phase.
“In phase” means
that they peak at
the same time.
Figure 31-9 (a) The current iR and the potential difference vR across the resistor are plotted
on the same graph, both versus time t.They are in phase and complete one cycle in one
period T. (b) A phasor diagram shows the same thing as (a).

916
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
Additional examples, video, and practice available at WileyPLUS
Figure 31-10 A capacitor is connected across
an alternating-current generator.
iC vC
C
alternating quantity at time t. In Fig. 31-9b, the voltage and current are in
phase; so their phasors always have the same phase vdt and the same rotation
angle, and thus they rotate together.
Mentally follow the rotation. Can you see that when the phasors have
rotated so that vdt ! 90° (they point vertically upward), they indicate that just
then vR ! VR and iR ! IR? Equations 31-30 and 31-32 give the same results.
Checkpoint 3
If we increase the driving frequency in a circuit with a purely resistive load, do 
(a) amplitude VR and (b) amplitude IR increase, decrease, or remain the same?
We can leave the argument of the sine in this form for con-
venience,or we can write it as (377 rad/s)t or as (377 s'1)t.
(b) What are the current iR(t) in the resistance and the 
amplitude IR of iR(t)?
KEY IDEA
In an ac circuit with a purely resistive load, the alternating
current iR(t) in the resistance is in phase with the alternating
potential difference vR(t) across the resistance; that is, the
phase constant f for the current is zero.
Calculations: Here we can write Eq. 31-29 as
iR ! IR sin(vdt ' f) ! IR sin vdt.
(31-35)
From Eq. 31-33, the amplitude IR is
(Answer)
Substituting this and vd ! 2pfd ! 120p into Eq. 31-35, we
have
iR ! (0.180 A) sin(120pt).
(Answer)
IR ! VR
R ! 36.0 V
200 " ! 0.180 A.
