C H A

P

T

E

R

2

3

Gauss’ Law

23-1 ELECTRIC FLUX

Learning Objectives
After reading this module, you should be able to . . .

23.01 Identify that Gauss’ law relates the electric field at points
on a closed surface (real or imaginary, said to be a Gaussian
surface) to the net charge enclosed by that surface.

23.02 Identify that the amount of electric field piercing a sur-
face (not skimming along the surface) is the electric flux )
through the surface.

23.03 Identify that an area vector for a flat surface is a vector
that is perpendicular to the surface and that has a magni-
tude equal to the area of the surface.

23.04 Identify that any surface can be divided into area ele-
ments (patch elements) that are each small enough and
flat enough for an area vector
to be assigned to it, with
the vector perpendicular to the element and having a mag-
nitude equal to the area of the element.

:
dA

Key Ideas
● The electric flux ) through a surface is the amount of electric
field that pierces the surface.

:
dA

● The area vector
for an area element (patch element) on
a surface is a vector that is perpendicular to the element and
has a magnitude equal to the area dA of the element.
● The electric flux d) through a patch element with area
vector

:
dA

is given by a dot product:
:
" dA
.

:
d) " E

23.05 Calculate the flux ) through a surface by integrating the
dot product of the electric field vector  and the area vec-
tor
(for patch elements) over the surface, in magnitude-
angle notation and unit-vector notation.

:
dA

:
E

23.06 For a closed surface, explain the algebraic signs associ-

ated with inward flux and outward flux.

23.07 Calculate the net flux ) through a closed surface, alge-
braic sign included, by integrating the dot product of the
:
E
electric field vector  and the area vector
ments) over the full surface.

(for patch ele-

:
dA

23.08 Determine whether a closed surface can be broken
up into parts (such as the sides of a cube) to simplify
the integration that yields the net flux through the
surface.

) " "E

:

:
" dA

(total flux),

where the integration is carried out over the surface.

● The net flux through a closed surface (which is used in
Gauss’ law) is given by

) " ,E

:

:
" dA

(net flux),

● The total flux through a surface is given by

where the integration is carried out over the entire surface.

What Is Physics?
In  the  preceding  chapter  we  found  the  electric  field  at  points  near  extended
charged  objects, such  as  rods. Our  technique  was  labor-intensive: We  split  the
charge distribution up into charge elements dq, found the field
due to an ele-
ment, and resolved the vector into components. Then we determined whether the
components from all the elements would end up canceling or adding. Finally we
summed the adding components by integrating over all the elements, with several
changes in notation along the way.

:
dE

One  of  the  primary  goals  of  physics  is  to  find  simple  ways  of  solving  such
labor-intensive problems. One of the main tools in reaching this goal is the use of
symmetry. In this chapter we discuss a beautiful relationship between charge and

659

660

CHAPTE R  23 GAUSS’  L AW

Gaussian
surface

E

Field line

Figure 23-1 Electric field vectors and field
lines pierce an imaginary, spherical
Gaussian surface that encloses a particle
with charge &Q.

Figure 23-2 Now the enclosed particle has
charge &2Q.

Figure 23-3 Can you tell what the enclosed
charge is now?

Figure 23-4 (a) An electric field vector pierces
a small square patch on a flat surface. (b)
Only the x component actually pierces the
patch; the y component skims across it. (c)
The area vector of the patch is perpendicu-
lar to the patch, with a magnitude equal to
the patch’s area.

electric  field  that  allows  us, in  certain  symmetric  situations, to  find  the  electric
field of an extended charged object with a few lines of algebra. The relationship is
called Gauss’ law, which was developed by German mathematician and physicist
Carl Friedrich Gauss (1777–1855).

