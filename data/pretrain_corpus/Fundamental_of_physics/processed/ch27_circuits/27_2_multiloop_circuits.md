27-2 M U LTI LOOP  CI RCU ITS

781

27-2 MULTILOOP CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .

27.17 Apply the junction rule.
27.18 Draw a schematic diagram for a battery and three

parallel resistors and distinguish it from a diagram with a
battery and three series resistors.

27.19 Identify that resistors in parallel have the same potential
difference, which is the same value that their equivalent
resistor has.

27.20 Calculate the resistance of the equivalent resistor of

several resistors in parallel.

equivalent resistors, until the current through the battery
can be determined, and then reverse the steps to find
the currents and potential differences of the individual
resistors.

27.23 If a circuit cannot be simplified by using equivalent

resistors, identify the several loops in the circuit, choose
names and directions for the currents in the branches, set
up loop equations for the various loops, and solve these
simultaneous equations for the unknown currents.

27.21 Identify that the total current through parallel resistors
is the sum of the currents through the individual resistors.
27.22 For a circuit with a battery and some resistors in parallel
and some in series, simplify the circuit in steps by finding

27.24 In a circuit with identical real batteries in series, replace

them with a single ideal battery and a single resistor.
27.25 In a circuit with identical real batteries in parallel, re-

place them with a single ideal battery and a single resistor.

Key Idea
● When resistances are in parallel, they have the same potential difference. The equivalent resistance that can replace a parallel
combination of resistances is given by

1
Req

n

! ’

j!1

1
Rj

(n resistances in parallel).

Multiloop Circuits
Figure  27-9  shows  a  circuit  containing  more  than  one  loop. For  simplicity, we
assume the batteries are ideal. There are two junctions in this circuit, at b and d,
and there are three branches connecting these junctions. The branches are the left
branch (bad), the right branch (bcd), and the central branch (bd). What are the
currents in the three branches?

We arbitrarily label the currents, using a different subscript for each branch.
Current i1 has the same value everywhere in branch bad, i2 has the same value
everywhere in branch bcd, and i3 is the current through branch bd. The directions
of the currents are assumed arbitrarily.

Consider  junction  d for  a  moment: Charge  comes  into  that  junction  via
incoming currents i1 and i3, and it leaves via outgoing current i2. Because there is
no variation in the charge at the junction, the total incoming current must equal
the total outgoing current:

You can easily check that applying this condition to junction b leads to exactly
the same equation. Equation 27-18 thus suggests a general principle:

i1 % i3 ! i2.

(27-18)

The current into the junction
must equal the current out
(charge is conserved).

a

1
+  –

b

2
–  +

c

  i 1

R1

R3

  i 3

R 2

  i 2

JUNCTION RULE: The sum of the currents entering any junction must be
equal to the sum of the currents leaving that junction.

This rule is often called Kirchhoff’s junction rule (or Kirchhoff’s current law). It is
simply a statement of the conservation of charge for a steady flow of charge —
there is neither a buildup nor a depletion of charge at a junction. Thus, our basic
tools for solving complex circuits are the loop rule (based on the conservation of
energy) and the junction rule (based on the conservation of charge).

d

Figure 27-9 A multiloop circuit consisting of
three branches: left-hand branch bad, right-
hand branch bcd, and central branch bd.
The circuit also consists of three loops: left-
hand loop badb, right-hand loop bcdb, and
big loop badcb.

782

CHAPTE R  27 CI RCU ITS

Equation 27-18 is a single equation involving three unknowns. To solve the
circuit completely (that is, to find all three currents), we need two more equations
involving those same unknowns. We obtain them by applying the loop rule twice.
In the circuit of Fig. 27-9, we have three loops from which to choose: the left-hand
loop  (badb), the  right-hand  loop  (bcdb), and  the  big  loop  (badcb). Which  two
loops we choose does not matter — let’s choose the left-hand loop and the right-
hand loop.

If we traverse the left-hand loop in a counterclockwise direction from point

b, the loop rule gives us

#1 # i1R1 % i3R3 ! 0.

(27-19)

If we traverse the right-hand loop in a counterclockwise direction from point b,
the loop rule gives us

#i3R3 # i2R2 # #2 ! 0.

(27-20)

We now have three equations (Eqs. 27-18, 27-19, and 27-20) in the three unknown
currents, and they can be solved by a variety of techniques.

