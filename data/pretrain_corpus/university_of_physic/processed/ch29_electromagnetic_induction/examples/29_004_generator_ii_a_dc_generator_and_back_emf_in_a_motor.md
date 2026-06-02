Example 29.4
Generator II: A DC generator and back emf in a motor
The alternator in Example 29.3 produces a sinusoidally varying
emf and hence an alternating current. Figure 29.10a shows a
direct-current (dc) generator that produces an emf that always has
the same sign. The arrangement of split rings, called a commutator,
reverses the connections to the external circuit at angular positions
at which the emf reverses. Figure 29.10b shows the resulting emf.
Commercial dc generators have a large number of coils and com-
mutator segments, smoothing out the bumps in the emf so that the
terminal voltage is not only one-directional but also practically
constant. This brush-and-commutator arrangement is the same as
that in the direct-current motor discussed in Section 27.8. The
motor’s back emf is just the emf induced by the changing magnetic
flux through its rotating coil. Consider a motor with a square, 500-
turn coil 10.0 cm on a side. If the magnetic field has magnitude
0.200 T, at what rotation speed is the average back emf of the
motor equal to 112 V?
SOLUTION
IDENTIFY and SET UP: As far as the rotating loop is concerned, the
situation is the same as in Example 29.3 except that we now have
N turns of wire. Without the commutator, the emf would alternate

29.2 Faraday’s Law
965
t
(a)
(b)
Loop (seen
end-on)
S
S
B
S
Brush
Brush
Commutator
b
a
f
v
A
B
E
E, FB
FB
E
29.10 (a) Schematic diagram of a dc generator, using a split-ring commutator. The ring halves are attached to the loop and
rotate with it. (b) Graph of the resulting induced emf between terminals a and b. Compare to Fig. 29.8b.
between positive and negative values and have an average value of
zero (see Fig. 29.8b). With the commutator, the emf is never nega-
tive and its average value is positive (Fig. 29.10b). We’ll use our
result from Example 29.3 to obtain an expression for this average
value and solve it for the rotational speed .
EXECUTE: Comparison of Figs. 29.8b and 29.10b shows that the
back emf of the motor is just N times the absolute value of the emf
found for an alternator in Example 29.3, as in Eq. (29.4):
. To find the average back emf, we must
replace 
by its average value. We find this by integrating
over half a cycle, from 
to 
and
dividing by the elapsed time 
During this half cycle, the sine
function is positive, so 
and we find
The average back emf is then
1ƒ sinvtƒ2av = 1
p>v
0
sinvt dt
p>v
= 2
p
ƒsinvtƒ = sinvt,
p>v.
t = T>2 = p>v,
t = 0
ƒsinvtƒ
ƒsinvtƒ
ƒEƒ = NvBAƒsinvtƒ
v
This confirms that the back emf is proportional to the rotation
speed 
as we stated without proof in Section 27.8. Solving for 
we obtain
(We used the unit relationships 
from
Example 29.1.)
EVALUATE: The average back emf is directly proportional to 
Hence the slower the rotation speed, the less the back emf and the
greater the possibility of burning out the motor, as we described in
Example 27.11 (Section 27.8).
v.
1 V = 1 Wb>s = 1 T # m2>s
=
p1112 V2
21500210.200 T210.100 m22 = 176 rad>s
v = pEav
2NBA
v,
v,
Eav = 2NvBA
p
