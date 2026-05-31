788

CHAPTE R  27 CI RCU ITS

27-3 THE AMMETER AND THE VOLTMETER

Learning Objective
After reading this module, you should be able to . . .

27.26 Explain the use of an ammeter and a voltmeter, includ-

Key Idea
● Here are three measurement instruments used with cir-
cuits: An ammeter measures current. A voltmeter measures

ing the resistance required of each in order not to affect the
measured quantities.

voltage (potential differences). A multimeter can be used to
measure current, voltage, or resistance.

i

R2

c

R1

d

+
–

a

A

b

r

i

V

Figure 27-14 A single-loop circuit, showing
how to connect an ammeter (A) and a
voltmeter (V).

The Ammeter and the Voltmeter
An  instrument  used  to  measure  currents  is  called  an  ammeter. To  measure  the
current in a wire, you usually have to break or cut the wire and insert the ammeter
so that the current to be measured passes through the meter. (In Fig. 27-14, amme-
ter A is set up to measure current i.) It is essential that the resistance RA of the am-
meter be very much smaller than other resistances in the circuit. Otherwise, the
very presence of the meter will change the current to be measured.

A meter used to measure potential differences is called a voltmeter. To find
the potential difference between any two points in the circuit, the voltmeter ter-
minals are connected between those points without breaking or cutting the wire.
(In Fig. 27-14, voltmeter V is set up to measure the voltage across R1.) It is essen-
tial that the resistance RV of a voltmeter be very much larger than the resistance
of  any  circuit  element  across  which  the  voltmeter  is  connected. Otherwise, the
meter alters the potential difference that is to be measured.

Often a single meter is packaged so that, by means of a switch, it can be made
to serve as either an ammeter or a voltmeter — and usually also as an ohmmeter,
designed to measure the resistance of any element connected between its termi-
nals. Such a versatile unit is called a multimeter.

27-4 RC CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .

27.27 Draw schematic diagrams of charging and discharging

RC circuits.

27.28 Write the loop equation (a differential equation) for a

charging RC circuit.

27.29 Write the loop equation (a differential equation) for a

discharging RC circuit.

27.30 For a capacitor in a charging or discharging RC circuit,

apply the relationship giving the charge as a function of time.

Key Ideas
● When an emf
in series, the charge on the capacitor increases according to

is applied to a resistance R and capacitance C

#

q ! C #(1 # e#t/RC)

(charging a capacitor),

in which C # ! q0 is the equilibrium (final) charge and RC ! t
is the capacitive time constant of the circuit.

● During the charging, the current is

i !

dq
dt

! # #

R $e#t/RC

(charging a capacitor).

27.31 From the function giving the charge as a function of
time in a charging or discharging RC circuit, find the ca-
pacitor’s potential difference as a function of time.

27.32 In a charging or discharging RC circuit, find the resis-
tor’s current and potential difference as functions of time.

27.33 Calculate the capacitive time constant t.
27.34 For a charging RC circuit and a discharging RC circuit,
determine the capacitor’s charge and potential difference
at the start of the process and then a long time later.

● When a capacitor discharges through a resistance R, the
charge on the capacitor decays according to

q ! q0e#t/RC

(discharging a capacitor).

● During the discharging, the current is

i !

dq
dt

! ## q0

RC $e#t/RC

(discharging a capacitor).

RC Circuits
In preceding modules we dealt only with circuits in which the currents did not
vary with time. Here we begin a discussion of time-varying currents.

Charging a Capacitor
The capacitor of capacitance C in Fig. 27-15 is initially uncharged. To charge it, we
close  switch  S  on  point  a. This  completes  an  RC  series  circuit consisting  of  the
capacitor, an ideal battery of emf #, and a resistance R.

