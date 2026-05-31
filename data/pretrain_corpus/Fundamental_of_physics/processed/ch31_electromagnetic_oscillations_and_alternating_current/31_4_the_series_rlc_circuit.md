31-4 TH E  SE R I ES  R LC CI RCU IT

921

31-4 THE SERIES RLC CIRCUIT

Learning Objectives
After reading this module, you should be able to . . .
31.32 Draw the schematic diagram of a series RLC

circuit.

phase constant f, resistance R, and reactances XL
and XC.

31.33 Identify the conditions for a mainly inductive circuit, a

31.38 Identify the values of the phase constant f correspon-

mainly capacitive circuit, and a resonant circuit.
31.34 For a mainly inductive circuit, a mainly capacitive

circuit, and a resonant circuit, sketch graphs for voltage
v(t) and current i(t) and sketch phasor diagrams, indicat-
ing leading, lagging, or resonance.

31.35 Calculate impedance Z.
31.36 Apply the relationship between current amplitude I,

impedance Z, and emf amplitude #m.

31.37 Apply the relationships between phase constant f
and voltage amplitudes VL and VC, and also between

ding to a mainly inductive circuit, a mainly capacitive
circuit, and a resonant circuit.

31.39 For resonance, apply the relationship between

the driving angular frequency vd, the natural angular
frequency v, the inductance L, and the capacitance C.
31.40 Sketch a graph of current amplitude versus the ratio
vd/v, identifying the portions corresponding to a mainly
inductive circuit, a mainly capacitive circuit, and a resonant
circuit and indicating what happens to the curve for an
increase in the resistance.

Key Ideas
● For a series RLC circuit with an external emf given by

and current given by

# ! #m sin vdt,

i ! I sin(vdt ’ f),

the current amplitude is given by

I !

!

em
R2 $ (XL ’ XC)2
#m
R2 $ (vdL ’ 1/vdC)2

1

1

(current amplitude).

● The phase constant is given by

tan f !

XL ’ XC
R

(phase constant).

● The impedance Z of the circuit is

Z !

R2 $ (XL ’ XC)2

(impedance).

● We relate the current amplitude and the impedance with

2

I ! #m /Z.

