Sample Problem 30.07
Energy stored in a magnetic field

889
30-8 ENERGY DENSITY OF A MAGNETIC FIELD
Energy Density of a Magnetic Field
Consider a length l near the middle of a long solenoid of cross-sectional area A
carrying current i; the volume associated with this length is Al. The energy UB
stored by the length l of the solenoid must lie entirely within this volume because
the magnetic field outside such a solenoid is approximately zero. Moreover,
the stored energy must be uniformly distributed within the solenoid because the
magnetic field is (approximately) uniform everywhere inside.
Thus, the energy stored per unit volume of the field is
or, since
we have
(30-53)
Here L is the inductance of length l of the solenoid.
Substituting for L/l from Eq. 30-31, we find
(30-54)
where n is the number of turns per unit length. From Eq. 29-23 (B ! m0in) we can
write this energy density as
(magnetic energy density).
(30-55)
This equation gives the density of stored energy at any point where the magni-
tude of the magnetic field is B. Even though we derived it by considering the
special case of a solenoid, Eq. 30-55 holds for all magnetic fields, no matter how
they are generated.The equation is comparable to Eq. 25-25,
(30-56)
which gives the energy density (in a vacuum) at any point in an electric field.
Note that both uB and uE are proportional to the square of the appropriate field
magnitude, B or E.
uE ! 1
2´0E2,
uB ! B2
2m0
uB ! 1
2m0n2i2,
uB ! Li2
2Al ! L
l
i2
2A .
UB ! 1
2Li2,
uB ! UB
Al
30-8 ENERGY DENSITY OF A MAGNETIC FIELD
After reading this module, you should be able to . . .
30.37 Identify that energy is associated with any magnetic
field.
30.38 Apply the relationship between energy density uB of a
magnetic field and the magnetic field magnitude B.
Learning Objectives
●If B is the magnitude of a magnetic field at any point (in an inductor or anywhere else), the density of stored magnetic energy
at that point is
(magnetic energy density).
uB !
B2
2m0
Key Idea

890
CHAPTER 30
INDUCTION AND INDUCTANCE
Mutual Induction
In this section we return to the case of two interacting coils, which we first dis-
cussed in Module 30-1, and we treat it in a somewhat more formal manner. We
saw earlier that if two coils are close together as in Fig. 30-2, a steady current i in
one coil will set up a magnetic flux 0 through the other coil (linking the other
coil). If we change i with time, an emf # given by Faraday’s law appears in the sec-
ond coil; we called this process induction. We could better have called it mutual
induction, to suggest the mutual interaction of the two coils and to distinguish it
from self-induction, in which only one coil is involved.
Let us look a little more quantitatively at mutual induction. Figure 30-19a
shows two circular close-packed coils near each other and sharing a common
central axis.With the variable resistor set at a particular resistance R, the battery
produces a steady current i1 in coil 1. This current creates a magnetic field repre-
sented by the lines of 
in the figure. Coil 2 is connected to a sensitive meter but
contains no battery; a magnetic flux 021 (the flux through coil 2 associated with
the current in coil 1) links the N2 turns of coil 2.
We define the mutual inductance M21 of coil 2 with respect to coil 1 as
(30-57)
M21 ! N2021
i1
,
B
:
1
Checkpoint 7
The table lists the number of turns per unit length, current, and cross-sectional area
for three solenoids. Rank the solenoids according to the magnetic energy density
within them, greatest first.
Turns per 
Solenoid
Unit Length
Current
Area
a
2n1
i1
2A1
b
n1
2i1
A1
c
n1
i1
6A1
30-9 MUTUAL INDUCTION
After reading this module, you should be able to . . .
30.39 Describe the mutual induction of two coils and sketch
the arrangement.
30.40 Calculate the mutual inductance of one coil with respect
to a second coil (or some second current that is changing).
30.41 Calculate the emf induced in one coil by a second coil
in terms of the mutual inductance and the rate of change
of the current in the second coil.
Learning Objectives
●If coils 1 and 2 are near each other, a changing current in either coil can induce an emf in the other. This mutual induction is
described by
and
where M (measured in henries) is the mutual inductance. 
# 1 ! %M di2
dt ,
# 2 ! %M di1
dt
Key Idea

