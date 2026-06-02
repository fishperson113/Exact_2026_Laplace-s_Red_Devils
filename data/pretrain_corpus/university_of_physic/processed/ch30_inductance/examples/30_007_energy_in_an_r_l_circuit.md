Example 30.7
Energy in an R-L circuit
When the current in an R-L circuit is decaying, what fraction of the
original energy stored in the inductor has been dissipated after 2.3
time constants?
SOLUTION
IDENTIFY and SET UP: This problem concerns current decay in an
R-L circuit as well as the relationship between the current in an
inductor and the amount of stored energy. The current at any time
is given by Eq. (30.18); the stored energy associated with this
current is given by Eq. (30.9), 
EXECUTE: From Eq. (30.18), the current at any time is
We substitute this into 
to obtain an expression for the
stored energy at any time:
U = 1
2 LI 2
0 e-21R>L2t = U0e-21R>L2t
U = 1
2Li2
i = I0e-1R>L2t
t
i
U = 1
2Li2.
t
i
where 
is the energy at the initial time 
When
we have
That is, only 0.010 or 1.0% of the energy initially stored in the
inductor remains, so 99.0% has been dissipated in the resistor.
EVALUATE: To get a sense of what this result means, consider the
R-L circuit we analyzed in Example 30.6, for which 
With 
and 
we have 
Of this, 99.0% or
is dissipated in 
In other words, this circuit can be almost completely powered off
(or powered on) in 0.90 ms, so the minimum time for a complete
on-off cycle is 1.8 ms. Even shorter cycle times are required for
many purposes, such as in fast switching networks for telecom-
munications. In such cases a smaller time constant 
is
needed.
t = L>R
s = 0.90 ms.
2.31390 ms2 = 9.0 * 10-4
10-5 J
4.4 *
1
210.069 H210.036 A22 = 4.5 * 10-5 J.
U0 = 1
2 LI 2
0 =
I0 = 36 mA,
L = 69 mH
= 390 ms.
t
U = U0e-212.32 = U0e-4.6 = 0.010U0
t = 2.3t = 2.3L>R,
t = 0.
U0 = 1
2 LI 2
0
Test Your Understanding of Section 30.4
(a) In Fig. 30.11, what are the
algebraic signs of the potential differences 
and 
when switch 
is closed and
switch 
is open? (i) 
(ii) 
(iii) 
(iv) 
(b) What are the signs of 
and 
when 
is open, 
is
closed, and current is flowing in the direction shown? (i) 
(ii) 
(iii) 
(iv) 
❙
vbc 6 0.
vab 6 0,
vbc 7 0;
vab 6 0,
vbc 6 0;
vab 7 0,
vbc 7 0;
vab 7 0,
S2
S1
vbc
vab
vbc 6 0.
vab 6 0,
vbc 7 0;
vab 6 0,
vbc 6 0;
vab 7 0,
vbc 7 0;
vab 7 0,
S2
S1
vbc
vab
30.5 The L-C Circuit
A circuit containing an inductor and a capacitor shows an entirely new mode of
behavior, characterized by oscillating current and charge. This is in sharp con-
trast to the exponential approach to a steady-state situation that we have seen
with both R-C and R-L circuits. In the L-C circuit in Fig. 30.14a we charge the
capacitor to a potential difference 
and initial charge 
on its left-hand
plate and then close the switch. What happens?
The capacitor begins to discharge through the inductor. Because of the
induced emf in the inductor, the current cannot change instantaneously; it starts at
zero and eventually builds up to a maximum value 
During this buildup the
capacitor is discharging. At each instant the capacitor potential equals the
induced emf, so as the capacitor discharges, the rate of change of current
decreases. When the capacitor potential becomes zero, the induced emf is also
zero, and the current has leveled off at its maximum value 
Figure 30.14b
shows this situation; the capacitor has completely discharged. The potential dif-
ference between its terminals (and those of the inductor) has decreased to zero,
and the current has reached its maximum value 
During the discharge of the capacitor, the increasing current in the inductor
has established a magnetic field in the space around it, and the energy that was
initially stored in the capacitor’s electric field is now stored in the inductor’s
magnetic field.
Although the capacitor is completely discharged in Fig. 30.14b, the current
persists (it cannot change instantaneously), and the capacitor begins to charge
with polarity opposite to that in the initial state. As the current decreases, the
magnetic field also decreases, inducing an emf in the inductor in the same direc-
tion as the current; this slows down the decrease of the current. Eventually, the
Im.
Im.
Im.
Q = CVm
Vm
ActivPhysics 14.2: AC Circuits: The RLC
Oscillator (Questions 1-6)