● The current amplitude I is maximum (I ! #m /R) when the
driving angular frequency vd equals the natural angular fre-
quency v of the circuit, a condition known as resonance. Then
XC ! XL, f ! 0, and the current is in phase with the emf.

The Series RLC Circuit
We are now ready to apply the alternating emf of Eq. 31-28,

# ! #m sin vdt

(applied emf),

(31-55)

to the full RLC circuit of Fig. 31-7. Because R, L, and C are in series, the same
current

i ! I sin(vdt ’ f)

(31-56)

is  driven  in  all  three  of  them. We  wish  to  find  the  current  amplitude  I and  the
phase constant f and to investigate how these quantities depend on the driving
angular frequency vd. The solution is simplified by the use of phasor diagrams as
introduced for the three basic circuits of Module 31-3: capacitive load, inductive
load, and resistive load. In particular we shall make use of how the voltage phasor
is related to the current phasor for each of those basic circuits. We shall find that
series RLC circuits can be separated into three types: mainly capacitive circuits,
mainly inductive circuits, and circuits that are in resonance.

922

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

The Current Amplitude
We  start  with  Fig. 31-14a, which  shows  the  phasor  representing  the  current  of
Eq. 31-56  at  an  arbitrary  time  t. The  length  of  the  phasor  is  the  current  ampli-
tude I, the projection of the phasor on the vertical axis is the current i at time t, and
the angle of rotation of the phasor is the phase vdt ’ f of the current at time t.

Figure 31-14b shows the phasors representing the voltages across R, L, and C
at  the  same  time  t. Each  phasor  is  oriented  relative  to  the  angle  of  rotation  of
current phasor I in Fig. 31-14a, based on the information in Table 31-2:

Resistor: Here current and voltage are in phase; so the angle of rotation of volt-

age phasor VR is the same as that of phasor I.

Capacitor: Here current leads voltage by 90°; so the angle of rotation of voltage

phasor VC is 90+ less than that of phasor I.

Inductor: Here  current  lags  voltage  by  90°; so  the  angle  of  rotation  of  voltage

phasor vL is 90+ greater than that of phasor I.

Figure 31-14b also shows the instantaneous voltages vR, vC, and vL across R, C,
and L at time t; those voltages are the projections of the corresponding phasors
on the vertical axis of the figure.

Figure 31-14c shows the phasor representing the applied emf of Eq. 31-55.
The length of the phasor is the emf amplitude #m, the projection of the phasor
on the vertical axis is the emf # at time t, and the angle of rotation of the phasor is
the phase vdt of the emf at time t.

From the loop rule we know that at any instant the sum of the voltages vR, vC,

and vL is equal to the applied emf #:

# ! vR $ vC $ vL.

(31-57)

Thus, at time t the projection # in Fig. 31-14c is equal to the algebraic sum of the
projections vR, vC, and vL in Fig. 31-14b. In fact, as the phasors rotate together, this
equality always holds. This means that phasor #m in Fig. 31-14c must be equal to
the vector sum of the three voltage phasors VR, VC, and VL in Fig. 31-14b.

That requirement is indicated in Fig. 31-14d, where phasor #m is drawn as the
sum of phasors VR, VL, and VC. Because phasors VL and VC have opposite direc-
tions  in  the  figure, we  simplify  the  vector  sum  by  first  combining  VL and VC to
form the single phasor VL ’ VC. Then we combine that single phasor with VR to
find the net phasor. Again, the net phasor must coincide with phasor #m, as shown.

i

I

 – ω
dt

φ

This is ahead
of I by 90º.

VL

(a)

vR

vL

vC

This is in
phase with I.
VR

φ – ωdt

VC

m

m

ωdt

(c)

φ

This    is the angle
between I and the
driving emf.

φ

VR
φ – ωdt

ωdt

VL – VC

(b)

This is behind
I by 90º.

(d)

Figure 31-14 (a) A phasor representing the
alternating current in the driven RLC cir-
cuit of Fig. 31-7 at time t. The amplitude I,
the instantaneous value i, and the phase
(vdt ’ f) are shown. (b) Phasors repre-
senting the voltages across the inductor,
resistor, and capacitor, oriented with re-
spect to the current phasor in (a). (c) A
phasor representing the alternating emf
that drives the current of (a). (d) The emf
phasor is equal to the vector sum of the
three voltage phasors of (b). Here, voltage
phasors VL and VC have been added vecto-
rially to yield their net phasor (VL ’ VC).

Both  triangles  in  Fig. 31-14d are  right  triangles. Applying  the  Pythagorean

theorem to either one yields

31-4 TH E  SE R I ES  R LC CI RCU IT

923

#m

2 ! VR

2 $ (VL ’ VC)2.

(31-58)

From  the  voltage  amplitude  information  displayed  in  the  rightmost  column  of
Table 31-2, we can rewrite this as

# m

2 ! (IR)2 $ (IXL ’ IXC)2,

(31-59)

and then rearrange it to the form

#m
R2 $ (XL ’ XC)2
The denominator in Eq. 31-60 is called the impedance Z of the circuit for the

(31-60)

I !

2

.

driving angular frequency vd:

Z !

R2 $ (XL ’ XC)2

(impedance defined).

(31-61)

We can then write Eq. 31-60 as

2

I !

#m
Z

.

(31-62)

If  we  substitute  for  XC and XL from  Eqs. 31-39  and  31-49, we  can  write

Eq. 31-60 more explicitly as

I !

em
R2 $ (vdL ’ 1/vdC)2

(current amplitude).

(31-63)

2

We have now accomplished half our goal: We have obtained an expression
for the current amplitude I in terms of the sinusoidal driving emf and the circuit
elements in a series RLC circuit.

The  value  of  I depends  on  the  difference  between  vdL and  1/vdC in
Eq. 31-63  or, equivalently, the  difference  between  XL and XC in  Eq. 31-60. In
either equation, it does not matter which of the two quantities is greater because
the difference is always squared.

The current that we have been describing in this module is the steady-state
current that  occurs  after  the  alternating  emf  has  been  applied  for  some
time. When  the  emf  is  first  applied  to  a  circuit, a  brief  transient  current
occurs. Its  duration  (before  settling  down  into  the  steady-state  current)  is
determined by the time constants tL ! L/R and tC ! RC as the inductive and
capacitive elements “turn on.” This transient current can, for example, destroy
a  motor  on  start-up  if  it  is  not  properly  taken  into  account  in  the  motor’s
circuit design.

The Phase Constant
From the right-hand phasor triangle in Fig. 31-14d and from Table 31-2 we can
write

tan , !

VL ’ VC
VR

!

IXL ’ IXC
IR

,

(31-64)

which gives us

tan f !

XL ’ XC
R

(phase constant).

(31-65)

This is the other half of our goal: an equation for the phase constant f in the si-
nusoidally driven series RLC circuit of Fig. 31-7. In essence, it gives us three dif-

924

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

ferent  results  for  the  phase  constant, depending  on  the  relative  values  of  the
reactances XL and XC:

XL - XC: The circuit is said to be more inductive than capacitive. Equation 31-65
tells us that f is positive for such a circuit, which means that phasor I rotates
behind  phasor  #m (Fig. 31-15a). A  plot  of # and i versus  time  is  like  that  in
Fig. 31-15b. (Figures 31-14c and d were drawn assuming XL - XC.)

XC - XL: The circuit is said to be more capacitive than inductive. Equation 31-65
tells us that f is negative for such a circuit, which means that phasor I rotates
ahead of phasor #m (Fig. 31-15c). A plot of # and i versus time is like that in
Fig. 31-15d.

XC ! XL: The  circuit  is  said  to  be  in  resonance, a  state  that  is  discussed  next.
Equation 31-65 tells us that f ! 0+ for such a circuit, which means that phasors
#m and I rotate together (Fig. 31-15e). A plot of # and i versus time is like that
in Fig. 31-15f.

As illustration, let us reconsider two extreme circuits: In the purely inductive
circuit of Fig. 31-12, where XL is nonzero and XC ! R ! 0, Eq. 31-65 tells us that
the circuit’s phase constant is f ! $90+ (the greatest value of f), consistent with
Fig. 31-13b. In the purely capacitive circuit of Fig. 31-10, where XC is nonzero and
XL ! R ! 0, Eq. 31-65 tells us that the circuit’s phase constant is f ! ’90+ (the
least value of f), consistent with Fig. 31-11b.

Resonance
Equation 31-63 gives the current amplitude I in an RLC circuit as a function of
the  driving  angular  frequency  vd of  the  external  alternating  emf. For  a  given
resistance R, that amplitude is a maximum when the quantity vdL ’ 1/vdC in the

φ

Positive    means that the
current lags the emf (ELI ):
the phasor is vertical later
and the curve peaks later.

m

I

(a)

(b)

φ

Negative    means that the
current leads the emf (ICE ) :
the phasor is vertical earlier
and the curve peaks earlier.

I

m

Figure 31-15 Phasor diagrams and
graphs of the alternating emf # and
current i for the driven RLC circuit
of Fig. 31-7. In the phasor diagram of
(a) and the graph of (b), the current i
lags the driving emf # and the cur-
rent’s phase constant f is positive. In
(c) and (d), the current i leads the
driving emf # and its phase constant
f is negative. In (e) and ( f ), the cur-
rent i is in phase with the driving emf
# and its phase constant f is zero.

(c)

(d)

φ

Zero   means that the current
and emf are in phase: the
phasors are vertical together
and the curves peak together.

m

I

(e)

( f )

Positive φ

i

Negative φ

i

i

Zero φ

, i

I

m

, i

I

m

, i

I

m

t

t

t

31-4 TH E  SE R I ES  R LC CI RCU IT

925

ω

ωd

Driving       equal to natural
• high current amplitude
• circuit is in resonance
• equally capacitive and inductive
• XC equals XL
• current and emf in phase
• zero

φ

A

m

I

Figure 31-16 Resonance curves for the
driven RLC circuit of Fig. 31-7 with
L ! 100 mH, C ! 100 pF, and three
values of R. The current amplitude I of
the alternating current depends on how
close the driving angular frequency vd is
to the natural angular frequency v. The
horizontal arrow on each curve meas-
ures the curve’s half-width, which is the
width at the half-maximum level and is
a measure of the sharpness of the reso-
nance. To the left of vd/v ! 1.00, the cir-
cuit is mainly capacitive, with XC - XL;
to the right, it is mainly inductive, with
XL - XC.

I

m

I

e
d
u
t
i
l

p
m
a

t
n
e
r
r
u
C

R = 10 Ω

R = 30 Ω

R = 100 Ω

0.90

0.95

1.00
ωd/ω

1.05

1.10

ωd

Low driving
• low current amplitude
• ICE side of the curve
• more capacitive
• XC is greater
• current leads emf
• negative

φ

ωd

High driving
• low current amplitude
• ELI side of the curve
• more inductive
• XL is greater
• current lags emf
• positive

φ

m

I

denominator is zero — that is, when

vdL !

1
vdC

or

vd !

1
LC

(maximum I).

(31-66)

LC,

Because  the  natural  angular  frequency  v of  the  RLC circuit  is  also  equal  to
the  maximum  value  of  I occurs  when  the  driving  angular  frequency
1/
matches the natural angular frequency — that is, at resonance. Thus, in an RLC
circuit, resonance and maximum current amplitude I occur when

1

1

vd ! v !

1
LC

(resonance).

(31-67)

1

Resonance  Curves. Figure  31-16  shows  three  resonance  curves for  sinu-
soidally driven oscillations in three series RLC circuits differing only in R. Each
curve peaks at its maximum current amplitude I when the ratio vd/v is 1.00, but
the maximum value of I decreases with increasing R. (The maximum I is always
#m/R; to  see  why, combine  Eqs. 31-61  and  31-62.)  In  addition, the  curves  in-
crease in width (measured in Fig. 31-16 at half the maximum value of I ) with
increasing R.

926

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

To make physical sense of Fig. 31-16, consider how the reactances XL and
XC change as we increase the driving angular frequency vd, starting with a value
much less than the natural frequency v. For small vd, reactance XL (! vdL) is
small and reactance XC (! 1/vdC) is large. Thus, the circuit is mainly capacitive
and the impedance is dominated by the large XC, which keeps the current low.
As we increase vd, reactance XC remains dominant but decreases while reac-
tance XL increases. The  decrease  in  XC decreases  the  impedance, allowing  the
current to increase, as we see on the left side of any resonance curve in Fig. 31-16.
When the increasing XL and the decreasing XC reach equal values, the current is
greatest and the circuit is in resonance, with vd ! v.

As  we  continue  to  increase  vd, the  increasing  reactance  XL becomes  pro-
gressively  more  dominant  over  the  decreasing  reactance  XC. The  impedance
increases  because  of  XL and  the  current  decreases, as  on  the  right  side  of  any
resonance curve in Fig. 31-16. In summary, then: The low-angular-frequency side
of a resonance curve is dominated by the capacitor’s reactance, the high-angular-
frequency side is dominated by the inductor’s reactance, and resonance occurs in
the middle.

Checkpoint 6

Here are the capacitive reactance and inductive reactance, respectively, for three
sinusoidally driven series RLC circuits: (1) 50 ", 100 "; (2) 100 ", 50 "; (3) 50 ", 50 ".
(a) For each, does the current lead or lag the applied emf, or are the two in phase?
(b) Which circuit is in resonance?

Sample Problem 31.06 Current amplitude, impedance, and phase constant

let  R ! 200 ", C ! 15.0 mF, L ! 230 mH,
In  Fig. 31-7,
fd ! 60.0 Hz, and #m ! 36.0 V. (These parameters are those
used in the earlier sample problems.)

(a) What is the current amplitude I?

KEY IDEA

The current amplitude I depends on the amplitude #m of the
driving emf and on the impedance Z of the circuit, accord-
ing to Eq. 31-62 (I ! #m/Z).

Calculations: So, we need to find Z, which depends on resis-
tance R, capacitive reactance XC, and inductive reactance XL.
The circuit’s resistance is the given resistance R. Its capacitive
reactance is due to the given capacitance and, from an earlier
sample problem, XC ! 177 ". Its inductive reactance is due
to the given inductance and, from another sample problem,
XL ! 86.7 ".Thus, the circuit’s impedance is

Z !

R2 $ (XL ’ XC)2

!

2

(200 ")2 $ (86.7 " ’ 177 ")2

2
! 219 ".

We then find

I !

#m
Z

!

36.0 V
219 "

! 0.164 A.

(Answer)

(b)  What  is  the  phase  constant  f of  the  current  in  the
circuit relative to the driving emf?

KEY IDEA

The phase constant depends on the inductive reactance, the
capacitive  reactance, and  the  resistance  of  the  circuit,
according to Eq. 31-65.

Calculation: Solving Eq. 31-65 for f leads to

f ! tan’1 XL ’ XC

R

! tan’1 86.7 " ’ 177 "

200 "

! ’24.3+ ! ’0.424 rad.

(Answer)

The negative phase constant is consistent with the fact that
the load is mainly capacitive; that is, XC - XL. In the com-
mon mnemonic for driven series RLC circuits, this circuit is
an ICE circuit — the current leads the driving emf.

Additional examples, video, and practice available at WileyPLUS
