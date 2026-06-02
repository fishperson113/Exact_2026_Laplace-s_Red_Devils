Example 24.9
Two ways to calculate energy stored in a capacitor
The spherical capacitor described in Example 24.3 (Section 24.1)
has charges 
and 
on its inner and outer conductors. Find
the electric potential energy stored in the capacitor (a) by using the
capacitance 
found in Example 24.3 and (b) by integrating the
electric-field energy density u.
SOLUTION
IDENTIFY and SET UP: We can determine the energy U stored in a
capacitor in two ways: in terms of the work done to put the charges
on the two conductors, and in terms of the energy in the electric
field between the conductors. The descriptions are equivalent, so
they must give us the same result. In Example 24.3 we found the
capacitance 
and the field magnitude 
in the space between the
conductors. (The electric field is zero inside the inner sphere and is
also zero outside the inner surface of the outer sphere, because a
Gaussian surface with radius 
or 
encloses zero net
r 7 rb
r 6 ra
E
C
C
-Q
+Q
charge. Hence the energy density is nonzero only in the space
between the spheres, 
.) In part (a) we use Eq. (24.9) to
find 
In part (b) we use Eq. (24.11) to find 
which we integrate
over the volume between the spheres to find U.
EXECUTE: (a) From Example 24.3, the spherical capacitor has
capacitance
where 
and 
are the radii of the inner and outer conducting
spheres, respectively. From Eq. (24.9) the energy stored in this
capacitor is
Continued
U = Q2
2C =
Q2
8pP0
rb - ra
rarb
rb
ra
C = 4pP0
rarb
rb - ra
u,
U.
ra 6 r 6 rb

24.4 Dielectrics
Most capacitors have a nonconducting material, or dielectric, between their con-
ducting plates. A common type of capacitor uses long strips of metal foil for the
plates, separated by strips of plastic sheet such as Mylar. A sandwich of these
materials is rolled up, forming a unit that can provide a capacitance of several
microfarads in a compact package (Fig. 24.13).
Placing a solid dielectric between the plates of a capacitor serves three func-
tions. First, it solves the mechanical problem of maintaining two large metal
sheets at a very small separation without actual contact.
Second, using a dielectric increases the maximum possible potential differ-
ence between the capacitor plates. As we described in Section 23.3, any insulat-
ing material, when subjected to a sufficiently large electric field, experiences a
partial ionization that permits conduction through it. This is called dielectric
breakdown. Many dielectric materials can tolerate stronger electric fields with-
out breakdown than can air. Thus using a dielectric allows a capacitor to sustain
a higher potential difference 
and so store greater amounts of charge and
energy.
Third, the capacitance of a capacitor of given dimensions is greater when
there is a dielectric material between the plates than when there is vacuum. We
can demonstrate this effect with the aid of a sensitive electrometer, a device that
measures the potential difference between two conductors without letting any
appreciable charge flow from one to the other. Figure 24.14a shows an electrom-
eter connected across a charged capacitor, with magnitude of charge 
on each
plate and potential difference 
When we insert an uncharged sheet of dielec-
tric, such as glass, paraffin, or polystyrene, between the plates, experiment shows
that the potential difference decreases to a smaller value 
(Fig. 24.14b). When
we remove the dielectric, the potential difference returns to its original value 
showing that the original charges on the plates have not changed.
The original capacitance 
is given by 
and the capacitance 
with the dielectric present is 
The charge 
is the same in both cases,
and 
is less than 
so we conclude that the capacitance 
with the dielectric
present is greater than 
When the space between plates is completely filled by
the dielectric, the ratio of 
to 
(equal to the ratio of 
to 
) is called the
dielectric constant of the material, 
(24.12)
K = C
C0  (definition of dielectric constant)
K:
V
V0
C0
C
C0.
C
V0,
V
Q
C = Q>V.
C
C0 = Q>V0,
C0
V0,
V
V0.
Q
V
800
CHAPTER 24 Capacitance and Dielectrics
(b) The electric field in the region 
between the two
conducting spheres has magnitude 
The energy
density in this region is
The energy density is not uniform; it decreases rapidly with
increasing distance from the center of the capacitor. To find the
total electric-field energy, we integrate 
(the energy per unit vol-
ume) over the region 
. We divide this region into
spherical shells of radius 
surface area 
thickness 
and
volume 
. Then
dV = 4pr 2 dr
dr,
4pr 2,
r,
ra 6 r 6 rb
u
u = 1
2 P0E2 = 1
2 P0a
Q
4pP0r 2b
2
=
Q2
32p2P0r 4
E = Q>4pP0r 2.
ra 6 r 6 rb
EVALUATE: Electric potential energy can be regarded as being
associated with either the charges, as in part (a), or the field, as in
part (b); the calculated amount of stored energy is the same in
either case.
=
Q2
8pP0
rb - ra
rarb
=
Q2
8pP0 L
rb
ra
dr
r 2 =
Q2
8pP0
a - 1
rb
+ 1
ra
b
U =
L
u dV =
L
rb
ra
a
Q2
32p2P0r 4 b4pr 2dr
Test Your Understanding of Section 24.3
You want to connect a 
capacitor and an 
capacitor. With which type of connection will the 
capacitor have a greater amount of stored energy than the 
capacitor? (i) series;
(ii) parallel; (iii) either series or parallel; (iv) neither series nor parallel.
❙
8-mF
4-mF
8-mF
4-mF
Conductor
(metal foil)
Conductor
(metal foil)
Dielectric
(plastic sheets)
24.13 A common type of capacitor uses
dielectric sheets to separate the conductors.

