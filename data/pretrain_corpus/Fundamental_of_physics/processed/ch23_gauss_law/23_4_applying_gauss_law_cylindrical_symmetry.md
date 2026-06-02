23-4 APPLYI NG  GAUSS’  L AW:  CYLI N DR ICAL  SYM M ETRY

671

23-4 APPLYING GAUSS’ LAW: CYLINDRICAL SYMMETRY

Learning Objectives
After reading this module, you should be able to . . .

23.20 Explain how Gauss’ law is used to derive the electric
field magnitude outside a line of charge or a cylindrical
surface (such as a plastic rod) with a uniform linear
charge density l.

23.21 Apply the relationship between linear charge density l

on a cylindrical surface and the electric field magnitude E
at radial distance r from the central axis.

23.22 Explain how Gauss’ law can be used to find the electric
field magnitude inside a cylindrical nonconducting surface
(such as a plastic rod) with a uniform volume charge density r.

Key Idea
● The electric field at a point near an infinite line of charge (or charged rod) with uniform linear charge density l is perpendicular
to the line and has magnitude

E $

l
2p´0r

(line of charge),

h

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

λ

r

2 rπ

Gaussian
surface

E

There is flux only
through the
curved surface.

Figure 23-14 A Gaussian surface in the form
of a closed cylinder surrounds a section
of a very long, uniformly charged, cylindri-
cal plastic rod.

where r is the perpendicular distance from the line to the point.

Applying Gauss’ Law: Cylindrical Symmetry
Figure 23-14 shows a section of an infinitely long cylindrical plastic rod with a uni-
form charge density l. We want to find an expression for the electric field magni-
tude E at radius r from the central axis of the rod, outside the rod. We could do
:
dE
that using the approach of Chapter 22 (charge element dq, field vector
, etc.).
However, Gauss’ law gives a much faster and easier (and prettier) approach.

The charge distribution and the field have cylindrical symmetry. To find the
field  at  radius  r, we  enclose  a  section  of  the  rod  with  a  concentric  Gaussian
cylinder of radius r and height h. (If you want the field at a certain point, put a
Gaussian surface through that point.) We can now apply Gauss’ law to relate the
charge enclosed by the cylinder and the net flux through the cylinder’s surface.

First note that because of the symmetry, the electric field at any point must
be radially outward (the charge is positive). That means that at any point on the
end  caps, the  field  only  skims  the  surface  and  does  not  pierce  it. So, the  flux
through each end cap is zero.

To find the flux through the cylinder’s curved surface, first note that for any
patch element on the surface, the area vector
is radially outward (away from
the  interior  of  the  Gaussian  surface)  and  thus  in  the  same  direction  as  the  field
piercing the patch.The dot product in Gauss’ law is then simply E dA cos 0 $ E dA,
and we can pull E out of the integral. The remaining integral is just the instruction
to sum the areas of all patch elements on the cylinder’s curved surface, but we al-
ready know that the total area is the product of the cylinder’s height h and cir-
cumference 2pr. The net flux through the cylinder is then

:
dA

& $ EA cos u $ E(2prh)cos 0 $ E(2prh).

On  the  other  side  of  Gauss’s  law  we  have  the  charge  qenc enclosed  by  the
cylinder. Because the linear charge density (charge per unit length, remember) is
uniform, the enclosed charge is lh. Thus, Gauss’ law,

reduces to

yielding

´0& $ qenc,
´0E(2prh) $ lh,

E $

l
2p´0r

(line of charge).

(23-12)

This is the electric field due to an infinitely long, straight line of charge, at a point
that  is  a  radial  distance  r from  the  line. The  direction  of
is  radially  outward

:
E

672

CHAPTE R  23 GAUSS’  L AW

from the line of charge if the charge is positive, and radially inward if it is nega-
tive. Equation 23-12 also approximates the field of a finite line of charge at points
that are not too near the ends (compared with the distance from the line).

If the rod has a uniform volume charge density r, we could use a similar pro-
cedure to find the electric field magnitude inside the rod. We would just shrink
the Gaussian cylinder shown in Fig. 23-14 until it is inside the rod. The charge qenc
enclosed by the cylinder would then be proportional to the volume of the rod en-
closed by the cylinder because the charge density is uniform.

Sample Problem 23.06 Gauss’ law and an upward streamer in a lightning storm

Upward streamer in a lightning
storm. The  woman  in  Fig. 23-
15 was standing on a lookout
platform  high  in  the  Sequoia
National  Park  when  a  large
storm cloud moved overhead.
Some  of  the  conduction  elec-
trons in her body were driven
into the ground by the cloud’s
negatively charged  base  (Fig.
23-16a), leaving  her  positively
charged. You  can  tell  she  was
highly  charged  because  her
hair  strands  repelled  one  an-
other and extended away from
her  along  the  electric  field
lines  produced  by  the  charge
on her.

Courtesy NOAA

Figure 23-15 This woman has
become positively charged by
an overhead storm cloud.

Lightning  did  not  strike
the  woman, but  she  was  in
extreme  danger  because  that
electric field was on the verge of causing electrical break-
down  in  the  surrounding  air. Such  a  breakdown  would
have  occurred  along  a  path  extending  away  from  her  in
what is called an upward streamer. An upward streamer is
dangerous  because  the  resulting  ionization  of  molecules
in  the  air  suddenly  frees  a  tremendous  number  of  elec-
trons from those molecules. Had the woman in Fig. 23-15
developed  an  upward  streamer, the  free  electrons  in  the
air would have moved to neutralize her (Fig. 23-16b), pro-
ducing  a  large, perhaps  fatal, charge  flow  through  her
body. That charge flow is dangerous because it could have
interfered  with  or  even  stopped  her  breathing  (which  is
obviously  necessary  for  oxygen)  and  the  steady  beat  of
her heart (which is obviously necessary for the blood flow
that carries the oxygen). The charge flow could also have
caused burns.

Let’s  model  her  body  as  a  narrow  vertical  cylinder  of
height L $ 1.8 m and radius R $ 0.10 m (Fig. 23-16c). Assume
that charge Q was uniformly distributed along the cylinder and
that electrical breakdown would have occurred if the electric

field magnitude along her body had exceeded the critical value
Ec $ 2.4 MN/C. What value of Q would have put the air along
her body on the verge of breakdown?

KEY IDEA

Because R * L, we can approximate the charge distribution
as a long line of charge. Further, because we assume that the
charge  is  uniformly  distributed  along  this  line, we  can
approximate  the  magnitude  of  the  electric  field  along  the
side of her body with Eq. 23-12 (E $ l/2p´0r).

Calculations: Substituting  the  critical  value  Ec for E, the
cylinder radius R for radial distance r, and the ratio Q/L for
linear charge density l, we have

Ec $

Q/L
2p´0R

,

Q $ 2p´0RLEc

.

or

Substituting given data then gives us

Q $ (2p)(8.85 ( 10 ’12 C 2 / N#m2)(0.10 m)

( (1.8 m)(2.4 ( 10 6 N/C)

$ 2.402 ( 10 ’5 C % 24 mC.

(Answer)

e

R

+Q

Upward
streamer

L

e

e

(a)

(b)

(c)

Figure 23-16 (a) Some of the conduction electrons in the woman’s
body are driven into the ground, leaving her positively charged. (b)
An upward streamer develops if the air undergoes electrical break-
down, which provides a path for electrons freed from molecules in
the air to move to the woman. (c) A cylinder represents the woman.

Additional examples, video, and practice available at WileyPLUS
