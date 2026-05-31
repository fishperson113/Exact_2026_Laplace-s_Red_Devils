Sample Problem 26.04
A material has resistivity, a block of the material has resistance
A rectangular block of iron has dimensions 1.2 cm
1.2 cm $ 15 cm. A potential difference is to be applied to
the block between parallel sides and in such a way that
those sides are equipotential surfaces (as in Fig. 26-8b).
What is the resistance of the block if the two parallel
sides are (1) the square ends (with dimensions 1.2 cm $
1.2 cm) and (2) two rectangular sides (with dimensions
1.2 cm $ 15 cm)?
KEY IDEA
The resistance R of an object depends on how the electric
potential is applied to the object. In particular, it depends
on the ratio L/A, according to Eq. 26-16 (R ! rL/A),
where A is the area of the surfaces to which the potential
difference is applied and L is the distance between those
surfaces.
$
Additional examples, video, and practice available at WileyPLUS
26-4 OHM’S LAW
After reading this module, you should be able to . . .
26.22 Distinguish between an object that obeys Ohm’s law
and one that does not.
26.23 Distinguish between a material that obeys Ohm’s law
and one that does not.
26.24 Describe the general motion of a conduction electron
in a current.
26.25 For the conduction electrons in a conductor, explain
the relationship between the mean free time t, the effective
speed, and the thermal (random) motion.
26.26 Apply the relationship between resistivity r, number
density n of conduction electrons, and the mean free time
t of the electrons.
Learning Objectives
●A given device (conductor, resistor, or any other 
electrical device) obeys Ohm’s law if its resistance 
R (! V/i) is independent of the applied potential 
difference V.
●A given material obeys Ohm’s law if its resistivity r (! E/J)
is independent of the magnitude and direction of the applied
electric field .
●The assumption that the conduction electrons in a metal
are free to move like the molecules in a gas leads to an
E
:
expression for the resistivity of a metal:
Here n is the number of free electrons per unit volume and t
is the mean time between the collisions of an electron with
the atoms of the metal.
●Metals obey Ohm’s law because the mean free time t is
approximately independent of the magnitude E of any electric
field applied to a metal.
r !
m
e2nt .
Key Ideas

Figure 26-11a shows how to distinguish such devices. A potential difference
V is applied across the device being tested, and the resulting current i through the
device is measured as V is varied in both magnitude and polarity. The polarity of
V is arbitrarily taken to be positive when the left terminal of the device is at a
higher potential than the right terminal. The direction of the resulting current
(from left to right) is arbitrarily assigned a plus sign. The reverse polarity of V
(with the right terminal at a higher potential) is then negative; the current it
causes is assigned a minus sign.
Figure 26-11b is a plot of i versus V for one device. This plot is a straight line
passing through the origin, so the ratio i/V (which is the slope of the straight line) is
the same for all values of V.This means that the resistance R ! V/i of the device is
independent of the magnitude and polarity of the applied potential difference V.
Figure 26-11c is a plot for another conducting device. Current can exist in this
device only when the polarity of V is positive and the applied potential difference
is more than about 1.5 V.When current does exist, the relation between i and V is
not linear; it depends on the value of the applied potential difference V.
We distinguish between the two types of device by saying that one obeys
Ohm’s law and the other does not.
757
26-4 OHM’S LAW
+2
0
-2
Current (mA) 
Potential difference (V) 
-2 
0 
+2 
+4 
+4
+2
0
-2
Current (mA) 
-4 
-2 
0 
+2 
+4 
(a)
(b)
(c)
V
?
i
+ 
- 
i
Potential difference (V) 
-4
Figure 26-11 (a) A potential difference V is
applied to the terminals of a device, estab-
lishing a current i. (b) A plot of current i
versus applied potential difference V when
the device is a 1000 0 resistor. (c) A plot
when the device is a semiconducting pn
junction diode.
(This assertion is correct only in certain situations; still, for historical reasons, the
term “law” is used.) The device of Fig. 26-11b-which turns out to be a 1000 0
resistor-obeys Ohm’s law.The device of Fig. 26-11c-which is called a pn junc-
tion diode-does not.
Ohm’s law is an assertion that the current through a device is always directly
proportional to the potential difference applied to the device.
A conducting device obeys Ohm’s law when the resistance of the device is
independent of the magnitude and polarity of the applied potential difference.
It is often contended that V ! iR is a statement of Ohm’s law.That is not true!
This equation is the defining equation for resistance,and it applies to all conducting
devices, whether they obey Ohm’s law or not. If we measure the potential differ-
ence V across, and the current i through, any device, even a pn junction diode, we
can find its resistance at that value of V as R
V/i.The essence of Ohm’s law, how-
ever,is that a plot of i versus V is linear;that is,R is independent of V.We can gener-
alize this for conducting materials by using Eq.26-11 (E
: ! r J
:):
!
Checkpoint 4
The following table gives the current i (in
amperes) through two devices for several
values of potential difference V (in volts).
From these data, determine which device
does not obey Ohm’s law.
Device 1
Device 2
V
i
V
i
2.00
4.50
2.00
1.50
3.00
6.75
3.00
2.20
4.00
9.00
4.00
2.80
A conducting material obeys Ohm’s law when the resistivity of the material is
independent of the magnitude and direction of the applied electric field.
All homogeneous materials, whether they are conductors like copper or semicon-
ductors like pure silicon or silicon containing special impurities, obey Ohm’s law
within some range of values of the electric field. If the field is too strong, how-
ever, there are departures from Ohm’s law in all cases.

