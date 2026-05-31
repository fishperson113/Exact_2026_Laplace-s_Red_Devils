26.5 When connected to the same source, two light bulbs in
series (shown at top) draw less power and glow less brightly than
when they are in parallel (shown at bottom).

26.2 Kirchhoff’s Rules

855

increased  power  compared  to  the  series  case  isn’t  obtained  “for
free”; energy is extracted from the source four times more rapidly
in the parallel case than in the series case. If the source is a battery,
it will be used up four times as fast.

(c) In the series case the same current ﬂows through both bulbs.
If one bulb burns out, there will be no current in the circuit, and
neither bulb will glow.

In the parallel case the potential difference across either bulb is
unchanged if a bulb burns out. The current through the functional
bulb and the power delivered to it are unchanged.

R = V>I

EVALUATE:  Our calculation isn’t completely accurate, because the
resistance
of real light bulbs depends on the potential dif-
ference V across  the  bulb. That’s  because  the  ﬁlament  resistance
increases with increasing operating temperature and therefore with
increasing V. But bulbs connected in series across a source do in
fact glow less brightly than when connected in parallel across the
same source (Fig. 26.5).

Test Your Understanding of Section 26.1 Suppose all three of the
R1 = R2 = R3 = R.
resistors shown in Fig. 26.1 have the same resistance, so
Rank the four arrangements shown in parts (a)–(d) of Fig. 26.1 in order of their
equivalent resistance, from highest to lowest.

❙

26.2 Kirchhoff’s Rules

E2

Many  practical  resistor  networks  cannot  be  reduced  to  simple  series-parallel
charging a bat-
combinations. Figure 26.6a shows a dc power supply with emf
tery with a smaller emf
and feeding current to a light bulb with resistance R.
Figure 26.6b is a “bridge” circuit, used in many different types of measurement
and  control  systems.  (Problem  26.81  describes  one  important  application  of  a
“bridge”  circuit.)  To  compute  the  currents  in  these  networks,  we’ll  use  the
techniques  developed  by  the  German  physicist  Gustav  Robert  Kirchhoff
(1824–1887).

E1

First, here are two terms that we will use often. A junction in a circuit is
a point where three or more conductors meet. A loop is any closed conducting
path.  In  Fig.  26.6a  points  a and b are  junctions,  but  points  c and d are  not;
in Fig. 26.6b the points a, b, c, and d are junctions, but points e and f are not.
The  blue  lines  in  Figs.  26.6a  and  26.6b  show  some  possible  loops  in  these
circuits.

Kirchhoff’s rules are the following two statements:

Kirchhoff’s junction rule: The algebraic sum of the currents into any junction
is zero. That is,

a I = 0

(junction rule, valid at any junction)

(26.5)

Kirchhoff’s  loop  rule: The  algebraic  sum  of  the  potential  differences  in  any
loop, including those associated with emfs and those of resistive elements, must
equal zero. That is,

a V = 0

(loop rule, valid for any closed loop)

(26.6)

26.6 Two networks that cannot be
reduced to simple series-parallel combina-
tions of resistors.

(a)

Junction

Loop 1
a

r2

E

2

+

Loop 2

Loop 3

R

b

Junction

d

Not a
junction

(2)

b

(1)

R1

Rm

R3

a

(3)

R2

c

R 4

(4)

d

r1

E

1

+

c

Not a
junction

(b)

f

+

e

r

E

856

CHAPTER 26 Direct-Current Circuits

26.7 Kirchhoff’s junction rule states that
as much current ﬂows into a junction as
ﬂows out of it.

(a) Kirchhoff’s junction rule

(b) Water-pipe analogy

Junction

I1

I1

(cid:3) I2

I2

The current leaving
a junction equals the
current entering it.

The flow rate of
water leaving the
pipe equals the flow
rate entering it.

