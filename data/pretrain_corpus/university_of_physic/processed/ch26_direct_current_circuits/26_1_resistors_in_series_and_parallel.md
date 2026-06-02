26

DIRECT-CURRENT
CIRCUITS

LEARNING GOALS

By studying this chapter, you will

learn:

• How to analyze circuits with multiple

resistors in series or parallel.

• Rules that you can apply to any

circuit with more than one loop.

• How to use an ammeter, voltmeter,

ohmmeter, or potentiometer in a

circuit.

• How to analyze circuits that include

both a resistor and a capacitor.

• How electric power is distributed in

the home.

ActivPhysics 12.1: DC Series Circuits
(Qualitative)

850

? In a complex circuit like the one on this circuit board, is it possible to connect

several resistors with different resistances so that they all have the same
potential difference? If so, will the current be the same through all of the
resistors?

If you look inside your TV, your computer, or under the hood of a car, you will

ﬁnd circuits of much greater complexity than the simple circuits we studied in
Chapter 25. Whether connected by wires or integrated in a semiconductor chip,
these circuits often include several sources, resistors, and other circuit elements
interconnected in a network.

In this chapter we study general methods for analyzing such networks, including
how to ﬁnd voltages and currents of circuit elements. We’ll learn how to determine
the equivalent resistance for several resistors connected in series or in parallel. For
more general networks we need two rules called Kirchhoff’s rules. One is based on
the principle of conservation of charge applied to a junction; the other is derived
from energy conservation for a charge moving around a closed loop. We’ll discuss
instruments for measuring various electrical quantities. We’ll also look at a circuit
containing resistance and capacitance, in which the current varies with time.

Our  principal  concern  in  this  chapter  is  with  direct-current (dc)  circuits,  in
which the direction of the current does not change with time. Flashlights and auto-
mobile wiring systems are examples of direct-current circuits. Household electri-
cal power is supplied in the form of alternating current (ac), in which the current
oscillates  back  and  forth.  The  same  principles  for  analyzing  networks  apply  to
both  kinds  of  circuits,  and  we  conclude  this  chapter  with  a  look  at  household
wiring systems. We’ll discuss alternating-current circuits in detail in Chapter 31.

26.1 Resistors in Series and Parallel

Resistors  turn  up  in  all  kinds  of  circuits,  ranging  from  hair  dryers  and  space
heaters to circuits that limit or divide current or reduce or divide a voltage. Such
circuits often contain several resistors, so it’s appropriate to consider combinations
of resistors. A simple example is a string of light bulbs used for holiday decorations;

each bulb acts as a resistor, and from a circuit-analysis perspective the string of
bulbs is simply a combination of resistors.

26.1 Four different ways of connecting
three resistors.

26.1 Resistors in Series and Parallel

851

(a) R1, R2, and R3 in series

R
1

R
2

x

R
3

y

b

a

I

(b) R1, R2, and R3 in parallel

R

1

R

2

R

3

b

a

I

I

I

(c) R1 in series with parallel combination

of R2 and R3

R
2

R

3

b

I

R

1

a

I

(d) R1 in parallel with series combination

of R2 and R3
R
2

R

3

a

I

R
1

b

I

R1,

R3.

R2,

and

Suppose we have three resistors with resistances

Figure 26.1
shows  four  different  ways  in  which  they  might  be  connected  between  points  a
and b. When  several  circuit  elements  such  as  resistors,  batteries,  and  motors
are  connected  in  sequence  as  in  Fig.  26.1a,  with  only  a  single  current  path
between  the  points,  we  say  that  they  are  connected  in  series. We  studied
capacitors in series in Section 24.2; we found that, because of conservation of
charge,  capacitors  in  series  all  have  the  same  charge  if  they  are  initially
uncharged.  In  circuits  we’re  often  more  interested  in  the  current, which  is
charge flow per unit time.

The resistors in Fig. 26.1b are said to be connected in parallel between points
a and b. Each resistor provides an alternative path between the points. For circuit
elements that are connected in parallel, the potential difference is the same across
each element. We studied capacitors in parallel in Section 24.2.
and
R2

are  in  parallel,  and  this  combination  is  in
R3
are in series, and this combination is in

