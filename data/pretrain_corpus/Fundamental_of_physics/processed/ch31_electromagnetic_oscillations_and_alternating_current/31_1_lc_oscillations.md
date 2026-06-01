C H A

P

T

E

R

3

1

Electromagnetic Oscillations
and Alternating Current

31-1 LC OSCILLATIONS

Learning Objectives
After reading this module, you should be able to . . .
31.01 Sketch an LC oscillator and explain which quantities

oscillate and what constitutes one period of the oscillation.

31.02 For an LC oscillator, sketch graphs of the potential
difference across the capacitor and the current through
the inductor as functions of time, and indicate the period
T on each graph.

31.03 Explain the analogy between a block–spring oscillator

and an LC oscillator.

31.04 For an LC oscillator, apply the relationships between
the angular frequency v (and the related frequency f
and period T ) and the values of the inductance and
capacitance.

31.05 Starting with the energy of a block–spring system,

explain the derivation of the differential equation for charge
q in an LC oscillator and then identify the solution for q(t).
31.06 For an LC oscillator, calculate the charge q on the ca-
pacitor for any given time and identify the amplitude Q of
the charge oscillations.

Key Ideas
● In an oscillating LC circuit, energy is shuttled periodically
between the electric field of the capacitor and the magnetic
field of the inductor; instantaneous values of the two forms of
energy are

UE !

q2
2C

    and    UB !

Li2
2

,

where q is the instantaneous charge on the capacitor and i is
the instantaneous current through the inductor.
● The total energy U (! UE $ UB) remains constant.
● The principle of conservation of energy leads to

L

d 2q
dt 2 $

1
C

q ! 0

(LC oscillations)

as the differential equation of LC oscillations (with no
resistance).

31.07 Starting from the equation giving the charge q(t)

on the capacitor in an LC oscillator, find the current i(t)
in the inductor as a function of time.

31.08 For an LC oscillator, calculate the current i in the

inductor for any given time and identify the amplitude I
of the current oscillations.

31.09 For an LC oscillator, apply the relationship between
the charge amplitude Q, the current amplitude I, and the
angular frequency v.

31.10 From the expressions for the charge q and the current
i in an LC oscillator, find the magnetic field energy UB(t)
and the electric field energy UE(t) and the total energy.
31.11 For an LC oscillator, sketch graphs of the magnetic

field energy UB(t), the electric field energy UE(t), and the
total energy, all as functions of time.

31.12 Calculate the maximum values of the magnetic field
energy UB and the electric field energy UE and also
calculate the total energy.

● The solution of this differential equation is

q ! Q cos(vt $ f)

(charge),

in which Q is the charge amplitude (maximum charge
on the capacitor) and the angular frequency v of the
oscillations is

v !

1
LC

.

1
● The phase constant f is determined by the initial conditions
(at t ! 0) of the system.
● The current i in the system at any time t is

i ! ’vQ sin(vt $ f)

(current),

in which vQ is the current amplitude I.

903

904

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

What Is Physics?
We  have  explored  the  basic  physics  of  electric  and  magnetic  fields  and  how
energy can be stored in capacitors and inductors. We next turn to the associated
applied physics, in which the energy stored in one location can be transferred to
another location so that it can be put to use. For example, energy produced at a
power plant can show up at your home to run a computer. The total worth of this
applied  physics  is  now  so  high  that  its  estimation  is  almost  impossible. Indeed,
modern civilization would be impossible without this applied physics.

In  most  parts  of  the  world, electrical  energy  is  transferred  not  as  a  direct
current but as a sinusoidally oscillating current (alternating current, or ac). The
challenge to both physicists and engineers is to design ac systems that transfer
energy efficiently and to build appliances that make use of that energy. Our first
step here is to study the oscillations in a circuit with inductance L and capacitance C.

LC Oscillations, Qualitatively
Of the three circuit elements, resistance R, capacitance C, and inductance L, we have
so far discussed the series combinations RC (in Module 27-4) and RL (in Module
30-6). In these two kinds of circuit we found that the charge, current, and potential
difference grow and decay exponentially. The time scale of the growth or decay is
given by a time constant t, which is either capacitive or inductive.

