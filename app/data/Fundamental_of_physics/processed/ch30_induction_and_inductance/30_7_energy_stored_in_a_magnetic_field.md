30-7 E N E RGY  STOR E D  I N  A  MAG N ETIC  FI E LD

887

30-7 ENERGY STORED IN A MAGNETIC FIELD

Learning Objectives
After reading this module, you should be able to . . .

30.35 Describe the derivation of the equation for the

magnetic field energy of an inductor in an RL circuit
with a constant emf source.

30.36 For an inductor in an RL circuit, apply the relationship
between the magnetic field energy U, the inductance L,
and the current i.

Key Idea
● If an inductor L carries a current i, the inductor’s magnetic field stores an energy given by

UB ! 1

2Li2

(magnetic energy).

Energy Stored in a Magnetic Field
When we pull two charged particles of opposite signs away from each other, we
say that the resulting electric potential energy is stored in the electric field of the
particles. We  get  it  back  from  the  field  by  letting  the  particles  move  closer
together again. In the same way we say energy is stored in a magnetic field, but
now we deal with current instead of electric charges.

To  derive  a  quantitative  expression  for  that  stored  energy, consider  again
Fig. 30-16, which shows a source of emf # connected to a resistor R and an induc-
tor L. Equation 30-39, restated here for convenience,

# ! L

di
dt

& iR,

(30-46)

is  the  differential  equation  that  describes  the  growth  of  current  in  this  circuit.
Recall  that  this  equation  follows  immediately  from  the  loop  rule  and  that  the
loop rule in turn is an expression of the principle of conservation of energy for
single-loop circuits. If we multiply each side of Eq. 30-46 by i, we obtain

# i ! Li

di
dt

& i2R,

(30-47)

which has the following physical interpretation in terms of the work done by the
battery and the resulting energy transfers:

1. If a differential amount of charge dq passes through the battery of emf # in
Fig. 30-16  in  time  dt, the  battery  does  work  on  it  in  the  amount  # dq. The
rate at which the battery does work is (# dq)/dt, or #i. Thus, the left side of
Eq. 30-47 represents the rate at which the emf device delivers energy to the
rest of the circuit.

2. The rightmost term in Eq. 30-47 represents the rate at which energy appears as

thermal energy in the resistor.

3. Energy  that  is  delivered  to  the  circuit  but  does  not  appear  as  thermal
energy  must, by  the  conservation-of-energy  hypothesis, be  stored  in  the
magnetic field of the inductor. Because Eq. 30-47 represents the principle of
conservation  of  energy  for  RL circuits, the  middle  term  must  represent
the rate  dUB/dt at  which  magnetic  potential  energy  UB is  stored  in  the
magnetic field.

Thus

dUB
dt

! Li

di
dt

.

(30-48)

888

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

We can write this as

Integrating yields

dUB ! Li di.

"UB

0

dUB !"i

0

Li di

or

UB ! 1

2 Li2

(magnetic energy),

(30-49)

which represents the total energy stored by an inductor L carrying a current i.
Note  the  similarity  in  form  between  this  expression  for  the  energy  stored  in  a
magnetic field and the expression for the energy stored in an electric field by a
capacitor with capacitance C and charge q; namely,

UE !

q2
2C

.

(30-50)

(The variable i2 corresponds to q2, and the constant L corresponds to 1/C.)

Sample Problem 30.07 Energy stored in a magnetic field

A  coil  has  an  inductance  of  53 mH  and  a  resistance  of
0.35 1.

be satisfied? Using Eq. 30-49 twice allows us to rewrite this
energy condition as

(a) If a 12 V emf is applied across the coil, how much energy
is stored in the magnetic field after the current has built up
to its equilibrium value?

or

2
2 Li.

1

2) 1
2 Li2 ! (1
i ! # 1

2 $ i..

(30-52)

KEY IDEA

The energy stored in the magnetic field of a coil at any time
depends on the current through the coil at that time, accord-
ing to Eq. 30-49

(UB ! 1

2 Li2)
.

Calculations: Thus, to find the energy UB. stored at equi-
librium, we  must  first  find  the  equilibrium  current. From
Eq. 30-41, the equilibrium current is

1
This equation tells us that, as the current increases from its
initial value of 0 to its final value of  i., the magnetic field
will have half its final stored energy when the current has in-
creased to this value. In general, we know that i is given by
Eq. 30-41, and  here  i. (see  Eq. 30-51)  is  #/R; so  Eq. 30-52
becomes

#
R

 (1 % e%t/tL) !

#
2R

.

! 34.3 A.

(30-51)

By canceling #/R and rearranging, we can write this as

1

i. !

#
R

!

12 V
0.35 1

Then substitution yields

2 ! (1

2)(53 $ 10 %3 H)(34.3 A)2

UB. ! 1

2 Li.
! 31 J.

(Answer)

(b) After how many time constants will half this equilibrium
energy be stored in the magnetic field?

Calculations: Now we are being asked: At what time t will
the relation

UB ! 1

2 UB.

which yields

e%t/tL ! 1 %

! 0.293,

1
2
1

t
*L

! %ln 0.293 ! 1.23

or

t % 1.2tL.

(Answer)

Thus, the energy stored in the magnetic field of the coil by
the  current  will  reach  half  its  equilibrium  value  1.2  time
constants after the emf is applied.

Additional examples, video, and practice available at WileyPLUS
