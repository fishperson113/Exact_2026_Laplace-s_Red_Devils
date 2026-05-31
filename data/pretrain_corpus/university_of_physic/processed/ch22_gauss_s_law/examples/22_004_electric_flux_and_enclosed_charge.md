Example 22.4
Electric flux and enclosed charge
Figure 22.15 shows the field produced by two point charges 
and 
(an electric dipole). Find the electric flux through each of
the closed surfaces 
and D.
C,
B,
A,
-q
+q
SOLUTION
Gauss’s law, Eq. (22.8), says that the total electric flux through a
closed surface is equal to the total enclosed charge divided by 
In
Continued
P0.

22.4 Applications of Gauss’s Law
Gauss’s law is valid for any distribution of charges and for any closed surface.
Gauss’s law can be used in two ways. If we know the charge distribution, and if it
has enough symmetry to let us evaluate the integral in Gauss’s law, we can find
the field. Or if we know the field, we can use Gauss’s law to find the charge dis-
tribution, such as charges on conducting surfaces.
In this section we present examples of both kinds of applications. As you
study them, watch for the role played by the symmetry properties of each system.
We will use Gauss’s law to calculate the electric fields caused by several simple
charge distributions; the results are collected in a table in the chapter summary.
In practical problems we often encounter situations in which we want to know
the electric field caused by a charge distribution on a conductor. These calcula-
tions are aided by the following remarkable fact: When excess charge is placed
on a solid conductor and is at rest, it resides entirely on the surface, not in the
interior of the material. (By excess we mean charges other than the ions and free
electrons that make up the neutral conductor.) Here’s the proof. We know from
Section 21.4 that in an electrostatic situation (with all charges at rest) the electric
field 
at every point in the interior of a conducting material is zero. If 
were
not zero, the excess charges would move. Suppose we construct a Gaussian sur-
face inside the conductor, such as surface 
in Fig. 22.17. Because 
every-
where on this surface, Gauss’s law requires that the net charge inside the surface
is zero. Now imagine shrinking the surface like a collapsing balloon until it
encloses a region so small that we may consider it as a point 
then the charge at
that point must be zero. We can do this anywhere inside the conductor, so there
can be no excess charge at any point within a solid conductor; any excess charge
must reside on the conductor’s surface. (This result is for a solid conductor. In the
next section we’ll discuss what can happen if the conductor has cavities in its
interior.) We will make use of this fact frequently in the examples that follow.
P;
E
S  0
A
E
S
E
S
736
CHAPTER 22 Gauss’s Law
Test Your Understanding of Section 22.3
Figure 22.16 shows six point
charges that all lie in the same plane. Five Gaussian surfaces-
and
-each enclose part of this plane, and Fig. 22.16 shows the intersection of each
surface with the plane. Rank these five surfaces in order of the electric flux
through them, from most positive to most negative.
❙
S5
S1, S2, S3, S4,
11.0 mC
19.0 mC
S1
S2
S4
S3
S5
210.0 mC
27.0 mC
15.0 mC
18.0 mC
22.16 Five Gaussian surfaces and six
point charges.
Conductor
(shown in
cross section)
Charge on surface
of conductor
Gaussian surface A
inside conductor
(shown in
cross section)
22.17 Under electrostatic conditions
(charges not in motion), any excess charge
on a solid conductor resides entirely on the
conductor’s surface.
Fig. 22.15, surface 
(shown in red) encloses the positive charge, so
surface 
(in blue) encloses the negative charge, 
so 
surface 
(in purple) encloses both charges, 
so 
and surface 
(in yellow) encloses no
charges, so 
Hence, without having to do any integration,
we have 
and 
These results depend only on the charges enclosed within each
Gaussian surface, not on the precise shapes of the surfaces.
We can draw similar conclusions by examining the electric field
lines. All the field lines that cross surface A are directed out of the
surface, so the flux through A must be positive. Similarly, the flux
through B must be negative since all of the field lines that cross that
surface point inward. For both surface C and surface D, there are as
many field lines pointing into the surface as there are field lines
pointing outward, so the flux through each of these surfaces is zero.
£ED = 0.
£EC =
£EB = -q>P0,
+q>P0,
£EA =
Qencl = 0.
D
Qencl = +q + 1-q2 = 0;
C
Qencl = -q;
B
Qencl = +q;
A
C
D
B
A
2q
E
S
1q
22.15 The net number of field lines leaving a closed surface is
proportional to the total charge enclosed by that surface.

22.4 Applications of Gauss’s Law
737
Problem-Solving Strategy 22.1
Gauss’s Law
IDENTIFY the relevant concepts: Gauss’s law is most useful when
the charge distribution has spherical, cylindrical, or planar symme-
try. In these cases the symmetry determines the direction of . Then
Gauss’s law yields the magnitude of 
if we are given the charge
distribution, and vice versa. In either case, begin the analysis by
asking the question: What is the symmetry?
SET UP the problem using the following steps:
1. List the known and unknown quantities and identify the target
variable.
2. Select the appropriate closed, imaginary Gaussian surface. For
spherical symmetry, use a concentric spherical surface. For
cylindrical symmetry, use a coaxial cylindrical surface with flat
ends perpendicular to the axis of symmetry (like a soup can).
For planar symmetry, use a cylindrical surface (like a tuna can)
with its flat ends parallel to the plane.
EXECUTE the solution as follows:
1. Determine the appropriate size and placement of your Gaussian
surface. To evaluate the field magnitude at a particular point,
the surface must include that point. It may help to place one end
of a can-shaped surface within a conductor, where 
and there-
fore 
are zero, or to place its ends equidistant from a charged
plane.
2. Evaluate the integral 
in Eq. (22.9). In this equation 
is the perpendicular component of the total electric field at each
point on the Gaussian surface. A well-chosen Gaussian surface
should make integration trivial or unnecessary. If the surface
comprises several separate surfaces, such as the sides and ends
E
AE dA
£
E
S
E
S
E
S
of a cylinder, the integral 
over the entire closed sur-
face is the sum of the integrals 
over the separate sur-
faces. Consider points 3-6 as you work.
3. If 
is perpendicular (normal) at every point to a surface with
area 
if it points outward from the interior of the surface, and
if it has the same magnitude at every point on the surface, then
and 
over that surface is equal to
(If 
is inward, then 
and 
) This
should be the case for part or all of your Gaussian surface. If 
is tangent to a surface at every point, then 
and the inte-
gral over that surface is zero. This may be the case for parts of a
cylindrical Gaussian surface. If 
at every point on a sur-
face, the integral is zero.
4. Even when there is no charge within a Gaussian surface, the
field at any given point on the surface is not necessarily zero. In
that case, however, the total electric flux through the surface is
always zero.
5. The flux integral 
can be approximated as the differ-
ence between the numbers of electric lines of force leaving and
entering the Gaussian surface. In this sense the flux gives the
sign of the enclosed charge, but is only proportional to it; zero
flux corresponds to zero enclosed charge.
6. Once you have evaluated 
use Eq. (22.9) to solve for
your target variable.
EVALUATE your answer: If your result is a function that describes
how the magnitude of the electric field varies with position, ensure
that it makes sense.
AE dA,
AE dA
E
S  0
E = 0
E
S
1E dA = -EA.
E = -E
E
S
EA.
1E dA
E = E = constant,
A,
E
S
1E dA
AE dA