24.4 Dielectrics
801
When the charge is constant, 
and 
In this case,
Eq. (24.12) can be rewritten as
(24.13)
With the dielectric present, the potential difference for a given charge 
is
reduced by a factor 
The dielectric constant 
is a pure number. Because 
is always greater than
is always greater than unity. Some representative values of 
are given in
Table 24.1. For vacuum, 
by definition. For air at ordinary temperatures
and pressures, 
is about 1.0006; this is so nearly equal to 1 that for most pur-
poses an air capacitor is equivalent to one in vacuum. Note that while water has a
very large value of 
it is usually not a very practical dielectric for use in capac-
itors. The reason is that while pure water is a very poor conductor, it is also an
excellent ionic solvent. Any ions that are dissolved in the water will cause charge
to flow between the capacitor plates, so the capacitor discharges.
K,
K
K = 1
K
K
C0,
C
K
K.
Q
V = V0
K  1when Q is constant2
C>C0 = V0>V.
Q = C0V0 = CV
Table 24.1 Values of Dielectric Constant K at 20 C
Material
Material
Vacuum
1
Polyvinyl chloride
3.18
Air (1 atm)
1.00059
Plexiglas®
3.40
Air (100 atm)
1.0548
Glass
5-10
Teflon
2.1
Neoprene
6.70
Polyethylene
2.25
Germanium
16
Benzene
2.28
Glycerin
42.5
Mica
3-6
Water
80.4
Mylar
3.1
Strontium titanate
310
K
K
°
No real dielectric is a perfect insulator. Hence there is always some leakage
current between the charged plates of a capacitor with a dielectric. We tacitly
ignored this effect in Section 24.2 when we derived expressions for the equiva-
lent capacitances of capacitors in series, Eq. (24.5), and in parallel, Eq. (24.7).
But if a leakage current flows for a long enough time to substantially change the
charges from the values we used to derive Eqs. (24.5) and (24.7), those equations
may no longer be accurate.
Induced Charge and Polarization
When a dielectric material is inserted between the plates while the charge is kept
constant, the potential difference between the plates decreases by a factor 
Therefore the electric field between the plates must decrease by the same factor.
If 
is the vacuum value and 
is the value with the dielectric, then
(24.14)
Since the electric-field magnitude is smaller when the dielectric is present, the
surface charge density (which causes the field) must be smaller as well. The sur-
face charge on the conducting plates does not change, but an induced charge of
the opposite sign appears on each surface of the dielectric (Fig. 24.15). The
dielectric was originally electrically neutral and is still neutral; the induced sur-
face charges arise as a result of redistribution of positive and negative charge
within the dielectric material, a phenomenon called polarization. We first
encountered polarization in Section 21.2, and we suggest that you reread the dis-
cussion of Fig. 21.8. We will assume that the induced surface charge is directly
proportional to the electric-field magnitude 
in the material; this is indeed the
case for many common dielectrics. (This direct proportionality is analogous to
E
E = E0
K  1when Q is constant2
E
E0
K.
+
-
+
-
Adding the dielectric
reduces the potential
difference across the
capacitor.
V0
Q
Vacuum
Electrometer
(measures potential
difference across
plates)
(a)
2Q
V
2Q
Dielectric
Q
(b)
24.14 Effect of a dielectric between the
plates of a parallel-plate capacitor. (a) With
a given charge, the potential difference is
(b) With the same charge but with a
dielectric between the plates, the potential
difference 
is smaller than V0.
V
V0.
(a)
(b)
For a given charge density s, the induced
charges on the dielectric’s surfaces reduce the
electric field between the plates.
s
2s
s
2s
E0
S
Vacuum
s
2s
2si
si
2si
si
s
2s
E
S
Dielectric
Induced
charges
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
+
+
+
+
+
+
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
24.15 Electric field lines with 
(a) vacuum between the plates and 
(b) dielectric between the plates.

Hooke’s law for a spring.) In that case, 
is a constant for any particular material.
When the electric field is very strong or if the dielectric is made of certain crys-
talline materials, the relationship between induced charge and the electric field
can be more complex; we won’t consider such cases here.
We can derive a relationship between this induced surface charge and the
charge on the plates. Let’s denote the magnitude of the charge per unit area
induced on the surfaces of the dielectric (the induced surface charge density) by
The magnitude of the surface charge density on the capacitor plates is 
as
usual. Then the net surface charge on each side of the capacitor has magnitude
as shown in Fig. 24.15b. As we found in Example 21.12 (Section
21.5) and in Example 22.8 (Section 22.4), the field between the plates is related
to the net surface charge density by 
Without and with the dielectric,
respectively, we have
(24.15)
Using these expressions in Eq. (24.14) and rearranging the result, we find
(24.16)
This equation shows that when 
is very large, 
is nearly as large as 
In this
case, 
nearly cancels 
and the field and potential difference are much smaller
than their values in vacuum.
The product 
is called the permittivity of the dielectric, denoted by 
(24.17)
In terms of we can express the electric field within the dielectric as
(24.18)
The capacitance when the dielectric is present is given by
(parallel-plate capacitor, 
dielectric between plates)
(24.19)
We can repeat the derivation of Eq. (24.11) for the energy density in an elec-
tric field for the case in which a dielectric is present. The result is
(24.20)
In empty space, where 
and Eqs. (24.19) and (24.20) reduce to
Eqs. (24.2) and (24.11), respectively, for a parallel-plate capacitor in vacuum. For
this reason, 
is sometimes called the “permittivity of free space” or the “permit-
tivity of vacuum.” Because 
is a pure number, 
and 
have the same units,
or
Equation (24.19) shows that extremely high capacitances can be obtained with
plates that have a large surface area 
and are separated by a small distance by
a dielectric with a large value of 
In an electrolytic double-layer capacitor, tiny
carbon granules adhere to each plate: The value of 
is the combined surface area
of the granules, which can be tremendous. The plates with granules attached are
separated by a very thin dielectric sheet. A capacitor of this kind can have a
capacitance of 5000 farads yet fit in the palm of your hand (compare Example
24.1 in Section 24.1).
Several practical devices make use of the way in which a capacitor responds
to a change in dielectric constant. One example is an electric stud finder, used by
A
K.
d
A
F>m.
C2>N # m2
P0
P
K
P0
P = P0
K = 1,
u = 1
2KP0E2 = 1
2 PE2  (electric energy density in a dielectric)
u
C = KC0 = KP0
A
d = P A
d
E = s
P
P
P = KP0  1definition of permittivity2
P:
KP0
s,
si
s.
si
K
si = sa1 - 1
K b  (induced surface charge density)
E0 = s
P0  E = s - si
P0
E = snet>P0.
1s - si2,
s,
si.
K
802
CHAPTER 24 Capacitance and Dielectrics

