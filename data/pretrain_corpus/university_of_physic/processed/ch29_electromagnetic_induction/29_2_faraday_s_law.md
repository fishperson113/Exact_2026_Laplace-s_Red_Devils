deformation, not before or after. When we increase the area to return the
coil  to  its  original  shape,  there  is  current  in  the  opposite  direction,  but
only while the area of the coil is changing.

5. If  we  rotate  the  coil  a  few  degrees  about  a  horizontal  axis,  the  meter
detects  current  during  the  rotation,  in  the  same  direction  as  when  we
decreased the area. When we rotate the coil back, there is a current in the
opposite direction during this rotation.

6. If we jerk the coil out of the magnetic ﬁeld, there is a current during the

motion, in the same direction as when we decreased the area.

7. If we decrease the number of turns in the coil by unwinding one or more
turns,  there  is  a  current  during  the  unwinding,  in  the  same  direction  as
when we decreased the area. If we wind more turns onto the coil, there is
a current in the opposite direction during the winding.

8. When the magnet is turned off, there is a momentary current in the direc-

tion opposite to the current when it was turned on.

9. The faster we carry out any of these changes, the greater the current.
10. If all these experiments are repeated with a coil that has the same shape
but different material and different resistance, the current in each case is
inversely proportional to the total circuit resistance. This shows that the
induced emfs that are causing the current do not depend on the material of
the coil but only on its shape and the magnetic ﬁeld.

29.2 Faraday’s Law

959

29.2 A coil in a magnetic ﬁeld. When the
S
ﬁeld is constant and the shape, location,
B
and orientation of the coil do not change, no
current is induced in the coil. A current is
induced when any of these factors change.

S
B

S

N

0
0

The common element in all these experiments is changing magnetic ﬂux
£B
through  the  coil  connected  to  the  galvanometer.  In  each  case  the  ﬂux
changes either because the magnetic ﬁeld changes with time or because the coil
is moving through a nonuniform magnetic ﬁeld. Faraday’s law of induction, the
subject of the next section, states that in all of these situations the induced emf is
through  the  coil.  The
proportional  to  the  rate  of  change of  magnetic  ﬂux
direction of  the  induced  emf  depends  on  whether  the  ﬂux  is  increasing  or
decreasing. If the ﬂux is constant, there is no induced emf.

?

£B

Induced emfs are not mere laboratory curiosities but have a tremendous num-
ber  of  practical  applications.  If  you  are  reading  these  words  indoors,  you  are
making  use  of  induced  emfs  right  now! At  the  power  plant  that  supplies  your
neighborhood,  an  electric  generator  produces  an  emf  by  varying  the  magnetic
ﬂux  through  coils  of  wire.  (In  the  next  section  we’ll  see  in  detail  how  this  is
done.) This emf supplies the voltage between the terminals of the wall sockets in
your home, and this voltage supplies the power to your reading lamp. Indeed, any
appliance that you plug into a wall socket makes use of induced emfs.

Magnetically induced emfs, just like the emfs discussed in Section 25.4, are
the result of nonelectrostatic forces. We have to distinguish carefully between the
electrostatic  electric  ﬁelds  produced  by  charges  (according  to  Coulomb’s  law)
and  the  nonelectrostatic  electric  ﬁelds  produced  by  changing  magnetic  ﬁelds.
We’ll return to this distinction later in this chapter and the next.

29.2 Faraday’s Law

29.3 Calculating the magnetic ﬂux
through an area element.

The common element in all induction effects is changing magnetic flux through
a  circuit.  Before  stating  the  simple  physical  law  that  summarizes  all  of  the
kinds of experiments described in Section 29.1, let’s first review the concept of
(which we introduced in Section 27.3). For an infinitesimal-
magnetic flux
d£B
area  element
in  a  magnetic  field
through the area is

(Fig.  29.3),  the  magnetic  flux

£B
S
dA

S
B

S # dA

S

d£B = B

= B(cid:2) dA = B dA cos f

f

B'

S
B

S
dA

Bi

dA

where
f
and

B(cid:2)
is the angle between

