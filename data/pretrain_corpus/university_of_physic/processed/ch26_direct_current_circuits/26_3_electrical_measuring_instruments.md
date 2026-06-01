860

CHAPTER 26 Direct-Current Circuits

Example 26.7

A potential difference in a complex network

In  the  circuit  of  Example  26.6  (Fig.  26.12),  find  the  potential
difference

Vab.

SOLUTION

Vab = Va - Vb

IDENTIFY  and SET  UP:  Our  target  variable
is  the
potential at point a with respect to point b. To ﬁnd it, we start at
point b and  follow  a  path  to  point  a,  adding  potential  rises  and
drops as we go. We can follow any of several paths from b to a; the
result must be the same for all such paths, which gives us a way to
check our result.

EXECUTE: The  simplest  path  is  through  the  center
In  Example  26.6  we  found

1-Æ
resistor.
showing  that  the  actual

I3 = - 1 A,

current direction through this resistor is from right to left. Thus, as
we  go  from  b to a,  there  is  a  drop of  potential  with  magnitude
ƒ I3 ƒ R = 11 A211 Æ2 = 1 V.
, and the poten-
Hence
tial at a is 1 V less than at point b.

Vab = - 1 V

EVALUATE: To check our result, let’s try a path from b to a that goes
through the lower two resistors. The currents through these are

I2 + I3 = 5 A + 1-1 A2 = 4 A  and
I1 - I3 = 6 A - 1-1 A2 = 7 A

and so

Vab = - 14 A212 Æ2 + 17 A211 Æ2 = - 1 V

You can conﬁrm this result using some other paths from b to a.

26.13 This ammeter (top) and volt-
meter (bottom) are both d’Arsonval gal-
vanometers. The difference has to do with
their internal connections (see Fig. 26.15).

Test Your Understanding of Section 26.2 Subtract Eq. (1) from Eq. (2) in
Example 26.6. To which loop in Fig. 26.12 does this equation correspond? Would this
equation have simpliﬁed the solution of Example 26.6?

❙

26.3 Electrical Measuring Instruments

We’ve  been  talking  about  potential  difference,  current,  and  resistance  for  two
chapters, so it’s about time we said something about how to measure these quan-
tities. Many common devices, including car instrument panels, battery chargers,
and  inexpensive  electrical  instruments,  measure  potential  difference  (voltage),
current, or resistance using a d’Arsonval galvanometer (Fig. 26.13). In the fol-
lowing discussion we’ll often call it just a meter. A pivoted coil of ﬁne wire is
placed in the magnetic ﬁeld of a permanent magnet (Fig. 26.14). Attached to the
coil is a spring, similar to the hairspring on the balance wheel of a watch. In the
equilibrium  position,  with  no  current  in  the  coil,  the  pointer  is  at  zero.  When
there is a current in the coil, the magnetic ﬁeld exerts a torque on the coil that is
proportional to the current. (We’ll discuss this magnetic interaction in detail in
Chapter 27.) As the coil turns, the spring exerts a restoring torque that is propor-
tional to the angular displacement.

26.14 A d’Arsonval galvanometer,
showing a pivoted coil with attached
pointer, a permanent magnet supplying a
magnetic ﬁeld that is uniform in magnitude,
and a spring to provide restoring torque,
which opposes magnetic-ﬁeld torque.

Magnetic-field torque
tends to push
pointer away
from zero.

Spring torque
  tends to push
    pointer
      toward zero.

5

10

0

Spring

Magnetic
field

Permanent
magnet

Soft-iron
core

Pivoted coil