The  junction  rule  is  based  on  conservation  of  electric  charge. No  charge
can accumulate at a junction, so the total charge entering the junction per unit
time must equal the total charge leaving per unit time (Fig. 26.7a). Charge per
unit  time  is  current,  so  if  we  consider  the  currents  entering  a  junction  to  be
positive and those leaving to be negative, the algebraic sum of currents into a
junction must be zero. It’s like a T branch in a water pipe (Fig. 26.7b); if you
have  a  total  of  1  liter  per  minute  coming  in  the  two  pipes,  you  can’t  have
3 liters per minute going out the third pipe. We may as well confess that we
used the junction rule (without saying so) in Section 26.1 in the derivation of
Eq. (26.2) for resistors in parallel.

The loop rule is a statement that the electrostatic force is conservative. Sup-
pose we go around a loop, measuring potential differences across successive cir-
cuit elements as we go. When we return to the starting point, we must ﬁnd that
the algebraic sum of these differences is zero; otherwise, we could not say that
the potential at this point has a deﬁnite value.

Sign Conventions for the Loop Rule
In  applying  the  loop  rule,  we  need  some  sign  conventions.  Problem-Solving
Strategy 26.2 describes in detail how to use these, but here’s a quick overview.
We ﬁrst assume a direction for the current in each branch of the circuit and mark
it on a diagram of the circuit. Then, starting at any point in the circuit, we imag-
ine traveling around a loop, adding emfs and IR terms as we come to them. When
we travel through a source in the direction from
the emf is considered to
-,
be positive; when we travel from
the emf is considered to be negative
(Fig.  26.8a).  When  we  travel  through  a  resistor  in  the  same direction  as  the
assumed current, the IR term is negative because the current goes in the direction
of  decreasing  potential.  When  we  travel  through  a  resistor  in  the  direction
opposite to the assumed current, the IR term is positive because this represents a
rise of potential (Fig. 26.8b).

+,

to

to

+

-

Kirchhoff’s  two  rules  are  all  we  need  to  solve  a  wide  variety  of  network
problems.  Usually,  some  of  the  emfs,  currents,  and  resistances  are  known,
and  others  are  unknown.  We  must  always  obtain  from  Kirchhoff’s  rules  a
number  of  independent  equations  equal  to  the  number  of  unknowns  so  that
we can solve the equations simultaneously. Often the hardest part of the solu-
tion  is  not  understanding  the  basic  principles  but  keeping  track  of  algebraic
signs!

26.8 Use these sign conventions when
you apply Kirchhoff’s loop rule. In each
part of the ﬁgure “Travel” is the direction
that we imagine going around the loop,
which is not necessarily the direction of
the current.

(a) Sign conventions for emfs

(b) Sign conventions for resistors

1E: Travel direction
from – to +:

2E: Travel direction
from + to –:

1IR: Travel opposite
to current direction:

2IR: Travel in
current direction:

Travel
–
+

E

Travel
–
+

E

Travel

I
–

+

R

I
–

Travel

+

R

Problem-Solving Strategy 26.2 Kirchhoff’s Rules

IDENTIFY the  relevant  concepts: Kirchhoff’s  rules  are  useful  for
analyzing any electric circuit.

SET UP the problem using the following steps:
1. Draw  a  circuit  diagram,  leaving  room  to  label  all  quantities,
known  and  unknown.  Indicate  an  assumed  direction  for  each
unknown  current  and  emf.  (Kirchhoff’s  rules  will  yield  the
magnitudes and directions of unknown currents and emfs. If the
actual  direction  of  a  quantity  is  opposite  to  your  assumption,
the resulting quantity will have a negative sign.)

2. As  you  label  currents,  it  helpful  to  use  Kirchhoff’s  junction
rule, as in Fig. 26.9, so as to express the currents in terms of as
few quantities as possible.
3. Identify the target variables.

EXECUTE the solution as follows:
1. Choose any loop in the network and choose a direction (clock-
wise  or  counterclockwise)  to  travel  around  the  loop  as  you
apply Kirchhoff’s loop rule. The direction need not be the same
as any assumed current direction.

26.2 Kirchhoff’s Rules

857

2. Travel around the loop in the chosen direction, adding potential
differences algebraically as you cross them. Use the sign con-
ventions of Fig. 26.8.

3. Equate the sum obtained in step 2 to zero in accordance with

the loop rule.