R2
In Fig. 26.1d,

In  Fig.  26.1c,  resistors

R3
and

R1.

series with
parallel with

R1.

For  any  combination  of  resistors  we  can  always  ﬁnd  a  single resistor  that
could replace the combination and result in the same total current and potential
difference. For example, a string of holiday light bulbs could be replaced by a
single,  appropriately  chosen  light  bulb  that  would  draw  the  same  current  and
have the same potential difference between its terminals as the original string of
bulbs. The resistance of this single resistor is called the equivalent resistance of
the  combination.  If  any  one  of  the  networks  in  Fig.  26.1 were  replaced  by  its
equivalent resistance

we could write

Req,

Vab = IReq  or  Req =

Vab
I

Vab

where
is the potential difference between terminals a and b of the network
and I is  the  current  at  point  a or b.  To  compute  an  equivalent  resistance,  we
assume a potential difference
across the actual network, compute the corre-
sponding current I, and take the ratio

Vab

Vab>I.

Resistors in Series
We can derive general equations for the equivalent resistance of a series or parallel
combination of resistors. If the resistors are in series, as in Fig. 26.1a, the current I
must be the same in all of them. (As we discussed in Section 25.4, current is not
to each resistor, we have
“used up” as it passes through a circuit.) Applying

V = IR

Vax = IR1    Vxy = IR2    Vyb = IR3

The potential differences across each resistor need not be the same (except for the
Vab
special case in which all three resistances are equal). The potential difference
across the entire combination is the sum of these individual potential differences:
Vab = Vax + Vxy + Vyb = I1R1 + R2 + R32

and so

Vab
I

= R1 + R2 + R3

The ratio

Vab>I

is, by deﬁnition, the equivalent resistance

Req.

Therefore

Req = R1 + R2 + R3
It is easy to generalize this to any number of resistors:
Req = R1 + R2 + R3 + Á

(resistors in series)

(26.1)

852

CHAPTER 26 Direct-Current Circuits

26.2 A car’s headlights and taillights are
connected in parallel. Hence each light is
exposed to the full potential difference
supplied by the car’s electrical system,
giving maximum brightness. Another
advantage is that if one headlight or tail-
light burns out, the other one keeps shining
(see Example 26.2).

The equivalent resistance of any number of resistors in series equals the sum of
their individual resistances.

The equivalent resistance is greater than any individual resistance.

Let’s compare this result with Eq. (24.5) for capacitors in series. Resistors in
series add directly because the voltage across each is directly proportional to its
resistance  and  to  the  common  current.  Capacitors  in  series  add  reciprocally
because  the  voltage  across  each  is  directly  proportional  to  the  common  charge
but inversely proportional to the individual capacitance.

Resistors in Parallel
If  the  resistors  are  in  parallel, as  in  Fig.  26.1b,  the  current  through  each
resistor need not be the same. But the potential difference between the termi-
(Fig. 26.2). (Remember
nals of each resistor must be the same and equal to
that the potential difference between any two points does not depend on the path
taken between the points.) Let’s call the currents in the three resistors
and
I3.

I = V>R,

Then from

?

Vab

I1,

I2,

I1 =

    I2 =

Vab
R1

    I3 =

Vab
R2

Vab
R3

In general, the current is different through each resistor. Because charge is not
accumulating or draining out of point a, the total current I must equal the sum of
the three currents in the resistors:

I = I1 + I2 + I3 = Vab a 1
R1

+ 1
R2

+ 1
R3

b  or

I
Vab

= 1
R1

+ 1
R2

+ 1
R3

But by the deﬁnition of the equivalent resistance

I>Vab = 1>Req,

so

1
Req

= 1
R1

+ 1
R2

Req,
+ 1
R3

Again it is easy to generalize to any number of resistors in parallel:

ActivPhysics 12.2: DC Parallel Circuits

1
Req

= 1
R1

+ 1
R2

+ 1
R3

+ Á

(resistors in parallel)

(26.2)

For any number of resistors in parallel, the reciprocal of the equivalent resistance
equals the sum of the reciprocals of their individual resistances.

The equivalent resistance is always less than any individual resistance.

