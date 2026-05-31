728

CHAPTE R  25 CAPACITANCE

is no electric field within the connecting wires to move con-
duction  electrons. The  initial  charge  on  capacitor  1  is  then
shared between the two capacitors.

Because the total charge cannot magically change, the total
after the transfer must be

Calculations: Initially, when capacitor 1 is connected to the
battery, the charge it acquires is, from Eq. 25-1,

thus

q1 % q2 ! q0

(charge conservation);

q2 ! q0 # q1.

q0 ! C1V0 ! (3.55 $ 10#6 F)(6.30 V)

! 22.365 $ 10#6 C.

When switch S in Fig. 25-11 is closed and capacitor 1 begins
to  charge  capacitor  2, the  electric  potential  and  charge  on
capacitor 1 decrease and those on capacitor 2 increase until

V1 ! V2

(equilibrium).

From Eq. 25-1, we can rewrite this as

q1
C1

!

q2
C2

(equilibrium).

We can now rewrite the second equilibrium equation as

q1
C1

!

q0 # q1
C2

.

Solving this for q1 and substituting given data, we find

q1 ! 6.35 mC.

(Answer)

The rest of the initial charge (q0 ! 22.365 mC) must be on
capacitor 2:

q2 ! 16.0 mC.

(Answer)

Additional examples, video, and practice available at WileyPLUS

25-4 ENERGY STORED IN AN ELECTRIC FIELD

Learning Objectives
After reading this module, you should be able to . . .

25.16 Explain how the work required to charge a capacitor

results in the potential energy of the capacitor.

25.17 For a capacitor, apply the relationship between the

potential energy U, the capacitance C, and the potential
difference V.

potential energy, the internal volume, and the internal
energy density.

25.19 For any electric field, apply the relationship between
the potential energy density u in the field and the field’s
magnitude E.

25.18 For a capacitor, apply the relationship between the

25.20 Explain the danger of sparks in airborne dust.

Key Ideas
● The electric potential energy U of a charged capacitor,

U !

q2
2c

! 1

2CV 2,

is equal to the work required to charge the capacitor. This en-
ergy can be associated with the capacitor’s electric field

:
.E

● Every electric field, in a capacitor or from any other source,
has an associated stored energy. In vacuum, the energy den-
sity u (potential energy per unit volume) in a field of magni-
tude E is

u ! 1

2´0E2.

Energy Stored in an Electric Field
Work must be done by an external agent to charge a capacitor. We can imagine
doing the work ourselves by transferring electrons from one plate to the other,
one by one. As the charges build, so does the electric field between the plates,
which opposes the continued transfer. So, greater amounts of work are required.
Actually, a battery does all this for us, at the expense of its stored chemical en-
ergy. We  visualize  the  work  as  being  stored  as  electric  potential  energy  in  the
electric field between the plates.

25-4 E N E RGY  STOR E D  I N  AN  E LECTR IC  FI E LD

729

Suppose that, at a given instant, a charge q- has been transferred from one
plate of a capacitor to the other. The potential difference V- between the plates at
that instant will be q-/C. If an extra increment of charge dq- is then transferred,
the increment of work required will be, from Eq. 24-6,

dW ! V- dq- !

q-
C

dq-.

The work required to bring the total capacitor charge up to a final value q is

W ! " dW !

1

C "q

0

q- dq- !

q2
2C

.

This work is stored as potential energy U in the capacitor, so that

U !

q2
2C

(potential energy).

(25-21)

From Eq. 25-1, we can also write this as

U ! 1

2 CV 2

(potential energy).

(25-22)

Equations 25-21 and 25-22 hold no matter what the geometry of the capacitor is.
To  gain  some  physical  insight  into  energy  storage, consider  two  parallel-
plate  capacitors  that  are  identical  except  that  capacitor  1  has  twice  the  plate
separation  of  capacitor  2. Then  capacitor  1  has  twice  the  volume  between  its
plates and also, from Eq. 25-9, half the capacitance of capacitor 2. Equation 25-
4 tells us that if both capacitors have the same charge q, the electric fields be-
tween their plates are identical. And Eq. 25-21 tells us that capacitor 1 has twice
the stored potential energy of capacitor 2. Thus, of two otherwise identical ca-
pacitors  with  the  same  charge  and  same  electric  field, the  one  with  twice  the
volume between its plates has twice the stored potential energy. Arguments like
this tend to verify our earlier assumption:

The potential energy of a charged capacitor may be viewed as being stored in the
electric field between its plates.

Explosions in Airborne Dust
As we discussed in Module 24-8, making contact with certain materials, such as
clothing, carpets, and even playground slides, can leave you with a significant
electrical  potential. You  might  become  painfully  aware  of  that  potential  if  a
spark leaps between you and a grounded object, such as a faucet. In many in-
dustries involving the production and transport of powder, such as in the cos-
metic and food industries, such a spark can be disastrous. Although the powder
in  bulk  may  not  burn  at  all, when  individual  powder  grains  are  airborne  and
thus surrounded by oxygen, they can burn so fiercely that a cloud of the grains
burns as an explosion. Safety engineers cannot eliminate all possible sources of
sparks  in  the  powder  industries. Instead, they  attempt  to  keep  the  amount  of
energy  available  in  the  sparks  below  the  threshold  value  Ut (% 150  mJ)  typi-
cally required to ignite airborne grains.

Suppose a person becomes charged by contact with various surfaces as he walks
through an airborne powder.We can roughly model the person as a spherical capaci-
tor of radius R ! 1.8 m. From Eq. 25-18
, we
see that the energy .f the capacitor is

(C ! 4p´0R)

and Eq. 25-22

(U ! 1

2CV 2)

U ! 1

2 (4p´0R)V 2.

730

CHAPTE R  25 CAPACITANCE

From this we see that the threshold energy corresponds to a potential of

V !

2Ut
4p´0R

!

2(150 $ 10 #3 J)
4p(8.85 $ 10#12 C2/N&m2)(1.8 m)

! 3.9 $ 104 V.

A

A

Safety engineers attempt to keep the potential of the personnel below this level
by “bleeding” off the charge through, say, a conducting floor.

Energy Density
In a parallel-plate capacitor, neglecting fringing, the electric field has the same
value  at  all  points  between  the  plates. Thus, the  energy  density u — that  is, the
potential energy per unit volume between the plates — should also be uniform.
We  can  find  u by  dividing  the  total  potential  energy  by  the  volume  Ad of  the
space between the plates. Using Eq. 25-22, we obtain

u !

U
Ad

!

CV 2
2Ad

.

(25-23)

With Eq. 25-9 (C ! ´0A/d), this result becomes
2 ´0 # V
d $

u ! 1

2

.

(25-24)

However, from Eq. 24-42 (E ! #’V/’s), V/d equals the electric field magnitude E; so

u ! 1

2 ´0E2

(energy density).

(25-25)

Although  we  derived  this  result  for  the  special  case  of  an  electric  field  of  a
ex-
parallel-plate capacitor, it holds for any electric field. If an electric field
ists at any point in space, that site has an electric potential energy with a den-
sity (amount per unit volume) given by Eq. 25-25.

:
E

Sample Problem 25.04 Potential energy and energy density of an electric field

An  isolated  conducting  sphere  whose  radius  R is  6.85 cm
has a charge q ! 1.25 nC.

(a) How much potential energy is stored in the electric field
of this charged conductor?

KEY IDEAS

(1) An  isolated  sphere  has  capacitance  given  by  Eq. 25-18
(C ! 4p´0R). (2)  The  energy  U stored  in  a  capacitor  de-
pends on the capacitor’s charge q and capacitance C accord-
ing to Eq. 25-21 (U ! q2/2C).

Calculation: Substituting C ! 4p´0R into Eq. 25-21 gives us

U !

q2
2C

!

q2
8p´0R

(b) What is the energy density at the surface of the sphere?

KEY IDEA

The  density  u of  the  energy  stored  in  an  electric  field
depends  on  the  magnitude  E of  the  field, according  to
Eq. 25-25

(u ! 1

.

2´0E2)

Calculations: Here  we  must  first  find  E at  the  surface  of
the sphere, as given by Eq. 23-15:

E !

1
4p´0

q
R2 .

The energy density is then
q2
32p 2´0R4

2´0E2 !

u ! 1

!

(1.25 $ 10#9 C)2
(8p)(8.85 $ 10#12 F/m)(0.0685 m)

!

(1.25 $ 10#9 C)2
(32p 2)(8.85 $ 10#12 C2/N&m2)(0.0685 m)4

! 1.03 $ 10#7 J ! 103 nJ.

(Answer)

! 2.54 $ 10#5 J/m3 ! 25.4 mJ/m3.

(Answer)

Additional examples, video, and practice available at WileyPLUS