4. If you need more independent equations, choose another loop
and  repeat  steps  1–3;  continue  until  you  have  as  many  inde-
pendent equations as unknowns or until every circuit element
has been included in at least one loop.

5. Solve the equations simultaneously to determine the unknowns.
6. You  can  use  the  loop-rule  bookkeeping  system  to  ﬁnd  the
potential
of any point a with respect to any other point b.
Start at b and add the potential changes you encounter in going
from b to a, using the same sign rules as in step 2. The alge-
braic sum of these changes is

Vab = Va - Vb.

Vab

EVALUATE your answer: Check all the steps in your algebra. Apply
steps 1 and 2 to a loop you have not yet considered; if the sum of
potential drops isn’t zero, you’ve made an error somewhere.

26.9 Applying the junction rule to point a reduces the number of unknown currents from three to two.

(a) Three unknown currents: I1, I2, I3
E
2

E
1

r1

r2

I1

+

I1

R1

I3

R3

a

+

I2

I2

R2

Example 26.3

A single-loop circuit

The circuit shown in Fig. 26.10a contains two batteries, each with
an emf and an internal resistance, and two resistors. Find (a) the
current  in  the  circuit,  (b)  the  potential  difference
and  (c)  the
power output of the emf of each battery.

Vab,

SOLUTION

IDENTIFY  and SET  UP: There are no junctions in this single-loop
circuit,  so  we  don’t  need  Kirchhoff’s  junction  rule.  To  apply
Kirchhoff’s loop rule, we ﬁrst assume a direction for the current;
let’s assume a counterclockwise direction as shown in Fig. 26.10a.

EXECUTE: (a) Starting at a and traveling counterclockwise with the
current,  we  add  potential  increases  and  decreases  and  equate  the
sum to zero as in Eq. (26.6):

-I14 Æ2 - 4 V - I17 Æ2 + 12 V - I12 Æ2 - I13 Æ2 = 0

Collecting like terms and solving for I, we ﬁnd

8 V = I116 Æ2    and    I = 0.5 A

The positive result for I shows that our assumed current direction
is correct.

(b) Applying the junction rule to point a eliminates I3.

r1

E

1

+

I1

I1

1 I2

R3

r2

E

2

+

I2

I2

I1

R1

a

R2

Vab,

(b) To ﬁnd

the potential at a with respect to b, we start at b
and add potential changes as we go toward a. There are two paths
from b to a; taking the lower one, we ﬁnd

Vab = 10.5 A217 Æ2 + 4 V + 10.5 A214 Æ2

= 9.5 V

Point a is at 9.5 V higher potential than b. All the terms in this sum,
including  the  IR terms,  are  positive  because  each  represents  an
increase in potential as we go from b to a. Taking the upper path,
we ﬁnd

Vab = 12 V - 10.5 A212 Æ2 - 10.5 A213 Æ2

= 9.5 V

Here  the  IR terms  are  negative  because  our  path  goes  in  the
direction  of  the  current,  with  potential  decreases  through  the
are the same for both paths, as they
resistors. The results for
must be in order for the total potential change around the loop to
be zero.

Vab

Continued

858

CHAPTER 26 Direct-Current Circuits

(c) The power outputs of the emf of the 12-V and 4-V batteries are

P12V = EI = 112 V210.5 A2 = 6 W
P4V = EI = 1-4 V210.5 A2 = - 2 W

E

The negative sign in
for the 4-V battery appears because the cur-
rent actually runs from the higher-potential side of the battery to
the lower-potential side. The negative value of P means that we are
storing energy in that battery; the 12-V battery is recharging it (if
it is in fact rechargeable; otherwise, we’re destroying it).

EVALUATE:  By  applying  the  expression
to  each  of  the
four  resistors  in  Fig.  26.10a,  you  can  show  that  the  total  power

P = I 2R

dissipated in all four resistors is 4 W. Of the 6 W provided by the
emf of the 12-V battery, 2 W goes into storing energy in the 4-V
battery and 4 W is dissipated in the resistances.

