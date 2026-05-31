31-5 POWE R  I N  ALTE R NATI NG-CU R R E NT  CI RCU ITS

927

31-5 POWER IN ALTERNATING-CURRENT CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .

31.41 For the current, voltage, and emf in an ac circuit,

31.45 For a driven RLC circuit in steady state, explain what

apply the relationship between the rms values and the
amplitudes.

31.42 For an alternating emf connected across a capacitor,
an inductor, or a resistor, sketch graphs of the sinusoidal
variation of the current and voltage and indicate the peak
and rms values.

31.43 Apply the relationship between average power Pavg,

rms current Irms, and resistance R.

happens to (a) the value of the average stored energy with
time and (b) the energy that the generator puts into the
circuit.

31.46 Apply the relationship between the power factor cos f,

the resistance R, and the impedance Z.

31.47 Apply the relationship between the average power

Pavg, the rms emf
factor cos f.

#rms

, the rms current Irms, and the power

31.44 In a driven RLC circuit, calculate the power of each

31.48 Identify what power factor is required in order to maxi-

element.

mize the rate at which energy is supplied to a resistive load.

Key Ideas
● In a series RLC circuit, the average power Pavg of the
generator is equal to the production rate of thermal energy in
the resistor:

Pavg ! I 2

rmsR ! #rmsIrms cos f.

● The abbreviation rms stands for root-mean-square; the
rms quantities are related to the maximum quantities by
Irms ! I/
V/
cos f is called the power factor of the circuit.
1

#rms ! #m /

2, Vrms !

The term

and

1

1

2.

2,

Power in Alternating-Current Circuits
In  the  RLC circuit  of  Fig. 31-7, the  source  of  energy  is  the  alternating-current
generator. Some of the energy that it provides is stored in the electric field in the
capacitor, some is stored in the magnetic field in the inductor, and some is dis-
sipated as thermal energy in the resistor. In steady-state operation, the average
stored energy remains constant. The net transfer of energy is thus from the gener-
ator to the resistor, where energy is dissipated.

The  instantaneous  rate  at  which  energy  is  dissipated  in  the  resistor  can  be

written, with the help of Eqs. 26-27 and 31-29, as

P ! i2R ! [I sin(vdt ’ f)]2R ! I 2R sin2(vdt ’ f).

(31-68)

θ

sin
+1

The average rate at which energy is dissipated in the resistor, however, is the aver-
age of Eq. 31-68 over time. Over one complete cycle, the average value of sin u,
1
where u is any variable, is zero (Fig. 31-17a) but the average value of sin2 u is
2
(Fig. 31-17b). (Note  in  Fig. 31-17b how  the  shaded  areas  under  the  curve  but
above  the  horizontal  line  marked
exactly  fill  in  the  unshaded  spaces  below
that line.) Thus, we can write, from Eq. 31-68,

$1
2

Pavg !

I 2R
2

2

! # I

2 $

R.

(31-69)

The quantity

I/

 2

is called the root-mean-square, or rms, value of the current i:

1

1

Irms !

We can now rewrite Eq. 31-69 as

I

2
1

(rms current).

(31-70)

Pavg ! I rms

2 R

(average power).

(31-71)

0

π

  π 2

3
π

θ

0

–1

(a)

θ

sin2
+1
+ 1–2
0

0

π

  π 2

π 3

θ

(b)

Figure 31-17 (a) A plot of sin u versus u.The
average value over one cycle is zero. (b) A
plot of sin2 u versus u.The average value
over one cycle is  .1
2

928

CHAPTE R  31 E LECTROMAG N ETIC  OSCI LL ATIONS  AN D  ALTE R NATI NG  CU R R E NT

Equation  31-71  has  the  same  mathematical  form  as  Eq. 26-27  (P ! i2R); the
message here is that if we switch to the rms current, we can compute the aver-
age rate of energy dissipation for alternating-current circuits just as for direct-
current circuits.

We can also define rms values of voltages and emfs for alternating-current

circuits:

Vrms !

V

2
1

#m
2
1

    and    #rms !

(rms voltage; rms emf).

(31-72)

Alternating-current  instruments, such  as  ammeters  and  voltmeters, are  usually
calibrated  to  read  Irms, Vrms, and  #rms. Thus, if  you  plug  an  alternating-current
voltmeter  into  a  household  electrical  outlet  and  it  reads  120 V, that  is  an  rms
voltage. The  maximum value  of  the  potential  difference  at  the  outlet  is
or 170 V. Generally scientists and engineers report rms values in-

2 & (120 V),

stead of maximum values.
1

Because the proportionality factor

1/

for all three variables, we can write Eqs. 31-62 and 31-60 as

2
1

in Eqs. 31-70 and 31-72 is the same

Irms !

#rms
Z

!

#rms
R2 $ (XL ’ XC)2

,

(31-73)

and, indeed, this is the form that we almost always use.

2

We  can  use  the  relationship  Irms ! #rms/Z to  recast  Eq. 31-71  in  a  useful

equivalent way. We write

Pavg !

#rms
Z

IrmsR ! #rmsIrms

R
Z

.

(31-74)

From Fig. 31-14d, Table 31-2, and Eq. 31-62, however, we see that R/Z is just the
cosine of the phase constant f:

cos f !

VR
#m

!

IR
IZ

!

R
Z

.

(31-75)

Equation 31-74 then becomes

