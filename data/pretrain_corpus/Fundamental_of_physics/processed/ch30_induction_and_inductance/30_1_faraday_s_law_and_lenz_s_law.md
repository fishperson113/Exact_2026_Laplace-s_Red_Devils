C H A

P

T

E

R

3

0

Induction and Inductance

30-1 FARADAY’S LAW AND LENZ’S LAW

Learning Objectives
After reading this module, you should be able to . . .

30.01 Identify that the amount of magnetic field piercing a

30.06 Identify that an induced current in a conducting loop

surface (not skimming along the surface) is the magnetic
flux 0 through the surface.

30.02 Identify that an area vector for a flat surface is a vector
that is perpendicular to the surface and that has a magni-
tude equal to the area of the surface.

30.03 Identify that any surface can be divided into area ele-
ments (patch elements) that are each small enough and
flat enough for an area vector
to be assigned to it, with
the vector perpendicular to the element and having a mag-
nitude equal to the area of the element.

:
dA

30.04 Calculate the magnetic flux 0 through a surface by
integrating the dot product of the magnetic field vector
and the area vector
face, in magnitude-angle notation and unit-vector notation.

:
B
(for patch elements) over the sur-

:
dA

is driven by an induced emf.

30.07 Apply Faraday’s law, which is the relationship between
an induced emf in a conducting loop and the rate at which
magnetic flux through the loop changes.

30.08 Extend Faraday’s law from a loop to a coil with multiple

loops.

30.09 Identify the three general ways in which the magnetic

flux through a coil can change.

30.10 Use a right-hand rule for Lenz’s law to determine
the direction of induced emf and induced current in a
conducting loop.

30.11 Identify that when a magnetic flux through a loop
changes, the induced current in the loop sets up a
magnetic field to oppose that change.

30.05 Identify that a current is induced in a conducting loop

while the number of magnetic field lines intercepted by the
loop is changing.

30.12 If an emf is induced in a conducting loop containing
a battery, determine the net emf and calculate the corre-
sponding current in the loop.

Key Ideas
● The magnetic flux 0B through an area A in a magnetic field
:
B

is defined as

0B ! " B

:

:
! dA

,

where the integral is taken over the area. The SI unit of
magnetic flux is the weber, where 1 Wb ! 1 T )m2.
● If

is perpendicular to the area and uniform over it, the flux is

:
B

an emf are produced in the loop; this process is called
induction. The induced emf is
d 0B
dt

(Faraday’s law).

# ! %

● If the loop is replaced by a closely packed coil of N turns, the
induced emf is

# ! %N

d 0B
dt

.

0B ! BA

: " A, B
(B

:

uniform).

● If the magnetic flux 0B through an area bounded by a
closed conducting loop changes with time, a current and

● An induced current has a direction such that the magnetic
field due to the current opposes the change in the magnetic
flux that induces the current. The induced emf has the same
direction as the induced current.

What Is Physics?
In Chapter 29 we discussed the fact that a current produces a magnetic field. That
fact  came  as  a  surprise  to  the  scientists  who  discovered  the  effect. Perhaps  even
more  surprising  was  the  discovery  of  the  reverse  effect: A  magnetic  field  can
produce an electric field that can drive a current. This link between a magnetic field
and the electric field it produces (induces) is now called Faraday’s law of induction.

864

30-1 FARADAY’S  L AW  AN D  LE N Z’S  L AW

865

The observations by Michael Faraday and other scientists that led to this law
were at first just basic science. Today, however, applications of that basic science
are almost everywhere. For example, induction is the basis of the electric guitars
that revolutionized early rock and still drive heavy metal and punk today. It is
also the basis of the electric generators that power cities and transportation lines
and  of  the  huge  induction  furnaces  that  are  commonplace  in  foundries  where
large amounts of metal must be melted rapidly.

Before we get to applications like the electric guitar, we must examine two