current and the magnetic field reach zero, and the capacitor has been charged in
the sense opposite to its initial polarity (Fig. 30.14c), with potential difference
and charge 
on its left-hand plate.
The process now repeats in the reverse direction; a little later, the capacitor
has again discharged, and there is a current in the inductor in the opposite direc-
tion (Fig. 30.14d). Still later, the capacitor charge returns to its original value
(Fig. 30.14a), and the whole process repeats. If there are no energy losses, the
charges on the capacitor continue to oscillate back and forth indefinitely. This
process is called an electrical oscillation.
From an energy standpoint the oscillations of an electrical circuit transfer
energy from the capacitor’s electric field to the inductor’s magnetic field and
back. The total energy associated with the circuit is constant. This is analogous to
the transfer of energy in an oscillating mechanical system from potential energy
to kinetic energy and back, with constant total energy. As we will see, this anal-
ogy goes much further.
Electrical Oscillations in an L-C Circuit
To study the flow of charge in detail, we proceed just as we did for the R-L cir-
cuit. Figure 30.15 shows our definitions of q and i.
CAUTION
Positive current in an L-C circuit After examining Fig. 30.14, the positive
direction for current in Fig. 30.15 may seem backward to you. In fact we’ve chosen
this direction to simplify the relationship between current and capacitor charge. We
define the current at each instant to be 
the rate of change of the charge on
the left-hand capacitor plate. Hence if the capacitor is initially charged and begins to
discharge as in Figs. 30.14a and 30.14b, then 
and the initial current i is neg-
ative; the direction of the current is then opposite to the (positive) direction shown in
Fig. 30.15. ❙
dq>dt 6 0
i = dq>dt,
-Q
-Vm
1006
CHAPTER 30 Inductance
(a) t 5 0 and t 5 T
(close switch at t 5 0)
(b) t 5
T
1
4
(c) t 5
T
1
2
(d) t 5
T
3
4
+
+
+
+
+
+
+
+
+
+
+
+
+
+
Circuit’s energy all
stored in electric field
Circuit’s energy all
stored in magnetic field
Circuit’s energy all
stored in electric field
Capacitor fully charged;
zero current
Capacitor fully
discharged;
current maximal
Capacitor polarity reverses.
Capacitor charging; I decreasing
Current direction reverses.
Capacitor fully charged;
zero current
Capacitor fully
discharged;
current maximal
Capacitor
discharging;
I increasing
Capacitor
charging;
I decreasing
Capacitor
discharging;
I increasing
Circuit’s energy all
stored in magnetic field
Em
+Qm
-Qm
Vm
C
L
Bm
Im
Im
+Qm
-Qm
Em
-Vm
Bm
Im
Im
zero
E 5 UB 1 UE
zero
E 5 UB 1 UE
zero
E 5 UB 1 UE
zero
E 5 UB 1 UE
30.14 In an oscillating L-C circuit, the charge on the capacitor and the current through the inductor both vary sinusoidally with time.
Energy is transferred between magnetic energy in the inductor 
and electric energy in the capacitor 
As in simple harmonic
motion, the total energy 
remains constant. (Compare Fig. 14.14 in Section 14.3.)
E
1UE2.
1UB2
Travel
+q
-q
C
i
L
30.15 Applying Kirchhoff’s loop rule to
the L-C circuit. The direction of travel
around the loop in the loop equation is
shown. Just after the circuit is completed
and the capacitor first begins to discharge,
as in Fig. 30.14a, the current is negative
(opposite to the direction shown).

