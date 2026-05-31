Sample Problem 27.05 Discharging an RC circuit to avoid a fire in a race car pit stop
As a car rolls along pavement, electrons move from the
pavement first onto the tires and then onto the car body.The
car stores this excess charge and the associated electric poten-
tial energy as if the car body were one plate of a capacitor and
the pavement were the other plate (Fig. 27-17a).When the car
stops, it discharges its excess charge and energy through the
tires, just as a capacitor can discharge through a resistor. If a
conducting object comes within a few centimeters of the car
before the car is discharged, the remaining energy can be
suddenly transferred to a spark between the car and the
object. Suppose the conducting object is a fuel dispenser.The
spark will not ignite the fuel and cause a fire if the spark
energy is less than the critical value Ufire ! 50 mJ.
When the car of Fig. 27-17a stops at time t ! 0, the car-
ground potential difference is V0 ! 30 kV. The car-ground
capacitance is C ! 500 pF, and the resistance of each tire is
Rtire ! 100 G0.How much time does the car take to discharge
through the tires to drop below the critical value Ufire?
KEY IDEAS
(1) At any time t,a capacitor’s stored electric potential energy U
is related to its stored charge q according to Eq. 25-21 (U !
q2/2C). (2) While a capacitor is discharging, the charge de-
creases with time according to Eq.27-39 (q ! q0e#t/RC).
Calculations: We can treat the tires as resistors that are
connected to one another at their tops via the car body and
at their bottoms via the pavement. Figure 27-17b shows how
the four resistors are connected in parallel across the car’s
capacitance, and Fig. 27-17c shows their equivalent resist-
ance R. From Eq. 27-24, R is given by
or
(27-44)
When the car stops, it discharges its excess charge and
energy through R.We now use our two Key Ideas to analyze
the discharge. Substituting Eq. 27-39 into Eq. 25-21 gives
(27-45)
From Eq. 25-1 (q ! CV), we can relate the initial charge q0
on the car to the given initial potential difference V0: q0 !
CV0. Substituting this equation into Eq. 27-45 brings us to
U ! (CV0)2
2C
e#2t/RC ! CV 0
2
2
e#2t/RC,
! q0
2
2C e#2t/RC.
U ! q2
2C ! (q0e#t/RC)2
2C
R ! Rtire
4
! 100 $ 10 9 0
4
! 25 $ 10 9 0.
1
R !
1
Rtire
%
1
Rtire
%
1
Rtire
%
1
Rtire
,
Additional examples, video, and practice available at WileyPLUS
or
(27-46)
Taking the natural logarithms of both sides, we obtain
or
(27-47)
Substituting the given data, we find that the time the car
takes to discharge to the energy level Ufire ! 50 mJ is
(Answer)
Fire or no fire: This car requires at least 9.4 s before fuel can be
brought safely near it.A pit crew cannot wait that long. So the
tires include some type of conducting material (such as carbon
black) to lower the tire resistance and thus increase the dis-
charge rate. Figure 27-17d shows the stored energy U versus
time t for tire resistances of R ! 100 G0 (our value) and R !
10 G0. Note how much more rapidly a car discharges to level
Ufire with the lower R value.
! 9.4 s.
$ ln#
2(50 $ 10 #3 J)
(500 $ 10 #12 F)(30 $ 10 3 V)2 $
t ! # (25 $ 10 9 0)(500 $ 10 #12 F)
2
t ! # RC
2  ln#
2U
CV0
2$.
# 2t
RC ! ln#
2U
CV0
2$,
e#2t/RC !
2U
CV 0
2 .
Tire
resistance
Effective
capacitance
DRIVE    THRU
DRIVE    THRU
3N
Bomman
Schtuff
MDOG
WNFR
True Vales 
RPM
XP3I
6
ULTRA
MOTEL
PST4
Rtire
Rtire
Rtire
Rtire
C
R
C
(a)
(b)
(c)
(d)
U
Ufire
0.94
t (s)
9.4
10 GΩ
100 GΩ
Figure 27-17 (a) A charged car and the
pavement acts like a capacitor that can
discharge through the tires. (b) The
effective circuit of the car-pavement
capacitor, with four tire resistances Rtire
connected in parallel. (c) The equivalent
resistance R of the tires. (d) The electric
potential energy U in the car-pavement
capacitor decreases during discharge.

793
QUESTIONS
Emf
An emf device does work on charges to maintain a potential
difference between its output terminals. If dW is the work the device
does to force positive charge dq from the negative to the positive ter-
minal,then the emf (work per unit charge) of the device is
(definition of #).
(27-1)
The volt is the SI unit of emf as well as of potential difference.An ideal
emf device is one that lacks any internal resistance.The potential dif-
ference between its terminals is equal to the emf. A real emf device
has internal resistance.The potential difference between its terminals
is equal to the emf only if there is no current through the device.
Analyzing Circuits
The change in potential in traversing a
resistance R in the direction of the current is #iR; in the opposite
direction it is %iR (resistance rule). The change in potential in tra-
versing an ideal emf device in the direction of the emf arrow is %#;
in the opposite direction it is ## (emf rule). Conservation of
energy leads to the loop rule:
Loop Rule.
The algebraic sum of the changes in potential encountered
in a complete traversal of any loop of a circuit must be zero.
Conservation of charge gives us the junction rule:
Junction Rule.
The sum of the currents entering any junction
must be equal to the sum of the currents leaving that junction.
Single-Loop Circuits
The current in a single-loop circuit con-
taining a single resistance R and an emf device with emf # and in-
ternal resistance r is
(27-4)
which reduces to i ! #/R for an ideal emf device with r ! 0.
Power
When a real battery of emf # and internal resistance r
does work on the charge carriers in a current i through the battery,
the rate P of energy transfer to the charge carriers is
P ! iV,
(27-14)
i !
#
R % r ,
# ! dW
dq
Review & Summary
where V is the potential across the terminals of the battery.The rate
Pr at which energy is dissipated as thermal energy in the battery is
Pr ! i2r.
(27-16)
The rate Pemf at which the chemical energy in the battery changes is
Pemf ! i#.
(27-17)
Series Resistances
When resistances are in series, they have
the same current. The equivalent resistance that can replace a se-
ries combination of resistances is
(n resistances in series).
(27-7)
Parallel Resistances
When resistances are in parallel,
they have the same potential difference. The equivalent resistance
that can replace a parallel combination of resistances is given by
(n resistances in parallel).
(27-24)
RC Circuits
When an emf # is applied to a resistance R and ca-
pacitance C in series, as in Fig. 27-15 with the switch at a, the charge
on the capacitor increases according to
q ! C#(1 # e#t/RC)
(charging a capacitor),
(27-33)
in which C# ! q0 is the equilibrium (final) charge and RC ! t is the ca-
pacitive time constant of the circuit. During the charging, the current is
(charging a capacitor).
(27-34)
When a capacitor discharges through a resistance R, the charge on
the capacitor decays according to
q ! q0e#t/RC
(discharging a capacitor).
(27-39)
During the discharging, the current is
(discharging a capacitor).
(27-40)
i ! dq
dt ! ##
q0
RC$e#t/RC
i ! dq
dt !#
#
R $e#t/RC
1
Req
! '
n
j!1
1
Rj
Req ! '
n
j!1
Rj
1
(a) In Fig. 27-18a, with R1
R2, is the potential difference
(
Questions
Figure 27-18 Questions 1 and 2.
(a)
+
-
R1
R2
R3
(b)
+
-
R3
R1
R2
(d)
(c)
R2
R1
+
-
R3
R3
+
-
R1
R2
across R2 more than, less than, or equal to that across R1? (b) Is the
current through resistor R2 more than, less than, or equal to that
through resistor R1?
2
(a) In Fig. 27-18a, are resistors R1 and R3 in series? (b) Are 
resistors R1 and R2 in parallel? (c) Rank the equivalent resistances
of the four circuits shown in Fig. 27-18, greatest first.
3
You are to connect resistors R1 and R2, with R1 ( R2, to a bat-
tery, first individually, then in series, and then in parallel. Rank
those arrangements according to the amount of current through the
battery, greatest first.
4
In Fig. 27-19, a circuit consists of
a battery and two uniform resistors,
and the section lying along an x axis
is divided into five segments of equal
lengths. (a) Assume that R1 ! R2 and
rank the segments according to the
magnitude of the average electric
Figure 27-19 Question 4.
+ 
- 
R1
R2
a 
b 
c 
d 
e 
x

794
CHAPTER 27
CIRCUITS
field in them, greatest first. (b) Now assume that R1 ( R2 and then
again rank the segments. (c) What is the direction of the electric
field along the x axis?
5
For each circuit in Fig. 27-20, are the resistors connected in se-
ries, in parallel, or neither?
Figure 27-21 Question 6.
R
Figure 27-20 Question 5.
Figure 27-22 Question 10.
+
-
+
-
+
-
(a) 
(b) 
(c)
6
Res-monster maze. In Fig. 27-21, all the resistors have a resis-
tance of 4.0 0 and all the (ideal) batteries have an emf of 4.0 V.
What is the current through resistor R? (If you can find the proper
loop through this maze, you can answer the question with a few
seconds of mental calculation.)
7
A resistor R1 is wired to a battery, then resistor R2 is added
in series. Are (a) the potential difference across R1 and (b) the
current i1 through R1 now more than, less than, or the same as pre-
viously? (c) Is the equivalent resistance R12 of R1 and R2 more
than, less than, or equal to R1?
8
What is the equivalent resistance of three resistors, each of
resistance R, if they are connected to an ideal battery (a) in se-
ries with one another and (b) in parallel with one another? (c)
Is the potential difference across the series arrangement
greater than, less than, or equal to that across the parallel
arrangement?
9
Two resistors are wired to a battery. (a) In which arrangement,
parallel or series, are the potential differences across each resistor
and across the equivalent resistance all equal? (b) In which
arrangement are the currents through each resistor and through
the equivalent resistance all equal?
10
Cap-monster maze. In Fig. 27-22, all the capacitors have a
capacitance of 6.0 mF, and all the batteries have an emf of 10 V.
What is the charge on capacitor C? (If you can find the proper loop
through this maze, you can answer the question with a few seconds
of mental calculation.)
11
Initially, a single resistor R1 is wired to a battery.Then resistor
R2 is added in parallel. Are (a) the potential difference across R1
and (b) the current i1 through R1 now more than, less than, or the
same as previously? (c) Is the equivalent resistance R12 of R1 and
R2 more than, less than, or equal to R1? (d) Is the total current
through R1 and R2 together more than, less than, or equal to the
current through R1 previously?
12
After the switch in Fig. 27-15 is closed on point a, there is cur-
rent i through resistance R. Figure 27-23 gives that current for four
sets of values of R and capacitance C: (1) R0 and C0, (2) 2R0 and C0,
(3) R0 and 2C0, (4) 2R0 and 2C0. Which set goes with which curve?
(1)
(2) 
(3)
C
i
d
c
a
b
t
Figure 27-24 Question 13.
Figure 27-23 Question 12.
13
Figure 27-24 shows three sections of circuit that are to be con-
nected in turn to the same battery via a switch as in Fig. 27-15.The
resistors are all identical, as are the capacitors. Rank the sections
according to (a) the final (equilibrium) charge on the capacitor and
(b) the time required for the capacitor to reach 50% of its final
charge, greatest first.

795
PROBLEMS
•5
A 5.0 A current is set up in a circuit for 6.0 min by a recharge-
able battery with a 6.0 V emf. By how much is the chemical energy
of the battery reduced?
VA
0
0
x
x
4
1 
2 
3 
∆VB
∆VC
V
V (V)
Figure 27-27
Problem 4.
Tutoring problem available (at instructor’s discretion) in WileyPLUS and WebAssign
SSM
Worked-out solution available in Student Solutions Manual      
• - •••
Number of dots indicates level of problem difficulty
Additional information available in The Flying Circus of Physics and at flyingcircusofphysics.com
WWW Worked-out solution is at
ILW
Interactive solution is at 
http://www.wiley.com/college/halliday
Problems
Module 27-1
Single-Loop Circuits
•1
In Fig. 27-25, the ideal
batteries have emfs 
V and
V. What are (a) the current,
the dissipation rate in (b) resistor 1 (4.0
) and (c) resistor 2 (8.0 0), and the en-
ergy transfer rate in (d) battery 1 and
(e) battery 2? Is energy being supplied
or absorbed by (f) battery 1 and (g) bat-
tery 2?
•2
In Fig. 27-26, the ideal batteries 
have emfs #1 ! 150 V and #2 ! 50 V
and the resistances are R1 ! 3.0 0 and
R2 ! 2.0 0. If the potential at P is 100 V,
what is it at Q?
•3
A car battery with a 12 V emf
and an internal resistance of 0.040 
is
being charged with a current of 50 A.
What are (a) the potential difference V across the terminals, (b)
the rate Pr of energy dissipation inside the battery, and (c) the rate
Pemf of energy conversion to chemical form? When the battery is
used to supply 50 A to the starter motor, what are (d) V and (e) Pr?
•4
Figure 27-27 shows a circuit of four resistors that are con-
nected to a larger circuit. The graph below the circuit shows the
electric potential V(x) as a function of position x along the lower
branch of the circuit, through resistor 4; the potential VA is 12.0 V.
The graph above the circuit shows the electric potential V(x)
versus position x along the upper branch of the circuit, through
resistors 1, 2, and 3; the potential differences are 'VB ! 2.00 V and
'VC ! 5.00 V. Resistor 3 has a resistance of 200 0. What is the
resistance of (a) resistor 1 and (b) resistor 2?
0
ILW
0
#2 ! 6.0
#1 ! 12
WWW
SSM
-
+
- +
1
2
R1
R2
Figure 27-25
Problem 1.
-
+
-
+
Q
P
R1
R2
1
2
Figure 27-26 Problem 2.
•6
A standard flashlight battery can deliver about 2.0 W&h of
energy before it runs down. (a) If a battery costs US$0.80, what is
the cost of operating a 100 W lamp for 8.0 h using batteries?
(b) What is the cost if energy is provided at the rate of US$0.06 per
kilowatt-hour?
•7
A wire of resistance 5.0 0 is connected to a battery whose emf
# is 2.0 V and whose internal resistance is 1.0 0. In 2.0 min, how
much energy is (a) transferred from chemical form in the battery,
(b) dissipated as thermal energy in the wire, and (c) dissipated as
thermal energy in the battery?
•8
A certain car battery with a 12.0 V emf has an initial charge of
120 A&h. Assuming that the potential across the terminals stays
constant until the battery is completely discharged, for how many
hours can it deliver energy at the rate of 100 W?
•9
(a) In electron-volts, how much work does an ideal battery
with a 12.0 V emf do on an electron that passes through the battery
from the positive to the negative terminal? (b) If 3.40 $ 10 18 elec-
trons pass through each second, what is the power of the battery in
watts?
••10
(a) In Fig. 27-28, what value
must R have if the current in the
circuit is to be 1.0 mA? Take #1 ! 2.0
V, #2 ! 3.0 V, and r1 ! r2 ! 3.0 0. (b)
What is the rate at which thermal en-
ergy appears in R?
••11
In Fig. 27-29, circuit sec-
tion AB absorbs energy at a rate of
50 W 
when 
current 
i ! 1.0 A
through it is in the indicated
direction. Resistance R ! 2.0 0. (a)
What is the potential difference be-
tween A and B? Emf device X lacks
internal resistance. (b) What is its
emf? (c) Is point B connected to the positive terminal of X or to
the negative terminal?
••12
Figure 27-30 shows a resistor of resis-
tance R ! 6.00 0 connected to an ideal battery
of emf # ! 12.0 V by means of two copper
wires. Each wire has length 20.0 cm and radius
1.00 mm. In dealing with such circuits in this
chapter, we generally neglect the potential
differences along the wires and the transfer of
energy to thermal energy in them. Check
the validity of this neglect for the circuit of
Fig. 27-30: What is the potential difference
across (a) the resistor and (b) each of the two sections of wire?
At what rate is energy lost to thermal energy in (c) the resistor
and (d) each section of wire?
••13
A 10-km-long underground cable extends east to west and
consists of two parallel wires, each of which has resistance 13 /km.
An electrical short develops at distance x from the west end when
0
SSM
-
+
r1
1
-
+
r2
2
R
Figure 27-28 Problem 10.
X
i
A 
B 
R
Figure 27-29 Problem 11.
Wire 1 
Wire 2 
R
Figure 27-30
Problem 12.

•21
Four 18.0 0 resistors are con-
nected in parallel across a 25.0 V
ideal battery. What is the current
through the battery?
•22
Figure 27-34 shows five 5.00 0
resistors. Find the equivalent resis-
tance between points (a) F and H and
(b) F and G. (Hint: For each pair of
points, imagine that a battery is con-
nected across the pair.)
•23
In Fig. 27-35, R1 ! 100 0, R2 !
50 0, and the ideal batteries have
emfs
#1 ! 6.0 V,
#2 ! 5.0 V,
and 
#3 ! 4.0 V. Find (a) the current in re-
sistor 1, (b) the current in resistor 2,
and (c) the potential difference be-
tween points a and b.
•24
In Fig. 27-36, R1 ! R2 ! 4.00 0
and R3 ! 2.50 0. Find the equivalent
resistance between points D and E.
(Hint: Imagine that a battery is con-
nected across those points.)
•25
Nine copper wires of length
l and diameter d are connected in par-
allel to form a single composite con-
ductor of resistance R. What must be
the diameter D of a single copper wire
of length l if it is to have the same re-
sistance?
••26
Figure 27-37 shows a battery
connected across a uniform resistor
R0. A sliding contact can move across
the resistor from x ! 0 at the left to 
x ! 10 cm at the right. Moving
the contact changes how much resist-
ance is to the left of the contact and
how much is to the right. Find the
rate at which energy is dissipated in
resistor R as a function of x. Plot the
function for # ! 50 V, R ! 2000 0,
and R0 ! 100 0.
••27
Side flash. Figure 27-38
indicates one reason no one should
stand under a tree during a lightning
storm. If lightning comes down the
side of the tree, a portion can jump
over to the person, especially if the
current on the tree reaches a dry re-
gion on the bark and thereafter must
travel through air to reach the
ground. In the figure, part of the lightning jumps through distance
d in air and then travels through the person (who has negligible
resistance relative to that of air because of the highly conducting
salty fluids within the body).The rest of the current travels through
air alongside the tree, for a distance h. If d/h ! 0.400 and the total
current is I ! 5000 A, what is the current through the person?
••28
The ideal battery in Fig. 27-39a has emf # ! 6.0 V. Plot 1 in
Fig. 27-39b gives the electric potential difference V that can appear
across resistor 1 versus the current i in that resistor when the resistor
SSM
a conducting path of resistance R
connects the wires (Fig. 27-31). The
resistance of the wires and the short
is then 100 0 when measured from
the east end and 200 0 when meas-
ured from the west end. What are
(a) x and (b) R?
••14
In Fig. 27-32a, both batteries have emf # ! 1.20 V and the
external resistance R is a variable resistor. Figure 27-32b gives the
electric potentials V between the terminals of each battery as func-
tions of R: Curve 1 corresponds to battery 1, and curve 2 corre-
sponds to battery 2.The horizontal scale is set by Rs ! 0.20 0.What
is the internal resistance of (a) battery 1 and (b) battery 2?
796
CHAPTER 27
CIRCUITS
R
1
2
1
2
Rs
R (Ω)
0.5
0
-0.3
V (V) 
(a)
(b)
-
+
-
+
Figure 27-32 Problem 14.
West 
East
Conducting 
path 
x
Figure 27-31 Problem 13.
x
+
-
R
R0
Sliding
contact
Figure 27-37 Problem 26.
G
H
F
R 
R 
R
R 
R 
Figure 27-34 Problem 22.
R2
+ -
1
R1
+ -
+ -
3
2
a
b
Figure 27-35 Problem 23.
R2
R3
D
E
R1
Figure 27-36 Problem 24.
h
d
I
Lightning
current
Figure 27-38 Problem 27.
••15
The current in a single-loop circuit with one resistance R
is 5.0 A.When an additional resistance of 2.0 
is inserted in series
with R, the current drops to 4.0 A.What is R?
•••16
A solar cell generates a potential difference of 0.10 V when
a 500 0 resistor is connected across it, and a potential difference of
0.15 V when a 1000 0 resistor is substituted.What are the (a) inter-
nal resistance and (b) emf of the solar cell? (c) The area of the cell is
5.0 cm2, and the rate per unit area at which it receives energy from
light is 2.0 mW/cm2.What is the efficiency of the cell for converting
light energy to thermal energy in the 1000 0 external resistor?
•••17
In Fig. 27-33, battery 1 has emf
V and internal resistance r1
0.016
and battery 2 has emf 
V
and internal resistance r2
0.012 
. The
batteries are connected in series with an ex-
ternal resistance R. (a) What R value makes
the terminal-to-terminal potential differ-
ence of one of the batteries zero? (b) Which
battery is that?
Module 27-2
Multiloop Circuits
•18
In Fig. 27-9, what is the potential difference Vd # Vc between
points d and c if #1 ! 4.0 V, #2 ! 1.0 V, R1 ! R2 ! 10 0, and R3 !
5.0 0, and the battery is ideal?
•19
A total resistance of 3.00 0 is to be produced by connecting
an unknown resistance to a 12.0 0 resistance. (a) What must be the
value of the unknown resistance, and (b) should it be connected in
series or in parallel?
•20
When resistors 1 and 2 are connected in series, the equivalent
resistance is 16.0 0. When they are connected in parallel, the
equivalent resistance is 3.0 0. What are (a) the smaller resistance
and (b) the larger resistance of these two resistors?
0
!
#2 ! 12.0
0
!
#1 ! 12.0
SSM
0
ILW
R
r1
r2
-
+
-
+
1
2
Figure 27-33
Problem 17.

797
PROBLEMS
battery is opposite the direction of that battery’s emf.What are (a)
emf #1, (b) resistance R1, and (c) resistance R2?
••33
In Fig. 27-44, the current in resistance 6 is i6 ! 1.40 A
and the resistances are R1
R2
R3
2.00 , R4
16.0 , R5
8.00 , and R6 ! 4.00 0.What is the emf of the ideal battery?
0
!
0
!
0
!
!
!
is individually tested by putting a variable potential across it. The
scale of the V axis is set by Vs ! 18.0 V, and the scale of the i axis is
set by is ! 3.00 m1. Plots 2 and 3 are similar plots for resistors 2
and 3, respectively, when they are individually tested by putting a
variable potential across them. What is the current in resistor 2 in
the circuit of Fig. 27-39a?
••34
The resistances in Figs.27-45a and b are all 6.0 0,and the batter-
ies are ideal 12 V batteries. (a) When switch S in Fig. 27-45a is closed,
what is the change in the electric potential V1 across resistor 1, or does
V1 remain the same? (b) When switch S in Fig.27-45b is closed,what is
the change in V1 across resistor 1,or does V1 remain the same?
••35
In Fig. 27-46, # ! 12.0 V,
R1
2000 
,
R2
3000 
,
and 
R3
4000 
. What are the potential
differences (a) VA
VB, (b) VB # VC,
(c) VC # VD, and (d) VA # VC?
••36
In Fig. 27-47,
V,
V, R1
100 ,
and R3
300 . One point of the cir-
cuit is grounded (V ! 0). What are
the (a) size and (b) direction (up or
down) of the current through resist-
ance 1, the (c) size and (d) direction
(left or right) of the current through
resistance 2, and the (e) size and
(f) direction of the current through
resistance 3? (g) What is the electric
potential at point A?
••37
In Fig. 27-48, the resistances
are R1 ! 2.00 0, R2 ! 5.00 0, and the
battery is ideal. What value of R3
maximizes the dissipation rate in
resistance 3?
••38
Figure 27-49 shows a section of
a circuit. The resistances are R1 ! 2.0
0, R2 ! 4.0 0, and R3 ! 6.0 0, and the
indicated 
current 
is 
i ! 6.0 A.
The electric potential difference be-
tween points A and B that connect
the section to the rest of the circuit is
VA # VB ! 78 V. (a) Is the device rep-
resented by “Box” absorbing or pro-
viding energy to the circuit, and (b) at
what rate?
0
!
R2 ! 200 0,
0
!
#2 ! 12.0
#1 ! 6.00
#
0
!
0
!
0
!
V (V) 
Vs
0
1
i (mA) 
2
is
3
(b)
R2
R1
R3
(a)
+
-
Figure 27-39 Problem 28.
2 (V)
Current (A)
is
0
-is
5
10
(b)
2
1
R2
R1
(a)
+
-
+
-
Figure 27-43 Problem 32.
i1
R1
R2
R2
R2
+ - 
Figure 27-40 Problem 29.
Figure 27-42 Problem 31.
+
-
2
R3
+
-
1
R2
R1
Figure 27-41 Problems 30, 41,
and 88.
V2
V1
1
+
-
2
+
-
••29
In Fig. 27-40, R1 ! 6.00 0,
R2 ! 18.0 0, and the ideal battery
has emf # ! 12.0 V. What are the
(a) size and (b) direction (left or
right) of current i1? (c) How much
energy is dissipated by all four resis-
tors in 1.00 min?
••30
In Fig. 27-41, the ideal
batteries have emfs 
V and
2
0.500
1, and the resistances are
each 4.00 
. What is the current in
(a) resistance 2 and (b) resistance 3?
••31
In Fig. 27-42, the
ideal batteries have emfs 
1
5.0 V
and 
V, the resistances are
each 2.0 
, and the potential is de-
fined to be zero at the grounded
point of the circuit. What are poten-
tials (a) V1 and (b) V2 at the indi-
cated points?
••32
Both batteries in Fig. 27-43a
are ideal. Emf #1 of battery 1 has a
fixed value, but emf #2 of battery 2
can be varied between 1.0 V and 10
V. The plots in Fig. 27-43b give the
currents through the two batteries as
a function of #2. The vertical scale is
set by is ! 0.20 A. You must decide
0
#2 ! 12
!
#
SSM
0
#
!
#
#1 ! 10.0
which plot corresponds to which battery, but for both plots, a nega-
tive current occurs when the direction of the current through the
(a)
(b)
R2
R1
S
R2
R1
R3
S
+
-
+
-
R2
R1
R5
R4
R6
R3
i6
+
-
Figure 27-44 Problem 33.
Figure 27-45 Problem 34.
R1
R1
R3
R2
R2
A
B
D
C
+
-
1
2
R1
R2
R3
A
+
-
+
-
Figure 27-46 Problem 35.
Figure 27-47 Problem 36.
+
-
R3
R2
R1
Figure 27-48 Problems 37
and 98.
Box
A 
B 
i
R1
R2
R3
Figure 27-49 Problem 38.

•••47
A copper wire of radius a ! 0.250 mm has an alu-
SSM
798
CHAPTER 27
CIRCUITS
through the battery as a function of R3. The horizontal scale is
set by R3s ! 20 0.The curve has an asymptote of 2.0 mA as R3 :
,.What are (a) resistance R1 and (b) resistance R2?
••39
In Fig. 27-50, two batteries with an
emf 
V and an internal resistance 
r ! 0.300 0 are connected in parallel across
a resistance R. (a) For what value of R is the
dissipation rate in the resistor a maximum?
(b) What is that maximum?
••40
Two identical batteries of emf # !
12.0 V and internal resistance r
0.200 
are
to be connected to an external resistance R,
either in parallel (Fig. 27-50) or in series
(Fig. 27-51). If R ! 2.00r, what is the current i
in the external resistance in the (a) parallel
and (b) series arrangements? (c) For which
arrangement is i greater? If R !
r/2.00, what is i in the external resist-
ance in the (d) parallel arrangement
and (e) series arrangement? (f) For
which arrangement is i greater now?
••41
In Fig. 27-41, #1 ! 3.00 V, #2 !
1.00 V, R1 ! 4.00 0, R2 ! 2.00 0, R3 !
5.00 0, and both batteries are ideal.
What is the rate at which energy is dis-
sipated in (a) R1, (b) R2, and (c) R3? What is the power of (d) battery
1 and (e) battery 2?
••42
In Fig. 27-52, an array of n par-
allel resistors is connected in series to
a resistor and an ideal battery. All the
resistors have the same resistance. If
an identical resistor were added in
parallel to the parallel array, the cur-
rent through the battery would
change by 1.25%. What is the value
of n?
••43
You are given a number of 10 0 resistors, each capable of
dissipating only 1.0 W without being destroyed. What is the mini-
mum number of such resistors that you need to combine in series
or in parallel to make a 10 0 resist-
ance that is capable of dissipating at
least 5.0 W?
••44
In Fig. 27-53, R1
100 
,
R2
R3
50.0 
, R4
75.0 
, and
the ideal battery has emf # ! 6.00 V.
(a) What is the equivalent resistance?
What is i in (b) resistance 1, (c) resist-
ance 2, (d) resistance 3, and (e) resist-
ance 4?
••45
In Fig. 27-54, the resistances
are
R1
1.0 
and R2
2.0 
,
and the ideal batteries have emfs 
#1 ! 2.0 V and #2 ! #3 ! 4.0 V. What
are the (a) size and (b) direction (up
or down) of the current in battery 1,
the (c) size and (d) direction of the
current in battery 2, and the (e) size
and (f) direction of the current in battery 3? (g) What is the poten-
tial difference Va # Vb?
••46
In Fig. 27-55a, resistor 3 is a variable resistor and the ideal
battery has emf # ! 12 V. Figure 27-55b gives the current i
0
!
0
!
ILW
0
!
0
!
!
0
!
0
!
# ! 12.0
+ - 
+ - 
r
r
R
Figure 27-50
Problems 39 
and 40.
+ - 
+ - 
r
r
R
R
R
R
n resistors 
in parallel
R3
R2
R1
i (mA)
6
4
2
0
R3 (Ω)
R3s
(a)
(b)
+
-
+
-
3
R1
+
-
2
R2
+
-
1
R1
R1
R1
a
b
R2
+
-
R1
R3
R4
Figure 27-53
Problems 44 and 48.
Figure 27-51 Problem 40.
Figure 27-52 Problem 42.
Figure 27-54 Problem 45.
Figure 27-55 Problem 46.
minum jacket of outer radius b
0.380 mm. There is a current i !
2.00 A in the composite wire. Using Table 26-1, calculate the cur-
rent in (a) the copper and (b) the aluminum. (c) If a potential dif-
ference V ! 12.0 V between the ends maintains the current, what
is the length of the composite wire?
•••48
In Fig. 27-53, the resistors have the values R1 ! 7.00 0,
!
R2
12.0 
, and R3
4.00 
, and the ideal battery’s emf is 
# ! 24.0 V. For what value of R4 will the rate at which the battery
transfers energy to the resistors equal (a) 60.0 W, (b) the maximum
possible rate Pmax, and (c) the minimum possible rate Pmin? What
are (d) Pmax and (e) Pmin?
Module 27-3
The Ammeter and
the Voltmeter
••49
(a) In Fig. 27-56, what cur-
rent does the ammeter read if 
5.0 V (ideal battery), R1 ! 2.0 0, R2 !
4.0 0, and R3 ! 6.0 0? (b) The am-
meter and battery are now inter-
changed. Show that the ammeter
reading is unchanged.
••50
In Fig. 27-57, R1
2.00R, the
ammeter resistance is zero, and the
battery is ideal. What multiple of #/R
gives the current in the ammeter?
••51
In Fig. 27-58, a voltmeter of
resistance RV ! 300 0 and an am-
meter of resistance RA ! 3.00 0 are
being used to measure a resistance
R in a circuit that also contains a re-
sistance R0 ! 100 0 and an ideal
battery with an emf of # ! 12.0 V.
Resistance R is given by R ! V/i,
where V is the potential across R
and i is the ammeter reading. The
voltmeter reading is V-, which is
V
plus the potential difference
across the ammeter. Thus, the ratio
of the two meter readings is not R but only an apparent resist-
ance R- ! V-/i. If R ! 85.0 0, what are (a) the ammeter reading,
(b) the voltmeter reading, and (c) R-? (d) If RA is decreased,
does the difference between R- and R increase, decrease, or
remain the same?
••52
A simple ohmmeter is made by connecting a 1.50 V flash-
light battery in series with a resistance R and an ammeter that
!
# !
ILW
0
!
0
!
+
-
R3
A
R2
R1
Figure 27-56 Problem 49.
+
-
R
A
R
R
R1
Figure 27-57 Problem 50.
+ - 
R
R0
V
A
Figure 27-58 Problem 51.

799
PROBLEMS
Module 27-4
RC Circuits
•57
Switch S in Fig. 27-63 is closed at
time t ! 0, to begin charging an initially
uncharged capacitor of capacitance C !
15.0 mF through a resistor of resistance 
R ! 20.0 0. At what time is the potential
across the capacitor equal to that across
the resistor?
•58
In an RC series circuit, emf # ! 12.0 V, resistance R !
1.40 M0, and capacitance C ! 1.80 mF. (a) Calculate the time con-
stant. (b) Find the maximum charge that will appear on the capaci-
tor during charging. (c) How long does it take for the charge to
build up to 16.0 mC?
•59
What multiple of the time constant t gives the time
taken by an initially uncharged capacitor in an RC series circuit to
be charged to 99.0% of its final charge?
•60
A capacitor with initial charge q0 is discharged through a
resistor. What multiple of the time constant t gives the time the
capacitor takes to lose (a) the first one-third of its charge and
(b) two-thirds of its charge?
•61
A 15.0 k0 resistor and a capacitor are connected in se-
ries, and then a 12.0 V potential difference is suddenly applied
across them. The potential difference across the capacitor rises to
5.00 V in 1.30 ms. (a) Calculate the time constant of the circuit.
(b) Find the capacitance of the capacitor.
••62
Figure 27-64 shows the circuit of
a flashing lamp, like those attached to
barrels at highway construction sites.
The fluorescent lamp L (of negligible
capacitance) is connected in parallel
across the capacitor C of an RC circuit.
There is a current through the lamp
only when the potential difference
across it reaches the breakdown volt-
age VL; then the capacitor discharges completely through the lamp
and the lamp flashes briefly. For a lamp with breakdown voltage 
VL ! 72.0 V, wired to a 95.0 V ideal battery and a 0.150 mF capacitor,
what resistance R is needed for two flashes per second?
••63
In the circuit of Fig.
WWW
SSM
ILW
SSM
reads from 0 to 1.00 mA, as shown in
Fig. 27-59. Resistance R is adjusted
so that when the clip leads are
shorted together, the meter deflects
to its full-scale value of 1.00 mA.
What external resistance across the
leads results in a deflection of (a)
10.0%, (b) 50.0%, and (c) 90.0% of full scale? (d) If the ammeter
has a resistance of 20.0 0 and the internal resistance of the battery
is negligible, what is the value of R?
••53
In Fig. 27-14, assume that # ! 3.0 V, r ! 100 0, R1 ! 250 0,
and R2 ! 300 0. If the voltmeter resistance RV is 5.0 k0, what per-
cent error does it introduce into the measurement of the potential
difference across R1? Ignore the presence of the ammeter.
••54
When the lights of a car are
switched on, an ammeter in series with
them reads 10.0 A and a voltmeter
connected across them reads 12.0 V (Fig.
27-60). When the electric starting motor is
turned on, the ammeter reading drops to
8.00 A and the lights dim somewhat. If the
internal resistance of the battery is 0.0500
0 and that of the ammeter is negligible,
what are (a) the emf of the battery and (b)
the current through the starting motor
when the lights are on?
••55
In Fig. 27-61, Rs is to be adjusted in
value by moving the sliding contact across
it until points a and b are brought to the
same potential. (One tests for this condition by momentarily con-
necting a sensitive ammeter be-
tween a and b; if these points are at
the same potential, the ammeter
will not deflect.) Show that when
this adjustment is made, the follow-
ing relation holds: Rx ! RsR2/R1.
An unknown resistance (Rx) can be
measured in terms of a standard
(Rs) using this device, which is
called a Wheatstone bridge.
••56
In Fig. 27-62, a voltmeter of
resistance RV ! 300 0 and an am-
meter of resistance RA ! 3.00 0
are being used to measure a resist-
ance R in a circuit that also con-
tains a resistance R0 ! 100 0 and
an ideal battery of emf # ! 12.0 V.
Resistance R is given by R ! V/i,
where V is the voltmeter reading
and i is the current in resistance R.
However, the ammeter reading is
not i but rather i-, which is i plus the
current through the voltmeter.
Thus, the ratio of the two meter
readings is not R but only an appar-
Figure 27-59 Problem 52.
+
-
0-1.00
mA
R
V
+
-
S
S
Starting
motor
Lights
A
r
Figure 27-60
Problem 54.
+ - 
R0
b
a
Rs
Rx
R1
R2
Sliding contact 
Figure 27-61 Problem 55.
+ - 
R
R0
V
A
Figure 27-62 Problem 56.
ent resistance R- ! V/i-. If R ! 85.0 0, what are (a) the ammeter
reading, (b) the voltmeter reading, and (c) R-? (d) If RV is in-
creased, does the difference between R- and R increase, decrease,
or remain the same?
C
R
S
+
-
Figure 27-63 Problems
57 and 96.
+
-
R
C
L
Figure 27-64
Problem 62.
C
+
-
S
R3
R2
R1
Figure 27-65 Problem 63.
27-65,
kV, C
6.5 mF, R1 !
R2 ! R3 ! 0.73 M0. With C completely
uncharged, switch S is suddenly closed
(at t ! 0). At t ! 0, what are (a) current
i1 in resistor 1, (b) current i2 in resistor 2,
and (c) current i3 in resistor 3? At t ! ,
(that is, after many time constants),
!
# ! 1.2
what are (d) i1, (e) i2, and (f) i3? What is the potential difference V2
across resistor 2 at (g) t ! 0 and (h) t ! ,? (i) Sketch V2 versus t be-
tween these two extreme times.
••64
A capacitor with an initial potential difference of 100 V is dis-
charged through a resistor when a switch between them is closed at
t ! 0.At t ! 10.0 s, the potential differ-
ence across the capacitor is 1.00 V. (a)
What is the time constant of the
circuit? (b) What is the potential differ-
ence across the capacitor at t ! 17.0 s?
••65
In Fig. 27-66, R1 ! 10.0 k0,
R2
15.0 k , C
0.400 mF, and the
!
0
!
+
-
R2
R1
C
Figure 27-66
Problems 65 and 99.

800
CHAPTER 27
CIRCUITS
73
Wires A and B, having equal lengths of 40.0 m and equal
diameters of 2.60 mm, are connected in series. A potential
difference of 60.0 V is applied between the ends of the composite
wire.The resistances are RA ! 0.127 0 and RB ! 0.729 0. For wire
A, what are (a) magnitude J of the current density and (b) poten-
tial difference V? (c) Of what type material is wire A made (see
Table 26-1)? For wire B, what are (d) J and (e) V? (f) Of what type
material is B made?
74
What are the (a) size and (b) direction (up or down) of cur-
rent i in Fig. 27-71, where all resistances are 4.0 0 and all batteries
are ideal and have an emf of 10 V? (Hint: This can be answered us-
ing only mental calculation.)
SSM
ideal battery has emf 
V. First, the switch is closed a long
time so that the steady state is reached. Then the switch is opened
at time t ! 0.What is the current in resistor 2 at t ! 4.00 ms?
••66
Figure 27-67 displays two cir-
cuits with a charged capacitor that
is to be discharged through a resis-
tor when a switch is closed. In Fig.
27-67a, R1 ! 20.0 0 and C1 ! 5.00
mF. In Fig. 27-67b, R2 ! 10.0 0 and
C2 ! 8.00 mF.The ratio of the initial
charges on the two capacitors is
q02/q01 ! 1.50. At time t ! 0, both switches are closed. At what
time t do the two capacitors have the same charge?
••67
The potential difference between the plates of a leaky
(meaning that charge leaks from one plate to the other) 2.0 mF
capacitor drops to one-fourth its initial value in 2.0 s. What is the
equivalent resistance between the capacitor plates?
••68
A 1.0 mF capacitor with an initial stored energy of 0.50 J is
discharged through a 1.0 M0 resistor. (a) What is the initial charge
on the capacitor? (b) What is the current through the resistor when
the discharge starts? Find an expression that gives, as a function of
time t, (c) the potential difference VC across the capacitor, (d) the
potential difference VR across the resistor, and (e) the rate at which
thermal energy is produced in the resistor.
•••69
A 3.00 M0 resistor and a 1.00 mF capacitor are
connected in series with an ideal battery of emf 
V.At 1.00 s
after the connection is made, what is the rate at which (a) the
charge of the capacitor is increasing, (b) energy is being stored in
the capacitor, (c) thermal energy is appearing in the resistor, and
(d) energy is being delivered by the battery?
Additional Problems
70
Each of the six real batteries in
Fig. 27-68 has an emf of 20 V and a resistance
of 4.0 
. (a) What is the current through the
(external) resistance R
4.0 
? (b) What is
the potential difference across each battery?
(c) What is the power of each battery? (d) At
what rate does each battery transfer energy
to internal thermal energy?
71
In Fig. 27-69, R1
20.0 
, R2
10.0 
, and the ideal battery has emf
#
120 V. What is the current at
point a if we close (a) only switch S1,
(b) only switches S1 and S2, and (c) all
three switches?
72
In Fig.27-70,the ideal battery has
emf #
30.0 V, and the resistances
are
R1
R2
14 
,
R3
R4
R5
6.0 
, R6
2.0 
, and R7
1.5
.What are currents (a) i2,(b) i4,(c) i1,(d) i3,and (e) i5?
0
!
0
!
0
!
!
!
0
!
!
!
!
0
!
0
!
0
!
0
# ! 4.00
# ! 20.0
C2
R1
R2
C1
(a)
(b)
Figure 27-67 Problem 66.
i
i3
i1
i2
R1
R2
R7
R3
R4
R5
R6
i4
i5
+
-
Figure 27-70
Problem 72.
Figure 27-71 Problem 74.
R
Figure 27-68
Problem 70.
a
S1
S2
S3
R1
R1
R1
R1
R2
R2
-
+
Figure 27-69 Problem 71.
75
Suppose that, while you are sitting in a chair, charge
separation between your clothing and the chair puts you at a
potential of 200 V, with the capacitance between you and the
chair at 150 pF. When you stand up, the increased separation
between your body and the chair decreases the capacitance to
10 pF. (a) What then is the potential of your body? That poten-
tial is reduced over time, as the charge on you drains through
your body and shoes (you are a capacitor discharging through a
resistance). Assume that the resistance along that route is 300
G0. If you touch an electrical component while your potential
is greater than 100 V, you could ruin the component. (b) How
long must you wait until your potential reaches the safe level of
100 V?
If you wear a conducting wrist strap that is connected to
ground, your potential does not increase as much when you stand
up; you also discharge more rapidly because the resistance through
the grounding connection is much less than through your body and
shoes. (c) Suppose that when you stand up, your potential is 1400 V
and the chair-to-you capacitance is 10 pF. What resistance in that
wrist-strap grounding connection will allow you to discharge to 100
V in 0.30 s, which is less time than you would need to reach for, say,
your computer?
76
In Fig. 27-72, the ideal batteries have emfs #1 ! 20.0 V,
V, and 
V, and the resistances are each 2.00
.
What are the (a) size and (b) direction (left or right) of current i1?
(c) Does battery 1 supply or absorb energy, and (d) what is its
power? (e) Does battery 2 supply or absorb energy, and (f) what is
0
#3 ! 5.00
#2 ! 10.0

801
PROBLEMS
unit is a float connected to a variable resistor whose resistance
varies linearly with the volume of gasoline. The resistance is 140 0
when the tank is empty and 20 0 when the tank is full. Find the
current in the circuit when the tank is (a) empty, (b) half-full, and
(c) full.Treat the battery as ideal.
85
The starting motor of a car is turning too slowly, and
the mechanic has to decide whether to replace the motor, the ca-
ble, or the battery. The car’s manual says that the 12 V battery
should have no more than 0.020 0 internal resistance, the motor no
more than 0.200 0 resistance, and the cable no more than 0.040 0
resistance. The mechanic turns on the motor and measures 11.4 V
across the battery, 3.0 V across the cable, and a current of 50 A.
Which part is defective?
86
Two resistors R1 and R2 may be connected either in series or in
parallel across an ideal battery with emf #.We desire the rate of en-
ergy dissipation of the parallel combination to be five times that of
the series combination. If R1 ! 100 0, what are the (a) smaller and
(b) larger of the two values of R2 that result in that dissipation rate?
87
The circuit of Fig. 27-75 shows a
capacitor,
two ideal batteries,
two
resistors, and a switch S. Initially S has
been open for a long time. If it is then
closed for a long time, what is the
change in the charge on the capacitor?
Assume C ! 10 mF, #1 ! 1.0 V, #2 ! 3.0
V, R1 ! 0.20 0, and R2 ! 0.40 0.
88
In Fig. 27-41, R1 ! 10.0 0, R2 !
20.0 0, and the ideal batteries have emfs
#1 ! 20.0 V and #2 ! 50.0 V.
What
value of R3 results in no current through
battery 1?
89
In Fig. 27-76, R ! 10 0. What is the
equivalent resistance between points A
and B? (Hint: This circuit section might
look simpler if you first assume that points
A and B are connected to a battery.)
90
(a) In Fig.27-4a,show that the rate
at which energy is dissipated in R as
thermal energy is a maximum when 
R ! r. (b) Show that this maximum
power is P ! #2/4r.
91
In Fig. 27-77, the ideal batteries
have emfs #1 ! 12.0 V and #2 ! 4.00
V, and the resistances are each 4.00 0.
What are the (a) size and (b) direction
(up or down) of i1 and the (c) size and
(d) direction of i2? (e) Does battery 1
supply or absorb energy, and (f) what
is its energy transfer rate? (g) Does
battery 2 supply or absorb energy, and
(h) what is its energy transfer rate?
92
Figure 27-78 shows a portion of a
circuit through which there is a current
I ! 6.00 A. The resistances are R1 !
R2 ! 2.00R3 ! 2.00R4 ! 4.00 0. What
is the current i1 through resistor 1?
93
Thermal energy is to be gener-
ated in a 0.10 0 resistor at the rate of
SSM
its power? (g) Does battery 3 supply or absorb energy, and (h)
what is its power?
i1
3
+
+
-
-
1
2
+
-
Figure 27-72 Problem 76.
77
A temperature-stable resistor is made by connecting a
resistor made of silicon in series with one made of iron. If the re-
quired total resistance is 1000 0 in a wide temperature range
around 20/C, what should be the resistance of the (a) silicon resis-
tor and (b) iron resistor? (See Table 26-1.)
78
In Fig. 27-14, assume that # ! 5.0 V, r ! 2.0 0, R1 ! 5.0 0, and
R2 ! 4.0 0. If the ammeter resistance RA is 0.10 0, what percent
error does it introduce into the measurement of the current?
Assume that the voltmeter is not present.
79
An initially uncharged capacitor C is fully charged by a
device of constant emf 
connected in series with a resistor R.
(a) Show that the final energy stored in the capacitor is half the en-
ergy supplied by the emf device. (b) By direct integration of i2R
over the charging time, show that the thermal energy dissipated by
the resistor is also half the energy supplied by the emf device.
80
In Fig. 27-73, R1 ! 5.00 0, R2 !
10.0 0, R3 ! 15.0 0, C1 ! 5.00 mF,
C2 ! 10.0 mF, and the ideal battery
has emf # ! 20.0V.Assuming that the
circuit is in the steady state,what is the
total energy stored in the two
capacitors?
81
In Fig. 27-5a, find the potential
difference across R2 if # ! 12 V, R1
! 3.0 0, R2 ! 4.0 0, and R3 ! 5.0 0.
82
In Fig. 27-8a, calculate the potential difference between a and
c by considering a path that contains R, r1, and #1.
83
A controller on an electronic arcade game consists of
a variable resistor connected across the plates of a 0.220 mF capaci-
tor.The capacitor is charged to 5.00 V, then discharged through the
resistor. The time for the potential difference across the plates to
decrease to 0.800 V is measured by a
clock inside the game. If the range of
discharge times that can be handled
effectively is from 10.0 ms to 6.00 ms,
what should be the (a) lower value
and (b) higher value of the resist-
ance range of the resistor?
84
An automobile gasoline gauge
is shown schematically in Fig. 27-74.
The indicator (on the dashboard)
has a resistance of 10 0. The tank
SSM
#
SSM
SSM
C1
C2
R2
R1
R3
+
-
Figure 27-73 Problem 80.
-
+
12 V 
Rindicator
Rtank
Connected
through
chassis
Indicator
Tank
unit
Figure 27-74 Problem 84.
2
R2
C
-
+
1
R1
-
+
S
Figure 27-75 Problem  87.
4.0R
2.0R
6.0R
3.0R
R
B
A
Figure 27-76 Problem 89.
i2
i1
1
+
-
-
+
2
Figure 27-77 Problem 91.
Figure 27-78 Problem 92.
i1
R1
R2
R3
R4
I
I

#3 ! 5.00 V, and #4 ! 5.00 V, and the resistances are each 2.00 0.
What are the (a) size and (b) direction (left or right) of current i1 and
the (c) size and (d) direction of current i2? (This can be answered
with only mental calculation.) (e) At what rate is energy being trans-
ferred in battery 4, and (f) is the energy being supplied or absorbed
by the battery?
101
In Fig. 27-82, an ideal battery
of emf # ! 12.0 V is connected to a
network of resistances R1 ! 6.00 0,
R2 ! 12.0 0,R3 ! 4.00 0,R4 ! 3.00 0,
and R5 ! 5.00 0. What is the poten-
tial difference across resistance 5?
102
The following table gives the
electric 
potential 
difference 
VT
across the terminals of a battery as a
function of current i being drawn
from the battery. (a) Write an equation that represents the rela-
tionship between VT and i. Enter the data into your graphing calcu-
lator and perform a linear regression fit of VT versus i. From the
parameters of the fit, find (b) the battery’s emf and (c) its internal
resistance.
i(A):
50.0
75.0
100
125
150
175
200
VT(V):
10.7
9.00
7.70
6.00
4.80
3.00
1.70
103
In Fig. 27-83, #1 ! 6.00 V, #2 !
12.0 V, R1 ! 200 0, and R2 ! 100 0.
What are the (a) size and (b) direction
(up or down) of the current through
resistance 1, the (c) size and (d) direc-
tion of the current through resistance
2, and the (e) size and (f) direction of
the current through battery 2?
104
A three-way 120 V lamp bulb that contains two filaments is
rated for 100-200-300 W. One filament burns out. Afterward, the
bulb operates at the same intensity (dissipates energy at the same
rate) on its lowest as on its highest switch positions but does not
operate at all on the middle position. (a) How are the two fila-
ments wired to the three switch positions? What are the (b) smaller
and (c) larger values of the filament resistances?
105
In Fig. 27-84, R1 ! R2 ! 2.0 0, R3 ! 4.0 0, R4 ! 3.0 0, R5 !
1.0 0, and R6 ! R7 ! R8 ! 8.0 0, and the ideal batteries have emfs
#1 ! 16 V and #2 ! 8.0 V. What are the (a) size and (b) direction
(up or down) of current i1 and the (c) size and (d) direction of
current i2? What is the energy transfer rate in (e) battery 1 and
(f) battery 2? Is energy being supplied or absorbed in (g) battery 1
and (h) battery 2?
802
CHAPTER 27
CIRCUITS
10 W by connecting the resistor to a battery whose emf is 1.5 V. (a)
What potential difference must exist across the resistor? (b) What
must be the internal resistance of the battery?
94
Figure 27-79 shows three 20.0 0
resistors. Find the equivalent resist-
ance between points (a) A and B, (b)
A and C, and (c) B and C. (Hint:
Imagine that a battery is connected
between a given pair of points.)
95
A 120 V power line is protected by a 15 A fuse. What is the
maximum number of 500 W lamps that can be simultaneously op-
erated in parallel on this line without “blowing” the fuse because
of an excess of current?
96
Figure 27-63 shows an ideal battery of emf # ! 12 V,
a resistor of resistance R ! 4.0 0, and an uncharged capacitor of
capacitance C ! 4.0 mF.After switch S is closed, what is the current
through the resistor when the charge on the capacitor is 8.0 mC?
97
A group of N identical batteries of emf # and internal re-
sistance r may be connected all in series (Fig. 27-80a) or all in par-
allel (Fig. 27-80b) and then across a resistor R. Show that both
arrangements give the same current in R if R ! r.
SSM
+ - 
+ - 
r
r
R
(a)
+ - 
r
N batteries in series 
+
-
+
-
+
-
R
(b)
N batteries in parallel 
r 
r 
r 
Figure 27-80 Problem 97.
A
B
C
Figure 27-79 Problem 94.
Figure 27-82 Problem 101.
+ - 
R1
R2
R4
R5
R3
Figure 27-83 Problem 103.
+
-
-
+
R1
R2
2
1
Figure 27-81 Problem 100.
i1
i2
2
3
4
1
+
-
+
-
+
+
-
-
98
In Fig. 27-48, R1 ! R2
10.0 , and the ideal battery has emf
V. (a) What value of R3
maximizes the rate at which the bat-
tery supplies energy and (b) what is
that maximum rate?
99
In Fig. 27-66, the ideal bat-
SSM
# ! 12.0
0
!
SSM
tery 
has 
emf 
# ! 30 V,
the 
resistances 
are 
R1
20 k
and
R2
10 k , and the capacitor is un-
charged.When the switch is closed at
time t ! 0, what is the current in (a)
resistance 1 and (b) resistance 2? (c)
A long time later, what is the current
in resistance 2?
100
In Fig. 27-81, the ideal batteries
have emfs #1 ! 20.0 V, #2 ! 10.0 V,
0
!
0
!
Figure 27-84 Problem 105.
i2
i1
R1
R2
R3
R4
R5
R6
R7
R8
1
+
-
- + 
2