If  we  had  applied  the  loop  rule  to  the  big  loop, we  would  have  obtained

(moving counterclockwise from b) the equation

#1 # i1R1 # i2R2 # #2 ! 0.

However, this is merely the sum of Eqs. 27-19 and 27-20.

Resistances in Parallel
Figure  27-10a shows  three  resistances  connected  in  parallel to  an  ideal  battery
of emf  #. The  term “in  parallel” means  that  the  resistances  are  directly  wired
together  on  one  side  and  directly  wired  together  on  the  other  side, and  that  a
potential difference V is applied across the pair of connected sides. Thus, all three
resistances have the same potential difference V across them, producing a cur-
rent through each. In general,

When a potential difference V is applied across resistances connected in parallel,
the resistances all have that same potential difference V.

In Fig. 27-10a, the applied potential difference V is maintained by the battery. In
Fig. 27-10b, the three parallel resistances have been replaced with an equivalent
resistance Req.

Parallel resistors and their
equivalent have the same
potential difference (“par-V”).

i

a

i2 + i3

+
–

R1

  i 1

R 2

  i 2

R3

  i 3

i

b

i2 + i3
(a )

i

+
–

i

a

b
(b )

R eq

i

Figure 27-10 (a) Three resistors connected in parallel across points a and b. (b) An equiva-
lent circuit, with the three resistors replaced with their equivalent resistance Req.

27-2 M U LTI LOOP  CI RCU ITS

783

Resistances connected in parallel can be replaced with an equivalent resistance
Req that has the same potential difference V and the same total current i as the
actual resistances.

You  might  remember  that  Req and  all  the  actual  parallel  resistances  have  the
same potential difference V with the nonsense word “par-V.”

To derive an expression for Req in Fig. 27-10b, we first write the current in

each actual resistance in Fig. 27-10a as

i1 !

V
R1

,    i2 !

V
R2

,    and    i3 !

V
R3

,

where V is the potential difference between a and b. If we apply the junction rule
at point a in Fig. 27-10a and then substitute these values, we find

i ! i1 % i2 % i3 ! V # 1

R1

%

1
R2

%

1

R3 $.

(27-21)

If  we  replaced  the  parallel  combination  with  the  equivalent  resistance  Req
(Fig. 27-10b), we would have

i !

V
Req

.

Comparing Eqs. 27-21 and 27-22 leads to

1
Req

!

1
R1

%

1
R2

%

1
R3

.

Extending this result to the case of n resistances, we have

(27-22)

(27-23)

1
Req

n

! ’

j!1

1
Rj

(n resistances in parallel).

(27-24)

For the case of two resistances, the equivalent resistance is their product divided
by their sum; that is,

Req !

R1R2
R1 % R2

.

(27-25)

Note that when two or more resistances are connected in parallel, the equivalent
resistance is smaller than any of the combining resistances.Table 27-1 summarizes the
equivalence relations for resistors and capacitors in series and in parallel.

Table 27-1 Series and Parallel Resistors and Capacitors

Series

n

Resistors

j!1

Rj

Eq. 27-7

Req ! ’
Same current through
all resistors

Parallel

Series

Capacitors

Parallel

n

n

! ’

Eq. 27-24

1
1
Rj
Req
Same potential difference
across all resistors

j!1

Eq. 25-20

n

1
Cj

! ’

1
Ceq
j!1
Same charge on all
capacitors

j!1

Cj

Eq. 25-19

Ceq ! ’
Same potential difference
across all capacitors

Checkpoint 4

A battery, with potential V across it, is connected to a combination of two identical re-
sistors and then has current i through it. What are the potential difference across and
the current through either resistor if the resistors are (a) in series and (b) in parallel?

784

CHAPTE R  27 CI RCU ITS

Sample Problem 27.02 Resistors in parallel and in series

Figure 27-11a shows a multiloop circuit containing one ideal
battery and four resistances with the following values:

R1 ! 20 0,    R2 ! 20 0,    # ! 12 V,

R3 ! 30 0,    R4 ! 8.0 0.

We  can  now  redraw  the  circuit  as  in  Fig. 27-11c; note  that
the current  through  R23 must  be  i1 because  charge  that
moves through R1 and R4 must also move through R23. For
this simple one-loop circuit, the loop rule (applied clockwise
from point a as in Fig. 27-11d) yields

(a) What is the current through the battery?

%# # i1R1 # i1R23 # i1R4 ! 0.

