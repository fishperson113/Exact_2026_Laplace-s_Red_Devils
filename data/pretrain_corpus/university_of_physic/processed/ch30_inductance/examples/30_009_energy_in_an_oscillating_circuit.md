Example 30.9
Energy in an oscillating circuit
For the L-C circuit of Example 30.8, find the magnetic and electric
energies (a) at 
and (b) at 
SOLUTION
IDENTIFY and SET UP: We must calculate the magnetic energy 
(stored in the inductor) and the electric energy 
(stored in the
capacitor) at two times during the L-C circuit oscillation. From
Example 30.8 we know the values of the capacitor charge q and cir-
cuit current i for both times. We use them to calculate 
and
EXECUTE: (a) At 
there is no current and 
Hence there
is no magnetic energy, and all the energy in the circuit is in the
form of electric energy in the capacitor:
UB = 1
2 Li2 = 0 
UE = Q2
2C =
17.5 * 10-3 C22
2125 * 10-6 F2
= 1.1 J
q = Q.
t = 0
UE = q2>2C.
UB = 1
2Li2
UE
UB
t = 1.2 ms.
t = 0
(b) From Example 30.8, at t  1.2 ms we have 
and
. Hence
EVALUATE: The magnetic and electric energies are the same at
halfway between the situations in Figs. 30.14b
and 30.14c. We saw in Example 30.8 that the time considered in
part (b), t  1.2 ms, equals 0.38T; this is slightly later than 0.375T,
so 
is slightly less than 
. At all times the total energy 
has the same value, 1.1 J. An L-C circuit without resist-
ance is a conservative system; no energy is dissipated.
UB + UE
E =
UE
UB
t = 3T>8 = 0.375T,
UE = q2
2C =
1-5.5 * 10-3 C22
2125 * 10-6 F2
= 0.6 J
UB = 1
2 Li2 = 1
2 110 * 10-3 H21-10 A22 = 0.5 J
q = -5.5 * 10-3 C
i = -10 A
Test Your Understanding of Section 30.5
One way to think about the energy
stored in an L-C circuit is to say that the circuit elements do positive or negative work on
the charges that move back and forth through the circuit. (a) Between stages (a) and 
(b) in Fig. 30.14, does the capacitor do positive work or negative work on the charges?
(b) What kind of force (electric or magnetic) does the capacitor exert on the charges to do
this work? (c) During this process, does the inductor do positive or negative work on the
charges? (d) What kind of force (electric or magnetic) does the inductor exert on the
charges?
❙
ActivPhysics 14.2: AC Circuits: The RLC
Oscillator (Questions 7-10)

underdamped. If we increase 
the oscillations die out more rapidly. When 
reaches a certain value, the circuit no longer oscillates; it is critically damped
(Fig. 30.16b). For still larger values of 
the circuit is overdamped (Fig.
30.16c), and the capacitor charge approaches zero even more slowly. We used
these same terms to describe the behavior of the analogous mechanical system,
the damped harmonic oscillator, in Section 14.7.
Analyzing an L-R-C Series Circuit
To analyze L-R-C series circuit behavior in detail, we consider the circuit shown
in Fig. 30.17. It is like the L-C circuit of Fig. 30.15 except for the added resistor
we also show the source that charges the capacitor initially. The labeling of the
positive senses of q and i are the same as for the L-C circuit.
First we close the switch in the upward position, connecting the capacitor to a
source of emf 
for a long enough time to ensure that the capacitor acquires its
final charge 
and any initial oscillations have died out. Then at time
we flip the switch to the downward position, removing the source from the
circuit and placing the capacitor in series with the resistor and inductor. Note that
the initial current is negative, opposite to the direction of i shown in Fig. 30.17.
To find how q and i vary with time, we apply Kirchhoff’s loop rule. Starting at
point a and going around the loop in the direction abcda, we obtain the equation
Replacing i with 
and rearranging, we get
(30.27)
Note that when 
this reduces to Eq. (30.20) for an L-C circuit.
There are general methods for obtaining solutions of Eq. (30.27). The form of
the solution is different for the underdamped (small 
and overdamped (large 
cases. When 
is less than 
the solution has the form
(30.28)
where 
and 
are constants. We invite you to take the first and second deriva-
tives of this function and show by direct substitution that it does satisfy 
Eq. (30.27).
This solution corresponds to the underdamped behavior shown in Fig. 30.16a;
the function represents a sinusoidal oscillation with an exponentially decaying
amplitude. (Note that the exponential factor 
is not the same as the factor
that we encountered in describing the R-L circuit in Section 30.4.) When
Eq. (30.28) reduces to Eq. (30.21) for the oscillations in an L-C circuit. If
is not zero, the angular frequency of the oscillation is less than
because of the term containing 
The angular frequency 
of the damped oscil-
lations is given by
(30.29)
When 
this reduces to Eq. (30.22), 
As 
increases, 
becomes smaller and smaller. When 
the quantity under the radical
becomes zero; the system no longer oscillates, and the case of critical damping
(Fig. 30.16b) has been reached. For still larger values of 
the system behaves as
in Fig. 30.16c. In this case the circuit is overdamped, and q is given as a function
of time by the sum of two decreasing exponential functions.
R
R2 = 4L>C,
v¿
R
v = 11>LC21>2.
R = 0,
v¿ = B
1
LC - R2
4L2  1underdamped L-R-C series circuit)
v¿
R.
1>1LC21>2
R
R = 0,
e-1R>L2t
e-1R>2L2t
f
A
q = Ae-1R>2L2tcosaB
1
LC - R2
4L2 t + fb
4L>C,
R2
R)
R)
R = 0,
d2q
dt 2 + R
L
dq
dt +
1
LC q = 0
dq>dt
-iR - L di
dt - q
C = 0
t = 0
Q = CE
E
R;
R,
R
R,
1010
CHAPTER 30 Inductance
(b) Critically damped circuit (larger resistance R)
q
O
Q
t
O
t
(a) Underdamped circuit (small resistance R)
q
Q
(c) Overdamped circuit (very large resistance R)
q
O
Q
t
30.16 Graphs of capacitor charge as a
function of time in an L-R-C series circuit
with initial charge Q.
When switch S is in this position,
the emf charges the capacitor.
When switch S is moved to this
position, the capacitor discharges
through the resistor and inductor.
+q
-q
C
b
a
d
i
S
R
L
+
E
c
30.17 An L-R-C series circuit.

30.5 The L-R-C Series Circuit
1011
In the underdamped case the phase constant 
in the cosine function of 
Eq. (30.28) provides for the possibility of both an initial charge and an initial cur-
rent at time 
analogous to an underdamped harmonic oscillator given both
an initial displacement and an initial velocity (see Exercise 30.40).
We emphasize once more that the behavior of the L-R-C series circuit is com-
pletely analogous to that of the damped harmonic oscillator studied in Section
14.7. We invite you to verify, for example, that if you start with Eq. (14.41) and
substitute q for x, 
for m, 
for k, and 
for the damping constant b, the result
is Eq. (30.27). Similarly, the cross-over point between underdamping and over-
damping occurs at 
for the mechanical system and at 
for
the electrical one. Can you find still other aspects of this analogy?
The practical applications of the L-R-C series circuit emerge when we include
a sinusoidally varying source of emf in the circuit. This is analogous to the forced
oscillations that we discussed in Section 14.7, and there are analogous resonance
effects. Such a circuit is called an alternating-current (ac) circuit; the analysis of
ac circuits is the principal topic of the next chapter.
R2 = 4L>C
b2 = 4km
R
1>C
L
t = 0,
f