891
30-9 MUTUAL INDUCTION
which has the same form as Eq. 30-28,
L ! N0/i,
(30-58)
the definition of inductance.We can recast Eq. 30-57 as
M21i1 ! N2021.
(30-59)
If we cause i1 to vary with time by varying R, we have
(30-60)
The right side of this equation is, according to Faraday’s law, just the magnitude
of the emf #2 appearing in coil 2 due to the changing current in coil 1.Thus, with a
minus sign to indicate direction,
(30-61)
which you should compare with Eq. 30-35 for self-induction (# ! %L di/dt).
Interchange. Let us now interchange the roles of coils 1 and 2, as in Fig. 30-19b;
that is, we set up a current i2 in coil 2 by means of a battery, and this produces a
magnetic flux 012 that links coil 1. If we change i2 with time by varying R, we then
have, by the argument given above,
(30-62)
Thus, we see that the emf induced in either coil is proportional to the rate of
change of current in the other coil. The proportionality constants M21 and M12
seem to be different. However, they turn out to be the same, although we cannot
prove that fact here. Thus, we have
M21 ! M12 ! M,
(30-63)
and we can rewrite Eqs. 30-61 and 30-62 as
(30-64)
and
(30-65)
# 1 ! %M di2
dt .
# 2 ! %M di1
dt
# 1 ! %M12
di2
dt .
# 2 ! %M21
di1
dt ,
M21
di1
dt ! N2
d021
dt
.
Figure 30-19 Mutual induction. (a) The mag-
netic field 
produced by current i1 in coil
1 extends through coil 2. If i1 is varied (by
varying resistance R), an emf is induced in
coil 2 and current registers on the meter
connected to coil 2. (b) The roles of the
coils interchanged.
B
:
1
+ - 
i 1
N 1
Coil 1 
Coil 2 
B1
N 2   21 
Φ 
(a)
+ -
i 2
N 2
Coil 1
Coil 2
(b)
N 1   12
Φ
B2
B2
B1
R
R
0
0

892
CHAPTER 30
INDUCTION AND INDUCTANCE
Substituting Eq. 30-68 for B1 and 
for A2 in Eq. 30-67
yields
.
Substituting this result into Eq. 30-66, we find
(Answer)
(30-69)
(b) What is the value of M for N1 ! N2 ! 1200 turns,
R2 ! 1.1 cm, and R1 ! 15 cm?
Calculations: Equation 30-69 yields
(Answer)
Consider the situation if we reverse the roles of the two
coils-that is, if we produce a current i2 in the smaller coil
and try to calculate M from Eq. 30-57 in the form
The calculation of 012 (the nonuniform flux of the smaller
coil’s magnetic field encompassed by the larger coil) is not
simple. If we were to do the calculation numerically using
a computer, we would find M to be 2.3 mH, as above! This
emphasizes that Eq. 30-63 (M21 ! M12 ! M) is not obvious.
M ! N1012
i2
.
! 2.29 $ 10 %3 H % 2.3 mH. 
M ! (p)(4p $ 10 %7 H/m)(1200)(1200)(0.011 m)2
(2)(0.15 m)
M ! N2021
i1
! pm0N1N2R2
2
2R1
.
N2021 ! pm0N1N2R2
2 i1
2R1
pR2
2
Figure 30-20 shows two circular close-packed coils, the
smaller (radius R2, with N2 turns) being coaxial with the
larger (radius R1, with N1 turns) and in the same plane.
(a) Derive an expression for the mutual inductance M for
this arrangement of these two coils, assuming that R1 / R2.
KEY IDEA
The mutual inductance M for these coils is the ratio of the
flux linkage (N0) through one coil to the current i in the
other coil, which produces that flux linkage. Thus, we need
to assume that currents exist in the coils; then we need to
calculate the flux linkage in one of the coils.
Calculations: The magnetic field through the larger coil
due to the smaller coil is nonuniform in both magnitude and
direction; so the flux through the larger coil due to the
smaller coil is nonuniform and difficult to calculate.
However, the smaller coil is small enough for us to assume
that the magnetic field through it due to the larger coil is ap-
proximately uniform. Thus, the flux through it due to the
larger coil is also approximately uniform. Hence, to find M
we shall assume a current i1 in the larger coil and calculate
the flux linkage N2021 in the smaller coil:
(30-66)
The flux 021 through each turn of the smaller coil is,
from Eq. 30-2,
021 ! B1A2,
where B1 is the magnitude of the magnetic field at points
within the small coil due to the larger coil and 
is
the area enclosed by the turn. Thus, the flux linkage in the
smaller coil (with its N2 turns) is
N2021 ! N2B1A2.
(30-67)
To find B1 at points within the smaller coil, we can use
Eq. 29-26,
with z set to 0 because the smaller coil is in the plane of the
larger coil.That equation tells us that each turn of the larger
coil produces a magnetic field of magnitude m0i1/2R1 at
points within the smaller coil. Thus, the larger coil (with its
N1 turns) produces a total magnetic field of magnitude
(30-68)
at points within the smaller coil.
B1 ! N1
m0i1
2R1
B(z) !
m0iR2
2(R2 & z2)3/2 ,
A2 (! pR2
2)
M ! N2021
i1
.
Additional examples, video, and practice available at WileyPLUS