KEY IDEA

Noting  that  the  current  through  the  battery  must  also  be
the  current  through  R1, we  see  that  we  might  find  the
current by applying the loop rule to a loop that includes R1
because  the  current  would  be  included  in  the  potential
difference across R1.

Incorrect method: Either the left-hand loop or the big loop
should do. Noting that the emf arrow of the battery points
upward, so the current the battery supplies is clockwise, we
might  apply  the  loop  rule  to  the  left-hand  loop, clockwise
from point a. With i being the current through the battery,
we would get

%# # iR1 # iR2 # iR4 ! 0 (incorrect).

However, this equation is incorrect because it assumes
that R1, R2, and R4 all have the same current i. Resistances
R1 and R4 do  have  the  same  current, because  the  current
passing through R4 must pass through the battery and then
through R1 with no change in value. However, that current
splits at junction point b — only part passes through R2, the
rest through R3.

Dead-end  method: To  distinguish  the  several  currents  in
the circuit, we must label them individually as in Fig. 27-11b.
Then, circling clockwise from a, we can write the loop rule
for the left-hand loop as

%# # i1R1 # i2R2 # i1R4 ! 0.

Unfortunately, this equation contains two unknowns, i1 and
i2; we would need at least one more equation to find them.

Successful  method: A  much  easier  option  is  to  simplify
the circuit of Fig. 27-11b by finding equivalent resistances.
Note  carefully  that  R1 and R2 are not in  series  and  thus
cannot  be  replaced  with  an  equivalent  resistance.
However, R2 and R3 are  in  parallel, so  we  can  use  either
Eq. 27-24  or  Eq. 27-25  to  find  their  equivalent  resistance
R23. From the latter,

Substituting the given data, we find

12 V # i1(20 0) # i1(12 0) # i1(8.0 0) ! 0,

which gives us

i1 !

12 V
40 0

! 0.30 A.

(Answer)

(b) What is the current i2 through R2?

KEY IDEAS

(1) we must now work backward from the equivalent circuit
of Fig. 27-11d, where R23 has replaced R2 and R3. (2) Because
R2 and R3 are in parallel, they both have the same potential
difference across them as R23.

Working backward: We know that the current through R23
is i1 ! 0.30 A. Thus, we  can  use  Eq. 26-8  (R ! V/i)  and
Fig. 27-11e to  find  the  potential  difference  V23 across R23.
Setting R23 ! 12 0 from (a), we write Eq. 26-8 as

V23 ! i1R23 ! (0.30 A)(12 0) ! 3.6 V.

The  potential  difference  across  R2
is  thus  also  3.6 V
(Fig. 27-11f), so the current i2 in R2 must be, by Eq. 26-8 and
Fig. 27-11g,

i2 !

V2
R2

!

3.6 V
20 0

! 0.18 A.

(Answer)

(c) What is the current i3 through R3?

KEY IDEAS

We can answer by using either of two techniques: (1) Apply
Eq. 26-8 as we just did. (2) Use the junction rule, which tells
us that at point b in Fig. 27-11b, the incoming current i1 and
the outgoing currents i2 and i3 are related by

i1 ! i2 % i3.

Calculation: Rearranging  this  junction-rule  result  yields
the result displayed in Fig. 27-11g:

R23 !

R2R3
R2 % R3

!

(20 0)(30 0)
50 0

! 12 0.

i3 ! i1 # i2 ! 0.30 A # 0.18 A

! 0.12 A.

(Answer)

Additional examples, video, and practice available at WileyPLUS

27-2 M U LTI LOOP  CI RCU ITS

785

A

The equivalent of parallel
resistors is smaller.

  i 1

R 1 = 20 Ω

R 4 = 8.0 Ω

  i 1
(c )

b

c

+
–

a

  i 1
R 23 = 12 Ω

b

R 1

R 3

+
–

a

R 4

R 2

c

(a )

  i 1

R 1

R 4

  i 1

+
–

a

b

  i 3

R 3

R 2

  i 2

c

(b )

Applying the loop rule
yields the current.

Applying V = iR yields
the potential difference.

  i 1 = 0.30 A
R 23 = 12 Ω

= 12 V

  i 1 = 0.30 A

R 1 = 20 Ω

V 23 = 3.6 V

R 4 = 8.0 Ω

  i 1 = 0.30 A

(e )

b

c

+
–