is the component of  perpendicular to the surface of the area element
(As in Chapter 27, be careful to distinguish

S
dA

S
B

.

S
B
and

S
Magnetic flux through element of area dA:

S

S

dF
B

5 B • dA 5 B(cid:2)dA 5 B dAcos f

960

CHAPTER 29 Electromagnetic Induction

29.4 Calculating the ﬂux of a uniform magnetic ﬁeld through a ﬂat area. (Compare to Fig. 22.6, which shows the rules for calculating
the ﬂux of a uniform electric ﬁeld.)

S

S

Surface is face-on to magnetic field:
S
• B and A are parallel (the angle between B
   and A is f 50).
•  The magnetic flux F

5 B • A 5 BA.

S S

S

B

Surface is tilted from a face-on orientation
by an angle f:
•  The angle between B and A is f.
•  The magnetic flux F

5 B • A 5 BA cos f.

S S

S

S

B

S

S

S

Surface is edge-on to magnetic field:
• B and A are perpendicular (the angle
   between B and A is f 590°).
•  The magnetic flux
S S
   F

5 B • A 5 BA cos 90° 5 0.

S

B

S
B

f 5 0

S
A

S
B

S
A

f

S
B

A

A

S
A

f 5 90°

A

between  two  quantities  named  “phi,”
through a ﬁnite area is the integral of this expression over the area:

and

The  total  magnetic  ﬂux

f

£B.2

£B

£B =

S
B

If

is uniform over a ﬂat area

L
S
A

,

S # dA

B

S

then

S # A

S

£B = B

=

L

B dA cos f

= BA cos f

(29.1)

(29.2)

Figure 29.4 reviews the rules for using Eq. (29.2).

S

S
dA

or

CAUTION Choosing the direction of
SA
In Eqs. (29.1) and (29.2) we have to be
careful to deﬁne the direction of the vector area
or  unambiguously. There are always
dA
two directions perpendicular to any given area, and the sign of the magnetic ﬂux through
the area depends on which one we choose to be positive. For example, in Fig. 29.3 we
is positive. We could have cho-
chose
90°
sen instead to have
90°
S
and
would have been negative. Either choice is equally good, but once we make a
choice we must stick with it. ❙

f
point downward, in which case  would have been greater than

to point upward so
S
dA

S # dA

S # dA

is less than

S
dA

and

S
A

B

B

f

S

Faraday’s law of induction states:

The induced emf in a closed loop equals the negative of the time rate of change of
magnetic ﬂux through the loop.

In symbols, Faraday’s law is

E = -

d£B
dt

    1Faraday’s law of induction)

(29.3)

To understand the negative sign, we have to introduce a sign convention for the
induced emf  But ﬁrst let’s look at a simple example of this law in action.

E.

Example 29.1

Emf and current induced in a loop

The  magnetic  field  between  the  poles  of  the  electromagnet  in
Fig. 29.5 is uniform at any time, but its magnitude is increasing
at the rate of
The area of the conducting loop in the
and  the  total  circuit  resistance,  including  the
field  is

0.020 T>s.

120 cm2,

5.0 Æ.

meter, is
(a) Find the induced emf and the induced current
in the circuit. (b) If the loop is replaced by one made of an insula-
tor,  what  effect  does  this  have  on  the  induced  emf  and  induced
current?

SOLUTION

£B

IDENTIFY  and SET  UP:  The  magnetic  ﬂux
through  the  loop
changes  as  the  magnetic  ﬁeld  changes.  Hence  there  will  be  an
induced emf
and an induced current I in the loop. We calculate
£B
using Eq. (29.2), then ﬁnd  using Faraday’s law. Finally, we
E = IR,
calculate I using
where R is the total resistance of the cir-
cuit that includes the loop.

E

E

S

EXECUTE: (a) The area vector
for the loop is perpendicular to the
S
plane of the loop; we take
to be vertically upward. Then
B
is uniform the magnetic ﬂux through
are parallel, and because
A = 0.012 m2
The area
the loop is
is constant, so the rate of change of magnetic ﬂux is

= BA cos 0 = BA.

S A
A
S
B

£B = B

S # A

and

S
A

S

29.5 A stationary conducting loop in an increasing magnetic ﬁeld.

dB/dt 5 0.020 T/s

S

S
A

I
N

A 5 120 cm2 5 0.012 m2

a

Total resistance in circuit
and meter 5 5.0 V

b

0

29.2 Faraday’s Law

961

d£B
dt

=

d1BA2
dt