simple experiments about Faraday’s law of induction.

Two Experiments
Let us examine two simple experiments to prepare for our discussion of Faraday’s
law of induction.

First Experiment. Figure 30-1 shows a conducting loop connected to a sensitive
ammeter. Because there is no battery or other source of emf included, there is no
current in the circuit. However, if we move a bar magnet toward the loop, a current
suddenly appears in the circuit.The current disappears when the magnet stops. If we
then move the magnet away, a current again suddenly appears, but now in the oppo-
site direction. If we experimented for a while, we would discover the following:

1. A current appears only if there is relative motion between the loop and the
magnet  (one  must  move  relative  to  the  other); the  current  disappears  when
the relative motion between them ceases.
2. Faster motion produces a greater current.
3. If  moving  the  magnet’s  north  pole  toward  the  loop  causes, say, clockwise
current, then  moving  the  north  pole  away  causes  counterclockwise  current.
Moving the south pole toward or away from the loop also causes currents, but
in the reversed directions.

The current produced in the loop is called an induced current; the work done
per unit charge to produce that current (to move the conduction electrons that
constitute the current) is called an induced emf; and the process of producing the
current and emf is called induction.

Second Experiment. For this experiment we use the apparatus of Fig. 30-2,
with the two conducting loops close to each other but not touching. If we close
switch  S, to  turn  on  a  current  in  the  right-hand  loop, the  meter  suddenly  and
briefly  registers  a  current — an  induced  current — in  the  left-hand  loop. If  we
then  open  the  switch, another  sudden  and  brief  induced  current  appears  in
the left-hand loop, but in the opposite direction. We get an induced current (and
thus an induced emf) only when the current in the right-hand loop is changing
(either turning on or turning off) and not when it is constant (even if it is large).
The induced emf and induced current in these experiments are apparently
caused when something changes — but what is that “something”? Faraday knew.

Faraday’s Law of Induction
Faraday realized that an emf and a current can be induced in a loop, as in our
two experiments, by changing the amount of magnetic field passing through the
loop. He further realized that the “amount of magnetic field” can be visualized
in terms of the magnetic field lines passing through the loop. Faraday’s law of
induction, stated in terms of our experiments, is this:

An emf is induced in the loop at the left in Figs. 30-1 and 30-2 when the number
of magnetic field lines that pass through the loop is changing.

The magnet’s motion
creates a current in
the loop.

S

N

Figure 30-1 An ammeter registers a current
in the wire loop when the magnet is moving
with respect to the loop.

+

–

S

Closing the switch
causes a current in
the left-hand loop.

Figure 30-2 An ammeter registers a current
in the left-hand wire loop just as switch S is
closed (to turn on the current in the right-
hand wire loop) or opened (to turn off the
current in the right-hand loop). No motion
of the coils is involved.

866

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

The actual number of field lines passing through the loop does not matter; the
values  of  the  induced  emf  and  induced  current  are  determined  by  the  rate at
which that number changes.

In our first experiment (Fig. 30-1), the magnetic field lines spread out from
the north pole of the magnet. Thus, as we move the north pole closer to the loop,
the number of field lines passing through the loop increases. That increase appar-
ently causes conduction electrons in the loop to move (the induced current) and
provides energy (the induced emf) for their motion. When the magnet stops mov-
ing, the number of field lines through the loop no longer changes and the induced
current and induced emf disappear.

In our second experiment (Fig. 30-2), when the switch is open (no current),
there are no field lines. However, when we turn on the current in the right-hand
loop, the increasing current builds up a magnetic field around that loop and at the
left-hand loop. While the field builds, the number of magnetic field lines through
the left-hand loop increases. As in the first experiment, the increase in field lines
through  that  loop  apparently  induces  a  current  and  an  emf  there. When  the
current in the right-hand loop reaches a final, steady value, the number of field
lines through the left-hand loop no longer changes, and the induced current and
induced emf disappear.

