752

CHAPTE R  26 CU R R E NT  AN D  R ESISTANCE

Sample Problem 26.03 In a current, the conduction electrons move very slowly

What  is  the  drift  speed  of  the  conduction  electrons  in  a
copper wire with radius r ! 900 mm when it has a uniform
current i ! 17 mA? Assume  that  each  copper  atom  con-
tributes  one  conduction  electron  to  the  current  and  that
the  current  density  is  uniform  across  the  wire’s  cross
section.

KEY IDEAS

:
J

1. The drift speed vd is related to the current density

and
the  number  n of  conduction  electrons  per  unit  volume
according to Eq. 26-7, which we can write as J ! nevd.
2. Because the current density is uniform, its magnitude J is
related  to  the  given  current  i and  wire  size  by  Eq. 26-5
(J ! i/A, where A is the cross-sectional area of the wire).
3. Because  we  assume  one  conduction  electron  per  atom,
the number n of conduction electrons per unit volume is
the same as the number of atoms per unit volume.

Calculations: Let us start with the third idea by writing

n ! # atoms

volume $ ! #atoms

mole $# moles

mass $# mass
volume $.

per unit

per unit

per unit

per

The number of atoms per mole is just Avogadro’s number
NA (! 6.02 $ 10 23 mol#1). Moles per unit mass is the inverse
of the  mass  per  mole, which  here  is  the  molar  mass  M of
copper. The mass per unit volume is the (mass) density rmass
of copper. Thus,

n ! NA# 1

M $rmass !

NArmass
M

.

Taking  copper’s  molar  mass  M and  density  rmass from
Appendix F, we then have (with some conversions of units)

n !

(6.02 $ 10 23 mol#1)(8.96 $ 10 3 kg/m3)
63.54 $ 10 #3 kg/mol

! 8.49 $ 10 28 electrons/m3

or

n ! 8.49 $ 10 28 m#3.

Next let us combine the first two key ideas by writing

i
A

! nevd.

Substituting for A with pr 2 (! 2.54 $ 10 #6 m2) and solving
for vd, we then find

vd !

i
ne(pr2)

!

17 $ 10 #3 A
(8.49 $ 10 28 m#3)(1.6 $ 10 #19 C)(2.54 $ 10 #6 m2)
(Answer)

! 4.9 $ 10 #7 m/s,

which is only 1.8 mm/h, slower than a sluggish snail.

Lights are fast: You may well ask: “If the electrons drift so
slowly, why do the room lights turn on so quickly when I throw
the switch?” Confusion on this point results from not distin-
guishing  between  the  drift  speed  of  the  electrons  and  the
speed  at which  changes in  the  electric  field  configuration
travel along wires. This latter speed is nearly that of light; elec-
trons everywhere in the wire begin drifting almost at once, in-
cluding into the lightbulbs. Similarly, when you open the valve
on  your  garden  hose  with  the  hose  full  of  water, a  pressure
wave  travels  along  the  hose  at  the  speed  of  sound  in  water.
The speed at which the water itself moves through the hose —
measured perhaps with a dye marker — is much slower.

Additional examples, video, and practice available at WileyPLUS

26-3 RESISTANCE AND RESISTIVITY

Learning Objectives
After reading this module, you should be able to . . .

26.14 Apply the relationship between the potential difference

V applied across an object, the object’s resistance R,
and the resulting current i through the object, between the
application points.
26.15 Identify a resistor.
26.16 Apply the relationship between the electric field magni-
tude E set up at a point in a given material, the material’s
resistivity r, and the resulting current density magnitude
J at that point.

26.17 For a uniform electric field set up in a wire, apply

the potential difference V between the two ends, and
the wire’s length L.

26.18 Apply the relationship between resistivity r and

conductivity s.

26.19 Apply the relationship between an object’s resistance

R, the resistivity of its material r, its length L, and its cross-
sectional area A.

26.20 Apply the equation that approximately gives a

conductor’s resistivity r as a function of temperature T.
26.21 Sketch a graph of resistivity r versus temperature T for

the relationship between the electric field magnitude E,

a metal.

Key Ideas
● The resistance R of a conductor is defined as

R !

V
i

,

where V is the potential difference across the conductor and
i is the current.
● The resistivity r and conductivity s of a material are related by

1
s
where E is the magnitude of the applied electric field and J is
the magnitude of the current density.

r !

E
J

!

,

26-3 R ESISTANCE  AN D  R ESISTIVITY

753

● The resistance R of a conducting wire of length L and
uniform cross section is

,

R ! r

L
A
where A is the cross-sectional area.
● The resistivity r for most materials changes with tempera-
ture. For many materials, including metals, the relation
between r and temperature T is approximated by the
equation

r # r0 ! r0a(T # T0).

● The electric field and current density are related to the
resistivity by

:
E

:
! r J

.

Here T0 is a reference temperature, r0 is the resistivity at
T0, and a is the temperature coefficient of resistivity for the
material.

Resistance and Resistivity
If we apply the same potential difference between the ends of geometrically simi-
lar rods of copper and of glass, very different currents result. The characteristic
of the conductor that enters here is its electrical resistance. We determine the re-
sistance between any two points of a conductor by applying a potential difference
V between those points and measuring the current i that results. The resistance R
is then

R !

V
i

(definition of R).

(26-8)

The SI unit for resistance that follows from Eq. 26-8 is the volt per ampere.This com-
bination occurs so often that we give it a special name, the ohm (symbol 0); that is,

 1 ohm ! 1 0 ! 1 volt per ampere

! 1 V/A.

(26-9)

A  conductor  whose  function  in  a  circuit  is  to  provide  a  specified  resistance  is
called a resistor (see Fig. 26-7). In a circuit diagram, we represent a resistor and
a resistance with the symbol

. If we write Eq. 26-8 as

s
k
r
o
W
e
g
a
m

I

e
h
T

i !

V
R

,

we see that, for a given V, the greater the resistance, the smaller the current.

The resistance of a conductor depends on the manner in which the potential
difference is applied to it. Figure 26-8, for example, shows a given potential dif-
ference  applied  in  two  different  ways  to  the  same  conductor. As  the  current
density streamlines suggest, the currents in the two cases — hence the measured
resistances — will be different. Unless otherwise stated, we shall assume that any
given potential difference is applied as in Fig. 26-8b.

(a )

(b )

Figure 26-8 Two ways of applying a potential difference to a conducting rod. The gray
connectors are assumed to have negligible resistance. When they are arranged as in
(a) in a small region at each rod end, the measured resistance is larger than when they
are arranged as in (b) to cover the entire rod end.

Figure 26-7 An assortment of resistors. The
circular bands are color-coding marks
that identify the value of the resistance.

754

CHAPTE R  26 CU R R E NT  AN D  R ESISTANCE

Table 26-1 Resistivities of Some Materials
at Room Temperature (20/C)

Material

Resistivity, r
(0&m)

Temperature
Coefficient
of Resistivity,
a (K#1)

Typical Metals
1.62 $ 10 #8
Silver
1.69 $ 10 #8
Copper
2.35 $ 10 #8
Gold
Aluminum 2.75 $ 10 #8
4.82 $ 10 #8
Manganina
5.25 $ 10 #8
Tungsten
9.68 $ 10 #8
Iron
10.6 $ 10 #8
Platinum

4.1 $ 10 #3
4.3 $ 10 #3
4.0 $ 10 #3
4.4 $ 10 #3
0.002 $ 10 #3
4.5 $ 10 #3
6.5 $ 10 #3
3.9 $ 10 #3

Typical Semiconductors

2.5 $ 10 3

#70 $ 10 #3

8.7 $ 10 #4

2.8 $ 10 #3

Typical Insulators
10 10#10 14

Silicon,
pure
Silicon,
n-typeb
Silicon,

p-typec

Glass
Fused

As we have done several times in other connections, we often wish to take a
general view and deal not with particular objects but with materials. Here we do
so by focusing not on the potential difference V across a particular resistor but on
at a point in a resistive material. Instead of dealing with the
the electric field
current i through the resistor, we deal with the current density
at the point in
question. Instead of the resistance R of an object, we deal with the resistivity r of
the material:

:
E

:
J

r !

E
J

(definition of r).

(26-10)

(Compare this equation with Eq. 26-8.)

If we combine the SI units of E and J according to Eq. 26-10, we get, for the

unit of r, the ohm-meter (0&m):

unit (E)
unit (J)

V/m
A/m2 !
(Do not confuse the ohm-meter, the unit of resistivity, with the ohmmeter, which
is  an  instrument  that  measures  resistance.)  Table  26-1  lists  the  resistivities  of
some materials.

 m ! 0&m.

V
A

!

We can write Eq. 26-10 in vector form as

:
E

:
! r J
.

(26-11)

Equations  26-10  and  26-11  hold  only  for  isotropic materials — materials  whose
electrical properties are the same in all directions.

We often speak of the conductivity s of a material. This is simply the recipro-

quartz

.10 16

cal of its resistivity, so

aAn alloy specifically designed to have a small
value of a.
bPure silicon doped with phosphorus impurities
to a charge carrier density of 10 23 m#3.
cPure silicon doped with aluminum impurities to
a charge carrier density of 10 23 m#3.

s !

1
r

(definition of s).

(26-12)

The SI unit of conductivity is the reciprocal ohm-meter, (0&m)#1. The unit name
mhos per meter is sometimes used (mho is ohm backwards). The definition of s
allows us to write Eq. 26-11 in the alternative form

:
J

:
! sE
.

(26-13)

Calculating Resistance from Resistivity
We have just made an important distinction:

Resistance is a property of an object. Resistivity is a property of a material.

If  we  know  the  resistivity  of  a  substance  such  as  copper, we  can  calculate  the
resistance of a length of wire made of that substance. Let A be the cross-sectional
area of the wire, let L be its length, and let a potential difference V exist between
its  ends  (Fig. 26-9). If  the  streamlines  representing  the  current  density  are
uniform  throughout  the  wire, the  electric  field  and  the  current  density  will
be constant for all points within the wire and, from Eqs. 24-42 and 26-5, will have
the values

E ! V/L and J ! i/A.

(26-14)

We can then combine Eqs. 26-10 and 26-14 to write

r !

E
J

!

V/L
i/A

.

(26-15)

Current is driven by
a potential difference.

L

i

i

A

V
Figure 26-9 A potential difference V is applied
between the ends of a wire of length L and
cross section A, establishing a current i.

26-3 R ESISTANCE  AN D  R ESISTIVITY

755

However, V/i is the resistance R, which allows us to recast Eq. 26-15 as

R ! r

L
A

.

(26-16)

Equation  26-16  can  be  applied  only  to  a  homogeneous  isotropic  conductor  of
uniform cross section, with the potential difference applied as in Fig. 26-8b.

The macroscopic quantities V, i, and R are of greatest interest when we are
making electrical measurements on specific conductors. They are the quantities
that we read directly on meters. We turn to the microscopic quantities E, J, and r
when we are interested in the fundamental electrical properties of materials.

Checkpoint 3

The figure here shows three cylindrical copper conductors along with their face areas
and lengths. Rank them according to the current through them, greatest first, when
the same potential difference V is placed across their lengths.

L

A

1.5L

L/2

A_
2

A_
2

(a)

(b)

(c)

Variation with Temperature
The values of most physical properties vary with temperature, and resistivity is no
exception. Figure  26-10, for  example, shows  the  variation  of  this  property  for
copper  over  a  wide  temperature  range. The  relation  between  temperature  and
resistivity for copper — and for metals in general — is fairly linear over a rather
broad  temperature  range. For  such  linear  relations  we  can  write  an  empirical
approximation that is good enough for most engineering purposes:

r # r0 ! r0a(T #T0).

(26-17)

Here T0 is a selected reference temperature and r0 is the resistivity at that temper-
ature. Usually T0 ! 293 K (room temperature), for which r0 ! 1.69 $ 10 #8 0&m
for copper.

Because temperature enters Eq. 26-17 only as a difference, it does not matter
whether you use the Celsius or Kelvin scale in that equation because the sizes of
degrees  on  these  scales  are  identical. The  quantity  a in  Eq. 26-17, called  the
temperature  coefficient  of  resistivity, is  chosen  so  that  the  equation  gives  good
agreement with experiment for temperatures in the chosen range. Some values of
a for metals are listed in Table 26-1.

Resistivity can depend
on temperature.

.

)
m
Ω
8
–
0
1
(

y
t
i
v
i
t
s
i
s
e
R

10

8

6

4

2

0

e
r
u
t
a
r
e
p
m
e
t

m
o
o
R

(T0, 0)
ρ

0

200  400  600  800  1000 1200
Temperature (K)

Figure 26-10 The resistivity of copper as a function of temperature. The dot on the curve
marks a convenient reference point at temperature T0 ! 293 K and resistivity r0 ! 1.69 $
10 #8 0&m.
