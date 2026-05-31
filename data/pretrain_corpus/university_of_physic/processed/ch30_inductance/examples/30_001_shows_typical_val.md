Example 30.1 shows, typical val-
ues of mutual inductance can be in the millihenry (mH) or microhenry 
range.
Drawbacks and Uses of Mutual Inductance
Mutual inductance can be a nuisance in electric circuits, since variations in cur-
rent in one circuit can induce unwanted emfs in other nearby circuits. To mini-
mize these effects, multiple-circuit systems must be designed so that 
is as
small as possible; for example, two coils would be placed far apart or with their
planes perpendicular.
Happily, mutual inductance also has many useful applications. A transformer,
used in alternating-current circuits to raise or lower voltages, is fundamentally no
different from the two coils shown in Fig. 30.1. A time-varying alternating cur-
rent in one coil of the transformer produces an alternating emf in the other coil;
the value of 
which depends on the geometry of the coils, determines the
amplitude of the induced emf in the second coil and hence the amplitude of the
output voltage. (We’ll describe transformers in more detail in Chapter 31 after
we’ve discussed alternating current in greater depth.)
M,
M
1mH2
1 H = 1 Wb>A = 1 V # s>A = 1 Æ # s = 1 J>A2
M = N2£B2
i1
= N1£B1
i2   
E2 = -M di1
dt and E1 = -M di2
dt  
Example 30.1
Calculating mutual inductance
In one form of Tesla coil (a high-voltage generator popular in sci-
ence museums), a long solenoid with length l and cross-sectional
area 
is closely wound with 
turns of wire. A coil with 
turns
surrounds it at its center (Fig. 30.3). Find the mutual inductance M.
N2
N1
A
SOLUTION
IDENTIFY and SET UP: Mutual inductance occurs here because a
current in either coil sets up a magnetic field that causes a flux
through the other coil. From Example 28.9 (Section 28.7) we have
Continued

30.2 Self-Inductance and Inductors
In our discussion of mutual inductance we considered two separate, independent
circuits: A current in one circuit creates a magnetic field that gives rise to a flux
through the second circuit. If the current in the first circuit changes, the flux
through the second circuit changes and an emf is induced in the second circuit.
994
CHAPTER 30 Inductance
an expression [Eq. (28.23)] for the field magnitude 
at the center of
the solenoid (coil 1) in terms of the solenoid current 
This allows
us to determine the flux through a cross section of the solenoid. Since
there is no magnetic field outside a very long solenoid, this is also
equal to the flux 
through each turn of the outer coil (2). We then
use Eq. (30.5), in the form 
to determine 
EXECUTE: Equation (28.23) is expressed in terms of the number of
turns per unit length, which for solenoid (1) is 
. We
then have
n1 = N1>L
M.
M = N2£B2>i1,
£B2
i1.
B1
The flux through a cross section of the solenoid equals 
As we
mentioned above, this also equals the flux 
through each turn
of the outer coil, independent of its cross-sectional area. From 
Eq. (30.5), the mutual inductance 
is then
EVALUATE: The mutual inductance M of any two coils is propor-
tional to the product 
of their numbers of turns. Notice that M
depends only on the geometry of the two coils, not on the current.
Here’s a numerical example to give you an idea of magnitudes.
Suppose
turns, and 
Then
= 25 * 10-6 Wb>A = 25 * 10-6 H = 25 mH
M =
14p * 10-7 Wb>A # m211.0 * 10-3 m221100021102
0.50 m
N2 = 10 turns.
N1 = 1000
l = 0.50 m, A = 10 cm2 = 1.0 * 10-3 m2,
N1N2
M = N2£B2
i1
= N2B1A
i1
= N2
i1
m0N1i1
l
A = m0AN1N2
l
M
£B2
B1A.
B1 = m0n1i1 = m0N1i1
l
Cross-sectional area A
N1 turns
N2 turns
l
30.3 A long solenoid with cross-sectional area 
and 
turns is
surrounded at its center by a coil with 
turns.
N2
N1
A
