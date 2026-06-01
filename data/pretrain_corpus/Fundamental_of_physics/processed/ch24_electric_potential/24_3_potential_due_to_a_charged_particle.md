694

CHAPTE R  24 E LECTR IC  POTE NTIAL

24-3 POTENTIAL DUE TO A CHARGED PARTICLE

Learning Objectives
After reading this module, you should be able to . . .

24.14 For a given point in the electric field of a charged parti-
cle, apply the relationship between the electric potential V,
the charge of the particle q, and the distance r from the
particle.

24.15 Identify the correlation between the algebraic signs of the
potential set up by a particle and the charge of the particle.

symmetric charge distribution, calculate the electric
potential as if all the charge is concentrated as a particle
at the center of the sphere.

24.17 Calculate the net potential at any given point due to

several charged particles, identifying that algebraic addi-
tion is used, not vector addition.

24.16 For points outside or on the surface of a spherically

24.18 Draw equipotential lines for a charged particle.

Key Ideas
● The electric potential due to a single charged particle at a
distance r from that charged particle is

1
4p´0
where V has the same sign as q.

V $

q
r

,

● The potential due to a collection of charged particles is

n

V $ ’

i$1

Vi $

1
4p´0

n

’

i$1

qi
ri

.

Thus, the potential is the algebraic sum of the individual po-
tentials, with no consideration of directions.

Potential Due to a Charged Particle
We  now  use  Eq. 24-18  to  derive, for  the  space  around  a  charged  particle, an
expression  for  the  electric  potential  V relative  to  the  zero  potential  at  infinity.
Consider a point P at distance R from a fixed particle of positive charge q (Fig. 24-9).
To use Eq. 24-18, we imagine that we move a positive test charge q0 from point P to
infinity. Because the path we take does not matter, let us choose the simplest one —
a line that extends radially from the fixed particle through P to infinity.

To use Eq. 24-18, we must evaluate the dot product

:
E

" d s: $ E cos 1ds.

(24-22)

:
E

in  Fig. 24-9  is  directed  radially  outward  from  the  fixed
The  electric  field
of the test particle along its path has
particle.Thus, the differential displacement
$
the same direction as
1.
Because the path is radial, let us write ds as dr.Then, substituting the limits R and 0,
we can write Eq. 24-18 as

. That means that in Eq. 24-22, angle u

0 and cos u

d s:

:
E

$

Vf ’ Vi $ ’"0

R

E dr.

(24-23)

Next, we  set  Vf $ 0  (at  0)  and  Vi $ V (at R). Then, for  the  magnitude  of  the
electric field at the site of the test charge, we substitute from Eq. 22-3:

E $

1
4p´0

q
r2 .

With these changes, Eq. 24-23 then gives us

0 ’ V $ ’

q

4p´0 "0

R

1
r2 dr $

$ ’

1
4p´0

q
R

.

q

4p´0 ( 1
r )

0

R

(24-24)

(24-25)

To find the potential of
the charged particle,
we move this test charge
out to infinity.

E

ds

q0

+

P

r

R

+

q

:
E

Figure 24-9 The particle with positive charge
q produces an electric field
and an elec-
tric potential V at point P. We find the
potential by moving a test charge q0 from
P to infinity. The test charge is shown at
distance r from the particle, during differ-
.d s:
ential displacement

Solving for V and switching R to r, we then have

V(r)

24-3 POTE NTIAL  DU E  TO  A  CHARG E D  PARTICLE

695

V $

1
4p´0

q
r

(24-26)

as  the  electric  potential  V due  to  a  particle  of  charge  q at  any  radial  distance
r from the particle.

Although  we  have  derived  Eq. 24-26  for  a  positively  charged  particle, the
derivation holds also for a negatively charged particle, in which case, q is a nega-
tive quantity. Note that the sign of V is the same as the sign of q:

A positively charged particle produces a positive electric potential. A negatively
charged particle produces a negative electric potential.

x

y

Figure 24-10 A computer-generated plot of
the electric potential V(r) due to a positive-
ly charged particle located at the origin of
an xy plane. The potentials at points in the
xy plane are plotted vertically. (Curved
lines have been added to help you visual-
ize the plot.) The infinite value of V pre-
dicted by Eq. 24-26 for r $ 0 is not plotted.

Figure 24-10 shows a computer-generated plot of Eq. 24-26 for a positively
charged particle; the magnitude of V is plotted vertically. Note that the magni-
tude  increases  as  r : 0. In  fact, according  to  Eq. 24-26, V is  infinite  at  r $ 0,
although Fig. 24-10 shows a finite, smoothed-off value there.

Equation 24-26 also gives the electric potential either outside or on the exter-
nal surface of a spherically symmetric charge distribution. We can prove this by
using one of the shell theorems of Modules 21-1 and 23-6 to replace the actual
spherical  charge  distribution  with  an  equal  charge  concentrated  at  its  center.
Then  the  derivation  leading  to  Eq. 24-26  follows, provided  we  do  not  consider
a point within the actual distribution.