30.5 The L-C Circuit
1007
We apply Kirchhoff’s loop rule to the circuit in Fig. 30.15. Starting at the
lower-right corner of the circuit and adding voltages as we go clockwise around
the loop, we obtain
Since 
it follows that 
We substitute this expression
into the above equation and divide by 
to obtain
(30.20)
Equation (30.20) has exactly the same form as the equation we derived for
simple harmonic motion in Section 14.2, Eq. (14.4). That equation is 
or
(You should review Section 14.2 before going on with this discussion.) In the 
L-C circuit the capacitor charge q plays the role of the displacement x, and the
current 
is analogous to the particle’s velocity 
The induc-
tance 
is analogous to the mass m, and the reciprocal of the capacitance, 
is
analogous to the force constant k.
Pursuing this analogy, we recall that the angular frequency 
of the
harmonic oscillator is equal to 
and the position is given as a function of
time by Eq. (14.13),
where the amplitude 
and the phase angle 
depend on the initial conditions. In
the analogous electrical situation the capacitor charge q is given by
(30.21)
and the angular frequency 
of oscillation is given by
(30.22)
You should verify that Eq. (30.21) satisfies the loop equation, Eq. (30.20), when
has the value given by Eq. (30.22). In doing this, you will find that the instanta-
neous current 
is given by
(30.23)
Thus the charge and current in an L-C circuit oscillate sinusoidally with time,
with an angular frequency determined by the values of and 
The ordinary fre-
quency 
the number of cycles per second, is equal to 
as always. The con-
stants 
and 
in Eqs. (30.21) and (30.23) are determined by the initial
conditions. If at time 
the left-hand capacitor plate in Fig. 30.15 has its max-
imum charge 
and the current i is zero, then 
If 
at time 
then
Energy in an L-C Circuit
We can also analyze the L-C circuit using an energy approach. The analogy to
simple harmonic motion is equally useful here. In the mechanical problem a body
with mass m is attached to a spring with force constant k. Suppose we displace
the body a distance 
from its equilibrium position and release it from rest at time
The kinetic energy of the system at any later time is 
and its elastic
potential energy is 
Because the system is conservative, the sum of these
1
2 kx2.
1
2 mvx
2,
t = 0.
A
f = p>2 rad.
t = 0,
q = 0
f = 0.
Q
t = 0
f
Q
v>2p
f,
C.
L
i = -vQsin1vt + f2
i = dq>dt
v
(angular frequency of oscillation
in an L-C circuit)
v = A
1
LC
v
q = Qcos1vt + f2
f
A
x = Acos1vt + f2
1k>m21>2,
v = 2pf
1>C,
L
vx = dx>dt.
i = dq>dt
d2x
dt 2 + k
m x = 0
-1k>m2x,
d2x>dt 2 =
d2q
dt 2 +
1
LC q = 0  1L-C circuit2
-L
di>dt = d2q>dt 2.
i = dq>dt,
-L di
dt - q
C = 0

energies equals the initial energy of the system, 
We find the velocity 
at
any position x just as we did in Section 14.3, Eq. (14.22):
(30.24)
The L-C circuit is also a conservative system. Again let 
be the maximum
capacitor charge. The magnetic-field energy 
in the inductor at any time cor-
responds to the kinetic energy 
of the oscillating body, and the electric-field
energy 
in the capacitor corresponds to the elastic potential energy 
of
the spring. The sum of these energies equals the total energy 
of the sys-
tem:
(30.25)
The total energy in the L-C circuit is constant; it oscillates between the magnetic
and the electric forms, just as the constant total mechanical energy in simple har-
monic motion is constant and oscillates between the kinetic and potential forms.
Solving Eq. (30.25) for i, we find that when the charge on the capacitor is q,
the current i is
(30.26)
You can verify this equation by substituting q from Eq. (30.21) and i from
Eq. (30.23). Comparing Eqs. (30.24) and (30.26), we see that current 
and charge q are related in the same way as are velocity 
and position
x in the mechanical problem.
Table 30.1 summarizes the analogies between simple harmonic motion and 
L-C circuit oscillations. The striking parallels shown there are so close that we can
solve complicated mechanical and acoustical problems by setting up analogous
electric circuits and measuring the currents and voltages that correspond to the
mechanical and acoustical quantities to be determined. This is the basic principle
of many analog computers. This analogy can be extended to damped oscillations,
which we consider in the next section. In Chapter 31 we will extend the analogy
further to include forced electrical oscillations, which occur in all alternating-
current circuits.
vx = dx>dt
i = dq>dt
i =  A
1
LC 2Q2 - q2
1
2 Li2 + q2
2C = Q2
2C
Q2>2C
1
2kx2
q2>2C
1
2 mv2
1
2 Li2
Q
vx =  A
k
m 2A2 - x2
vx
1
2 kA2.
1008
CHAPTER 30 Inductance
Table 30.1 Oscillation of a 
Mass-Spring System Compared
with Electrical Oscillation in 
an L-C Circuit
Mass-Spring System
Inductor-Capacitor Circuit
q = Qcos1vt + f2
v = A
1
LC
i = dq>dt
i =  21>LC 2Q2 - q2
1
2 Li2 + q2>2C = Q2>2C
Electric energy = q2>2C
Magnetic energy = 1
2 Li2
x = Acos1vt + f2
v = A
k
m
vx = dx>dt
vx =  2k>m 2A2 - x2
1
2 mvx
2 + 1
2 kx2 = 1
2 kA2
Potential energy = 1
2 kx2
Kinetic energy = 1
2 mvx
2
