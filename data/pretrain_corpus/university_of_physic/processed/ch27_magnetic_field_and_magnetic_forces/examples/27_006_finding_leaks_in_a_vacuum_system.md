Example 27.6
Finding leaks in a vacuum system
There is almost no helium in ordinary air, so helium sprayed near a
leak in a vacuum system will quickly show up in the output of a
vacuum pump connected to such a system. You are designing a leak
detector that uses a mass spectrometer to detect 
ions (charge
mass 
The ions
emerge from the velocity selector with a speed of 
They are curved in a semicircular path by a magnetic field 
and
are detected at a distance of 10.16 cm from the slit 
in Fig. 27.24.
Calculate the magnitude of the magnetic field 
SOLUTION
IDENTIFY and SET UP: After it passes through the slit, the ion fol-
lows a circular path as described in Section 27.4 (see Fig. 27.17).
We solve Eq. (27.11) for 
.
B¿
B¿.
S3
B¿
1.00 * 105 m>s.
6.65 * 10-27 kg2.
+e = +1.60 * 10-19 C,
He+
EXECUTE: The distance given is the diameter of the semicircular
path shown in Fig. 27.24, so the radius is 
From Eq. (27.11), 
we get
EVALUATE: Helium leak detectors are widely used with high-
vacuum systems. Our result shows that only a small magnetic field
is required, so leak detectors can be relatively compact.
= 0.0818 T
B¿ = mv
qR =
16.65 * 10-27 kg211.00 * 105 m>s2
11.60 * 10-19 C215.08 * 10-2 m2
R = mv>qB¿,
10-2 m2.
R = 1
2 110.16 *
Test Your Understanding of Section 27.5
In Example 27.6 
ions with
charge 
move at 
in a straight line through a velocity selector. Suppose
the 
ions were replaced with 
ions, in which both electrons have been removed
from the helium atom and the ion charge is 
At what speed must the 
ions travel
through the same velocity selector in order to move in a straight line? (i) about 
(ii) about 
(iii) 
(iv) about 
(v) about 
❙
0.25 * 105 m/s.
0.50 * 105 m/s;
1.00 * 105 m/s;
2.00 * 105 m/s;
105 m/s;
4.00 *
He2+
+2e.
He2+
He+
1.00 * 105 m/s
+e
He+
q
l
A
Drift velocity
of charge
carriers
B
S
vd
S
F
S
J
S
J
S
27.25 Forces on a moving positive
charge in a current-carrying conductor.
ActivPhysics 13.7: Mass Spectrometer

27.6 Magnetic Force on a Current-Carrying Conductor
899
segment of a conducting wire, with length and cross-sectional area 
the current
is from bottom to top. The wire is in a uniform magnetic field 
perpendicular to
the plane of the diagram and directed into the plane. Let’s assume first that the mov-
ing charges are positive. Later we’ll see what happens when they are negative.
The drift velocity 
is upward, perpendicular to 
The average force on each
charge is 
directed to the left as shown in the figure; since 
and
are perpendicular, the magnitude of the force is 
We can derive an expression for the total force on all the moving charges in a
length l of conductor with cross-sectional area A using the same language we
used in Eqs. (25.2) and (25.3) of Section 25.1. The number of charges per unit
volume is ; a segment of conductor with length has volume 
and contains a
number of charges equal to 
The total force 
on all the moving charges in
this segment has magnitude
(27.16)
From Eq. (25.3) the current density is 
The product 
is the total cur-
rent 
so we can rewrite Eq. (27.16) as
(27.17)
If the 
field is not perpendicular to the wire but makes an angle 
with it, we
handle the situation the same way we did in Section 27.2 for a single charge.
Only the component of 
perpendicular to the wire (and to the drift velocities of
the charges) exerts a force; this component is 
The magnetic force
on the wire segment is then
(27.18)
The force is always perpendicular to both the conductor and the field, with the
direction determined by the same right-hand rule we used for a moving positive
charge (Fig. 27.26). Hence this force can be expressed as a vector product, just like
the force on a single moving charge. We represent the segment of wire with a vector
along the wire in the direction of the current; then the force 
on this segment is
(magnetic force on a straight wire segment)
(27.19)
Figure 27.27 illustrates the directions of 
and 
for several cases.
If the conductor is not straight, we can divide it into infinitesimal segments
The force 
on each segment is
(magnetic force on an infinitesimal wire section)
(27.20)
Then we can integrate this expression along the wire to find the total force on a con-
ductor of any shape. The integral is a line integral, the same mathematical operation
we have used to define work (Section 6.3) and electric potential (Section 23.2).
CAUTION
Current is not a vector Recall from Section 25.1 that the current is not a
vector. The direction of current flow is described by 
not 
If the conductor is curved,
the current is the same at all points along its length, but 
changes direction so that it is
always tangent to the conductor. ❙
Finally, what happens when the moving charges are negative, such as elec-
trons in a metal? Then in Fig. 27.25 an upward current corresponds to a down-
ward drift velocity. But because is now negative, the direction of the force 
is
the same as before. Thus Eqs. (27.17) through (27.20) are valid for both positive
and negative charges and even when both signs of charge are present at once.
This happens in some semiconductor materials and in ionic solutions.
A common application of the magnetic forces on a current-carrying wire is found
in loudspeakers (Fig. 27.28). The radial magnetic field created by the permanent
F
S
q
dl
S
I
I.
dl
S,
I
dF
S  I dl
S : B
S
dF
S
dl
S.
F
S
l
S,
B
S,
F
S  Il
S : B
S
F
S
l
S
F = IlB = IlBsinf
B = Bsinf.
B
S
f
B
S
F = IlB
I,
JA
J = nqvd.
F = 1nAl21qvdB2 = 1nqvdA21lB2
F
S
nAl.
Al
l
n
F = qvdB.
B
S
v
S
d
F
S  qv
S
d : B
S,
B
S.
v
S
d
B
S,
A;
l
Force F on a straight wire carrying a positive
current and oriented at an angle f to a
magnetic field B:
• Magnitude is F 5 IlB 5 IlB sin f.
• Direction of F is given by the right-hand rule.
I
Bi
f
B' 5 B sin f
B
S
S
l
F
S
S
S
S
27.26 A straight wire segment of
length 
carries a current I in the 
direction of 
The magnetic force on this
segment is perpendicular to both 
and
the magnetic field B
S.
l
S
l
S.
l
S
y
x
z
I
(a)
B
S
S
S
Sl
F
S
f
y
x
z
I
(b)
l
B
S
S
F
S
f
y
x
z
I
(c)
l
B
S
F
S
Reversing B reverses
the force direction.
Reversing the current [relative to (b)]
reverses the force
direction.
f
27.27 Magnetic field 
length 
and
force 
vectors for a straight wire carrying
a current I.
F
S
l
S,
B
S,

magnet exerts a force on the voice coil that is proportional to the current in the
coil; the direction of the force is either to the left or to the right, depending on the
direction of the current. The signal from the amplifier causes the current to oscil-
late in direction and magnitude. The coil and the speaker cone to which it is
attached respond by oscillating with an amplitude proportional to the amplitude
of the current in the coil. Turning up the volume knob on the amplifier increases
the current amplitude and hence the amplitudes of the cone’s oscillation and of
the sound wave produced by the moving cone.
900
CHAPTER 27 Magnetic Field and Magnetic Forces
B field of
permanent
magnet
S
(b)
I
Direction
of motion
of voice coil
and speaker
cone
Current in
voice coil
(a)
Magnets
Basket
Signal
from
amplifier
Flexible
suspension
ring
Voice
coil
Rigid
speaker
cone
27.28 (a) Components of a loudspeaker. (b) The permanent magnet creates a magnetic field that exerts forces on the current in the
voice coil; for a current I in the direction shown, the force is to the right. If the electric current in the voice coil oscillates, the speaker
cone attached to the voice coil oscillates at the same frequency.
