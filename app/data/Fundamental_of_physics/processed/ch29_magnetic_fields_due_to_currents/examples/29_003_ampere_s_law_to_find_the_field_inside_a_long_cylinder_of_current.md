Sample Problem 29.03
Ampere’s law to find the field inside a long cylinder of current
A
Figure 29-16 (a)-(b) To find the magnetic field at a point within this conducting cylinder,we use a concentric Amperian
loop through the point.We then need the current encircled by the loop.(c)-(h) Because the current density is nonuni-
form,we start with a thin ring and then sum (via integration) the currents in all such rings in the encircled area.
Amperian
loop
r
a
r
b
We want the
magnetic field at
the dot at radius r.
We start with a ring
that is so thin that
we can approximate
the current density as
being uniform within it.
a
Our job is to sum
the currents in all
rings from this
smallest one ...
r
... to this largest
one, which has the
same radius as the
Amperian loop.
dr
Its area dA is the
product of the ring’s
circumference
and the width dr.
dA
The current within the
ring is the product of
the current density J
and the ring’s area dA.
So, we put a concentric
Amperian loop through
the dot.
We need to find the
current in the area
encircled by the loop.
(g)
(h)
(e)
( f )
(a)
(b)
(c)
(d)
Figure 29-16a shows the cross section of a long conducting
cylinder with inner radius a ! 2.0 cm and outer radius 
b ! 4.0 cm.The cylinder carries a current out of the page, and
the magnitude of the current density in the cross section is
given by J ! cr2, with c ! 3.0 $ 106 A/m4 and r in meters.
What is the magnetic field 
at the dot in Fig. 29-16a, which is
at radius r ! 3.0 cm from the central axis of the cylinder?
KEY IDEAS
The point at which we want to evaluate 
is inside the mate-
rial of the conducting cylinder, between its inner and outer
radii. We note that the current distribution has cylindrical
symmetry (it is the same all around the cross section for any
given radius).Thus, the symmetry allows us to use Ampere’s
law to find 
at the point. We first draw the Amperian loop
shown in Fig. 29-16b. The loop is concentric with the cylin-
der and has radius r ! 3.0 cm because we want to evaluate
at that distance from the cylinder’s central axis.
B
:
B
:
B
:
B
:
Next, we must compute the current ienc that is encircled
by the Amperian loop. However, we cannot set up a propor-
tionality as in Eq. 29-19, because here the current is not uni-
formly distributed. Instead, we must integrate the current
density magnitude from the cylinder’s inner radius a to the
loop radius r, using the steps shown in Figs. 29-16c through h.
Calculations: We write the integral as
Note that in these steps we took the differential area dA to
be the area of the thin ring in Figs. 29-16d-f and then
! pc(r 4 % a4)
2
.
! 2pc"
r
a
r 3 dr ! 2pc(
r 4
4 )
a
r
ienc !" J dA !"
r
a
cr2(2pr dr)

848
CHAPTER 29
MAGNETIC FIELDS DUE TO CURRENTS
29-4 SOLENOIDS AND TOROIDS
Learning Objectives
unit length n of the solenoid.
29.20 Explain how Ampere’s law is used to find the magnetic
field inside a toroid.
29.21 Apply the relationship between a toroid’s internal mag-
netic field B, the current i, the radius r, and the total num-
ber of turns N.
After reading this module, you should be able to . . . 
29.17 Describe a solenoid and a toroid and sketch their
magnetic field lines.
29.18 Explain how Ampere’s law is used to find the magnetic
field inside a solenoid.
29.19 Apply the relationship between a solenoid’s internal
magnetic field B, the current i, and the number of turns per
Additional examples, video, and practice available at WileyPLUS
replaced it with its equivalent, the product of the ring’s cir-
cumference 2pr and its thickness dr.
For the Amperian loop, the direction of integration indi-
cated in Fig. 29-16b is (arbitrarily) clockwise. Applying the
right-hand rule for Ampere’s law to that loop, we find that we
should take ienc as negative because the current is directed out
of the page but our thumb is directed into the page.
We next evaluate the left side of Ampere’s law 
as we did in Fig. 29-15, and we again obtain Eq. 29-18. Then
Ampere’s law,
gives us
B(2pr) ! % m 0pc
2
 (r 4 % a 4).
