796

CHAPTER 24 Capacitance and Dielectrics

C2.

that for the parallel combination in part (b) is greater than either
C1
For two capacitors in series, as in part (a), the charge is the
or
same  on  either  capacitor  and  the  larger potential  difference
appears across the capacitor with the smaller capacitance. Further-
more,  the  sum  of  the  potential  differences  across  the  individual
capacitors  in  series  equals  the  potential  difference  across  the

Example 24.6

A capacitor network

Find  the  equivalent  capacitance  of  the  ﬁve-capacitor  network
shown in Fig. 24.10a.

SOLUTION

IDENTIFY  and SET  UP: These  capacitors  are  neither  all  in  series
nor  all  in  parallel.  We  can,  however,  identify  portions  of  the
arrangement that are either in series or parallel. We combine these
as  described  in  Problem-Solving  Strategy  24.1  to  ﬁnd  the  net
equivalent capacitance, using Eq. (24.5) for series connections and
Eq. (24.7) for parallel connections.

EXECUTE: The  caption  of  Fig.  24.10 outlines  our  procedure.  We
ﬁrst use Eq. (24.5) to replace the
series combina-
tion by its equivalent capacitance

12-mF
C¿:

6-mF

and

1
C¿

=

1
12 mF

+

1
6 mF

       C ¿ = 4 mF

Vac + Vcb = Vab = 18 V

equivalent  capacitor:
.  By  contrast,  for
two  capacitors  in  parallel,  as  in  part  (b),  each  capacitor  has  the
same  potential  difference  and  the  larger charge  appears  on  the
capacitor with the larger capacitance. Can you show that the total
charge
on the parallel combination is equal to the charge
Q = CeqV

on the equivalent capacitor?

Q1 + Q2

This gives us the equivalent combination of Fig. 24.10b. Now we
see  three  capacitors  in  parallel,  and  we  use  Eq.  (24.7) to  replace
them with their equivalent capacitance

C–:

C– = 3 mF + 11 mF + 4 mF = 18 mF

This gives us the equivalent combination of Fig. 24.10c, which has
two  capacitors  in  series. We  use  Eq.  (24.5) to  replace  them  with
Ceq
their  equivalent  capacitance
,  which  is  our  target  variable
(Fig. 24.10d):

1
Ceq

=

1
18 mF

+

1
9 mF

       C eq = 6 mF

EVALUATE: If the potential difference across the entire network in
=  9.0  V,  the  net  charge  on  the  network  is
Fig.  24.10a  is
Q = CeqVab = 16 mF219.0 V2 = 54 mC
. Can you ﬁnd the charge
on, and the voltage across, each of the ﬁve individual capacitors?

Vab

24.10 (a) A capacitor network between points  and
4-mF
lent
(d) Finally, the

capacitor. (c) The
18-mF

3-mF,
9-mF

11-mF,

a
4-mF

and

and

capacitors in series in (c) are replaced by an equivalent

6-mF

capacitor.

b.

(b) The

6-mF
capacitors in parallel in (b) are replaced by an equivalent

12-mF

and

capacitors in series in (a) are replaced by an equiva-

18-mF

capacitor.

(a)

a

(b)

a

(c)

a

(d)

a

3 mF

11 mF

12 mF

6 mF

3 mF

11 mF

4 mF

9 mF

Replace these series capacitors
by an equivalent capacitor ...

9 mF

... replace these
parallel capacitors by
an equivalent capacitor ...

... replace these series
capacitors by an equivalent
capacitor.

6 mF

18 mF

9 mF

b

b

b

b

8-mF

capacitor and an
capacitor have a greater potential difference across it than the

Test Your Understanding of Section 24.2 You want to connect a
4-mF
4-mF
tor? (i) series; (ii) parallel; (iii) either series or parallel; (iv) neither series nor parallel.
(b) With which type of connection will the
8-mF
parallel.

capacitor have a greater charge than the
capacitor? (i) series; (ii) parallel; (iii) either series or parallel; (iv) neither series nor

capacitor. (a) With which type of connection will the
capaci-

4-mF

8-mF

❙

24.3 Energy Storage in Capacitors

and Electric-Field Energy

Many of the most important applications of capacitors depend on their ability to
store  energy. The  electric  potential  energy  stored  in  a  charged  capacitor  is  just
equal to the amount of work required to charge it—that is, to separate opposite
charges  and  place  them  on  different  conductors.  When  the  capacitor  is  dis-
charged, this stored energy is recovered as work done by electrical forces.

