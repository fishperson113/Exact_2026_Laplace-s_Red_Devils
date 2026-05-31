25-3 CAPACITORS  I N  PARALLE L  AN D  I N  SE R I ES

723

Sample Problem 25.01 Charging the plates in a parallel-plate capacitor

In  Fig. 25-7a, switch  S  is  closed  to  connect  the  uncharged
capacitor of capacitance C ! 0.25 mF to the battery of poten-
tial difference V ! 12 V. The lower capacitor plate has thick-
ness L ! 0.50  cm  and  face  area  A ! 2.0 $ 10#4 m2, and  it
consists of copper, in which the density of conduction elec-
trons  is  n ! 8.49 $ 1028 electrons/m3. From  what  depth  d
within the plate (Fig. 25-7b) must electrons move to the plate
face as the capacitor becomes charged?

KEY IDEA

The  charge  collected  on  the  plate  is  related  to  the  capaci-
tance  and  the  potential  difference  across  the  capacitor  by
Eq. 25-1 (q ! CV).

Calculations: Because the lower plate is connected to the
negative terminal of the battery, conduction electrons move
up to the face of the plate. From Eq. 25-1, the total charge

or

magnitude that collects there is

q ! CV ! (0.25 $ 10#6 F)(12 V)

! 3.0 $ 10#6 C.

Dividing this result by e gives us the number N of conduc-
tion electrons that come up to the face:
3.0 $ 10 #6 C
1.602 $ 10 #19 C

N !

q
e

!

! 1.873 $ 1013 electrons.

These electrons come from a volume that is the product of the
face area A and the depth d we seek. Thus, from the density of
conduction electrons (number per volume), we can write

n !

N
Ad

,

d !

N
An

!

1.873 $ 1013 electrons
(2.0 $ 10 #4 m2)(8.49 $ 1028 electrons/m3)

Figure 25-7 (a) A
battery and ca-
pacitor circuit.
(b) The lower ca-
pacitor plate.

C

S

(a)

–

–

–

–

–

–

(b)

d

! 1.1 $ 10#12 m ! 1.1 pm.

(Answer)

We commonly say that electrons move from the battery to
the negative face but, actually, the battery sets up an electric
field in the wires and plate such that electrons very close to
the plate face move up to the negative face.

Additional examples, video, and practice available at WileyPLUS

25-3 CAPACITORS IN PARALLEL AND IN SERIES

Learning Objectives
After reading this module, you should be able to . . .

25.06 Sketch schematic diagrams for a battery and (a) three
capacitors in parallel and (b) three capacitors in series.
25.07 Identify that capacitors in parallel have the same poten-
tial difference, which is the same value that their equivalent
capacitor has.

25.08 Calculate the equivalent of parallel capacitors.
25.09 Identify that the total charge stored on parallel capacitors is
the sum of the charges stored on the individual capacitors.
25.10 Identify that capacitors in series have the same charge,
which is the same value that their equivalent capacitor has.

25.11 Calculate the equivalent of series capacitors.
25.12 Identify that the potential applied to capacitors in series is

equal to the sum of the potentials across the individual capacitors.

25.13 For a circuit with a battery and some capacitors in

parallel and some in series, simplify the circuit in steps by
finding equivalent capacitors, until the charge and potential
on the final equivalent capacitor can be determined, and
then reverse the steps to find the charge and potential on
the individual capacitors.

25.14 For a circuit with a battery, an open switch, and one or
more uncharged capacitors, determine the amount of
charge that moves through a point in the circuit when the
switch is closed.

25.15 When a charged capacitor is connected in parallel to one or
more uncharged capacitors, determine the charge and potential
difference on each capacitor when equilibrium is reached.

Key Idea

● The equivalent capacitances Ceq of combinations of individual
capacitors connected in parallel and in series can be found from

and

1
Ceq

n

! ’

j!1

1
Cj

(n capacitors in series).

n

Ceq ! ’

j!1

Cj

(n capacitors in parallel)

Equivalent capacitances can be used to calculate the capaci-
tances of more complicated series – parallel combinations.

724

CHAPTE R  25 CAPACITANCE

Terminal

+
–

B

V

+q3

V

–q3

C3

+q2

+q1

–q2 C2

V

V
–q1 C1

(a)

Terminal

Parallel capacitors and
their equivalent have
the same V (“par-V”).

+
–

B

V

(b)

+q

–q

Ceq

Figure 25-8 (a) Three capacitors connected
in parallel to battery B. The battery main-
tains potential difference V across its termi-
nals and thus across each capacitor. (b) The
equivalent capacitor, with capacitance Ceq,
replaces the parallel combination.

Capacitors in Parallel and in Series
When there is a combination of capacitors in a circuit, we can sometimes replace
that  combination  with  an  equivalent  capacitor — that  is, a  single  capacitor  that
has  the  same  capacitance  as  the  actual  combination  of  capacitors. With  such  a
replacement, we can simplify the circuit, affording easier solutions for unknown
quantities  of  the  circuit. Here  we  discuss  two  basic  combinations  of  capacitors
that allow such a replacement.

Capacitors in Parallel
Figure 25-8a shows an electric circuit in which three capacitors are connected in par-
allel to battery B. This description has little to do with how the capacitor plates are
drawn. Rather, “in parallel” means that the capacitors are directly wired together at
one plate and directly wired together at the other plate, and that the same potential
difference V is applied across the two groups of wired-together plates. Thus, each ca-
pacitor has the same potential difference V, which produces charge on the capacitor.
(In Fig. 25-8a, the applied potential V is maintained by the battery.) In general:

When a potential difference V is applied across several capacitors connected in
parallel, that potential difference V is applied across each capacitor.The total
charge q stored on the capacitors is the sum of the charges stored on all the capacitors.

When we analyze a circuit of capacitors in parallel, we can simplify it with

this mental replacement:

Capacitors connected in parallel can be replaced with an equivalent capacitor that has
the same total charge q and the same potential difference V as the actual capacitors.

(You might remember this result with the nonsense word “par-V,” which is close to
“party,” to mean “capacitors in parallel have the same V.”) Figure 25-8b shows the
equivalent capacitor (with equivalent capacitance Ceq) that has replaced the three ca-
pacitors (with actual capacitances C1, C2, and C3) of Fig. 25-8a.

To derive an expression for Ceq in Fig. 25-8b, we first use Eq. 25-1 to find the

charge on each actual capacitor:

q1 ! C1V, q2 ! C2V,

and q3 ! C3V.

The total charge on the parallel combination of Fig. 25-8a is then

q ! q1 % q2 % q3 ! (C1 % C2 % C3)V.

The equivalent capacitance, with the same total charge q and applied potential
difference V as the combination, is then

Ceq !

q
V

! C1 % C2 % C3,

a result that we can easily extend to any number n of capacitors, as

n

Ceq ! ’

j!1

Cj

(n capacitors in parallel).

(25-19)

Thus, to find the equivalent capacitance of a parallel combination, we simply add
the individual capacitances.

Capacitors in Series
Figure 25-9a shows three capacitors connected in series to battery B.This description
has little to do with how the capacitors are drawn. Rather,“in series” means that the
capacitors are wired serially, one after the other, and that a potential difference V is

25-3 CAPACITORS  I N  PARALLE L  AN D  I N  SE R I ES

725

applied across the two ends of the series. (In Fig. 25-9a, this potential difference V is
maintained by battery B.) The potential differences that then exist across the capaci-
tors in the series produce identical charges q on them.

Terminal

V1

When a potential difference V is applied across several capacitors connected in
series, the capacitors have identical charge q. The sum of the potential differences
across all the capacitors is equal to the applied potential difference V.

+
–

B

V

V2

+q

–q

C1

+q

–q

C2

+q

–q

C3

Series capacitors and
their equivalent have
the same q (“seri-q”).

V3

Terminal

(a)

+
–

B

V

+q

–q

Ceq

(b)

Figure 25-9 (a) Three capacitors connected
in series to battery B. The battery main-
tains potential difference V between the
top and bottom plates of the series combi-
nation. (b) The equivalent capacitor,
with capacitance Ceq, replaces the series
combination.

We can explain how the capacitors end up with identical charge by following a
chain reaction of events, in which the charging of each capacitor causes the charging
of the next capacitor.We start with capacitor 3 and work upward to capacitor 1.When
the battery is first connected to the series of capacitors, it produces charge #q on the
bottom plate of capacitor 3. That charge then repels negative charge from the top
plate of capacitor 3 (leaving it with charge %q). The repelled negative charge moves
to the bottom plate of capacitor 2 (giving it charge #q). That charge on the bottom
plate  of  capacitor  2  then  repels  negative  charge  from  the  top  plate  of  capacitor  2
(leaving it with charge %q) to the bottom plate of capacitor 1 (giving it charge #q).
Finally, the charge on the bottom plate of capacitor 1 helps move negative charge
from the top plate of capacitor 1 to the battery, leaving that top plate with charge %q.

Here are two important points about capacitors in series:

1. When charge is shifted from one capacitor to another in a series of capacitors,
it can move along only one route, such as from capacitor 3 to capacitor 2 in
Fig. 25-9a. If there are additional routes, the capacitors are not in series.

2. The battery directly produces charges on only the two plates to which it is
connected (the bottom plate of capacitor 3 and the top plate of capacitor 1 in
Fig. 25-9a). Charges that are produced on the other plates are due merely to
the shifting of charge already there. For example, in Fig. 25-9a, the part of the
circuit enclosed by dashed lines is electrically isolated from the rest of the
circuit. Thus, its charge can only be redistributed.

When we analyze a circuit of capacitors in series, we can simplify it with this

mental replacement:

Capacitors that are connected in series can be replaced with an equivalent capaci-
tor that has the same charge q and the same total potential difference V as the
actual series capacitors.

(You might remember this with the nonsense word “seri-q” to mean “capacitors
in series have the same q.”)  Figure  25-9b shows the equivalent capacitor (with
equivalent  capacitance  Ceq)  that  has  replaced  the  three  actual  capacitors
(with actual capacitances C1, C2, and C3) of Fig. 25-9a.

To derive an expression for Ceq in Fig. 25-9b, we first use Eq. 25-1 to find the

potential difference of each actual capacitor:

V1 !

q
C1

,  V2 !

q
C2

,  and  V3 !

q
C3

.

The total potential difference V due to the battery is the sum

V ! V1 % V2 % V3 ! q # 1

C1

%

1
C2

%

1

C3 $.

The equivalent capacitance is then

or

Ceq !

q
V

!

1
1/C1 % 1/C2 % 1/C3

,

1
Ceq

!

1
C1

%

1
C2

%

1
C3

.

726

CHAPTE R  25 CAPACITANCE

We can easily extend this to any number n of capacitors as

1
Ceq

n

! ’

j!1

1
Cj

(n capacitors in series).

(25-20)

Using  Eq. 25-20  you  can  show  that  the  equivalent  capacitance  of  a  series  of
capacitances is always less than the least capacitance in the series.

Checkpoint 3

A battery of potential V stores charge q on a combination of two identical capacitors.
What are the potential difference across and the charge on either capacitor if the ca-
pacitors are (a) in parallel and (b) in series?

Sample Problem 25.02 Capacitors in parallel and in series

(a) Find the equivalent capacitance for the combination of
capacitances  shown  in  Fig. 25-10a, across  which  potential
difference V is applied. Assume

parallel  can  be  replaced  with  their  equivalent  capacitor.
Therefore, we should first check whether any of the capaci-
tors in Fig. 25-10a are in parallel or series.

C1 ! 12.0 mF, C2 ! 5.30 mF, and C3 ! 4.50 mF.

KEY IDEA

Any  capacitors  connected  in  series  can  be  replaced  with
their equivalent capacitor, and any capacitors connected in

Finding  equivalent  capacitance: Capacitors  1  and  3  are
connected  one  after  the  other, but  are  they  in  series?  No.
The  potential  V that  is  applied  to  the  capacitors  produces
charge  on  the  bottom  plate  of  capacitor  3. That  charge
causes  charge  to  shift  from  the  top  plate  of  capacitor  3.
However, note that the shifting charge can move to the bot-

A

We first reduce the
circuit to a single
capacitor.

The equivalent of
parallel capacitors
is larger.

The equivalent of
series capacitors
is smaller.

A

C1 =
12.0 µ F
V

C2 =
5.30 µ F

B

C3 =
4.50 µ F

(a)

A

C12 =
17.3 µF

C3 =
4.50 µ F

(b)

V

B

V

C123 =
3.57 µF

12.5 V

Next, we work
backwards to the
desired capacitor.

Applying q = CV
yields the charge.

q123 =
44.6 µ C

C123 =
3.57 µF

V123 =
12.5 V

12.5 V

C123 =
3.57 µF

V123 =
12.5 V

(c )

(d )

(e )

Series capacitors and
their equivalent have
the same q (“seri-q”).

Applying V = q/C yields
the potential difference.

Parallel capacitors and
their equivalent have
the same V (“par-V”).

Applying q = CV
yields the charge.

12.5 V

q12 =
44.6 µC
C12 =
17.3 µF
q3 =
44.6 µ C
C3 =
4.50 µ F

( f )

12.5 V

q12 =
44.6 µC
C12 =
17.3 µF
q3 =
44.6 µ C
C3 =
4.50 µ F

(g )

V12 =
2.58 V

V3 =
9.92 V

C1 =
12.0 µF

C2 =
5.30 µ F

V2 =
2.58 V

V1 =
2.58 V
q3 =
44.6 µ C
C3 =
4.50 µ F

12.5 V

12.5 V

V3 =
9.92 V

q1 =
31.0 µC
C1 =
12.0 µ F

V2 =
2.58 V

q2 =
13.7 µ C
C2 =
5.30 µ F

V3 =
9.92 V

V1 =
2.58 V
q3 =
44.6 µ C
C3 =
4.50 µ F

(h)

(i )

Figure 25-10 (a)–(d) Three capacitors are reduced to one equivalent capacitor. (e)–(i) Working backwards to get the charges.

25-3 CAPACITORS  I N  PARALLE L  AN D  I N  SE R I ES

727

tom  plates  of  both  capacitor  1  and  capacitor  2. Because
there is more than one route for the shifting charge, capaci-
tor 3 is not in series with capacitor 1 (or capacitor 2). Any
time you think you might have two capacitors in series, ap-
ply this check about the shifting charge.

Are capacitor 1 and capacitor 2 in parallel? Yes. Their
top  plates  are  directly  wired  together  and  their  bottom
plates  are directly  wired  together, and  electric  potential
is applied between the top-plate pair and the bottom-plate
pair. Thus, capacitor  1  and  capacitor  2  are  in  parallel, and
Eq. 25-19 tells us that their equivalent capacitance C12 is

C12 ! C1 % C2 ! 12.0 mF % 5.30 mF ! 17.3 mF.

In  Fig. 25-10b, we  have  replaced  capacitors  1  and  2  with
their  equivalent  capacitor, called  capacitor  12  (say  “one
two” and not “twelve”). (The connections at points A and B
are exactly the same in Figs. 25-10a and b.)

Is capacitor 12 in series with capacitor 3? Again apply-
ing  the  test  for  series  capacitances, we  see  that  the  charge
that shifts from the top plate of capacitor 3 must entirely go
to the bottom plate of capacitor 12. Thus, capacitor 12 and
capacitor 3 are in series, and we can replace them with their
equivalent C123 (“one two three”), as shown in Fig. 25-10c.
From Eq. 25-20, we have

1
C123

!

!

from which

1
C12

%

1
C3

1
17.3 mF

%

1
4.50 mF

! 0.280 mF#1,

(b) The potential difference applied to the input terminals
in Fig. 25-10a is V ! 12.5 V. What is the charge on C1?

KEY IDEAS

We  now  need  to  work  backwards  from  the  equivalent
capacitance to get the charge on a particular capacitor. We
have two techniques for such “backwards work”: (1) Seri-q:
Series capacitors have the same charge as their equivalent
capacitor. (2)  Par-V: Parallel  capacitors  have  the  same
potential difference as their equivalent capacitor.

Working  backwards: To  get  the  charge  q1 on  capacitor  1,
we  work  backwards  to  that  capacitor, starting  with  the
equivalent capacitor 123. Because the given potential differ-
ence V (! 12.5 V) is applied across the actual combination
of  three  capacitors  in  Fig. 25-10a, it  is  also  applied  across
C123 in Figs. 25-10d and e. Thus, Eq. 25-1 (q ! CV) gives us

q123 ! C123V ! (3.57 mF)(12.5 V) ! 44.6 mC.

The series capacitors 12 and 3 in Fig. 25-10b each have the
same charge as their equivalent capacitor 123 (Fig. 25-10f ).
Thus, capacitor  12  has  charge  q12 ! q123 ! 44.6 mC. From
Eq. 25-1 and Fig. 25-10g, the potential difference across ca-
pacitor 12 must be

V12 !

q12
C12

!

44.6 mC
17.3 mF

! 2.58 V.

The parallel capacitors 1 and 2 each have the same potential
difference as their equivalent capacitor 12 (Fig. 25-10h). Thus,
capacitor  1  has  potential  difference  V1 ! V12 ! 2.58 V, and,
from Eq. 25-1 and Fig. 25-10i, the charge on capacitor 1 must be

C123 !

1

0.280 mF#1 ! 3.57 mF.

(Answer)

q1 ! C1V1 ! (12.0 mF)(2.58 V)
! 31.0 mC.

(Answer)

Sample Problem 25.03 One capacitor charging up another capacitor

!

3.55 mF, is  charged  to  a  potential
Capacitor  1, with  C1
difference V0 ! 6.30 V, using a 6.30 V battery. The battery is
then removed, and the capacitor is connected as in Fig. 25-11
to an uncharged capacitor 2, with C2 ! 8.95 mF. When switch
S  is  closed, charge  flows  between  the  capacitors. Find  the
charge on each capacitor when equilibrium is reached.

KEY IDEAS

The  situation  here  differs  from  the  previous  example  be-
cause  here  an  applied  electric  potential  is  not maintained
across  a  combination  of  capacitors  by  a  battery  or  some
other source. Here, just after switch S is closed, the only ap-
plied electric potential is that of capacitor 1 on capacitor 2,
and  that  potential  is  decreasing. Thus, the  capacitors  in
Fig. 25-11 are not connected in series; and although they are
drawn parallel, in this situation they are not in parallel.

As  the  electric  potential  across  capacitor  1  decreases,
that  across  capacitor  2  increases. Equilibrium  is  reached
when the two potentials are equal because, with no potential
difference between connected plates of the capacitors, there

After the switch is closed,
charge is transferred until
the potential differences
match.

S

q0

C1

C2

Figure 25-11 A potential difference
V0 is applied to capacitor 1 and the
charging battery is removed. Switch
S is then closed so that the charge
on capacitor 1 is shared with
capacitor 2.
