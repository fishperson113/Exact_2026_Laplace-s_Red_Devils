Example 29.1
Emf and current induced in a loop
The magnetic field between the poles of the electromagnet in 
Fig. 29.5 is uniform at any time, but its magnitude is increasing
at the rate of 
The area of the conducting loop in the
field is 
and the total circuit resistance, including the
120 cm2,
0.020 T>s.
meter, is 
(a) Find the induced emf and the induced current
in the circuit. (b) If the loop is replaced by one made of an insula-
tor, what effect does this have on the induced emf and induced
current?
5.0 Æ.

29.2 Faraday’s Law
961
Direction of Induced emf
We can find the direction of an induced emf or current by using Eq. (29.3)
together with some simple sign rules. Here’s the procedure:
1. Define a positive direction for the vector area 
2. From the directions of 
and the magnetic field 
determine the sign of
the magnetic flux 
and its rate of change 
Figure 29.6 shows
several examples.
3. Determine the sign of the induced emf or current. If the flux is increasing, so
is positive, then the induced emf or current is negative; if the flux is
decreasing, 
is negative and the induced emf or current is positive.
4. Finally, determine the direction of the induced emf or current using your
right hand. Curl the fingers of your right hand around the 
vector, with
your right thumb in the direction of 
If the induced emf or current in the
circuit is positive, it is in the same direction as your curled fingers; if the
induced emf or current is negative, it is in the opposite direction.
In Example 29.1, in which 
is upward, a positive 
would be directed coun-
terclockwise around the loop, as seen from above. Both 
and 
are upward in
this example, so 
is positive; the magnitude B is increasing, so 
is pos-
itive. Hence by Eq. (29.3), 
in Example 29.1 is negative. Its actual direction is
thus clockwise around the loop, as seen from above.
If the loop in Fig. 29.5 is a conductor, an induced current results from this
emf; this current is also clockwise, as Fig. 29.5 shows. This induced current pro-
duces an additional magnetic field through the loop, and the right-hand rule
described in Section 28.6 shows that this field is opposite in direction to the
increasing field produced by the electromagnet. This is an example of a general
rule called Lenz’s law, which says that any induction effect tends to oppose the
change that caused it; in this case the change is the increase in the flux of the
E
d£B>dt
£B
B
S
A
S
E
A
S
A
S.
A
S
d£B>dt
d£B>dt
d£B/dt.
£B
B
S,
A
S
A
S.
SOLUTION
IDENTIFY and SET UP: The magnetic flux 
through the loop
changes as the magnetic field changes. Hence there will be an
induced emf 
and an induced current I in the loop. We calculate
using Eq. (29.2), then find 
using Faraday’s law. Finally, we
calculate I using 
where R is the total resistance of the cir-
cuit that includes the loop.
EXECUTE: (a) The area vector 
for the loop is perpendicular to the
plane of the loop; we take 
to be vertically upward. Then 
and 
are parallel, and because 
is uniform the magnetic flux through
the loop is 
The area 
is constant, so the rate of change of magnetic flux is
A = 0.012 m2
£B = B
S # A
S = BAcos0 = BA.
B
S
B
S
A
S
A
S
A
S
E = IR,
E
£B
E
£B
This, apart from a sign that we haven’t discussed yet, is the
induced emf . The corresponding induced current is
(b) By changing to an insulating loop, we’ve made the resist-
ance of the loop very high. Faraday’s law, Eq. (29.3), does not
involve the resistance of the circuit in any way, so the induced emf
does not change. But the current will be smaller, as given by the
equation 
. If the loop is made of a perfect insulator with
infinite resistance, the induced current is zero. This situation is
analogous to an isolated battery whose terminals aren’t connected
to anything: An emf is present, but no current flows.
EVALUATE: Let’s verify unit consistency in this calculation. One
way to do this is to note that the magnetic-force relationship
implies that the units of 
are the units of force
divided by the units of (charge times velocity): 
The units of magnetic flux are then 
and the rate of change of magnetic flux is
Thus the unit of 
is the volt, as
required by Eq. (29.3). Also recall that the unit of magnetic flux is
the weber (Wb): 
so 1 V = 1 Wb>s.
1 T # m2 = 1 Wb,
d£B>dt
1 N # m>C = 1 J>C = 1 V.
1 N # s # m>C,
11 T211 m22 =
11 C # m>s2.
1 T = 11 N2>
B
S
F
S  qv
S : B
S
I = E>R
I = E
R = 2.4 * 10-4 V
5.0 Æ
= 4.8 * 10-5A = 0.048 mA
E
= 2.4 * 10-4 V = 0.24 mV
d£B
dt
=
d1BA2
dt
= dB
dt A = 10.020 T>s210.012 m22
A 5 120 cm2 5 0.012 m2
Total resistance in circuit
and meter 5 5.0 V
I
SA
S
b
a
N
dB/dt 5 0.020 T/s
0
29.5 A stationary conducting loop in an increasing magnetic field.
Application Exploring the Brain 
with Induced emfs
Transcranial magnetic stimulation (TMS) is a
technique for studying the function of various
parts of the brain. A coil held to the subject’s
head carries a varying electric current, and so
produces a varying magnetic field. This field
causes an induced emf, and that triggers elec-
tric activity in the region of the brain under-
neath the coil. By observing how the TMS
subject responds (for instance, which muscles
move as a result of stimulating a certain part
of the brain), a physician can test for various
neurological conditions.

