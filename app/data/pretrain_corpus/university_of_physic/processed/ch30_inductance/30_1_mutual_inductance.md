INDUCTANCE

? Many trafﬁc lights change when a car rolls up to the intersection. How does

the light sense the presence of the car?

Take a length of copper wire and wrap it around a pencil to form a coil. If you

put this coil in a circuit, does it behave any differently than a straight piece
of  wire?  Remarkably,  the  answer  is  yes.  In  an  ordinary  gasoline-powered
car,  a  coil  of  this  kind  makes  it  possible  for  the  12-volt  car  battery  to  provide
thousands  of  volts  to  the  spark  plugs,  which  in  turn  makes  it  possible  for  the
plugs to ﬁre and make the engine run. Other coils of this type are used to keep
ﬂuorescent light ﬁxtures shining. Larger coils placed under city streets are used
to control the operation of trafﬁc signals. All of these applications, and many oth-
ers, involve the induction effects that we studied in Chapter 29.

A changing current in a coil induces an emf in an adjacent coil. The coupling
between the coils is described by their mutual inductance. A changing current in
a coil also induces an emf in that same coil. Such a coil is called an inductor, and
the relationship of current to emf is described by the inductance (also called self-
inductance) of the coil. If a coil is initially carrying a current, energy is released
when the current decreases; this principle is used in automotive ignition systems.
We’ll ﬁnd that this released energy was stored in the magnetic ﬁeld caused by the
current that was initially in the coil, and we’ll look at some of the practical appli-
cations of magnetic-ﬁeld energy.

We’ll also take a ﬁrst look at what happens when an inductor is part of a cir-
cuit. In Chapter 31 we’ll go on to study how inductors behave in alternating-current
circuits; in that chapter we’ll learn why inductors play an essential role in modern
electronics, including communication systems, power supplies, and many other
devices.

30.1 Mutual Inductance

In Section 28.4 we considered the magnetic interaction between two wires carry-
ing steady currents; the current in one wire causes a magnetic ﬁeld, which exerts
a  force  on  the  current  in  the  second  wire.  But  an  additional  interaction  arises

30

LEARNING GOALS

By studying this chapter, you will

learn:

• How a time-varying current in one

coil can induce an emf in a second,

unconnected coil.

• How to relate the induced emf in a

circuit to the rate of change of

current in the same circuit.

• How to calculate the energy stored

in a magnetic field.

• How to analyze circuits that include

both a resistor and an inductor (coil).

• Why electrical oscillations occur in

circuits that include both an inductor

and a capacitor.

• Why oscillations decay in circuits

with an inductor, a resistor, and a

capacitor.

991

992

CHAPTER 30 Inductance

30.1 A current
magnetic ﬂux through coil 2.

i1

in coil 1 gives rise to a

Mutual inductance: If the
current in coil 1 is changing,
the changing flux through coil 2
induces an emf in coil 2.

Coil 1
N1 turns

i1

i1

Coil 2
N2 turns

S
B

F

B2

30.2 This electric toothbrush makes use
of mutual inductance. The base contains a
coil that is supplied with alternating cur-
rent from a wall socket. This varying cur-
rent induces an emf in a coil within the
toothbrush itself, which is used to recharge
the toothbrush battery.

Toothbrush with
coil connected
to battery

Base with
recharging coil
connected to
wall socket

between two circuits when there is a changing current in one of the circuits. Con-
sider two neighboring coils of wire, as in Fig. 30.1. A current ﬂowing in coil 1
produces a magnetic ﬁeld  and hence a magnetic ﬂux through coil 2. If the current
in coil 1 changes, the ﬂux through coil 2 changes as well; according to Faraday’s
law, this induces an emf in coil 2. In this way, a change in the current in one cir-
cuit can induce a current in a second circuit.

S
B

i,

i1

Let’s analyze the situation shown in Fig. 30.1 in more detail. We will use low-
ercase  letters  to  represent  quantities  that  vary  with  time;  for  example,  a  time-
varying current is  often with a subscript to identify the circuit. In Fig. 30.1 a
current
in coil 1 sets up a magnetic ﬁeld (as indicated by the blue lines), and
some  of  these  ﬁeld  lines  pass  through  coil  2.  We  denote  the  magnetic  ﬂux
through each turn of coil 2, caused by the current
(If the ﬂux
is  different  through  different  turns  of  the  coil,  then
denotes  the  average
£B2
i1.
ﬂux.) The magnetic ﬁeld is proportional to
£B2
i1
in coil 2,
When
given by

i1,
changes; this changing ﬂux induces an emf

in coil 1, as
£B2
is also proportional to

changes,

£B2.

E2

so

i1

E2 = - N2

d£B2
dt
£B2

(30.1)

We  could  represent  the  proportionality  of
1constant)i1,
in the relationship. Introducing a proportionality constant
inductance of the two coils, we write

and

i1

but instead it is more convenient to include the number of turns

in  the  form

£B2 =
N2
called the mutual

M21,

N2£B2 = M21i1

(30.2)

where

£B2

is the ﬂux through a single turn of coil 2. From this,
d£B2
dt