Thus the angular deﬂection of the coil and pointer is directly proportional to
the coil current, and the device can be calibrated to measure current. The maxi-
90°
or so, is called full-scale deﬂection. The essential
mum deﬂection, typically
electrical  characteristics  of  the  meter  are  the  current
Ifs
required  for  full-scale
to 10 mA) and the resistance
deﬂection (typically on the order of
of the
).
coil (typically on the order of 10 to

10 mA
1000 Æ

Rc

The meter deﬂection is proportional to the current in the coil. If the coil obeys
Ohm’s law, the current is proportional to the potential difference between the ter-
minals of the coil, and the deﬂection is also proportional to this potential differ-
Rc = 20.0 Æ
ence.  For  example,  consider  a  meter  whose  coil  has  a  resistance
and that deﬂects full scale when the current in its coil is
The cor-
responding potential difference for full-scale deﬂection is

Ifs = 1.00 mA.

V = IfsRc = 11.00 * 10-3 A2120.0 Æ2 = 0.0200 V

Ammeters
A current-measuring instrument is usually called an ammeter (or milliammeter,
microammeter, and so forth, depending on the range). An ammeter always meas-
ures the current passing through it. An ideal ammeter, discussed in Section 25.4,
would  have  zero resistance,  so  including  it  in  a  branch  of  a  circuit  would  not

26.3 Electrical Measuring Instruments

861

affect the current in that branch. Real ammeters always have some finite resist-
ance,  but  it  is  always  desirable  for  an  ammeter  to  have  as  little  resistance  as
possible.

We can adapt any meter to measure currents that are larger than its full-scale
reading by connecting a resistor in parallel with it (Fig. 26.15a) so that some of
the current bypasses the meter coil. The parallel resistor is called a shunt resistor
or simply a shunt, denoted as

Rsh.
Suppose we want to make a meter with full-scale current
and coil resistance
into an ammeter with full-scale reading
To determine the shunt resistance
needed, note that at full-scale deﬂection the total current through the parallel
and the current
Vab
is  the

Rc
Rsh
Ia,
combination is
through  the  shunt  is  the  difference
same for both paths, so

the current through the coil of the meter is
Ia - Ifs.
IfsRc = 1Ia - Ifs2Rsh    (for an ammeter)

The  potential  difference

(26.7)

Ifs,

Ia.

Ifs

26.15 Using the same meter to measure
(a) current and (b) voltage.

(a)

Moving-coil
ammeter

(b)

Moving-coil
voltmeter

|||||||||||| | | | |||||||||||

||||||||||| | | | | |||||||||||

Rc

+
a

Rsh

–
b

I

I

Rc

Rs

+
a

–
b

Circuit
element

Vb

I

Va

I

Example 26.8

Designing an ammeter

What shunt resistance is required to make the 1.00-mA,
meter  described  above  into  an  ammeter  with  a  range  of  0  to
50.0 mA?

SOLUTION

IDENTIFY and SET UP: Since the meter is being used as an amme-
ter, its internal connections are as shown in Fig. 26.15a. Our target
,  which  we  will  ﬁnd  using
variable  is  the  shunt  resistance
Eq.  (26.7).  The  ammeter  must  handle  a  maximum  current
Ia = 50.0 * 10-3 A.
and the
The coil resistance is
meter shows full-scale deﬂection when the current through the coil
is

Ifs = 1.00 * 10-3 A.

Rc = 20.0 Æ,

Rsh

EXECUTE: Solving Eq. (26.7) for

Rsh,

we ﬁnd

Rsh =

IfsRc
Ia - Ifs
= 0.408 Æ

=

11.00 * 10-3 A2120.0 Æ2
50.0 * 10-3 A - 1.00 * 10-3 A

20.0-Æ EVALUATE:  It’s useful to consider the equivalent resistance

Req

of

the ammeter as a whole. From Eq. (26.2),

+ 1
Rsh

Req = a 1
Rc
= 0.400 Æ

-1

b

= a

1
20.0 Æ

+

1
0.408 Æ

b

-1

The  shunt  resistance  is  so  small  in  comparison  to  the  coil  resist-
ance that the equivalent resistance is very nearly equal to the shunt
resistance. The result is an ammeter with a low equivalent resist-
ance  and  the  desired  0–50.0-mA range.  At  full-scale  deﬂection,
I = Ia = 50.0 mA,
the  current  through  the  galvanometer  is  1.00
mA,  the  current  through  the  shunt  resistor  is  49.0  mA,  and
Vab = 0.0200 V.
If the current I is less than 50.0 mA, the coil cur-
rent and the deﬂection are proportionally less.

Voltmeters
This  same  basic  meter  may  also  be  used  to  measure  potential  difference  or
voltage. A voltage-measuring  device  is  called  a  voltmeter. A voltmeter  always
measures the potential difference between two points, and its terminals must be
connected to these points. (Example 25.6 in Section 25.4 described what can hap-
pen if a voltmeter is connected incorrectly.) As we discussed in Section 25.4, an
ideal voltmeter would have inﬁnite resistance, so connecting it between two points
in a circuit would not alter any of the currents. Real voltmeters always have ﬁnite
resistance, but a voltmeter should have large enough resistance that connecting it
in a circuit does not change the other currents appreciably.

Application Electromyography
A ﬁne needle containing two electrodes is
being inserted into a muscle in this patient’s
hand. By using a sensitive voltmeter to mea-
sure the potential difference between these
electrodes, a physician can probe the muscle’s
electrical activity. This is an important
technique for diagnosing neurological and
neuromuscular diseases.

IfsRc = 11.00 * 10-3 A2120.0 Æ2 = 0.0200 V.

For the meter described in Example 26.8 the voltage across the meter coil at
We
full-scale deﬂection is only
can  extend  this  range  by  connecting  a  resistor
in  series with  the  coil  (Fig.
26.15b). Then only a fraction of the total potential difference appears across the
coil itself, and the remainder appears across
For a voltmeter with full-scale
reading

we need a series resistor

in Fig. 26.15b such that

Rs.

Rs

VV,

Rs

VV = Ifs1Rc + Rs2

(for a voltmeter)

(26.8)

862

CHAPTER 26 Direct-Current Circuits

Example 26.9

Designing a voltmeter

What  series  resistance  is  required  to  make  the  1.00-mA,
meter described above into a voltmeter with a range of 0 to 10.0 V?

20.0-Æ EVALUATE:  At  full-scale  deﬂection,

SOLUTION

IDENTIFY  and SET  UP:  Since  this  meter  is  being  used  as  a  volt-
meter,  its  internal  connections  are  as  shown  in  Fig.  26.15b.  Our
The maximum allowable
target variable is the series resistance
We  want  this  to
voltage  across  the  voltmeter  is
Ifs = 1.00 * 10-3 A.
occur  when  the  current  through  the  coil  is
, which we ﬁnd using
Our target variable is the series resistance
Rs
Eq. (26.8).

Rs.
VV = 10.0 V.

EXECUTE: From Eq. (26.8),

Rs =

VV
Ifs

- Rc =

10.0 V
0.00100 A

- 20.0 Æ = 9980 Æ

Req

Vab = 10.0 V,
Rs

20.0 Æ + 9980 Æ

the  voltage
across the meter is 0.0200 V, the voltage across
is 9.98 V, and
the current through the voltmeter is 0.00100 A. Most of the voltage
appears across the series resistor. The meter’s equivalent resistance
is a desirably high  (cid:2)
Such a
meter is called a “1000 ohms-per-volt” meter, referring to the ratio
of resistance to full-scale deﬂection. In normal operation the cur-
rent through the circuit element being measured (I in Fig. 26.15b)
is much greater than 0.00100 A, and the resistance between points
a and b in the circuit is much less than
The voltmeter
draws off only a small fraction of the current and thus disturbs the
circuit being measured only slightly.

10,000 Æ.

10,000 Æ.

(cid:2)

ActivPhysics 12.4: Using Ammeters and
Voltmeters

Ammeters and Voltmeters in Combination
A voltmeter  and  an  ammeter  can  be  used  together  to  measure  resistance and
power. The resistance R of a resistor equals the potential difference
between
The power input P to any
its terminals divided by the current I; that is,
circuit element is the product of the potential difference across it and the current
through it:
In principle, the most straightforward way to measure R or
P is to measure

and I simultaneously.

R = Vab>I.

P = Vab I.
Vab

Vab

With practical ammeters and voltmeters this isn’t quite as simple as it seems.
In  Fig.  26.16a,  ammeter  A reads  the  current  I in  the  resistor  R.  Voltmeter  V,
Vab
however,  reads  the sum of  the  potential  difference
across  the  resistor  and
across the ammeter. If we transfer the voltmeter ter-
Vbc
the potential difference
minal from c to b, as in Fig. 26.16b, then the voltmeter reads the potential dif-
correctly, but the ammeter now reads the sum of the current I in the
ference
resistor and the current
in the voltmeter. Either way, we have to correct the
reading of one instrument or the other unless the corrections are small enough
to be negligible.

Vab

IV

26.16 Ammeter–voltmeter method for measuring resistance.

b

RA

A

c

(b)

a

(a)

a

R

I

V

RV

b

A

c

R

I

V

RV

IV

Example 26.10 Measuring resistance I

The  voltmeter  in  the  circuit  of  Fig.  26.16a  reads  12.0 V and  the
RV = 10,000 Æ
ammeter reads 0.100 A. The meter resistances are
(for the voltmeter) and
(for the ammeter). What are
the resistance R and the power dissipated in the resistor?

RA = 2.00 Æ

SOLUTION

I = 0.100 A
IDENTIFY and SET UP: The ammeter reads the current
through the resistor, and the voltmeter reads the potential difference

V = 12.0 V

RA = 0
between a and c.  If  the  ammeter  were  ideal (that  is,  if
),
there would be zero potential difference between b and c, the volt-
meter reading
would be equal to the potential differ-
across  the  resistor,  and  the  resistance  would  simply  be
ence
Vab
R = V>I = 112.0 V2>
The  amme-
equal  to
ter  is  not ideal,  however  (its  resistance  is
),  so  the
voltmeter reading V is actually the sum of the potential differences
(across  the  resistor).  We  use
(across  the  ammeter)  and
Vbc
Vab
Vbc
from  the  known  current  and
Ohm’s  law  to  find  the  voltage

10.100 A2 = 120 Æ.

RA = 2.00 Æ

ammeter  resistance.  Then  we  solve  for
and  the  resistance
R.  Given  these,  we  are  able  to  calculate  the  power  P into  the
resistor.

Vab

EXECUTE: From  Ohm’s  law,
0.200 V
potential  difference  across  the  resistor  is
112.0 V2 - 10.200 V2 = 11.8 V.

Vbc = IRA = 10.100 A212.00 Æ2 =
so  the
Vab = V - Vbc =

Hence the resistance is

The  sum  of  these  is

V = 12.0 V,

Vab = IR.

and

Example 26.11 Measuring resistance II

Suppose the meters of Example 26.10 are connected to a differ-
ent resistor as shown in Fig. 26.16b, and the readings obtained on
the meters are the same as in Example 26.10. What is the value of
this  new  resistance  R,  and  what  is  the  power  dissipated  in  the
resistor?

SOLUTION

IA = 0.100 A

IDENTIFY  and SET  UP:  In  Example  26.10  the  ammeter  read  the
actual current through the resistor, but the voltmeter reading was
not the same as the potential difference across the resistor. Now the
V = 12.0 V
situation is reversed: The voltmeter reading
shows the
across the resistor, but the ammeter
actual potential difference
reading
is  not equal  to  the  current  I through  the
resistor. Applying the junction rule at b in Fig. 26.16b shows that
IA = I + IV,
is the current through the voltmeter. We
RV,
ﬁnd
and we use this value to ﬁnd the resistor current I. We then deter-
mine the resistance R from I and the voltmeter reading, and calcu-
late the power as in Example 26.10.

from the given values of V and the voltmeter resistance

where

Vab

IV

IV

26.3 Electrical Measuring Instruments

863

R =

Vab
I

= 11.8 V
0.100 A

= 118 Æ

The power dissipated in this resistor is

P = VabI = 111.8 V210.100 A2 = 1.18 W

EVALUATE: You can conﬁrm this result for the power by using the
alternative formula

Do you get the same answer?

P = I 2R.

EXECUTE: We  have
1.20  mA.  The  actual  current  I in  the  resistor  is
0.100 A - 0.0012 A = 0.0988 A,

IV = V>RV = 112.0 V2>110,000 Æ2 =
I = IA - IV =

and the resistance is

R =

Vab
I

= 12.0 V
0.0988 A

= 121 Æ

The power dissipated in the resistor is

P = VabI = 112.0 V210.0988 A2 = 1.19 W

and

R = 12.0 V>0.100 A = 120 Æ

EVALUATE:  Had  the  meters  been  ideal,  our  results  would  have
P = VI = 112.0 V2 *
been
10.100 A2 = 1.2 W
both  here  and  in  Example  26.10.  The  actual
(correct) results are not too different in either case. That’s because
the  ammeter  and  voltmeter  are  nearly  ideal:  Compared  with  the
is  very  small
resistance R under  test,  the  ammeter  resistance
RA
is very large. Under these condi-
and the voltmeter resistance
tions, treating the meters as ideal yields pretty good results; accu-
rate work requires calculations as in these two examples.

RV

The series resistance

Ohmmeters
An alternative method for measuring resistance is to use a d’Arsonval meter in an
arrangement called an ohmmeter. It consists of a meter, a resistor, and a source
(often a ﬂashlight battery) connected in series (Fig. 26.17). The resistance R to be
measured is connected between terminals x and y.
Rs

is variable; it is adjusted so that when terminals x and
R = 0
),  the  meter  deﬂects  full  scale. When
y are  short-circuited  (that  is,  when
nothing is connected to terminals x and y, so that the circuit between x and y is
open (that is, when
), there is no current and hence no deﬂection. For any
intermediate value of R the meter deﬂection depends on the value of R, and the
meter  scale  can  be  calibrated  to  read  the  resistance  R directly.  Larger  currents
correspond to smaller resistances, so this scale reads backward compared to the
scale showing the current.

R S q

In  situations  in  which  high  precision  is  required,  instruments  containing
d’Arsonval  meters  have  been  supplanted  by  electronic  instruments  with  direct
digital  readouts.  Digital  voltmeters  can  be  made  with  extremely  high  internal
resistance, of the order of
Figure 26.18 shows a digital multimeter, an
instrument that can measure voltage, current, or resistance over a wide range.

100 MÆ.

The Potentiometer
The potentiometer is  an  instrument  that  can  be  used  to  measure  the  emf  of  a
source without drawing any current from the source; it also has a number of other
useful  applications.  Essentially,  it  balances  an  unknown  potential  difference
against an adjustable, measurable potential difference.

Rs
26.17 Ohmmeter circuit. The resistor
has a variable resistance, as is indicated by
the arrow through the resistor symbol. To
use the ohmmeter, ﬁrst connect x directly
to y and adjust
until the meter reads
zero. Then connect x and y across the
resistor R and read the scale.

Rs

||||||||| | | | | | |
`

|

|
0

E

+

y

Rs

x

R
