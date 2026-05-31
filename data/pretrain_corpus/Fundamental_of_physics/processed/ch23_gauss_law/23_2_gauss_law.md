664

CHAPTE R  23 GAUSS’  L AW

y

dA

The y component of the
field skims the surface
and gives no flux. The
dot product is just zero.

x

The x component of the
field pierces the surface
and gives inward flux. The
dot product is negative.

E x

E y

z

(d )

The y component of the
field pierces the surface
and gives outward flux.
The dot product is positive.

y

dA

E y

The x component of the
field skims the surface
and gives no flux. The
dot product is just zero.

E x

x

z

(e )

Figure 23-7 (Continued from previous page) (d) Left face: the x component of the
field produces negative (inward) flux. (e) Top face: the y component of the field
produces positive (outward) flux.

points in
two factors change. (1) The element area vector
$ ’dAiˆ
the  negative  direction  of  the  x axis, and  thus
(Fig. 23-7d). (2) On  the  left  face, x $ 1.0 m. With  these
&l
changes, we find that the flux

through the left face is

:
dA
:
dA

&l $ ’12 N #m2/C.

(Answer)

:
dA
Top face: Now
:
dA
axis, and thus

$ dAjˆ

points in the positive direction of the y

&t $ "(3.0xiˆ " 4.0jˆ) " (dAjˆ)
$ " [(3.0x)(dA)iˆ " jˆ " (4.0)(dA)jˆ " jˆ]
$ "  (0 " 4.0 dA) $ 4.0" dA

(Fig. 23-7e). The flux

is&t

$ 16 N # m2/C.

(Answer)

Additional examples, video, and practice available at WileyPLUS

23-2 GAUSS’ LAW

Learning Objectives

After reading this module, you should be able to . . .
23.09 Apply Gauss’ law to relate the net flux & through a

closed surface to the net enclosed charge qenc.

no contribution to the net flux through the closed surface.
23.12 Derive the expression for the magnitude of the electric

23.10 Identify how the algebraic sign of the net enclosed

field of a charged particle by using Gauss’ law.

charge corresponds to the direction (inward or outward)
of the net flux through a Gaussian surface.

23.11 Identify that charge outside a Gaussian surface makes

23.13 Identify that for a charged particle or uniformly charged
sphere, Gauss’ law is applied with a Gaussian surface that
is a concentric sphere.

Key Ideas
● Gauss’ law relates the net flux & penetrating a closed sur-
face to the net charge qenc enclosed by the surface:

´0& $ qenc

(Gauss’ law).

● Gauss’ law can also be written in terms of the electric field
piercing the enclosing Gaussian surface:

´0,E

:

:
" dA

$ qenc

(Gauss’ law).

Gauss’ Law
Gauss’  law  relates  the  net  flux  & of  an  electric  field  through  a  closed  surface
(a Gaussian surface) to the net charge qenc that is enclosed by that surface. It tells us that

´0& $ qenc

(Gauss’ law).

(23-6)

23-2 GAUSS’  L AW

665

S1

S4

S2

+

–

S3

Figure 23-8 Two charges, equal in magnitude
but opposite in sign, and the field lines that
represent their net electric field. Four
Gaussian surfaces are shown in cross sec-
tion. Surface S1 encloses the positive
charge. Surface S2 encloses the negative
charge. Surface S3 encloses no charge.
Surface S4 encloses both charges and thus
no net charge.

By substituting Eq. 23-4, the definition of flux, we can also write Gauss’ law as

´0, E

:

:
" dA

$ qenc

(Gauss’ law).

(23-7)

Equations 23-6 and 23-7 hold only when the net charge is located in a vacuum or
(what is the same for most practical purposes) in air. In Chapter 25, we modify Gauss’
law to include situations in which a material such as mica, oil, or glass is present.

In Eqs. 23-6 and 23-7, the net charge qenc is the algebraic sum of all the enclosed
positive and negative charges, and it can be positive, negative, or zero. We include
the sign, rather than just use the magnitude of the enclosed charge, because the sign
tells us something about the net flux through the Gaussian surface: If qenc is posi-
tive, the net flux is outward; if qenc is negative, the net flux is inward.

Charge outside the surface, no matter how large or how close it may be, is not in-
cluded in the term qenc in Gauss’ law. The exact form and location of the charges in-
side the Gaussian surface are also of no concern; the only things that matter on the
right  side  of  Eqs. 23-6  and  23-7  are  the  magnitude  and  sign  of  the  net  enclosed
charge.The quantity  on the left side of Eq. 23-7, however, is the electric field result-
ing from all charges, both those inside and those outside the Gaussian surface. This
statement may seem to be inconsistent, but keep this in mind: The electric field due
to a charge outside the Gaussian surface contributes zero net flux through the sur-
face, because as many field lines due to that charge enter the surface as leave it.

:
E

