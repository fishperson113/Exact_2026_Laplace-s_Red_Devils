Example 22.2
Electric flux through a cube
An imaginary cubical surface of side 
is in a region of uniform
electric field 
Find the electric flux through each face of the cube
and the total flux through the cube when (a) it is oriented with two
of its faces perpendicular to 
(Fig. 22.8a) and (b) the cube is
turned by an angle about a vertical axis (Fig. 22.8b).
SOLUTION
IDENTIFY and SET UP: Since 
is uniform and each of the six
faces of the cube is flat, we find the flux 
through each face
using Eqs. (22.3) and (22.4). The total flux through the cube is the
sum of the six individual fluxes.
EXECUTE: (a) Figure 22.8a shows the unit vectors 
through 
for
each face; each unit vector points outward from the cube’s closed
surface. The angle between 
and 
is 180°, the angle between E
S
nN 1
E
S
nN 6
nN 1
£Ei
E
S
u
E
S
E
S.
L
and 
is 0°, and the angle between 
and each of the other four
unit vectors is 90°. Each face of the cube has area 
so the fluxes
through the faces are
The flux is negative on face 1, where 
is directed into the cube,
and positive on face 2, where 
is directed out of the cube. The
total flux through the cube is
(b) The field 
is directed into faces 1 and 3, so the fluxes
through them are negative; 
is directed out of faces 2 and 4, so the
fluxes through them are positive. We find
The total flux 
through the surface of the cube is again zero.
EVALUATE: We came to the same conclusion in our discussion of
Fig. 22.3c: There is zero net flux of a uniform electric field through
a closed surface that contains no electric charge.
£E = £E1 + £E2 + £E3 + £E4 + £E5 + £E6
£E5 = £E6 = EL2cos90° = 0
£E4 = E
S # nN 4 A = EL2cos190° - u2 = +EL2sin u
£E3 = E
S # nN 3 A = EL2cos190° + u2 = -EL2sin u
£E2 = E
S # nN 2 A = +EL2cosu
£E1 = E
S # nN 1A = EL2cos1180° - u2 = -EL2cos u
E
S
E
S
= -EL2 + EL2 + 0 + 0 + 0 + 0 = 0
£E = £E1 + £E2 + £E3 + £E4 + £E5 + £E6
E
S
E
S
£E3 = £E4 = £E5 = £E6 = EL2cos90° = 0
£E2 = E
S # nN 2A = EL2cos0° = +EL2
£E1 = E
S # nN 1A = EL2cos180° = -EL2
L2,
E
S
nN 2
(a)
E
r
^n5
^n3
^n2
^n6
^n1
^n4
(b)
90° 2 u
u
E
r
^n5
^n3
^n2
^n6
^n1
^n4
22.8 Electric flux of a uniform field 
through a cubical box of
side 
in two orientations.
L
E
S
Example 22.3
Electric flux through a sphere
A point charge 
is surrounded by an imaginary
sphere of radius 
centered on the charge (Fig. 22.9).
Find the resulting electric flux through the sphere.
SOLUTION
IDENTIFY and SET UP: The surface is not flat and the electric field
is not uniform, so to calculate the electric flux (our target variable)
r = 0.20 m
q = +3.0 mC
we must use the general definition, Eq. (22.5). We use Eq. (22.5) to
calculate the electric flux (our target variable). Because the sphere
is centered on the point charge, at any point on the spherical sur-
face, 
is directed out of the sphere perpendicular to the surface.
The positive direction for both 
and 
is outward, so 
and the flux through a surface element 
is 
This
greatly simplifies the integral in Eq. (22.5).
Continued
E
S # dA
S = E dA.
dA
E = E
E
nN
E
S