We now examine the remaining two-element circuit combination LC. You will
see that in this case the charge, current, and potential difference do not decay expo-
nentially with time but vary sinusoidally (with period T and angular frequency v).
The resulting oscillations of the capacitor’s electric field and the inductor’s magnetic
field are said to be electromagnetic oscillations. Such a circuit is said to oscillate.

Parts a through h of Fig. 31-1 show succeeding stages of the oscillations in
a simple LC circuit. From Eq. 25-21, the energy stored in the electric field of the

Figure 31-1 Eight stages in a single cycle of
oscillation of a resistanceless LC circuit.
The bar graphs by each figure show the
stored magnetic and electrical energies. The
magnetic field lines of the inductor and the
electric field lines of the capacitor are
shown. (a) Capacitor with maximum
charge, no current. (b) Capacitor discharg-
ing, current increasing. (c) Capacitor fully
discharged, current maximum. (d)
Capacitor charging but with polarity
opposite that in (a), current decreasing. (e)
Capacitor with maximum charge having
polarity opposite that in (a), no current. (f )
Capacitor discharging, current increasing
with direction opposite that in (b). (g)
Capacitor fully discharged, current
maximum. (h) Capacitor charging, current
decreasing.

UB

UE

i

L

C
++

–

–

UB

UE
max i

L

C

L

UB

UE

i

C
–

–

++

i = 0

L

C
+  + +
+

–
–  –
–

(a )

i

L

UB

UE

Entirely
electrical
energy

C
++

–

–

(b )

(c )

Entirely
magnetic
energy

(d )

i = 0

L

max i

L

C

L

i

C
–

–

++

UB

UE

(h )

UB

UE

(g )

Entirely
magnetic
energy

UB

UE

(f )

C
–  – –
–

+  + +
+

(e )

UB

UE

Entirely
electrical
energy

31-1 LC OSCI LL ATIONS

905

capacitor at any time is

UE !

q2
2C

,

(31-1)

where q is the charge on the capacitor at that time. From Eq. 30-49, the energy
stored in the magnetic field of the inductor at any time is

UB !

Li 2
2

,

(31-2)

where i is the current through the inductor at that time.

We  now  adopt  the  convention  of  representing  instantaneous  values of  the
electrical  quantities  of  a  sinusoidally  oscillating  circuit  with  small  letters, such
as q, and the amplitudes of those quantities with capital letters, such as Q. With
this convention in mind, let us assume that initially the charge q on the capac-
itor in  Fig. 31-1  is  at  its  maximum  value  Q and  that  the  current  i through  the
inductor  is  zero. This  initial  state  of  the  circuit  is  shown  in  Fig. 31-1a. The  bar
graphs for energy included there indicate that at this instant, with zero current
through the inductor and maximum charge on the capacitor, the energy UB of the
magnetic field is zero and the energy UE of the electric field is a maximum. As the
circuit oscillates, energy shifts back and forth from one type of stored energy to
the other, but the total amount is conserved.

The capacitor now starts to discharge through the inductor, positive charge
carriers moving counterclockwise, as shown in Fig. 31-1b. This means that a cur-
rent i, given  by  dq/dt and  pointing  down  in  the  inductor, is  established. As  the
capacitor’s  charge  decreases, the  energy  stored  in  the  electric  field  within  the
capacitor  also  decreases. This  energy  is  transferred  to  the  magnetic  field  that
appears around the inductor because of the current  i that is building up there.
Thus, the  electric  field  decreases  and  the  magnetic  field  builds  up  as  energy  is
transferred from the electric field to the magnetic field.

The capacitor eventually loses all its charge (Fig. 31-1c) and thus also loses its
electric field and the energy stored in that field. The energy has then been fully
transferred  to  the  magnetic  field  of  the  inductor. The  magnetic  field  is  then  at
its maximum  magnitude, and  the  current  through  the  inductor  is  then  at  its
maximum value I.

Although  the  charge  on  the  capacitor  is  now  zero, the  counterclockwise
current must continue because the inductor does not allow it to change suddenly
to zero. The current continues to transfer positive charge from the top plate to
the  bottom  plate  through  the  circuit  (Fig. 31-1d). Energy  now  flows  from  the
inductor  back  to  the  capacitor  as  the  electric  field  within  the  capacitor  builds
up again. The  current  gradually  decreases  during  this  energy  transfer. When,
eventually, the  energy  has  been  transferred  completely  back  to  the  capacitor
(Fig. 31-1e), the  current  has  decreased  to  zero  (momentarily). The  situation
of Fig. 31-1e is like the initial situation, except that the capacitor is now charged
oppositely.

