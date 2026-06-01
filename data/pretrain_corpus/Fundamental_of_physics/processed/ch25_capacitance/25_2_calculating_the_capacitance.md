25-2 CALCU L ATI NG  TH E  CAPACITANCE

719

The  circuit  shown  in  Figs. 25-4a and b is  said  to  be  incomplete because
switch S is open; that is, the switch does not electrically connect the wires at-
tached to it. When the switch is closed, electrically connecting those wires, the
circuit is complete and charge can then flow through the switch and the wires.
As we discussed in Chapter 21, the charge that can flow through a conductor,
such as a wire, is that of electrons. When the circuit of Fig. 25-4 is completed,
electrons are driven through the wires by an electric field that the battery sets
up in the wires. The field drives electrons from capacitor plate h to the positive
terminal  of  the  battery; thus, plate  h, losing  electrons, becomes  positively
charged. The field drives just as many electrons from the negative terminal of
the battery to capacitor plate l; thus, plate l, gaining electrons, becomes nega-
tively  charged  just  as  much as  plate  h, losing  electrons, becomes  positively
charged.

Initially, when the plates are uncharged, the potential difference between
them is zero. As the plates become oppositely charged, that potential differ-
ence increases until it equals the potential difference V between the terminals
of the battery. Then plate h and the positive terminal of the battery are at the
same  potential, and  there  is  no  longer  an  electric  field  in  the  wire  between
them. Similarly, plate  l and  the  negative  terminal  reach  the  same  potential,
and  there  is  then  no  electric  field  in  the  wire  between  them. Thus, with  the
field zero, there is no further drive of electrons. The capacitor is then said to
be fully charged, with a potential difference V and charge q that are related
by Eq. 25-1.

In this book we assume that during the charging of a capacitor and after-
ward, charge cannot pass from one plate to the other across the gap separating
them. Also, we assume that a capacitor can retain (or store) charge indefinitely,
until it is put into a circuit where it can be discharged.

Checkpoint 1

Does the capacitance C of a capacitor increase, decrease, or remain the same (a) when
the charge q on it is doubled and (b) when the potential difference V across it is tripled?

25-2 CALCULATING THE CAPACITANCE

Learning Objectives
After reading this module, you should be able to . . .

25.04 Explain how Gauss’ law is used to find the capacitance of a parallel-plate capacitor.
25.05 For a parallel-plate capacitor, a cylindrical capacitor, a spherical capacitor, and an isolated sphere, calculate the capacitance.

Key Ideas
● We generally determine the capacitance of a particular
capacitor configuration by (1) assuming a charge q to have
been placed on the plates, (2) finding the electric field  due
to this charge, (3) evaluating the potential difference V be-
tween the plates, and (4) calculating C from q ! CV. Some
results are the following:
● A parallel-plate capacitor with flat parallel plates of area A
and spacing d has capacitance

:
E

C !

´0A
d

.

L and radii a and b has capacitance

C ! 2p´0

L
ln(b
a)

.

● A spherical capacitor with concentric spherical plates of
radii a and b has capacitance

C ! 4p´0

ab
b # a

.

● An isolated sphere of radius R has capacitance

● A cylindrical capacitor (two long coaxial cylinders) of length

C ! 4p´0R.

720

CHAPTE R  25 CAPACITANCE

Calculating the Capacitance
Our  goal  here  is  to  calculate  the  capacitance  of  a  capacitor  once  we  know  its
geometry. Because we shall consider a number of different geometries, it seems
wise to develop a general plan to simplify the work. In brief our plan is as follows:
(1) Assume a charge q on the plates; (2) calculate the electric field
between
the plates in terms of this charge, using Gauss’ law; (3) knowing
, calculate the
potential difference V between the plates from Eq. 24-18; (4) calculate C from
Eq. 25-1.

:
E

:
E

Before we start, we can simplify the calculation of both the electric field
and the potential difference by making certain assumptions. We discuss each in
turn.

Calculating the Electric Field
:
To relate the electric field  between the plates of a capacitor to the charge q on
E
either plate, we shall use Gauss’ law:

´0, E

:

:
" dA

! q.

(25-3)

Here q is  the  charge  enclosed  by  a  Gaussian  surface  and
is  the  net
electric flux through that surface. In all cases that we shall consider, the Gaussian
surface will be such that whenever there is an electric flux through it, will have
:
a uniform magnitude E and the vectors
E
will be parallel. Equation 25-3
then reduces to

:
dA

and

:
E

:
- E

:
" dA

q ! ´0EA (special case of Eq. 25-3),

(25-4)

in which A is the area of that part of the Gaussian surface through which there is
a flux. For convenience, we shall always draw the Gaussian surface in such a way
that it completely encloses the charge on the positive plate; see Fig. 25-5 for an
example.

Calculating the Potential Difference
In  the  notation  of  Chapter  24  (Eq. 24-18), the  potential  difference  between
the plates of a capacitor is related to the field  by

:
E

Vf # Vi ! #"f

i

:
E

" ds:,

(25-5)

in which the integral is to be evaluated along any path that starts on one plate
and ends  on  the  other. We  shall  always  choose  a  path  that  follows  an  electric
field line, from the negative plate to the positive plate. For this path, the vectors
:
E
will be equal
to E ds. Thus, the right side of Eq. 25-5 will then be positive. Letting V represent
the difference Vf # Vi, we can then recast Eq. 25-5 as

will have opposite directions; so the dot product

and
#

" ds:

d s:

:
E

V ! "%

#

E ds

(special case of Eq. 25-5),

(25-6)

in which the # and % remind us that our path of integration starts on the nega-
tive plate and ends on the positive plate.

We are now ready to apply Eqs. 25-4 and 25-6 to some particular cases.

A Parallel-Plate Capacitor
We assume, as Fig. 25-5 suggests, that the plates of our parallel-plate capacitor are
so large and so close together that we can neglect the fringing of the electric field

We use Gauss’ law to relate
q and E. Then we integrate the
E to get the potential difference.

+ + + + + + + + + +

+q

Ad

–q

– – – – – – – – – –

Gaussian
surface

Path of
integration

Figure 25-5 A charged parallel-plate capaci-
tor. A Gaussian surface encloses the charge
on the positive plate. The integration of
Eq. 25-6 is taken along a path extending
directly from the negative plate to the
positive plate.

25-2 CALCU L ATI NG  TH E  CAPACITANCE

721

at the edges of the plates, taking
the plates.

:
E

to be constant throughout the region between

We draw a Gaussian surface that encloses just the charge q on the positive

plate, as in Fig. 25-5. From Eq. 25-4 we can then write

where A is the area of the plate.

Equation 25-6 yields

q ! ´0EA,

V ! "%

#

E ds ! E"d

0

ds ! Ed.

(25-7)

(25-8)

In Eq. 25-8, E can be placed outside the integral because it is a constant; the sec-
ond integral then is simply the plate separation d.

If we now substitute q from Eq. 25-7 and V from Eq. 25-8 into the relation

q ! CV (Eq. 25-1), we find

C !

+0 A
d

(parallel-plate capacitor).

(25-9)

Thus, the capacitance does indeed depend only on geometrical factors — namely,
the plate area A and the plate separation d. Note that C increases as we increase
area A or decrease separation d.

As an aside, we point out that Eq. 25-9 suggests one of our reasons for writing
the  electrostatic  constant  in  Coulomb’s  law  in  the  form  1/4p´0. If  we  had  not
done  so, Eq. 25-9 — which  is  used  more  often  in  engineering  practice  than
Coulomb’s  law — would  have  been  less  simple  in  form. We  note  further  that
Eq. 25-9 permits us to express the permittivity constant ´0 in a unit more appro-
priate for use in problems involving capacitors; namely,

´0 ! 8.85 $ 10#12 F/m ! 8.85 pF/m.

We have previously expressed this constant as

´0 ! 8.85 $ 10#12 C2/N &m2.

(25-10)

(25-11)