Pavg ! #rmsIrms cos f

(average power),

(31-76)

in  which  the  term  cos  f is  called  the  power  factor. Because  cos  f ! cos(’f),
Eq. 31-76 is independent of the sign of the phase constant f.

To  maximize  the  rate  at  which  energy  is  supplied  to  a  resistive  load  in  an
RLC circuit, we should keep the power factor cos f as close to unity as possible.
This is equivalent to keeping the phase constant f in Eq. 31-29 as close to zero as
possible. If, for example, the circuit is highly inductive, it can be made less so by
putting more capacitance in the circuit, connected in series. (Recall that putting
an additional capacitance into a series of capacitances decreases the equivalent
capacitance Ceq of  the  series.) Thus, the  resulting  decrease  in  Ceq in  the  circuit
reduces the phase constant and increases the power factor in Eq. 31-76. Power
companies place series-connected capacitors throughout their transmission sys-
tems to get these results.

Checkpoint 7

(a) If the current in a sinusoidally driven series RLC circuit leads the emf, would we
increase or decrease the capacitance to increase the rate at which energy is supplied
to the resistance? (b) Would this change bring the resonant angular frequency of the
circuit closer to the angular frequency of the emf or put it farther away?

31-5 POWE R  I N  ALTE R NATI NG-CU R R E NT  CI RCU ITS

929

Sample Problem 31.07 Driven RLC circuit: power factor and average power

A  series  RLC circuit, driven  with
at  fre-
, an"
quency  fd
60.0 Hz, contains  a  resistance  R
inductance with  inductive  reactance  XL ! 80.0 ", and  a
capacitance with capacitive reactance XC ! 150 ".

#rms ! 120 V

200

!

!

(a) What are the power factor cos f and phase constant f of
the circuit?

KEY IDEA

The power factor cos f can be found from the resistance R
and impedance Z via Eq. 31-75 (cos f ! R/Z).

Calculations: To calculate Z, we use Eq. 31-61:

Z !

R2 $ (XL ’ XC)2

2

!

(200 ")2 $ (80.0 " ’ 150 ")2 ! 211.90 ".

Equation 31-75 then gives us

2

cos f !

R
Z

!

200 "
211.90 "

! 0.9438 % 0.944.

(Answer)

determined by the rms value of the driving emf and the cir-
cuit’s impedance Z (which we know), according to Eq. 31-73:

Irms !

#rms
Z

.

Substituting this into Eq. 31-76 then leads to

Pavg ! #rmsIrms cos f !

#2
rms
Z

 cos f

!

(120 V)2
211.90 "

 (0.9438) ! 64.1 W.

(Answer)

Second way: Instead, we can write

Pavg ! Irms

2 R !

2
#rms
Z2 R

!

(120 V)2
(211.90 ")2  (200 ") ! 64.1 W.
(c) What new capacitance Cnew is needed to maximize Pavg if
the other parameters of the circuit are not changed?

(Answer)

Taking the inverse cosine then yields

f ! cos’1 0.944 ! .19.3°.

KEY IDEAS

+

$

The inverse cosine on a calculator gives only the positive an-
swer here, but both  19.3 and  19.3 have a cosine of 0.944.
To  determine  which  sign  is  correct, we  must  consider
whether  the  current  leads  or  lags  the  driving  emf. Because
XC - XL, this  circuit  is  mainly  capacitive, with  the  current
leading the emf.Thus, f must be negative:

’

+

f ! ’19.3°.

(Answer)

We could, instead, have found f with Eq. 31-65. A calculator
would then have given us the answer with the minus  sign.

(b)  What  is  the  average  rate  Pavg at  which  energy  is
dissipated in the resistance?

KEY IDEAS

There  are  two  ways  and  two  ideas  to  use: (1)  Because  the
circuit is assumed to be in steady-state operation, the rate at
which energy is dissipated in the resistance is equal to the
rate  at  which  energy  is  supplied  to  the  circuit, as  given  by
Eq. 31-76  (Pavg ! #rmsIrms cos f). (2)  The  rate  at  which
energy is dissipated in a resistance R depends on the square
of  the  rms  current  Irms through  it, according  to  Eq. 31-71
(Pavg ! I 2

rms R).

First  way: We  are  given  the  rms  driving  emf  #rms and  we
already  know  cos  f from  part  (a). The  rms  current  Irms is

(1)  The  average  rate  Pavg at  which  energy  is  supplied
and dissipated  is  maximized  if  the circuit  is  brought  into
resonance  with  the  driving  emf. (2)  Resonance  occurs
when XC ! XL.

Calculations: From the given data, we have XC - XL. Thus,
we  must  decrease  XC to  reach  resonance. From  Eq. 31-39
(XC ! 1/vdC), we see that this means we must increase C to
the new value Cnew.

Using Eq. 31-39, we can write the resonance condition

XC ! XL as

1
vdCnew

! XL.

Substituting 2pfd for vd (because we are given fd and not vd)
and then solving for Cnew, we find

Cnew !

1
2p fdXL

!

1
(2p)(60 Hz)(80.0 ")

! 3.32 & 10’5 F ! 33.2 mF.

(Answer)

Following the procedure of part (b), you can show that with
Cnew, the  average  power  of  energy  dissipation  Pavg would
then be at its maximum value of

Pavg, max ! 72.0 W.

Additional examples, video, and practice available at WileyPLUS
