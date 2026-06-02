698

CHAPTE R  24 E LECTR IC  POTE NTIAL

The electric field shifts the positive
and negative charges, creating a dipole.

+

(a)

E

p

+

(b)

Figure 24-14 (a) An atom, showing the posi-
tively charged nucleus (green) and the
negatively charged electrons (gold
shading). The centers of positive and nega-
tive charge coincide. (b) If the atom is
placed in an external electric field
electron orbits are distorted so that the
centers of positive and negative charge no
longer coincide. An induced dipole
p:
moment
ly exaggerated here.

appears. The distortion is great-

, the

:
E

Checkpoint 4

Suppose that three points are set at equal (large) distances r from the center of the
dipole in Fig. 24-13: Point a is on the dipole axis above the positive charge, point b is on
the axis below the negative charge, and point c is on a perpendicular bisector through
the line connecting the two charges. Rank the points according to the electric potential
of the dipole there, greatest (most positive) first.

Induced Dipole Moment
Many molecules, such as water, have permanent electric dipole moments. In other
molecules (called nonpolar molecules) and in every isolated atom, the centers of
the  positive  and  negative  charges  coincide  (Fig. 24-14a)  and  thus  no  dipole
moment is set up. However, if we place an atom or a nonpolar molecule in an
external electric field, the field distorts the electron orbits and separates the centers
of positive and negative charge (Fig. 24-14b). Because the electrons are negatively
charged, they tend to be shifted in a direction opposite the field. This shift sets up a
dipole moment
that points in the direction of the field. This dipole moment is
said to be induced by the field, and the atom or molecule is then said to be polar-
ized by the field (that is, it has a positive side and a negative side). When the field is
removed, the induced dipole moment and the polarization disappear.

p:

24-5 POTENTIAL DUE TO A CONTINUOUS CHARGE DISTRIBUTION

Learning Objective
After reading this module, you should be able to . . .

24.22 For charge that is distributed uniformly along a line or over a surface, find the net potential at a given point by splitting the

distribution up into charge elements and summing (by integration) the potential due to each one.

Key Ideas
● For a continuous distribution of charge (over an extended
object), the potential is found by (1) dividing the distribution
into charge elements dq that can be treated as particles and
then (2) summing the potential due to each element by inte-
grating over the full distribution:
1

V $

4p)0" dq

r

.

● In order to carry out the integration, dq is replaced with the
product of either a linear charge density l and a length ele-
ment (such as dx), or a surface charge density s and area ele-
ment (such as dx dy).
● In some cases where the charge is symmetrically distrib-
uted, a two-dimensional integration can be reduced to a one-
dimensional integration.

Potential Due to a Continuous Charge Distribution
When  a  charge  distribution  q is  continuous  (as  on  a  uniformly  charged  thin  rod
or disk), we cannot use the summation of Eq. 24-27 to find the potential V at a point
P. Instead, we  must  choose  a  differential  element  of  charge  dq, determine the
potential dV at P due to dq, and then integrate over the entire charge distribution.

Let us again take the zero of potential to be at infinity. If we treat the element of
charge dq as a particle, then we can use Eq. 24-26 to express the potential dV at point
P due to dq:

dV $

1
4p´0

dq
r

(positive or negative dq).

(24-31)

Here r is the distance between P and dq. To find the total potential V at P, we

24-5 POTE NTIAL  DU E  TO  A  CONTI N UOUS  CHARG E  DISTR I B UTION

699

integrate to sum the potentials due to all the charge elements:

V $ " dV $

1

4p´0 " dq

r

.

(24-32)

The integral must be taken over the entire charge distribution. Note that because
the  electric  potential  is  a  scalar, there  are  no  vector  components to  consider  in
Eq. 24-32.

We now examine two continuous charge distributions, a line and a disk.

Line of Charge
In  Fig. 24-15a, a  thin  nonconducting  rod  of  length  L has  a  positive  charge  of
uniform linear density l. Let us determine the electric potential V due to the rod
at point P, a perpendicular distance d from the left end of the rod.