= dB
dt
= 2.4 * 10-4 V = 0.24 mV

A = 10.020 T>s210.012 m22

This,  apart  from  a  sign  that  we  haven’t  discussed  yet,  is  the
E
. The corresponding induced current is
induced emf
= 2.4 * 10-4 V
5.0 Æ

= 4.8 * 10-5 A = 0.048 mA

I =

R

E

(b) By changing to an insulating loop, we’ve made the resist-
ance  of  the  loop  very  high.  Faraday’s  law,  Eq.  (29.3),  does  not
involve the resistance of the circuit in any way, so the induced emf
does not change. But the current will be smaller, as given by the
equation
. If the loop is made of a perfect insulator with
inﬁnite  resistance,  the  induced  current  is  zero.  This  situation  is
analogous to an isolated battery whose terminals aren’t connected
to anything: An emf is present, but no current ﬂows.

I = E>R

S

implies  that  the  units  of

EVALUATE: Let’s  verify  unit  consistency  in  this  calculation.  One
way  to  do  this  is  to  note  that  the  magnetic-force  relationship
S
S : B
(cid:2) qv
are  the  units  of  force
F
1 T = 11 N2>
divided  by  the  units  of  (charge  times  velocity):
11 C # m>s2.
11 T211 m22 =
The  units  of  magnetic  ﬂux  are  then
1 N # s # m>C,
and  the  rate  of  change  of  magnetic  ﬂux  is
1 N # m>C = 1 J>C = 1 V.
is the volt, as
required by Eq. (29.3). Also recall that the unit of magnetic ﬂux is
the weber (Wb):

1 T # m2 = 1 Wb,

so 1 V = 1 Wb>s.

Thus the unit of

d£B>dt

S
B

Direction of Induced emf
We  can  ﬁnd  the  direction  of  an  induced  emf  or  current  by  using  Eq.  (29.3)
together with some simple sign rules. Here’s the procedure:

Application Exploring the Brain
with Induced emfs
Transcranial magnetic stimulation (TMS) is a
technique for studying the function of various
parts of the brain. A coil held to the subject’s
head carries a varying electric current, and so
produces a varying magnetic ﬁeld. This ﬁeld
causes an induced emf, and that triggers elec-
tric activity in the region of the brain under-
neath the coil. By observing how the TMS
subject responds (for instance, which muscles
move as a result of stimulating a certain part
of the brain), a physician can test for various
neurological conditions.

1. Deﬁne a positive direction for the vector area
2. From the directions of
£B
the  magnetic  ﬂux
several examples.

S
A
and  its  rate  of  change

and the magnetic ﬁeld

.

S
,
B
d£B/dt.

S
A

determine the sign of
Figure  29.6 shows

3. Determine the sign of the induced emf or current. If the ﬂux is increasing, so
is positive, then the induced emf or current is negative; if the ﬂux is

is negative and the induced emf or current is positive.

d£B>dt
decreasing,

d£B>dt

4. Finally, determine the direction of the induced emf or current using your
vector, with
right hand. Curl the ﬁngers of your right hand around the
S
your right thumb in the direction of
If the induced emf or current in the
.
A
circuit is positive, it is in the same direction as your curled ﬁngers; if the
induced emf or current is negative, it is in the opposite direction.

S
A

S
A

In Example 29.1, in which

terclockwise around the loop, as seen from above. Both
this example, so
itive. Hence by Eq. (29.3),
thus clockwise around the loop, as seen from above.

is upward, a positive  would be directed coun-
S
are upward in
B
d£B>dt
is positive; the magnitude B is increasing, so
is pos-
in Example 29.1 is negative. Its actual direction is

£B

and

S
A

E

E

If  the  loop  in  Fig.  29.5 is  a  conductor,  an  induced  current  results  from  this
emf; this current is also clockwise, as Fig. 29.5 shows. This induced current pro-
duces  an  additional  magnetic  ﬁeld  through  the  loop,  and  the  right-hand  rule
described  in  Section  28.6  shows  that  this  ﬁeld  is  opposite in  direction  to  the
increasing ﬁeld produced by the electromagnet. This is an example of a general
rule called Lenz’s law, which says that any induction effect tends to oppose the
change  that  caused  it;  in  this  case  the  change  is  the  increase  in  the  ﬂux  of  the

962