electromagnet’s field through the loop. (We’ll study this law in detail in the next
section.)
You should check out the signs of the induced emfs and currents for the list of
experiments in Section 29.1. For example, when the loop in Fig. 29.2 is in a con-
stant field and we tilt it or squeeze it to decrease the flux through it, the induced
emf and current are counterclockwise, as seen from above.
CAUTION
Induced emfs are caused by changes in flux Since magnetic flux plays a cen-
tral role in Faraday’s law, it’s tempting to think that flux is the cause of induced emf and
that an induced emf will appear in a circuit whenever there is a magnetic field in the region
bordered by the circuit. But Eq. (29.3) shows that only a change in flux through a circuit,
not flux itself, can induce an emf in a circuit. If the flux through a circuit has a constant
value, whether positive, negative, or zero, there is no induced emf. ❙
If we have a coil with N identical turns, and if the flux varies at the same rate
through each turn, the total rate of change through all the turns is N times as large
as for a single turn. If 
is the flux through each turn, the total emf in a coil with
N turns is
(29.4)
As we discussed in this chapter’s introduction, induced emfs play an essential
role in the generation of electric power for commercial use. Several of the fol-
lowing examples explore different methods of producing emfs by the motion of a
conductor relative to a magnetic field, giving rise to a changing flux through a
circuit.
E = -N d£B
dt
£B
962
CHAPTER 29 Electromagnetic Induction
B
(increasing)
A
f
• Flux is positive (FB  0) ...
• ... and becoming more positive (dFB/dt  0).
• Induced emf is negative (E  0).
E
B
(decreasing)
A
f
• Flux is positive (FB  0) ...
• ... and becoming less positive (dFB/dt  0).
• Induced emf is positive (E  0).
E
B
(increasing)
A
f
• Flux is negative (FB  0) ...
• ... and becoming more negative (dFB/dt  0).
• Induced emf is positive (E  0).
E
B
(decreasing)
A
f
• Flux is negative (FB  0) ...
• ... and becoming less negative (dFB/dt  0).
• Induced emf is negative (E  0).
E
(d)
S
S
S
S
S
S
S
S
(c)
(b)
(a)
29.6 The magnetic flux is becoming (a) more positive, (b) less positive, (c)
more negative, and (d) less negative. Therefore 
is increasing in (a) and (d) and
decreasing in (b) and (c). In (a) and (d) the emfs are negative (they are opposite to
the direction of the curled fingers of your right hand when your right thumb points along
In (b) and (c) the emfs are positive (in the same direction as the curled fingers).
A
S).
£B
PhET: Faraday’s Electromagnetic Lab
PhET: Faraday’s Law
PhET: Generator

29.2 Faraday’s Law
963
Problem-Solving Strategy 29.1
Faraday’s Law
IDENTIFY the relevant concepts: Faraday’s law applies when there
is a changing magnetic flux. To use the law, identify an area
through which there is a flux of magnetic field. This will usually be
the area enclosed by a loop made of a conducting material (though
not always-see part (b) of Example 29.1). Identify the target
variables.
SET UP the problem using the following steps:
1. Faraday’s law relates the induced emf to the rate of change of
magnetic flux. To calculate this rate of change, you first have to
understand what is making the flux change. Is the conductor
moving? Is it changing orientation? Is the magnetic field
changing? Remember that it’s not the flux itself that counts, but
its rate of change.
2. The area vector 
(or 
) must be perpendicular to the plane of
the area. You always have two choices of its direction; for
example, if the area is in a horizontal plane, 
could point up or
A
S
dA
S
A
S
down. Choose a direction and use it consistently throughout the
problem.
EXECUTE the solution as follows:
1. Calculate the magnetic flux using Eq. (29.2) if 
is uniform
over the area of the loop or Eq. (29.1) if it isn’t uniform.
Remember the direction you chose for the area vector.
2. Calculate the induced emf using Eq. (29.3) or (if your conduc-
tor has N turns in a coil) Eq. (29.4). Apply the sign rule
(described just after Example 29.1) to determine the positive
direction of emf.
3. If the circuit resistance is known, you can calculate the magni-
tude of the induced current I using
EVALUATE your answer: Check your results for the proper units,
and double-check that you have properly implemented the sign
rules for magnetic flux and induced emf.
E = IR.
B
S
