Sample Problem 31.07
Driven RLC circuit: power factor and average power
A series RLC circuit, driven with 
at fre-
quency fd
60.0 Hz, contains a resistance R
200 
, an
"
!
!
#rms ! 120 V
Additional examples, video, and practice available at WileyPLUS
inductance with inductive reactance XL ! 80.0 ", and a
capacitance with capacitive reactance XC ! 150 ".
(a) What are the power factor cos f and phase constant f of
the circuit?
KEY IDEA
The power factor cos f can be found from the resistance R
and impedance Z via Eq. 31-75 (cos f ! R/Z).
Calculations: To calculate Z, we use Eq. 31-61:
Equation 31-75 then gives us
(Answer)
Taking the inverse cosine then yields
f ! cos'1 0.944 ! .19.3°.
The inverse cosine on a calculator gives only the positive an-
swer here, but both 19.3 and 19.3 have a cosine of 0.944.
To determine which sign is correct, we must consider
whether the current leads or lags the driving emf. Because
XC - XL, this circuit is mainly capacitive, with the current
leading the emf.Thus,f must be negative:
f ! '19.3°.
(Answer)
We could, instead, have found f with Eq. 31-65.A calculator
would then have given us the answer with the minus  sign.
(b) What is the average rate Pavg at which energy is
dissipated in the resistance?
KEY IDEAS
There are two ways and two ideas to use: (1) Because the
circuit is assumed to be in steady-state operation, the rate at
which energy is dissipated in the resistance is equal to the
rate at which energy is supplied to the circuit, as given by
Eq. 31-76 (Pavg ! #rmsIrms cos f). (2) The rate at which
energy is dissipated in a resistance R depends on the square
of the rms current Irms through it, according to Eq. 31-71
(Pavg! I 2
rmsR).
First way: We are given the rms driving emf #rms and we
already know cos f from part (a). The rms current Irms is
+
'
+
$
cos f ! R
Z !
200 "
211.90 " ! 0.9438 % 0.944.
! 2(200 ")2 $ (80.0 " ' 150 ")2 ! 211.90 ".
Z ! 2R2 $ (XL ' XC)2

930
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
Transformers
Energy Transmission Requirements
When an ac circuit has only a resistive load, the power factor in Eq. 31-76 is 
cos 0° ! 1 and the applied rms emf #rms is equal to the rms voltage Vrms across the
load. Thus, with an rms current Irms in the load, energy is supplied and dissipated
at the average rate of
Pavg ! #I ! IV.
(31-77)
(In Eq. 31-77 and the rest of this module, we follow conventional practice and drop
the subscripts identifying rms quantities. Engineers and scientists assume that all
time-varying currents and voltages are reported as rms values; that is what the me-
ters read.) Equation 31-77 tells us that, to satisfy a given power requirement, we
have a range of choices for I and V, provided only that the product IV is as required.
In electrical power distribution systems it is desirable for reasons of safety
and for efficient equipment design to deal with relatively low voltages at both the
generating end (the electrical power plant) and the receiving end (the home or
factory). Nobody wants an electric toaster to operate at, say, 10 kV. However, in
the transmission of electrical energy from the generating plant to the consumer,
we want the lowest practical current (hence the largest practical voltage) to mini-
mize I 2R losses (often called ohmic losses) in the transmission line.
As an example, consider the 735 kV line used to transmit electrical energy
from the La Grande 2 hydroelectric plant in Quebec to Montreal, 1000 km away.
Suppose that the current is 500 A and the power factor is close to unity. Then
from Eq. 31-77, energy is supplied at the average rate
Pavg ! #I ! (7.35 & 10 5 V)(500 A) ! 368 MW.
31-6 TRANSFORMERS
After reading this module, you should be able to . . .
31.49 For power transmission lines, identify why the
transmission should be at low current and high voltage.
31.50 Identify the role of transformers at the two ends of a
transmission line.
31.51 Calculate the energy dissipation in a transmission line.
31.52 Identify a transformer’s primary and secondary.
31.53 Apply the relationship between the voltage and
number of turns on the two sides of a transformer.
31.54 Distinguish between a step-down transformer and a
step-up transformer.
31.55 Apply the relationship between the current and number
of turns on the two sides of a transformer.
31.56 Apply the relationship between the power into and out
of an ideal transformer.
31.57 Identify the equivalent resistance as seen from the
primary side of a transformer.
31.58 Apply the relationship between the equivalent
resistance and the actual resistance.
31.59 Explain the role of a transformer in impedance
matching.
Learning Objectives
●A transformer (assumed to be ideal) is an iron core on
which are wound a primary coil of Np turns and a secondary
coil of Ns turns. If the primary coil is connected across an
alternating-current generator, the primary and secondary
voltages are related by
(transformation of voltage).
●The currents through the coils are related by
Vs ! Vp
Ns
Np
(transformation of currents).
●The equivalent resistance of the secondary circuit, as seen
by the generator, is
where R is the resistive load in the secondary circuit. The
ratio Np/Ns is called the transformer’s turns ratio.
Req !#
Np
Ns $
2
R,
Is ! Ip
Np
Ns
Key Ideas

The resistance of the transmission line is about 0.220 "/km; thus, there is a total
resistance of about 220 " for the 1000 km stretch. Energy is dissipated due to that
resistance at a rate of about
Pavg ! I 2R ! (500 A)2(220 ") ! 55.0 MW,
which is nearly 15% of the supply rate.
Imagine what would happen if we doubled the current and halved the volt-
age. Energy would be supplied by the plant at the same average rate of 368 MW
as previously, but now energy would be dissipated at the rate of about
Pavg ! I 2R ! (1000 A)2(220 ") ! 220 MW,
which is almost 60% of the supply rate. Hence the general energy transmission
rule:Transmit at the highest possible voltage and the lowest possible current.
The Ideal Transformer
The transmission rule leads to a fundamental mismatch between the requirement
for efficient high-voltage transmission and the need for safe low-voltage gener-
ation and consumption. We need a device with which we can raise (for trans-
mission) and lower (for use) the ac voltage in a circuit, keeping the product
current
voltage essentially constant. The transformer is such a device. It has
no moving parts, operates by Faraday’s law of induction, and has no simple
direct-current counterpart.
The ideal transformer in Fig. 31-18 consists of two coils, with different num-
bers of turns, wound around an iron core. (The coils are insulated from the core.)
In use, the primary winding, of Np turns, is connected to an alternating-current
generator whose emf # at any time t is given by
# ! #m sin vt.
(31-78)
The secondary winding, of Ns turns, is connected to load resistance R, but its
circuit is an open circuit as long as switch S is open (which we assume for the
present). Thus, there can be no current through the secondary coil. We assume
further for this ideal transformer that the resistances of the primary and second-
ary windings are negligible. Well-designed, high-capacity transformers can have
energy losses as low as 1%; so our assumptions are reasonable.
For the assumed conditions, the primary winding (or primary) is a pure
inductance and the primary circuit is like that in Fig. 31-12.Thus, the (very small)
primary current, also called the magnetizing current Imag, lags the primary voltage
Vp by 90°; the primary’s power factor (! cos f in Eq. 31-76) is zero; so no power
is delivered from the generator to the transformer.
However, the small sinusoidally changing primary current Imag produces a
sinusoidally changing magnetic flux #B in the iron core. The core acts to
strengthen the flux and to bring it through the secondary winding (or secondary).
Because #B varies, it induces an emf #turn (! d#B/dt) in each turn of the
secondary. In fact, this emf per turn #turn is the same in the primary and the
secondary.Across the primary, the voltage Vp is the product of #turn and the num-
ber of turns Np; that is, Vp ! #turnNp. Similarly, across the secondary the voltage is
Vs ! #turnNs.Thus, we can write
or
(transformation of voltage).
(31-79)
If Ns - Np,the device is a step-up transformer because it steps the primary’s voltage
Vp up to a higher voltage Vs.Similarly,if Ns / Np,it is a step-down transformer.
Vs ! Vp
Ns
Np
#turn ! Vp
Np
! Vs
Ns
,
&
931
31-6 TRANSFORMERS
Figure 31-18 An ideal transformer (two coils
wound on an iron core) in a basic trans-
former circuit.An ac generator produces
current in the coil at the left (the primary).
The coil at the right (the secondary) is con-
nected to the resistive load R when switch S
is closed.
R
Vp
Vs
S
Np
Ns
Φ B
Primary 
Secondary 

932
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
With switch S open, no energy is transferred from the generator to the rest of
the circuit, but when we close S to connect the secondary to the resistive load R,
energy is transferred. (In general, the load would also contain inductive and
capacitive elements, but here we consider just resistance R.) Here is the process:
1. An alternating current Is appears in the secondary circuit, with corresponding
energy dissipation rate 
in the resistive load.
2. This current produces its own alternating magnetic flux in the iron core, and
this flux induces an opposing emf in the primary windings.
3. The voltage Vp of the primary, however, cannot change in response to this
opposing emf because it must always be equal to the emf # that is provided by
the generator; closing switch S cannot change this fact.
4. To maintain Vp, the generator now produces (in addition to Imag) an alternat-
ing current Ip in the primary circuit; the magnitude and phase constant of
Ip are just those required for the emf induced by Ip in the primary to exactly
cancel the emf induced there by Is. Because the phase constant of Ip is not 90°
like that of Imag, this current Ip can transfer energy to the primary.
Energy Transfers. We want to relate Is to Ip. However, rather than analyze the
foregoing complex process in detail, let us just apply the principle of conservation
of energy.The rate at which the generator transfers energy to the primary is equal
to IpVp.The rate at which the primary then transfers energy to the secondary (via
the alternating magnetic field linking the two coils) is IsVs. Because we assume
that no energy is lost along the way,conservation of energy requires that
IpVp ! IsVs.
Substituting for Vs from Eq. 31-79, we find that
(transformation of currents).
(31-80)
This equation tells us that the current Is in the secondary can differ from the
current Ip in the primary, depending on the turns ratio Np/Ns.
Current Ip appears in the primary circuit because of the resistive load R in
the secondary circuit. To find Ip, we substitute Is ! Vs/R into Eq. 31-80 and then
we substitute for Vs from Eq. 31-79.We find
(31-81)
This equation has the form Ip ! Vp/Req, where equivalent resistance Req is
(31-82)
This Req is the value of the load resistance as “seen” by the generator; the genera-
tor produces the current Ip and voltage Vp as if the generator were connected to a
resistance Req.
Impedance Matching
Equation 31-82 suggests still another function for the transformer. For maximum
transfer of energy from an emf device to a resistive load, the resistance of the emf
device must equal the resistance of the load. The same relation holds for ac
circuits except that the impedance (rather than just the resistance) of the genera-
tor must equal that of the load. Often this condition is not met. For example, in
a music-playing system, the amplifier has high impedance and the speaker set has
low impedance. We can match the impedances of the two devices by coupling
them through a transformer that has a suitable turns ratio Np/Ns.
Req !#
Np
Ns $
2
R.
Ip ! 1
R #
Ns
Np $
2
Vp.
Is ! Ip
Np
Ns
I s
2R (! Vs
2/R)

933
REVIEW & SUMMARY
Checkpoint 8
An alternating-current emf device in a certain circuit has a smaller resistance than that
of the resistive load in the circuit;to increase the transfer of energy from the device to
the load,a transformer will be connected between the two.(a) Should Ns be greater
than or less than Np? (b) Will that make it a step-up or step-down transformer?
Eq. 31-77 yields
(Answer)
Similarly, in the secondary circuit,
(Answer)
You can check that Is ! Ip(Np/Ns) as required by Eq.31-80.
(c) What is the resistive load Rs in the secondary circuit? What
is the corresponding resistive load Rp in the primary circuit?
One way: We can use V ! IR to relate the resistive load to the
rms voltage and current.For the secondary circuit,we find
(Answer)
Similarly, for the primary circuit we find
(Answer)
Second way: We use the fact that Rp equals the equivalent re-
sistive load “seen” from the primary side of the transformer,
which is a resistance modified by the turns ratio and given by
Eq. 31-82 (Req ! (Np/Ns)2R). If we substitute Rp for Req and Rs
for R,that equation yields
(Answer)
! 926 " % 930 ".
Rp !#
Np
Ns $
2
Rs ! (70.83)2(0.1846 ")
Rp !
Vp
Ip
! 8.5 & 10 3 V
9.176 A
! 926 " % 930 ".
Rs ! Vs
Is
! 120 V
650 A ! 0.1846 " % 0.18 ".
Is !
Pavg
Vs
! 78 & 10 3 W
120 V
! 650 A.
Ip !
Pavg
Vp
! 78 & 103 W
8.5 & 103 V ! 9.176 A % 9.2 A.
