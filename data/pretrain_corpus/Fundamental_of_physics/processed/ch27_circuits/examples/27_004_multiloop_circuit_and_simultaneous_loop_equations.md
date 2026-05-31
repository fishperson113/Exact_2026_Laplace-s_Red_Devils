Sample Problem 27.04
Multiloop circuit and simultaneous loop equations

The Ammeter and the Voltmeter
An instrument used to measure currents is called an ammeter. To measure the
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
of any circuit element across which the voltmeter is connected. Otherwise, the
meter alters the potential difference that is to be measured.
Often a single meter is packaged so that, by means of a switch, it can be made
to serve as either an ammeter or a voltmeter-and usually also as an ohmmeter,
designed to measure the resistance of any element connected between its termi-
nals. Such a versatile unit is called a multimeter.
788
CHAPTER 27
CIRCUITS
27-3 THE AMMETER AND THE VOLTMETER
After reading this module, you should be able to . . .
27.26 Explain the use of an ammeter and a voltmeter, includ-
Learning Objective
●Here are three measurement instruments used with cir-
cuits: An ammeter measures current. A voltmeter measures
Key Idea
+
-
R2
A
R1
r
a
b
c
d
V
i
i
Figure 27-14 A single-loop circuit, showing
how to connect an ammeter (A) and a
voltmeter (V).
27-4 RC CIRCUITS
After reading this module, you should be able to . . .
27.27 Draw schematic diagrams of charging and discharging
RC circuits.
27.28 Write the loop equation (a differential equation) for a
charging RC circuit.
27.29 Write the loop equation (a differential equation) for a
discharging RC circuit.
27.30 For a capacitor in a charging or discharging RC circuit,
apply the relationship giving the charge as a function of time.
27.31 From the function giving the charge as a function of
time in a charging or discharging RC circuit, find the ca-
pacitor’s potential difference as a function of time.
27.32 In a charging or discharging RC circuit, find the resis-
tor’s current and potential difference as functions of time.
27.33 Calculate the capacitive time constant t.
27.34 For a charging RC circuit and a discharging RC circuit,
determine the capacitor’s charge and potential difference
at the start of the process and then a long time later.
Learning Objectives
●When an emf is applied to a resistance R and capacitance C
in series, the charge on the capacitor increases according to
q ! C#(1 # e#t/RC)
(charging a capacitor),
in which C# ! q0 is the equilibrium (final) charge and RC ! t
is the capacitive time constant of the circuit. 
●During the charging, the current is
(charging a capacitor).
i ! dq
dt !#
#
R $e#t/RC
#
Key Ideas
●When a capacitor discharges through a resistance R, the
charge on the capacitor decays according to
q ! q0e#t/RC
(discharging a capacitor).
●During the discharging, the current is
(discharging a capacitor).
i ! dq
dt ! ##
q0
RC$e#t/RC
ing the resistance required of each in order not to affect the
measured quantities.
voltage (potential differences). A multimeter can be used to
measure current, voltage, or resistance.