A Cylindrical Capacitor
Figure 25-6 shows, in cross section, a cylindrical capacitor of length L formed by
two  coaxial  cylinders  of  radii  a and b. We  assume  that  L * b so  that  we  can
neglect the fringing of the electric field that occurs at the ends of the cylinders.
Each plate contains a charge of magnitude q.

As a Gaussian surface, we choose a cylinder of length L and radius r, closed
by end caps and placed as is shown in Fig. 25-6. It is coaxial with the cylinders
and encloses  the  central  cylinder  and  thus  also  the  charge q on  that  cylinder.
Equation 25-4 then relates that charge and the field magnitude E as

q ! ´0EA ! ´0E(2prL),

in  which  2prL is  the  area  of  the  curved  part  of  the  Gaussian  surface. There  is
no flux through the end caps. Solving for E yields

E !

q
2p´0Lr

.

(25-12)

Substitution of this result into Eq. 25-6 yields

V ! "%

#

E ds ! #

q

2p´0L "a

b

dr
r

!

q
2p´0L

 ln# b
a $,

(25-13)

where we have used the fact that here ds ! #dr (we integrated radially inward).

Total charge +q

Total charge –q

–

–

–

–

–

–

–

–

–

+
+
+
+
+

++++
b
a

r
+ + +  +

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

Path of
integration

Gaussian
surface

Figure 25-6 A cross section of a long cylindri-
cal capacitor, showing a cylindrical
Gaussian surface of radius r (that encloses
the positive plate) and the radial path of
integration along which Eq. 25-6 is to be
applied. This figure also serves to illustrate
a spherical capacitor in a cross section
through its center.

722

CHAPTE R  25 CAPACITANCE

From the relation C ! q/V, we then have

C ! 2p´0

L
ln(b/a)

(cylindrical capacitor).

(25-14)

We see that the capacitance of a cylindrical capacitor, like that of a parallel-plate
capacitor, depends only on geometrical factors, in this case the length L and the
two radii b and a.

A Spherical Capacitor
Figure 25-6 can also serve as a central cross section of a capacitor that consists of
two concentric spherical shells, of radii a and b. As a Gaussian surface we draw a
sphere of radius r concentric with the two shells; then Eq. 25-4 yields

q ! ´0EA ! ´0E(4pr 2),
in which 4pr2 is the area of the spherical Gaussian surface. We solve this equation
for E, obtaining

E !

1
4p´0

q
r2  ,

(25-15)

which  we  recognize  as  the  expression  for  the  electric  field  due  to  a  uniform
spherical charge distribution (Eq. 23-15).

If we substitute this expression into Eq. 25-6, we find

V ! "%

#

E ds ! #

q

4p´0 "a

b

dr
r2 !

q

4p´0 # 1

a

#

1

b $ !

q
4p´0

b # a
ab

,

(25-16)

where again we have substituted #dr for ds. If we now substitute Eq. 25-16 into
Eq. 25-1 and solve for C, we find

C ! 4p´0

ab
b # a

(spherical capacitor).

(25-17)

An Isolated Sphere
We can assign a capacitance to a single isolated spherical conductor of radius R
by  assuming  that  the “missing  plate” is  a  conducting  sphere  of  infinite  radius.
After  all, the  field  lines  that  leave  the  surface  of  a  positively  charged  isolated
conductor must end somewhere; the walls of the room in which the conductor is
housed can serve effectively as our sphere of infinite radius.

To find the capacitance of the conductor, we first rewrite Eq. 25-17 as

a
1 # a/b
If we then let b : , and substitute R for a, we find

C ! 4p´0

.

C ! 4p´0R (isolated sphere).

(25-18)

Note that this formula and the others we have derived for capacitance (Eqs. 25-9,
25-14, and  25-17)  involve  the  constant  ´0 multiplied  by  a  quantity  that  has  the
dimensions of a length.

Checkpoint 2

For capacitors charged by the same battery, does the charge stored by the capacitor
increase, decrease, or remain the same in each of the following situations? (a) The
plate separation of a parallel-plate capacitor is increased. (b) The radius of the inner
cylinder of a cylindrical capacitor is increased. (c) The radius of the outer spherical
shell of a spherical capacitor is increased.