24.3 Energy Storage in Capacitors and Electric-Field Energy

797

We can calculate the potential energy  of a charged capacitor by calculating the
required to charge it. Suppose that when we are done charging the capac-
From Eq. (24.1)
and the ﬁnal potential difference is

V.

U

W

work
itor, the ﬁnal charge is
these quantities are related by

Q

V =

Q
C

v

q

Let  and  be the charge and potential difference, respectively, at an intermedi-
ate stage during the charging process; then
dW
required to transfer an additional element of charge

At this stage the work
is

v = q>C.
dq

dW = v dq =

q dq
C

The total work
value
Q

is

W

needed to increase the capacitor charge

q

from zero to a ﬁnal

W =

W

L
0

dW = 1

C L
0

Q

q dq =

Q2
2C

(work to charge a capacitor) (24.8)

This is also equal to the total work done by the electric ﬁeld on the charge when
to zero as the
the capacitor discharges. Then q decreases from an initial value
V
elements  of  charge
down to zero.

“fall”  through  potential  differences

that  vary  from

dq

Q

v

W
If we deﬁne the potential energy of an uncharged capacitor to be zero, then
in Eq. (24.8) is equal to the potential energy  of the charged capacitor. The ﬁnal
stored charge is

so we can express

(which is equal to

Q = CV,

U
U

) as

W

U =

Q2
2C

= 1

2 CV 2 = 1

2 QV

(potential energy stored
in a capacitor)

(24.9)

Q
When
per coulomb),

U

is in joules.

is in coulombs,

C

in farads (coulombs per volt), and

V