Let’s  first  take  a  quick  look  at  some  simple  examples  that  give  the  spirit  of
Gauss’ law. Figure 23-1 shows a particle with charge &Q that is surrounded by an
imaginary concentric sphere.At points on the sphere (said to be a Gaussian surface),
the electric field vectors have a moderate magnitude (given by E " kQ/r2) and point
radially away from the particle (because it is positively charged). The electric field
lines are also outward and have a moderate density (which, recall, is related to the
field magnitude).We say that the field vectors and the field lines pierce the surface.

Figure  23-2  is  similar  except  that  the  enclosed  particle  has  charge  &2Q.
Because  the  enclosed  charge  is  now  twice  as  much, the  magnitude  of  the  field
vectors piercing outward through the (same) Gaussian surface is twice as much
as in Fig. 23-1, and the density of the field lines is also twice as much. That sen-
tence, in a nutshell, is Gauss’ law.

Guass’ law relates the electric field at points on a (closed) Gaussian surface to the
net charge enclosed by that surface.

Let’s check this with a third example with a particle that is also enclosed by the
same spherical Gaussian surface (a Gaussian sphere, if you like, or even the catchy
G-sphere)  as  shown  in  Fig. 23-3. What  is  the  amount  and  sign  of  the  enclosed
charge? Well, from the inward piercing we see immediately that the charge must be
negative. From the fact that the density of field lines is half that of Fig. 23-1, we also
see that the charge must be 0.5Q. (Using Gauss’ law is like being able to tell what is
inside a gift box by looking at the wrapping paper on the box.)

The  problems  in  this  chapter  are  of  two  types. Sometimes  we  know  the
charge and we use Gauss’ law to find the field at some point. Sometimes we know
the field on a Gaussian surface and we use Gauss’ law to find the charge enclosed
by the surface. However, we cannot do all this by simply comparing the density of
field lines in a drawing as we just did. We need a quantitative way of determining
how much electric field pierces a surface. That measure is called the electric flux.

:
E

Electric Flux
Flat Surface, Uniform Field. We begin with a flat surface with area A in a uni-
. Figure 23-4a shows one of the electric field vectors  pierc-
form electric field
ing a small square patch with area *A (where * indicates “small”). Actually, only
the x component (with magnitude Ex " E cos u in Fig. 23-4b) pierces the patch.
The y component merely skims along the surface (no piercing in that) and does
not come into play in Gauss’ law. The amount of electric field piercing the patch is
defined to be the electric flux %& through it:

:
E

*) " (E cos u) *A.

y

E y

y

x

E x

x

!A

!A

y

u

A

!A

E

x

(a )

(b )

(c )

23-1 E LECTR IC  FLUX

661

There is another way to write the right side of this statement so that we have only
that is perpendicular to
.We define an area vector
the piercing component of
the patch and that has a magnitude equal to the area *A of the patch (Fig. 23-4c).
Then we can write

:
*A

:
E

:
*) " E

:
" *A
,

and the dot product automatically gives us the component of
:
*A

and thus piercing the patch.
To  find  the  total  flux  ) through  the  surface  in  Fig. 23-4, we  sum  the  flux

:
E

that is parallel to

through every patch on the surface:

:

) " ’ E

:
" *A
.

(23-1)

However, because we do not want to sum hundreds (or more) flux values, we trans-
form the summation into an integral by shrinking the patches from small squares
with area *A to patch elements (or area elements) with area dA.The total flux is then

) " "E

:

:
" dA

(total flux).

(23-2)

iˆ

Now we can find the total flux by integrating the dot product over the full surface.
Dot Product. We can evaluate the dot product inside the integral by writing the
" dA and  might
two vectors in unit-vector notation. For example, in Fig. 23-4,
be, say, (4 " 4 ) N/C. Instead, we can evaluate the dot product in magnitude-angle
notation: E cos u dA. When the electric field is uniform and the surface is flat, the
product E cos u is a constant and comes outside the integral. The remaining
is
just an instruction to sum the areas of all the patch elements to get the total area, but
we already know that the total area is A. So the total flux in this simple situation is

"dA

:
dA

:
E

jˆ

iˆ

) " (E cos u)A (uniform field, flat surface).

(23-3)

Closed Surface. To use Gauss’ law to relate flux and charge, we need a closed
surface. Let’s use the closed surface in Fig. 23-5 that sits in a nonuniform electric
field. (Don’t worry.The homework problems involve less complex surfaces.) As be-
fore, we first consider the flux through small square patches. However, now we are
interested in not only the piercing components of the field but also on whether the
piercing is inward or outward (just as we did with Figs. 23-1 through 23-3).

