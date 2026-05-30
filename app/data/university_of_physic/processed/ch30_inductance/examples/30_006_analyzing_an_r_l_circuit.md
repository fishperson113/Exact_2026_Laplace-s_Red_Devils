Example 30.6
Analyzing an R-L circuit
A sensitive electronic device of resistance 
is to be
connected to a source of emf (of negligible internal resistance) by
a switch. The device is designed to operate with a 36-mA current,
but to avoid damage to the device, the current can rise to no more
than 4.9 mA in the first 
after the switch is closed. An inductor
is therefore connected in series with the device, as in Fig. 30.11;
the switch in question is 
(a) What is the required source emf 
(b) What is the required inductance L? (c) What is the R-L time
constant
SOLUTION
IDENTIFY and SET UP: This problem concerns current and current
growth in an R-L circuit, so we can use the ideas of this section.
Figure 30.12 shows the current i versus the time t that has elapsed
since closing 
. The graph shows that the final current is 
;
we are given R
, so the emf is determined by the require-
ment that the final current be I
36 mA. The other requirement is
that the current be no more than 
at 
to sat-
isfy this, we use Eq. (30.14) for the current as a function of time
and solve for the inductance, which is the only unknown quantity.
Equation (30.16) then tells us the time constant.
EXECUTE: (a) We solve 
for 
E = IR = 10.036 A21175 Æ2 = 6.3 V
E:
I = E>R
t = 58 ms;
i = 4.9 mA
=
= 175 Æ
I = E>R
S1
t?
?
E
S1.
58 ms
R = 175 Æ
(b) To find the required inductance, we solve Eq. (30.14) for 
First we multiply through by 
and then add 1 to both sides
to obtain
Then we take natural logs of both sides, solve for 
and insert the
numbers:
(c) From Eq. (30.16),
EVALUATE: Note that 
is much less than the time constant. In
the current builds up from zero to 4.9 mA, a small fraction
of its final value of 36 mA; after 
the current equals
of its final value, or about 10.632136 mA2 = 23 mA.
11 - 1>e2
390 ms
58 ms
58 ms
t = L
R = 69 * 10-3 H
175 Æ
= 3.9 * 10-4 s = 390 ms
=
-1175 Æ2158 * 10-6 s2
ln31 - 14.9 * 10-3 A21175 Æ2>16.3 V24
= 69 mH
L =
-Rt
ln11 - iR>E2
L,
1 - iR
E = e-1R>L2t
1-R>E2
L.
Current Decay in an R-L Circuit
Now suppose switch 
in the circuit of Fig. 30.11 has been closed for a while
and the current has reached the value 
Resetting our stopwatch to redefine the
initial time, we close switch 
at time 
bypassing the battery. (At the same
time we should open 
to save the battery from ruin.) The current through 
and
does not instantaneously go to zero but decays smoothly, as shown in Fig.
30.13. The Kirchhoff’s-rule loop equation is obtained from Eq. (30.12) by simply
omitting the 
term. We challenge you to retrace the steps in the above analysis
and show that the current i varies with time according to
(30.18)
where 
is the initial current at time 
The time constant, 
is the
time for current to decrease to 
or about 37%, of its original value. In time 
it has dropped to 13.5%, in time 
to 0.67%, and in 
to 0.0045%.
The energy that is needed to maintain the current during this decay is provided
by the energy stored in the magnetic field of the inductor. The detailed energy
analysis is simpler this time. In place of Eq. (30.17) we have
(30.19)
In this case, 
is negative; Eq. (30.19) shows that the energy stored in the
inductor decreases at a rate equal to the rate of dissipation of energy 
in the
resistor.
This entire discussion should look familiar; the situation is very similar to that
of a charging and discharging capacitor, analyzed in Section 26.4. It would be a
good idea to compare that section with our discussion of the R-L circuit.
i2R
Li di>dt
0 = i2R + Li di
dt
10t
5t
2t
1>e,
t = L>R,
t = 0.
I0
i = I0e-1R>L2t
E
L
R
S1
t = 0,
S2
I0.
S1
R
L
i
t
i
I0
I0
e
O
t 5 L
R
t
S2
Switch S2 is closed at t 5 0.
30.13 Graph of versus for decay of
current in an R-L circuit. After one time
constant 
the current is 
of its initial
value.
1>e
t,
t
i

30.5 The L-C Circuit
1005