CHAPTER 29 Electromagnetic Induction

29.6 The magnetic ﬂux is becoming (a) more positive, (b) less positive, (c)
more negative, and (d) less negative. Therefore
is increasing in (a) and (d) and
decreasing in (b) and (c). In (a) and (d) the emfs are negative (they are opposite to
the direction of the curled ﬁngers of your right hand when your right thumb points along
S
In (b) and (c) the emfs are positive (in the same direction as the curled ﬁngers).
A

£B

).

(a)

S
B
(increasing)

S
A

f

(b)

S
B
(decreasing)

S
A

f

• Flux is positive (F
• ... and becoming more positive (dF
• Induced emf is negative (E (cid:3) 0).

(cid:2) 0) ...

B

E

B/dt (cid:2) 0).

(c)

S
A

E

f

S
B
(increasing)

• Flux is negative (F
B
• ... and becoming more negative (dF
• Induced emf is positive (E (cid:2) 0).

(cid:3) 0) ...

B/dt (cid:3) 0).

• Flux is positive (F
• ... and becoming less positive (dF
• Induced emf is positive (E (cid:2) 0).

(cid:2) 0) ...

B

E

B/dt (cid:3) 0).

(d)

E

S
A

f

S
B
(decreasing)

• Flux is negative (F
B
• ... and becoming less negative (dF
• Induced emf is negative (E (cid:3) 0).

(cid:3) 0) ...

B/dt (cid:2) 0).

PhET: Faraday’s Electromagnetic Lab
PhET: Faraday’s Law
PhET: Generator

electromagnet’s ﬁeld through the loop. (We’ll study this law in detail in the next
section.)

You should check out the signs of the induced emfs and currents for the list of
experiments in Section 29.1. For example, when the loop in Fig. 29.2 is in a con-
stant ﬁeld and we tilt it or squeeze it to decrease the ﬂux through it, the induced
emf and current are counterclockwise, as seen from above.

CAUTION Induced emfs are caused by changes in ﬂux Since magnetic ﬂux plays a cen-
tral role in Faraday’s law, it’s tempting to think that ﬂux is the cause of induced emf and
that an induced emf will appear in a circuit whenever there is a magnetic ﬁeld in the region
bordered by the circuit. But Eq. (29.3) shows that only a change in ﬂux through a circuit,
not ﬂux itself, can induce an emf in a circuit. If the ﬂux through a circuit has a constant
value, whether positive, negative, or zero, there is no induced emf. ❙

If we have a coil with N identical turns, and if the ﬂux varies at the same rate
through each turn, the total rate of change through all the turns is N times as large
as for a single turn. If
is the ﬂux through each turn, the total emf in a coil with
N turns is

£B

E = - N

d£B
dt

(29.4)

As we discussed in this chapter’s introduction, induced emfs play an essential
role in the generation of electric power for commercial use. Several of the fol-
lowing examples explore different methods of producing emfs by the motion of a
conductor relative to a magnetic ﬁeld, giving rise to a changing ﬂux through a
circuit.

Problem-Solving Strategy 29.1

Faraday’s Law

IDENTIFY the relevant concepts: Faraday’s law applies when there
is  a  changing  magnetic  ﬂux.  To  use  the  law,  identify  an  area
through which there is a ﬂux of magnetic ﬁeld. This will usually be
the area enclosed by a loop made of a conducting material (though
not  always—see  part  (b)  of  Example  29.1).  Identify  the  target
variables.

SET UP the problem using the following steps:
1. Faraday’s law relates the induced emf to the rate of change of
magnetic ﬂux. To calculate this rate of change, you ﬁrst have to
understand  what  is  making  the  ﬂux  change.  Is  the  conductor
moving?  Is  it  changing  orientation?  Is  the  magnetic  ﬁeld
changing? Remember that it’s not the ﬂux itself that counts, but
its rate of change.
S
A

) must be perpendicular to the plane of
the  area.  You  always  have  two  choices  of  its  direction;  for
could point up or
example, if the area is in a horizontal plane,

2. The area vector

S
dA