Compare this with Eq. (24.7) for capacitors in parallel. Resistors in parallel
add reciprocally because the current in each is proportional to the common volt-
age across them and inversely proportional to the resistance of each. Capacitors
in parallel add directly because the charge on each is proportional to the common
voltage across them and directly proportional to the capacitance of each.

For the special case of two resistors in parallel,

1
Req

= 1
R1

+ 1
R2

=

R1 + R2
R1R2

  and

Req =

R1R2
R1 + R2

(two resistors in parallel)

(26.3)

26.1 Resistors in Series and Parallel

853

Because

it follows that

Vab = I1R1 = I2R2,
R2
R1

I1
I2

=

(two resistors in parallel)

(26.4)

This  shows  that  the  currents  carried  by  two  resistors  in  parallel  are  inversely
proportional to  their  resistances.  More  current  goes  through  the  path  of  least
resistance.

Problem-Solving Strategy 26.1

Resistors in Series and Parallel

IDENTIFY the relevant concepts: As in Fig. 26.1, many resistor net-
works are made up of resistors in series, in parallel, or a combination
thereof. Such networks can be replaced by a single equivalent resis-
tor. The logic is similar to that of Problem-Solving Strategy 24.1 for
networks of capacitors.

SET UP the problem using the following steps:
1. Make a drawing of the resistor network.
2. Identify groups of resistors connected in series or parallel.
3. Identify the target variables. They could include the equivalent
resistance of the network, the potential difference across each
resistor, or the current through each resistor.

EXECUTE the solution as follows:
1. Use  Eq.  (26.1) or  (26.2),  respectively,  to  ﬁnd  the  equivalent

resistance for series or parallel combinations.

2. If the network is more complex, try reducing it to series and paral-
lel combinations. For example, in Fig. 26.1c we ﬁrst replace the
R3
and  with its equivalent resistance;
parallel combination of

R2

this then forms a series combination with
combination of
and
tion with

In Fig. 26.1d, the
in series forms a parallel combina-

R1.

R2

R3

R1.

3. Keep in mind that the total potential difference across resistors
connected in series is the sum of the individual potential differ-
ences.  The  potential  difference  across  resistors  connected  in
parallel is the same for every resistor and equals the potential
difference across the combination.

4. The current through resistors connected in series is the same
through  every  resistor  and  equals  the  current  through  the
combination. The total current through resistors connected in
parallel  is  the  sum  of  the  currents  through  the  individual
resistors.

EVALUATE  your  answer: Check  whether  your  results  are  consis-
tent.  The  equivalent  resistance  of  resistors  connected  in  series
should be greater than that of any individual resistor; that of resis-
tors in parallel should be less than that of any individual resistor.

Example 26.1

Equivalent resistance

Find the equivalent resistance of the network in Fig. 26.3a and the
current in each resistor. The source of emf has negligible internal
resistance.

SOLUTION

IDENTIFY and SET UP: This network of three resistors is a combination
of  series  and  parallel  resistances,  as  in  Fig.  26.1c. We  determine

26.3 Steps in reducing a combination of resistors to a single equivalent resistor and ﬁnding the current in each resistor.

(a)

+

E (cid:2) 18 V, r (cid:2) 0

4 V

a

c

6 V

3 V

b

(b)

(c)

(d)

(e)

(f )

Continued

854

CHAPTER 26 Direct-Current Circuits

6-Æ

3-Æ

and

the equivalent resistance of the parallel
resistors, and
4-Æ
then that of their series combination with the
resistor: This is
of the network as a whole. We then
the equivalent resistance
4-Æ
ﬁnd the current in the emf, which is the same as that in the
resistor. The potential difference is the same across each of the par-
3-Æ
allel
resistors; we use this to determine how the cur-
rent is divided between these.

6-Æ

and

Req

6-Æ

EXECUTE: Figures  26.3b  and  26.3c  show  successive  steps  in
reducing  the network  to  a  single  equivalent  resistance
From
3-Æ
resistors in parallel in Fig. 26.3a are
Eq. (26.2), the
and
2-Æ
resistor in Fig. 26.3b:
equivalent to the single
= 1
2 Æ

= 1
6 Æ

+ 1
3 Æ

