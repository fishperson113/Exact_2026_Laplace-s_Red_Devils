Sample Problem 31.01
LC oscillator: potential change, rate of current change
A 1.5 mF capacitor is charged to 57 V by a battery, which is
then removed.At time t ! 0, a 12 mH coil is connected in se-
ries with the capacitor to form an LC oscillator (Fig. 31-1).
(a) What is the potential difference vL(t) across the inductor
as a function of time?
KEY IDEAS
(1) The current and potential differences of the circuit (both
the potential difference of the capacitor and the potential
difference of the coil) undergo sinusoidal oscillations.
(2) We can still apply the loop rule to these oscillating
potential differences, just as we did for the nonoscillating
circuits of Chapter 27.

910
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
31-2 DAMPED OSCILLATIONS IN AN RLC CIRCUIT
After reading this module, you should be able to . . .
31.13 Draw the schematic of a damped RLC circuit and
explain why the oscillations are damped.
31.14 Starting with the expressions for the field energies
and the rate of energy loss in a damped RLC circuit,
write the differential equation for the charge q on the
capacitor.
31.15 For a damped RLC circuit, apply the expression for
charge q(t).
31.16 Identify that in a damped RLC circuit, the charge
amplitude and the amplitude of the electric field energy
decrease exponentially with time.
31.17 Apply the relationship between the angular frequency
of a given damped RLC oscillator and the angular
frequency v of the circuit if R is removed.
31.18 For a damped RLC circuit, apply the expression for
the electric field energy UE as a function of time.
v*
Learning Objectives
●Oscillations in an LC circuit are damped when a 
dissipative element R is also present in the circuit. 
Then
(RLC circuit).
L d 2q
dt2 $ R dq
dt $ 1
C q ! 0
●The solution of this differential equation is
q ! Qe'Rt/2L cos(v*t $ f),
where
We consider only situations with small R and thus small
damping; then v* % v.
v* ! 2v2 ' (R/2L)2.
Key Ideas
Additional examples, video, and practice available at WileyPLUS
(Note that this cosine function does indeed yield maximum
q (! Q) when t ! 0.) To get the potential difference vC(t),
we divide both sides of Eq. 31-19 by C to write
and then use Eq. 25-1 to write
vC ! VC cos vt.
(31-20)
Here, VC is the amplitude of the oscillations in the potential
difference vC across the capacitor.
Next, substituting vC
vL from Eq. 31-18, we find
vL ! VC cos vt.
(31-21)
We can evaluate the right side of this equation by first not-
ing that the amplitude VC is equal to the initial (maximum)
potential difference of 57 V across the capacitor. Then we
find v with Eq. 31-4:
Thus, Eq. 31-21 becomes
vL ! (57 V) cos(7500 rad/s)t.
(Answer)
! 7454 rad/s % 7500 rad/s.
v !
1
1LC
!
1
[(0.012 H)(1.5 & 10'6 F)]0.5
!
q
C ! Q
C  cos vt,
(b) What is the maximum rate (di/dt)max at which the current
i changes in the circuit?
KEY IDEA
With the charge on the capacitor oscillating as in Eq. 31-12,
the current is in the form of Eq. 31-13. Because f ! 0, that
equation gives us
i ! 'vQ sin vt.
Calculations: Taking the derivative, we have
We can simplify this equation by substituting CVC for Q
(because we know C and VC but not Q) and 
for v
according to Eq. 31-4.We get
This tells us that the current changes at a varying (sinu-
soidal) rate, with its maximum rate of change being
(Answer)
VC
L !
57 V
0.012 H ! 4750 A/s % 4800 A/s.
di
dt ! '
1
LC CVC cos vt ! ' VC
L  cos vt.
1/1LC
di
dt ! d
dt  ('vQ sin vt) ! 'v2Q cos vt.

911
31-2 DAMPED OSCILLATIONS IN AN RLC CIRCUIT
Damped Oscillations in an RLC Circuit
A circuit containing resistance, inductance, and capacitance is called an RLC
circuit. We shall here discuss only series RLC circuits like that shown in Fig. 31-5.
With a resistance R present, the total electromagnetic energy U of the circuit (the
sum of the electrical energy and magnetic energy) is no longer constant; instead,
it decreases with time as energy is transferred to thermal energy in the resistance.
Because of this loss of energy, the oscillations of charge, current, and potential
difference continuously decrease in amplitude, and the oscillations are said to be
damped, just as with the damped block-spring oscillator of Module 15-5.
To analyze the oscillations of this circuit, we write an equation for the total
electromagnetic energy U in the circuit at any instant. Because the resistance
does not store electromagnetic energy, we can use Eq. 31-9:
(31-22)
Now, however, this total energy decreases as energy is transferred to thermal
energy. The rate of that transfer is, from Eq. 26-27,
(31-23)
where the minus sign indicates that U decreases. By differentiating Eq. 31-22 with
respect to time and then substituting the result in Eq. 31-23, we obtain
Substituting dq/dt for i and d 2q/dt2 for di/dt, we obtain
(RLC circuit),
(31-24)
which is the differential equation for damped oscillations in an RLC circuit.
Charge Decay. The solution to Eq. 31-24 is
q ! Qe'Rt/2L cos(v*t $ f),
(31-25)
in which
(31-26)
where 
, as with an undamped oscillator. Equation 31-25 tells us how
the charge on the capacitor oscillates in a damped RLC circuit; that equation is
the electromagnetic counterpart of Eq. 15-42, which gives the displacement of
a damped block-spring oscillator.
Equation 31-25 describes a sinusoidal oscillation (the cosine function) with
an exponentially decaying amplitude Qe'Rt/2L (the factor that multiplies the
cosine). The angular frequency v* of the damped oscillations is always less than
the angular frequency v of the undamped oscillations; however, we shall here
consider only situations in which R is small enough for us to replace v* with v.
Energy Decay. Let us next find an expression for the total electromagnetic
energy U of the circuit as a function of time. One way to do so is to monitor
the energy of the electric field in the capacitor, which is given by Eq. 31-1 
(UE ! q2/2C). By substituting Eq. 31-25 into Eq. 31-1, we obtain
(31-27)
Thus, the energy of the electric field oscillates according to a cosine-squared
term, and the amplitude of that oscillation decreases exponentially with time.
UE ! q2
2C ! [Qe'Rt/2L cos(v*t $ f)]2
2C
! Q2
2C e'Rt/L cos2(v*t $ f).
v ! 1/1LC
v* ! 2v2 ' (R/2L)2,
L d 2q
dt2 $ R dq
dt $ 1
C q ! 0
dU
dt ! Li di
dt $ q
C
dq
dt ! 'i2R.
dU
dt ! 'i2R,
U ! UB $ UE ! Li2
2
$ q2
2C .
Figure 31-5 A series RLC circuit. As the
charge contained in the circuit oscillates
back and forth through the resistance,
electromagnetic energy is dissipated as
thermal energy, damping (decreasing the
amplitude of) the oscillations.
C
L
R

912
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS
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
Learning Objectives
Solving for t and then substituting given data yield
(Answer)
(b) How many oscillations are completed within this time?
KEY IDEA
The time for one complete oscillation is the period T !
2p/v, where the angular frequency for LC oscillations is
given by Eq. 31-4 
.
Calculation: In the time interval )t ! 0.0111 s, the number
of complete oscillations is
(Answer)
Thus, the amplitude decays by 50% in about 13 complete
oscillations. This damping is less severe than that shown in
Fig. 31-3, where the amplitude decays by a little more than
50% in one oscillation.
!
0.0111 s
2p[(12 & 10'3 H)(1.6 & 10'6 F)]1/2 % 13.
)t
T !
)t
2p 1LC
(v ! 1/1LC)
! 0.0111 s % 11 ms. 
t ! ' 2L
R  ln 0.50 ! ' (2)(12 & 10'3 H)(ln 0.50)
1.5 "
