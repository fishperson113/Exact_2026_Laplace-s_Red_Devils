23-5 APPLYI NG  GAUSS’  L AW:  PL ANAR  SYM M ETRY

673

23-5 APPLYING GAUSS’ LAW: PLANAR SYMMETRY

Learning Objectives
After reading this module, you should be able to . . .

23.23 Apply Gauss’ law to derive the electric field magnitude
E near a large, flat, nonconducting surface with a uniform
surface charge density s.

23.24 For points near a large, flat nonconducting surface

with a uniform charge density s, apply the relationship be-

Key Ideas
● The electric field due to an infinite nonconducting sheet
with uniform surface charge density s is perpendicular to the
plane of the sheet and has magnitude

E $

s
2´0

(nonconducting sheet of charge).

tween the charge density and the electric field magnitude
E and also specify the direction of the field.

23.25 For points near two large, flat, parallel, conducting sur-
faces with a uniform charge density s, apply the relation-
ship between the charge density and the electric field
magnitude E and also specify the direction of the field.

● The external electric field just outside the surface of an iso-
lated charged conductor with surface charge density s is per-
pendicular to the surface and has magnitude

E $

s
´0

(external, charged conductor).

Inside the conductor, the electric field is zero.

Applying Gauss’ Law: Planar Symmetry
Nonconducting Sheet
Figure 23-17 shows a portion of a thin, infinite, nonconducting sheet with a uni-
form (positive) surface charge density s. A sheet of thin plastic wrap, uniformly
:
E
charged on one side, can serve as a simple model. Let us find the electric field
a distance r in front of the sheet.

A  useful  Gaussian  surface  is  a  closed  cylinder  with  end  caps  of  area  A,
arranged to pierce the sheet perpendicularly as shown. From symmetry, must
be perpendicular to the sheet and hence to the end caps. Furthermore, since the
is directed away from the sheet, and thus the electric field
charge is positive,
lines pierce the two Gaussian end caps in an outward direction. Because the field
lines do not pierce the curved surface, there is no flux through this portion of the
Gaussian surface. Thus

is simply E dA; then Gauss’ law,

:
" dA

:
E

:
E

:
E

becomes

´0, E

:

:
" dA

$ qenc,

´0(EA " EA) $ sA,

where sA is the charge enclosed by the Gaussian surface. This gives

E $

s
2´0

(sheet of charge).

(23-13)

Since we are considering an infinite sheet with uniform charge density, this result
holds for any point at a finite distance from the sheet. Equation 23-13 agrees with
Eq. 22-27, which we found by integration of electric field components.

Figure 23-17 (a) Perspective view
and (b) side view of a portion of a
very large, thin plastic sheet, uni-
formly charged on one side to sur-
face charge density s. A closed
cylindrical Gaussian surface passes
through the sheet and is perpendi-
cular to it.

(a)

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
A

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

r
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

E

+
+

+
+
+
+
+

σ

Gaussian
surface

E

There is flux only
through the
two end faces.

A

E

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
(b)

A

E

674

CHAPTE R  23 GAUSS’  L AW

σ 1

E

––

––

––

––

–

–

(b)

E = 0

σ 1

E

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

(a)

E = 0

σ 1

E

σ 1

E

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

–
–
–
–
–
–
–
–
–
–

  σ2 1

E

(c)

Figure 23-18 (a) A thin, very large conduct-
ing plate with excess positive charge.
(b) An identical plate with excess negative
charge. (c) The two plates arranged so
they are parallel and close.

Two Conducting Plates
Figure 23-18a shows a cross section of a thin, infinite conducting plate with excess
positive charge. From Module 23-3 we know that this excess charge lies on the
surface  of  the  plate. Since  the  plate  is  thin  and  very  large, we  can  assume  that
essentially all the excess charge is on the two large faces of the plate.

If there is no external electric field to force the positive charge into some par-
ticular  distribution, it  will  spread  out  on  the  two  faces  with  a  uniform  surface
charge  density  of  magnitude  s1. From  Eq. 23-11  we  know  that  just  outside  the
plate  this  charge  sets  up  an  electric  field  of  magnitude  E $ s1/´0. Because  the
excess charge is positive, the field is directed away from the plate.

Figure  23-18b shows  an  identical  plate  with  excess  negative  charge  having
the same magnitude of surface charge density s1. The only difference is that now
the electric field is directed toward the plate.

Suppose we arrange for the plates of Figs. 23-18a and b to be close to each
other and parallel (Fig. 23-18c). Since the plates are conductors, when we bring
them  into  this  arrangement, the  excess  charge  on  one  plate  attracts  the  excess
charge on the other plate, and all the excess charge moves onto the inner faces of
the plates as in Fig. 23-18c. With twice as much charge now on each inner face, the
new surface charge density (call it s) on each inner face is twice s1. Thus, the elec-
tric field at any point between the plates has the magnitude

2s1
´0
This field is directed away from the positively charged plate and toward the nega-
tively charged plate. Since no excess charge is left on the outer faces, the electric
field to the left and right of the plates is zero.

(23-14)

s
´0

E $

$

.

Because the charges moved when we brought the plates close to each other,
the  charge  distribution  of  the  two-plate  system  is  not  merely  the  sum  of  the
charge distributions of the individual plates.

One reason why we discuss seemingly unrealistic situations, such as the field set
up by an infinite sheet of charge, is that analyses for “infinite” situations yield good
approximations to many real-world problems. Thus, Eq. 23-13 holds well for a finite
nonconducting sheet as long as we are dealing with points close to the sheet and not
too near its edges. Equation 23-14 holds well for a pair of finite conducting plates as
long as we consider points that are not too close to their edges. The trouble with the
edges is that near an edge we can no longer use planar symmetry to find expressions
for the fields. In fact, the field lines there are curved (said to be an edge effect or fring-
ing), and the fields can be very difficult to express algebraically.

Sample Problem 23.07 Electric field near two parallel nonconducting sheets with charge

Figure  23-19a shows  portions  of  two  large, parallel, non-
conducting sheets, each with a fixed uniform charge on one
side. The  magnitudes  of  the  surface  charge  densities  are
s(") $ 6.8 mC/m2 for the positively charged sheet and s(’) $
4.3 mC/m2 for the negatively charged sheet.

Find  the  electric  field

:
E
(b) between the sheets, and (c) to the right of the sheets.

(a)  to  the  left  of  the  sheets,

KEY IDEA

With the charges fixed in place (they are on nonconductors),
we can find the electric field of the sheets in Fig. 23-19a by
(1) finding the field of each sheet as if that sheet were isolated
and (2) algebraically adding the fields of the isolated sheets

+
+σ (+)
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

(a)

σ (–)

–
–
–
–
–
–
–
–
–
–

Figure 23-19 (a) Two large, paral-
lel sheets, uniformly charged on
one side. (b) The individual
electric fields resulting from the
two charged sheets. (c) The net
field due to both charged
sheets, found by superposition.

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

E(+)

L

E(–)

EL

(b)

(c)

E(+)

B

E(–)

EB

E(+)

R

E(–)

ER

–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