22.3 Gauss’s Law
Gauss’s law is an alternative to Coulomb’s law. While completely equivalent to
Coulomb’s law, Gauss’s law provides a different way to express the relationship
between electric charge and electric field. It was formulated by Carl Friedrich Gauss
(1777-1855), one of the greatest mathematicians of all time (Fig. 22.10).
Point Charge Inside a Spherical Surface
Gauss’s law states that the total electric flux through any closed surface (a surface
enclosing a definite volume) is proportional to the total (net) electric charge
inside the surface. In Section 22.1 we observed this relationship qualitatively for
certain special cases; now we’ll develop it more rigorously. We’ll start with the
field of a single positive point charge 
The field lines radiate out equally in all
directions. We place this charge at the center of an imaginary spherical surface
with radius 
The magnitude 
of the electric field at every point on the surface
is given by
At each point on the surface, 
is perpendicular to the surface, and its magnitude
is the same at every point, just as in Example 22.3 (Section 22.2). The total elec-
tric flux is the product of the field magnitude 
and the total area 
of
the sphere:
(22.6)
The flux is independent of the radius R of the sphere. It depends only on the
charge enclosed by the sphere.
q
£E = EA =
1
4pP0
q
R2 14pR22 = q
P0
A = 4pR2
E
E
S
E =
1
4pP0
q
R2
E
R.
q.
732
CHAPTER 22 Gauss’s Law
EXECUTE: We must evaluate the integral of Eq. (22.5), 
. At any point on the sphere of radius r the electric field has
the same magnitude 
. Hence E can be taken outside
the integral, which becomes 
where A is the
£E = E1dA = EA,
E = q>4pP0r 2
1E dA
£E =
area of the spherical surface: 
. Hence the total flux
through the sphere is
EVALUATE: The radius 
of the sphere cancels out of the result for
We would have obtained the same flux with a sphere of radius
2.0 m or 200 m. We came to essentially the same conclusion in our
discussion of Fig. 22.4 in Section 22.1, where we considered rectan-
gular closed surfaces of two different sizes enclosing a point charge.
There we found that the flux of 
was independent of the size of the
surface; the same result holds true for a spherical surface. Indeed,
the flux through any surface enclosing a single point charge is inde-
pendent of the shape or size of the surface, as we’ll soon see.
E
S
£E.
r
=
3.0 * 10-6 C
8.85 * 10-12 C2>N # m2 = 3.4 * 105 N # m2>C
£E = EA =
q
4pP0r 2 4pr 2 = q
P0
A = 4pr 2
E
S
q
r
dA
S
22.9 Electric flux through a sphere centered on a point charge.
Test Your Understanding of Section 22.2
Rank the following sur-
faces in order from most positive to most negative electric flux. (i) a flat rectangu-
lar surface with vector area 
in a uniform electric field
(ii) a flat circular surface with vector area 
in a uniform electric field
(iii) a flat square surface with vector area
in a uniform electric field 
(iv) a flat oval surface with vector area 
in a uniform 
electric field 
❙
E
S  14.0 N>C2ıN  12.0 N>C2≥N.
A
S  13.0 m22ıN  17.0 m22≥N
E
S  14.0 N>C2ıN  12.0 N>C2≥N;
13.0 m22ıN  17.0 m22≥N
A
S 
12.0 N>C2≥N;
E
S  14.0 N>C2ıN +
A
S  13.0 m22≥N
E
S  14.0 N>C2≥N;
A
S  16.0 m22ıN
22.10 Carl Friedrich Gauss helped
develop several branches of mathematics,
including differential geometry, real analy-
sis, and number theory. The “bell curve” of
statistics is one of his inventions. Gauss
also made state-of-the-art investigations of
the earth’s magnetism and calculated the
orbit of the first asteroid to be discovered.