The capacitor then starts to discharge again but now with a clockwise current
(Fig. 31-1f ). Reasoning as before, we see that the clockwise current builds to a
maximum (Fig. 31-1g) and then decreases (Fig. 31-1h), until the circuit eventually
returns  to  its  initial  situation  (Fig. 31-1a). The  process  then  repeats  at  some
frequency f and thus at an angular frequency v ! 2pf. In the ideal LC circuit with
no resistance, there are no energy transfers other than that between the electric
field of the capacitor and the magnetic field of the inductor. Because of the con-
servation  of  energy, the  oscillations  continue  indefinitely. The  oscillations  need
not begin with the energy all in the electric field; the initial situation could be any
other stage of the oscillation.

906

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

Courtesy Agilent Technologies
Figure 31-3 An oscilloscope trace showing
how the oscillations in an RLC circuit actu-
ally die away because energy is dissipated in
the resistor as thermal energy.

Figure 31-2 (a) The potential difference
across the capacitor in the circuit of Fig. 31-1 as a
function of time.This quantity is proportional to
the charge on the capacitor. (b) A potential pro-
portional to the current in the circuit of Fig. 31-1.
The letters refer to the correspondingly labeled
oscillation stages in Fig. 31-1.

)
C
/
q
=
(

C

v

)
R