A Quantitative Treatment
To put Faraday’s law to work, we need a way to calculate the amount of magnetic
field that passes through a loop. In Chapter 23, in a similar situation, we needed to
calculate  the  amount  of  electric  field  that  passes  through  a  surface. There  we
:
0E ! " E
. Here we define a magnetic flux: Suppose
defined an electric flux
a loop enclosing an area A is placed in a magnetic field
. Then the magnetic flux
through the loop is

:
! dA

:
B

0B ! " B

:

:
! dA

(magnetic flux through area A).

(30-1)

:
dA

is  a  vector  of  magnitude  dA that  is  perpendicular  to  a
As  in  Chapter  23,
differential  area  dA. As  with  electric  flux, we  want  the  component  of  the  field
that pierces the surface (not skims along it). The dot product of the field and the
area vector automatically gives us that piercing component.

Special Case. As a special case of Eq. 30-1, suppose that the loop lies in a
plane  and  that  the  magnetic  field  is  perpendicular  to  the  plane  of  the  loop.
Then we can write the dot product in Eq. 30-1 as B dA cos 0° ! B dA. If the
magnetic field is also uniform, then B can be brought out in front of the inte-
then gives just the area A of the loop. Thus, Eq.
gral sign. The remaining
30-1 reduces to

" dA

0B ! BA

: " area A, B
(B

:

 uniform).

(30-2)

Unit. From Eqs. 30-1 and 30-2, we see that the SI unit for magnetic flux is the

tesla – square meter, which is called the weber (abbreviated Wb):

1 weber ! 1 Wb ! 1 T )m2.

(30-3)

Faraday’s Law. With the notion of magnetic flux, we can state Faraday’s law

in a more quantitative and useful way:

The magnitude of the emf # induced in a conducting loop is equal to the rate at
which the magnetic flux 0B through that loop changes with time.

As  you  will  see  below, the  induced  emf  # tends  to  oppose  the  flux  change, so

30-1 FARADAY’S  L AW  AN D  LE N Z’S  L AW

867

Faraday’s law is formally written as

# ! %

d0B
dt

(Faraday’s law),

(30-4)

with the minus sign indicating that opposition. We often neglect the minus sign in
Eq. 30-4, seeking only the magnitude of the induced emf.

If  we  change  the  magnetic  flux  through  a  coil  of  N turns, an  induced  emf
appears in every turn and the total emf induced in the coil is the sum of these
individual  induced  emfs. If  the  coil  is  tightly  wound  (closely  packed), so  that
the same magnetic flux 0B passes through all the turns, the total emf induced in
the coil is

# ! %N

d0B
dt

(coil of N turns).

(30-5)

Here  are  the  general  means  by  which  we  can  change  the  magnetic  flux

through a coil:

1. Change the magnitude B of the magnetic field within the coil.
2. Change  either  the  total  area  of  the  coil  or  the  portion  of  that  area  that  lies
within the magnetic field (for example, by expanding the coil or sliding it into
or out of the field).

3. Change the angle between the direction of the magnetic field
of the coil (for example, by rotating the coil so that field
lar to the plane of the coil and then is along that plane).

:
B

:
B

and the plane
is first perpendicu-

Checkpoint 1

The graph gives the magnitude B(t) of a uniform
magnetic field that exists throughout a conduct-
ing loop, with the direction of the field perpendi-
cular to the plane of the loop. Rank the five
regions of the graph according to the magnitude
of the emf induced in the loop, greatest first.

B

a

b

c

d

e

t

Sample Problem 30.01 Induced emf in coil due to a solenoid

The long solenoid S shown (in cross section) in Fig. 30-3 has
220 turns/cm and carries a current i ! 1.5 A; its diameter D
is  3.2 cm. At  its  center  we  place  a  130-turn  closely  packed
coil C of diameter d ! 2.1 cm. The current in the solenoid is
reduced to zero at a steady rate in 25 ms. What is the magni-
tude of the emf that is induced in coil C while the current in
the solenoid is changing?

