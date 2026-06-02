Sample Problem 31.03
Purely resistive load: potential difference and current 
In Fig. 31-8, resistance R is 200 
and the sinusoidal alter-
nating emf device operates at amplitude #m ! 36.0 V and
frequency fd ! 60.0 Hz.
(a) What is the potential difference vR(t) across the resistance
as a function of time t, and what is the amplitude VR of vR(t)?
KEY IDEA
In a circuit with a purely resistive load, the potential differ-
ence vR(t) across the resistance is always equal to the potential
difference (t) across the emf device.
Calculations: For our situation, vR(t)
#(t) and VR
#m.
Since #m is given, we can write
VR ! #m ! 36.0 V.
(Answer)
To find vR(t), we use Eq. 31-28 to write
vR(t) ! #(t) ! #m sin vdt
(31-34)
and then substitute #m ! 36.0 V and
vd ! 2pfd ! 2p(60 Hz) ! 120p
to obtain
vR ! (36.0 V) sin(120pt).
(Answer)
!
!
#
"
A Capacitive Load
Figure 31-10 shows a circuit containing a capacitance and a generator with the
alternating emf of Eq. 31-28. Using the loop rule and proceeding as we did when
we obtained Eq. 31-30, we find that the potential difference across the capacitor is
vC ! VC sin vdt,
(31-36)
where VC is the amplitude of the alternating voltage across the capacitor. From
the definition of capacitance we can also write
qC ! CvC ! CVC sin vdt.
(31-37)
Our concern, however, is with the current rather than the charge. Thus, we differ-

917
31-3 FORCED OSCILLATIONS OF THREE SIMPLE CIRCUITS
entiate Eq. 31-37 to find
(31-38)
We now modify Eq. 31-38 in two ways. First, for reasons of symmetry of nota-
tion, we introduce the quantity XC, called the capacitive reactance of a capacitor,
defined as
(capacitive reactance).
(31-39)
Its value depends not only on the capacitance but also on the driving angular
frequency vd. We know from the definition of the capacitive time constant 
(t ! RC) that the SI unit for C can be expressed as seconds per ohm. Applying
this to Eq. 31-39 shows that the SI unit of XC is the ohm, just as for resistance R.
Second, we replace cos vdt in Eq. 31-38 with a phase-shifted sine:
cos vdt ! sin(vdt $ 90°).
You can verify this identity by shifting a sine curve 90° in the negative direction.
With these two modifications, Eq. 31-38 becomes
(31-40)
From Eq. 31-29, we can also write the current iC in the capacitor of Fig. 31-10 as
iC ! IC sin(vdt ' f),
(31-41)
where IC is the amplitude of iC. Comparing Eqs. 31-40 and 31-41, we see that for
a purely capacitive load the phase constant f for the current is '90°. We also
see that the voltage amplitude and current amplitude are related by
VC ! ICXC
(capacitor).
(31-42)
Although we found this relation for the circuit of Fig. 31-10, it applies to any
capacitance in any ac circuit.
Comparison of Eqs. 31-36 and 31-40, or inspection of Fig. 31-11a, shows that
the quantities vC and iC are 90°, p/2 rad, or one-quarter cycle, out of phase.
Furthermore, we see that iC leads vC, which means that, if you monitored the
current iC and the potential difference vC in the circuit of Fig. 31-10, you would
find that iC reaches its maximum before vC does, by one-quarter cycle.
iC !#
VC
XC$ sin(vdt $ 90+).
XC !
1
vdC
iC ! dqC
dt
! vdCVC  cos vdt.
Figure 31-11 (a) The current in the capacitor leads
the voltage by 90° (! p/2 rad). (b) A phasor dia-
gram shows the same thing.
vC, iC
T
iC
vC
0
Instants
represented in (b)
(a)
(b)
iC
vC
VC
IC
Rotation of
phasors at
rate
d
dt
ω
T/2
IC
VC
= -90° = -   /2 rad 
φ 
π 
ω
t
For a capacitive load, the
current leads the potential
difference by 90º.
“Leads” means that the
current peaks at an
earlier time than the
potential difference.

918
CHAPTER 31
ELECTROMAGNETIC OSCILLATIONS AND ALTERNATING CURRENT
An Inductive Load
Figure 31-12 shows a circuit containing an inductance and a generator with the al-
ternating emf of Eq. 31-28. Using the loop rule and proceeding as we did to
obtain Eq. 31-30, we find that the potential difference across the inductance is
vL ! VL sin vdt,
(31-45)
KEY IDEA
In an ac circuit with a purely capacitive load, the alternating
current iC(t) in the capacitance leads the alternating poten-
tial difference vC(t) by 90+; that is, the phase constant f for
the current is '90°, or 'p/2 rad.
Calculations: Thus, we can write Eq. 31-29 as
iC ! IC sin(vdt ' f) ! IC sin(vdt $ p/2).
(31-44)
We can find the amplitude IC from Eq. 31-42 (VC ! ICXC) if
we first find the capacitive reactance XC. From Eq. 31-39
(XC ! 1/vdC), with vd ! 2pfd, we can write
Then Eq. 31-42 tells us that the current amplitude is
(Answer)
Substituting this and vd ! 2pfd ! 120p into Eq. 31-44, we
have
iC ! (0.203 A) sin(120pt $ p/2).
(Answer)
IC ! VC
XC
! 36.0 V
177 " ! 0.203 A.
! 177 ".
XC !
1
2pfdC !
1
(2p)(60.0 Hz)(15.0 & 10'6 F)