Gaussian
surface

1

Directions. To keep track of the piercing direction, we again use an area vec-
:
*A
tor
that is perpendicular to a patch, but now we always draw it pointing outward
from the surface (away from the interior). Then if a field vector pierces outward, it
and the area vector are in the same direction, the angle is u " 0, and cos u " 1.
Thus, the dot product
is positive and so is the flux. Conversely, if a field vec-
tor pierces inward, the angle is u " 180$ and cos u " %1. Thus, the dot product is
negative and so is the flux. If a field vector skims the surface (no piercing), the dot
product is zero (because cos 90$ " 0) and so is the flux. Figure 23-5 gives some
general examples and here is a summary:

:
*A

:
E

’

An inward piercing field is negative flux. An outward piercing field is positive
flux. A skimming field is zero flux.

Net Flux. In principle, to find the net flux through the surface in Fig. 23-5, we
find the flux at every patch and then sum the results (with the algebraic signs in-
cluded). However, we are not about to do that much work. Instead, we shrink the
squares to patch elements with area vectors

and then integrate:

:
dA

) " , E

:

:
" dA

(net flux).

(23-4)

3

2

E

∆ A

E

θ

3
Φ > 0

Pierce
outward:
positive
flux

A
∆

θ

E

1
Φ < 0

Pierce
inward:
negative
flux

2

∆ A
Φ = 0

Skim: zero flux

Figure 23-5 A Gaussian surface of arbitrary
shape immersed in an electric field. The
surface is divided into small squares of area
!A. The electric field vectors  and the
area vectors
for three representative
squares, marked 1, 2, and 3, are shown.

:
!A

:
E

662

CHAPTE R  23 GAUSS’  L AW

The loop on the integral sign indicates that we must integrate over the entire closed
surface, to get the net flux through the surface (as in Fig. 23-5, flux might enter on
one side and leave on another side). Keep in mind that we want to determine the
net flux through a surface because that is what Gauss’ law relates to the charge en-
closed by the surface. (The law is coming up next.) Note that flux is a scalar (yes, we
talk about field vectors but flux is the amount of piercing field, not a vector itself).
The SI unit of flux is the newton–square-meter per coulomb