Let us apply these ideas to Fig. 23-8, which shows two particles, with charges
equal in magnitude but opposite in sign, and the field lines describing the electric
fields the particles set up in the surrounding space. Four Gaussian surfaces are
also shown, in cross section. Let us consider each in turn.
Surface S1. The electric field is outward for all points on this surface. Thus, the
flux  of  the  electric  field  through  this  surface  is  positive, and  so  is  the  net
charge within the surface, as Gauss’ law requires. (That is, in Eq. 23-6, if & is
positive, qenc must be also.)

Surface S2. The electric field is inward for all points on this surface. Thus, the flux
of the electric field through this surface is negative and so is the enclosed charge,
as Gauss’ law requires.

Surface S3. This  surface  encloses  no  charge, and  thus  qenc $ 0. Gauss’  law
(Eq. 23-6) requires that the net flux of the electric field through this surface
be zero. That is reasonable because all the field lines pass entirely through
the surface, entering it at the top and leaving at the bottom.

Surface S4. This surface encloses no net charge, because the enclosed positive
and negative charges have equal magnitudes. Gauss’ law requires that the net
flux  of  the  electric  field  through  this  surface  be  zero. That  is  reasonable
because there are as many field lines leaving surface S4 as entering it.

What would happen if we were to bring an enormous charge Q up close to sur-
face S4 in Fig. 23-8? The pattern of the field lines would certainly change, but the
net flux for each of the four Gaussian surfaces would not change. Thus, the value
of Q would not enter Gauss’ law in any way, because Q lies outside all four of the
Gaussian surfaces that we are considering.

Checkpoint 2

The figure shows three situations in which a Gaussian cube sits in
an electric field.The arrows and the values indicate the directions
of the field lines and the magnitudes (in N ?m2/C) of the flux
through the six sides of each cube. (The lighter arrows are for the
hidden faces.) In which situation does the cube enclose (a) a posi-
tive net charge, (b) a negative net charge, and (c) zero net charge?

5

3

7

3

6

8

2

10

3

5

2

(1)

7

4

4

(2)

6

5

7

(3)

5

666

CHAPTE R  23 GAUSS’  L AW

Gaussian
surface

r

E

+

q

Figure 23-9 A spherical Gaussian surface
centered on a particle with charge q.

Gauss’ Law and Coulomb’s Law
One of the situations in which we can apply Gauss’ law is in finding the electric
field of a charged particle. That field has spherical symmetry (the field depends
on the distance r from the particle but not the direction). So, to make use of that
symmetry, we enclose the particle in a Gaussian sphere that is centered on the
particle, as shown in Fig. 23-9 for a particle with positive charge q. Then the elec-
tric field has the same magnitude E at any point on the sphere (all points are at
the same distance r). That feature will simplify the integration.

The drill here is the same as previously. Pick a patch element on the surface and
perpendicular to the patch and directed outward. From the
at the patch is also radi-

draw its area vector
symmetry of the situation, we know that the electric field
ally outward and thus at angle u $ 0 with

:
E
. So, we rewrite Gauss’ law as

:
dA

:
dA

´0, E

:

:
" dA

$ ´0, E dA $ qenc.

(23-8)

Here qenc $ q. Because the field magnitude E is the same at every patch element, E
can be pulled outside the integral:

´0E, dA $ q.

(23-9)

The remaining integral is just an instruction to sum all the areas of the patch elements
on the sphere, but we already know that the total area is 4pr 2. Substituting this, we have

or

´0E(4pr 2) $ q

E $

1
4p´0

q
r2 .

(23-10)

This is exactly Eq. 22-3, which we found using Coulomb’s law.

Checkpoint 3

There is a certain net flux &i through a Gaussian sphere of radius r enclosing an iso-
lated charged particle. Suppose the enclosing Gaussian surface is changed to (a) a
larger Gaussian sphere, (b) a Gaussian cube with edge length equal to r, and (c) a
Gaussian cube with edge length equal to 2r. In each case, is the net flux through the
new Gaussian surface greater than, less than, or equal to &i?

Sample Problem 23.03 Using Gauss’ law to find the electric field

Figure  23-10a shows, in  cross  section, a  plastic, spherical  shell
with uniform charge Q $ ’16e and radius R $ 10 cm. A parti-
cle with charge q $ "5e is at the center.What is the electric field
(magnitude and direction) at (a) point P1 at radial distance r1 $
6.00 cm and (b) point P2 at radial distance r2 $ 12.0 cm?

KEY IDEAS

(1) Because the situation in Fig. 23-10a has spherical symmetry,
we can apply Gauss’ law (Eq. 23-7) to find the electric field at a
point if we use a Gaussian surface in the form of a sphere con-
centric with the particle and shell. (2) To find the electric field
at a point, we put that point on a Gaussian surface (so that the
:
E
in  the  dot  product  inside  the  integral  in
Gauss’ law). (3) Gauss’ law relates the net electric flux through
a  closed  surface  to  the  net  enclosed  charge. Any  external
charge is not included.

we  want  is  the

:
E

