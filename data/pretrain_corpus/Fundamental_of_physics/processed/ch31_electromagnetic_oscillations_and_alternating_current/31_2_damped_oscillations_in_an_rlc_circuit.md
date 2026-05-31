910

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

(Note that this cosine function does indeed yield maximum
q (! Q) when t ! 0.) To get the potential difference vC(t),
we divide both sides of Eq. 31-19 by C to write

(b) What is the maximum rate (di/dt)max at which the current
i changes in the circuit?

q
C

!

Q
C

 cos vt,

and then use Eq. 25-1 to write

vC ! VC cos vt.

(31-20)

Here, VC is the amplitude of the oscillations in the potential
difference vC across the capacitor.

Next, substituting vC

!

vL from Eq. 31-18, we find

vL ! VC cos vt.

(31-21)

We can evaluate the right side of this equation by first not-
ing that the amplitude VC is equal to the initial (maximum)
potential  difference  of  57 V  across  the  capacitor. Then  we
find v with Eq. 31-4:

v !

1
LC

!

1
[(0.012 H)(1.5 & 10’6 F)]0.5

1

! 7454 rad/s % 7500 rad/s.

Thus, Eq. 31-21 becomes

vL ! (57 V) cos(7500 rad/s)t.

(Answer)

KEY IDEA

With the charge on the capacitor oscillating as in Eq. 31-12,
the current is in the form of Eq. 31-13. Because f ! 0, that
equation gives us

i ! ’vQ sin vt.

Calculations: Taking the derivative, we have

di
dt

!

d
dt

 (’vQ sin vt) ! ’v2Q cos vt.

We  can  simplify  this  equation  by  substituting  CVC for Q
for v
(because we know C and VC but not Q) and
according to Eq. 31-4. We get

LC

1/

1

di
dt

! ’

1
LC

CVC cos vt ! ’

VC
L

 cos vt.

This  tells  us  that  the  current  changes  at  a  varying  (sinu-
soidal) rate, with its maximum rate of change being

VC
L

!

57 V
0.012 H

! 4750 A/s % 4800 A/s.

(Answer)

Additional examples, video, and practice available at WileyPLUS

31-2 DAMPED OSCILLATIONS IN AN RLC CIRCUIT

Learning Objectives
After reading this module, you should be able to . . .
31.13 Draw the schematic of a damped RLC circuit and

explain why the oscillations are damped.

31.14 Starting with the expressions for the field energies
and the rate of energy loss in a damped RLC circuit,
write the differential equation for the charge q on the
capacitor.

31.16 Identify that in a damped RLC circuit, the charge

amplitude and the amplitude of the electric field energy
decrease exponentially with time.

31.17 Apply the relationship between the angular frequency
of a given damped RLC oscillator and the angular

v*
frequency v of the circuit if R is removed.

31.15 For a damped RLC circuit, apply the expression for

31.18 For a damped RLC circuit, apply the expression for

charge q(t).

the electric field energy UE as a function of time.

Key Ideas
● Oscillations in an LC circuit are damped when a
dissipative element R is also present in the circuit.
Then

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

● The solution of this differential equation is
q ! Qe’Rt/2L cos(v*t $ f),

v* !

where
We consider only situations with small R and thus small
damping; then v* % v.

v2 ’ (R/2L)2.

2

31-2 DAM PE D  OSCI LL ATIONS  I N  AN  R LC CI RCU IT

911

R

L

C

Figure 31-5 A series RLC circuit. As the
charge contained in the circuit oscillates
back and forth through the resistance,
electromagnetic energy is dissipated as
thermal energy, damping (decreasing the
amplitude of) the oscillations.

Damped Oscillations in an RLC Circuit
A  circuit  containing  resistance, inductance, and  capacitance  is  called  an  RLC
circuit. We shall here discuss only series RLC circuits like that shown in Fig. 31-5.
With a resistance R present, the total electromagnetic energy U of the circuit (the
sum of the electrical energy and magnetic energy) is no longer constant; instead,
it decreases with time as energy is transferred to thermal energy in the resistance.
Because of this loss of energy, the oscillations of charge, current, and potential
difference continuously decrease in amplitude, and the oscillations are said to be
damped, just as with the damped block – spring oscillator of Module 15-5.

To analyze the oscillations of this circuit, we write an equation for the total
electromagnetic  energy  U in  the  circuit  at  any  instant. Because  the  resistance
does not store electromagnetic energy, we can use Eq. 31-9:

U ! UB $ UE !

Li 2
2

$

q2
2C

.

(31-22)

Now, however, this  total  energy  decreases  as  energy  is  transferred  to  thermal
energy. The rate of that transfer is, from Eq. 26-27,

dU
dt

! ’i 2R,

(31-23)

where the minus sign indicates that U decreases. By differentiating Eq. 31-22 with
respect to time and then substituting the result in Eq. 31-23, we obtain

dU
dt
Substituting dq/dt for i and d 2q/dt2 for di/dt, we obtain

dq
dt

! Li

di
dt

q
C

$

! ’i 2R.

L

d 2q
dt 2 $ R

dq
dt

$

1
C

q ! 0

(RLC circuit),

(31-24)

which is the differential equation for damped oscillations in an RLC circuit.

Charge Decay. The solution to Eq. 31-24 is

in which

q ! Qe’Rt/2L cos(v*t $ f),

(31-25)

v* !

v2 ’ (R/2L)2 ,

(31-26)

LC

v ! 1/

where
, as with an undamped oscillator. Equation 31-25 tells us how
the charge on the capacitor oscillates in a damped RLC circuit; that equation is
the  electromagnetic  counterpart  of  Eq. 15-42, which  gives  the  displacement  of
a damped block – spring oscillator.

1

2

Equation 31-25 describes a sinusoidal oscillation (the cosine function) with
an exponentially  decaying  amplitude  Qe’Rt/2L (the  factor  that  multiplies  the
cosine). The angular frequency v* of the damped oscillations is always less than
the  angular  frequency  v of  the  undamped  oscillations; however, we  shall  here
consider only situations in which R is small enough for us to replace v* with v.

Energy Decay. Let us next find an expression for the total electromagnetic
energy U of  the circuit  as  a  function  of  time. One  way  to  do  so  is  to  monitor
the energy  of the electric  field  in  the  capacitor, which  is  given  by  Eq. 31-1
(UE ! q2/2C). By substituting Eq. 31-25 into Eq. 31-1, we obtain

UE !

q2
2C

!

[Qe’Rt/2L cos(v*t $ f)]2
2C

!

Q2
2C

e’Rt/L cos2(v*t $ f).

(31-27)

Thus, the  energy  of  the  electric  field  oscillates  according  to  a  cosine-squared
term, and the amplitude of that oscillation decreases exponentially with time.
