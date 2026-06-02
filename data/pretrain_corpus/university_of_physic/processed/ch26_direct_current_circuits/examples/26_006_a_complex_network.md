Example 26.6
A complex network
Figure 26.12 shows a “bridge” circuit of the type described at the
beginning of this section (see Fig. 26.6b). Find the current in
each resistor and the equivalent resistance of the network of five
resistors.
SOLUTION
IDENTIFY and SET UP: This network is neither a series combina-
tion nor a parallel combination. Hence we must use Kirchhoff’s
rules to find the values of the target variables. There are five
unknown currents, but by applying the junction rule to junctions a
and b, we can represent them in terms of three unknown currents
and , as shown in Fig. 26.12.
I3
I2,
I1,
EXECUTE: We apply the loop rule to the three loops shown:
(1)
(2)
(3)
One way to solve these simultaneous equations is to solve Eq. (3)
for 
obtaining 
and then substitute this expression
into Eq. (2) to eliminate 
We then have
(1 )
(2 )
Now we can eliminate 
by multiplying Eq. 
by 5 and adding
the two equations. We obtain
We substitute this result into Eq. 
to obtain 
and
from Eq. (3) we find 
The negative value of 
tells us
that its direction is opposite to the direction we assumed.
The total current through the network is 
and
the potential drop across it is equal to the battery emf, 13 V. The
equivalent resistance of the network is therefore
EVALUATE: You can check our results for 
and 
by substitut-
ing them back into Eqs. (1)-(3). What do you find?
I3
I2,
I1,
Req = 13 V
11 A = 1.2 Æ
I1 + I2 = 11 A,
I3
I2 = 5 A.
I3 = -1 A,
(1¿)
78 V = I1113 Æ2  I1 = 6 A
(1¿)
I3
¿
13 V = I113 Æ2 + I315 Æ2
¿
13 V = I112 Æ2 - I311 Æ2
I2.
I2 = I1 + I3,
I2,
-I111 Æ2 - I311 Æ2 + I211 Æ2 = 0
-I211 Æ2 - 1I2 + I3212 Æ2 + 13 V = 0
13 V - I111 Æ2 - 1I1 - I3211 Æ2 = 0
c
b
I1
I2
I1 - I3
(2)
I3
(3)
2 V
1 V
1 V
1 V
1 V
+
(1)
13 V
a
d
I2 + I3
I1 + I2
26.12 A network circuit with several resistors.

26.3 Electrical Measuring Instruments
We’ve been talking about potential difference, current, and resistance for two
chapters, so it’s about time we said something about how to measure these quan-
tities. Many common devices, including car instrument panels, battery chargers,
and inexpensive electrical instruments, measure potential difference (voltage),
current, or resistance using a d’Arsonval galvanometer (Fig. 26.13). In the fol-
lowing discussion we’ll often call it just a meter. A pivoted coil of fine wire is
placed in the magnetic field of a permanent magnet (Fig. 26.14). Attached to the
coil is a spring, similar to the hairspring on the balance wheel of a watch. In the
equilibrium position, with no current in the coil, the pointer is at zero. When
there is a current in the coil, the magnetic field exerts a torque on the coil that is
proportional to the current. (We’ll discuss this magnetic interaction in detail in
Chapter 27.) As the coil turns, the spring exerts a restoring torque that is propor-
tional to the angular displacement.
Thus the angular deflection of the coil and pointer is directly proportional to
the coil current, and the device can be calibrated to measure current. The maxi-
mum deflection, typically 
or so, is called full-scale deflection. The essential
electrical characteristics of the meter are the current 
required for full-scale
deflection (typically on the order of 
to 10 mA) and the resistance 
of the
coil (typically on the order of 10 to 
).
The meter deflection is proportional to the current in the coil. If the coil obeys
Ohm’s law, the current is proportional to the potential difference between the ter-
minals of the coil, and the deflection is also proportional to this potential differ-
ence. For example, consider a meter whose coil has a resistance 
and that deflects full scale when the current in its coil is 
The cor-
responding potential difference for full-scale deflection is
Ammeters
A current-measuring instrument is usually called an ammeter (or milliammeter,
microammeter, and so forth, depending on the range). An ammeter always meas-
ures the current passing through it. An ideal ammeter, discussed in Section 25.4,
would have zero resistance, so including it in a branch of a circuit would not
V = IfsRc = 11.00 * 10-3 A2120.0 Æ2 = 0.0200 V
Ifs = 1.00 mA.
Rc = 20.0 Æ
1000 Æ
Rc
10 mA
Ifs
90°
860
CHAPTER 26 Direct-Current Circuits
Test Your Understanding of Section 26.2
Subtract Eq. (1) from Eq. (2) in
Example 26.6. To which loop in Fig. 26.12 does this equation correspond? Would this
equation have simplified the solution of Example 26.6?
❙
