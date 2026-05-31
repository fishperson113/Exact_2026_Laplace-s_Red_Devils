800

CHAPTER 24 Capacitance and Dielectrics

(b) The electric ﬁeld in the region
conducting  spheres  has  magnitude
density in this region is

ra 6 r 6 rb
E = Q>4pP0r 2.

between the two
The  energy

u = 1
2

P0E 2 = 1

2

P0a

2

b

=

Q
4pP0r 2

Q2
32p2P0r 4

The  energy  density  is  not uniform;  it  decreases  rapidly  with
increasing  distance  from  the  center  of  the  capacitor.  To  ﬁnd  the
total electric-ﬁeld energy, we integrate
(the energy per unit vol-
.  We  divide  this  region  into
ume)  over  the  region
and
spherical  shells  of  radius
volume

dV = 4pr 2 dr

ra 6 r 6 rb

r,
. Then

surface  area

thickness

4pr 2,

dr,

u

a

Q2
32p2P0r 4
Q2
a - 1
8pP0
rb

b4pr 2dr

+ 1
ra

b

U =

u dV =

L

rb

L
ra

=

=

=

rb

Q2
dr
8pP0 L
r 2
ra
Q2
rb - ra
8pP0
rarb

EVALUATE: Electric  potential  energy  can  be  regarded  as  being
associated with either the charges, as in part (a), or the ﬁeld, as in
part  (b);  the  calculated  amount  of  stored  energy  is  the  same  in
either case.

Test Your Understanding of Section 24.3 You want to connect a
capacitor and an
capacitor have a greater amount of stored energy than the
(ii) parallel; (iii) either series or parallel; (iv) neither series nor parallel.

capacitor. With which type of connection will the

4-mF
capacitor? (i) series;

8-mF

8-mF

4-mF

❙

24.13 A common type of capacitor uses
dielectric sheets to separate the conductors.

Conductor
(metal foil)

Conductor
(metal foil)

Dielectric
(plastic sheets)

24.4 Dielectrics

Most capacitors have a nonconducting material, or dielectric, between their con-
ducting plates. A common type of capacitor uses long strips of metal foil for the
plates,  separated  by  strips  of  plastic  sheet  such  as  Mylar. A sandwich  of  these
materials  is  rolled  up,  forming  a  unit  that  can  provide  a  capacitance  of  several
microfarads in a compact package (Fig. 24.13).

Placing a solid dielectric between the plates of a capacitor serves three func-
tions.  First,  it  solves  the  mechanical  problem  of  maintaining  two  large  metal
sheets at a very small separation without actual contact.

Second, using a dielectric increases the maximum possible potential differ-
ence between the capacitor plates. As we described in Section 23.3, any insulat-
ing material, when subjected to a sufﬁciently large electric ﬁeld, experiences a
partial  ionization  that  permits  conduction  through  it.  This  is  called  dielectric
breakdown. Many dielectric materials can tolerate stronger electric ﬁelds with-
out breakdown than can air. Thus using a dielectric allows a capacitor to sustain
a  higher  potential  difference
and  so  store  greater  amounts  of  charge  and
energy.

V

Third,  the  capacitance  of  a  capacitor  of  given  dimensions  is  greater when
there is a dielectric material between the plates than when there is vacuum. We
can demonstrate this effect with the aid of a sensitive electrometer, a device that
measures  the  potential  difference  between  two  conductors  without  letting  any
appreciable charge ﬂow from one to the other. Figure 24.14a shows an electrom-
eter connected across a charged capacitor, with magnitude of charge
on each
plate and potential difference  When we insert an uncharged sheet of dielec-
tric, such as glass, parafﬁn, or polystyrene, between the plates, experiment shows
(Fig. 24.14b). When
that the potential difference decreases to a smaller value
V0,
we remove the dielectric, the potential difference returns to its original value
showing that the original charges on the plates have not changed.

V0.

Q

V

C0 = Q>V0,

V

is less than

is  given  by

C0
C = Q>V.

C
and  the  capacitance
The  original  capacitance
is the same in both cases,
with the dielectric present is
so we conclude that the capacitance  with the dielectric
and
C0.
present is greater than  When the space between plates is completely ﬁlled by
C0
the  dielectric,  the  ratio  of
)  is  called  the
dielectric constant of the material,