i

i

S

C

Axis

Figure 30-3 A coil C is located inside a solenoid S, which carries
current i.

KEY IDEAS

1. Because it is located in the interior of the solenoid, coil C
lies within the magnetic field produced by current i in the
solenoid; thus, there is a magnetic flux 0B through coil C.

2. Because current i decreases, flux 0B also decreases.
3. As 0B decreases, emf # is induced in coil C.
4. The flux through each turn of coil C depends on the area
A and orientation of that turn in the solenoid’s magnetic
field
is uniform and directed perpendicular
to area A, the flux is given by Eq. 30-2 (0B ! BA).

. Because

:
B

:
B

5. The magnitude B of the magnetic field in the interior of
a solenoid  depends  on  the  solenoid’s  current  i and  its
number n of turns per unit length, according to Eq. 29-23
(B ! m0in).

868

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

Calculations: Because  coil  C  consists  of  more  than  one
turn, we  apply  Faraday’s  law  in  the  form  of  Eq. 30-5
(# ! %N d0B/dt), where the number of turns N is 130 and
d0B/dt is the rate at which the flux changes.

Because  the  current  in  the  solenoid  decreases  at  a
steady rate, flux 0B also decreases at a steady rate, and so we
can write d0B/dt as ’0B/’t. Then, to evaluate ’0B, we need
the final and initial flux values. The final flux 0B,f is zero be-
cause the final current in the solenoid is zero. To find the ini-
tial flux 0B,i, we note that area A is pd 2 (! 3.464 $ 10 %4 m2)
and the  number  n is  220 turns/cm, or  22 000  turns/m. Sub-
stituting Eq. 29-23 into Eq. 30-2 then leads to

1
4

Now we can write

d0B
dt

!

!

’0B
’t

!

0B, f % 0B,i
’t

(0 % 1.44 $ 10 %5 Wb)
25 $ 10 %3 s

! %5.76 $ 10 %4 Wb/s

! %5.76 $ 10 %4 V.

We are interested only in magnitudes; so we ignore the mi-
nus signs here and in Eq. 30-5, writing

0B, i ! BA ! (m0 in)A

! (4p $ 10 %7 T )m /A)(1.5 A)(22 000 turns/m)

# ! N

d0B
dt

! (130 turns)(5.76 $ 10 %4 V)

$ (3.464 $ 10 %4 m2)

! 1.44 $ 10 %5 Wb.

! 7.5 $ 10 %2 V

! 75 mV.

(Answer)

Additional examples, video, and practice available at WileyPLUS

Lenz’s Law
Soon  after  Faraday  proposed  his  law  of  induction, Heinrich  Friedrich  Lenz
devised a rule for determining the direction of an induced current in a loop:

An induced current has a direction such that the magnetic field due to the current
opposes the change in the magnetic flux that induces the current.

Furthermore, the direction of an induced emf is that of the induced current. The
key word in Lenz’s law is “opposition.” Let’s apply the law to the motion of the
north pole toward the conducting loop in Fig. 30-4.

The magnet’s motion
creates a magnetic
dipole that opposes
the motion.

S

N
N

µµ

i

S

Figure 30-4 Lenz’s law at work. As the mag-
net is moved toward the loop, a current is
induced in the loop. The current produces
its own magnetic field, with magnetic di-
pole moment  oriented so as to oppose
the motion of the magnet. Thus, the in-
duced current must be counterclockwise
as shown.

m:

m:

1. Opposition to Pole Movement. The approach of the magnet’s north pole in
Fig. 30-4 increases the magnetic flux through the loop and thereby induces a
current  in  the  loop. From  Fig. 29-22, we  know  that  the  loop  then  acts  as  a
magnetic  dipole  with  a  south  pole  and  a  north  pole, and  that  its  magnetic
is directed from south to north. To oppose the magnetic
dipole moment
flux increase being caused by the approaching magnet, the loop’s north pole
) must face toward the approaching north pole so as to repel it
(and thus
(Fig. 30-4). Then the curled – straight right-hand rule for
(Fig. 29-22) tells
us that the current induced in the loop must be counterclockwise in Fig. 30-4.
If  we  next  pull  the  magnet  away  from  the  loop, a  current  will  again  be
induced  in  the  loop. Now, however, the  loop  will  have  a  south  pole  facing
the retreating north pole of the magnet, so as to oppose the retreat. Thus, the
induced current will be clockwise.

m:

m:

2. Opposition to Flux Change. In Fig. 30-4, with the magnet initially distant, no
magnetic flux passes through the loop. As the north pole of the magnet then
:
directed downward, the flux through
B
nears the loop with its magnetic field
the loop increases. To oppose this increase in flux, the induced current i must
directed upward inside the loop, as shown in Fig. 30-5a;
set up its own field
then  the  upward  flux  of  field
opposes  the  increasing  downward  flux  of
. The curled – straight right-hand rule of Fig. 29-22 then tells us that i
field
must be counterclockwise in Fig. 30-5a.

:
B

:
B

:
B

ind

ind

30-1 FARADAY’S  L AW  AN D  LE N Z’S  L AW

869

:
B

ind

ind
is not always opposite

always  opposes  the  change in  the  flux  of
Heads  Up. The  flux  of
, but
:
:
B
B
. For example, if we next pull the magnet away
from the loop in Fig. 30-4, the magnet’s flux  B is still downward through the
must now be downward inside
loop, but it is now decreasing. The flux of
:
B
the loop, to oppose that decrease (Fig. 30-5b). Thus,
are now in the
same direction. In Figs. 30-5c and d, the south pole of the magnet approaches
and retreats from the loop, again with opposition to change.

and

:
B

:
B

0

ind

ind

:
B

Increasing the external
field B induces a current
with a field Bind that
opposes the change.

Decreasing the external
field B induces a current
with a field Bind that
opposes the change.

Increasing the external
field B induces a current
with a field Bind that
opposes the change.

Decreasing the external
field B induces a current
with a field Bind that
opposes the change.

A

The induced
current creates
this field, trying
to offset the
change.

The fingers are
in the current's
direction; the
thumb is in the
induced field's
direction.

Bind

B

Bind

B

Bind

i

i

i

B

(a)

i

i

i

B

Bind

B

Bind

B

Bind

(b)

i

i

i

B

Bind

B

Bind

B

Bind

(c)

Bind

B

Bind

B

Bind

B

i

i

i

(d)

opposes the change in the magnetic

Figure 30-5 The direction of the current i induced in a loop is such that the current’s magnetic field
field
:
B

inducing i. The field
. The curled – straight right-hand rule gives the direction of the induced current based on the direction of the induced field.

is always directed opposite an increasing field

and in the same direction as a decreasing field

:
B
(b, d )

(a, c)

:
B

:
B

ind

ind

:
B

Checkpoint 2

The figure shows three situations in which identical circular
conducting loops are in uniform magnetic fields that are either
increasing (Inc) or decreasing (Dec) in magnitude at identical rates.
In each, the dashed line coincides with a diameter. Rank the situa-
tions according to the magnitude of the current induced in the loops,
greatest first.

Inc

Inc

(a)

Inc

Dec

(b)

Dec

Inc

(c)

870

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

Sample Problem 30.02 Induced emf and current due to a changing uniform B field

Figure 30-6 shows a conducting loop consisting of a half-circle
of  radius  r ! 0.20 m  and  three  straight  sections. The  half-
circle  lies in a uniform magnetic field
that is directed out
of the page; the  field  magnitude  is  given  by  B ! 4.0t2 &
2.0t & 3.0, with B in teslas and t in seconds. An ideal battery
with emf #bat ! 2.0 V is connected to the loop. The resistance
of the loop is 2.0 1.

:
B

(a) What  are  the  magnitude  and  direction  of  the  emf  #ind
induced around the loop by field  at t ! 10 s?

:
B

KEY IDEAS

1. According  to  Faraday’s  law, the  magnitude  of  #ind is
equal  to  the  rate  d0B/dt at  which  the  magnetic  flux
through the loop changes.

2. The flux through the loop depends on how much of the
loop’s  area  lies  within  the  flux  and  how  the  area  is  ori-
:
B
.
ented in the magnetic field

:
B

3. Because

is uniform and is perpendicular to the plane
of the  loop, the  flux  is  given  by  Eq. 30-2  (0B ! BA).
(We don’t  need  to  integrate  B over  the  area  to  get
the flux.)

4. The induced field Bind (due to the induced current) must

always oppose the change in the magnetic flux.

Magnitude: Using Eq. 30-2 and realizing that only the field
magnitude B changes in time (not the area A), we rewrite
Faraday’s law, Eq. 30-4, as

# ind !

d 0B
dt

!

d(BA)
dt

! A

dB
dt

.

Because  the  flux  penetrates  the  loop  only  within  the  half-
circle, the  area  A in  this  equation  is
. Substituting  this
and the given expression for B yields

2p r2

1

e ind ! A

dB
dt

!

p r2
2

d
dt

 (4.0t 2 & 2.0t & 3.0)

!

p r2
2

 (8.0t & 2.0).

r

r/2

–  +

bat

Figure 30-6 A battery is connected to a conducting loop that
includes a half-circle of radius r lying in a uniform magnetic
field. The field is directed out of the page; its magnitude is
changing.

At t ! 10 s, then,

# ind !

p (0.20 m)2
2
! 5.152 V % 5.2 V.

 [8.0(10) & 2.0]

(Answer)

Direction: To find the direction of #ind, we first note that in
Fig. 30-6 the flux through the loop is out of the page and in-
creasing. Because the induced field Bind (due to the induced
current) must oppose that increase, it must be into the page.
Using the curled – straight right-hand rule (Fig. 30-5c), we find
that  the  induced  current  is  clockwise  around  the  loop, and
thus so is the induced emf #ind.
(b) What is the current in the loop at t ! 10 s?

KEY IDEA

The  point  here  is  that  two emfs  tend  to  move charges
around the loop.

Calculation: The induced emf #ind tends to drive a current
clockwise  around  the  loop; the  battery’s  emf #bat tends  to
drive  a  current  counterclockwise. Because  #ind is greater
than #bat, the  net  emf  #net is  clockwise, and  thus  so is the
current. To  find  the  current  at  t ! 10 s, we  use  Eq. 27-2
(i ! #/R):

i !

!

!

e ind % e bat
R

e net
R
5.152 V % 2.0 V
2.0 1

! 1.58 A % 1.6 A.

(Answer)

Sample Problem 30.03 Induced emf due to a changing nonuniform B field

:
B

Figure 30-7 shows a rectangular loop of wire immersed in a
nonuniform and varying magnetic field
that is perpendi-
cular to and directed into the page. The field’s magnitude is
given  by  B ! 4t2x2, with  B in  teslas, t in  seconds, and  x in
meters. (Note  that  the  function  depends  on  both time  and
position.)  The loop  has  width  W ! 3.0 m  and  height  H !
2.0 m. What are the magnitude and direction of the induced
emf # around the loop at t ! 0.10 s?

KEY IDEAS

1. Because the magnitude of the magnetic field

is chang-
ing  with  time, the  magnetic  flux  0B through  the  loop  is
also changing.

:
B

2. The changing flux induces an emf # in the loop according

to Faraday’s law, which we can write as # ! d0B/dt.

3. To use that law, we need an expression for the flux 0B at
