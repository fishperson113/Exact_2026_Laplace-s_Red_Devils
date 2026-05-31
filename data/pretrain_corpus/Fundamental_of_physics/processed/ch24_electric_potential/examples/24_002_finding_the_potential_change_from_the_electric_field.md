Sample Problem 24.02
Finding the potential change from the electric field
(a) Figure 24-8a shows two points i and f in a uniform elec-
tric field 
.The points lie on the same electric field line (not
shown) and are separated by a distance d. Find the potential
difference Vf ' Vi by moving a positive test charge q0 from
i to f along the path shown, which is parallel to the field
direction.
KEY IDEA
We can find the potential difference between any two points
in an electric field by integrating 
along a path con-
necting those two points according to Eq. 24-18.
Calculations: We have actually already done the calculation
for such a path in the direction of an electric field line in a
uniform field when we derived Eq.24-21.With slight changes in
notation,Eq.24-21 gives us
Vf ' Vi $ 'Ed.
(Answer)
(b) Now find the potential difference Vf ' Vi by moving the
positive test charge q0 from i to f along the path icf shown in
Fig.24-8b.
Calculations: The Key Idea of (a) applies here too, except
now we move the test charge along a path that consists of
two lines: ic and cf. At all points along line ic, the displace-
E
:"ds:
E
:
(a)
(b)
d
i
f
q0
d
i
f
q0
q0
c
45°
45°
+
+
+
ds
ds
ds
E
E
E
The electric field points from
higher potential to lower potential.
The field is perpendicular to this ic path, 
so there is no change in the potential.
The field has a component
along this cf path, so there
is a  change in the potential.
Higher potential
Lower potential
Additional examples, video, and practice available at WileyPLUS

694
CHAPTER 24
ELECTRIC POTENTIAL
q0
r
R
P
q
+
+
ds
E
To find the potential of
the charged particle,
we move this test charge
out to infinity.
Figure 24-9 The particle with positive charge
q produces an electric field 
and an elec-
tric potential V at point P. We find the
potential by moving a test charge q0 from
P to infinity. The test charge is shown at
distance r from the particle, during differ-
ential displacement 
.
d s:
E
:
24-3 POTENTIAL DUE TO A CHARGED PARTICLE
After reading this module, you should be able to . . .
24.14 For a given point in the electric field of a charged parti-
cle, apply the relationship between the electric potential V,
the charge of the particle q, and the distance r from the
particle.
24.15 Identify the correlation between the algebraic signs of the
potential set up by a particle and the charge of the particle.
24.16 For points outside or on the surface of a spherically
symmetric charge distribution, calculate the electric
potential as if all the charge is concentrated as a particle
at the center of the sphere.
24.17 Calculate the net potential at any given point due to
several charged particles, identifying that algebraic addi-
tion is used, not vector addition.
24.18 Draw equipotential lines for a charged particle.
Learning Objectives
●The electric potential due to a single charged particle at a
distance r from that charged particle is
where V has the same sign as q.
V $
1
4p´0
q
r ,
●The potential due to a collection of charged particles is
Thus, the potential is the algebraic sum of the individual po-
tentials, with no consideration of directions.
V $ '
n
i$1
Vi $
1
4p´0 '
n
i$1
qi
ri
.
Key Ideas
Potential Due to a Charged Particle
We now use Eq. 24-18 to derive, for the space around a charged particle, an
expression for the electric potential V relative to the zero potential at infinity.
Consider a point P at distance R from a fixed particle of positive charge q (Fig.24-9).
To use Eq. 24-18, we imagine that we move a positive test charge q0 from point P to
infinity.Because the path we take does not matter,let us choose the simplest one-
a line that extends radially from the fixed particle through P to infinity.
To use Eq. 24-18, we must evaluate the dot product
(24-22)
The electric field 
in Fig. 24-9 is directed radially outward from the fixed 
particle.Thus,the differential displacement 
of the test particle along its path has
the same direction as 
. That means that in Eq. 24-22, angle u
0 and cos u
1.
Because the path is radial,let us write ds as dr.Then,substituting the limits R and 0,
we can write Eq.24-18 as
(24-23)
Next, we set Vf $ 0 (at 0) and Vi $ V (at R). Then, for the magnitude of the
electric field at the site of the test charge, we substitute from Eq. 22-3:
(24-24)
With these changes, Eq. 24-23 then gives us
(24-25)
$ '
1
4p´0
q
R .
0 ' V $ '
q
4p´0 "
0
R
1
r2 dr $
q
4p´0 (
1
r)
0
R
E $
1
4p´0
q
r2 .
Vf ' Vi $ '"
0
R
E dr.
$
$
E
:
ds:
E
:
E
:"ds: $ E cos 1 ds.