(equal  to  the  ratio  of
K:

The charge

V0,

to

to

V0

Q

C

C

V

    (definition of dielectric constant)

(24.12)

K = C
C0

When  the  charge  is  constant,
Eq. (24.12) can be rewritten as
V0
K

V =

Q = C0V0 = CV

and

C>C0 = V0>V.

In  this  case,

    1when Q is constant2

(24.13)

With  the  dielectric  present,  the  potential  difference  for  a  given  charge
reduced by a factor

K.

Q

is

K

K

C

K = 1

The dielectric constant

is a pure number. Because

is always greater than unity. Some representative values of

is always greater than
KC0,
are given in
Table  24.1.  For  vacuum,
by  deﬁnition.  For  air  at  ordinary  temperatures
is about 1.0006; this is so nearly equal to 1 that for most pur-
and pressures,
poses an air capacitor is equivalent to one in vacuum. Note that while water has a
very large value of
it is usually not a very practical dielectric for use in capac-
itors. The reason is that while pure water is a very poor conductor, it is also an
excellent ionic solvent. Any ions that are dissolved in the water will cause charge
to ﬂow between the capacitor plates, so the capacitor discharges.

K,

K

Table 24.1 Values of Dielectric Constant K at 20 C

°

Material

Vacuum

Air (1 atm)

Air (100 atm)

Teﬂon

Polyethylene

Benzene

Mica

Mylar

K

1

1.00059

1.0548

2.1

2.25

2.28

3–6

3.1

Material

Polyvinyl chloride

Plexiglas®

Glass

Neoprene

Germanium

Glycerin

Water

Strontium titanate

K

3.18

3.40

5–10

6.70

16

42.5

80.4

310

No real dielectric is a perfect insulator. Hence there is always some leakage
current between  the  charged  plates  of  a  capacitor  with  a  dielectric.  We  tacitly
ignored this effect in Section 24.2 when we derived expressions for the equiva-
lent capacitances of capacitors in series, Eq. (24.5), and in parallel, Eq. (24.7).
But if a leakage current ﬂows for a long enough time to substantially change the
charges from the values we used to derive Eqs. (24.5) and (24.7), those equations
may no longer be accurate.

Induced Charge and Polarization
When a dielectric material is inserted between the plates while the charge is kept
K.
constant,  the  potential  difference  between  the  plates  decreases  by  a  factor
Therefore the electric ﬁeld between the plates must decrease by the same factor.
If

is the value with the dielectric, then

is the vacuum value and

E

E0

E =

E0
K

    1when Q is constant2

(24.14)

Since  the  electric-ﬁeld  magnitude  is  smaller  when  the  dielectric  is  present,  the
surface charge density (which causes the ﬁeld) must be smaller as well. The sur-
face charge on the conducting plates does not change, but an induced charge of
the  opposite  sign  appears  on  each  surface  of  the  dielectric  (Fig.  24.15).  The
dielectric was originally electrically neutral and is still neutral; the induced sur-
face  charges  arise  as  a  result  of  redistribution of  positive  and  negative  charge
within  the  dielectric  material,  a  phenomenon  called  polarization. We  ﬁrst
encountered polarization in Section 21.2, and we suggest that you reread the dis-
cussion of Fig. 21.8. We will assume that the induced surface charge is directly
proportional to the electric-ﬁeld magnitude
in the material; this is indeed the
case  for  many  common  dielectrics.  (This  direct  proportionality  is  analogous  to

E

24.4 Dielectrics

801

24.14 Effect of a dielectric between the
plates of a parallel-plate capacitor. (a) With
a given charge, the potential difference is
V0.
(b) With the same charge but with a
dielectric between the plates, the potential
is smaller than V0.
difference

V

(a)

Vacuum

Q

2Q

V0

Electrometer
(measures potential
difference across
plates)

+ –

(b)

Dielectric

Q

2Q

V

+ –

Adding the dielectric
reduces the potential
difference across the
capacitor.

24.15 Electric ﬁeld lines with
(a) vacuum between the plates and
(b) dielectric between the plates.

(a)
s

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
s

Vacuum

(b)

Dielectric

S
E0

2s

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

2s

s

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
s

2s

i

s

i

–

–

–

–

–

–

S
E

Induced
charges

+

+

+

+

+

+

–
2s
i

s

+
i

2s

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
2s

For a given charge density s, the induced
charges on the dielectric’s surfaces reduce the
electric field between the plates.

802

CHAPTER 24 Capacitance and Dielectrics

K
Hooke’s law for a spring.) In that case,
is a constant for any particular material.
When the electric ﬁeld is very strong or if the dielectric is made of certain crys-
talline  materials,  the  relationship  between  induced  charge  and  the  electric  ﬁeld
can be more complex; we won’t consider such cases here.

We  can  derive  a  relationship  between  this  induced  surface  charge  and  the
charge  on  the  plates.  Let’s  denote  the  magnitude  of  the  charge  per  unit  area
induced on the surfaces of the dielectric (the induced surface charge density) by
si.
The magnitude of the surface charge density on the capacitor plates is
as
usual. Then the net surface charge on each side of the capacitor has magnitude
1s - si2,
as  shown  in  Fig.  24.15b.  As  we  found  in  Example  21.12  (Section
21.5) and in Example 22.8 (Section 22.4), the ﬁeld between the plates is related
to the net surface charge density by
Without and with the dielectric,
respectively, we have

E = snet>P0.

s,

E0 =

    E =

s
P0

s - si
P0

(24.15)

Using these expressions in Eq. (24.14) and rearranging the result, we ﬁnd

si = sa1 - 1
K

b    (induced surface charge density)

(24.16)

This equation shows that when
case,
nearly cancels
than their values in vacuum.

si

s,

K

is very large,

In this
and the ﬁeld and potential difference are much smaller

is nearly as large as

si

s.

The product

is called the permittivity of the dielectric, denoted by

KP0

P =KP 0    1definition of permittivity2

In terms of  we can express the electric ﬁeld within the dielectric as

P

E =

s
P

P:

(24.17)

(24.18)

The capacitance when the dielectric is present is given by

C = KC0 = KP0

A
d

= P A
d

(parallel-plate capacitor,
dielectric between plates)

(24.19)

u
We can repeat the derivation of Eq. (24.11) for the energy density

in an elec-

tric ﬁeld for the case in which a dielectric is present. The result is

u = 1

2 KP0E 2 = 1

2

PE 2    (electric energy density in a dielectric)

(24.20)

K = 1,

P = P0

In empty space, where

and Eqs. (24.19) and (24.20) reduce to
Eqs. (24.2) and (24.11), respectively, for a parallel-plate capacitor in vacuum. For
P0
this reason,
is sometimes called the “permittivity of free space” or the “permit-
tivity of vacuum.” Because
have the same units,
C2>N # m2

is a pure number,

F>m.

and

P0

or

K

P

Equation (24.19) shows that extremely high capacitances can be obtained with
A
and are separated by a small distance  by
plates that have a large surface area
In an electrolytic double-layer capacitor, tiny
a dielectric with a large value of
carbon granules adhere to each plate: The value of
is the combined surface area
of the granules, which can be tremendous. The plates with granules attached are
separated  by  a  very  thin  dielectric  sheet.  A capacitor  of  this  kind  can  have  a
capacitance of 5000 farads yet ﬁt in the palm of your hand (compare Example
24.1 in Section 24.1).

K.

A

d

Several practical devices make use of the way in which a capacitor responds
to a change in dielectric constant. One example is an electric stud ﬁnder, used by

home repair workers to locate metal studs hidden behind a wall’s surface. It con-
sists  of  a  metal  plate  with  associated  circuitry.  The  plate  acts  as  one  half  of  a
capacitor, with the wall acting as the other half. If the stud ﬁnder moves over a
metal stud, the effective dielectric constant for the capacitor changes, changing
the capacitance and triggering a signal.

24.4 Dielectrics

803

Problem-Solving Strategy 24.2

Dielectrics

IDENTIFY the relevant concepts: The relationships in this section
are useful whenever there is an electric ﬁeld in a dielectric, such as
a dielectric between charged capacitor plates. Typically you must
Vab
between the plates, the electric
relate the potential difference
s
on  the
ﬁeld  magnitude  E in  the  capacitor,  the  charge  density
on the surfaces
capacitor plates, and the induced charge density
of the capacitor.

si

SET UP the problem using the following steps:
1. Make a drawing of the situation.
2. Identify the target variables, and choose which equations from

this section will help you solve for those variables.

EXECUTE the solution as follows:
1. In problems such as the next example, it is easy to get lost in a
blizzard  of  formulas. Ask  yourself  at  each  step  what  kind  of

quantity  each  symbol  represents.  For  example,  distinguish
clearly  between  charges  and  charge  densities,  and  between
electric ﬁelds and electric potential differences.

2. Check for consistency of units. Distances must be in meters. A
farad, and so on. Don’t confuse the numeri-
Electric-ﬁeld magni-
P0

10-6
microfarad is
P0
cal value of  with the value of
tude  can  be  expressed  in  both
C2>N # m2
or
are

1>4pP0.
N>C and V>m.

The  units  of

F>m.

EVALUATE your answer: With a dielectric present, (a) the capaci-
tance is greater than without a dielectric; (b) for a given charge on
the  capacitor,  the  electric  ﬁeld  and  potential  difference  are  less
than without a dielectric; and (c) the magnitude of the induced sur-
face  charge  density
on  the  dielectric  is  less  than  that  of  the
charge density

on the capacitor plates.

si

s

Example 24.10

A capacitor with and without a dielectric

(

(

1.00 cm

V0 = 3.00 kV,

2.00 * 10-1 m2

Suppose  the  parallel  plates  in  Fig.  24.15 each  have  an  area  of
1.00 * 10-2 m
2000 cm2
)
)  and  are
apart. We connect the capacitor to a power supply, charge it to a
potential difference
and disconnect the power sup-
ply. We then insert a sheet of insulating plastic material between
the plates, completely ﬁlling the space between them. We ﬁnd that
the potential difference decreases to 1.00 kV while the charge on
each capacitor plate remains constant. Find (a) the original capaci-
tance
on  each  plate;  (c)  the
capacitance
after the dielectric is inserted; (d) the dielectric con-
stant  of the dielectric; (e) the permittivity  of the dielectric; (f )
K
on each face of the dielectric;
the magnitude of the induced charge
Qi
between  the  plates;  and  (h)  the
(g)  the  original  electric  ﬁeld
electric ﬁeld  after the dielectric is inserted.
E

(b)  the  magnitude  of  charge

C0;

E0

Q

C

P

SOLUTION

IDENTIFY and SET UP: This problem uses most of the relationships
we have discussed for capacitors and dielectrics. (Energy relation-
ships  are  treated  in  Example  24.11.)  Most  of  the  target  variables
can  be  obtained  in  several  ways.  The  methods  used  below  are  a
sample;  we  encourage  you  to  think  of  others  and  compare  your
results.

EXECUTE: (a) With vacuum between the plates, we use Eq. (24.19)
with

K = 1:

C0 = P0

A
d

= 18.85 * 10-12 F>m2 2.00 * 10-1 m2
1.00 * 10-2 m

= 1.77 * 10-10 F = 177 pF

(b) From the deﬁnition of capacitance, Eq. (24.1),

Q = C0V0 = 11.77 * 10-10 F213.00 * 103 V2

= 5.31 * 10-7 C = 0.531 mC

(c)  When  the  dielectric  is  inserted,  Q is  unchanged  but  the
Hence  from  Eq.

V = 1.00 kV.

potential  difference  decreases  to
(24.1), the new capacitance is
= 5.31 * 10-7 C
1.00 * 103 V

C =

Q
V

= 5.31 * 10-10 F = 531 pF

(d) From Eq. (24.12), the dielectric constant is
= 5.31 * 10-10 F
1.77 * 10-10 F

K = C
C0

531 pF
177 pF

=

= 3.00

Alternatively, from Eq. (24.13),

K =

V0
V

= 3000 V
1000 V

= 3.00

(e) Using

K

from part (d) in Eq. (24.17), the permittivity is

P =KP 0 = 13.00218.85 * 10-12 C2>N # m22
= 2.66 * 10-11 C2>N # m2

(f )  Multiplying  both  sides  of  Eq.  (24.16) by  the  plate  area  A
Q = sA

in terms of the charge

Qi = siA

gives the induced charge
on each plate:

Qi = Q a1 - 1
K

b = 15.31 * 10-7 C2a1 - 1
3.00

b

= 3.54 * 10-7 C

Continued

804

CHAPTER 24 Capacitance and Dielectrics

(g)  Since  the  electric  ﬁeld  between  the  plates  is  uniform,  its
magnitude is the potential difference divided by the plate separa-
tion:

=

V0
d

E0 =

3000 V
1.00 * 10-2 m
(h) After the dielectric is inserted,

= 3.00 * 105 V>m

E = V
d

=

1000 V
1.00 * 10-2 m

= 1.00 * 105 V>m

or, from Eq. (24.18),

E =

s
P

=

Q
PA

=

5.31 * 10-7 C
12.66 * 10-11 C2>N # m2212.00 * 10-1 m22

= 1.00 * 105 V>m

or, from Eq. (24.15),

E =

s - si
P0

=

Q - Qi
P0A

=

15.31 - 3.542 * 10-7 C
18.85 * 10-12 C2>N # m2212.00 * 10-1 m22

= 1.00 * 105 V>m

or, from Eq. (24.14),

E =

E0
K

=

3.00 * 105 V>m
3.00

= 1.00 * 105 V>m

K = 3.00

EVALUATE:  Inserting the dielectric increased the capacitance by a
and  reduced  the  electric  ﬁeld  between  the
factor  of
plates  by  a  factor  of
It  did  so  by  developing
induced  charges  on  the  faces  of  the  dielectric  of  magnitude
Q11 - 1>K2

Q11 - 1>3.002

1>K = 1>3.00.

= 0.667Q.

=

Example 24.11

Energy storage with and without a dielectric

Find  the  energy  stored  in  the  electric  ﬁeld  of  the  capacitor  in
Example  24.10  and  the  energy  density,  both  before  and  after  the
dielectric sheet is inserted.

Since the electric ﬁeld between the plates is uniform,
is  uniform  as  well  and  the  energy  density  is  just  the  stored

0.00200 m3.
u0
energy divided by the volume:

SOLUTION

IDENTIFY and SET UP: We now consider the ideas of energy stored
in  a  capacitor  and  of  electric-ﬁeld  energy  density.  We  use  Eq.
(24.9) to ﬁnd the stored energy and Eq. (24.20) to ﬁnd the energy
density.

EXECUTE: From Eq. (24.9), the stored energies
and with the dielectric in place are

U0

and  without

U

U0 = 1
U = 1

0 = 1
2 C0V 2
2 CV 2 = 1

2

11.77 * 10-10 F213000 V22 = 7.97 * 10-4 J
2
15.31 * 10-10 F211000 V22 = 2.66 * 10-4 J

The ﬁnal energy is one-third of the original energy.

Equation  (24.20) gives  the  energy  densities  without  and  with

the dielectric:

u0 = 1

2

P0 E 2

0 = 1

2

18.85 * 10-12 C2>N # m2213.00 * 105 N>C22

= 0.398 J>m3

u = 1
2

PE 2 = 1
2

12.66 * 10-11 C2>N # m2211.00 * 105 N>C22

= 0.133 J>m3

The energy density with the dielectric is one-third of the original
energy density.

EVALUATE: We  can  check  our  answer  for
by  noting  that  the
volume  between  the  plates  is  V = 10.200 m2210.0100 m2 =

u0

U0
V

u0 =

= 7.97 * 10-4 J
0.00200 m3
This  agrees  with  our  earlier  answer.  You  can  use  the  same
approach to check our result for u.

= 0.398 J>m3

K

PE 2

In general, when a dielectric is inserted into a capacitor while
P
the  charge  on  each  plate  remains  the  same,  the  permittivity
(the dielectric constant), and the electric
increases by a factor of
u = 1
decrease  by  a  factor  of
ﬁeld E and  the  energy  density
2
1>K.
Where  does  the  energy  go? The  answer  lies  in  the  fringing
ﬁeld  at  the  edges  of  a  real  parallel-plate  capacitor. As  Fig.  24.16
shows, that ﬁeld tends to pull the dielectric into the space between
the plates, doing work on it as it does so. We could attach a spring
to the left end of the dielectric in Fig. 24.16 and use this force to
stretch  the  spring.  Because  work  is  done  by  the  ﬁeld,  the  ﬁeld
energy density decreases.

24.16 The fringing ﬁeld at the edges of the capacitor exerts forces
S
F
of a dielectric, pulling the dielectric into the capacitor.

on the negative and positive induced surface charges

and

S
F

+i

-i

S
F2i

+ + + + + + + + + + + + + +

Dielectric

S
E

–

– – – – – – – – – – – – –

S
F1i

Dielectric Breakdown
We mentioned earlier that when a dielectric is subjected to a sufﬁciently strong
electric ﬁeld, dielectric breakdown takes place and the dielectric becomes a con-
ductor. This occurs when the electric ﬁeld is so strong that electrons are ripped
loose from their molecules and crash into other molecules, liberating even more
