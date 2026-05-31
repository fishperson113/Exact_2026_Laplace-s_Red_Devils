Example 29.10
The Faraday disk dynamo
Figure 29.16 shows a conducting disk with radius R that lies in the
xy-plane and rotates with constant angular velocity 
about the 
z-axis. The disk is in a uniform, constant 
field in the z-direction.
Find the induced emf between the center and the rim of the disk.
SOLUTION
IDENTIFY and SET UP: A motional emf arises because the con-
ducting disk moves relative to . The complication is that different
B
S
B
S
v
parts of the disk move at different speeds 
depending on their
distance from the rotation axis. We’ll address this by considering
small segments of the disk and integrating their contributions to
determine our target variable, the emf between the center and the
rim. Consider the small segment of the disk shown in red in 
Fig. 29.16 and labeled by its velocity vector 
The magnetic force
per unit charge on this segment is 
which points radially out-
ward from the center of the disk. Hence the induced emf tends to
make a current flow radially outward, which tells us that the mov-
ing conducting path to think about here is a straight line from the
center to the rim. We can find the emf from each small disk seg-
ment along this line using 
and then integrate
to find the total emf.
EXECUTE: The length vector 
(of length dr) associated with the
segment points radially outward, in the same direction as 
The vectors 
and 
are perpendicular, and the magnitude of 
is
The emf from the segment is then 
. The total
emf is the integral of 
from the center 
to the rim
:
EVALUATE: We can use this device as a source of emf in a circuit by
completing the circuit through two stationary brushes (labeled b in
the figure) that contact the disk and its conducting shaft as shown.
Such a disk is called a Faraday disk dynamo or a homopolar gen-
erator. Unlike the alternator in Example 29.3, the Faraday disk
dynamo is a direct-current generator; it produces an emf that is
constant in time. Can you use Lenz’s law to show that for the
direction of rotation in Fig. 29.16, the current in the external circuit
must be in the direction shown?
E =
L
R
0
vBrdr = 1
2 vBR2
1r = R2
1r = 02
dE
dE = vBrdr
v = vr.
v
S
B
S
v
S
v
S : B
S.
dl
S
dE = 1v
S : B
S2 # dl
S
v
S : B
S,
v
S.
v,
R
y
z
b
b
I
x
r
dr
B
B
v
Speed of small radial segment
of length dr at radius r is v  vr.
Emf induced across this segment is
dE  vB dr  vBr dr.
B
B
v
S
S
S
S
S
29.16 A conducting disk with radius R rotating at an angular
speed 
in a magnetic field 
The emf is induced along radial
lines of the disk and is applied to an external circuit through the
two sliding contacts labeled b.
B
S.
v
Test Your Understanding of Section 29.4
The earth’s magnetic field
points toward (magnetic) north. For simplicity, assume that the field has no verti-
cal component (as is the case near the earth’s equator). (a) If you hold a metal rod
in your hand and walk toward the east, how should you orient the rod to get the maxi-
mum motional emf between its ends? (i) east-west; (ii) north-south; (iii) up-down; (iv)
you get the same motional emf with all of these orientations. (b) How should you hold it
to get zero emf as you walk toward the east? (i) east-west; (ii) north-south; (iii) up-down;
(iv) none of these. (c) In which direction should you travel so that the motional emf
across the rod is zero no matter how the rod is oriented? (i) west; (ii) north; 
(iii) south; (iv) straight up; (v) straight down.
❙