a

  i 1 = 0.30 A
R 23 = 12 Ω

= 12 V

+
–

a

  i 1 = 0.30 A

R 1 = 20 Ω

R 4 = 8.0 Ω

  i 1 = 0.30 A

(d )

b

c

Parallel resistors and
their equivalent have
the same V (“par-V”).

  i 1 = 0.30 A

R 1 = 20 Ω

= 12 V

+
–

V 2 = 3.6 V

  i 3

b

R 3 = 30 Ω
V 3 = 3.6 V

  i 2
R 2 = 20 Ω

= 12 V

+
–

R 4 = 8.0 Ω

  i 1 = 0.30 A

c

( f )

Applying i = V/R
yields the current.

i 3 = 0.12 A

R 3 = 30 Ω
V 3 = 3.6 V

i 2 = 0.18 A
R 2 = 20 Ω

  i 1 = 0.30 A

R 1 = 20 Ω

V 2 = 3.6 V

R 4 = 8.0 Ω

b

c

  i 1 = 0.30 A

( g )

Figure 27-11 (a) A circuit with an ideal battery. (b) Label the currents. (c) Replacing the parallel resistors with their equivalent.
(d)–(g) Working backward to find the currents through the parallel resistors.

786

CHAPTE R  27 CI RCU ITS

Sample Problem 27.03 Many real batteries in series and in parallel in an electric fish

Electric fish can generate current with biological emf cells
called electroplaques. In  the  South American  eel  they  are
arranged in 140 rows, each row stretching horizontally along
the  body  and  each  containing  5000  cells, as  suggested  by
Fig. 27-12a. Each electroplaque has an emf # of 0.15 V and
an internal resistance r of 0.25 0. The water surrounding the
eel completes a circuit between the two ends of the electro-
plaque  array, one  end  at  the  head  of  the  animal  and  the
other near the tail.

(a) If the surrounding water has resistance Rw ! 800 0, how
much current can the eel produce in the water?

KEY IDEA

We  can  simplify  the  circuit  of  Fig. 27-12a by  replacing
combinations of emfs and internal resistances with equiva-
lent emfs and resistances.

Calculations: We  first  consider  a  single  row. The  total  emf
#row along a row of 5000 electroplaques is the sum of the emfs:
#row ! 5000# ! (5000)(0.15 V) ! 750 V.

The total resistance Rrow along a row is the sum of the inter-
nal resistances of the 5000 electroplaques:

Rrow ! 5000r ! (5000)(0.25 0) ! 1250 0.

We can now represent each of the 140 identical rows as hav-
ing a single emf #row and a single resistance Rrow (Fig. 27-12b).
In Fig. 27-12b, the emf between point a and point b on
any row is #row ! 750 V. Because the rows are identical and
because  they  are  all  connected  together  at  the  left  in
Fig. 27-12b, all points b in that figure are at the same electric
potential. Thus, we  can  consider  them  to  be  connected  so
that there is only a single point b. The emf between point a
and this single point b is #row ! 750 V, so we can draw the
circuit as shown in Fig. 27-12c.

Between points b and c in Fig. 27-12c are 140 resistances
Rrow ! 1250 0, all in parallel. The equivalent resistance Req
of this combination is given by Eq. 27-24 as

1
Req

140

! ’

j!1

1
Rj

! 140

1
Rrow

,

or

Req !

Rrow
140

!

1250 0
140

! 8.93 0.

First, reduce each row to one emf and one resistance.

Electroplaque

–+

–+

–+

r

 5000 electroplaques per row

–+

–+

–+

140 rows

–+

–+

–+

(a )

Emfs in parallel
act as a single emf.

row

= 750 V
–+

a

b

Rw

Rw

Rrow

Rrow

Rrow

c

(b )

Replace the parallel
resistances with their
equivalent.

row
+ –

a

b

(c )

(d )

Figure 27-12 (a) A model of the electric circuit of an eel in water. Along each of 140 rows extending from the head to the tail of the eel, there are
5000 electroplaques.The surrounding water has resistance Rw. (b) The emf #row and resistance Rrow of each row. (c) The emf between points a
and b is #row. Between points b and c are 140 parallel resistances Rrow. (d) The simplified circuit.

Points with the same
potential can be taken
as though connected.

750 V

row
–+

row
–+

Rrow

Rrow

b

b

a

c

row
–+

Rrow

b
Rw