(N#m2/C)

.

Checkpoint 1

The figure here shows a Gaussian cube of face area A
immersed in a uniform electric field
that has the positive
direction of the z axis. In terms of E and A, what is the flux
through (a) the front face (which is in the xy plane), (b) the
rear face, (c) the top face, and (d) the whole cube?

:
E

y

A

x

E

z

Sample Problem 23.01 Flux through a closed cylinder, uniform field

Figure  23-6  shows  a  Gaussian  surface  in  the  form  of  a
closed  cylinder  (a  Gaussian  cylinder  or  G-cylinder)  of
radius R. It  lies  in  a  uniform  electric  field
with  the
cylinder’s  central  axis  (along  the  length  of  the  cylinder)
parallel to the field. What is the net flux & of the electric
field through the cylinder?

:
E

KEY IDEAS

:
E

:
" dA

We can find the net flux & with Eq. 23-4 by integrating the
dot  product
over  the  cylinder’s  surface. However,
we  cannot  write  out  functions  so  that  we  can  do  that  with
one integral. Instead, we need to be a bit clever: We break
up the surface into sections with which we can actually eval-
uate an integral.

Calculations: We  break  the  integral  of  Eq. 23-4  into  three
terms: integrals over the left cylinder cap a, the curved cylin-
drical surface b, and the right cap c:

:
" dA

:

& $ , E
$ "

:
E

a

:
" dA

" "

b

:
E

:
" dA

" "

c

:
E

:
" dA
.

(23-5)

:
dA
Pick a patch element on the left cap. Its area vector
must be perpendicular to the patch and pointing away from
the interior of the cylinder. In Fig. 23-6, that means the angle
between it and the field piercing the patch is 180%. Also, note
that  the  electric  field  through  the  end  cap  is  uniform  and
thus E can be pulled out of the integration. So, we can write the
flux through the left cap as

:
E

:
" dA

$ " E(cos 180%) dA $ ’E" dA $ ’EA,

"

a

" dA
where
right cap, where

u $

0 for all points,

gives the cap’s area A ($ pR2). Similarly, for the

:
E

:
" dA

$ " E(cos 0) dA $ EA.

"

c

Finally, for the cylindrical surface, where the angle u is 90% at
all points,

:
E

:
" dA

$ " E(cos 90%) dA $ 0.

"

b

Substituting these results into Eq. 23-5 leads us to

& $ ’EA " 0 " EA $ 0.

(Answer)

The net flux is zero because the field lines that represent the
electric field all pass entirely through the Gaussian surface,
from the left to the right.

dA

θ

a

E

dA

θ

E

b

Gaussian
surface

E

dA

c

Figure 23-6 A cylindrical Gaussian surface, closed by end caps, is
immersed in a uniform electric field. The cylinder axis is parallel to
the field direction.

Additional examples, video, and practice available at WileyPLUS

Sample Problem 23.02 Flux through a closed cube, nonuniform field

23-1 E LECTR IC  FLUX

663

$ 3.0xiˆ " 4.0jˆ
A nonuniform electric  field  given  by
pierces  the  Gaussian  cube  shown  in  Fig. 23-7a. (E is  in
newtons  per  coulomb  and  x is  in  meters.)  What  is  the
electric flux through the right face, the left face, and the top
face?  (We  consider  the  other  faces  in  another  sample
problem.)

:
E

KEY IDEA

We  can  find  the  flux  & through  the  surface  by  integrating
the scalar product

over each face.

:
" dA

:
E

:
A
Right face: An area vector
is always perpendicular to its
surface  and  always  points  away  from  the  interior  of  a
Gaussian surface. Thus, the vector
for any patch element
(small section) on the right face of the cube must point in
the positive direction of the x axis. An example of such an
element is shown in Figs. 23-7b and c, but we would have an
identical  vector  for  any  other  choice  of  a  patch  element
on that face. The most convenient way to express the vector
is in unit-vector notation,

:
dA

:
dA

$ dAiˆ.

:

:
" dA

$ " (3.0xiˆ " 4.0jˆ) " (dAiˆ)
&r $ " E
$ " [(3.0x)(dA)iˆ " iˆ " (4.0)(dA)jˆ " iˆ]
$ " (3.0x dA " 0) $ 3.0" x dA.

We are about to integrate over the right face, but we note
that x has the same value everywhere on that face — namely,
x $ 3.0 m. This means we can substitute that constant value
for x. This can be a confusing argument. Although x is cer-
tainly a variable as we move left to right across the figure,
because the right face is perpendicular to the x axis, every
point on the face has the same x coordinate. (The y and z co-
ordinates do not matter in our integral.) Thus, we have

&r $  3.0 " (3.0) dA $ 9.0" dA.

The integral
right face, so

" dA

merely gives us the area A 4.0 m2 of the

$

&r $ (9.0 N/C)(4.0 m2) $ 36 N #m2/C.

(Answer)

From Eq. 23-4, the flux &r through the right face is then

Left face: We repeat this procedure for the left face. However,

y

Gaussian
surface

The y component
is a constant.
E y

E

x

E x

y

dA

dA

The element area vector
(for a patch element) is
perpendicular to the surface
and outward.

dA

dA

x

A

dA

(b )

y

x = 1.0 m x = 3.0 m

z

(a )

The x component
depends on the
value of x.

z

Figure 23-7 (a) A Gaussian cube with one edge on the x
axis lies within a nonuniform electric field that de-
pends on the value of x. (b) Each patch element has an
outward vector that is perpendicular to the area. (c)
Right face: the x component of the field pierces the
area and produces positive (outward) flux. The y com-
ponent does not pierce the area and thus does not
produce any flux. (Figure continues on following page)
z

The y component of the
field skims the surface
and gives no flux. The
dot product is just zero.

E y

E x

dA

x

The x component of the
field pierces the surface
and gives outward flux.
The dot product is positive.

(c )