(or

S
A

29.2 Faraday’s Law

963

down. Choose a direction and use it consistently throughout the
problem.

EXECUTE the solution as follows:
1. Calculate  the  magnetic  ﬂux  using  Eq.  (29.2) if

is  uniform
over  the  area  of  the  loop  or  Eq.  (29.1) if  it  isn’t  uniform.
Remember the direction you chose for the area vector.

S
B

2. Calculate the induced emf using Eq. (29.3) or (if your conduc-
tor  has  N turns  in  a  coil)  Eq.  (29.4).  Apply  the  sign  rule
(described  just  after  Example  29.1)  to  determine  the  positive
direction of emf.

3. If the circuit resistance is known, you can calculate the magni-

tude of the induced current I using

E = IR.

EVALUATE your answer: Check your results for the proper units,
and  double-check  that  you  have  properly  implemented  the  sign
rules for magnetic ﬂux and induced emf.

Example 29.2 Magnitude and direction of an induced emf

A 500-loop  circular  wire  coil  with  radius  4.00  cm  is  placed
between the poles of a large electromagnet. The magnetic ﬁeld is
uniform and makes an angle of
with the plane of the coil; it
decreases at 0.200
What are the magnitude and direction of
the induced emf?

T>s.

60°

SOLUTION

IDENTIFY and SET UP: Our target variable is the emf induced by a
varying magnetic ﬂux through the coil. The ﬂux varies because the
magnetic ﬁeld decreases in amplitude. We choose the area vector
S
A
to be in the direction shown in Fig. 29.7. With this choice, the
geometry is similar to that of Fig. 29.6b. That ﬁgure will help us
determine the direction of the induced emf.

29.7 Our sketch for this problem.

Example 29.3

Generator I: A simple alternator

Figure 29.8a shows a simple alternator, a device that generates an
v
emf. A rectangular loop is rotated with constant angular speed
is  uniform  and  con-
about  the  axis  shown. The  magnetic  ﬁeld
stant. At time

Determine the induced emf.

f = 0.

t = 0,

S
B

EXECUTE: The magnetic ﬁeld is uniform over the loop, so we can
f =
calculate  the  ﬂux  using  Eq.  (29.2):
In this expression, the only quantity that changes with time is
30°.
the magnitude B of the ﬁeld, so

d£B>dt = 1dB>dt2A cos f

£B = BA cos f,

where

.

CAUTION Remember  how
f = 60°
tempted to say that
S
f
A
plane of the loop. ❙

is the angle between

and

f
is  deﬁned You  may  have  been
in this problem. If so, remember that
S
and the
B

not the angle between

S
B

,

From Eq. (29.4), the induced emf in the coil of

N = 500

turns is

E = - N

d£B
dt

= N

dB
dt

A cos f

= 5001-0.200 T>s2p10.0400 m221cos 30°2 = 0.435 V

The positive answer means that when you point your right thumb in
below the magnetic ﬁeld
the direction of the area vector
in
(
Fig. 29.7), the positive direction for
is in the direction of the curled
ﬁngers of your right hand. If you viewed the coil from the left in Fig.
29.7 and looked in the direction of

the emf would be clockwise.

30°
E

S
A
,

S
B

S
A

EVALUATE:  If the ends of the wire are connected, the direction of
current  in  the  coil  is  in  the  same  direction  as  the  emf—that  is,
clockwise as seen from the left side of the coil. A clockwise current
increases the magnetic ﬂux through the coil, and therefore tends to
oppose the decrease in total ﬂux. This is an example of Lenz’s law,
which we’ll discuss in Section 29.3.

SOLUTION

IDENTIFY and SET UP: The magnetic ﬁeld
and the area A of the
loop are both constant, but the ﬂux through the loop varies because
f
and the area vector
the loop rotates and so the angle

between

S
B

S
B

Continued

964

CHAPTER 29 Electromagnetic Induction

29.8 (a) Schematic diagram of an alternator. A conducting loop rotates in a magnetic ﬁeld, producing an emf. Connections
from each end of the loop to the external circuit are made by means of that end’s slip ring. The system is shown at the time when
the angle
(b) Graph of the ﬂux through the loop and the resulting emf between terminals a and b, along with the
corresponding positions of the loop during one complete rotation.

f = vt = 90°.

v

(b)
Loop (seen
end-on)

(a)

Brush

Slip
rings

S
B

f

S
A

Brush

S
B

Flux decreasing
most rapidly,
largest positive emf.

Flux increasing
most rapidly,
largest negative emf.

B/dt

E 5 2dF
E, F
B

Flux at its most
negative value,
emf is zero.

Flux at its most
positive value,
emf is zero.

a

E

b

F

B

t

changes (Fig. 29.8a). Because the angular speed is constant and
,  the  angle  as  a  function  of  time  is  given  by

t = 0

at

S
A
f = 0
f = vt.

EXECUTE: The magnetic ﬁeld is uniform over the loop, so the mag-
£B =
netic  ﬂux  is
Hence,  by  Faraday’s
law [Eq. (29.3)] the induced emf is

BA cos f =

BA cos vt.

E = -

d£B
dt

= - d
dt

1BA cos vt2 = vBA sin vt

E

£B

180°2,

EVALUATE:  The induced emf  varies sinusoidally with time (Fig.
1f = 0
29.8b). When the plane of the loop is perpendicular to
reaches its maximum and minimum values. At these
or
times, its instantaneous rate of change is zero and
is zero. Con-
reaches  its  maximum  and  minimum  values  when  the
versely,
S
1f = 90°
plane  of  the  loop  is  parallel  to
is
B
changing  most  rapidly.  We  note  that  the  induced  emf  does  not
depend on the shape of the loop, but only on its area.

270°2

£B

and

or

S
B

E

E

Alternators are used in automobiles to generate the currents in
the ignition, the lights, and the entertainment system. The arrange-
ment is a little different than in this example; rather than having a
rotating loop in a magnetic ﬁeld, the loop stays ﬁxed and an elec-
tromagnet rotates. (The rotation is provided by a mechanical con-
nection between the alternator and the engine.) But the result is the
same;  the  ﬂux  through  the  loop  varies  sinusoidally,  producing  a
sinusoidally varying emf. Larger alternators of this same type are
used in electric power plants (Fig. 29.9).

29.9 A commercial alternator uses many loops of wire wound
around a barrel-like structure called an armature. The armature and
wire remain stationary while electromagnets rotate on a shaft (not
shown) through the center of the armature. The resulting induced
emf is far larger than would be possible with a single loop of wire.

We can use the alternator as a source of emf in an external cir-
cuit by using two slip rings that rotate with the loop, as shown in
Fig.  29.8a.  The  rings  slide  against  stationary  contacts  called
brushes, which  are  connected  to  the  output  terminals  a and b.
Since the emf varies sinusoidally, the current that results in the cir-
cuit is an alternating current that also varies sinusoidally in magni-
tude and direction. The amplitude of the emf can be increased by
increasing the rotation speed, the ﬁeld magnitude, or the loop area
or by using N loops instead of one, as in Eq. (29.4).

Example 29.4

Generator II: A DC generator and back emf in a motor

The  alternator  in  Example  29.3  produces  a  sinusoidally  varying
emf  and  hence  an  alternating  current.  Figure  29.10a  shows  a
direct-current (dc) generator that produces an emf that always has
the same sign. The arrangement of split rings, called a commutator,
reverses the connections to the external circuit at angular positions
at which the emf reverses. Figure 29.10b shows the resulting emf.
Commercial dc generators have a large number of coils and com-
mutator segments, smoothing out the bumps in the emf so that the
terminal  voltage  is  not  only  one-directional  but  also  practically
constant. This brush-and-commutator arrangement is the same as
that  in  the  direct-current  motor  discussed  in  Section  27.8.  The

motor’s back emf is just the emf induced by the changing magnetic
ﬂux through its rotating coil. Consider a motor with a square, 500-
turn  coil  10.0  cm  on  a  side.  If  the  magnetic  ﬁeld  has  magnitude
0.200  T,  at  what  rotation  speed  is  the  average back  emf  of  the
motor equal to 112 V?

SOLUTION

IDENTIFY and SET UP: As far as the rotating loop is concerned, the
situation is the same as in Example 29.3 except that we now have
N turns of wire. Without the commutator, the emf would alternate

between positive and negative values and have an average value of
zero (see Fig. 29.8b). With the commutator, the emf is never nega-
tive and its average value is positive (Fig. 29.10b). We’ll use our
result from Example 29.3 to obtain an expression for this average
value and solve it for the rotational speed

v

.

EXECUTE: Comparison  of  Figs.  29.8b  and  29.10b  shows  that  the
back emf of the motor is just N times the absolute value of the emf
found  for  an  alternator  in  Example  29.3,  as  in  Eq.  (29.4):
ƒ Eƒ = NvBAƒsin vtƒ
.  To  ﬁnd  the  average back  emf,  we  must
replace
by  its  average  value.  We  ﬁnd  this  by  integrating
ƒsin vtƒ
t = 0
and
to
During this half cycle, the sine
dividing by the elapsed time
function is positive, so

ƒsin vtƒ
over  half  a  cycle,  from
p>v.
ƒsin vtƒ = sin vt,

t = T>2 = p>v,

and we ﬁnd

29.2 Faraday’s Law

965

Eav = 2NvBA

p

This  conﬁrms  that  the  back  emf  is  proportional  to  the  rotation
v,
v,
speed
we obtain

as we stated without proof in Section 27.8. Solving for

pEav
2NBA

v =

=

p1112 V2
21500210.200 T210.100 m22

= 176 rad>s

1 V = 1 Wb>s = 1 T # m2>s

from

(We used the unit relationships
Example 29.1.)

1ƒ sin vtƒ2av =

p>v
1
0

sin vt dt
p>v

= 2
p

The average back emf is then

v.
EVALUATE:  The  average  back  emf  is  directly  proportional  to
Hence the slower the rotation speed, the less the back emf and the
greater the possibility of burning out the motor, as we described in
Example 27.11 (Section 27.8).

29.10 (a) Schematic diagram of a dc generator, using a split-ring commutator. The ring halves are attached to the loop and
rotate with it. (b) Graph of the resulting induced emf between terminals a and b. Compare to Fig. 29.8b.

v

(b)
Loop (seen
end-on)

(a)

Brush

S
B

f

S
A

Brush

a

E

b

Commutator

E, F

B

E

S
B

t

F

B

Example 29.5

Generator III: The slidewire generator

S
B

Figure 29.11 shows a U-shaped conductor in a uniform magnetic
ﬁeld  perpendicular to the plane of the ﬁgure and directed into the
page.  We  lay  a  metal  rod  (the  “slidewire”)  with  length  L across
the two arms of the conductor, forming a circuit, and move it to the
right with constant velocity  This induces an emf and a current,
which is why this device is called a slidewire generator. Find the
magnitude and direction of the resulting induced emf.

S
v
.

SOLUTION

IDENTIFY  and SET  UP:  The  magnetic  ﬂux  changes  because  the
area  of  the  loop—bounded  on  the  right  by  the  moving  rod—is

29.11 A slidewire generator. The magnetic ﬁeld
area
are both directed into the ﬁgure. The increase in magnetic
ﬂux (caused by an increase in area) induces the emf and current.

and the vector

S
A

S
B

v dt

S
v

E

L

I

S
B

S
A

I

E

S
A

£B = BA cos f.
to point straight into the page, in the same direction as

increasing. Our target variable is the emf
induced in this expand-
ing loop. The magnetic ﬁeld is uniform over the area of the loop,
We choose the area
so we can ﬁnd the ﬂux using
S
vector
.
B
With this choice a positive emf will be one that is directed clock-
wise around the loop. (You can check this with the right-hand rule:
Using  your  right  hand,  point  your  thumb  into  the  page  and  curl
your ﬁngers as in Fig. 29.6.)

S
EXECUTE: Since
B
f = 0
£B = BA.
and
so the induced emf is

S
A

and

point  in  the  same  direction,  the  angle
The magnetic ﬁeld magnitude B is constant,

E = -

d£B
dt

= - B

dA
dt

To calculate
v dt
distance
dA = Lv dt.

dA>dt,
note that in a time dt the sliding rod moves a
(Fig. 29.11) and the loop area increases by an amount
Hence the induced emf is

E = - B

Lv dt
dt

= - BLv

The minus sign tells us that the emf is directed counterclockwise
around the loop. The induced current is also counterclockwise, as
shown in the ﬁgure.

Continued

966

CHAPTER 29 Electromagnetic Induction

EVALUATE: The emf of a slidewire generator is constant if
is con-
stant. Hence the slidewire generator is a direct-current generator.
It’s not a very practical device because the rod eventually moves

S
v

beyond the U-shaped conductor and loses contact, after which the
current stops.

Example 29.6 Work and power in the slidewire generator

In the slidewire generator of Example 29.5, energy is dissipated in
the circuit owing to its resistance. Let the resistance of the circuit
(made up of the moving slidewire and the U-shaped conductor that
connects  the  ends  of  the  slidewire)  at  a  given  point  in  the
slidewire’s motion be R. Find the rate at which energy is dissipated
in the circuit and the rate at which work must be done to move the
rod through the magnetic ﬁeld.

SOLUTION

ƒEƒ>R;

Pdissipated = I 2R.

we found an expression for the induced emf

IDENTIFY and SET UP: Our target variables are the rates at which
energy  is  dissipated  and  at  which  work  is  done.  Energy  is  dissi-
The current I in the
pated in the circuit at the rate
E
circuit equals
in  this  circuit  in  Example  29.5.  There  is  a  magnetic  force
S
S
on the rod, where  points along the rod in the direc-
F
L
tion of the current. Figure 29.12 shows that this force is opposite to
; to maintain the motion, whoever is pushing the
the rod velocity
S
v
rod  must  apply  a  force  of  equal  magnitude  in  the  direction  of
.
This force does work at the rate Papplied = Fv.

(cid:2) IL

: B

S
v

S

S

29.12 The magnetic force
S
to the induced current is to the left, opposite to v
.

S
F

S

(cid:2) IL

S

: B

that acts on the rod due

I

S
B

I

S
L

S
v

S
F

E

EXECUTE: First  we’ll  calculate
E = - BLv,

so the current in the rod is I

Pdissipated.

From  Example  29.5,
Blv>R
. Hence

Pdissipated = I 2R = a BLv
R

b

= ƒEƒ>R =
R = B2L2v2

2

R

To  calculate
S
S
S
: B
.
F

(cid:2) IL

Papplied,
S
Since  and
L

S
B

we  ﬁrst  calculate

the  magnitude  of

are perpendicular, this magnitude is

F = ILB = BLv
R

LB = B2L2v
R

The applied force has the same magnitude and does work at the rate

Papplied = Fv = B2L2v2

R

EVALUATE:  The rate at which work is done is exactly equal to the
rate at which energy is dissipated in the resistance.

S

S
F

S v

S
B
S
(cid:2) IL

CAUTION You can’t violate energy conservation You might think
or of  might make it possible to
that reversing the direction of
: B
have the magnetic force
be in the same direction as
S
v
This would be a pretty neat trick. Once the rod was moving, the
.
changing magnetic ﬂux would induce an emf and a current, and the
magnetic  force  on  the  rod  would  make  it  move  even  faster,
increasing the emf and current; this would go on until the rod was
moving  at  tremendous  speed  and  producing  electric  power  at  a
prodigious rate. If this seems too good to be true, not to mention a
S
violation of energy conservation, that’s because it is. Reversing
B
also reverses the sign of the induced emf and current and hence the
direction of
so the magnetic force still opposes the motion of the
rod; a similar result holds true if we reverse

S
❙v
.

S
,
L

Generators As Energy Converters
Example 29.6 shows that the slidewire generator doesn’t produce electric energy
out  of  nowhere;  the  energy  is  supplied  by  whatever  body  exerts  the  force  that
keeps the rod moving. All that the generator does is convert that energy into a dif-
ferent form. The equality between the rate at which  mechanical energy is sup-
plied to a generator and the rate at which electric energy is generated holds for all
types of generators. This is true in particular for the alternator described in Exam-
ple 29.3. (We are neglecting the effects of friction in the bearings of an alternator
or between the rod and the U-shaped conductor of a slidewire generator. If these
are included, the conservation of energy demands that the energy lost to friction is
not  available  for  conversion  to  electric  energy.  In  real  generators  the  friction  is
kept to a minimum to keep the energy-conversion process as efﬁcient as possible.)
In Chapter 27 we stated that the magnetic force on moving charges can never
do work. But you might think that the magnetic force
in Example
29.6 is doing (negative) work on the current-carrying rod as it moves, contradict-
ing our earlier statement. In fact, the work done by the magnetic force is actually
zero. The moving charges that make up the current in the rod in Fig. 29.12 have a
vertical component of velocity, causing a horizontal component of force on these
charges. As a result, there is a horizontal displacement of charge within the rod,

(cid:2) IL

: B

S
F

S

S