A Microscopic View of Ohm’s Law
To find out why particular materials obey Ohm’s law, we must look into the
details of the conduction process at the atomic level. Here we consider only con-
duction in metals, such as copper. We base our analysis on the free-electron
model, in which we assume that the conduction electrons in the metal are free to
move throughout the volume of a sample, like the molecules of a gas in a closed
container. We also assume that the electrons collide not with one another but
only with atoms of the metal.
According to classical physics,the electrons should have a Maxwellian speed dis-
tribution somewhat like that of the molecules in a gas (Module 19-6),and thus the av-
erage electron speed should depend on the temperature. The motions of electrons
are, however, governed not by the laws of classical physics but by those of quantum
physics. As it turns out, an assumption that is much closer to the quantum reality is
that conduction electrons in a metal move with a single effective speed veff, and this
speed is essentially independent of the temperature. For copper, veff % 1.6 $ 106 m/s.
When we apply an electric field to a metal sample, the electrons modify their
random motions slightly and drift very slowly-in a direction opposite that of
the field-with an average drift speed vd. The drift speed in a typical metallic
conductor is about 5 $ 10 #7 m/s, less than the effective speed (1.6 $ 10 6 m/s) by
many orders of magnitude. Figure 26-12 suggests the relation between these two
speeds.The gray lines show a possible random path for an electron in the absence
of an applied field; the electron proceeds from A to B, making six collisions along
the way. The green lines show how the same events might occur when an electric
field 
is applied.We see that the electron drifts steadily to the right, ending at B-
rather than at B. Figure 26-12 was drawn with the assumption that vd % 0.02veff.
However, because the actual value is more like vd % (10 #13)veff, the drift dis-
played in the figure is greatly exaggerated.
The motion of conduction electrons in an electric field 
is thus a combina-
tion of the motion due to random collisions and that due to 
When we consider
all the free electrons, their random motions average to zero and make no con-
tribution to the drift speed. Thus, the drift speed is due only to the effect of the
electric field on the electrons.
If an electron of mass m is placed in an electric field of magnitude E, the elec-
tron will experience an acceleration given by Newton’s second law:
(26-18)
After a typical collision, each electron will-so to speak-completely lose its
memory of its previous drift velocity, starting fresh and moving off in a random di-
rection. In the average time t between collisions, the average electron will acquire a
drift speed of vd ! at.Moreover,if we measure the drift speeds of all the electrons at
any instant, we will find that their average drift speed is also at.Thus, at any instant,
on average,the electrons will have drift speed vd ! at.Then Eq.26-18 gives us
(26-19)
vd ! at ! eEt
m .
a ! F
m ! eE
m .
E
:.
E
:
E
:
758
CHAPTER 26
CURRENT AND RESISTANCE
B
B'
A
E
Figure 26-12 The gray lines show an electron moving
from A to B, making six collisions en route.The green
lines show what the electron’s path might be in the
presence of an applied electric field 
Note the steady
drift in the direction of 
(Actually, the green lines
should be slightly curved, to represent the parabolic
paths followed by the electrons between collisions, un-
der the influence of an electric field.)
#E
:.
E
:.

Combining this result with Eq. 26-7 
in magnitude form, yields
(26-20)
which we can write as
(26-21)
Comparing this with Eq. 26-11 
in magnitude form, leads to
(26-22)
Equation 26-22 may be taken as a statement that metals obey Ohm’s law if we
can show that, for metals, their resistivity r is a constant, independent of the
strength of the applied electric field 
Let’s consider the quantities in Eq. 26-22.
We can reasonably assume that n, the number of conduction electrons per vol-
ume, is independent of the field, and m and e are constants.Thus, we only need to
convince ourselves that t, the average time (or mean free time) between colli-
sions, is a constant, independent of the strength of the applied electric field.
Indeed, t can be considered to be a constant because the drift speed vd caused by
the field is so much smaller than the effective speed veff that the electron speed-
and thus t-is hardly affected by the field. Thus, because the right side of 
Eq. 26-22 is independent of the field magnitude, metals obey Ohm’s law.
E
:.
r !
m
e2nt .
(E
: ! r J
:),
E !#
m
e2nt$ J.
vd !
J
ne ! eEt
m ,
( J
: ! nev
:
d),
759
26-4 OHM’S LAW
Using these results and substituting for the electron mass m,
we then have
(Answer)
(b) The mean free path l of the conduction electrons in a
conductor is the average distance traveled by an electron
between collisions. (This definition parallels that in
Module 19-5 for the mean free path of molecules in a gas.)
What is l for the conduction electrons in copper, assuming
that their effective speed veff is 1.6 $ 10 6 m/s?
KEY IDEA
The distance d any particle travels in a certain time t at a
constant speed v is d ! vt.
Calculation: For the electrons in copper, this gives us
(26-24)
(Answer)
This is about 150 times the distance between nearest-
neighbor atoms in a copper lattice. Thus, on the average,
each conduction electron passes many copper atoms before
finally hitting one.
! 4.0 $ 10 #8 m ! 40 nm.
! (1.6 $ 10 6 m/s)(2.5 $ 10 #14 s)
l ! vefft
t !
9.1 $ 10 #31 kg
3.67 $ 10 #17 kg/s ! 2.5 $ 10 #14 s.