22.3 Gauss’s Law
733
We can also interpret this result in terms of field lines. Figure 22.11 shows two
spheres with radii 
and 
centered on the point charge 
Every field line that
passes through the smaller sphere also passes through the larger sphere, so the
total flux through each sphere is the same.
What is true of the entire sphere is also true of any portion of its surface. In
Fig. 22.11 an area 
is outlined on the sphere of radius 
and then projected
onto the sphere of radius 
by drawing lines from the center through points on
the boundary of 
The area projected on the larger sphere is clearly 4 
But
since the electric field due to a point charge is inversely proportional to 
the
field magnitude is as great on the sphere of radius 
as on the sphere of radius
Hence the electric flux is the same for both areas and is independent of the
radius of the sphere.
Point Charge Inside a Nonspherical Surface
This projection technique shows us how to extend this discussion to nonspherical
surfaces. Instead of a second sphere, let us surround the sphere of radius 
by a
surface of irregular shape, as in Fig. 22.12a. Consider a small element of area 
on the irregular surface; we note that this area is larger than the corresponding
element on a spherical surface at the same distance from 
If a normal to 
makes an angle 
with a radial line from 
two sides of the area projected onto
the spherical surface are foreshortened by a factor 
(Fig. 22.12b). The other
two sides are unchanged. Thus the electric flux through the spherical surface ele-
ment is equal to the flux 
through the corresponding irregular surface
element.
We can divide the entire irregular surface into elements 
compute the elec-
tric flux 
for each, and sum the results by integrating, as in Eq. (22.5).
Each of the area elements projects onto a corresponding spherical surface ele-
ment. Thus the total electric flux through the irregular surface, given by any of
the forms of Eq. (22.5), must be the same as the total flux through a sphere,
which Eq. (22.6) shows is equal to 
Thus, for the irregular surface,
(22.7)
Equation (22.7) holds for a surface of any shape or size, provided only that it is a
closed surface enclosing the charge 
The circle on the integral sign reminds us
that the integral is always taken over a closed surface.
The area elements 
and the corresponding unit vectors always point out of
the volume enclosed by the surface. The electric flux is then positive in areas
nN
dA
S
q.
£E =
C
E
S # dA
S = q
P0
q>P0.
E dAcosf
dA,
E dAcosf
cosf
q,
f
dA
q.
dA
R
R.
2R
1
4
r 2,
dA.
dA.
2R
R
dA
q.
2R
R
2
The same number of field lines and the same
flux pass through both of these area elements.
R
4 dA
dA
q
R
E
S
22.11 Projection of an element of area
of a sphere of radius 
onto a concentric
sphere of radius 
The projection multi-
plies each linear dimension by 2, so the
area element on the larger sphere is 4 dA.
2R.
R
dA
(a) The outward normal to the
       surface makes an angle f
       with the direction of E.
dA
E'
dA cos f
(b)
f
f
E
S
S
q
R
r
q
E'
The projection of the
area element dA onto
the spherical surface
is dA cos f.
dA
f
E
S
22.12 Calculating the electric flux
through a nonspherical surface.