The circuit shown in Fig. 26.10a is much like that used when a
fully charged 12-V storage battery (in a car with its engine run-
ning) is used to “jump-start” a car with a run-down battery (Fig.
26.10b).  The  run-down  battery  is  slightly  recharged  in  the
process. The
resistors in Fig. 26.10a represent the
resistances  of  the  jumper  cables  and  of  the  conducting  path
through the automobile with the run-down battery. (The values of
the resistances in actual automobiles and jumper cables are con-
siderably lower.)

3-Æ

7-Æ

and

26.10 (a) In this example we travel around the loop in the same direction as the assumed current, so all the IR terms are negative.
The potential decreases as we travel from
to
(b) A real-life example of a circuit of this kind.

through the bottom emf but increases as we travel from

through the top emf.

to

+

-

+

-

(a)

(b)

2 V

12 V
+

b

Dead
battery

Live
battery

I

7 V

3 V

I

a

I
Travel

I

+

4 V

4 V

Example 26.4

Charging a battery

In  the  circuit  shown  in  Fig.  26.11,  a  12-V power  supply  with
unknown  internal  resistance  r is  connected  to  a  run-down
rechargeable battery with unknown emf
and internal resistance
1 Æ
carrying  a
current of 2 A. The current through the run-down battery is 1 A in
the direction shown. Find r,
, and the current I through the power
supply.

and  to  an  indicator  light  bulb  of  resistance

3 Æ

E

E

SOLUTION

IDENTIFY and SET UP: This circuit has more than one loop, so we
must apply both the junction and loop rules. We assume the direc-
tion of the current through the 12-V power supply, and the polarity
of  the  run-down  battery,  to  be  as  shown  in  Fig.  26.11. There  are
three target variables, so we need three equations.

26.11 In this circuit a power supply charges a run-down
battery and lights a bulb. An assumption has been made about the
polarity of the emf  of the run-down battery. Is this assumption
correct?

E

(2)

2 A

3 V

1 A

(1)

(3)

a

+

E

1 V

b

+

I

12 V

r

EXECUTE: We apply the junction rule, Eq. (26.5), to point a:

-I + 1 A + 2 A = 0    so    I = 3 A

To  determine  r,  we  apply  the  loop  rule,  Eq.  (26.6),  to  the  large,
outer loop (1):

12 V - 13 A2r - 12 A213 Æ2 = 0    so    r = 2 Æ

E,

To determine  we apply the loop rule to the left-hand loop (2):

-E + 11 A211 Æ2 - 12 A213 Æ2 = 0    so    E = - 5 V

The negative value for
shows that the actual polarity of this emf
is  opposite  to  that  shown  in  Fig.  26.11. As  in  Example  26.3,  the
battery is being recharged.

E

EVALUATE:  Try  applying  the  junction  rule  at  point  b instead  of
point a, and try applying the loop rule by traveling counterclock-
wise  rather  than  clockwise  around  loop  (1). You’ll  get  the  same
results for I and r. We can check our result for  by using the right-
hand loop (3):

E

12 V - 13 A212 Æ2 - 11 A211 Æ2 + E = 0

which again gives us

E = - 5 V

.

Vba = Vb - Va

resistance,  which  is

As an additional check, we note that
3-Æ

equals the
12 A213 Æ2 = 6 V.
voltage  across  the
Going from a to b by the top branch, we encounter potential differ-
and going by the middle
ences
branch,  we  ﬁnd
The  three
ways of getting

-1-5 V2 + 11 A211 Æ2 = + 6 V.
give the same results.

+12 V - 13 A212 Æ2 = + 6 V,

Vba

Example 26.5

Power in a battery-charging circuit

In  the  circuit  of  Example  26.4  (shown  in  Fig.  26.11),  ﬁnd  the
power  delivered  by  the  12-V power  supply  and  by  the  battery
being recharged, and ﬁnd the power dissipated in each resistor.

E
The power output of the emf  of the battery being charged is

Pemf = EIbattery = 1-5 V211 A2 = - 5 W

26.2 Kirchhoff’s Rules

859

SOLUTION

IDENTIFY  and SET  UP:  We  use  the  results  of  Section  25.5,  in
which we found that the power delivered from an emf to a circuit
and  the  power  delivered  to a  resistor  from  a  circuit  is
is
VabI = I 2R.
We know the values of all relevant quantities from
Example 26.4.

