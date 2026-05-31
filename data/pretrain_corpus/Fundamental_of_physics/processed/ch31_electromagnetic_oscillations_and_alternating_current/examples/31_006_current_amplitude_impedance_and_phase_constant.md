Sample Problem 31.06
Current amplitude, impedance, and phase constant
In Fig. 31-7, let R ! 200 ", C ! 15.0 mF, L ! 230 mH,
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
XL ! 86.7 ".Thus,the circuit’s impedance is
! 219 ".
! 2(200 ")2 $ (86.7 " ' 177 ")2
Z ! 2R2 $ (XL ' XC)2
Additional examples, video, and practice available at WileyPLUS
To make physical sense of Fig. 31-16, consider how the reactances XL and
XC change as we increase the driving angular frequency vd, starting with a value
much less than the natural frequency v. For small vd, reactance XL (! vdL) is
small and reactance XC (! 1/vdC) is large. Thus, the circuit is mainly capacitive
and the impedance is dominated by the large XC, which keeps the current low.
As we increase vd, reactance XC remains dominant but decreases while reac-
tance XL increases. The decrease in XC decreases the impedance, allowing the
current to increase, as we see on the left side of any resonance curve in Fig. 31-16.
When the increasing XL and the decreasing XC reach equal values, the current is
greatest and the circuit is in resonance, with vd ! v.
As we continue to increase vd, the increasing reactance XL becomes pro-
gressively more dominant over the decreasing reactance XC. The impedance
increases because of XL and the current decreases, as on the right side of any
resonance curve in Fig. 31-16. In summary, then: The low-angular-frequency side
of a resonance curve is dominated by the capacitor’s reactance, the high-angular-
frequency side is dominated by the inductor’s reactance, and resonance occurs in
the middle.
Checkpoint 6
Here are the capacitive reactance and inductive reactance, respectively, for three
sinusoidally driven series RLC circuits: (1) 50 ", 100 "; (2) 100 ", 50 "; (3) 50 ", 50 ".
(a) For each, does the current lead or lag the applied emf, or are the two in phase?
(b) Which circuit is in resonance?

927
31-5 POWER IN ALTERNATING-CURRENT CIRCUITS
31-5 POWER IN ALTERNATING-CURRENT CIRCUITS
After reading this module, you should be able to . . .
31.41 For the current, voltage, and emf in an ac circuit,
apply the relationship between the rms values and the
amplitudes.
31.42 For an alternating emf connected across a capacitor,
an inductor, or a resistor, sketch graphs of the sinusoidal
variation of the current and voltage and indicate the peak
and rms values.
31.43 Apply the relationship between average power Pavg,
rms current Irms, and resistance R.
31.44 In a driven RLC circuit, calculate the power of each
element.
31.45 For a driven RLC circuit in steady state, explain what
happens to (a) the value of the average stored energy with
time and (b) the energy that the generator puts into the
circuit.
31.46 Apply the relationship between the power factor cos f,
the resistance R, and the impedance Z.
31.47 Apply the relationship between the average power
Pavg, the rms emf 
, the rms current Irms, and the power
factor cos f.
31.48 Identify what power factor is required in order to maxi-
mize the rate at which energy is supplied to a resistive load.
#rms
Learning Objectives
●In a series RLC circuit, the average power Pavg of the
generator is equal to the production rate of thermal energy in
the resistor:
Pavg ! I 2
rmsR ! #rmsIrms cos f.
●The abbreviation rms stands for root-mean-square; the
rms quantities are related to the maximum quantities by
and 
The term 
cos f is called the power factor of the circuit.
#rms ! #m/12.
V/12,
Irms ! I/12, Vrms !
Key Ideas
Power in Alternating-Current Circuits
In the RLC circuit of Fig. 31-7, the source of energy is the alternating-current
generator. Some of the energy that it provides is stored in the electric field in the
capacitor, some is stored in the magnetic field in the inductor, and some is dis-
sipated as thermal energy in the resistor. In steady-state operation, the average
stored energy remains constant.The net transfer of energy is thus from the gener-
ator to the resistor, where energy is dissipated.
The instantaneous rate at which energy is dissipated in the resistor can be
written, with the help of Eqs. 26-27 and 31-29, as
P ! i2R ! [I sin(vdt ' f)]2R ! I 2R sin2(vdt ' f).
(31-68)
The average rate at which energy is dissipated in the resistor, however, is the aver-
age of Eq. 31-68 over time. Over one complete cycle, the average value of sin u,
where u is any variable, is zero (Fig. 31-17a) but the average value of sin2 u is
(Fig. 31-17b). (Note in Fig. 31-17b how the shaded areas under the curve but
above the horizontal line marked 
exactly fill in the unshaded spaces below
that line.) Thus, we can write, from Eq. 31-68,
(31-69)
The quantity 
is called the root-mean-square, or rms, value of the current i:
(rms current).
(31-70)
We can now rewrite Eq. 31-69 as
(average power).
(31-71)
Pavg ! I rms
2 R
Irms !
I
12
I/1 2
Pavg ! I 2R
2
!#
I
12 $
2
R.
$1
2
1
2
Figure 31-17 (a) A plot of sin u versus u.The
average value over one cycle is zero.(b) A
plot of sin2 u versus u.The average value
over one cycle is .
1
2
0
+1
-1
0
π 
  π 
2
π 
sin
(a)
0
+1
0
π 
  π 
2
sin2
(b)
+ 1-2
θ 
θ 
θ 
θ 
3
π 
3

Equation 31-71 has the same mathematical form as Eq. 26-27 (P ! i2R); the
message here is that if we switch to the rms current, we can compute the aver-
age rate of energy dissipation for alternating-current circuits just as for direct-
current circuits.
We can also define rms values of voltages and emfs for alternating-current
circuits:
(rms voltage; rms emf).
(31-72)
Alternating-current instruments, such as ammeters and voltmeters, are usually
calibrated to read Irms, Vrms, and #rms. Thus, if you plug an alternating-current
voltmeter into a household electrical outlet and it reads 120 V, that is an rms
voltage. The maximum value of the potential difference at the outlet is
or 170 V. Generally scientists and engineers report rms values in-
stead of maximum values.
Because the proportionality factor 
in Eqs. 31-70 and 31-72 is the same
for all three variables, we can write Eqs. 31-62 and 31-60 as
(31-73)
and, indeed, this is the form that we almost always use.
We can use the relationship Irms ! #rms/Z to recast Eq. 31-71 in a useful
equivalent way.We write
(31-74)
From Fig. 31-14d, Table 31-2, and Eq. 31-62, however, we see that R/Z is just the
cosine of the phase constant f:
(31-75)
Equation 31-74 then becomes
(average power),
(31-76)
in which the term cos f is called the power factor. Because cos f ! cos('f),
Eq. 31-76 is independent of the sign of the phase constant f.
To maximize the rate at which energy is supplied to a resistive load in an
RLC circuit, we should keep the power factor cos f as close to unity as possible.
This is equivalent to keeping the phase constant f in Eq. 31-29 as close to zero as
possible. If, for example, the circuit is highly inductive, it can be made less so by
putting more capacitance in the circuit, connected in series. (Recall that putting
an additional capacitance into a series of capacitances decreases the equivalent
capacitance Ceq of the series.) Thus, the resulting decrease in Ceq in the circuit
reduces the phase constant and increases the power factor in Eq. 31-76. Power
companies place series-connected capacitors throughout their transmission sys-
tems to get these results.
Pavg ! #rmsIrms cos f
cos f ! VR
#m
! IR
IZ ! R
Z .
Pavg ! #rms
Z
IrmsR ! #rmsIrms
R
Z .
Irms ! #rms
Z
!
#rms
2R2 $ (XL ' XC)2 ,
1/12
12 & (120 V),
Vrms !
V
12   and  #rms ! #m
12
928
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
Checkpoint 7
(a) If the current in a sinusoidally driven series RLC circuit leads the emf, would we
increase or decrease the capacitance to increase the rate at which energy is supplied
to the resistance? (b) Would this change bring the resonant angular frequency of the
circuit closer to the angular frequency of the emf or put it farther away?

929
31-5 POWER IN ALTERNATING-CURRENT CIRCUITS
determined by the rms value of the driving emf and the cir-
cuit’s impedance Z (which we know), according to Eq. 31-73:
Substituting this into Eq. 31-76 then leads to
(Answer)
Second way: Instead, we can write
(Answer)
(c) What new capacitance Cnew is needed to maximize Pavg if
the other parameters of the circuit are not changed?
KEY IDEAS
(1) The average rate Pavg at which energy is supplied
and dissipated is maximized if the circuit is brought into
resonance with the driving emf. (2) Resonance occurs
when XC ! XL.
Calculations: From the given data, we have XC - XL. Thus,
we must decrease XC to reach resonance. From Eq. 31-39
(XC ! 1/vdC), we see that this means we must increase C to
the new value Cnew.
Using Eq. 31-39, we can write the resonance condition
XC ! XL as
Substituting 2pfd for vd (because we are given fd and not vd)
and then solving for Cnew, we find
(Answer)
Following the procedure of part (b), you can show that with
Cnew, the average power of energy dissipation Pavg would
then be at its maximum value of 
Pavg, max ! 72.0 W.
! 3.32 & 10'5 F ! 33.2 mF.
Cnew !
1
2pfdXL
!
1
(2p)(60 Hz)(80.0 ")
1
vdCnew
! XL.
!
(120 V)2
(211.90 ")2  (200 ") ! 64.1 W.
Pavg ! Irms
2 R ! #rms
2
Z2
R
! (120 V)2
211.90 "  (0.9438) ! 64.1 W.
Pavg ! #rmsIrms cos f ! #2
rms
Z  cos f
Irms ! #rms
Z .
