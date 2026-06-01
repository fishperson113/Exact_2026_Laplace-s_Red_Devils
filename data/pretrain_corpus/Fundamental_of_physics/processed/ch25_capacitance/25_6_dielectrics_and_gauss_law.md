25-6 DI E LECTR ICS  AN D  GAUSS’  L AW

735

25-6 DIELECTRICS AND GAUSS’ LAW

Learning Objectives
After reading this module, you should be able to . . .

25.28 In a capacitor with a dielectric, distinguish free charge

from induced charge.

25.29 When a dielectric partially or fully fills the space in a

capacitor, find the free charge, the induced charge, the elec-
tric field between the plates (if there is a gap, there is more
than one field value), and the potential between the plates.

Key Ideas
● Inserting a dielectric into a capacitor causes induced
charge to appear on the faces of the dielectric and weakens
the electric field between the plates.

● The induced charge is less than the free charge on the
plates.

● When a dielectric is present, Gauss’ law may be

generalized to

´0, kE

:

:
" dA

! q,

where q is the free charge. Any induced surface charge is
accounted for by including the dielectric constant k inside
the integral.

Dielectrics and Gauss’ Law
In  our  discussion  of  Gauss’  law  in  Chapter  23, we  assumed  that  the  charges
existed in a vacuum. Here we shall see how to modify and generalize that law if
dielectric materials, such as those listed in Table 25-1, are present. Figure 25-16
shows  a  parallel-plate  capacitor  of  plate  area  A, both  with  and  without  a
dielectric. We assume that the charge q on the plates is the same in both situa-
tions. Note that the field between the plates induces charges on the faces of the
dielectric by one of the methods described in Module 25-5.

For the situation of Fig. 25-16a, without a dielectric, we can find the electric
:
between the plates as we did in Fig. 25-5: We enclose the charge %q on
E
field
0
the top plate with a Gaussian surface and then apply Gauss’ law. Letting E0 rep-
resent the magnitude of the field, we find

or

´0, E

:

:
" dA

! ´0EA ! q,

E0 !

q
´0A

.

(25-30)

(25-31)

In  Fig. 25-16b, with  the  dielectric  in  place, we  can  find  the  electric  field
between the plates (and within the dielectric) by using the same Gaussian sur-
face. However, now  the  surface  encloses  two  types  of  charge: It  still  encloses
charge %q on the top plate, but it now also encloses the induced charge #q- on
the top face of the dielectric. The charge on the conducting plate is said to be free
charge because it can move if we change the electric potential of the plate; the
induced  charge  on  the  surface  of  the  dielectric  is  not  free  charge  because  it
cannot move from that surface.

Gaussian surface

Gaussian surface

+q

+

+ + + + + + + +

+

E0

+q

–q

–

– – – – – – – –

–

(a)

+
+
+ + + + + + + +
–
–
–

–

–

E

κ

+
–

+

+
– – – – – – – –

+

+
–

–q'

+q'

–q

(b)

Figure 25-16 A parallel-plate capacitor (a) without and (b) with a dielectric slab inserted.
The charge q on the plates is assumed to be the same in both cases.

736

CHAPTE R  25 CAPACITANCE

The net charge enclosed by the Gaussian surface in Fig. 25-16b is q # q-, so

Gauss’ law now gives

or

´0, E

:

:
" dA

! ´0EA ! q # q-,

E !

q # q-
´0A

.

(25-32)

(25-33)

The effect of the dielectric is to weaken the original field E0 by a factor of k; so we
may write

E !

E0
k

!

q
k´0 A

.

Comparison of Eqs. 25-33 and 25-34 shows that

q # q- !

q
k

.

(25-34)

(25-35)

Equation  25-35  shows  correctly  that  the  magnitude  q- of  the  induced  surface
charge is less than that of the free charge q and is zero if no dielectric is present
(because then k ! 1 in Eq. 25-35).

By substituting for q # q- from Eq. 25-35 in Eq. 25-32, we can write Gauss’

law in the form

´0, kE

:

:
" dA

! q

(Gauss’ law with dielectric).

(25-36)

This  equation, although  derived  for  a  parallel-plate  capacitor, is  true  generally
and is the most general form in which Gauss’ law can be written. Note:

1. The flux integral now involves
called the electric displacement
:
- D

:
" dA

! q.)

not just

:
kE
is sometimes
,
:
D
so that Eq. 25-36 can be written in the form
,