i
=
(

R
v

(a)

(b)

a

c

 e

 g

 a

c

 e

 g

t

t

To determine the charge q on the capacitor as a function of time, we can put
in a voltmeter to measure the time-varying potential difference (or voltage) vC
that exists across the capacitor C. From Eq. 25-1 we can write

vC ! # 1

C $ q,

which allows us to find q. To measure the current, we can connect a small resis-
tance R in series with the capacitor and inductor and measure the time-varying
potential difference vR across it; vR is proportional to i through the relation

vR ! iR.

We assume here that R is so small that its effect on the behavior of the circuit is
negligible. The variations in time of vC and vR, and thus of q and i, are shown in
Fig. 31-2. All four quantities vary sinusoidally.

In an actual LC circuit, the oscillations will not continue indefinitely because
there  is  always  some  resistance  present  that  will  drain  energy  from  the  elec-
tric and  magnetic  fields  and  dissipate  it  as  thermal  energy  (the  circuit  may
become  warmer). The  oscillations, once  started, will  die  away  as  Fig. 31-3  sug-
gests. Compare this figure with Fig. 15-17, which shows the decay of mechanical
oscillations caused by frictional damping in a block – spring system.

Checkpoint 1

A charged capacitor and an inductor are connected in series at time t ! 0. In terms
of the period T of the resulting oscillations, determine how much later the following
reach their maximum value: (a) the charge on the capacitor; (b) the voltage across
the capacitor, with its original polarity; (c) the energy stored in the electric field; and
(d) the current.

The Electrical–Mechanical Analogy
Let  us  look  a  little  closer  at  the  analogy  between  the  oscillating  LC system  of
Fig. 31-1  and  an  oscillating  block – spring  system. Two  kinds  of  energy  are
involved in the block – spring system. One is potential energy of the compressed
or extended spring; the other is kinetic energy of the moving block. These two
energies are given by the formulas in the first energy column in Table 31-1.

Table 31-1 Comparison of the Energy in Two Oscillating Systems

Block – Spring System

LC Oscillator

Element

Energy

Element

Energy

Spring

Block

Potential,

1
2kx2
1
2mv2

Kinetic,

v ! dx/dt

Capacitor

Electrical,

Inductor

Magnetic,

1
2(1/C)q2
1
2Li 2

i ! dq/dt

31-1 LC OSCI LL ATIONS

907

The  table  also  shows, in  the  second  energy  column, the  two  kinds  of  energy
involved  in  LC oscillations. By  looking  across  the  table, we  can  see  an  analogy
between  the  forms  of  the  two  pairs  of  energies — the  mechanical  energies  of  the
block – spring  system  and  the  electromagnetic  energies  of  the  LC oscillator. The
equations for v and i at the bottom of the table help us see the details of the analogy.
They tell us that q corresponds to x and i corresponds to v (in both equations, the
former is differentiated to obtain the latter). These correspondences then suggest
that, in the energy expressions, 1/C corresponds to k and L corresponds to m. Thus,

q corresponds to x,
1/C corresponds to k,
i corresponds to v, and L corresponds to m.

These correspondences suggest that in an LC oscillator, the capacitor is mathemat-
ically like the spring in a block – spring system and the inductor is like the block.

In Module 15-1 we saw that the angular frequency of oscillation of a (fric-

tionless) block – spring system is

v !

k
m

(block – spring system).

(31-3)

The correspondences listed above suggest that to find the angular frequency of
oscillation for an ideal (resistanceless) LC circuit, k should be replaced by 1/C
and m by L, yielding

A

v !

1
LC

1

(LC circuit).

(31-4)

LC Oscillations, Quantitatively
Here  we  want  to  show  explicitly  that  Eq. 31-4  for  the  angular  frequency  of  LC
oscillations is correct. At the same time, we want to examine even more closely the
analogy between LC oscillations and block – spring oscillations. We start by extend-
ing somewhat our earlier treatment of the mechanical block – spring oscillator.

The Block–Spring Oscillator
We analyzed block – spring oscillations in Chapter 15 in terms of energy transfers
and did not — at that early stage — derive the fundamental differential equation
that governs those oscillations. We do so now.

We can write, for the total energy U of a block–spring oscillator at any instant,

U ! Ub $ Us ! 1

2 mv2 $ 1

2 kx2,

(31-5)

where Ub and Us are, respectively, the kinetic energy of the moving block and the
potential energy of the stretched or compressed spring. If there is no friction —
which we assume — the total energy U remains constant with time, even though
v and x vary. In more formal language, dU/dt ! 0. This leads to

dU
dt

!

d
dt

2 mv2 $ 1
 (1

2 kx2) ! mv

dv
dt

$ kx

dx
dt

! 0.

(31-6)

Substituting v ! dx/dt and dv/dt ! d 2x/dt2, we find

m

d 2x
dt 2 $ kx ! 0

(block – spring oscillations).

(31-7)

Equation 31-7 is the fundamental differential equation that governs the friction-
less block – spring oscillations.

The general solution to Eq. 31-7 is (as we saw in Eq. 15-3)

x ! X cos(vt $ f)

(displacement),

(31-8)

908

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

in which X is the amplitude of the mechanical oscillations (xm in Chapter 15), v is
the angular frequency of the oscillations, and f is a phase constant.

The LC Oscillator
Now  let  us  analyze  the  oscillations  of  a  resistanceless  LC circuit, proceeding
exactly as we just did for the block – spring oscillator. The total energy U present
at any instant in an oscillating LC circuit is given by

U ! UB $ UE !

Li 2
2

$

q2
2C

,

(31-9)

in which UB is the energy stored in the magnetic field of the inductor and UE is the
energy stored in the electric field of the capacitor. Since we have assumed the cir-
cuit resistance to be zero, no energy is transferred to thermal energy and U remains
constant with time. In more formal language, dU/dt must be zero.This leads to

q2
2C $ ! Li
However, i ! dq/dt and di/dt ! d 2q/dt2. With these substitutions, Eq. 31-10 becomes

dt # Li 2

dU
dt

(31-10)

dq
dt

di
dt

! 0.

q
C

$

!

$

d

2

L

d 2q
dt 2 $

1
C

q ! 0

(LC oscillations).

(31-11)

This is the differential equation that describes the oscillations of a resistanceless
LC circuit. Equations 31-11 and 31-7 are exactly of the same mathematical form.

Charge and Current Oscillations
Since the differential equations are mathematically identical, their solutions must
also be mathematically identical. Because q corresponds to x, we can write the
general solution of Eq. 31-11, by analogy to Eq. 31-8, as

q ! Q cos(vt $ f)

(charge),

(31-12)

where Q is the amplitude of the charge variations, v is the angular frequency of
the electromagnetic oscillations, and f is the phase constant. Taking the first de-
rivative of Eq. 31-12 with respect to time gives us the current:

i !

dq
dt

! ’vQ sin(vt $ f)

(current).

(31-13)

The amplitude I of this sinusoidally varying current is

and so we can rewrite Eq. 31-13 as

I ! vQ,

i ! ’I sin(vt $ f).

(31-14)

(31-15)

Angular Frequencies
We can test whether Eq. 31-12 is a solution of Eq. 31-11 by substituting Eq. 31-12
and its second derivative with respect to time into Eq. 31-11. The first derivative
of Eq. 31-12 is Eq. 31-13. The second derivative is then

d 2q
dt 2 ! ’v2Q cos(vt $ f).
Substituting for q and d 2q/dt2 in Eq. 31-11, we obtain

’Lv2Q cos(vt $ f) $

1
C

Q cos(vt $ f) ! 0.

31-1 LC OSCI LL ATIONS

909

Canceling Q cos(vt $ f) and rearranging lead to

v !

1
LC

.

1

1
Thus, Eq. 31-12  is  indeed  a  solution  of  Eq. 31-11  if  v has  the  constant  value
. Note  that  this  expression  for  v is  exactly  that  given  by  Eq. 31-4.
LC
1/
The phase constant f in Eq. 31-12 is determined by the conditions that exist
at any certain time — say, t ! 0. If the conditions yield f ! 0 at t ! 0, Eq. 31-12
requires that q ! Q and Eq. 31-13 requires that i ! 0; these are the initial con-
ditions represented by Fig. 31-1a.

Q2
2C

y
g
r
e
n
E

The electrical and magnetic
energies vary but the total
is constant.

U (= UB + UE )

UE (t)

UB (t)

Electrical and Magnetic Energy Oscillations
The electrical energy stored in the LC circuit at time t is, from Eqs. 31-1 and 31-12,

0

T/2

T

Time

UE !

q2
2C

!

Q2
2C

 cos2(vt $ f).

(31-16)

The magnetic energy is, from Eqs. 31-2 and 31-13,

Figure 31-4 The stored magnetic energy and
electrical energy in the circuit of Fig. 31-1
as a function of time. Note that their sum
remains constant. T is the period of
oscillation.

UB ! 1

2Li 2 ! 1

2Lv2Q2 sin2(vt $ f).

Substituting for v from Eq. 31-4 then gives us

UB !

Q2
2C

 sin2(vt $ f).

(31-17)

Figure 31-4 shows plots of UE(t) and UB(t) for the case of f ! 0. Note that

1. The maximum values of UE and UB are both Q2/2C.
2. At any instant the sum of UE and UB is equal to Q2/2C, a constant.
3. When UE is maximum, UB is zero, and conversely.

Checkpoint 2

A capacitor in an LC oscillator has a maximum potential difference of 17 V and a
maximum energy of 160 mJ. When the capacitor has a potential difference of 5 V and
an energy of 10 mJ, what are (a) the emf across the inductor and (b) the energy stored
in the magnetic field?

Sample Problem 31.01 LC oscillator: potential change, rate of current change

A 1.5 mF capacitor is charged to 57 V by a battery, which is
then removed. At time t ! 0, a 12 mH coil is connected in se-
ries with the capacitor to form an LC oscillator (Fig. 31-1).

(a) What is the potential difference vL(t) across the inductor
as a function of time?

KEY IDEAS

(1) The current and potential differences of the circuit (both
the  potential  difference  of  the  capacitor  and  the  potential
difference  of  the  coil)  undergo  sinusoidal  oscillations.
(2) We  can  still  apply  the  loop  rule  to  these  oscillating
potential  differences, just  as  we  did  for  the  nonoscillating
circuits of Chapter 27.

Calculations: At any time t during the oscillations, the loop
rule and Fig. 31-1 give us

vL(t) ! vC(t);

(31-18)

that is, the potential difference vL across the inductor must
always  be  equal  to  the  potential  difference  vC across  the
capacitor, so  that  the  net  potential  difference  around  the
circuit  is  zero. Thus, we  will  find  vL(t)  if  we  can  find  vC(t),
and we can find vC(t) from q(t) with Eq. 25-1 (q ! CV).

Because  the  potential  difference  vC(t)  is  maximum
when the oscillations begin at time t ! 0, the charge q on the
capacitor must also be maximum then. Thus, phase constant
f must be zero; so Eq. 31-12 gives us

q ! Q cos vt.

(31-19)