where the electric field points out of the surface and negative where it points
inward. Also, 
is positive at points where 
points out of the surface and nega-
tive at points where 
points into the surface.
If the point charge in Fig. 22.12 is negative, the 
field is directed radially
inward; the angle 
is then greater than 
its cosine is negative, and the
integral in Eq. (22.7) is negative. But since 
is also negative, Eq. (22.7) still
holds.
For a closed surface enclosing no charge,
This is the mathematical statement that when a region contains no charge, any
field lines caused by charges outside the region that enter on one side must leave
again on the other side. (In Section 22.1 we came to the same conclusion by con-
sidering the special case of a rectangular box in a uniform field.) Figure 22.13
illustrates this point. Electric field lines can begin or end inside a region of space
only when there is charge in that region.
General Form of Gauss’s Law
Now comes the final step in obtaining the general form of Gauss’s law. Suppose
the surface encloses not just one point charge 
but several charges 
The total (resultant) electric field 
at any point is the vector sum of the 
fields of the individual charges. Let 
be the total charge enclosed by the sur-
face: 
Also let 
be the total field at the position
of the surface area element 
and let 
be its component perpendicular to the
plane of that element (that is, parallel to 
). Then we can write an equation like
Eq. (22.7) for each charge and its corresponding field and add the results. When
we do, we obtain the general statement of Gauss’s law:
(Gauss’s law)
(22.8)
The total electric flux through a closed surface is equal to the total (net) electric
charge inside the surface, divided by
CAUTION
Gaussian surfaces are imaginary Remember that the closed surface in
Gauss’s law is imaginary; there need not be any material object at the position of the sur-
face. We often refer to a closed surface used in Gauss’s law as a Gaussian surface. ❙
Using the definition of 
and the various ways to express electric flux given
in Eq. (22.5), we can express Gauss’s law in the following equivalent forms:
(22.9)
As in Eq. (22.5), the various forms of the integral all express the same thing, the
total electric flux through the Gaussian surface, in different terms. One form is
sometimes more convenient than another.
As an example, Fig. 22.14a shows a spherical Gaussian surface of radius 
around a positive point charge 
The electric field points out of the Gaussian sur-
face, so at every point on the surface 
is in the same direction as 
and
is equal to the field magnitude 
Since 
is the same at all points
E
E = q>4pP0r 2.
E
f = 0,
dA
S,
E
S
+q.
r
(various forms 
of Gauss’s law)
£E =
C
Ecosf dA =
C
E dA =
C
E
S # dA
S = Qencl
P0
Qencl
`0.
£E =
C
E
S # dA
S = Qencl
P0
dA
S
E
dA
S,
E
S
Qencl = q1 + q2 + q3 + Á  .
Qencl
E
S
E
S
q3, Á .
q2,
q1,
q
£E =
C
E
S # dA
S = 0
q
90°,
f
E
S
E
S
E
S
E
734
CHAPTER 22 Gauss’s Law
E
S
Field line
entering surface
Same field line
leaving surface
22.13 A point charge outside a closed
surface that encloses no charge. If an
electric field line from the external
charge enters the surface at one point,
it must leave at another.

22.3 Gauss’s Law
735
on the surface, we can take it outside the integral in Eq. (22.9). Then the remaining
integral is 
the area of the sphere. Hence Eq. (22.9) becomes
The enclosed charge 
is just the charge 
so this agrees with Gauss’s law.
If the Gaussian surface encloses a negative point charge as in Fig. 22.14b, then 
points into the surface at each point in the direction opposite 
Then 
and 
is equal to the negative of the field magnitude: 
Equation (22.9) then becomes
This again agrees with Gauss’s law because the enclosed charge in Fig. 22.14b is
In Eqs. (22.8) and (22.9), 
is always the algebraic sum of all the positive
and negative charges enclosed by the Gaussian surface, and 
is the total field at
each point on the surface. Also note that in general, this field is caused partly by
charges inside the surface and partly by charges outside. But as Fig. 22.13 shows,
the outside charges do not contribute to the total (net) flux through the surface. So
Eqs. (22.8) and (22.9) are correct even when there are charges outside the surface
that contribute to the electric field at the surface. When 
the total flux
through the Gaussian surface must be zero, even though some areas may have
positive flux and others may have negative flux (see Fig. 22.3b).
Gauss’s law is the definitive answer to the question we posed at the beginning
of Section 22.1: “If the electric field pattern is known in a given region, what
can we determine about the charge distribution in that region?” It provides a
relationship between the electric field on a closed surface and the charge distri-
bution within that surface. But in some cases we can use Gauss’s law to answer
the reverse question: “If the charge distribution is known, what can we deter-
mine about the electric field that the charge distribution produces?” Gauss’s law
may seem like an unappealing way to address this question, since it may look as
though evaluating the integral in Eq. (22.8) is a hopeless task. Sometimes it is,
but other times it is surprisingly easy. Here’s an example in which no integration
is involved at all; we’ll work out several more examples in the next section.
Qencl = 0,
E
S
Qencl
Qencl = -q.
£E =
C
E dA =
C
a
-q
4pP0r 2 b dA =
-q
4pP0r 2 C
dA =
-q
4pP0r 2 4pr 2 = -q
P0
- ƒ -qƒ>4pP0r 2 = -q>4pP0r 2.
E = -E =
E
180°
f =
dA
S.
E
S
+q,
Qencl
£E =
C
E dA =
C
a
q
4pP0r 2 b dA =
q
4pP0r 2 C
dA =
q
4pP0r 2  4pr 2 = q
P0
1dA = A = 4pr 2,
(a) Gaussian surface around positive charge:
positive (outward) flux
1q
r
dA
E
S
S
(b) Gaussian surface around negative charge:
negative (inward) flux
2q
r
dA
E
S
S
22.14 Spherical Gaussian surfaces
around (a) a positive point charge and 
(b) a negative point charge.
Conceptual
