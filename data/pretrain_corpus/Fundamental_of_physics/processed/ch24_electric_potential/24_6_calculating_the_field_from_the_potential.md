24-6 CALCULATING THE FIELD FROM THE POTENTIAL

24-6 CALCU L ATI NG  TH E  FI E LD  FROM  TH E  POTE NTIAL

701

Learning Objectives
After reading this module, you should be able to . . .

24.23 Given an electric potential as a function of position
along an axis, find the electric field along that axis.
24.24 Given a graph of electric potential versus position

along an axis, determine the electric field along the axis.
24.25 For a uniform electric field, relate the field magnitude E

Key Ideas
● The component of
which the potential changes with distance in that direction:

in any direction is the negative of the rate at

:
E

Es $ ’

3V
3s
:
● The x, y, and z components of  may be found from
E
;    Ey $ ’

;    Ez $ ’

Ex $ ’

.

3V
3x

3V
3y

3V
3z

and the separation  x and potential difference  V
between adjacent equipotential lines.

!

!

24.26 Relate the direction of the electric field and

the directions in which the potential decreases and
increases.

When

:
E

is uniform, all this reduces to

E $ ’

!V
!s

,

where s is perpendicular to the equipotential surfaces.
● The electric field is zero parallel to an equipotential
surface.

.

Calculating the Field from the Potential
In  Module  24-2, you  saw  how  to  find  the  potential  at  a  point  f if  you  know
the electric field along a path from a reference point to point f. In this module,
we propose to go the other way — that is, to find the electric field when we know
the potential. As Fig. 24-5 shows, solving this problem graphically is easy: If we
know the potential V at all points near an assembly of charges, we can draw in
a family of equipotential surfaces. The electric field lines, sketched perpendicular
:
E
. What we are seeking here is the math-
to those surfaces, reveal the variation of
ematical equivalent of this graphical procedure.

Figure  24-17  shows  cross  sections  of  a  family  of  closely  spaced  equipo-
tential surfaces, the potential difference between each pair of adjacent surfaces
at any point P is perpendicular to the
being dV. As the figure suggests, the field
equipotential surface through P.

:
E

d s:
Suppose  that  a  positive  test  charge  q0 moves  through  a  displacement
from one equipotential surface to the adjacent surface. From Eq. 24-6, we see that
the work the electric field does on the test charge during the move is  ’q0 dV.
From Eq. 24-16 and Fig. 24-17, we see that the work done by the electric field may
:
or q0E(cos u) ds. Equating these
(q0E
also be written as the scalar product
two expressions for the work yields

) " d s:,

or

’q0 dV $ q0E(cos u) ds,

E cos u $ ’

dV
ds

.

(24-38)

(24-39)

Since E cos u is the component of

:
E

in the direction of

d s:,

Eq. 24-39 becomes

Es $ ’

3V
3s

.

(24-40)

We have added a subscript to E and switched to the partial derivative symbols
to emphasize that Eq. 24-40 involves only the variation of V along a specified axis
(here called the s axis) and only the component of
along that axis. In words,
Eq. 24-40 (which is essentially the reverse operation of Eq. 24-18) states:

:
E

θ

s

q0

P
+

E

ds

Two
equipotential
surfaces

d s:

from one equipotential sur-

Figure 24-17 A test charge q0 moves a
distance
face to another. (The separation between
the surfaces has been exaggerated for clar-
ity.) The displacement  makes an angle
:
u with the direction of the electric field
.E

d s:

702

CHAPTE R  24 E LECTR IC  POTE NTIAL

The component of
electric potential changes with distance in that direction.

in any direction is the negative of the rate at which the

:
E

If we take the s axis to be, in turn, the x, y, and z axes, we find that the x, y, and
z components of

at any point are

:
E

Ex $ ’

3V
3x

;    Ey $ ’

3V
3y

;    Ez $ ’

3V
3z

.

(24-41)

Thus, if we know V for all points in the region around a charge distribution — that
is, if we know the function V(x, y, z) — we can find the components of
, and thus
:
E

itself, at any point by taking partial derivatives.

:
E

For  the  simple  situation  in  which  the  electric  field

becomes

E $ ’

!V
! s

,

:
E

is  uniform, Eq. 24-40

(24-42)

where s is  perpendicular  to  the  equipotential  surfaces. The  component  of  the
electric field is zero in any direction parallel to the equipotential surfaces because
there is no change in potential along the surfaces.

Checkpoint 5
The figure shows
three pairs of parallel
plates with the same
separation, and the
electric potential of
each plate. The elec-
tric field between the
plates is uniform and
perpendicular to the plates. (a) Rank the pairs according to the magnitude of the elec-
tric field between the plates, greatest first. (b) For which pair is the electric field point-
ing rightward? (c) If an electron is released midway between the third pair of plates,
does it remain there, move rightward at constant speed, move leftward at constant
speed, accelerate rightward, or accelerate leftward?

–200 V  –400 V

–20 V  +200 V

–50 V  +150 V

(2)

(3)

(1)

Sample Problem 24.05 Finding the field from the potential

The electric potential at any point on the central axis of a
uniformly charged disk is given by Eq. 24-37,

V $

s
2´0

2

 (

z2 " R2 ’ z).

Starting  with  this  expression, derive  an  expression  for  the
electric field at any point on the axis of the disk.

KEY IDEAS

as a function of distance z along
We want the electric field
the axis of the disk. For any value of z, the direction of  must
be  along  that  axis  because  the  disk  has  circular  symmetry

:
E

:
E

about that axis. Thus, we want the component Ez of
in the
direction of z. This component is the negative of the rate at
which the electric potential changes with distance z.

:
E

Calculation: Thus, from the last of Eqs. 24-41, we can write

Ez $ ’

3V
3z

$ ’

s
2´0

d
dz

 (

z2 " R2 ’ z)

2

$

s

2´0 #1 ’

z

z2 " R2 $.

(Answer)

This is the same expression that we derived in Module 22-5
by integration, using Coulomb’s law.

2

Additional examples, video, and practice available at WileyPLUS