RC Circuits
In preceding modules we dealt only with circuits in which the currents did not
vary with time. Here we begin a discussion of time-varying currents.
Charging a Capacitor
The capacitor of capacitance C in Fig. 27-15 is initially uncharged.To charge it, we
close switch S on point a. This completes an RC series circuit consisting of the
capacitor, an ideal battery of emf #, and a resistance R.
From Module 25-1, we already know that as soon as the circuit is com-
plete, charge begins to flow (current exists) between a capacitor plate and a
battery terminal on each side of the capacitor. This current increases the
charge q on the plates and the potential difference VC (! q/C) across the ca-
pacitor. When that potential difference equals the potential difference across
the battery (which here is equal to the emf #), the current is zero. From Eq.
25-1 (q ! CV), the equilibrium (final) charge on the then fully charged capacitor
is equal to C #.
Here we want to examine the charging process. In particular we want to
know how the charge q(t) on the capacitor plates, the potential difference VC(t)
across the capacitor, and the current i(t) in the circuit vary with time during the
charging process. We begin by applying the loop rule to the circuit, traversing it
clockwise from the negative terminal of the battery.We find
(27-30)
The last term on the left side represents the potential difference across the capac-
itor.The term is negative because the capacitor’s top plate, which is connected to
the battery’s positive terminal, is at a higher potential than the lower plate.Thus,
there is a drop in potential as we move down through the capacitor.
We cannot immediately solve Eq. 27-30 because it contains two variables,
i and q. However, those variables are not independent but are related by
(27-31)
Substituting this for i in Eq. 27-30 and rearranging, we find
(charging equation).
(27-32)
This differential equation describes the time variation of the charge q on the
capacitor in Fig. 27-15. To solve it, we need to find the function q(t) that satisfies
this equation and also satisfies the condition that the capacitor be initially
uncharged; that is, q ! 0 at t ! 0.
We shall soon show that the solution to Eq. 27-32 is
q ! C#(1 # e#t/RC)
(charging a capacitor).
(27-33)
(Here e is the exponential base, 2.718 . . . , and not the elementary charge.)
Note that Eq. 27-33 does indeed satisfy our required initial condition, because
at t ! 0 the term e#t/RC is unity; so the equation gives q ! 0. Note also that as t
goes to infinity (that is, a long time later), the term e#t/RC goes to zero; so
the equation gives the proper value for the full (equilibrium) charge on the
capacitor-namely, q ! C #. A plot of q(t) for the charging process is given in
Fig. 27-16a.
The derivative of q(t) is the current i(t) charging the capacitor:
(charging a capacitor).
(27-34)
i ! dq
dt !#
#
R$e#t/RC
R dq
dt % q
C ! #
i ! dq
dt .
# # iR # q
C ! 0.
789
27-4 RC CIRCUITS
Figure 27-15 When switch S is closed on a,the
capacitor is charged through the resistor.
When the switch is afterward closed on b,the
capacitor discharges through the resistor.
C
+
-
S
R
b
a
Figure 27-16 (a) A plot of Eq. 27-33, which
shows the buildup of charge on the capaci-
tor of Fig. 27-15. (b) A plot of Eq. 27-34,
which shows the decline of the charging
current in the circuit of Fig. 27-15.The
curves are plotted for R ! 2000 0,C ! 1 mF,
and # ! 10 V; the small triangles represent
successive intervals of one time constant t.
q (  C) 
12
i (mA) 
6
8
4
4
2
0
0
2 
4 
6 
8 
10 
2 
4 
6 
8 
Time (ms) 
Time (ms) 
(a)
(b)
10
µ 
C
/R
The capacitor’s charge
grows as the resistor’s
current dies out.

A plot of i(t) for the charging process is given in Fig. 27-16b. Note that the current
has the initial value #/R and that it decreases to zero as the capacitor becomes
fully charged.
790
CHAPTER 27
CIRCUITS
A capacitor that is being charged initially acts like ordinary connecting wire 
relative to the charging current. A long time later, it acts like a broken wire.
By combining Eq. 25-1 (q ! CV) and Eq. 27-33, we find that the potential
difference VC(t) across the capacitor during the charging process is
(charging a capacitor).
(27-35)
This tells us that VC ! 0 at t ! 0 and that VC ! # when the capacitor becomes
fully charged as t : ,.
The Time Constant
The product RC that appears in Eqs. 27-33, 27-34, and 27-35 has the dimensions
of time (both because the argument of an exponential must be dimensionless and
because, in fact, 1.0 0 $ 1.0 F ! 1.0 s). The product RC is called the capacitive
time constant of the circuit and is represented with the symbol t:
t ! RC
(time constant).
(27-36)
From Eq. 27-33, we can now see that at time t ! t (! RC), the charge on the
initially uncharged capacitor of Fig. 27-15 has increased from zero to
q ! C#(1 # e#1) ! 0.63C#.
(27-37)
In words, during the first time constant t the charge has increased from zero to
63% of its final value C#. In Fig. 27-16, the small triangles along the time axes
mark successive intervals of one time constant during the charging of the capaci-
tor.The charging times for RC circuits are often stated in terms of t. For example,
a circuit with t ! 1 ms charges quickly while one with t ! 100 s charges much
more slowly,
Discharging a Capacitor
Assume now that the capacitor of Fig. 27-15 is fully charged to a potential V0
equal to the emf # of the battery.At a new time t ! 0, switch S is thrown from a to
b so that the capacitor can discharge through resistance R. How do the charge
q(t) on the capacitor and the current i(t) through the discharge loop of capacitor
and resistance now vary with time?
The differential equation describing q(t) is like Eq. 27-32 except that now,
with no battery in the discharge loop, # ! 0.Thus,
(discharging equation).
(27-38)
The solution to this differential equation is
q ! q0e#t/RC
(discharging a capacitor),
(27-39)
where q0 (! CV0) is the initial charge on the capacitor.You can verify by substitu-
tion that Eq. 27-39 is indeed a solution of Eq. 27-38.
R dq
dt % q
C ! 0
VC ! q
C ! #(1 # e#t/RC)

Equation 27-39 tells us that q decreases exponentially with time, at a rate that
is set by the capacitive time constant t ! RC. At time t ! t, the capacitor’s
charge has been reduced to q0e#1, or about 37% of the initial value. Note that a
greater t means a greater discharge time.
Differentiating Eq. 27-39 gives us the current i(t):
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
(27-41)
The general solution to this differential equation is of the form
q ! qp % Ke#at,
(27-42)
where qp is a particular solution of the differential equation, K is a constant to
be evaluated from the initial conditions, and a ! 1/RC is the coefficient of q in
Eq. 27-41. To find qp, we set dq/dt ! 0 in Eq. 27-41 (corresponding to the final
condition of no further charging), let q ! qp, and solve, obtaining
qp ! C#.
(27-43)
To evaluate K, we first substitute this into Eq. 27-42 to get
q ! C# % Ke#at.
Then substituting the initial conditions q ! 0 and t ! 0 yields
0 ! C# % K,
or K ! #C#. Finally, with the values of qp, a, and K inserted, Eq. 27-42 becomes
q ! C# # C#e#t/RC,
which, with a slight modification, is Eq. 27-33.
dq
dt %
q
RC ! #
R .
i ! dq
dt ! ##
q0
RC$e#t/RC
791
27-4 RC CIRCUITS
Checkpoint 5
The table gives four sets of values for the circuit elements in Fig. 27-15. Rank the
sets according to (a) the initial current (as the switch is closed on a) and (b) the time
required for the current to decrease to half its initial value, greatest first.
1
2
3
4
# (V)
12
12
10
10
R (0)
2
3
10
5
C (mF)
3
2
0.5
2

792
CHAPTER 27
CIRCUITS