We consider a differential element dx of the rod as shown in Fig. 24-15b. This

(or any other) element of the rod has a differential charge of

dq $ l dx.

(24-33)

This  element  produces  an  electric  potential  dV at  point  P, which  is  a  distance
r $ (x2 " d 2)1/2 from  the  element  (Fig. 24-15c). Treating  the  element  as  a  point
charge, we can use Eq. 24-31 to write the potential dV as

dV $

1
4p´0

dq
r

$

1
4p´0

l dx
(x2 " d 2)1/2 .

(24-34)

A

P

d

P

d

But we can treat this
element as a particle.

P

d

r

Here is how to find
distance r from the
element.

x

dx

x

x

dx

(c)

(b)

r

This charged rod
is obviously not a
particle.

P

d

x

L

(a)

Our job is to add the
potentials due to all
the elements.

x

P

d = r

x = 0

Here is the leftmost
element.

Here is the rightmost
element.

(d )

(e )

x

x = L

Figure 24-15 (a) A thin, uniformly charged rod produces an electric potential V at point P. (b) An
element can be treated as a particle. (c) The potential at P due to the element depends on the
distance r. We need to sum the potentials due to all the elements, from the left side (d) to the
right side (e).

700

CHAPTE R  24 E LECTR IC  POTE NTIAL

Since the charge on the rod is positive and we have taken V $ 0 at infinity, we
know from Module 24-3 that dV in Eq. 24-34 must be positive.

We now find the total potential V produced by the rod at point P by integrat-
ing Eq. 24-34 along the length of the rod, from x $ 0 to x $ L (Figs. 24-15d and e),
using integral 17 in Appendix E. We find

l
(x2 " d 2)1/2 dx

0

l

1
4p´0

V $ "dV $ "L
4p´0 "L
4p´0 (ln#x " (x2 " d 2)1/2$)0

dx
(x2 " d 2)1/2

$

$

l

0

L

$

l

4p´0 (ln#L " (L2 " d2)1/2$ ’ ln d).

We can simplify this result by using the general relation ln A ln B ln(A/B).
We then find

$

’

V $

l
4p´0

 ln ( L " (L2 " d 2)1/2

d

).

(24-35)

Because V is the sum of positive values of dV, it too is positive, consistent with
the logarithm being positive for an argument greater than 1.

Charged Disk
In Module 22-5, we calculated the magnitude of the electric field at points on the
central axis of a plastic disk of radius R that has a uniform charge density s on
one surface. Here we derive an expression for V(z), the electric potential at any
point on the central axis. Because we have a circular distribution of charge on the
disk, we could start with a differential element that occupies angle du and radial
distance dr. We  would  then  need  to  set  up  a  two-dimensional  integration.
However, let’s do something easier.

In Fig. 24-16, consider a differential element consisting of a flat ring of radius

R. and radial width dR.. Its charge has magnitude

dq $ s(2pR.)(dR.),

P

r

z

Every charge element
in the ring contributes
to the potential at P.

in  which  (2pR.)(dR.)  is  the  upper  surface  area  of  the  ring. All  parts  of  this
charged element are the same distance r from point P on the disk’s axis. With the
aid of Fig. 24-16, we can use Eq. 24-31 to write the contribution of this ring to
the electric potential at P as

R'

R

dR'

dV $

1
4p´0

dq
r

$

1
4p´0

s(2pR.)(dR.)

z2 " R.2

.

(24-36)

We find the net potential at P by adding (via integration) the contributions of all
the rings from R. $ 0 to R. $ R:

2

Figure 24-16 A plastic disk of radius R,
charged on its top surface to a uniform
surface charge density s. We wish to
find the potential V at point P on the
central axis of the disk.

V $ "dV $

s

2´0 "R

0

R. dR.

z2 " R.2

$

s
2´0

 (

z2 " R2 ’ z).

(24-37)

2

Note that the variable in the second integral of Eq. 24-37 is R. and not z, which
remains constant while the integration over the surface of the disk is carried out.
(Note also that, in evaluating the integral, we have assumed that z - 0.)

2