in volts (joules

U = 1

1
2 V
U = 1
2

shows that the total work

during the charging process.

The last form of Eq. (24.9),

2 QV,
required
to charge the capacitor is equal to the total charge  multiplied by the average
potential difference
The expression

in Eq. (24.9) shows that a charged capacitor is
2 kx 2.
x,
and the reciprocal of the capacitance,
is analogous to the force constant  The energy supplied to a capacitor in the

the electrical analog of a stretched spring with elastic potential energy
The charge
1>C,
k.
charging process is analogous to the work we do on a spring when we stretch it.

is analogous to the elongation

1Q2>C2

U = 1

W

Q

Q

Equations (24.8) and (24.9) tell us that capacitance measures the ability of a
capacitor to store both energy and charge. If a capacitor is charged by connecting
it to a battery or other source that provides a ﬁxed potential difference
then
C
increasing the value of  gives a greater charge
and a greater amount of
2 CV 2.
If  instead  the  goal  is  to  transfer  a  given  quantity  of
stored  energy
W
charge
the greater the capacitance, the easier it is
required is inversely proportional to
to give a capacitor a ﬁxed amount of charge.

from  one  conductor  to  another,  Eq.  (24.8) shows  that  the  work

Q = CV

U = 1

C;

V,

Q

Applications of Capacitors: Energy Storage
Most  practical  applications  of  capacitors  take  advantage  of  their  ability  to
store and release energy. In electronic ﬂash units used by photographers, the
energy stored in a capacitor (see Fig. 24.4) is released by depressing the camera’s
shutter  button. This  provides  a  conducting  path  from  one  capacitor  plate  to  the
other through the ﬂash tube. Once this path is established, the stored energy is rap-
idly converted into a brief but intense ﬂash of light. An extreme example of the
same principle is the Z machine at Sandia National Laboratories in New Mexico,

?

798

CHAPTER 24 Capacitance and Dielectrics

C

2 CV 2

U = 1

24.11 The Z machine uses a large
number of capacitors in parallel to give a
(see
tremendous equivalent capacitance
Section 24.2). Hence a large amount of
energy
a modest potential difference  The arcs
shown here are produced when the capaci-
tors discharge their energy into a target,
which is no larger than a spool of thread.
This heats the target to a temperature
higher than

can be stored with even
V.

2 * 109

K.

which is used in experiments in controlled nuclear fusion (Fig. 24.11). A bank of
charged capacitors releases more than a million joules of energy in just a few bil-
lionths  of  a  second.  For  that  brief  space  of  time,  the  power  output  of  the  Z
2.9 * 1014
machine is
W, or about 80 times the power output of all the electric
power plants on earth combined!

In other applications, the energy is released more slowly. Springs in the sus-
pension of an automobile help smooth out the ride by absorbing the energy from
sudden jolts and releasing that energy gradually; in an analogous way, a capacitor
in  an  electronic  circuit  can  smooth  out  unwanted  variations  in  voltage  due  to
power surges. We’ll discuss these circuits in detail in Chapter 26.

Electric-Field Energy
We can charge a capacitor by moving electrons directly from one plate to another.
This requires doing work against the electric ﬁeld between the plates. Thus we can
think of the energy as being stored in the ﬁeld in the region between the plates. To
develop  this  relationship,  let’s  ﬁnd  the  energy  per  unit  volume in  the  space
between the plates of a parallel-plate capacitor with plate area  and separation
d.
We call this the energy density, denoted by
From Eq. (24.9) the total stored
2 CV 2
hence the
potential energy is
energy density is

u.
and the volume between the plates is just

Ad;

A

1

u = Energy density =

(24.10)

From Eq. (24.2) the capacitance
ence
expressions in Eq. (24.10), the geometric factors  and  cancel, and we ﬁnd

E
is  related  to  the  electric-ﬁeld  magnitude
A

The potential differ-
If  we  use  these

V = Ed.
d

is given by

C

V

1

2 CV 2
Ad
C = P0 A>d.
by

P0E 2

u = 1
2

(electric energy density in a vacuum)

(24.11)

Although we have derived this relationship only for a parallel-plate capacitor, it
turns out to be valid for any capacitor in vacuum and indeed for any electric ﬁeld
conﬁguration in vacuum. This result has an interesting implication. We think of
vacuum as space with no matter in it, but vacuum can nevertheless have electric
ﬁelds and therefore energy. Thus “empty” space need not be truly empty after all.
We will use this idea and Eq. (24.11) in Chapter 32 in connection with the energy
transported by electromagnetic waves.

CAUTION Electric-ﬁeld energy is electric potential energy It’s a common misconception
that  electric-ﬁeld  energy  is  a  new  kind  of  energy,  different  from  the  electric  potential
energy described before. This is not the case; it is simply a different way of interpreting
electric potential energy. We can regard the energy of a given system of charges as being a
shared property of all the charges, or we can think of the energy as being a property of the
electric ﬁeld that the charges create. Either interpretation leads to the same value of the
potential energy. ❙

Example 24.7

Transferring charge and energy between capacitors

C1 = 8.0 mF
V0 = 120 V

?  (b)  What  is  the  energy  stored  in

to a power supply, charge it
We connect a capacitor
,  and  disconnect  the  power
to  a  potential  difference
supply (Fig. 24.12). Switch
on
?  (c)  Capacitor
C1
C2 = 4.0 mF
is  initially  uncharged.  We  close  switch  S.  After
charge no longer ﬂows, what is the potential difference across each
capacitor, and what is the charge on each capacitor? (d) What is the
ﬁnal energy of the system?

is open. (a) What is the charge

Q0

C1

S

24.12 When the switch
connected to an uncharged capacitor
switch is an insulating handle; charge can ﬂow only between the
two upper terminals and between the two lower terminals.

C1
The center part of the

is closed, the charged capacitor

C2.

S

is

Q0
+ + + +
– – – –

5 120 V

V0

C1

5 8.0 mF

S

C2

5 4.0 mF

SOLUTION

24.3 Energy Storage in Capacitors and Electric-Field Energy

799

Uinitial

for the single charged capacitor

IDENTIFY  and SET  UP: In parts (a) and (b) we ﬁnd the charge
Q0
using
and stored energy
Eqs. (24.1) and (24.9), respectively. After we close switch S, one
wire  connects  the  upper  plates  of  the  two  capacitors  and  another
wire connects the lower plates; the capacitors are now connected
in parallel. In part (c) we use the character of the parallel connec-
tion to determine how
is shared between the two capacitors. In
part (d) we again use Eq. (24.9) to ﬁnd the energy stored in capaci-
the energy of the system is the sum of these values.
tors

and

Q0

C1

C1

C2;

EXECUTE: (a) The initial charge

Q0
Q0 = C1V0 = 18.0 mF21120 V2 = 960 mC

on

C1

is

(b) The energy initially stored in

C1

is

Uinitial = 1

2 Q0V0 = 1

2

1960 * 10-6 C21120 V2 = 0.058 J

(c) When we close the switch, the positive charge

is distrib-
uted  over  the  upper  plates  of  both  capacitors  and  the  negative
be
is distributed over the lower plates. Let
charge
the magnitudes of the ﬁnal charges on the capacitors. Conservation

-Q0

and

Q2

Q1

Q0

Example 24.8

Electric-field energy

of electric potential energy in a volume of

(a)  What  is  the  magnitude  of  the  electric  ﬁeld  required  to  store
in vac-
1.00 J
uum? (b) If the ﬁeld magnitude is 10 times larger than that, how
much energy is stored per cubic meter?

1.00 m3

SOLUTION

E

IDENTIFY and SET UP: We use the relationship between the electric-
ﬁeld magnitude
In part (a) we use the
then we use Eq. (24.11) to ﬁnd the cor-
given information to ﬁnd
responding value of
In part (b), Eq. (24.11) tells us how u varies
with

and the energy density

E.

E.

u;

u.

EXECUTE: (a) The desired energy density is
from Eq. (24.11),

u = 1.00 J>m3.

Then

Q1 + Q2 = Q0

of charge requires that
V
between the plates is the same for both capacitors because they are
Q2 = C2V
connected in parallel, so the charges are
.
We  now  have  three  independent  equations  relating  the  three
, and V. Solving these, we ﬁnd
unknowns

. The potential difference

Q1 = C1V

and

,

Q1

Q2

Q0
C1 + C2

960 mC
V =
8.0 mF + 4.0 mF
Q1 = 640 mC    Q2 = 320 mC

=

= 80 V

(d) The ﬁnal energy of the system is

Ufinal = 1

2 Q2V = 1

2 Q1V + 1
1960 * 10-6 C2180 V2 = 0.038 J

2 Q0V

= 1
2

EVALUATE: The ﬁnal energy is less than the initial energy; the dif-
ference was converted to energy of some other form. The conduc-
tors become a little warmer because of their resistance, and some
energy is radiated as electromagnetic waves. We’ll study the behav-
ior of capacitors in more detail in Chapters 26 and 31.

E =

=

A

2u
P0

211.00 J>m32
8.85 * 10-12 C2>N # m2
= 4.75 * 105 N>C = 4.75 * 105 V>m

B

(b)  Equation  (24.11) shows  that

u

is  proportional  to

increases by a factor of 10,
so the energy density becomes u =

u

100 J>m3.

increases by a factor of

If

E 2.
E
102 = 100,

EVALUATE: Dry  air  can  sustain  an  electric  field  of  about
3 * 106 V>m
without experiencing dielectric breakdown, which
we will discuss in Section 24.4. There we will see that field mag-
nitudes  in  practical  insulators  can  be  as  great  as  this  or  even
larger.

Example 24.9

Two ways to calculate energy stored in a capacitor

and

+Q

The spherical capacitor described in Example 24.3 (Section 24.1)
has charges
on its inner and outer conductors. Find
the electric potential energy stored in the capacitor (a) by using the
capacitance
found  in  Example  24.3  and  (b)  by  integrating  the
electric-ﬁeld energy density u.

-Q

C

SOLUTION

IDENTIFY and SET UP: We can determine the energy U stored in a
capacitor in two ways: in terms of the work done to put the charges
on the two conductors, and in terms of the energy in the electric
ﬁeld  between  the  conductors. The  descriptions  are  equivalent,  so
they must give us the same result. In Example 24.3 we found the
capacitance
in the space between the
conductors. (The electric ﬁeld is zero inside the inner sphere and is
also zero outside the inner surface of the outer sphere, because a
r 6 ra
encloses  zero  net
Gaussian  surface  with  radius

and the ﬁeld magnitude

r 7 rb

or

C

E

charge.  Hence  the  energy  density  is  nonzero  only  in  the  space
between the spheres,
.) In part (a) we use Eq. (24.9) to
u,
In part (b) we use Eq. (24.11) to ﬁnd  which we integrate
ﬁnd
over the volume between the spheres to ﬁnd U.

ra 6 r 6 rb

U.

EXECUTE: (a)  From  Example  24.3,  the  spherical  capacitor  has
capacitance

C = 4pP0

rarb
rb - ra

ra

rb

and

where
are  the  radii  of  the  inner  and  outer  conducting
spheres,  respectively.  From  Eq.  (24.9) the  energy  stored  in  this
capacitor is

U =

Q2
2C

=

Q2
8pP0

rb - ra
rarb

Continued