i

Req

c

Rw

i

27-2 M U LTI LOOP  CI RCU ITS

787

Replacing the parallel combination with Req, we obtain the
simplified  circuit  of  Fig. 27-12d. Applying  the  loop  rule  to
this circuit counterclockwise from point b, we have

#row # iRw # iReq ! 0.

Solving for i and substituting the known data, we find

i !

# row
Rw % Req

!

750 V
800 0 % 8.93 0

! 0.927 A % 0.93 A.

(Answer)

If  the  head  or  tail  of  the  eel  is  near  a  fish, some  of  this
current  could  pass  along  a  narrow  path  through  the  fish,
stunning or killing it.

(b)  How  much  current  irow travels  through  each  row  of
Fig. 27-12a?

KEY IDEA

Because the rows are identical, the current into and out of
the eel is evenly divided among them.

Calculation: Thus, we write

irow !

i
140

!

0.927 A
140

! 6.6 $ 10 #3 A.

(Answer)

Thus, the  current  through  each  row  is  small, so  that  the  eel
need not stun or kill itself when it stuns or kills a fish.

Sample Problem 27.04 Multiloop circuit and simultaneous loop equations

# 1 ! 3.0 V,  # 2 ! 6.0 V,

Figure  27-13  shows  a  circuit  whose  elements  have  the  fol-
R2 !
lowing  values:
4.0 0.
The three batteries are ideal batteries. Find the mag-
nitude  and  direction  of  the  current  in  each  of  the  three
branches.

R1 ! 2.0 0,

KEY IDEAS

It is not worthwhile to try to simplify this circuit, because no
two resistors are in parallel, and the resistors that are in series
(those in the right branch or those in the left branch) present
no problem. So, our plan is to apply the junction and loop rules.

Junction rule: Using arbitrarily chosen directions for the cur-
rents as shown in Fig. 27-13, we apply the junction rule at point
a by writing

i3 ! i1 % i2.

(27-26)

An application of the junction rule at junction b gives only
the same equation, so we next apply the loop rule to any two
of the three loops of the circuit.

Left-hand  loop: We  first  arbitrarily  choose  the  left-hand
loop, arbitrarily start at point b, and arbitrarily traverse the
loop in the clockwise direction, obtaining

+
–1

Figure 27-13 A multi-
loop circuit with three
ideal batteries and five
resistances.

i1

R1

R1

i1

i2

R1

a

i3

R 2

2

+
–

b

i2

+
–

2

R1

Combining equations: We now have a system of two equa-
tions (Eqs. 27-27 and 27-28) in two unknowns (i1 and i2) to
solve either “by hand” (which is easy enough here) or with a
“math package.” (One solution technique is Cramer’s rule,
given in Appendix E.) We find

i1 ! #0.50 A.

(27-29)

(The minus sign signals that our arbitrary choice of direction
for i1 in Fig. 27-13 is wrong, but we must wait to correct it.)
Substituting i1 ! #0.50 A  into  Eq. 27-28  and  solving  for
i2 then give us

i2 ! 0.25 A.

(Answer)

#i1R1 % #1 # i1R1 # (i1 % i2)R2 # #2 ! 0,

With Eq. 27-26 we then find that

where  we  have  used  (i1 % i2)  instead  of  i3 in  the  middle
branch. Substituting the given data and simplifying yield

i1(8.0 0) % i2(4.0 0) ! #3.0 V.

(27-27)

Right-hand  loop: For  our  second  application  of  the  loop
rule, we  arbitrarily  choose  to  traverse  the  right-hand  loop
counterclockwise from point b, finding

#i2R1 % #2 # i2R1 # (i1 % i2)R2 # #2 ! 0.

Substituting the given data and simplifying yield

i1(4.0 0) % i2(8.0 0) ! 0.

(27-28)

i3 ! i1 % i2 ! #0.50 A % 0.25 A
! #0.25 A.

The positive answer we obtained for i2 signals that our choice of
direction for that current is correct. However, the negative an-
swers for i1 and i3 indicate that our choices for those currents are
wrong.Thus, as a last step here, we correct the answers by revers-
ing the arrows for i1 and i3 in Fig. 27-13 and then writing

i1 ! 0.50 A and i3 ! 0.25 A.

(Answer)

Caution: Always make any such correction as the last step
and not before calculating all the currents.

Additional examples, video, and practice available at WileyPLUS