, B
: !ds
: ! m 0ienc,
Solving for B and substituting known data yield
Thus, the magnetic field 
at a point 3.0 cm from the central
axis has magnitude
B ! 2.0 $ 10%5 T
(Answer)
and forms magnetic field lines that are directed opposite our
direction of integration, hence counterclockwise in Fig. 29-16b.
B
:
! %2.0 $ 10%5 T.
$ [(0.030 m)4 % (0.020 m)4]
! % (4p $ 10 %7 T)m/A)(3.0 $ 10 6 A/m4)
4(0.030 m)
B ! % m0c
4r  (r4 % a4)
●Inside a long solenoid carrying current i, at points not near
its ends, the magnitude B of the magnetic field is
B ! m0in
(ideal solenoid),
where n is the number of turns per unit length.
●At a point inside a toroid, the magnitude B of the magnetic
field is
(toroid),
where r is the distance from the center of the toroid to the point.
B ! m 0iN
2p
1
r
Key Ideas
Solenoids and Toroids
Magnetic Field of a Solenoid
We now turn our attention to another situation in which Ampere’s law proves
useful. It concerns the magnetic field produced by the current in a long, tightly
wound helical coil of wire. Such a coil is called a solenoid (Fig. 29-17).We assume
that the length of the solenoid is much greater than the diameter.
Figure 29-18 shows a section through a portion of a “stretched-out” sole-
noid. The solenoid’s magnetic field is the vector sum of the fields produced by
the individual turns (windings) that make up the solenoid. For points very
Figure 29-17 A solenoid carrying current i.
i
i