From  Module  25-1, we  already  know  that  as  soon  as  the  circuit  is  com-
plete, charge  begins  to  flow  (current  exists)  between  a  capacitor  plate  and  a
battery  terminal  on  each  side  of  the  capacitor. This  current  increases  the
charge q on the plates and the potential difference VC (! q/C) across the ca-
pacitor. When that potential difference equals the potential difference across
the battery (which here is equal to the emf #), the current is zero. From Eq.
25-1 (q ! CV), the equilibrium (final) charge on the then fully charged capacitor
is equal to C #.

Here  we  want  to  examine  the  charging  process. In  particular  we  want  to
know how the charge q(t) on the capacitor plates, the potential difference VC(t)
across the capacitor, and the current i(t) in the circuit vary with time during the
charging process. We begin by applying the loop rule to the circuit, traversing it
clockwise from the negative terminal of the battery. We find

# # iR #

q
C

! 0.

(27-30)

The last term on the left side represents the potential difference across the capac-
itor. The term is negative because the capacitor’s top plate, which is connected to
the battery’s positive terminal, is at a higher potential than the lower plate. Thus,
there is a drop in potential as we move down through the capacitor.

We  cannot  immediately  solve  Eq. 27-30  because  it  contains  two  variables,

i and q. However, those variables are not independent but are related by

i !

dq
dt

.

(27-31)

Substituting this for i in Eq. 27-30 and rearranging, we find

R

dq
dt

%

q
C

! #

(charging equation).

(27-32)

This  differential  equation  describes  the  time  variation  of  the  charge  q on  the
capacitor in Fig. 27-15. To solve it, we need to find the function q(t) that satisfies
this  equation  and  also  satisfies  the  condition  that  the  capacitor  be  initially
uncharged; that is, q ! 0 at t ! 0.

We shall soon show that the solution to Eq. 27-32 is

q ! C #(1 # e#t/RC)

(charging a capacitor).

(27-33)

(Here e is  the  exponential  base, 2.718  . . . , and  not  the  elementary  charge.)
Note that Eq. 27-33 does indeed satisfy our required initial condition, because
at t ! 0 the term e#t/RC is unity; so the equation gives q ! 0. Note also that as t
goes  to  infinity  (that  is, a  long  time  later), the  term  e#t/RC goes  to  zero; so
the equation  gives  the  proper  value  for  the  full  (equilibrium)  charge  on  the
capacitor — namely, q ! C #. A plot of q(t) for the charging process is given in
Fig. 27-16a.

The derivative of q(t) is the current i(t) charging the capacitor:

i !

dq
dt

! # #

R $e#t/RC

(charging a capacitor).

(27-34)

27-4 RC CI RCU ITS

789

S

a

b

+
–

R

C

Figure 27-15 When switch S is closed on a, the
capacitor is charged through the resistor.
When the switch is afterward closed on b, the
capacitor discharges through the resistor.

The capacitor’s charge
grows as the resistor’s
current dies out.

 12
)
C
µ
(

8

q

4

0

  6
)
A
m
(

4

i

2

0

C

2

8  10

4
6
Time (ms)
(a)

/R

2

10

4
8
6
Time (ms)
(b)

Figure 27-16 (a) A plot of Eq. 27-33, which
shows the buildup of charge on the capaci-
tor of Fig. 27-15. (b) A plot of Eq. 27-34,
which shows the decline of the charging
current in the circuit of Fig. 27-15. The
curves are plotted for R ! 2000 0, C ! 1 mF,
and # ! 10 V; the small triangles represent
successive intervals of one time constant t.

790

CHAPTE R  27 CI RCU ITS

A plot of i(t) for the charging process is given in Fig. 27-16b. Note that the current
has the initial value #/R and that it decreases to zero as the capacitor becomes
fully charged.

A capacitor that is being charged initially acts like ordinary connecting wire
relative to the charging current. A long time later, it acts like a broken wire.

By combining Eq. 25-1 (q ! CV ) and Eq. 27-33, we find that the potential

difference VC(t) across the capacitor during the charging process is

VC !

q
C

! #(1 # e#t/RC)

(charging a capacitor).

(27-35)

This  tells  us  that  VC ! 0  at  t ! 0  and  that  VC ! # when  the  capacitor  becomes
fully charged as t : ,.

The Time Constant
The product RC that appears in Eqs. 27-33, 27-34, and 27-35 has the dimensions
of time (both because the argument of an exponential must be dimensionless and
because, in  fact, 1.0  0 $ 1.0 F ! 1.0 s). The  product  RC is  called  the  capacitive
time constant of the circuit and is represented with the symbol t:

t ! RC (time constant).

(27-36)

From  Eq. 27-33, we  can  now  see  that  at  time  t ! t (!  RC), the  charge  on  the
initially uncharged capacitor of Fig. 27-15 has increased from zero to

q ! C #(1 # e#1) ! 0.63C #.

(27-37)

In words, during the first time constant t the charge has increased from zero to
63% of its final value C #. In Fig. 27-16, the small triangles along the time axes
mark successive intervals of one time constant during the charging of the capaci-
tor. The charging times for RC circuits are often stated in terms of t. For example,
a  circuit  with  t ! 1 ms  charges  quickly  while  one  with  t ! 100  s  charges  much
more slowly,

Discharging a Capacitor
Assume  now  that  the  capacitor  of  Fig. 27-15  is  fully  charged  to  a  potential  V0
equal to the emf # of the battery. At a new time t ! 0, switch S is thrown from a to
b so that the capacitor can discharge through resistance R. How do the charge
q(t) on the capacitor and the current i(t) through the discharge loop of capacitor
and resistance now vary with time?

The  differential  equation  describing  q(t)  is  like  Eq. 27-32  except  that  now,

with no battery in the discharge loop, # ! 0. Thus,

R

dq
dt

%

q
C

! 0

(discharging equation).

(27-38)

The solution to this differential equation is

q ! q0e#t/RC

(discharging a capacitor),

(27-39)

where q0 (! CV0) is the initial charge on the capacitor. You can verify by substitu-
tion that Eq. 27-39 is indeed a solution of Eq. 27-38.

27-4 RC CI RCU ITS

791

Equation 27-39 tells us that q decreases exponentially with time, at a rate that
is  set  by  the  capacitive  time  constant  t ! RC. At  time  t ! t, the  capacitor’s
charge has been reduced to q0e#1, or about 37% of the initial value. Note that a
greater t means a greater discharge time.

Differentiating Eq. 27-39 gives us the current i(t):

i !

dq
dt

! ## q0

RC $e#t/RC

(discharging a capacitor).

(27-40)

This tells us that the current also decreases exponentially with time, at a rate set
by t. The initial current i0 is equal to q0/RC. Note that you can find i0 by simply
applying the loop rule to the circuit at t ! 0; just then the capacitor’s initial poten-
tial V0 is connected across the resistance R, so the current must be i0 ! V0/R !
(q0/C)/R ! q0/RC. The minus sign in Eq. 27-40 can be ignored; it merely means
that the capacitor’s charge q is decreasing.

Derivation of Eq. 27-33
To solve Eq. 27-32, we first rewrite it as

dq
dt

%

q
RC

!

#
R

.

The general solution to this differential equation is of the form

q ! qp % Ke#at,

(27-41)

(27-42)

where qp is a particular solution of the differential equation, K is a constant to
be evaluated from the initial conditions, and a ! 1/RC is the coefficient of q in
Eq. 27-41. To  find  qp, we  set  dq/dt ! 0  in  Eq. 27-41  (corresponding  to  the  final
condition of no further charging), let q ! qp, and solve, obtaining

qp ! C #.

(27-43)

To evaluate K, we first substitute this into Eq. 27-42 to get

q ! C # % Ke#at.

Then substituting the initial conditions q ! 0 and t ! 0 yields

0 ! C # % K,

or K ! #C #. Finally, with the values of qp, a, and K inserted, Eq. 27-42 becomes

which, with a slight modification, is Eq. 27-33.

q ! C # # C #e#t/RC,

Checkpoint 5

The table gives four sets of values for the circuit elements in Fig. 27-15. Rank the
sets according to (a) the initial current (as the switch is closed on a) and (b) the time
required for the current to decrease to half its initial value, greatest first.

# (V)
R (0)
C (mF)

1

12
2
3

2

12
3
2

3

10
10

0.5

4

10
5
2

792

CHAPTE R  27 CI RCU ITS

Sample Problem 27.05 Discharging an RC circuit to avoid a fire in a race car pit stop

As  a  car  rolls  along  pavement, electrons  move  from  the
pavement first onto the tires and then onto the car body. The
car stores this excess charge and the associated electric poten-
tial energy as if the car body were one plate of a capacitor and
the pavement were the other plate (Fig. 27-17a). When the car
stops, it discharges its excess charge and energy through the
tires, just as a capacitor can discharge through a resistor. If a
conducting object comes within a few centimeters of the car
before  the  car  is  discharged, the  remaining  energy  can  be
suddenly  transferred  to  a  spark  between  the  car  and  the
object. Suppose the conducting object is a fuel dispenser. The
spark  will  not  ignite  the  fuel  and  cause  a  fire  if  the  spark
energy is less than the critical value Ufire ! 50 mJ.

When the car of Fig. 27-17a stops at time t ! 0, the car –
ground  potential  difference  is  V0 ! 30 kV. The  car – ground
capacitance  is  C ! 500 pF, and  the  resistance  of  each tire  is
Rtire ! 100 G0. How much time does the car take to discharge
through the tires to drop below the critical value Ufire?

KEY IDEAS

(1) At any time t, a capacitor’s stored electric potential energy U
is  related  to  its  stored  charge  q according  to  Eq. 25-21  (U !
q2/2C). (2)  While  a  capacitor  is  discharging, the  charge  de-
creases with time according to Eq. 27-39 (q ! q0e#t/RC).

Calculations: We  can  treat  the  tires  as  resistors  that  are
connected to one another at their tops via the car body and
at their bottoms via the pavement. Figure 27-17b shows how
the four resistors are connected in parallel across the car’s
capacitance, and  Fig. 27-17c shows  their  equivalent  resist-
ance R. From Eq. 27-24, R is given by
1
Rtire

1
Rtire

1
Rtire

1
Rtire

1
R

!

%

%

%

,

or

R !

Rtire
4

!

100 $ 10 9 0
4

! 25 $ 10 9 0.

(27-44)

When  the  car  stops, it  discharges  its  excess  charge  and
energy through R. We now use our two Key Ideas to analyze
the discharge. Substituting Eq. 27-39 into Eq. 25-21 gives

U !

!

q2
2C
2
q0
2C

!

(q0e#t/RC)2
2C

e#2t/RC.

(27-45)

From Eq. 25-1 (q ! CV ), we can relate the initial charge q0
on the car to the given initial potential difference V0: q0 !
CV0. Substituting this equation into Eq. 27-45 brings us to

U !

(CV0)2
2C

e#2t/RC !

2
CV 0
2

e#2t/RC,

MDOG
PST4
XP3I

WNFR

True Vales

RPM
3N

Schtuff
Bomman

Effective
capacitance

DRIVE    THRU
DRIVE    THRU

ULTRA

6

MOTEL

Tire
resistance

R tire

R tire

C

R tire

R tire

C

R

(a)

(b)

Figure 27-17 (a) A charged car and the
pavement acts like a capacitor that can
discharge through the tires. (b) The
effective circuit of the car – pavement
capacitor, with four tire resistances Rtire
connected in parallel. (c) The equivalent
resistance R of the tires. (d) The electric
potential energy U in the car – pavement
capacitor decreases during discharge.

or

e#2t/RC !

2U
2 .
CV 0

(c)

U

100 GΩ

10 GΩ

0.94

9.4

t (s)

Ufire

(d)

(27-46)

Taking the natural logarithms of both sides, we obtain

#

2t
RC

! ln# 2U

2 $,
CV0

or

t ! #

RC
2

 ln# 2U

2 $.
CV0

(27-47)

Substituting  the  given  data, we  find  that  the  time  the  car
takes to discharge to the energy level Ufire ! 50 mJ is

t ! #

(25 $ 10 9 0)(500 $ 10 #12 F)
2

$ ln#

2(50 $ 10 #3 J)
(500 $ 10 #12 F)(30 $ 10 3 V)2 $

! 9.4 s.

(Answer)

Fire or no fire: This car requires at least 9.4 s before fuel can be
brought safely near it. A pit crew cannot wait that long. So the
tires include some type of conducting material (such as carbon
black)  to  lower  the  tire  resistance  and  thus  increase  the  dis-
charge  rate. Figure  27-17d shows  the  stored  energy  U versus
time t for tire resistances of R ! 100 G0 (our value) and R !
10 G0. Note how much more rapidly a car discharges to level
Ufire with the lower R value.

Additional examples, video, and practice available at WileyPLUS

Review & Summary

Emf An emf device does work on charges to maintain a potential
difference between its output terminals. If dW is the work the device
does to force positive charge dq from the negative to the positive ter-
minal, then the emf (work per unit charge) of the device is

# !

dW
dq

(definition of #).

(27-1)

The volt is the SI unit of emf as well as of potential difference.An ideal
emf device is one that lacks any internal resistance. The potential dif-
ference between its terminals is equal to the emf. A real emf device
has internal resistance. The potential difference between its terminals
is equal to the emf only if there is no current through the device.

Analyzing  Circuits The  change  in  potential  in  traversing  a
resistance R in the direction of the current is #iR; in the opposite
direction it is %iR (resistance rule). The change in potential in tra-
versing an ideal emf device in the direction of the emf arrow is %#;
in  the  opposite  direction  it  is  ## (emf  rule). Conservation  of
energy leads to the loop rule:

Loop Rule. The algebraic sum of the changes in potential encountered
in a complete traversal of any loop of a circuit must be zero.

Conservation of charge gives us the junction rule:

Junction  Rule. The  sum  of  the  currents  entering  any  junction
must be equal to the sum of the currents leaving that junction.

Single-Loop Circuits The current in a single-loop circuit con-
taining a single resistance R and an emf device with emf # and in-
ternal resistance r is

i !

#
R % r

,

which reduces to i ! #/R for an ideal emf device with r ! 0.

QU ESTIONS

793

where V is the potential across the terminals of the battery. The rate
Pr at which energy is dissipated as thermal energy in the battery is

Pr ! i2r.

(27-16)

The rate Pemf at which the chemical energy in the battery changes is

Pemf ! i#.

(27-17)

Series Resistances When resistances are in series, they have
the same current. The equivalent resistance that can replace a se-
ries combination of resistances is

n

Req ! ’

j!1

Rj

(n resistances in series).

(27-7)

Parallel  Resistances When  resistances  are  in  parallel,
they have the same potential difference. The equivalent resistance
that can replace a parallel combination of resistances is given by

1
Req

n

! ’

j!1

1
Rj

(n resistances in parallel).

(27-24)

RC Circuits When an emf # is applied to a resistance R and ca-
pacitance C in series, as in Fig. 27-15 with the switch at a, the charge
on the capacitor increases according to

q ! C #(1 # e#t/RC)

(charging a capacitor),

(27-33)

in which C # ! q0 is the equilibrium (final) charge and RC ! t is the ca-
pacitive time constant of the circuit. During the charging, the current is

i !

dq
dt

! # #

R $e#t/RC

(charging a capacitor).

(27-34)

(27-4)

When a capacitor discharges through a resistance R, the charge on
the capacitor decays according to

Power When  a  real  battery  of  emf # and  internal  resistance  r
does work on the charge carriers in a current i through the battery,
the rate P of energy transfer to the charge carriers is

P ! iV,

(27-14)

q ! q0e#t/RC

(discharging a capacitor).

(27-39)

During the discharging, the current is

i !

dq
dt

! ## q0

RC $e#t/RC

(discharging a capacitor).

(27-40)

Questions

(
1 (a)  In  Fig. 27-18a, with  R1 R2, is  the  potential  difference

+
–

(a)

R1

(c)

R3

R2

R1

R1

R2

R3

–
+

(b)

R1

–
+

R3

R3

+
–

R2

(d)

R2

Figure 27-18 Questions 1 and 2.

across R2 more than, less than, or equal to that across R1? (b) Is the
current through resistor R2 more than, less than, or equal to that
through resistor R1?
2 (a)  In  Fig. 27-18a, are  resistors  R1 and R3 in  series?  (b) Are
resistors R1 and R2 in parallel? (c) Rank the equivalent resistances
of the four circuits shown in Fig. 27-18, greatest first.

3 You are to connect resistors R1 and R2, with R1 ( R2, to a bat-
tery, first  individually, then  in  series, and  then  in  parallel. Rank
those arrangements according to the amount of current through the
battery, greatest first.

4 In Fig. 27-19, a circuit consists of
a battery and two uniform resistors,
and the section lying along an x axis
is divided into five segments of equal
lengths. (a) Assume that R1 ! R2 and
rank  the  segments  according  to  the
magnitude  of  the  average  electric

+  –

R1

R2

x

a

b

c  d

e

Figure 27-19 Question 4.

794

CHAPTE R  27 CI RCU ITS

field in them, greatest first. (b) Now assume that R1 ( R2 and then
again rank the segments. (c) What is the direction of the electric
field along the x axis?

5 For each circuit in Fig. 27-20, are the resistors connected in se-
ries, in parallel, or neither?

–

+

+–

(a)

(b)

Figure 27-20 Question 5.

+
–

(c)

6 Res-monster maze. In Fig. 27-21, all the resistors have a resis-
tance  of  4.0  0 and  all  the  (ideal)  batteries  have  an  emf  of  4.0 V.
What is the current through resistor R? (If you can find the proper
loop  through  this  maze, you  can  answer  the  question  with  a  few
seconds of mental calculation.)

C

Figure 27-22 Question 10.

11 Initially, a single resistor R1 is wired to a battery. Then resistor
R2 is added in parallel. Are (a) the potential difference across R1
and (b) the current i1 through R1 now more than, less than, or the
same as previously? (c) Is the equivalent resistance R12 of R1 and
R2 more  than, less  than, or  equal  to  R1?  (d)  Is  the  total  current
through R1 and R2 together more than, less than, or equal to the
current through R1 previously?
12 After the switch in Fig. 27-15 is closed on point a, there is cur-
rent i through resistance R. Figure 27-23 gives that current for four
sets of values of R and capacitance C: (1) R0 and C0, (2) 2R0 and C0,
(3) R0 and 2C0, (4) 2R0 and 2C0. Which set goes with which curve?

R

i

c

a

d

Figure 27-21 Question 6.

7 A  resistor  R1 is  wired  to  a  battery, then  resistor  R2 is  added
in series. Are  (a)  the  potential  difference  across  R1 and  (b)  the
current i1 through R1 now more than, less than, or the same as pre-
viously?  (c)  Is  the  equivalent  resistance  R12 of R1 and R2 more
than, less than, or equal to R1?

8 What is the equivalent resistance of three resistors, each of
resistance R, if they are connected to an ideal battery (a) in se-
ries with one another and (b) in parallel with one another? (c)
Is  the  potential  difference  across  the  series  arrangement
greater  than, less  than, or  equal  to  that  across  the  parallel
arrangement?

9 Two resistors are wired to a battery. (a) In which arrangement,
parallel or series, are the potential differences across each resistor
and  across  the  equivalent  resistance  all  equal?  (b)  In  which
arrangement  are  the  currents  through  each  resistor  and  through
the equivalent resistance all equal?

10 Cap-monster  maze. In  Fig. 27-22, all  the  capacitors  have  a
capacitance  of  6.0 mF, and  all  the  batteries  have  an  emf  of  10 V.
What is the charge on capacitor C? (If you can find the proper loop
through this maze, you can answer the question with a few seconds
of mental calculation.)

Figure 27-23 Question 12.

b

t

13 Figure 27-24 shows three sections of circuit that are to be con-
nected in turn to the same battery via a switch as in Fig. 27-15. The
resistors are all identical, as are the capacitors. Rank the sections
according to (a) the final (equilibrium) charge on the capacitor and
(b)  the  time  required  for  the  capacitor  to  reach  50%  of  its  final
charge, greatest first.

(1)

(2)

(3)

Figure 27-24 Question 13.

Problems

Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign

SSM Worked-out solution available in Student Solutions Manual
• – ••• Number of dots indicates level of problem difficulty

WWW Worked-out solution is at

ILW Interactive solution is at

http://www.wiley.com/college/halliday

Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com

PROB LE M S

795

SSM

WWW

Module 27-1 Single-Loop Circuits
In Fig. 27-25, the ideal
•1
#1 ! 12
V  and
batteries  have  emfs
#2 ! 6.0
V. What  are  (a)  the  current,
the dissipation rate in (b) resistor 1 (4.0
) and (c) resistor 2 (8.0 0), and the en-
0
ergy  transfer  rate  in  (d)  battery  1  and
(e) battery 2? Is energy being supplied
or absorbed by (f) battery 1 and (g) bat-
tery 2?

•2 In  Fig. 27-26, the  ideal  batteries
have  emfs  #1 ! 150 V  and  #2 ! 50 V
and  the  resistances  are  R1 ! 3.0 0 and
R2 ! 2.0 0. If the potential at P is 100 V,
what is it at Q?

+
–

Q

–
+

R1

2

R2

1

– +

Figure 27-25
Problem 1.

R1

1

2

R2

ILW

A  car  battery  with  a  12 V  emf
•3
is
and an internal resistance of 0.040
being  charged  with  a  current  of  50 A.
What  are  (a)  the  potential  difference  V across  the  terminals, (b)
the rate Pr of energy dissipation inside the battery, and (c) the rate
Pemf of energy conversion to chemical form? When the battery is
used to supply 50 A to the starter motor, what are (d) V and (e) Pr?

Figure 27-26 Problem 2.

0

Figure 27-27 shows a circuit of four resistors that are con-
•4
nected  to  a  larger  circuit. The  graph  below  the  circuit  shows  the
electric potential V(x) as a function of position x along the lower
branch of the circuit, through resistor 4; the potential VA is 12.0 V.
The  graph  above  the  circuit  shows  the  electric  potential  V(x)
versus  position  x along  the  upper  branch  of  the  circuit, through
resistors 1, 2, and 3; the potential differences are ’VB ! 2.00 V and
’VC ! 5.00 V. Resistor  3  has  a  resistance  of  200  0. What  is  the
resistance of (a) resistor 1 and (b) resistor 2?

∆VB

∆VC

V

0

1

2

3

4

x

x

Figure 27-27
Problem 4.

)
V
(
V

VA

0

•6 A  standard  flashlight  battery  can  deliver  about  2.0 W &h  of
energy before it runs down. (a) If a battery costs US$0.80, what is
the  cost  of  operating  a  100 W  lamp  for  8.0 h  using  batteries?
(b) What is the cost if energy is provided at the rate of US$0.06 per
kilowatt-hour?

•7 A wire of resistance 5.0 0 is connected to a battery whose emf
# is 2.0 V and whose internal resistance is 1.0 0. In 2.0 min, how
much energy is (a) transferred from chemical form in the battery,
(b) dissipated as thermal energy in the wire, and (c) dissipated as
thermal energy in the battery?

•8 A certain car battery with a 12.0 V emf has an initial charge of
120 A &h. Assuming  that  the  potential  across  the  terminals  stays
constant until the battery is completely discharged, for how many
hours can it deliver energy at the rate of 100 W?

•9 (a)  In  electron-volts, how  much  work  does  an  ideal  battery
with a 12.0 V emf do on an electron that passes through the battery
from the positive to the negative terminal? (b) If 3.40 $ 10 18 elec-
trons pass through each second, what is the power of the battery in
watts?

••10 (a)  In  Fig. 27-28, what  value
must R have  if  the  current  in  the
circuit is to be 1.0 mA? Take #1 ! 2.0
V, #2 ! 3.0 V, and r1 ! r2 ! 3.0 0. (b)
What is the rate at which thermal en-
ergy appears in R?

+
–

1

r1

R

+
–

2

r2

–
+

P

it

is

SSM

current
in  the

Figure 27-28 Problem 10.

In Fig. 27-29, circuit sec-
••11
tion AB absorbs energy at a rate of
i ! 1.0 A
50 W  when
indicated
through
direction. Resistance R ! 2.0 0. (a)
What is the potential difference be-
tween A and B? Emf device X lacks
internal  resistance. (b)  What  is  its
emf? (c) Is point B connected to the positive terminal of X or to
the negative terminal?

Figure 27-29 Problem 11.

A

B

X

R

i

Wire 1

••12 Figure  27-30  shows  a  resistor  of  resis-
tance R ! 6.00 0 connected to an ideal battery
of  emf  # ! 12.0 V  by  means  of  two  copper
wires. Each wire has length 20.0 cm and radius
1.00 mm. In  dealing  with  such  circuits  in  this
chapter, we  generally  neglect  the  potential
differences along the wires and the transfer of
energy  to  thermal  energy  in  them. Check
the validity  of  this  neglect  for  the  circuit  of
Fig. 27-30: What  is  the potential  difference
across (a) the resistor and (b) each of the two sections of wire?
At what rate is energy lost to thermal energy in (c) the resistor
and (d) each section of wire?

Figure 27-30
Problem 12.

R

Wire 2

•5 A 5.0 A current is set up in a circuit for 6.0 min by a recharge-
able battery with a 6.0 V emf. By how much is the chemical energy
of the battery reduced?

••13 A  10-km-long  underground  cable  extends  east  to  west  and
consists of two parallel wires, each of which has resistance 13
/km.
An electrical short develops at distance x from the west end when

0

796

CHAPTE R  27 CI RCU ITS

a  conducting  path  of  resistance  R
connects the wires (Fig. 27-31). The
resistance of the wires and the short
is  then  100  0 when  measured  from
the east end and 200 0 when meas-
ured  from  the  west  end. What  are
(a) x and (b) R?

Conducting
path

East

West

x

Figure 27-31 Problem 13.

In Fig. 27-32a, both batteries have emf # ! 1.20 V and the
••14
external resistance R is a variable resistor. Figure 27-32b gives the
electric potentials V between the terminals of each battery as func-
tions  of  R: Curve  1  corresponds  to  battery  1, and  curve  2  corre-
sponds to battery 2. The horizontal scale is set by Rs ! 0.20 0. What
is the internal resistance of (a) battery 1 and (b) battery 2?

1

2

+
–

+
–

R

)
V
(
V

0.5

0

–0.3

(a)

1

2

Rs

R (Ω)

(b)

Figure 27-32 Problem 14.

ILW

••15
is 5.0 A. When an additional resistance of 2.0
with R, the current drops to 4.0 A. What is R?

The current in a single-loop circuit with one resistance R
is inserted in series

0

•••16 A solar cell generates a potential difference of 0.10 V when
a 500 0 resistor is connected across it, and a potential difference of
0.15 V when a 1000 0 resistor is substituted. What are the (a) inter-
nal resistance and (b) emf of the solar cell? (c) The area of the cell is
5.0 cm2, and the rate per unit area at which it receives energy from
light is 2.0 mW/cm2. What is the efficiency of the cell for converting
light energy to thermal energy in the 1000 0 external resistor?

0

and battery 2 has emf

V  and  internal  resistance  r1
#2 ! 12.0
0

In Fig. 27-33, battery 1 has emf
•••17
SSM
#1 ! 12.0
!
V
0.016
and  internal  resistance  r2
. The
batteries are connected in series with an ex-
ternal resistance R. (a) What R value makes
the  terminal-to-terminal  potential  differ-
ence of one of the batteries zero? (b) Which
battery is that?

0.012

!

+
–

+
–

r1

r 2

1

2

R

Figure 27-33
Problem 17.

Module 27-2 Multiloop Circuits
•18 In Fig. 27-9, what is the potential difference Vd # Vc between
points d and c if #1 ! 4.0 V, #2 ! 1.0 V, R1 ! R2 ! 10 0, and R3 !
5.0 0, and the battery is ideal?

•19 A total resistance of 3.00 0 is to be produced by connecting
an unknown resistance to a 12.0 0 resistance. (a) What must be the
value of the unknown resistance, and (b) should it be connected in
series or in parallel?

•20 When resistors 1 and 2 are connected in series, the equivalent
resistance  is  16.0  0. When  they  are  connected  in  parallel, the
equivalent resistance is 3.0 0. What are (a) the smaller resistance
and (b) the larger resistance of these two resistors?

•21 Four  18.0  0 resistors  are  con-
nected  in  parallel  across  a  25.0 V
ideal  battery. What  is  the  current
through the battery?

•22 Figure  27-34  shows  five  5.00  0
resistors. Find  the  equivalent  resis-
tance between points (a) F and H and
(b) F and G. (Hint: For  each  pair  of
points, imagine  that  a  battery  is  con-
nected across the pair.)
•23 In  Fig. 27-35, R1 ! 100 0, R2 !
50 0, and  the  ideal  batteries  have
emfs #1 ! 6.0 V, #2 ! 5.0 V,
and
#3 ! 4.0 V. Find (a) the current in re-
sistor  1, (b)  the  current  in  resistor  2,
and  (c)  the  potential  difference  be-
tween points a and b.
•24 In  Fig. 27-36, R1 ! R2 ! 4.00 0
and R3 ! 2.50 0. Find the equivalent
resistance  between  points  D and E.
(Hint: Imagine  that  a  battery  is  con-
nected across those points.)

SSM

Nine copper wires of length
•25
l and diameter d are connected in par-
allel  to  form  a  single  composite  con-
ductor  of  resistance  R. What  must  be
the diameter D of a single copper wire
of length l if it is to have the same re-
sistance?

R

R

H

R

R

R

G

Figure 27-34 Problem 22.

+ –

1

R2

b

+ –

3

+ –

2
R1

Figure 27-35 Problem 23.

R1

R2

R 3

E

F

a

D

Figure 27-36 Problem 24.

R

x

Sliding
contact

I

R0

+ –

Lightning
current

Figure 27-37 Problem 26.

••26 Figure  27-37  shows  a  battery
connected  across  a  uniform  resistor
R0. A sliding contact can move across
the resistor from x ! 0 at the left to
x ! 10  cm  at  the  right. Moving
the contact changes how much resist-
ance is to the left of the contact and
how  much  is  to  the  right. Find  the
rate  at  which  energy  is  dissipated  in
resistor R as a function of x. Plot the
function  for  # ! 50 V, R ! 2000 0,
and R0 ! 100 0.
Side  flash. Figure  27-38
••27
indicates  one  reason  no  one  should
stand under a tree during a lightning
storm. If  lightning  comes  down  the
side  of  the  tree, a  portion  can  jump
over  to  the  person, especially  if  the
current on the tree reaches a dry re-
gion on the bark and thereafter must
travel  through  air  to  reach  the
ground. In the figure, part of the lightning jumps through distance
d in  air  and  then  travels  through  the  person  (who  has  negligible
resistance relative to that of air because of the highly conducting
salty fluids within the body). The rest of the current travels through
air alongside the tree, for a distance h. If d/h ! 0.400 and the total
current is I ! 5000 A, what is the current through the person?

Figure 27-38 Problem 27.

d

h

••28 The ideal battery in Fig. 27-39a has emf # ! 6.0 V. Plot 1 in
Fig. 27-39b gives the electric potential difference V that can appear
across resistor 1 versus the current i in that resistor when the resistor

is individually tested by putting a variable potential across it. The
scale of the V axis is set by Vs ! 18.0 V, and the scale of the i axis is
set by is ! 3.00 m1. Plots 2 and 3 are similar plots for resistors 2
and 3, respectively, when they are individually tested by putting a
variable potential across them. What is the current in resistor 2 in
the circuit of Fig. 27-39a?

R3

+
–

R1

R2

(a)

Vs

)
V
(
V

1

2

3

0

(b)

is

i (mA)

Figure 27-39 Problem 28.

••29 In  Fig. 27-40, R1 ! 6.00 0,
R2 ! 18.0 0, and  the  ideal  battery
has  emf  # ! 12.0 V. What  are  the
(a) size  and  (b)  direction  (left  or
right)  of  current  i1?  (c)  How  much
energy is dissipated by all four resis-
tors in 1.00 min?

In  Fig. 27-41, the  ideal
••30
#1 ! 10.0
V and
batteries have emfs
!#
0.500 1, and the resistances are
2
each  4.00
. What  is  the  current  in
(a) resistance 2 and (b) resistance 3?

#
0

+  –

R 2

i1
R2

R 1

R2

Figure 27-40 Problem 29.

R1

R2

+
–

1

R3

2

+
–

SSM

!#
1

#2 ! 12
0

In  Fig. 27-42, the
••31
ideal batteries have emfs
5.0 V
V, the  resistances  are
and
each  2.0
, and  the  potential  is  de-
fined  to  be  zero  at  the  grounded
point of the circuit. What are poten-
tials  (a)  V1 and  (b)  V2 at  the  indi-
cated points?

Figure 27-41 Problems 30, 41,
and 88.

+
–

••32 Both  batteries  in  Fig. 27-43a
are  ideal. Emf  #1 of  battery  1  has  a
fixed  value, but  emf  #2 of  battery  2
can  be  varied  between  1.0 V  and  10
V. The  plots  in  Fig. 27-43b give  the
currents through the two batteries as
a function of #2. The vertical scale is
set  by  is ! 0.20 A. You  must  decide
which plot corresponds to which battery, but for both plots, a nega-
tive current occurs when the direction of the current through the

Figure 27-42 Problem 31.

+
–
V1

V2

2

1

+
–

2

(a)

R1

1

+
–

R 2

)
A
(

t
n
e
r
r
u
C

is

0

–is

5

10

(b)
Figure 27-43 Problem 32.

2 (V)

PROB LE M S

797

battery is opposite the direction of that battery’s emf. What are (a)
emf #1, (b) resistance R1, and (c) resistance R2?

••33
and the resistances are R1 R2 R3
8.00

!!!
0
, and R6 ! 4.00 0. What is the emf of the ideal battery?

In  Fig. 27-44, the  current  in  resistance  6  is  i6 ! 1.40 A
!

2.00

16.0

, R4

, R5

!

0

0

R1

R2

R5

R3

R4

i 6

R6

+
–

Figure 27-44 Problem 33.

••34 The resistances in Figs. 27-45a and b are all 6.0 0, and the batter-
ies are ideal 12 V batteries. (a) When switch S in Fig. 27-45a is closed,
what is the change in the electric potential V1 across resistor 1, or does
V1 remain the same? (b) When switch S in Fig. 27-45b is closed, what is
the change in V1 across resistor 1, or does V1 remain the same?

+
–

S

R1

(a)

R 2

R 3

+
–

Figure 27-45 Problem 34.

S

R1

(b)

R2

R1

R 2

A

R3

D

R1

R2

B

C

+
–

Figure 27-46 Problem 35.

A

R2

1

R1

+
–

R3

+
–

2

Figure 27-47 Problem 36.

R 1

+
–

R 2

R 3

Figure 27-48 Problems 37
and 98.

R1

A

R2

R3

i

Box

B

Figure 27-49 Problem 38.

, R2

2000
4000

In  Fig. 27-46, # ! 12.0 V,
••35
!
0
R1
, and
3000
!
R3
. What  are  the  potential
#
differences (a) VA VB, (b) VB # VC,
(c) VC # VD, and (d) VA # VC?

!

0

0

100

#1 ! 6.00
V,
In  Fig. 27-47,
••36
R2 ! 200 0,
#2 ! 12.0
!
0
V, R1
,
!
0
and R3
. One point of the cir-
300
cuit  is  grounded  (V ! 0). What  are
the  (a)  size  and  (b)  direction  (up  or
down)  of  the  current  through  resist-
ance  1, the  (c)  size  and  (d)  direction
(left  or  right)  of  the  current  through
resistance  2, and  the  (e)  size  and
(f) direction  of  the  current  through
resistance  3?  (g) What  is  the  electric
potential at point A?

••37 In  Fig. 27-48, the  resistances
are R1 ! 2.00 0, R2 ! 5.00 0, and the
battery  is  ideal. What  value  of  R3
maximizes  the  dissipation  rate  in
resistance 3?

is

current

••38 Figure 27-49 shows a section of
a circuit. The resistances are R1 ! 2.0
0, R2 ! 4.0 0, and R3 ! 6.0 0, and the
i ! 6.0 A.
indicated
The  electric  potential  difference  be-
tween  points  A and B that  connect
the section to the rest of the circuit is
VA # VB ! 78 V. (a) Is the device rep-
resented by “Box” absorbing or pro-
viding energy to the circuit, and (b) at
what rate?

798

CHAPTE R  27 CI RCU ITS

# ! 12.0

In  Fig. 27-50, two  batteries  with  an
••39
V  and  an  internal  resistance
emf
r ! 0.300 0 are  connected  in  parallel  across
a resistance  R. (a)  For  what  value  of  R is  the
dissipation  rate  in  the  resistor  a  maximum?
(b) What is that maximum?

0

!

0.200

Two  identical  batteries  of  emf  # !
••40
12.0 V  and  internal  resistance  r
are
to  be  connected  to  an  external  resistance  R,
either  in  parallel  (Fig. 27-50)  or  in  series
(Fig. 27-51). If  R ! 2.00r, what  is  the  current  i
in the  external  resistance  in  the  (a)  parallel
and (b)  series  arrangements?  (c) For  which
arrangement  is  i greater?  If  R !
r/2.00, what is i in the external resist-
ance in the (d) parallel arrangement
and  (e)  series  arrangement?  (f)  For
which arrangement is i greater now?

+  –

+  –

+  –

r

r

R

Figure 27-50
Problems 39
and 40.

+  –

r

r

••41 In Fig. 27-41, #1 ! 3.00 V, #2 !
1.00 V, R1 ! 4.00 0, R2 ! 2.00 0, R3 !
5.00 0, and  both  batteries  are  ideal.
What is the rate at which energy is dis-
sipated in (a) R1, (b) R2, and (c) R3? What is the power of (d) battery
1 and (e) battery 2?

Figure 27-51 Problem 40.

R

••42 In Fig. 27-52, an array of n par-
allel resistors is connected in series to
a resistor and an ideal battery. All the
resistors  have  the  same  resistance. If
an  identical  resistor  were  added  in
parallel to the parallel array, the cur-
rent
the  battery  would
change  by  1.25%. What  is  the  value
of n?

through

R

R

R

n resistors
in parallel

Figure 27-52 Problem 42.

••43 You are given a number of 10 0 resistors, each capable of
dissipating only 1.0 W without being destroyed. What is the mini-
mum number of such resistors that you need to combine in series
or  in  parallel  to  make  a  10  0 resist-
ance  that  is  capable  of  dissipating  at
least 5.0 W?

R1

+
–

R4

R2

R3

0

!

, R4

!!

100
0

!
75.0

In  Fig. 27-53, R1
50.0

0
,
••44
R2 R3
, and
the  ideal  battery  has  emf  # ! 6.00 V.
(a) What is the equivalent resistance?
What is i in (b) resistance 1, (c) resist-
ance 2, (d) resistance 3, and (e) resist-
ance 4?

Figure 27-53
Problems 44 and 48.

R1

R1

a

0

!

!

+
–

ILW

2.0

+
–3

In Fig. 27-54, the resistances
••45
0
are R1
and  R2
,
1.0
and  the  ideal  batteries  have  emfs
#1 ! 2.0 V and #2 ! #3 ! 4.0 V. What
are  the  (a)  size  and  (b)  direction  (up
or  down)  of  the  current  in  battery  1,
the  (c)  size  and  (d)  direction  of  the
current  in  battery  2, and  the  (e)  size
and (f) direction of the current in battery 3? (g) What is the poten-
tial difference Va # Vb?

Figure 27-54 Problem 45.

R2

R1

R1

+
–

b

2

1

through  the  battery  as  a  function  of  R3. The  horizontal  scale  is
set by R3s ! 20 0. The curve has an asymptote of 2.0 mA as R3 :
,. What are (a) resistance R1 and (b) resistance R2?

)
A
m
(
i

6

4

2

0

R 1

R2

+
–

R3

(a)

R 3s

R3 (Ω)
(b)

Figure 27-55 Problem 46.

SSM

A  copper  wire  of  radius  a ! 0.250 mm  has  an  alu-
•••47
!
0.380 mm. There is a current i !
minum jacket of outer radius b
2.00 A in the composite wire. Using Table 26-1, calculate the cur-
rent in (a) the copper and (b) the aluminum. (c) If a potential dif-
ference V ! 12.0 V between the ends maintains the current, what
is the length of the composite wire?

!

4.00

12.0

, and  R3

In Fig. 27-53, the resistors have the values R1 ! 7.00 0,
•••48
!
0
R2
, and  the  ideal  battery’s  emf  is
# ! 24.0 V. For what value of R4 will the rate at which the battery
transfers energy to the resistors equal (a) 60.0 W, (b) the maximum
possible rate Pmax, and (c) the minimum possible rate Pmin? What
are (d) Pmax and (e) Pmin?

0

The Ammeter and

Module 27-3
the Voltmeter
(a) In Fig. 27-56, what cur-
••49
ILW
# !
rent  does  the  ammeter  read  if
5.0 V (ideal battery), R1 ! 2.0 0, R2 !
4.0 0, and  R3 ! 6.0 0?  (b) The  am-
meter  and  battery  are  now  inter-
changed. Show  that
the  ammeter
reading is unchanged.

+
–

R1

A

R2

R3

Figure 27-56 Problem 49.

!

••50 In  Fig. 27-57, R1
2.00R, the
ammeter  resistance  is  zero, and  the
battery is ideal. What multiple of #/R
gives the current in the ammeter?

+
–

R1

R

A

R

R

R

A

Figure 27-57 Problem 50.

••51 In  Fig. 27-58, a  voltmeter  of
resistance RV ! 300 0 and  an  am-
meter of resistance RA ! 3.00 0 are
being used to measure a resistance
R in a circuit that also contains a re-
sistance R0 ! 100 0 and  an  ideal
battery  with  an  emf  of  # ! 12.0 V.
Resistance R is  given  by  R ! V/i,
where V is  the  potential  across  R
and i is  the  ammeter  reading. The
voltmeter  reading  is  V-, which  is
V plus  the  potential  difference
across the ammeter. Thus, the ratio
of  the  two  meter  readings  is  not  R but  only  an  apparent resist-
ance R- ! V-/i. If R ! 85.0 0, what are (a) the ammeter reading,
(b) the  voltmeter  reading, and  (c)  R-?  (d)  If  RA is  decreased,
does  the difference  between  R- and R increase, decrease, or
remain the same?

Figure 27-58 Problem 51.

+  –

R0

V

••46 In Fig. 27-55a, resistor 3 is a variable resistor and the ideal
battery  has  emf  # ! 12 V. Figure  27-55b gives  the  current  i

••52 A  simple  ohmmeter  is  made  by  connecting  a  1.50 V  flash-
light  battery  in  series  with  a  resistance  R and  an  ammeter  that

S

A

S

Starting
motor

•60 A  capacitor  with  initial  charge  q0 is  discharged  through  a
resistor. What  multiple  of  the  time  constant  t gives  the  time  the
capacitor  takes  to  lose  (a)  the  first  one-third  of  its  charge  and
(b) two-thirds of its charge?

0–1.00
mA

–
+

reads from 0 to 1.00 mA, as shown in
Fig. 27-59. Resistance  R is  adjusted
so  that  when  the  clip  leads  are
shorted together, the meter deflects
to  its  full-scale  value  of  1.00 mA.
What  external  resistance  across  the
leads  results  in  a  deflection  of  (a)
10.0%, (b) 50.0%, and (c) 90.0% of full scale? (d) If the ammeter
has a resistance of 20.0 0 and the internal resistance of the battery
is negligible, what is the value of R?

Figure 27-59 Problem 52.

R

••53 In Fig. 27-14, assume that # ! 3.0 V, r ! 100 0, R1 ! 250 0,
and R2 ! 300 0. If the voltmeter resistance RV is 5.0 k0, what per-
cent error does it introduce into the measurement of the potential
difference across R1? Ignore the presence of the ammeter.

lights  of  a  car  are
••54 When  the
switched  on, an  ammeter  in  series  with
them  reads  10.0 A  and  a  voltmeter
connected  across  them  reads  12.0 V  (Fig.
27-60). When the electric starting motor is
turned  on, the  ammeter  reading  drops  to
8.00 A and the lights dim somewhat. If the
internal resistance of the battery is 0.0500
0 and  that  of  the  ammeter  is  negligible,
what are (a) the emf of the battery and (b)
the  current  through  the  starting  motor
when the lights are on?

Lights

V

+ –

r

Figure 27-60
Problem 54.

••55 In Fig. 27-61, Rs is to be adjusted in
value by moving the sliding contact across
it  until  points  a and b are  brought  to the
same potential. (One tests for this condition by momentarily con-
necting  a  sensitive  ammeter  be-
tween a and b; if these points are at
the  same  potential, the  ammeter
will  not  deflect.)  Show  that  when
this adjustment is made, the follow-
ing  relation  holds: Rx ! RsR2/R1.
An unknown resistance (Rx) can be
measured  in  terms  of  a  standard
(Rs)  using  this  device, which  is
called a Wheatstone bridge.

Sliding contact

R1

R2

Rx

Rs

a

b

R

A

R0

+  –

Figure 27-61 Problem 55.

••56 In  Fig. 27-62, a  voltmeter  of
resistance RV ! 300 0 and  an  am-
meter  of  resistance  RA ! 3.00 0
are being used to measure a resist-
ance R in  a  circuit  that  also  con-
tains  a  resistance  R0 ! 100 0 and
an ideal battery of emf # ! 12.0 V.
Resistance R is  given  by  R ! V/i,
where V is  the  voltmeter  reading
and i is the current in resistance R.
However, the  ammeter  reading  is
not i but rather i-, which is i plus the
current
the  voltmeter.
Thus, the  ratio  of  the  two  meter
readings is not R but only an appar-
ent resistance R- ! V/i-. If R ! 85.0 0, what are (a) the ammeter
reading, (b)  the  voltmeter  reading, and  (c)  R-?  (d)  If  RV is  in-
creased, does the difference between R- and R increase, decrease,
or remain the same?

Figure 27-62 Problem 56.

through

+  –

R0

V

PROB LE M S

799

Module 27-4 RC Circuits
•57 Switch  S  in  Fig. 27-63  is  closed  at
time t ! 0, to  begin  charging  an  initially
uncharged  capacitor  of  capacitance  C !
15.0 mF  through  a  resistor  of  resistance
R ! 20.0 0. At what time is the potential
across  the  capacitor  equal  to  that  across
the resistor?

S

R

+
–

C

Figure 27-63 Problems
57 and 96.

•58 In  an  RC series  circuit, emf  # ! 12.0 V, resistance  R !
1.40 M0, and capacitance C ! 1.80 mF. (a) Calculate the time con-
stant. (b) Find the maximum charge that will appear on the capaci-
tor  during  charging. (c)  How  long  does  it  take  for  the  charge  to
build up to 16.0 mC?

SSM

What  multiple  of  the  time  constant  t gives  the  time
•59
taken by an initially uncharged capacitor in an RC series circuit to
be charged to 99.0% of its final charge?

ILW

A 15.0 k0 resistor and a capacitor are connected in se-
•61
ries, and  then  a  12.0 V  potential  difference  is  suddenly  applied
across them. The potential difference across the capacitor rises to
5.00 V  in  1.30 ms. (a)  Calculate  the  time  constant  of  the  circuit.
(b) Find the capacitance of the capacitor.

R

+
–

••62 Figure 27-64 shows the circuit of
a  flashing  lamp, like  those  attached  to
barrels  at  highway  construction  sites.
The  fluorescent  lamp  L  (of  negligible
capacitance)  is  connected  in parallel
across the capacitor C of an RC circuit.
There  is  a  current  through  the  lamp
only  when  the  potential  difference
across  it  reaches  the  breakdown  volt-
age VL; then the capacitor discharges completely through the lamp
and  the  lamp  flashes  briefly. For  a  lamp  with  breakdown  voltage
VL ! 72.0 V, wired to a 95.0 V ideal battery and a 0.150 mF capacitor,
what resistance R is needed for two flashes per second?

Figure 27-64
Problem 62.

L

C

S

!

R1

SSM

WWW

# ! 1.2

In the circuit of Fig.
••63
kV, C 6.5 mF, R1 !
27-65,
R2 ! R3 ! 0.73 M0. With C completely
uncharged, switch  S  is  suddenly  closed
(at t ! 0). At t ! 0, what are (a) current
i1 in resistor 1, (b) current i2 in resistor 2,
and (c) current i3 in resistor 3? At t ! ,
(that  is, after  many  time  constants),
what are (d) i1, (e) i2, and (f) i3? What is the potential difference V2
across resistor 2 at (g) t ! 0 and (h) t ! ,? (i) Sketch V2 versus t be-
tween these two extreme times.

Figure 27-65 Problem 63.

R3

R2

+
–

C

••64 A capacitor with an initial potential difference of 100 V is dis-
charged through a resistor when a switch between them is closed at
t ! 0.At t ! 10.0 s, the potential differ-
ence across the capacitor is 1.00 V. (a)
What  is  the  time  constant  of  the
circuit? (b) What is the potential differ-
ence across the capacitor at t ! 17.0 s?

R2

R1

+
–

C

••65
!
R2

In  Fig. 27-66, R1 ! 10.0 k0,
15.0 k , C 0.400 mF, and  the

!

0

Figure 27-66
Problems 65 and 99.

800

CHAPTE R  27 CI RCU ITS

ideal battery has emf
V. First, the switch is closed a long
time so that the steady state is reached. Then the switch is opened
at time t ! 0. What is the current in resistor 2 at t ! 4.00 ms?

# ! 20.0

C1

••66 Figure 27-67 displays two cir-
cuits  with  a  charged  capacitor  that
is to be discharged through a resis-
tor when a switch is closed. In Fig.
27-67a, R1 ! 20.0 0 and C1 ! 5.00
mF. In Fig. 27-67b, R2 ! 10.0 0 and
C2 ! 8.00 mF. The ratio of the initial
charges  on  the  two  capacitors  is
q02/q01 ! 1.50. At time  t ! 0, both  switches  are  closed. At  what
time t do the two capacitors have the same charge?

Figure 27-67 Problem 66.

(a)

R2

R1

(b)

C 2

SSM

Wires A and B, having equal lengths of 40.0 m and equal
73
diameters  of  2.60 mm, are  connected  in  series. A  potential
difference of 60.0 V is applied between the ends of the composite
wire. The resistances are RA ! 0.127 0 and RB ! 0.729 0. For wire
A, what are (a) magnitude J of the current density and (b) poten-
tial difference V? (c) Of what type material is wire A made (see
Table 26-1)? For wire B, what are (d) J and (e) V? (f) Of what type
material is B made?

74 What are the (a) size and (b) direction (up or down) of cur-
rent i in Fig. 27-71, where all resistances are 4.0 0 and all batteries
are ideal and have an emf of 10 V? (Hint: This can be answered us-
ing only mental calculation.)

••67 The  potential  difference  between  the  plates  of  a  leaky
(meaning  that  charge  leaks  from  one  plate  to  the  other)  2.0  mF
capacitor drops to one-fourth its initial value in 2.0 s. What is the
equivalent resistance between the capacitor plates?

••68 A 1.0 mF capacitor with an initial stored energy of 0.50 J is
discharged through a 1.0 M0 resistor. (a) What is the initial charge
on the capacitor? (b) What is the current through the resistor when
the discharge starts? Find an expression that gives, as a function of
time t, (c) the potential difference VC across the capacitor, (d) the
potential difference VR across the resistor, and (e) the rate at which
thermal energy is produced in the resistor.

A  3.00 M0 resistor  and  a  1.00 mF  capacitor  are
•••69
connected in series with an ideal battery of emf
V.At 1.00 s
after  the  connection  is  made, what  is  the  rate  at  which  (a)  the
charge of the capacitor is increasing, (b) energy is being stored in
the capacitor, (c) thermal energy is appearing in the resistor, and
(d) energy is being delivered by the battery?

# ! 4.00

i

0

Additional Problems
Each  of  the  six  real  batteries  in
70
Fig. 27-68 has an emf of 20 V and a resistance
. (a) What is the current through the
of 4.0
(external) resistance R
4.0  ? (b) What is
the potential difference across each battery?
(c) What is the power of each battery? (d) At
what rate does each battery transfer energy
to internal thermal energy?

!

0

R

Figure 27-68
Problem 70.

0

, R2

20.0

!
!
71 In Fig. 27-69, R1
0
, and the ideal battery has emf
10.0
!
#
120 V. What  is  the  current  at
point a if we close (a) only switch S1,
(b) only switches S1 and S2, and (c) all
three switches?

a

–
+

S1

S2

S3

R1

R1

R1

R1

R2

R2

Figure 27-69 Problem 71.

!

72 In Fig. 27-70, the ideal battery has
emf #
30.0 V, and  the  resistances
!!
0
!
are R1 R2
0
!
0
R5
, R6
1.5
6.0
0

!
, R3 R4
!
, and  R7
.What are currents (a) i2, (b) i4, (c) i1, (d) i3, and (e) i5?

14
2.0

!

i2

i4

R1

i3

R3

R2

R4

+
–

i1

R7

i5

R5

R6

Figure 27-70
Problem 72.

Figure 27-71 Problem 74.

Suppose that, while you are sitting in a chair, charge
75
separation  between  your  clothing  and  the  chair  puts  you  at  a
potential  of  200 V, with  the  capacitance  between  you  and  the
chair  at  150 pF. When  you  stand  up, the increased  separation
between your body and the chair decreases the capacitance to
10 pF. (a) What then is the potential of your body? That poten-
tial  is  reduced  over  time, as  the  charge  on  you  drains  through
your body and shoes (you are a capacitor discharging through a
resistance). Assume  that  the  resistance  along  that  route  is  300
G0. If you touch an electrical component while your potential
is  greater  than  100 V, you  could  ruin  the  component. (b)  How
long must you wait until your potential reaches the safe level of
100 V?

If  you  wear  a  conducting  wrist  strap  that  is  connected  to
ground, your potential does not increase as much when you stand
up; you also discharge more rapidly because the resistance through
the grounding connection is much less than through your body and
shoes. (c) Suppose that when you stand up, your potential is 1400 V
and the chair-to-you capacitance is 10 pF. What resistance in that
wrist-strap grounding connection will allow you to discharge to 100
V in 0.30 s, which is less time than you would need to reach for, say,
your computer?

V, and

In  Fig. 27-72, the  ideal  batteries  have  emfs  #1 ! 20.0 V,
76
0
#2 ! 10.0
.
What are the (a) size and (b) direction (left or right) of current i1?
(c)  Does  battery  1  supply  or  absorb  energy, and  (d)  what  is  its
power? (e) Does battery 2 supply or absorb energy, and (f) what is

V, and the resistances are each 2.00

#3 ! 5.00

its  power?  (g)  Does  battery  3  supply  or  absorb  energy, and  (h)
what is its power?

+–

1

+
–

3

+
–

2

Figure 27-72 Problem 76.

i1

SSM

A  temperature-stable  resistor  is  made  by  connecting  a
77
resistor made of silicon in series with one made of iron. If the re-
quired  total  resistance  is  1000 0 in  a  wide  temperature  range
around 20/C, what should be the resistance of the (a) silicon resis-
tor and (b) iron resistor? (See Table 26-1.)

78 In Fig. 27-14, assume that # ! 5.0 V, r ! 2.0 0, R1 ! 5.0 0, and
R2 ! 4.0 0. If the ammeter resistance RA is 0.10 0, what percent
error  does  it  introduce  into  the  measurement  of  the  current?
Assume that the voltmeter is not present.

#

SSM

An initially uncharged capacitor C is fully charged by a
79
connected  in  series  with  a  resistor  R.
device  of  constant  emf
(a) Show that the final energy stored in the capacitor is half the en-
ergy  supplied  by  the  emf  device. (b)  By  direct  integration  of  i2R
over the charging time, show that the thermal energy dissipated by
the resistor is also half the energy supplied by the emf device.

80 In  Fig. 27-73, R1 ! 5.00 0, R2 !
10.0 0, R3 ! 15.0 0, C1 ! 5.00 mF,
C2 ! 10.0 mF, and  the  ideal  battery
has emf # ! 20.0 V.Assuming that the
circuit is in the steady state, what is the
two
total  energy  stored
capacitors?

the

in

81 In Fig. 27-5a, find the potential
difference  across  R2 if # ! 12 V, R1
! 3.0 0, R2 ! 4.0 0, and R3 ! 5.0 0.

C1

R 1

R 2

C 2

+
–

R3

Figure 27-73 Problem 80.

82 In Fig. 27-8a, calculate the potential difference between a and
c by considering a path that contains R, r1, and #1.

SSM

A  controller  on  an  electronic  arcade  game  consists  of
83
a variable resistor connected across the plates of a 0.220 mF capaci-
tor. The capacitor is charged to 5.00 V, then discharged through the
resistor. The time for the potential difference across the plates to
decrease to 0.800 V is measured by a
clock inside the game. If the range of
discharge times that can be handled
effectively is from 10.0 ms to 6.00 ms,
what  should  be  the  (a)  lower  value
and  (b) higher  value  of  the  resist-
ance range of the resistor?

Tank
unit

Rindicator

Indicator

12 V

+
–

84 An  automobile  gasoline  gauge
is shown schematically in Fig. 27-74.
The  indicator  (on  the  dashboard)
has  a  resistance  of  10  0. The  tank

Connected
through
chassis

Rtank

Figure 27-74 Problem 84.

PROB LE M S

801

unit  is  a  float  connected  to  a  variable  resistor  whose  resistance
varies linearly with the volume of gasoline. The resistance is 140 0
when the tank is empty and 20 0 when the tank is full. Find the
current in the circuit when the tank is (a) empty, (b) half-full, and
(c) full. Treat the battery as ideal.

SSM

The  starting  motor  of  a  car  is  turning  too  slowly, and
85
the mechanic has to decide whether to replace the motor, the ca-
ble, or  the  battery. The  car’s  manual  says  that  the  12 V  battery
should have no more than 0.020 0 internal resistance, the motor no
more than 0.200 0 resistance, and the cable no more than 0.040 0
resistance. The mechanic turns on the motor and measures 11.4 V
across  the  battery, 3.0 V  across  the  cable, and  a  current  of  50 A.
Which part is defective?

86 Two resistors R1 and R2 may be connected either in series or in
parallel across an ideal battery with emf #. We desire the rate of en-
ergy dissipation of the parallel combination to be five times that of
the series combination. If R1 ! 100 0, what are the (a) smaller and
(b) larger of the two values of R2 that result in that dissipation rate?

two

ideal  batteries,

87 The  circuit  of  Fig. 27-75  shows  a
capacitor,
two
resistors, and a switch S. Initially S has
been open for a long time. If it is then
closed  for  a  long  time, what  is  the
change in the charge on the capacitor?
Assume C ! 10 mF, #1 ! 1.0 V, #2 ! 3.0
V, R1 ! 0.20 0, and R2 ! 0.40 0.

88 In  Fig. 27-41, R1 ! 10.0 0, R2 !
20.0 0, and the ideal batteries have emfs
#1 ! 20.0 V  and  #2 ! 50.0 V. What
value of R3 results in no current through
battery 1?

89 In Fig. 27-76, R ! 10 0. What is the
equivalent  resistance  between  points  A
and B?  (Hint: This  circuit  section  might
look simpler if you first assume that points
A and B are connected to a battery.)

90 (a) In Fig. 27-4a, show that the rate
at  which  energy  is  dissipated  in  R as
thermal  energy  is  a  maximum  when
R ! r. (b)  Show  that  this  maximum
power is P ! #2/4r.

91 In  Fig. 27-77, the  ideal  batteries
have  emfs  #1 ! 12.0 V  and  #2 ! 4.00
V, and the resistances are each 4.00 0.
What are the (a) size and (b) direction
(up or down) of i1 and the (c) size and
(d) direction of i2? (e) Does battery 1
supply or absorb energy, and (f) what
is  its  energy  transfer  rate?  (g)  Does
battery 2 supply or absorb energy, and
(h) what is its energy transfer rate?

92 Figure 27-78 shows a portion of a
circuit through which there is a current
I ! 6.00 A. The  resistances  are  R1 !
R2 ! 2.00R3 ! 2.00R4 ! 4.00 0. What
is the current i1 through resistor 1?

93 Thermal  energy  is  to  be  gener-
ated in a 0.10 0 resistor at the rate of

S

1

–
+

R1

–
+

2

R2

C

Figure 27-75 Problem  87.

B

R

2.0R

6.0R

3.0R

4.0R

A

Figure 27-76 Problem 89.

+
–

i1

1

i2

–
+

2

Figure 27-77 Problem 91.

I

i1

R 1

R 2

R 3

R 4

I

Figure 27-78 Problem 92.

802

CHAPTE R  27 CI RCU ITS

10 W by connecting the resistor to a battery whose emf is 1.5 V. (a)
What potential difference must exist across the resistor? (b) What
must be the internal resistance of the battery?

94 Figure 27-79 shows three 20.0 0
resistors. Find  the  equivalent  resist-
ance between points (a) A and B, (b)
A and C, and  (c)  B and C. (Hint:
Imagine  that  a  battery  is  connected
between a given pair of points.)

A

B

C

Figure 27-79 Problem 94.

95 A 120 V power line is protected by a 15 A fuse. What is the
maximum number of 500 W lamps that can be simultaneously op-
erated in parallel on this line without “blowing” the fuse because
of an excess of current?

96 Figure  27-63  shows  an  ideal  battery  of  emf  # ! 12 V,
a resistor of resistance R ! 4.0 0, and an uncharged capacitor of
capacitance C ! 4.0 mF. After switch S is closed, what is the current
through the resistor when the charge on the capacitor is 8.0 mC?

SSM

A group of N identical batteries of emf # and internal re-
97
sistance r may be connected all in series (Fig. 27-80a) or all in par-
allel  (Fig. 27-80b)  and  then  across  a  resistor  R. Show  that  both
arrangements give the same current in R if R ! r.

#3 ! 5.00 V, and #4 ! 5.00 V, and the resistances are each 2.00 0.
What are the (a) size and (b) direction (left or right) of current i1 and
the (c) size and (d) direction of current i2? (This can be answered
with only mental calculation.) (e) At what rate is energy being trans-
ferred in battery 4, and (f) is the energy being supplied or absorbed
by the battery?

101 In  Fig. 27-82, an  ideal  battery
of emf # ! 12.0 V is connected to a
network of resistances R1 ! 6.00 0,
R2 ! 12.0 0, R3 ! 4.00 0, R4 ! 3.00 0,
and R5 ! 5.00 0. What is the poten-
tial difference across resistance 5?

R 1

R 2

R3

R4

R5

+  –

102 The  following  table  gives  the
electric  potential  difference  VT
across the terminals of a battery as a
function  of  current  i being  drawn
from  the  battery. (a) Write  an  equation  that  represents  the  rela-
tionship between VT and i. Enter the data into your graphing calcu-
lator and perform a linear regression fit of VT versus i. From the
parameters of the fit, find (b) the battery’s emf and (c) its internal
resistance.

Figure 27-82 Problem 101.

N batteries in series

i(A):
VT(V):

50.0
10.7

75.0
9.00

100
7.70

125
6.00

150
4.80

175
3.00

200
1.70

+  –

+  –

r

r

+  –

r

R

(a)

N batteries in parallel

+
–

+
–

r

r

+
–

R

r

(b)
Figure 27-80 Problem 97.

In  Fig. 27-48, R1 ! R2
!
98
SSM
0
, and the ideal battery has emf
10.0
# ! 12.0
V. (a)  What  value  of  R3
maximizes the rate at which the bat-
tery supplies energy and (b) what is
that maximum rate?

1

–

+

!

SSM

has

20 k

emf  # ! 30 V,
!
0

In Fig. 27-66, the ideal bat-
99
the
tery
resistances  are  R1
and
0
R2
10 k , and the capacitor is un-
charged. When the switch is closed at
time t ! 0, what is the current in (a)
resistance 1 and (b) resistance 2? (c)
A long time later, what is the current
in resistance 2?

+
–

4

i2

i1

2

+–

+–

3

103 In Fig. 27-83, #1 ! 6.00 V, #2 !
12.0 V, R1 ! 200 0, and  R2 ! 100 0.
What are the (a) size and (b) direction
(up  or  down)  of  the  current  through
resistance 1, the (c) size and (d) direc-
tion  of  the  current  through  resistance
2, and the (e) size and (f) direction of
the current through battery 2?

R2

1

R1

–
+

+
–

2

Figure 27-83 Problem 103.

104 A three-way 120 V lamp bulb that contains two filaments is
rated  for  100-200-300 W. One  filament  burns  out. Afterward, the
bulb operates at the same intensity (dissipates energy at the same
rate) on its lowest as on its highest switch positions but does not
operate  at  all  on  the  middle  position. (a)  How  are  the  two  fila-
ments wired to the three switch positions? What are the (b) smaller
and (c) larger values of the filament resistances?

105 In Fig. 27-84, R1 ! R2 ! 2.0 0, R3 ! 4.0 0, R4 ! 3.0 0, R5 !
1.0 0, and R6 ! R7 ! R8 ! 8.0 0, and the ideal batteries have emfs
#1 ! 16 V and #2 ! 8.0 V. What are the (a) size and (b) direction
(up  or  down)  of  current  i1 and  the  (c)  size  and  (d)  direction  of
current i2? What  is  the  energy  transfer  rate  in  (e)  battery  1  and
(f) battery 2? Is energy being supplied or absorbed in (g) battery 1
and (h) battery 2?

R2

R 3

R 4

R1

R 6

1

i2

R8

R7

i1

+
–

R 5

2
–  +

100 In Fig. 27-81, the ideal batteries
have emfs #1 ! 20.0 V, #2 ! 10.0 V,

Figure 27-81 Problem 100.

Figure 27-84 Problem 105.