695
24-3 POTENTIAL DUE TO A CHARGED PARTICLE
Solving for V and switching R to r, we then have
(24-26)
as the electric potential V due to a particle of charge q at any radial distance
r from the particle.
Although we have derived Eq. 24-26 for a positively charged particle, the
derivation holds also for a negatively charged particle, in which case, q is a nega-
tive quantity. Note that the sign of V is the same as the sign of q:
V $
1
4p´0
q
r
A positively charged particle produces a positive electric potential. A negatively
charged particle produces a negative electric potential.
Figure 24-10 A computer-generated plot of
the electric potential V(r) due to a positive-
ly charged particle located at the origin of
an xy plane. The potentials at points in the
xy plane are plotted vertically. (Curved
lines have been added to help you visual-
ize the plot.) The infinite value of V pre-
dicted by Eq. 24-26 for r $ 0 is not plotted.
x
y
V(r)
Figure 24-10 shows a computer-generated plot of Eq. 24-26 for a positively
charged particle; the magnitude of V is plotted vertically. Note that the magni-
tude increases as r : 0. In fact, according to Eq. 24-26, V is infinite at r $ 0,
although Fig. 24-10 shows a finite, smoothed-off value there.
Equation 24-26 also gives the electric potential either outside or on the exter-
nal surface of a spherically symmetric charge distribution. We can prove this by
using one of the shell theorems of Modules 21-1 and 23-6 to replace the actual
spherical charge distribution with an equal charge concentrated at its center.
Then the derivation leading to Eq. 24-26 follows, provided we do not consider
a point within the actual distribution.
Potential Due to a Group of Charged Particles
We can find the net electric potential at a point due to a group of charged parti-
cles with the help of the superposition principle. Using Eq. 24-26 with the plus or
minus sign of the charge included, we calculate separately the potential resulting
from each charge at the given point. Then we sum the potentials. Thus, for n
charges, the net potential is
(n charged particles).
(24-27)
Here qi is the value of the ith charge and ri is the radial distance of the given point
from the ith charge. The sum in Eq. 24-27 is an algebraic sum, not a vector sum
like the sum that would be used to calculate the electric field resulting from
a group of charged particles. Herein lies an important computational advantage
of potential over electric field: It is a lot easier to sum several scalar quantities
than to sum several vector quantities whose directions and components must
be considered.
V $ '
n
i$1
Vi $
1
4p´0 '
n
i$1
qi
ri
Checkpoint 3
The figure here shows three arrangements of two protons. Rank the arrangements ac-
cording to the net electric potential produced at point P by the protons, greatest first.
P
d
D
(b)
P
D
d
D
d
P
(a)
(c)

696
CHAPTER 24
ELECTRIC POTENTIAL
electric potential is a scalar, the orientations of the electrons
do not matter. (2) The electric field at C is a vector quantity
and thus the orientation of the electrons is important.
Calculations: Because the electrons all have the same nega-
tive charge 'e and are all the same distance R from C, Eq.
24-27 gives us
(Answer)
(24-28)
Because of the symmetry of the arrangement in Fig. 24-12a,
the electric field vector at C due to any given electron is
canceled by the field vector due to the electron that is dia-
metrically opposite it.Thus, at C,
(Answer)
(b) The electrons are moved along the circle until they are
nonuniformly spaced over a 120% arc (Fig. 24-12b).At C, find
the electric potential and describe the electric field.
Reasoning: The potential is still given by Eq. 24-28, because
the distance between C and each electron is unchanged and
orientation is irrelevant. The electric field is no longer zero,
however, because the arrangement is no longer symmetric.
A net field is now directed toward the charge distribution.
E
:$ 0.
V $ '12
1
4p´0
e
R .