EI

EXECUTE: The power output

Ps

from the emf of the power supply is

Psupply = EsupplyIsupply = 112 V213 A2 = 36 W

The power dissipated in the power supply’s internal resistance r is

Pr - supply = I supply

2rsupply = 13 A2212 Æ2 = 18 W

so  the  power  supply’s  net power  output  is
18 W = 18 W.
voltage of the battery is

Pnet = 36 W -
Alternatively,  from  Example  26.4  the  terminal

so the net power output is

Vba = 6 V,

Pnet = Vba Isupply = 16 V213 A2 = 18 W

This is negative because the 1-A current runs through the battery
from the higher-potential side to the lower-potential side. (As we
mentioned in Example 26.4, the polarity assumed for this battery
in Fig. 26.11 was wrong.) We are storing energy in the battery as
we charge it. Additional power is dissipated in the battery’s inter-
nal resistance; this power is

Pr-battery = I battery

2rbattery = 11 A2211 Æ2 = 1 W

1 W + ƒ - 5 W ƒ =
Of this, 5 W represents useful energy stored in the battery;

The  total  power  input  to  the  battery  is  thus
6 W.
the remainder is wasted in its internal resistance.
The power dissipated in the light bulb is

Pbulb = I bulb

2Rbulb = 12 A2213 Æ2 = 12 W

EVALUATE: As a check, note that all of the power from the supply
is accounted for. Of the 18 W of net power from the power supply,
5 W goes to recharge the battery, 1 W is dissipated in the battery’s
internal resistance, and 12 W is dissipated in the light bulb.

Example 26.6

A complex network

Figure 26.12 shows a “bridge” circuit of the type described at the
beginning  of  this  section  (see  Fig.  26.6b).  Find  the  current  in
each resistor and the equivalent resistance of the network of five
resistors.

EXECUTE: We apply the loop rule to the three loops shown:

13 V - I111 Æ2 - 1I1 - I3211 Æ2 = 0
-I211 Æ2 - 1I2 + I3212 Æ2 + 13 V = 0
-I111 Æ2 - I311 Æ2 + I211 Æ2 = 0

(1)

(2)

(3)

SOLUTION

IDENTIFY  and SET  UP: This network is neither a series combina-
tion  nor  a  parallel  combination.  Hence  we  must  use  Kirchhoff’s
rules  to  ﬁnd  the  values  of  the  target  variables.  There  are  ﬁve
unknown currents, but by applying the junction rule to junctions a
and b, we can represent them in terms of three unknown currents
I1,

, as shown in Fig. 26.12.

and

I2,

I3

26.12 A network circuit with several resistors.

One way to solve these simultaneous equations is to solve Eq. (3)
for
and then substitute this expression
into Eq. (2) to eliminate  We then have

I2 = I1 + I3,

obtaining

I2,

I2.

Now we can eliminate
the two equations. We obtain

13 V = I112 Æ2 - I311 Æ2
13 V = I113 Æ2 + I315 Æ2
by multiplying Eq.

(1¿)
78 V = I1113 Æ2    I1 = 6 A

I3

¿
(1 )

¿
(2 )

by 5 and adding

(1)

+

13 V

I 1 + I 2

(2)

I1

1 V

c

(3)

1 V

a

I2

1 V

b

I 2 + I 3

I3

1 V

2 V

I 1 – I 3

d

to  obtain
We  substitute  this  result  into  Eq.
I2 = 5 A.
from  Eq.  (3) we  ﬁnd
The negative  value  of
that its direction is opposite to the direction we assumed.

I3 = - 1 A,
I3

and
tells  us

(1¿)

The total current through the network is

and
the potential drop across it is equal to the battery emf, 13 V. The
equivalent resistance of the network is therefore

I1 + I2 = 11 A,

Req = 13 V
11 A

= 1.2 Æ

EVALUATE: You can check our results for
ing them back into Eqs. (1)–(3). What do you ﬁnd?

I2,

I1,

and  by substitut-

I3
