in the dielectric, shown in Fig. 24.20d, is therefore decreased in magnitude. In
the ﬁeld-line representation, some of the ﬁeld lines leaving the positive plate go
through  the  dielectric,  while  others  terminate  on  the  induced  charges  on  the
faces of the dielectric.

24.6 Gauss’s Law in Dielectrics

807

B

B

As  we  discussed  in  Section  21.2,  polarization  is  also  the  reason  a  charged
body, such as an electriﬁed plastic rod, can exert a force on an uncharged body
such as a bit of paper or a pith ball. Figure 24.21 shows an uncharged dielectric
in the radial ﬁeld of a positively charged body  The induced positive
sphere
experience a force toward the right, while the force on the induced
charges on
negative charges is toward the left. The negative charges are closer to
and thus
are in a stronger ﬁeld, than are the positive charges. The force toward the left is
B
stronger than that toward the right, and
even though its
net charge is zero. The attraction occurs whether the sign of  ’s charge is positive
or negative (see Fig. 21.8). Furthermore, the effect is not limited to dielectrics; an
uncharged conducting body would be attracted in the same way.

is attracted toward
A

A,

A.

A,

Q

and

-Q

Test Your Understanding of Section 24.5 A parallel-plate capacitor has
charges
is then inserted into the
space between the plates as shown in Fig. 24.20. Rank the following electric-ﬁeld magni-
tudes in order from largest to smallest. (i) the ﬁeld before the slab is inserted; (ii) the
resultant ﬁeld after the slab is inserted; (iii) the ﬁeld due to the bound charges.

on its two plates. A dielectric slab with

K = 3

❙

24.6 Gauss’s Law in Dielectrics

We can extend the analysis of Section 24.4 to reformulate Gauss’s law in a form
that is particularly useful for dielectrics. Figure 24.22 is a close-up view of the left
capacitor plate and left surface of the dielectric in Fig. 24.15b. Let’s apply Gauss’s
law to the rectangular box shown in cross section by the purple line; the surface
area of the left and right sides is  The left side is embedded in the conductor that
forms the left capacitor plate, and so the electric ﬁeld everywhere on that surface
is zero. The right side is embedded in the dielectric, where the electric ﬁeld has
magnitude
everywhere on the other four sides. The total charge
enclosed, including both the charge on the capacitor plate and the induced charge
on the dielectric surface, is

so Gauss’s law gives

E(cid:2) = 0

and

A.

E,

Qencl = 1s - si2A,
1s - si2A
P0

EA =

This equation is not very illuminating as it stands because it relates two unknown
But
quantities:
now we can use Eq. (24.16), developed for this same situation, to simplify this
equation by eliminating

inside the dielectric and the induced surface charge density

Equation (24.16) is

si.

E

si.
si = sa1 - 1
K

b  or  s - si =

s

K

Combining this with Eq. (24.21), we get

EA =

sA
KP0

  or  KEA =

sA
P0
S
through the Gaussian surface
,
E
sA
P0.
in Fig. 24.22 is equal to the enclosed free charge
It turns out
that for any Gaussian surface, whenever the induced charge is proportional to the
electric ﬁeld in the material, we can rewrite Gauss’s law as

Equation (24.22) says that the ﬂux of

divided by

(24.22)

S
KE

not

,

S # dA

S

KE

C

=

Qencl-free
P0

(Gauss’s law in a dielectric)

(24.23)

24.21 A neutral sphere
electric ﬁeld of a positively charged sphere
A
polarization.

is attracted to the charge because of

in the radial

B

+
+
+

+

+

++

+

A

+ + +

+

+

+
+
+

–
+
–
+
B
– +

S
E

24.22 Gauss’s law with a dielectric.
This ﬁgure shows a close-up of the left-
hand capacitor plate in Fig. 24.15b. The
Gaussian surface is a rectangular box that
lies half in the conductor and half in the
dielectric.

S

E 5 0

S
E

+
Conductor Dielectric
+

–

–σ
i
–

+
σ
+

+

Gaussian
surface

Conductor

Perspective
view

A

A

Dielectric

(24.21)

Side view

808

CHAPTER 24 Capacitance and Dielectrics

Qencl-free

where
is the total free charge (not bound charge) enclosed by the Gaussian
surface. The signiﬁcance of these results is that the right sides contain only the
free charge on the conductor, not the bound (induced) charge. In fact, although
we have not proved it, Eq. (24.23) remains valid even when different parts of the
Gaussian surface are embedded in dielectrics having different values of
pro-
vided  that  the  value  of
in  each  dielectric  is  independent  of  the  electric  ﬁeld
(usually the case for electric ﬁelds that are not too strong) and that we use the
appropriate value of

for each point on the Gaussian surface.

K,

K

K

Example 24.12

A spherical capacitor with dielectric

Use Gauss’s law to ﬁnd the capacitance of the spherical capacitor
of Example 24.3 (Section 24.1) if the volume between the shells is
ﬁlled with an insulating oil with dielectric constant

K.

SOLUTION

IDENTIFY  and SET  UP: The spherical symmetry of the problem is
not  changed  by  the  presence  of  the  dielectric,  so  as  in  Example
24.3,  we  use  a  concentric  spherical  Gaussian  surface  of  radius
r
between  the  shells.  Since  a  dielectric  is  present,  we  use  Gauss’s
law in the form of Eq. (24.23).

EXECUTE: From Eq. (24.23),

S # dA

S

KE

C

=

C

KE dA = KE

C

dA = 1KE214pr 22 =

Q
P0

E =

Q
4pKP0r 2

=

Q
4pPr 2

P =KP 0

. Compared to the case in which there is vacuum
where
1>K.
between the shells, the electric ﬁeld is reduced by a factor of
between the shells is reduced by the
The potential difference
is increased by a
same factor, and so the capacitance
factor of
just as for a parallel-plate capacitor when a dielectric is
inserted. Using the result of Example 24.3, we ﬁnd that the capaci-
tance with the dielectric is

C = Q>Vab

Vab

K,

C =

4pKP0rarb
rb - ra

=

4pPrarb
rb - ra

EVALUATE:  If the dielectric ﬁlls the volume between the two con-
ductors, the capacitance is just
times the value with no dielectric.
The result is more complicated if the dielectric only partially ﬁlls
this volume (see Challenge Problem 24.78).

K

Test Your Understanding of Section 24.6 A single point charge
in a dielectric of dielectric constant  At a point inside the dielectric a distance
K.
q>4pP0r 2;
from the point charge, what is the magnitude of the electric ﬁeld? (i)
(ii)

(iv) none of these.

q>4pKP0r 2;

Kq>4pP0r 2;

(iii)

q

is imbedded

r

❙