24.4 Dielectrics
803
home repair workers to locate metal studs hidden behind a wall’s surface. It con-
sists of a metal plate with associated circuitry. The plate acts as one half of a
capacitor, with the wall acting as the other half. If the stud finder moves over a
metal stud, the effective dielectric constant for the capacitor changes, changing
the capacitance and triggering a signal.
Problem-Solving Strategy 24.2
Dielectrics
IDENTIFY the relevant concepts: The relationships in this section
are useful whenever there is an electric field in a dielectric, such as
a dielectric between charged capacitor plates. Typically you must
relate the potential difference 
between the plates, the electric
field magnitude E in the capacitor, the charge density 
on the
capacitor plates, and the induced charge density 
on the surfaces
of the capacitor.
SET UP the problem using the following steps:
1. Make a drawing of the situation.
2. Identify the target variables, and choose which equations from
this section will help you solve for those variables.
EXECUTE the solution as follows:
1. In problems such as the next example, it is easy to get lost in a
blizzard of formulas. Ask yourself at each step what kind of
si
s
Vab
quantity each symbol represents. For example, distinguish
clearly between charges and charge densities, and between
electric fields and electric potential differences.
2. Check for consistency of units. Distances must be in meters. A
microfarad is 
farad, and so on. Don’t confuse the numeri-
cal value of 
with the value of 
Electric-field magni-
tude can be expressed in both 
The units of 
are 
or 
EVALUATE your answer: With a dielectric present, (a) the capaci-
tance is greater than without a dielectric; (b) for a given charge on
the capacitor, the electric field and potential difference are less
than without a dielectric; and (c) the magnitude of the induced sur-
face charge density 
on the dielectric is less than that of the
charge density 
on the capacitor plates.
s
si
F>m.
C2>N # m2
P0
N>C and V>m.
1>4pP0.
P0
10-6