(The vector

:
´0kE

:
E
.

2. The  charge  q enclosed  by  the  Gaussian  surface  is  now  taken  to  be  the  free
charge only. The  induced  surface  charge  is  deliberately  ignored  on  the  right
side  of  Eq. 25-36, having  been  taken  fully  into  account  by  introducing  the
dielectric constant k on the left side.

3. Equation  25-36  differs  from  Eq. 23-7, our  original  statement  of  Gauss’  law,
only  in  that  +0 in  the  latter  equation  has  been  replaced  by  k+0. We  keep  k
inside the integral of Eq. 25-36 to allow for cases in which k is not constant
over the entire Gaussian surface.

Sample Problem 25.06 Dielectric partially filling the gap in a capacitor

Figure  25-17  shows  a  parallel-plate  capacitor  of  plate  area
A and  plate  separation  d. A  potential  difference  V0 is  ap-
plied  between  the  plates  by  connecting  a  battery  between
them. The battery is then disconnected, and a dielectric slab
of  thickness  b and  dielectric  constant  k is  placed  between
the  plates  as  shown. Assume  A ! 115 cm2, d ! 1.24 cm,
V0 ! 85.5 V, b ! 0.780 cm, and k ! 2.61.
(a) What is the capacitance C0 before the dielectric slab is
inserted?

Gaussian
surface I

+  +  +  +  +  +  +  +

–q'

+q'

–

+

–

+

κ

–

+

–

+

Gaussian
surface II

–  –  –  –  –  –  –  –

+q

–q

b

d

Figure 25-17 A parallel-plate capacitor containing a dielectric slab
that only partially fills the space between the plates.

Calculation: From Eq. 25-9 we have

KEY IDEA

25-6 DI E LECTR ICS  AN D  GAUSS’  L AW

737

C0 !

+0 A
d

!

(8.85 $ 10#12 F/m)(115 $ 10#4 m2)
1.24 $ 10#2 m

! 8.21 $ 10#12  F ! 8.21 pF.

(Answer)

(b) What free charge appears on the plates?

Calculation: From Eq. 25-1,

q ! C0V0 ! (8.21 $ 10#12 F)(85.5 V)

! 7.02 $ 10#10 C ! 702 pC.

(Answer)

Because  the  battery  was  disconnected  before  the  slab  was
inserted, the free charge is unchanged.

(c)  What  is  the  electric  field  E0 in  the  gaps  between  the
plates and the dielectric slab?

KEY IDEA

We  need  to  apply  Gauss’  law, in  the  form  of  Eq. 25-36, to
Gaussian surface I in Fig. 25-17.

Calculations: That  surface  passes  through  the  gap, and  so  it
encloses only the  free  charge  on  the  upper  capacitor  plate.
Electric field pierces only the bottom of the Gaussian surface.
Because there the area vector
are
both directed downward, the dot product in Eq. 25-36 becomes

and the field vector

:
dA

:
E
0

:
:
0 " dA
E

! E0 dA cos 0/ ! E0 dA.

Equation 25-36 then becomes

´0kE0, dA ! q.

The integration now simply gives the surface area A of the
plate. Thus, we obtain

or

´0kE0A ! q,

E0 !

q
´0kA

.

We  must  put  k ! 1  here  because  Gaussian  surface  I  does
not pass through the dielectric. Thus, we have

E0 !

q
´0kA

!

7.02 $ 10#10 C
(8.85 $ 10#12 F/m)(1)(115 $ 10#4 m2)

Now  we  apply  Gauss’  law  in  the  form  of    Eq. 25-36  to
Gaussian surface II in Fig. 25-17.

Calculations: Only the free charge #q is in Eq. 25-36, so

´0, kE

:
:
1 " dA

! #´0kE1A ! #q.

(25-37)

:
E

The  first  minus  sign  in  this  equation  comes  from  the  dot
:
1 " dA
along  the  top  of  the  Gaussian  surface  be-
product
cause now the field vector
is directed downward and the
:
dA
area vector
(which, as always, points outward from the
interior  of  a  closed  Gaussian  surface)  is  directed  upward.
With 180/ between the vectors, the dot product is negative.
Now k ! 2.61. Thus, Eq. 25-37 gives us

:
E
1

E1 !

!

q
´0kA
! 2.64 kV/m.

E0
k

!

6.90 kV/m
2.61

(Answer)

(e) What  is  the  potential  difference  V between  the  plates
after the slab has been introduced?

KEY IDEA

We find V by integrating along a straight line directly from
the bottom plate to the top plate.

Calculation: Within the dielectric, the path length is b and
the electric field is E1. Within the two gaps above and below
the dielectric, the total path length is d # b and the electric
field is E0. Equation 25-6 then yields

V ! "%

#

E ds ! E0(d # b) % E1b

! (6900 V/m)(0.0124 m # 0.00780 m)

% (2640 V/m)(0.00780 m)

! 52.3 V.

(Answer)

This is less than the original potential difference of 85.5 V.

(f) What is the capacitance with the slab in place?

KEY IDEA

The capacitance C is related to q and V via Eq. 25-1.

! 6900 V/m ! 6.90 kV/m.

(Answer)

Calculation: Taking q from (b) and V from (e), we have

Note that the value of E0 does not change when the slab is
introduced  because  the  amount  of  charge  enclosed  by
Gaussian surface I in Fig. 25-17 does not change.

C !

q
V

!

7.02 $ 10#10 C
52.3 V

! 1.34 $ 10#11 F ! 13.4 pF.

(Answer)

(d) What is the electric field E1 in the dielectric slab?

This is greater than the original capacitance of 8.21 pF.

Additional examples, video, and practice available at WileyPLUS

738

CHAPTE R  25 CAPACITANCE

Review & Summary

Capacitor; Capacitance A capacitor consists of two isolated
conductors (the plates) with charges %q and #q. Its capacitance C
is defined from

Equivalent capacitances can be used to calculate the capacitances
of more complicated series – parallel combinations.

where V is the potential difference between the plates.

q ! CV,

(25-1)

Potential Energy and Energy Density The electric poten-
tial energy U of a charged capacitor,

Determining  Capacitance We  generally  determine
the
capacitance of a particular capacitor configuration by (1) assuming a
charge q to have been placed on the plates, (2) finding the electric field
:
due to this charge, (3) evaluating the potential difference V, and (4)
E
calculating C from Eq. 25-1. Some specific results are the following:

A parallel-plate  capacitor with  flat  parallel  plates  of  area  A

and spacing d has capacitance

U !

q2
2C

! 1

2 CV2,

(25-21, 25-22)

is equal to the work required to charge the capacitor. This energy
can be associated with the capacitor’s electric field  By extension
we can associate stored energy with any electric field. In vacuum,
the energy density u, or potential energy per unit volume, within an
electric field of magnitude E is given by

:
E
.

C !

´0A
d

.

(25-9)

u ! 1

2´0 E2.

(25-25)

A cylindrical capacitor (two long coaxial cylinders) of length

L and radii a and b has capacitance

L
ln(b/a)
A spherical capacitor with concentric spherical plates of radii

C ! 2p´0

(25-14)

.

a and b has capacitance

C ! 4p´0

ab
b # a

.

An isolated sphere of radius R has capacitance

C ! 4p´0R.

(25-17)

(25-18)

Capacitors  in  Parallel  and  in  Series The  equivalent
capacitances Ceq of  combinations  of  individual  capacitors  con-
nected in parallel and in series can be found from

n

Ceq ! ’
1
Ceq

! ’

j!1
n

j!1

Cj

(n capacitors in parallel)

1
Cj

(n capacitors in series).

and

Questions

q

1 Figure  25-18  shows  plots  of
charge  versus  potential  difference
for  three  parallel-plate  capacitors
that have the plate areas and sepa-
rations  given  in  the  table. Which
plot goes with which capacitor?

Figure 25-18 Question 1.

Capacitor

Area

Separation

1
2
3

A
2A
A

d
d
2d

2 What is Ceq of three capacitors, each of capacitance C, if they
are connected to a battery (a) in series with one another and (b) in
parallel?  (c)  In  which  arrangement  is  there  more  charge  on  the
equivalent capacitance?

(25-19)

(25-20)

a

b
c

V

Capacitance  with  a  Dielectric If  the  space  between  the
plates of a capacitor is completely filled with a dielectric material,
the  capacitance  C is  increased  by  a  factor  k, called  the  dielectric
constant, which  is  characteristic  of  the  material. In  a  region  that
is completely filled by a dielectric, all electrostatic equations con-
taining +0 must be modified by replacing +0 with k+0.

The effects of adding a dielectric can be understood physically
in  terms  of  the  action  of  an  electric  field  on  the  permanent  or
induced electric dipoles in the dielectric slab. The result is the for-
mation of induced charges on the surfaces of the dielectric, which
results in a weakening of the field within the dielectric for a given
amount of free charge on the plates.

Gauss’ Law with a Dielectric When a dielectric is present,
Gauss’ law may be generalized to

´0, kE

:

:
" dA

! q.

(25-36)

Here q is the free charge; any induced surface charge is accounted
for by including the dielectric constant k inside the integral.

3 (a) In Fig. 25-19a, are capacitors 1 and 3 in series? (b) In the same

+
–

C1

C3

C2

(a)

(b)

C3

+
–

C2

C1

C1

(c)

C3

+
–

C2

+
–

C1

C3

(d)

C2

Figure 25-19 Question 3.

figure, are  capacitors  1  and  2  in  parallel?  (c)  Rank  the  equivalent
capacitances of the four circuits shown in Fig. 25-19, greatest first.

4 Figure  25-20  shows  three  circuits, each  consisting  of  a  switch
and  two  capacitors,
initially  charged  as  indicated  (top  plate
positive). After  the  switches  have  been  closed, in  which  circuit
(if any)  will  the  charge  on  the  left-hand  capacitor  (a) increase,
(b) decrease, and (c) remain the same?

6q

2C

3q

C

6q

3C

3q

C

6q

2C

3q

2C

(1)

(2)

(3)

Figure 25-20 Question 4.

5 Initially, a single capacitance C1 is wired to a battery. Then ca-
pacitance C2 is added in parallel. Are (a) the potential difference
across C1 and (b) the charge q1 on C1 now more than, less than, or
the same as previously? (c) Is the equivalent capacitance C12 of C1
and C2 more than, less than, or equal to C1? (d) Is the charge stored
on C1 and C2 together more than, less than, or equal to the charge
stored previously on C1?
6 Repeat Question 5 for C2 added in series rather than in parallel.

7 For  each  circuit  in  Fig. 25-21, are  the  capacitors  connected  in
series, in parallel, or in neither mode?

+–

+–

+
–

(a)

(b)

(c)

Figure 25-21 Question 7.

PROB LE M S

739

C

A

C

C

8 Figure  25-22  shows  an  open
switch, a  battery  of  potential  differ-
ence V, a  current-measuring  meter
A, and  three  identical  uncharged
capacitors  of  capacitance  C. When
the  switch  is  closed  and  the  circuit
reaches equilibrium, what are (a) the
potential difference across each capacitor and (b) the charge on
the  left  plate  of  each  capacitor?  (c)  During  charging, what  net
charge passes through the meter?

Figure 25-22 Question 8.

+  –
V

9 A  parallel-plate  capacitor  is  connected  to  a  battery  of  elec-
tric potential difference V. If the plate separation is decreased,
do  the  following  quantities  increase, decrease, or  remain  the
same: (a) the capacitor’s capacitance, (b) the potential difference
across the capacitor, (c) the charge on the capacitor, (d) the en-
ergy  stored  by  the  capacitor, (e)  the  magnitude  of  the  electric
field between the plates, and (f ) the energy density of that elec-
tric field?

10 When  a  dielectric  slab  is  inserted
between  the  plates  of  one  of  the  two
identical  capacitors  in  Fig. 25-23, do  the
following properties of that capacitor in-
crease, decrease, or  remain  the  same:
(a) capacitance, (b)  charge, (c)  potential
difference, and  (d)  potential  energy?
(e) How about the same properties of the
other capacitor?

C

C

κ

+
–

B

Figure 25-23
Question 10.

11 You are to connect capacitances C1 and C2, with C1 ( C2, to
a  battery, first  individually, then  in  series, and  then  in  parallel.
Rank  those  arrangements  according  to  the  amount  of  charge
stored, greatest first.

Problems

Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign

SSM Worked-out solution available in Student Solutions Manual
• – ••• Number of dots indicates level of problem difficulty

WWW Worked-out solution is at

ILW Interactive solution is at

http://www.wiley.com/college/halliday

Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com

Module 25-1 Capacitance
•1 The  two  metal  objects  in  Fig. 25-24  have  net  charges of
%70 pC  and  #70 pC, which  result  in  a  20 V  potential  difference
between them. (a) What is the capacitance of the system? (b) If the
charges are changed to %200 pC and #200 pC, what does the capac-
itance become? (c) What does the potential difference become?

Figure 25-24 Problem 1.

•2 The capacitor in Fig. 25-25 has a
capacitance of 25 mF and is initially
uncharged. The  battery  provides  a
potential  difference  of  120 V. After
switch S is closed, how much charge
will pass through it?

+
–

S

C

Figure 25-25 Problem 2.

SSM

Module 25-2 Calculating the Capacitance
A  parallel-plate  capacitor  has  circular  plates  of  8.20 cm
•3
radius  and  1.30 mm  separation. (a)  Calculate  the  capacitance.
(b) Find the charge for a potential difference of 120 V.

•4 The  plates  of  a  spherical  capacitor  have  radii  38.0 mm  and
40.0 mm. (a) Calculate the capacitance. (b) What must be the plate
area  of  a  parallel-plate  capacitor  with  the  same  plate  separation
and capacitance?

•5 What  is  the  capacitance  of  a  drop  that  results  when  two
mercury spheres, each of radius R ! 2.00 mm, merge?

•6 You  have  two  flat  metal  plates, each  of  area  1.00 m2, with
which  to  construct  a  parallel-plate  capacitor. (a)  If  the  capac-
itance of the device is to be 1.00 F, what must be the separation
between  the  plates?  (b)  Could  this  capacitor  actually  be
constructed?

•7 If  an  uncharged  parallel-plate  capacitor  (capacitance  C)  is
connected to a battery, one plate becomes negatively charged as

740

CHAPTE R  25 CAPACITANCE

electrons  move  to  the  plate  face  (area
A). In Fig. 25-26, the depth d from which
the electrons come in the plate in a par-
ticular  capacitor  is  plotted  against  a
range  of  values  for  the  potential  differ-
ence V of the battery. The density of con-
duction electrons in the copper plates is
8.49 $ 10 28 electrons/m3. The  vertical
scale is set by ds ! 1.00 pm, and the hori-
zontal scale is set by Vs ! 20.0 V. What is
the ratio C/A?

d (pm)

ds

0

Vs
V (V)

Figure 25-26 Problem 7.

Module 25-3 Capacitors in Parallel and in Series
•8 How many 1.00 mF capacitors must be connected in parallel to
store  a  charge  of  1.00 C  with  a  potential  of  110 V  across  the
capacitors?

capacitor  drops  to  35 V, what  is  the  capacitance  of  this  second
capacitor?

In Fig. 25-30, the battery has
••14
a  potential  difference  of  V 10.0 V
and  the  five  capacitors  each  have  a
capacitance  of  10.0 mF. What
is
the charge  on  (a)  capacitor  1  and
(b) capacitor 2?

!

C2

C1

+
–

V

Figure 25-30 Problem 14.

In Fig. 25-31, a 20.0 V bat-
••15
tery  is  connected  across  capacitors
of  capacitances  C1 ! C6 ! 3.00 mF
and C3 ! C5 ! 2.00C2 ! 2.00C4 ! 4.00 mF. What are (a) the equiv-
alent capacitance Ceq of the capacitors and (b) the charge stored by
Ceq? What are (c) V1 and (d) q1 of capacitor 1, (e) V2 and (f) q2 of
capacitor 2, and (g) V3 and (h) q3 of capacitor 3?

•9 Each of the uncharged capaci-
tors in Fig. 25-27 has a capacitance
of  25.0 mF. A  potential  difference
of V ! 4200 V is established when
the  switch  is  closed. How  many
coulombs  of  charge  then  pass
through meter A?

A

C

C

C

V

•10 In Fig. 25-28, find the equiva-
lent capacitance of the combination. Assume that C1 is 10.0 mF, C2
is 5.00 mF, and C3 is 4.00 mF.

Figure 25-27 Problem 9.

V

C1

C2

C3

Figure 25-28 Problems 10 and 34.

ILW

•11
combination. Assume  that  C1
4.00 mF.

In  Fig. 25-29, find  the  equivalent  capacitance  of  the
10.0 mF, C2
!

5.00 mF, and  C3

!

!

C2

V

C1

C3

Figure 25-29 Problems 11, 17, and 38.

••12 Two parallel-plate capacitors, 6.0 mF each, are connected in
parallel to a 10 V battery. One of the capacitors is then squeezed so
that its plate separation is 50.0% of its initial value. Because of the
squeezing, (a) how much additional charge is transferred to the ca-
pacitors  by  the  battery  and  (b)  what  is  the  increase  in  the  total
charge stored on the capacitors?

ILW

SSM

A 100 pF capacitor is charged to a potential dif-
••13
ference  of  50 V, and  the  charging  battery  is  disconnected. The
capacitor  is  then  connected  in  parallel  with  a  second  (initially
uncharged)  capacitor. If  the  potential  difference  across  the  first

C4

C2

C5

C3

V

+
–

C6

C1

Figure 25-31 Problem 15.

••16 Plot 1 in Fig. 25-32a gives the charge q that can be stored
on capacitor 1 versus the electric potential V set up across it. The
vertical scale is set by qs ! 16.0 mC, and the horizontal scale is set
by Vs ! 2.0 V. Plots 2 and 3 are similar plots for capacitors 2 and
3, respectively. Figure  25-32b shows  a  circuit  with  those  three
capacitors  and  a  6.0 V  battery. What  is  the  charge  stored  on
capacitor 2 in that circuit?

)
C
µ
(

q

qs

0

C 1

V

C 2

C 3

1

2

3

Vs

V (V)

(a)

(b)

Figure 25-32 Problem 16.

!

5.00 mF, and C3

In Fig. 25-29, a potential difference of  V 100.0 V is ap-
••17
10.0 mF,
plied across a capacitor arrangement with capacitances C1
4.00 mF. If capacitor 3 undergoes electrical
C2
breakdown so that it becomes equivalent to conducting wire, what
is the increase in (a) the charge on capacitor 1 and (b) the potential
difference across capacitor 1?

!

!

!

••18 Figure 25-33 shows a circuit section of four air-filled capacitors
that is connected to a larger circuit.The graph below the section shows
the electric potential V(x) as a function of position x along the lower
part of the section, through capacitor 4. Similarly, the graph above the
section shows the electric potential V(x) as a function of position x
along the upper part of the section, through capacitors 1, 2, and 3.

Capacitor  3  has  a  capacitance  of  0.80 mF. What  are  the  capaci-
tances of (a) capacitor 1 and (b) capacitor 2?

V

2 V

5 V

1

2

3

4

x

x

12

)
V
(
V

Figure 25-33
Problem 18.

!

In Fig. 25-34, the battery has potential difference V 9.0
••19
4.0 mF, and all the capacitors are initially un-
3.0 mF, C4
V, C2
charged. When  switch  S  is  closed, a  total  charge  of  12 mC  passes
through point a and a total charge of 8.0 mC passes through point
b. What are (a) C1 and (b) C3?

!

!

S

C 1

C 2

a

C 3

b
C4

V

Figure 25-34 Problem 19.

••20 Figure  25-35  shows  a
variable “air gap” capacitor for
manual tuning. Alternate plates
are connected  together; one
group  of  plates  is  fixed  in  posi-
tion, and  the  other  group  is
capable  of  rotation. Consider  a
capacitor  of  n ! 8  plates  of  al-
ternating  polarity, each  plate
having  area  A ! 1.25 cm2 and
separated from adjacent plates by distance d ! 3.40 mm. What is the
maximum capacitance of the device?

Figure 25-35 Problem 20.

A

A

d

a

!

!

S1

SSM

WWW

+ + + +
– – – –

In Fig. 25-36, the
••21
1.0 mF  and
capacitances  are  C1
3.0 mF, and both capacitors are
C2
charged  to  a  potential  difference  of
V ! 100 V  but  with  opposite  polar-
ity as shown. Switches S1 and S2 are
now closed. (a) What is now the po-
tential difference between points a and b? What now is the charge
on capacitor (b) 1 and (c) 2?

Figure 25-36 Problem 21.

– – – –
+ + + +

C2

C1

S2

b

••22 In Fig. 25-37, V ! 10 V, C1 ! 10
mF, and  C2 ! C3 ! 20 mF. Switch  S  is
first thrown to the left side until capac-
itor  1  reaches  equilibrium. Then  the
switch  is  thrown  to  the  right. When
equilibrium  is  again  reached, how
much charge is on capacitor 1?

S

V

C1

C2

C3

Figure 25-37 Problem 22.

PROB LE M S

741

S

••23 The capacitors in Fig. 25-38 are ini-
tially  uncharged. The capacitances  are
C1 ! 4.0 mF, C2 ! 8.0 mF, and  C3 ! 12 mF,
and  the  battery’s  potential  difference  is
V ! 12 V. When  switch  S  is  closed, how
many electrons travel through (a) point a,
(b) point b, (c) point c, and (d) point d? In
the figure, do the electrons travel up or down through (e) point b and
(f) point c?

Figure 25-38 Problem 23.

a
C 1

C 3

C2

V

d

b

c

!

Figure 25-39 represents two air-filled cylindrical capacitors
••24
connected  in  series  across  a  battery  with  potential  V 10 V.
Capacitor 1 has an inner plate radius of 5.0 mm, an outer plate radius
of 1.5 cm, and a length of 5.0 cm. Capacitor 2 has an inner plate radius
of 2.5 mm, an outer plate radius of 1.0 cm, and a length of 9.0 cm.The
outer plate of capacitor 2 is a conducting
organic membrane that can be stretched,
and  the  capacitor  can  be  inflated  to  in-
crease  the  plate  separation. If the  outer
plate radius is increased to 2.5 cm by in-
flation, (a) how  many  electrons  move
through point P and (b) do they move to-
ward or away from the battery?

Figure 25-39 Problem 24.

C2

C1

V

P

In  Fig. 25-40, two  parallel-plate
••25
capacitors  (with  air  between  the  plates)
are  connected  to  a  battery. Capacitor  1
has a plate area of 1.5 cm2 and an electric
field  (between  its  plates)  of  magnitude
2000 V/m. Capacitor 2 has a plate area of
0.70 cm2 and an electric field of magnitude 1500 V/m. What is the
total charge on the two capacitors?

Figure 25-40
Problem 25.

C 1

C2

Capacitor  3  in  Fig. 25-41a is  a  variable  capacitor (its
•••26
capacitance C3 can be varied). Figure 25-41b gives the electric po-
tential V1 across capacitor 1 versus C3. The horizontal scale is set by
C3s =  12.0  mF. Electric  potential  V1 approaches  an  asymptote  of
10 V  as  C3 : ,. What  are  (a)  the  electric  potential V across  the
battery, (b) C1, and (c) C2?

)
V
(

1
V

10

8

6

4

2

0

V

C1

C 3

C2

(a)

Figure 25-41 Problem 26.

!

2.00 mF, C3

Figure 25-42 shows a 12.0 V
•••27
battery  and  four  uncharged  capaci-
!
1.00 mF,
tors  of  capacitances  C1
!
3.00 mF, and C4 !
C2
4.00 mF. If  only  switch  S1 is  closed,
what is the charge on (a) capacitor 1,
(b)  capacitor  2, (c)  capacitor  3, and
(d) capacitor 4? If both switches are
closed, what  is  the  charge  on  (e)  ca-
pacitor 1, (f) capacitor 2, (g) capacitor
3, and (h) capacitor 4?

C3s

C 3 (  F) µ
(b)

C1

C3

S2

C4

S1

C2

+ –
B

Figure 25-42 Problem 27.

742

CHAPTE R  25 CAPACITANCE

!

!

Figure 25-43 displays a 12.0
•••28
V  battery  and  3  uncharged  capaci-
4.00 mF,
tors  of  capacitances  C1
6.00 mF, and  C3 ! 3.00 mF. The
C2
switch is thrown to the left side until
capacitor 1 is fully charged. Then the
switch is thrown to the right. What is
the  final  charge  on  (a) capacitor  1,
(b)  capacitor 2, and  (c)  capacitor  3?

+
–

V0

S

C1

C2

C3

Figure 25-43 Problem 28.

Module 25-4 Energy Stored in an Electric Field
•29 What capacitance is required to store an energy of 10 kW &h
at a potential difference of 1000 V?

•30 How much energy is stored in 1.00 m3 of air due to the “fair
weather” electric field of magnitude 150 V/m?

SSM

A 2.0 mF capacitor and a 4.0 mF capacitor are connected
•31
in parallel across a 300 V potential difference. Calculate the total
energy stored in the capacitors.

•32 A  parallel-plate  air-filled  capacitor  having  area  40 cm2 and
plate spacing 1.0 mm is charged to a potential difference of 600 V.
Find (a) the capacitance, (b) the magnitude of the charge on each
plate, (c)  the  stored  energy, (d)  the  electric  field  between  the
plates, and (e) the energy density between the plates.

••33 A charged isolated metal sphere of diameter 10 cm has a po-
tential of 8000 V relative to V ! 0 at infinity. Calculate the energy
density in the electric field near the surface of the sphere.

••34 In  Fig. 25-28, a  potential  difference  V ! 100 V  is  applied
across  a  capacitor  arrangement  with  capacitances  C1 ! 10.0 mF,
C2 ! 5.00 mF, and C3 ! 4.00 mF. What are (a) charge q3, (b) poten-
tial difference V3, and (c) stored energy U3 for capacitor 3, (d) q1,
(e) V1, and (f) U1 for capacitor 1, and (g) q2, (h) V2, and (i) U2 for
capacitor 2?

••35 Assume that a stationary electron is a point of charge. What
is the energy density u of its electric field at radial distances (a) r !
1.00 mm, (b)  r ! 1.00 mm, (c)  r ! 1.00 nm, and  (d)  r ! 1.00 pm?
(e) What is u in the limit as r : 0?

Venting port

–
–
–

–
–
– h

Figure 25-44 Problem 36.

–  –  –  –
+
+
–  –  –  –
+
+
–  –  –
+ +  +  +  +  +  +  +
+
–
–  –  –  –  –  –
r

As  a  safety  engineer,
••36
you  must  evaluate  the  practice  of
storing  flammable  conducting  liq-
uids  in  nonconducting  containers.
The  company  supplying  a  certain
liquid has been using a squat, cylin-
drical  plastic  container  of  radius
r ! 0.20 m  and  filling  it  to  height
h ! 10 cm, which  is  not  the  con-
tainer’s full interior height (Fig. 25-44). Your investigation reveals
that  during  handling  at  the  company, the  exterior  surface  of  the
container commonly acquires a negative charge density of magni-
tude 2.0 mC/m2 (approximately uniform). Because the liquid is a
conducting material, the charge on the container induces charge
separation  within  the  liquid. (a)  How  much  negative  charge  is
induced in the center of the liquid’s bulk? (b) Assume the capaci-
tance  of  the  central  portion  of  the  liquid  relative  to  ground  is
35 pF. What is the potential energy associated with the negative
charge in that effective capacitor? (c) If a spark occurs between
the ground and the central portion of the liquid (through the vent-
ing port), the potential energy can be fed into the spark. The mini-
mum  spark  energy  needed  to  ignite  the  liquid  is  10 mJ. In  this
situation, can a spark ignite the liquid?

ILW

SSM

WWW

The parallel plates in a capacitor, with a
••37
plate area of 8.50 cm2 and an air-filled separation of 3.00 mm, are
charged by a 6.00 V battery. They are then disconnected from the
battery  and  pulled  apart  (without  discharge)  to  a  separation  of
8.00 mm. Neglecting fringing, find (a) the potential difference be-
tween the plates, (b) the initial stored energy, (c) the final stored
energy, and (d) the work required to separate the plates.

!

5.00 mF, and C3

••38 In  Fig. 25-29, a  potential  difference  V ! 100 V  is  applied
across  a  capacitor  arrangement  with  capacitances  C1 ! 10.0 mF,
15.0 mF. What are (a) charge q3, (b) poten-
C2
tial difference V3, and (c) stored energy U3 for capacitor 3, (d) q1,
(e) V1, and (f) U1 for capacitor 1, and (g) q2, (h) V2, and (i) U2 for
capacitor 2?

!

A

B

C 1

In Fig. 25-45, C1 ! 10.0
••39
mF, C2
!
!
20.0 mF, and  C3
25.0 mF. If  no  capacitor  can
withstand  a  potential  differ-
ence of more than 100 V without failure, what are (a) the magni-
tude of the maximum potential difference that can exist between
points A and B and (b) the maximum energy that can be stored in
the three-capacitor arrangement?

Figure 25-45 Problem 39.

C2

C3

Module 25-5 Capacitor with a Dielectric
•40 An  air-filled  parallel-plate  capacitor  has  a  capacitance  of
1.3 pF. The separation of the plates is doubled, and wax is inserted
between  them. The  new  capacitance  is  2.6 pF. Find  the  dielectric
constant of the wax.

SSM

A coaxial cable used in a transmission line has an inner
•41
radius  of  0.10 mm  and  an  outer  radius  of  0.60 mm. Calculate  the
capacitance  per  meter  for  the  cable. Assume  that  the  space
between the conductors is filled with polystyrene.

•42 A  parallel-plate  air-filled  capacitor  has  a  capacitance  of
50 pF. (a) If each of its plates has an area of 0.35 m2, what is the
separation? (b) If the region between the plates is now filled with
material having k ! 5.6, what is the capacitance?

•43 Given a 7.4 pF air-filled capacitor, you are asked to convert it to
a capacitor that can store up to 7.4 mJ with a maximum potential dif-
ference of 652 V. Which dielectric in Table 25-1 should you use to fill
the gap in the capacitor if you do not allow for a margin of error?

••44 You are asked to construct a capacitor having a capacitance
near  1 nF  and  a  breakdown  potential  in  excess  of  10 000 V. You
think of using the sides of a tall Pyrex drinking glass as a dielectric,
lining the inside and outside curved surfaces with aluminum foil to
act  as  the  plates. The  glass  is  15 cm  tall  with  an  inner  radius  of
3.6 cm and an outer radius of 3.8 cm. What are the (a) capacitance
and (b) breakdown potential of this capacitor?

••45 A  certain  parallel-plate  capacitor  is  filled  with  a  dielectric
for which k ! 5.5. The area of each plate is 0.034 m2, and the plates
are separated by 2.0 mm. The capacitor will fail (short out and burn
up) if the electric field between the plates exceeds 200 kN/C. What
is the maximum energy that can be stored in the capacitor?

••46 In Fig. 25-46, how much charge is
stored  on  the  parallel-plate  capacitors
by  the  12.0 V  battery?  One  is  filled
with air, and the other is filled with a di-
electric for which k ! 3.00; both capaci-
tors have a plate area of 5.00 $ 10#3 m2
and a plate separation of 2.00 mm.

V

C1 C2

Figure 25-46 Problem 46.

ILW

SSM

A  certain  substance  has  a  dielectric  constant  of
••47
2.8 and a dielectric strength of 18 MV/m. If it is used as the dielec-
tric  material  in  a  parallel-plate  capacitor, what  minimum  area
should the plates of the capacitor have to obtain a capacitance of
7.0 $ 10#2 mF and to ensure that the capacitor will be able to with-
stand a potential difference of 4.0 kV?

••48 Figure  25-47  shows  a  parallel-
plate  capacitor  with  a  plate  area  A
! 5.56 cm2 and  separation  d ! 5.56
mm. The left half of the gap is filled
with  material  of  dielectric  constant
k1 ! 7.00; the right half is filled with
material  of  dielectric  constant  k2 !
12.0. What is the capacitance?

A/2

  1κ

A/2

  2κ

d

Figure 25-47 Problem 48.

••49 Figure  25-48  shows  a  parallel-plate  ca-
pacitor  with  a  plate  area  A ! 7.89 cm2 and
plate separation d ! 4.62 mm. The top half of
the  gap  is  filled  with  material  of  dielectric
constant k1 ! 11.0; the  bottom  half  is  filled
with material of dielectric constant k2 ! 12.0.
What is the capacitance?

κ 2
κ 1

d

Figure 25-48
Problem 49.

Figure 25-49 shows a parallel-
••50
plate  capacitor  of  plate  area  A ! 10.5
cm2 and plate separation 2d ! 7.12 mm.
The left half of the gap is filled with ma-
terial  of  dielectric  constant  k1 ! 21.0;
the top of the right half is filled with ma-
terial  of  dielectric  constant  k2 ! 42.0;
the  bottom  of  the  right  half  is  filled
with material of dielectric constant k3 !
58.0.What is the capacitance?

A/2

2d

κ 1

A/2

κ 2

κ 3

d

d

Figure 25-49 Problem 50.

SSM

WWW

Module 25-6 Dielectrics and Gauss’ Law
A parallel-plate capacitor has a capacitance of
•51
100 pF, a  plate  area  of  100 cm2, and  a  mica  dielectric  (k
5.4)
completely filling the space between the plates. At 50 V potential
difference, calculate (a) the electric field magnitude E in the mica,
(b) the magnitude of the free charge on the plates, and (c) the mag-
nitude of the induced surface charge on the mica.

!

•52 For the arrangement of Fig. 25-17, suppose that the battery
remains  connected  while  the  dielectric  slab  is  being  introduced.
Calculate  (a)  the  capacitance, (b)  the  charge  on  the  capacitor
plates, (c) the electric field in the gap, and (d) the electric field in
the slab, after the slab is in place.
••53 A  parallel-plate  capacitor  has  plates  of  area  0.12 m2 and  a
separation of 1.2 cm. A battery charges the plates to a potential dif-
ference of 120 V and is then disconnected. A dielectric slab of thick-
ness 4.0 mm and dielectric constant 4.8 is then placed symmetrically
between the plates. (a) What is the capacitance before the slab is in-
serted? (b) What is the capacitance with the slab in place? What is
the free charge q (c) before and (d) after the slab is inserted? What is
the  magnitude  of  the  electric  field  (e)  in  the  space  between  the
plates and dielectric and (f) in the dielectric itself? (g) With the slab
in place, what is the potential difference across the plates? (h) How
much external work is involved in inserting the slab?
••54 Two  parallel  plates  of  area  100 cm2 are  given  charges  of
equal  magnitudes  8.9 $ 10#7 C  but  opposite  signs. The  electric
field  within  the  dielectric  material  filling  the  space  between  the
plates is 1.4 $ 106 V/m. (a) Calculate the dielectric constant of the

PROB LE M S

743

material. (b) Determine the magnitude of the charge induced on
each dielectric surface.

••55 The space between two concentric conducting spherical shells
of radii b ! 1.70 cm and a ! 1.20 cm is filled with
a  substance  of  dielectric  constant  k
23.5. A
potential difference V ! 73.0 V is applied across
the inner and outer shells. Determine (a) the ca-
pacitance of the device, (b) the free charge q on
the  inner  shell, and  (c)  the charge  q- induced
along the surface of the inner shell.

–  +
V

!

C1

Additional Problems
56 In  Fig. 25-50,
the  battery  potential
difference V is  10.0 V  and  each  of  the  seven
capacitors has capacitance 10.0 mF. What is the
charge on (a) capacitor 1 and (b) capacitor 2?

C2

Figure 25-50
Problem 56.

SSM

57
mF, and C3 C4

In Fig. 25-51, V ! 9.0 V, C1 ! C2
!!

15 mF. What is the charge on capacitor 4?

!

30

V

C1

C2

C4

C3

Figure 25-51 Problem 57.

58 (a) If C ! 50 mF in Fig. 25-52, what
is the equivalent capacitance between
points A and B?  (Hint: First  imagine
that  a  battery  is  connected  between
those two points.) (b) Repeat for points
A and D.

59 In Fig. 25-53, V ! 12 V, C1 ! C4 !
2.0 mF, C2 ! 4.0 mF, and  C3 ! 1.0 mF.
What is the charge on capacitor 4?

C

A

2C

B

6C

Figure 25-52 Problem 58.

4C

D

V

C1

C3

C2

C4

Figure 25-53 Problem 59.

The chocolate crumb mystery.
60
This  story  begins  with  Problem  60  in
Chapter 23. As part of the investigation
of the biscuit factory explosion, the elec-
tric  potentials  of  the  workers  were
measured  as  they  emptied  sacks  of
chocolate crumb powder into the load-
ing bin, stirring up a cloud of the powder
around themselves. Each worker had an
electric potential of about 7.0 kV relative to the ground, which was
taken  as  zero  potential. (a) Assuming  that  each  worker  was  effec-
tively a capacitor with a typical capacitance of 200 pF, find the energy
stored  in  that  effective  capacitor. If  a  single  spark  between  the
worker and any conducting object connected to the ground neutral-
ized  the  worker, that  energy  would  be  transferred  to  the  spark.
According  to  measurements, a  spark  that  could  ignite  a  cloud  of
chocolate crumb powder, and thus set off an explosion, had to have
an energy of at least 150 mJ. (b) Could a spark from a worker have
set off an explosion in the cloud of
powder  in  the  loading  bin?  (The
story continues with Problem 60 in
Chapter 26.)

C 1

P

S

61 Figure 25-54 shows capacitor
1  (C1 ! 8.00 mF), capacitor 2  (C2
! 6.00 mF), and  capacitor  3  (C3 !

V

C2

C 3

C4

Figure 25-54 Problem 61.

744

CHAPTE R  25 CAPACITANCE

8.00 mF) connected to a 12.0 V battery. When switch S is closed so as
6.00 mF), (a)  how  much
to  connect  uncharged  capacitor  4  (C4
charge passes through point P from the battery and (b) how much
charge  shows  up  on  capacitor  4?  (c) Explain  the  discrepancy  in
those two results.

!

62 Two air-filled, parallel-plate capacitors are to be connected to a
10 V battery, first individually, then in series, and then in parallel. In
those arrangements, the energy stored in the capacitors turns out to
be, listed least to greatest: 75 mJ, 100 mJ, 300 mJ, and 400 mJ. Of the
two capacitors, what is the (a) smaller and (b) greater capacitance?

63 Two  parallel-plate  capacitors, 6.0 mF  each, are  connected
in series to a 10 V battery. One of the capacitors is then squeezed
so  that  its  plate  separation  is  halved. Because  of  the  squeezing,
(a) how much additional charge is transferred to the capacitors by
the battery and (b) what is the increase in the total charge stored
on the capacitors (the charge on the positive plate of one capacitor
plus the charge on the positive plate of the other capacitor)?

!!

In  Fig. 25-55, V ! 12 V, C1
6.0 mF, and  C2 C3 C4

!
64
!!!
C5 C6
4.0 mF. What  are  (a)  the  net  charge
stored  on  the  capacitors  and  (b) the
charge on capacitor 4?

$

SSM

In Fig. 25-56, the parallel-plate
65
10#2 m2
capacitor  of  plate  area  2.00
is  filled  with  two  dielectric  slabs, each
with thickness 2.00 mm. One slab has di-
electric  constant  3.00, and  the  other,
4.00. How much charge does the 7.00 V
battery store on the capacitor?

C1
C2

C3

C4

V

C5

C6

Figure 25-55 Problem 64.

66 A  cylindrical  capacitor  has  radii  a
and b as in Fig. 25-6. Show that half the
stored  electric  potential  energy  lies
within  a  cylinder  whose  radius
is
r !

ab.

V

Figure 25-56
Problem 65.

1

67 A  capacitor  of  capacitance  C1 !
6.00 mF is connected in series with a capacitor of capacitance C2 !
4.00 mF, and  a potential  difference  of  200 V  is  applied  across  the
pair. (a) Calculate the equivalent capacitance. What are (b) charge
q1 and (c) potential difference V1 on capacitor 1 and (d) q2 and (e)
V2 on capacitor 2?

68 Repeat Problem 67 for the same two capacitors but with them
now connected in parallel.

69 A certain capacitor is charged to a potential difference V. If
you wish to increase its stored energy by 10%, by what percentage
should you increase V?

b

70 A  slab  of  copper  of  thickness
b ! 2.00 mm is thrust into a parallel-
plate capacitor of plate area A ! 2.40
cm2 and  plate  separation  d ! 5.00
mm, as shown in Fig. 25-57; the slab is
exactly  halfway  between  the  plates.
(a) What is the capacitance after the
slab  is  introduced?  (b)  If  a  charge
q ! 3.40 mC  is  maintained  on  the
plates, what is the ratio of the stored energy before to that after the
slab is inserted? (c) How much work is done on the slab as it is in-
serted? (d) Is the slab sucked in or must it be pushed in?

Figure 25-57
Problems 70 and  71.

d

71 Repeat Problem 70, assuming that a potential difference V !
85.0 V, rather than the charge, is held constant.

72 A  potential  difference  of  300 V  is  applied  to  a  series
connection  of  two  capacitors  of  capacitances  C1 ! 2.00 mF  and
C2 ! 8.00 mF. What are (a) charge q1 and (b) potential difference
V1 on capacitor 1 and (c) q2 and (d) V2 on capacitor 2? The charged
capacitors  are  then  disconnected  from  each  other  and  from  the
battery. Then  the  capacitors  are  reconnected  with  plates  of  the
same signs wired together (the battery is not used). What now are
(e) q1, (f) V1, (g) q2, and (h) V2? Suppose, instead, the capacitors
charged  in  part  (a)  are  reconnected  with  plates  of  opposite signs
wired together. What now are (i) q1, (j) V1, (k) q2, and (l) V2?

A

C3

C1

73 Figure  25-58  shows  a  four-
capacitor  arrangement  that  is  con-
nected to a larger circuit at points A
and B. The  capacitances  are  C1 !
10 mF  and  C2 ! C3 ! C4 ! 20 mF.
The charge on capacitor 1 is 30 mC.
What is the magnitude of the poten-
tial difference VA # VB?
74 You have two plates of copper, a sheet of mica (thickness !
0.10 mm, k ! 5.4), a sheet of glass (thickness ! 2.0 mm, k ! 7.0),
and  a  slab  of  paraffin  (thickness ! 1.0 cm, k ! 2.0). To  make  a
parallel-plate capacitor with the largest C, which sheet should you
place between the copper plates?

Figure 25-58 Problem 73.

C2

C4

B

75 A capacitor of unknown capacitance C is charged to 100 V and
connected across an initially uncharged 60 mF capacitor. If the final
potential difference across the 60 mF capacitor is 40 V, what is C?

76 A 10 V battery is connected to a series of n capacitors, each of
capacitance 2.0 mF. If the total stored energy is 25 mJ, what is n?

B

+
–

SSM

In Fig. 25-59, two parallel-
77
plate  capacitors  A and B are  con-
nected  in  parallel  across  a  600 V
battery. Each plate has area 80.0 cm2;
the  plate  separations  are  3.00 mm.
Capacitor A is filled with air; capaci-
tor B is  filled  with  a  dielectric  of  dielectric  constant  k
2.60.
Find the magnitude of the electric field within (a) the dielectric of
capacitor B and (b) the air of capacitor A. What are the free charge
densities s on  the  higher-potential  plate  of  (c)  capacitor  A and
(d) capacitor B? (e) What is the induced charge density s- on the
top surface of the dielectric?

Figure 25-59 Problem 77.

!

A

78 You  have  many  2.0 mF  capacitors, each  capable  of  with-
standing 200 V without undergoing electrical breakdown (in which
they conduct charge instead of storing it). How would you assem-
ble a combination having an equivalent capacitance of (a) 0.40 mF
and (b) 1.2 mF, each combination capable of withstanding 1000 V?
79 A  parallel-plate  capacitor  has  charge  q and  plate  area  A.
(a) By  finding  the  work  needed  to  increase  the  plate  separation
from x to x % dx, determine the force between the plates. (Hint:
See Eq. 8-22.) (b) Then show that the force per unit area (the elec-
trostatic stress) acting on either plate is equal to the energy density
´0E2/2 between the plates.
80 A capacitor is charged until its stored energy is 4.00 J. A sec-
ond capacitor is then connected to it in parallel. (a) If the charge
distributes  equally, what  is  the  total  energy  stored  in  the  electric
fields? (b) Where did the missing energy go?
