Substituting this and Eq. 30-23 into Eq. 30-20 (without the
minus sign) and solving for E yield
dB
dt

(Answer)

(30-27)

R2
2r

E !

.

30-4 I N DUCTORS  AN D  I N DUCTANCE

879

Equations  30-25  and  30-27  give  the  same  result  for
r ! R. Figure 30-12 shows a plot of E(r). Note that the in-
side and outside plots meet at r ! R.

Because E is not zero here, we know that an electric field is
induced  even  at  points  that  are  outside  the  changing  mag-
netic  field, an  important  result  that  (as  you  will  see  in
Module 31-6) makes transformers possible.

With the given data, Eq. 30-27 yields the magnitude of

at r ! 12.5 cm:

:
E

E !

(8.5 $ 10 %2 m)2
(2)(12.5 $ 10 %2 m)

 (0.13 T/s)

6

4

2

)
m
/
V
m
(
E

0

0

10

20
r  (cm)

30

40

! 3.8 $ 10 %3 V/m ! 3.8 mV/m.

(Answer)

Figure 30-12 A plot of the induced electric field E(r).

Additional examples, video, and practice available at WileyPLUS

30-4 INDUCTORS AND INDUCTANCE

Learning Objectives
After reading this module, you should be able to . . .

30.19 Identify an inductor.
30.20 For an inductor, apply the relationship between

inductance L, total flux N0, and current i.

Key Ideas
● An inductor is a device that can be used to produce a known
magnetic field in a specified region. If a current i is established
through each of the N windings of an inductor, a magnetic flux
0B links those windings. The inductance L of the inductor is

L !

N 0B
i

(inductance defined).

30.21 For a solenoid, apply the relationship between the

inductance per unit length L/l, the area A of each turn,
and the number of turns per unit length n.

● The SI unit of inductance is the henry (H), where 1 henry
1 H ! 1 T ) m2/A.
● The inductance per unit length near the middle of a long so-
lenoid of cross-sectional area A and n turns per unit length is

!

L
l

! m0 n2A

(solenoid).

Inductors and Inductance
We found in Chapter 25 that a capacitor can be used to produce a desired elec-
tric field. We considered the parallel-plate arrangement as a basic type of ca-
pacitor. Similarly, an inductor (symbol
) can be used to produce a desired
magnetic  field. We  shall  consider  a  long  solenoid  (more  specifically, a  short
length near the middle of a long solenoid, to avoid any fringing effects) as our
basic type of inductor.

If  we  establish  a  current  i in  the  windings  (turns)  of  the  solenoid  we  are
taking  as  our  inductor, the  current  produces  a  magnetic  flux  0B through  the
central region of the inductor. The inductance of the inductor is then defined in
terms of that flux as

L !

N0B
i

(inductance defined),

(30-28)

880

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

The Royal Institution/Bridgeman Art Library/NY

The crude inductors with which Michael
Faraday discovered the law of induction. In
those days amenities such as insulated wire
were not commercially available. It is said
that Faraday insulated his wires by wrap-
ping them with strips cut from one of his
wife’s petticoats.

in which N is the number of turns. The windings of the inductor are said to be
linked by the shared flux, and the product N0B is called the magnetic flux linkage.
The inductance L is thus a measure of the flux linkage produced by the inductor
per unit of current.

Because the SI unit of magnetic flux is the tesla – square meter, the SI unit of
inductance  is  the  tesla – square  meter  per  ampere  (T )m2/A). We  call  this  the
henry (H), after American physicist Joseph Henry, the codiscoverer of the law of
induction and a contemporary of Faraday. Thus,

1 henry ! 1 H ! 1 T )m2/A.

(30-29)

Through  the  rest  of  this  chapter  we  assume  that  all  inductors, no  matter  what
their  geometric  arrangement, have  no  magnetic  materials  such  as  iron  in  their
vicinity. Such materials would distort the magnetic field of an inductor.

Inductance of a Solenoid
Consider  a  long  solenoid  of  cross-sectional  area  A. What  is  the  inductance
per unit  length  near  its  middle?  To  use  the  defining  equation  for  inductance
(Eq. 30-28), we must calculate the flux linkage set up by a given current in the so-
lenoid  windings. Consider  a  length  l near  the  middle  of  this  solenoid. The  flux
linkage there is

N0B ! (nl)(BA),

in  which  n is  the  number  of  turns  per  unit  length  of  the  solenoid  and  B is  the
magnitude of the magnetic field within the solenoid.

The magnitude B is given by Eq. 29-23,

and so from Eq. 30-28,

B ! m0in,

L !

!

N0B
i
! m0 n2 lA.

(nl)(BA)
i

!

(nl)(m 0 in)(A)
i

(30-30)

Thus, the inductance per unit length near the center of a long solenoid is

L
l

! m0 n2A

(solenoid).

(30-31)

Inductance — like  capacitance — depends  only  on  the  geometry  of  the  device.
The dependence on the square of the number of turns per unit length is to be
expected. If you, say, triple n, you not only triple the number of turns (N) but you
also triple the flux (0B ! BA ! m0inA) through each turn, multiplying the flux
linkage N0B and thus the inductance L by a factor of 9.

If the solenoid is very much longer than its radius, then Eq. 30-30 gives its
inductance to a good approximation. This approximation neglects the spreading
of the magnetic field lines near the ends of the solenoid, just as the parallel-plate
capacitor formula (C ! ´0A/d) neglects the fringing of the electric field lines near
the edges of the capacitor plates.

From Eq. 30-30, and recalling that n is a number per unit length, we can see
that an inductance can be written as a product of the permeability constant m0
and  a  quantity  with  the  dimensions  of  a  length. This  means  that  m0 can  be  ex-
pressed in the unit henry per meter:

m0 ! 4p $ 10 %7 T )m/A
! 4p $ 10 %7 H/m.

(30-32)

The latter is the more common unit for the permeability constant.