849
29-4 SOLENOIDS AND TOROIDS
close to a turn, the wire behaves magnetically almost like a long straight wire,
and the lines of 
there are almost concentric circles. Figure 29-18 suggests
that the field tends to cancel between adjacent turns. It also suggests that, at
points inside the solenoid and reasonably far from the wire,
is approxi-
mately parallel to the (central) solenoid axis. In the limiting case of an ideal
solenoid, which is infinitely long and consists of tightly packed (close-packed)
turns of square wire, the field inside the coil is uniform and parallel to the so-
lenoid axis.
At points above the solenoid, such as P in Fig. 29-18, the magnetic field set
up by the upper parts of the solenoid turns (these upper turns are marked $)
is directed to the left (as drawn near P) and tends to cancel the field set up at P
by the lower parts of the turns (these lower turns are marked #), which is di-
rected to the right (not drawn). In the limiting case of an ideal solenoid, the
magnetic field outside the solenoid is zero. Taking the external field to be zero
is an excellent assumption for a real solenoid if its length is much greater than
its diameter and if we consider external points such as point P that are not at
either end of the solenoid. The direction of the magnetic field along the sole-
noid axis is given by a curled-straight right-hand rule: Grasp the solenoid with
your right hand so that your fingers follow the direction of the current in the
windings; your extended right thumb then points in the direction of the axial
magnetic field.
Figure 29-19 shows the lines of 
for a real solenoid. The spacing of these
lines in the central region shows that the field inside the coil is fairly strong
and uniform over the cross section of the coil. The external field, however, is
relatively weak.
Ampere’s Law. Let us now apply Ampere’s law,
(29-21)
to the ideal solenoid of Fig. 29-20, where 
is uniform within the solenoid and
zero outside it, using the rectangular Amperian loop abcda. We write 
as
the sum of four integrals, one for each loop segment:
(29-22)
&"
d
c
B
:!ds
: &"
a
d
B
:!ds
:.
, B
: !ds
: !"
b
a
B
: !ds
: &"
c
b
B
: !ds
:
- B
: !ds
:
B
:
, B
: !ds
: ! m 0ienc,
B
:
B
:
B
:
Figure 29-18 A vertical cross section through the central axis of a “stretched-out” solenoid.
The back portions of five turns are shown, as are the magnetic field lines due to a current
through the solenoid. Each turn produces circular magnetic field lines near itself. Near the
solenoid’s axis, the field lines combine into a net magnetic field that is directed along the
axis.The closely spaced field lines there indicate a strong magnetic field. Outside the sole-
noid the field lines are widely spaced; the field there is very weak.
P
Figure 29-19 Magnetic field lines for a real
solenoid of finite length.The field is strong
and uniform at interior points such as P1
but relatively weak at external points such
as P2.
P2
P1
Figure 29-20 Application of Ampere’s law to
a section of a long ideal solenoid carrying
a current i.The Amperian loop is the rec-
tangle abcda.
a
b
d
c
h
i
B

850
CHAPTER 29
MAGNETIC FIELDS DUE TO CURRENTS
i
(a)
Amperian loop 
r
i
(b)
B
Figure 29-21 (a) A toroid carrying a current i.
(b) A horizontal cross section of the toroid.
The interior magnetic field (inside the
bracelet-shaped tube) can be found by ap-
plying Ampere’s law with the Amperian
loop shown.
The first integral on the right of Eq. 29-22 is Bh, where B is the magnitude of
the uniform field 
inside the solenoid and h is the (arbitrary) length of the
segment from a to b. The second and fourth integrals are zero because for every
element ds of these segments,
either is perpendicular to ds or is zero, and thus
the product 
is zero.The third integral, which is taken along a segment that
lies outside the solenoid, is zero because B
0 at all external points. Thus,
for the entire rectangular loop has the value Bh.
Net Current. The net current ienc encircled by the rectangular Amperian
loop in Fig. 29-20 is not the same as the current i in the solenoid windings because
the windings pass more than once through this loop. Let n be the number of turns
per unit length of the solenoid; then the loop encloses nh turns and
ienc ! i(nh).
Ampere’s law then gives us
Bh ! m0inh
or
B ! m0in
(ideal solenoid).
(29-23)
Although we derived Eq. 29-23 for an infinitely long ideal solenoid, it
holds quite well for actual solenoids if we apply it only at interior points and
well away from the solenoid ends. Equation 29-23 is consistent with the ex-
perimental fact that the magnetic field magnitude B within a solenoid does
not depend on the diameter or the length of the solenoid and that B is uni-
form over the solenoidal cross section. A solenoid thus provides a practical
way to set up a known uniform magnetic field for experimentation, just as a
parallel-plate capacitor provides a practical way to set up a known uniform
electric field.
Magnetic Field of a Toroid
Figure 29-21a shows a toroid, which we may describe as a (hollow) solenoid that
has been curved until its two ends meet, forming a sort of hollow bracelet. What
magnetic field 
is set up inside the toroid (inside the hollow of the bracelet)? We
can find out from Ampere’s law and the symmetry of the bracelet.
From the symmetry, we see that the lines of 
form concentric circles inside
the toroid, directed as shown in Fig. 29-21b. Let us choose a concentric circle of
radius r as an Amperian loop and traverse it in the clockwise direction.Ampere’s
law (Eq. 29-14) yields
(B)(2pr) ! m0iN,
where i is the current in the toroid windings (and is positive for those windings
enclosed by the Amperian loop) and N is the total number of turns.This gives
(toroid).
(29-24)
In contrast to the situation for a solenoid, B is not constant over the cross section
of a toroid.
It is easy to show, with Ampere’s law, that B ! 0 for points outside an ideal
toroid (as if the toroid were made from an ideal solenoid). The direction of the
magnetic field within a toroid follows from our curled-straight right-hand rule:
Grasp the toroid with the fingers of your right hand curled in the direction of
the current in the windings; your extended right thumb points in the direction
of the magnetic field.
B ! m 0iN
2p
1
r
B
:
B
:
- B
:!ds
:
!
B
: !ds
:
B
:
B
:

851
29-5 A CURRENT-CARRYING COIL AS A MAGNETIC DIPOLE 
Calculation: Because B does not depend on the diameter of
the windings, the value of n for five identical layers is simply
five times the value for each layer.Equation 29-23 then tells us
(Answer)
To a good approximation, this is the field magnitude through-
out most of the solenoid.
! 2.42 $ 10 %2 T ! 24.2 mT.
B ! m0in ! (4p $ 10 %7 T)m/A)(5.57 A) 5 $ 850 turns
1.23 m
