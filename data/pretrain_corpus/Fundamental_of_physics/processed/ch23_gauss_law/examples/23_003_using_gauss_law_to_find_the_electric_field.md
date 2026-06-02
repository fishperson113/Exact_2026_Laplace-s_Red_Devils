Sample Problem 23.03
Using Gauss’ law to find the electric field
Figure 23-10a shows, in cross section, a plastic, spherical shell
with uniform charge Q $ '16e and radius R $ 10 cm.A parti-
cle with charge q $ "5e is at the center.What is the electric field
(magnitude and direction) at (a) point P1 at radial distance r1 $
6.00 cm and (b) point P2 at radial distance r2 $ 12.0 cm?
KEY IDEAS
(1) Because the situation in Fig.23-10a has spherical symmetry,
we can apply Gauss’ law (Eq.23-7) to find the electric field at a
point if we use a Gaussian surface in the form of a sphere con-
centric with the particle and shell. (2) To find the electric field
at a point, we put that point on a Gaussian surface (so that the
we want is the 
in the dot product inside the integral in
Gauss’ law).(3) Gauss’ law relates the net electric flux through
a closed surface to the net enclosed charge. Any external
charge is not included.
E
:
E
:
Gauss’ Law and Coulomb’s Law
One of the situations in which we can apply Gauss’ law is in finding the electric
field of a charged particle. That field has spherical symmetry (the field depends
on the distance r from the particle but not the direction). So, to make use of that
symmetry, we enclose the particle in a Gaussian sphere that is centered on the
particle, as shown in Fig. 23-9 for a particle with positive charge q. Then the elec-
tric field has the same magnitude E at any point on the sphere (all points are at
the same distance r).That feature will simplify the integration.
The drill here is the same as previously. Pick a patch element on the surface and
draw its area vector 
perpendicular to the patch and directed outward. From the
symmetry of the situation, we know that the electric field 
at the patch is also radi-
E
:
dA
:
Figure 23-9 A spherical Gaussian surface
centered on a particle with charge q.
r
q
Gaussian
surface 
+
E
Checkpoint 3
There is a certain net flux &i through a Gaussian sphere of radius r enclosing an iso-
lated charged particle. Suppose the enclosing Gaussian surface is changed to (a) a
larger Gaussian sphere, (b) a Gaussian cube with edge length equal to r, and (c) a
Gaussian cube with edge length equal to 2r. In each case, is the net flux through the
new Gaussian surface greater than, less than, or equal to &i?
ally outward and thus at angle u $ 0 with 
.So,we rewrite Gauss’ law as
(23-8)
Here qenc $ q. Because the field magnitude E is the same at every patch element, E
can be pulled outside the integral:
(23-9)
The remaining integral is just an instruction to sum all the areas of the patch elements
on the sphere,but we already know that the total area is 4pr2.Substituting this,we have
´0E(4pr 2) $ q
or
(23-10)
This is exactly Eq. 22-3, which we found using Coulomb’s law.
E $
1
4p´0
q
r2 .
´0E, dA $ q.
´0, E
: " dA
: $ ´0, E dA $ qenc.
dA
:

667
23-2 GAUSS’ LAW
Figure 23-10 (a) A charged plastic spherical shell encloses a 
charged particle. (b) To find the electric field at P1, arrange for
the point to be on a Gaussian sphere. The electric field pierces
outward. The area vector for the patch element is outward. (c) P2
is on a Gaussian sphere,
is inward, and 
is still outward.
dA
:
E
:
The only charge enclosed by the Gaussian surface through P1
is that of the particle. Solving for E and substituting qenc $ 5e
and r $ r1 $ 6.00 ( 10'2 m, we find that the magnitude of the
electric field at P1 is
$ 2.00 ( 10'6N/C.
(Answer)
To find the electric field at P2, we follow the same pro-
cedure by constructing a Gaussian sphere with P2 on its sur-
face.This time,however,the net charge enclosed by the sphere
is qenc $ q " Q $ 5e " ('16e) $ '11e. Because the net
charge is negative, the electric field vectors on the sphere’s
surface pierce inward (Fig. 23-10c), the angle u between
and 
is 180%, and the dot product is E (cos 180%) dA $
dA
:
E
:
$
5(1.60 ( 10'19 C)
4p(8.85 ( 10'12 C2/N#m2)(0.0600 m)2
E $
qenc
4p´0r2
where in the last step we pull the field magnitude E out of
the integral because it is the same at all points on the
Gaussian sphere and thus is a constant. The remaining inte-
gral is simply an instruction for us to sum the areas of all the
patch elements on the sphere, but we already know that the
surface area of a sphere is 4pr2. Substituting these results,
Eq. 23-7 for Gauss’ law gives us
´0E4pr2 $ qenc.
and we find
&b $ '16 N?m2/C.
For the front face we have 
, and for the back face,
.When we take the dot product of the given elec-
tric field 
with either of these expressions for
, we get 0 and thus there is no flux through those faces. We
can now find the total flux through the six sides of the cube:
Enclosed charge: Next, we use Gauss’ law to find the
charge qenc enclosed by the cube:
(Answer)
Thus, the cube encloses a net positive charge.
$ 2.1 ( 10'10 C.
qenc $ )0& $ (8.85 ( 10'12 C2/N#m2)(24 N#m2/C)
$ 24 N#m2/C.
& $ (36 ' 12 " 16 ' 16 " 0 " 0) N#m2/C
dA
:
E
: $ 3.0xiˆ " 4.0 jˆ
dA
: $ 'dAkˆ
dA
: $ dAkˆ
dA
: $ 'dAjˆ ,