Calculations: To  find  the  field  at  point  P1, we  construct  a
Gaussian sphere with P1 on its surface and thus with a radius
of r1. Because the charge enclosed by the Gaussian sphere is
positive, the electric flux through the surface must be positive
and thus outward. So, the electric field
pierces the surface
outward and, because of the spherical symmetry, must be radi-
ally outward, as drawn in Fig. 23-10b. That figure does not in-
clude the plastic shell because the shell is not enclosed by the
Gaussian sphere.

:
E

Consider a patch element on the sphere at P1. Its area vec-
:
dA
is radially outward (it must always be outward from a
is zero.

tor
Gaussian surface). Thus the angle u between  and
We can now rewrite the left side of Eq. 23-7 (Gauss’ law) as

:
dA

:
E

´0, E

:

:
" dA

$ ´0, E cos 0 dA $ ´0, E dA $ ´0 E,dA,

Q

q

P1

P2

E

dA

r1

q

(b )

r1

r2

(a )

Q

r2

q

E

dA

(c )

Figure 23-10 (a) A charged plastic spherical shell encloses a
charged particle. (b) To find the electric field at P1, arrange for
the point to be on a Gaussian sphere. The electric field pierces
outward. The area vector for the patch element is outward. (c) P2
is on a Gaussian sphere,

is still outward.

is inward, and

:
dA

:
E

where in the last step we pull the field magnitude E out of
the  integral  because  it  is  the  same  at  all  points  on  the
Gaussian sphere and thus is a constant. The remaining inte-
gral is simply an instruction for us to sum the areas of all the
patch elements on the sphere, but we already know that the
surface  area  of  a  sphere  is  4pr2. Substituting  these  results,
Eq. 23-7 for Gauss’ law gives us

´0E4pr2 $ qenc.

23-2 GAUSS’  L AW

667

The only charge enclosed by the Gaussian surface through P1
is that of the particle. Solving for E and substituting qenc $ 5e
and r $ r1 $ 6.00 ( 10’2 m, we find that the magnitude of the
electric field at P1 is
qenc
4p´0r2

E $

$

5(1.60 ( 10’19 C)
4p(8.85 ( 10’12 C2/N#m2)(0.0600 m)2

$ 2.00 ( 10’6 N/C.

(Answer)

To find the electric field at P2, we follow the same pro-
cedure by constructing a Gaussian sphere with P2 on its sur-
face.This time, however, the net charge enclosed by the sphere
is qenc $ q " Q $ 5e " (’16e) $  ’11e. Because  the  net
charge is negative, the electric field vectors on the sphere’s
:
surface pierce inward (Fig. 23-10c), the angle u between
E
is  180%, and  the  dot  product  is E (cos  180%) dA $
and
’E dA. Now solving Gauss’ law for E and substituting r $
r2 $ 12.00 ( 10’2 m and the new qenc, we find

:
dA

E $

’qenc
4p´0r2

$

’ [’11(1.60 ( 10’19 C)]
4p(8.85 ( 10’12 C2/N#m2)(0.120 m)2

$ 1.10 ( 10’6 N/C.

(Answer)

Note how different the calculations would have been if
we had put P1 or P2 on the surface of a Gaussian cube in-
stead of mimicking the spherical symmetry with a Gaussian
sphere. Then  angle  u and  magnitude  E would  have  varied
considerably over the surface of the cube and evaluation of
the integral in Gauss’ law would have been difficult.

Sample Problem 23.04 Using Gauss’ law to find the enclosed charge

What  is  the  net  charge  enclosed  by  the  Gaussian  cube  of
Sample Problem 23.02?

KEY IDEA

The net charge enclosed by a (real or mathematical) closed
surface  is  related  to  the  total  electric  flux  through  the
surface by Gauss’ law as given by Eq. 23-6 (´0& $ qenc).

Flux: To use Eq. 23-6, we need to know the flux through all
six faces of the cube. We already know the flux through the
right  face  (&r $ 36  N #m2/C),
the  left  face  (&l $ ’12
N ?m2/C), and the top face (&t $ 16 N ?m2/C).

For the bottom face, our calculation is just like that for
the  top  face  except that  the  element  area  vector
is
now directed downward along the y axis (recall, it must be
outward from  the  Gaussian  enclosure). Thus, we  have

:
dA

:
dA

$ ’dAjˆ ,

and we find

&b $ ’16 N ?m2/C.
:
dA

$ dAkˆ

$ ’dAkˆ
:
E

, and for the back face,
. When we take the dot product of the given elec-
with either of these expressions for
, we get 0 and thus there is no flux through those faces. We

For the front face we have
:
dA
tric field
:
dA
can now find the total flux through the six sides of the cube:

$ 3.0xiˆ " 4.0 jˆ

& $ (36 ’ 12 " 16 ’ 16 " 0 " 0) N#m2/C

$ 24 N#m2/C.

Enclosed  charge: Next, we  use  Gauss’  law  to  find  the
charge qenc enclosed by the cube:

qenc $ )0& $ (8.85 ( 10’12 C2/N#m2)(24 N#m2/C)

$ 2.1 ( 10’10 C.

(Answer)

Thus, the cube encloses a net positive charge.

Additional examples, video, and practice available at WileyPLUS