1
R6 Æ + 3 Æ

Req.

[Equation (26.3) gives the same result.] From Eq. (26.1) the series
2-Æ
resistor is equiva-
resistor with the
combination of this
6-Æ
resistor in Fig. 26.3c.
lent to the single

4-Æ

Example 26.2

Series versus parallel combinations

R = 2 Æ,

E = 8 V

are
Two  identical  light  bulbs,  each  with  resistance
connected  to  a  source  with
and  negligible  internal
resistance.  Find  the  current  through  each  bulb,  the  potential
difference  across  each  bulb,  and  the  power  delivered  to  each
bulb and to the entire network if the bulbs are connected (a) in
series and (b) in parallel. (c) Suppose one of the bulbs burns out;
that  is,  its  filament  breaks  and  current  can  no  longer  flow
through it. What happens to the other bulb in the series case? In
the parallel case?

SOLUTION

IDENTIFY and SET UP: The light bulbs are just resistors in simple
series and parallel connections (Figs. 26.4a and 26.4b). Once we
ﬁnd the current I through each bulb, we can ﬁnd the power deliv-
ered to each bulb using Eq. (25.18),

P = I 2R = V 2>R.

EXECUTE: (a) From Eq. (26.1) the equivalent resistance of the two
Req = 2R = 212 Æ2 =
bulbs between points a and c in Fig. 26.4a is
4 Æ

. In series, the current is the same through each bulb:

I =

Vac
Req

= 8 V
4 Æ

= 2 A

Since the bulbs have the same resistance, the potential difference is
the same across each bulb:

Vab = Vbc = IR = 12 A212 Æ2 = 4 V

From Eq. (25.18), the power delivered to each bulb is

P = I 2R = 12 A2212 Æ2 = 8 W    or

P =

2

V ab
R

=

2

V bc
R

=

14 V22
2 Æ

= 8 W

The total power delivered to both bulbs is

Ptot = 2P = 16 W.

(b) If the bulbs are in parallel, as in Fig. 26.4b, the potential differ-
across each bulb is the same and equal to 8 V, the terminal

ence
voltage of the source. Hence the current through each light bulb is

Vde

4-Æ

I = Vab>R = 118 V2>16 Æ2 = 3 A.
2-Æ

We reverse these steps to ﬁnd the current in each resistor of the
original  network.  In  the  circuit  shown  in  Fig.  26.3d  (identical  to
So
Fig. 26.3c), the current is
resistors in Fig. 26.3e (identical to
the current in the
and
Fig.  26.3b)  is  also  3  A.  The  potential  difference
across  the
2-Æ
This
potential  difference  must  also  be  6  V in  Fig.  26.3f  (identical  to
3-Æ
Fig.  26.3a).  From
and
resistors  in  Fig.  26.3f  are  respectively
16 V2>13 Æ2 = 2 A

and
16 V2>16 Æ2 = 1 A

Vcb = IR = 13 A212 Æ2 = 6 V.

resistor  is  therefore

the  currents  in  the

I = Vcb>R,

6-Æ

Vcb

.

3-Æ

resistor as through the

EVALUATE:  Note  that  for  the  two  resistors  in  parallel  between
points c and b in  Fig.  26.3f,  there  is  twice  as  much  current
through the
resistor; more cur-
rent goes through the path of least resistance, in accordance with
Eq.  (26.4).  Note  also  that  the  total  current  through  these  two
resistor between
resistors is 3 A, the same as it is through the
points a and c.

4-Æ

6-Æ

I =

Vde
R

= 8 V
2 Æ

= 4 A

and the power delivered to each bulb is

P = I 2R = 14 A2212 Æ2 = 32 W    or

P =

2

V de
R

=

18 V22
2 Æ

= 32 W

Both  the  potential  difference  across  each  bulb  and  the  current
through each bulb are twice as great as in the series case. Hence
the  power  delivered  to  each  bulb  is  four times  greater,  and  each
bulb is brighter.

The  total  power  delivered  to  the  parallel  network  is

Ptotal =
four  times  greater  than  in  the  series  case.  The

2P = 64 W,

26.4 Our sketches for this problem.

(a) Light bulbs in series

(b) Light bulbs in parallel