If we neglect the small field outside the solenoid and take the area vector 
to
point in the same direction as 
then the magnetic flux 
through the loop is
When the solenoid current I changes with time, the magnetic flux 
also
changes, and according to Faraday’s law the induced emf in the loop is given by
(29.8)
If the total resistance of the loop is R, the induced current in the loop, which we
may call 
is 
But what force makes the charges move around the wire loop? It can’t be a
magnetic force because the loop isn’t even in a magnetic field. We are forced to
conclude that there has to be an induced electric field in the conductor caused by
the changing magnetic flux. This may be a little jarring; we are accustomed to
thinking about electric field as being caused by electric charges, and now we are
saying that a changing magnetic field somehow acts as a source of electric field.
Furthermore, it’s a strange sort of electric field. When a charge q goes once
around the loop, the total work done on it by the electric field must be equal to q
times the emf 
That is, the electric field in the loop is not conservative, as we
used the term in Chapter 23, because the line integral of 
around a closed path is
not zero. Indeed, this line integral, representing the work done by the induced 
field per unit charge, is equal to the induced emf 
(29.9)
From Faraday’s law the emf 
is also the negative of the rate of change of mag-
netic flux through the loop. Thus for this case we can restate Faraday’s law as
(29.10)
Note that Faraday’s law is always true in the form 
the form given
in Eq. (29.10) is valid only if the path around which we integrate is stationary.
As an example of a situation to which Eq. (29.10) can be applied, consider the
stationary circular loop in Fig. 29.17b, which we take to have radius r. Because
of cylindrical symmetry, the electric field 
has the same magnitude at every
point on the circle and is tangent to it at each point. (Symmetry would also permit
the field to be radial, but then Gauss’s law would require the presence of a net
charge inside the circle, and there is none.) The line integral in Eq. (29.10)
becomes simply the magnitude E times the circumference 
of the loop,
and Eq. (29.10) gives
(29.11)
The directions of 
at points on the loop are shown in Fig. 29.17b. We know that
has to have the direction shown when 
in the solenoid is increasing, because
has to be negative when 
is positive. The same approach can be
used to find the induced electric field inside the solenoid when the solenoid 
field is changing; we leave the details to you (see Exercise 29.35).
Nonelectrostatic Electric Fields
Now let’s summarize what we’ve learned. Faraday’s law, Eq. (29.3), is valid for
two rather different situations. In one, an emf is induced by magnetic forces on
charges when a conductor moves through a magnetic field. In the other, a 
B
S
d£B>dt
AE
S # dl
S
B
S
E
S
E
S
E =
1
2pr ` d£B
dt `
AE
S # dl
S = 2prE,
2pr
E
S
E = -d£B/dt;
C
E
S # dl
S = - d£B
dt   (stationary integration path)
E
C
E
S # dl
S = E
E:
E
S
E
S
E.
I¿ = E/R.
I¿,
E = - d£B
dt
= -m0nA dI
dt
£B
£B = BA = m0nIA
£B
B
S,
A
S
972
CHAPTER 29 Electromagnetic Induction
G
G
(a)
I, dI
dt
I'
I, dI
dt
B
Solenoid
Wire loop
Galvanometer
Blue cylinder shows region
with magnetic field B.
(b)
I
r
E
E
E
B
S
S
S
S
S
S
A
29.17 (a) The windings of a long sole-
noid carry a current I that is increasing at a
rate 
The magnetic flux in the sole-
noid is increasing at a rate 
and this
changing flux passes through a wire loop.
An emf 
is induced in the
loop, inducing a current 
that is measured
by the galvanometer G. (b) Cross-sectional
view.
I¿
E = -d£B/dt
d£B/dt,
dI/dt.

29.5 Induced Electric Fields
973
time-varying magnetic field induces an electric field in a stationary conductor
and hence induces an emf; in fact, the 
field is induced even when no conductor
is present. This 
field differs from an electrostatic field in an important way. It is
nonconservative; the line integral 
around a closed path is not zero, and
when a charge moves around a closed path, the field does a nonzero amount of
work on it. It follows that for such a field the concept of potential has no mean-
ing. We call such a field a nonelectrostatic field. In contrast, an electrostatic field
is always conservative, as we discussed in Section 23.1, and always has an asso-
ciated potential function. Despite this difference, the fundamental effect of any
electric field is to exert a force 
on a charge q. This relationship is valid
whether 
is a conservative field produced by a charge distribution or a noncon-
servative field caused by changing magnetic flux.
So a changing magnetic field acts as a source of electric field of a sort that we
cannot produce with any static charge distribution. This may seem strange, but
it’s the way nature behaves. What’s more, we’ll see in Section 29.7 that a chang-
ing electric field acts as a source of magnetic field. We’ll explore this symmetry
between the two fields in greater detail in our study of electromagnetic waves in
Chapter 32.
If any doubt remains in your mind about the reality of magnetically induced
electric fields, consider a few of the many practical applications (Fig. 29.18).
Pickups in electric guitars use currents induced in stationary pickup coils by the
vibration of nearby ferromagnetic strings. Alternators in most cars use rotating
magnets to induce currents in stationary coils. Whether we realize it or not, mag-
netically induced electric fields play an important role in everyday life.
E
S
F
S  qE
S
AE
S # dl
S
E
S
E
S
29.18 Applications of induced electric fields. (a) Data are stored on a computer hard disk in a pattern of magnetized areas on the sur-
face of the disk. To read these data, a coil on a movable arm is placed next to the spinning disk. The coil experiences a changing mag-
netic flux, inducing a current whose characteristics depend on the pattern coded on the disk. (b) This hybrid automobile has both a
gasoline engine and an electric motor. As the car comes to a halt, the spinning wheels run the motor backward so that it acts as a genera-
tor. The resulting induced current is used to recharge the car’s batteries. (c) The rotating crankshaft of a piston-engine airplane spins a
magnet, inducing an emf in an adjacent coil and generating the spark that ignites fuel in the engine cylinders. This keeps the engine run-
ning even if the airplane’s other electrical systems fail.
(a)
(b)
(c)