Potential Due to a Group of Charged Particles
We can find the net electric potential at a point due to a group of charged parti-
cles with the help of the superposition principle. Using Eq. 24-26 with the plus or
minus sign of the charge included, we calculate separately the potential resulting
from  each  charge  at  the given  point. Then  we  sum  the  potentials. Thus, for  n
charges, the net potential is

n

V $ ’

i$1

Vi $

1
4p´0

n

’

i$1

qi
ri

(n charged particles).

(24-27)

Here qi is the value of the ith charge and ri is the radial distance of the given point
from the ith charge. The sum in Eq. 24-27 is an algebraic sum, not a vector sum
like  the  sum  that  would  be  used  to  calculate  the  electric  field  resulting  from
a group of charged particles. Herein lies an important computational advantage
of potential over electric field: It is a lot easier to sum several scalar quantities
than to  sum  several  vector  quantities  whose  directions  and  components  must
be considered.

Checkpoint 3

The figure here shows three arrangements of two protons. Rank the arrangements ac-
cording to the net electric potential produced at point P by the protons, greatest first.

D

d

(a)

P

P

d

D

(b)

d

D

P

(c)

696

CHAPTE R  24 E LECTR IC  POTE NTIAL

Sample Problem 24.03 Net potential of several charged particles

What is the electric potential at point P, located at the cen-
ter of the square of charged particles shown in Fig. 24-11a?
The distance d is 1.3 m, and the charges are

q1 $ "12 nC,    q3 $ "31 nC,
q2 $ ’24 nC,    q4 $ "17 nC.

KEY IDEA

The  electric  potential V at  point  P is  the  algebraic  sum  of
the  electric  potentials  contributed  by  the  four  particles.

q1

d

q3

d

d

q2

q1

P

d

P

V = 350 V

q4

q3

q2

q4

(a)

(b)

Figure 24-11 (a) Four charged particles. (b) The closed curve is a
(roughly drawn) cross section of the equipotential surface that
contains point P.

(Because electric potential is a scalar, the orientations of the
particles do not matter.)

Calculations: From Eq. 24-27, we have

4

V $ ’

i$1

Vi $

1

4p´0 # q1

r

"

q2
r

"

q3
r

"

q4
r $.

The distance r is
charges is

d/

 2

, which is 0.919 m, and the sum of the

1

q1 " q2 " q3 " q4 $ (12 ’ 24 " 31 " 17) ( 10’9 C
$ 36 ( 10’9 C.

Thus,

V $

(8.99 ( 109 N#m2/C2)(36 ( 10’9 C)
0.919 m

% 350 V.

(Answer)

Close  to  any  of  the  three  positively  charged  particles  in
Fig. 24-11a, the  potential  has  very  large  positive  values.
Close  to  the  single  negative  charge, the  potential  has  very
large negative values. Therefore, there must be points within
the square that have the same intermediate potential as that
at point P. The curve in Fig. 24-11b shows the intersection of
the  plane  of  the  figure  with  the  equipotential  surface  that
contains point P.

Sample Problem 24.04 Potential is not a vector, orientation is irrelevant

e)  are  equally
(a)  In  Fig. 24-12a, 12  electrons  (of  charge
spaced  and  fixed  around  a  circle  of  radius  R. Relative  to
V $ 0  at  infinity, what  are  the  electric  potential  and  electric
field at the center C of the circle due to these electrons?

’

KEY IDEAS

(1) The electric potential V at C is the algebraic sum of the
electric potentials contributed by all the electrons. Because

Potential is a scalar and
orientation is irrelevant.

R

C

R

C

120°

(a)

(b)

Figure 24-12 (a) Twelve electrons uniformly spaced around a circle.
(b) The electrons nonuniformly spaced along an arc of the original circle.

electric potential is a scalar, the orientations of the electrons
do not matter. (2) The electric field at C is a vector quantity
and thus the orientation of the electrons is important.

Calculations: Because the electrons all have the same nega-
tive  charge  ’e and  are  all  the  same  distance  R from C, Eq.
24-27 gives us

V $ ’12

.

(Answer)

(24-28)

1
4p´0

e
R

Because of the symmetry of the arrangement in Fig. 24-12a,
the  electric  field  vector  at  C due  to  any  given  electron  is
canceled by the field vector due to the electron that is dia-
metrically opposite it. Thus, at C,

:
E

$ 0.

(Answer)

(b) The electrons are moved along the circle until they are
nonuniformly spaced over a 120% arc (Fig. 24-12b). At C, find
the electric potential and describe the electric field.

Reasoning: The potential is still given by Eq. 24-28, because
the distance between C and each electron is unchanged and
orientation  is  irrelevant. The  electric  field  is  no  longer  zero,
however, because  the  arrangement  is  no  longer  symmetric.
A net field is now directed toward the charge distribution.

Additional examples, video, and practice available at WileyPLUS