= M21

di1
dt

N2

and we can rewrite Eq. (30.1) as

E2 = - M21

di1
dt

(30.3)

That is, a change in the current
proportional to the rate of change of

i1

i1
We may also write the deﬁnition of mutual inductance, Eq. (30.2), as

(Fig. 30.2).

in coil 1 induces an emf in coil 2 that is directly

M21 =

N2£B2
i1

£B2

i1.

Then  the  mutual  inductance

through each turn of coil 2 is directly pro-
If the coils are in vacuum, the ﬂux
M21
portional  to  the  current
is  a  constant  that
depends only on the geometry of the two coils (the size, shape, number of turns,
and orientation of each coil and the separation between the coils). If a magnetic
material is present,
also depends on the magnetic properties of the material.
If the material has nonlinear magnetic properties—that is, if the relative perme-
(deﬁned in Section 28.8) is not constant and magnetization is not pro-
ability
In
portional to magnetic ﬁeld—then
i1.
In this discussion
that case the mutual inductance also depends on the value of
we will assume that any magnetic material present has constant
Km
so that ﬂux is
depends on geometry only.
directly proportional to current and

is no longer directly proportional to

£B2

M21

Km

i1.

M21

i2

in coil 2 causes a changing ﬂux

We can repeat our discussion for the opposite case in which a changing cur-
£B1
in coil 1. We might
rent
M12
M21
expect that the corresponding constant
because
in  general  the  two  coils  are  not  identical  and  the  ﬂux  through  them  is  not  the
same. It turns out, however, that
even when the two
coils are not symmetric. We call this common value simply the mutual inductance,

would be different from

is always equal to

and an emf

M21,

M12

E1

30.1 Mutual Inductance

993

denoted  by  the  symbol  M without  subscripts;  it  characterizes  completely  the
induced-emf interaction of two coils. Then we can write

E2 = - M

  and  E1 = - M

di1
dt

di2
dt

where the mutual inductance M is

(mutually induced emfs)

(30.4)

M =

N2£B2
i1

=

N1£B1
i2

(mutual inductance)

(30.5)

The negative signs in Eq. (30.4) are a reﬂection of Lenz’s law. The ﬁrst equation
says  that  a  change  in  current  in  coil  1  causes  a  change  in  ﬂux  through  coil  2,
inducing an emf in coil 2 that opposes the ﬂux change; in the second equation the
roles of the two coils are interchanged.

CAUTION Only a time-varying current induces an emf Note that only a time-varying cur-
rent  in  a  coil  can  induce  an  emf  and  hence  a  current  in  a  second  coil.  Equations  (30.4)
show that the induced emf in each coil is directly proportional to the rate of change of the
current in the other coil, not to the value of the current. A steady current in one coil, no
matter how strong, cannot induce a current in a neighboring coil. ❙

The SI unit of mutual inductance is called the henry (1 H), in honor of the
American physicist Joseph Henry (1797–1878), one of the discoverers of electro-
magnetic  induction.  From  Eq.  (30.5),  one  henry  is  equal  to  one  weber  per
ampere. Other equivalent units, obtained by using Eq. (30.4), are one volt-second
per ampere, one ohm-second, and one joule per ampere squared:
1 H = 1 Wb>A = 1 V # s>A = 1 Æ # s = 1 J>A2
Just as the farad is a rather large unit of capacitance (see Section 24.1), the henry
is a rather large unit of mutual inductance. As Example 30.1 shows, typical val-
1mH2
ues  of  mutual  inductance  can  be  in  the  millihenry  (mH)  or  microhenry
range.

Drawbacks and Uses of Mutual Inductance
Mutual inductance can be a nuisance in electric circuits, since variations in cur-
rent in one circuit can induce unwanted emfs in other nearby circuits. To mini-
mize  these  effects,  multiple-circuit  systems  must  be  designed  so  that
is  as
small as possible; for example, two coils would be placed far apart or with their
planes perpendicular.

M

Happily, mutual inductance also has many useful applications. A transformer,
used in alternating-current circuits to raise or lower voltages, is fundamentally no
different from the two coils shown in Fig. 30.1. A time-varying alternating cur-
rent in one coil of the transformer produces an alternating emf in the other coil;
the  value  of
which  depends  on  the  geometry  of  the  coils,  determines  the
amplitude of the induced emf in the second coil and hence the amplitude of the
output  voltage.  (We’ll  describe  transformers  in  more  detail  in  Chapter  31 after
we’ve discussed alternating current in greater depth.)

M,

Example 30.1

Calculating mutual inductance

In one form of Tesla coil (a high-voltage generator popular in sci-
ence museums), a long solenoid with length l and cross-sectional
area
turns
surrounds it at its center (Fig. 30.3). Find the mutual inductance M.

turns of wire. A coil with

is closely wound with

N1

N2

A

SOLUTION

IDENTIFY  and SET  UP: Mutual inductance occurs here because a
current  in  either  coil  sets  up  a  magnetic  ﬁeld  that  causes  a  ﬂux
through the other coil. From Example 28.9 (Section 28.7) we have

Continued
