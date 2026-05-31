Sample Problem 23.05
Spherical metal shell, electric field and enclosed charge
Figure 23-13a shows a cross section of a spherical metal shell
of inner radius R. A particle with a charge of '5.0 mC is lo-
cated at a distance R/2 from the center of the shell. If the shell
is electrically neutral, what are the (induced) charges on its in-
ner and outer surfaces? Are those charges uniformly distrib-
uted? What is the field pattern inside and outside the shell?
KEY IDEAS
Figure 23-13b shows a cross section of a spherical Gaussian
surface within the metal, just outside the inner wall of the
shell. The electric field must be zero inside the metal (and
thus on the Gaussian surface inside the metal). This means
that the electric flux through the Gaussian surface must also
be zero. Gauss’ law then tells us that the net charge enclosed
by the Gaussian surface must be zero.
Reasoning: With a particle of charge '5.0 mC within the
shell, a charge of "5.0 mC must lie on the inner wall of
the shell in order that the net enclosed charge be zero. If the
particle were centered, this positive charge would be uni-
formly distributed along the inner wall. However, since the
particle is off-center, the distribution of positive charge is
skewed, as suggested by Fig. 23-13b, because the positive
charge tends to collect on the section of the inner wall near-
est the (negative) particle.
Because the shell is electrically neutral, its inner wall
can have a charge of "5.0 mC only if electrons, with a total
charge of '5.0 mC, leave the inner wall and move to the
outer wall. There they spread out uniformly, as is also sug-
gested by Fig. 23-13b. This distribution of negative charge is
Figure 23-13 (a) A negatively charged particle is located within a
spherical metal shell that is electrically neutral. (b) As a result,
positive charge is nonuniformly distributed on the inner wall of
the shell, and an equal amount of negative charge is uniformly 
distributed on the outer wall.
R
R/2
(a)
(b)
+
+
+
+
+ +
+
+
+
+
+ +
+
+
Gaussian
surface
_
_
_
_
_
_
_
_
_
_
_
_
_
_
uniform because the shell is spherical and because the
skewed distribution of positive charge on the inner wall
cannot produce an electric field in the shell to affect the dis-
tribution of charge on the outer wall. Furthermore, these
negative charges repel one another.
The field lines inside and outside the shell are shown
approximately in Fig. 23-13b. All the field lines intersect the
shell and the particle perpendicularly. Inside the shell the pat-
tern of field lines is skewed because of the skew of the
positive charge distribution. Outside the shell the pattern is
the same as if the particle were centered and the shell were
missing. In fact, this would be true no matter where inside
the shell the particle happened to be located.
Additional examples, video, and practice available at WileyPLUS

671
23-4 APPLYING GAUSS’ LAW: CYLINDRICAL SYMMETRY
Applying Gauss’ Law: Cylindrical Symmetry
Figure 23-14 shows a section of an infinitely long cylindrical plastic rod with a uni-
form charge density l. We want to find an expression for the electric field magni-
tude E at radius r from the central axis of the rod, outside the rod. We could do
that using the approach of Chapter 22 (charge element dq, field vector 
, etc.).
However,Gauss’ law gives a much faster and easier (and prettier) approach.
The charge distribution and the field have cylindrical symmetry. To find the
field at radius r, we enclose a section of the rod with a concentric Gaussian
cylinder of radius r and height h. (If you want the field at a certain point, put a
Gaussian surface through that point.) We can now apply Gauss’ law to relate the
charge enclosed by the cylinder and the net flux through the cylinder’s surface.
First note that because of the symmetry, the electric field at any point must
be radially outward (the charge is positive). That means that at any point on the
end caps, the field only skims the surface and does not pierce it. So, the flux
through each end cap is zero.
To find the flux through the cylinder’s curved surface, first note that for any
patch element on the surface, the area vector 
is radially outward (away from
the interior of the Gaussian surface) and thus in the same direction as the field
piercing the patch.The dot product in Gauss’ law is then simply E dA cos 0 $ E dA,
and we can pull E out of the integral.The remaining integral is just the instruction
to sum the areas of all patch elements on the cylinder’s curved surface, but we al-
ready know that the total area is the product of the cylinder’s height h and cir-
cumference 2pr.The net flux through the cylinder is then
On the other side of Gauss’s law we have the charge qenc enclosed by the
cylinder. Because the linear charge density (charge per unit length, remember) is
uniform, the enclosed charge is lh.Thus, Gauss’ law,
´0& $ qenc,
reduces to
´0E(2prh) $ lh,
yielding
(line of charge).
(23-12)
This is the electric field due to an infinitely long, straight line of charge, at a point
that is a radial distance r from the line. The direction of 
is radially outward
E
:
E $
l
2p´0r
& $ EA cos u $ E(2prh)cos 0 $ E(2prh).
dA
:
dE
:
23-4 APPLYING GAUSS’ LAW: CYLINDRICAL SYMMETRY
Learning Objectives
on a cylindrical surface and the electric field magnitude E
at radial distance r from the central axis.
23.22 Explain how Gauss’ law can be used to find the electric
field magnitude inside a cylindrical nonconducting surface
(such as a plastic rod) with a uniform volume charge density r.
●The electric field at a point near an infinite line of charge (or charged rod) with uniform linear charge density l is perpendicular
to the line and has magnitude
(line of charge),
where r is the perpendicular distance from the line to the point.
E $
l
2p´0r
After reading this module, you should be able to . . . 
23.20 Explain how Gauss’ law is used to derive the electric
field magnitude outside a line of charge or a cylindrical
surface (such as a plastic rod) with a uniform linear
charge density l.
23.21 Apply the relationship between linear charge density l
Key Idea
Figure 23-14 A Gaussian surface in the form
of a closed cylinder surrounds a section
of a very long, uniformly charged, cylindri-
cal plastic rod.
r
h
λ 
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
2 r
π 
Gaussian
surface
E
There is flux only
through the
curved surface.

672
CHAPTER 23
GAUSS’ LAW
Additional examples, video, and practice available at WileyPLUS
Figure 23-16 (a) Some of the conduction electrons in the woman’s
body are driven into the ground, leaving her positively charged. (b)
An upward streamer develops if the air undergoes electrical break-
down, which provides a path for electrons freed from molecules in
the air to move to the woman. (c) A cylinder represents the woman.
+Q
R
L
e 
e 
e
Upward
streamer
(a) 
(b) 
(c)
from the line of charge if the charge is positive, and radially inward if it is nega-
tive. Equation 23-12 also approximates the field of a finite line of charge at points
that are not too near the ends (compared with the distance from the line).
If the rod has a uniform volume charge density r, we could use a similar pro-
cedure to find the electric field magnitude inside the rod. We would just shrink
the Gaussian cylinder shown in Fig. 23-14 until it is inside the rod.The charge qenc
enclosed by the cylinder would then be proportional to the volume of the rod en-
closed by the cylinder because the charge density is uniform.
