Sample Problem 30.03
Induced emf due to a changing nonuniform B field
Figure 30-7 shows a rectangular loop of wire immersed in a
nonuniform and varying magnetic field 
that is perpendi-
cular to and directed into the page. The field’s magnitude is
given by B ! 4t2x2, with B in teslas, t in seconds, and x in
meters. (Note that the function depends on both time and
position.) The loop has width W ! 3.0 m and height H !
2.0 m.What are the magnitude and direction of the induced
emf # around the loop at t ! 0.10 s?
B
:

871
30-2 INDUCTION AND ENERGY TRANSFERS
dA to be the area of a vertical strip of height H and width dx
(as shown in Fig. 30-7). Then dA ! H dx, and the flux
through the loop is
Treating t as a constant for this integration and inserting the
integration limits x ! 0 and x ! 3.0 m, we obtain
where we have substituted H ! 2.0 m and 0B is in webers.
Now we can use Faraday’s law to find the magnitude of # at
any time t:
in which # is in volts.At t ! 0.10 s,
# ! (144 V/s)(0.10 s) % 14 V.
(Answer)
The flux of 
through the loop is into the page in
Fig. 30-7 and is increasing in magnitude because B is in-
creasing in magnitude with time. By Lenz’s law, the field Bind
of the induced current opposes this increase and so is di-
rected out of the page. The curled-straight right-hand rule
in Fig. 30-5a then tells us that the induced current is counter-
clockwise around the loop, and thus so is the induced emf #.
B
:
# ! d0B
dt
! d(72t2)
dt
! 144t,
0B ! 4t2H "
3.0
0
x2 dx ! 4t2H(
x3
3 )
0
3.0
! 72t2,
0B !" B
: !dA
: !" B dA !" BH dx !" 4t2x2H dx.
any time t. However, because B is not uniform over the
area enclosed by the loop, we cannot use Eq. 30-2 (0B !
BA) to find that expression; instead we must use Eq. 30-1
.
Calculations: In Fig. 30-7,
is perpendicular to the plane
of the loop (and hence parallel to the differential area 
vector 
); so the dot product in Eq. 30-1 gives B dA.
Because the magnetic field varies with the coordinate x but
not with the coordinate y, we can take the differential area
dA
:
B
:
(0B ! " B
:!dA
:)
Additional examples, video, and practice available at WileyPLUS
Figure 30-7 A closed conducting loop, of width W and height H, lies
in a nonuniform, varying magnetic field that points directly into the
page. To apply Faraday’s law, we use the vertical strip of height H,
width dx, and area dA.
W
H
y
x
dx
dA
B
If the field varies with position,
we must integrate to get the
flux through the loop.
We start with a strip
so thin that we can
approximate the field as
being uniform within it.
30-2 INDUCTION AND ENERGY TRANSFERS
After reading this module, you should be able to . . .
30.13 For a conducting loop pulled into or out of a magnetic
field, calculate the rate at which energy is transferred to
thermal energy.
30.14 Apply the relationship between an induced current and
the rate at which it produces thermal energy.
30.15 Describe eddy currents.
Learning Objectives
●The induction of a current by a changing flux means that energy is being transferred to that current. The energy can then be
transferred to other forms, such as thermal energy.
Key Idea
Induction and Energy Transfers
By Lenz’s law, whether you move the magnet toward or away from the loop in
Fig. 30-1, a magnetic force resists the motion, requiring your applied force to do
positive work. At the same time, thermal energy is produced in the material of
the loop because of the material’s electrical resistance to the current that is
induced by the motion.The energy you transfer to the closed loop & magnet sys-
tem via your applied force ends up in this thermal energy. (For now, we neglect
energy that is radiated away from the loop as electromagnetic waves during the

induction.) The faster you move the magnet, the more rapidly your applied force
does work and the greater the rate at which your energy is transferred to thermal
energy in the loop; that is, the power of the transfer is greater.
Regardless of how current is induced in a loop, energy is always transferred
to thermal energy during the process because of the electrical resistance of the
loop (unless the loop is superconducting). For example, in Fig. 30-2, when switch S
is closed and a current is briefly induced in the left-hand loop, energy is trans-
ferred from the battery to thermal energy in that loop.
Figure 30-8 shows another situation involving induced current.A rectangular
loop of wire of width L has one end in a uniform external magnetic field that is
directed perpendicularly into the plane of the loop. This field may be produced,
for example, by a large electromagnet. The dashed lines in Fig. 30-8 show the
assumed limits of the magnetic field; the fringing of the field at its edges is
neglected.You are to pull this loop to the right at a constant velocity .
Flux Change. The situation of Fig. 30-8 does not differ in any essential way
from that of Fig. 30-1. In each case a magnetic field and a conducting loop are in
relative motion; in each case the flux of the field through the loop is changing
with time. It is true that in Fig. 30-1 the flux is changing because 
is changing and
in Fig. 30-8 the flux is changing because the area of the loop still in the magnetic
field is changing, but that difference is not important. The important difference
between the two arrangements is that the arrangement of Fig. 30-8 makes calcu-
lations easier. Let us now calculate the rate at which you do mechanical work as
you pull steadily on the loop in Fig. 30-8.
Rate of Work. As you will see, to pull the loop at a constant velocity , you
must apply a constant force 
to the loop because a magnetic force of equal mag-
nitude but opposite direction acts on the loop to oppose you. From Eq. 7-48, the
rate at which you do work-that is, the power-is then
P ! Fv,
(30-6)
where F is the magnitude of your force. We wish to find an expression for P in
terms of the magnitude B of the magnetic field and the characteristics of the
loop-namely, its resistance R to current and its dimension L.
As you move the loop to the right in Fig. 30-8, the portion of its area within
the magnetic field decreases. Thus, the flux through the loop also decreases and,
according to Faraday’s law, a current is produced in the loop. It is the presence of
this current that causes the force that opposes your pull.
Induced emf. To find the current, we first apply Faraday’s law.When x is the
length of the loop still in the magnetic field, the area of the loop still in the field is
Lx.Then from Eq. 30-2, the magnitude of the flux through the loop is
0B ! BA ! BLx.
(30-7)
F
:
v:
B
:
v:
872
CHAPTER 30
INDUCTION AND INDUCTANCE
Figure 30-8 You pull a closed conduct-
ing loop out of a magnetic field at
constant velocity
. While the loop
is moving,a clockwise current i is
induced in the loop,and the loop seg-
ments still within the magnetic field
experience forces 
,
, and 
.
F
:
3
F
:
2
F
:
1
v
:
i
x
b
L
F1
F2
F3
B
v
Decreasing the area
decreases the flux,
inducing a current.

873
30-2 INDUCTION AND ENERGY TRANSFERS
As x decreases, the flux decreases. Faraday’s law tells us that with this flux
decrease, an emf is induced in the loop. Dropping the minus sign in Eq. 30-4 and
using Eq. 30-7, we can write the magnitude of this emf as
(30-8)
in which we have replaced dx/dt with v, the speed at which the loop moves.
Figure 30-9 shows the loop as a circuit: induced emf # is represented on the
left, and the collective resistance R of the loop is represented on the right.
The direction of the induced current i is obtained with a right-hand rule as in
Fig. 30-5b for decreasing flux; applying the rule tells us that the current must be
clockwise, and # must have the same direction.
Induced Current. To find the magnitude of the induced current, we cannot
apply the loop rule for potential differences in a circuit because, as you will see in
Module 30-3, we cannot define a potential difference for an induced emf.
However, we can apply the equation i ! #/R.With Eq. 30-8, this becomes
(30-9)
Because three segments of the loop in Fig. 30-8 carry this current through the
magnetic field, sideways deflecting forces act on those segments. From Eq. 28-26
we know that such a deflecting force is, in general notation,
(30-10)
In Fig. 30-8, the deflecting forces acting on the three segments of the loop are
marked 
and 
. Note, however, that from the symmetry, forces 
and 
are equal in magnitude and cancel. This leaves only force 
, which is directed
opposite your force 
on the loop and thus is the force opposing you.So,
.
Using Eq. 30-10 to obtain the magnitude of 
and noting that the angle
between 
and the length vector 
for the left segment is 90 , we write
F ! F1 ! iLB sin 90" ! iLB.
(30-11)
Substituting Eq. 30-9 for i in Eq. 30-11 then gives us
(30-12)
Because B, L, and R are constants, the speed v at which you move the loop is con-
stant if the magnitude F of the force you apply to the loop is also constant.
Rate of Work. By substituting Eq. 30-12 into Eq. 30-6, we find the rate at
which you do work on the loop as you pull it from the magnetic field:
(rate of doing work).
(30-13)
Thermal Energy. To complete our analysis, let us find the rate at which
thermal energy appears in the loop as you pull it along at constant speed. We
calculate it from Eq. 26-27,
P ! i 2R.
(30-14)
Substituting for i from Eq. 30-9, we find
(thermal energy rate),
(30-15)
which is exactly equal to the rate at which you are doing work on the loop
(Eq. 30-13). Thus, the work that you do in pulling the loop through the magnetic
field appears as thermal energy in the loop.
P !#
BLv
R $
2
R ! B2L2v2
R
P ! Fv ! B2L2v2
R
F ! B2L2v
R
.
"
L
:
B
:
F
:
1
F
: ! %F
:
1
F
:
F
:
1
F
:
3
F
:
2
F
:
3
F
:
2,
F
:
1,
F
:
d ! iL
: $ B
:.
i ! BLv
R
.
# ! d0B
dt
! d
dt BLx ! BL dx
dt ! BLv,
Figure 30-9 A circuit diagram for the loop of
Fig. 30-8 while the loop is moving.
i
i
R

Eddy Currents
Suppose we replace the conducting loop of Fig. 30-8 with a solid conducting
plate. If we then move the plate out of the magnetic field as we did the loop 
(Fig. 30-10a), the relative motion of the field and the conductor again induces a
current in the conductor.Thus, we again encounter an opposing force and must
do work because of the induced current. With the plate, however, the conduc-
tion electrons making up the induced current do not follow one path as they
do with the loop. Instead, the electrons swirl about within the plate as if they
were caught in an eddy (whirlpool) of water. Such a current is called an eddy
current and can be represented, as it is in Fig. 30-10a, as if it followed a single
path.
As with the conducting loop of Fig. 30-8, the current induced in the plate
results in mechanical energy being dissipated as thermal energy. The dissipa-
tion is more apparent in the arrangement of Fig. 30-10b; a conducting plate,
free to rotate about a pivot, is allowed to swing down through a magnetic field
like a pendulum. Each time the plate enters and leaves the field, a portion
of its mechanical energy is transferred to its thermal energy. After several
swings, no mechanical energy remains and the warmed-up plate just hangs
from its pivot.
874
CHAPTER 30
INDUCTION AND INDUCTANCE
Figure 30-10 (a) As you pull a solid conduct-
ing plate out of a magnetic field, eddy cur-
rents are induced in the plate.A typical
loop of eddy current is shown. (b) A con-
ducting plate is allowed to swing like a pen-
dulum about a pivot and into a region of
magnetic field.As it enters and leaves the
field, eddy currents are induced in the
plate.
Checkpoint 3
The figure shows four wire loops, with edge lengths of either L or 2L.All four loops
will move through a region of uniform magnetic field 
(directed out of the page) at
the same constant velocity. Rank the four loops according to the maximum magni-
tude of the emf induced as they move through the field, greatest first.
B
:
a 
b 
c 
d 
B
Eddy
current
loop
(a)
B
Pivot
(b)
B
30-3 INDUCED ELECTRIC FIELDS
After reading this module, you should be able to . . .
30.16 Identify that a changing magnetic field induces an elec-
tric field, regardless of whether there is a conducting loop.
30.17 Apply Faraday’s law to relate the electric field 
induced along a closed path (whether it has conducting
E
:
material or not) to the rate of change d0/dt of the magnetic
flux encircled by the path.
30.18 Identify that an electric potential cannot be associated
with an induced electric field.
Learning Objectives
●An emf is induced by a changing magnetic flux even if the
loop through which the flux is changing is not a physical
conductor but an imaginary line. The changing magnetic field
induces an electric field 
at every point of such a loop; the
induced emf is related to 
by
# !, E
:!ds
:.
E
:
E
:
Key Ideas
●Using the induced electric field, we can write Faraday’s law
in its most general form as
(Faraday’s law).
A changing magnetic field induces an electric field
.
E
:
, E
:!ds
:! % d0B
dt

875
30-3 INDUCED ELECTRIC FIELDS
Induced Electric Fields
Let us place a copper ring of radius r in a uniform external magnetic field, as in
Fig. 30-11a. The field-neglecting fringing-fills a cylindrical volume of radius R.
Suppose that we increase the strength of this field at a steady rate, perhaps by
increasing-in an appropriate way-the current in the windings of the electro-
magnet that produces the field. The magnetic flux through the ring will then
change at a steady rate and-by Faraday’s law-an induced emf and thus an
induced current will appear in the ring. From Lenz’s law we can deduce that the
direction of the induced current is counterclockwise in Fig. 30-11a.
If there is a current in the copper ring,an electric field must be present along the
ring because an electric field is needed to do the work of moving the conduction
electrons. Moreover, the electric field must have been produced by the changing
magnetic flux. This induced electric field
is just as real as an electric field pro-
duced by static charges; either field will exert a force 
on a particle of charge q0.
By this line of reasoning, we are led to a useful and informative restatement
of Faraday’s law of induction:
q0E
:
E
:
The striking feature of this statement is that the electric field is induced even if
there is no copper ring.Thus, the electric field would appear even if the changing
magnetic field were in a vacuum.
To fix these ideas, consider Fig. 30-11b, which is just like Fig. 30-11a except
the copper ring has been replaced by a hypothetical circular path of radius r. We
assume, as previously, that the magnetic field 
is increasing in magnitude at
a constant rate dB/dt. The electric field induced at various points around the
B
:
A changing magnetic field produces an electric field.
Figure 30-11 (a) If the magnetic field increases at a steady rate, a constant induced current
appears, as shown, in the copper ring of radius r. (b) An induced electric field exists even
when the ring is removed; the electric field is shown at four points. (c) The complete
picture of the induced electric field, displayed as field lines.(d) Four similar closed paths that
enclose identical areas.Equal emfs are induced around paths 1 and 2,which lie entirely within
the region of changing magnetic field.A smaller emf is induced around path 3,which only
partially lies in that region.No net emf is induced around path 4,which lies entirely outside
the magnetic field.
R
Copper
ring
r
i
(a)
Circular
path
(b)
(c)
(d)
Electric field
lines
R
r
1
3
4
R
R
2
B
B
E
E
E
E
B
B

circular path must-from the symmetry-be tangent to the circle, as Fig. 30-11b
shows.* Hence, the circular path is an electric field line. There is nothing special
about the circle of radius r, so the electric field lines produced by the changing
magnetic field must be a set of concentric circles, as in Fig. 30-11c.
As long as the magnetic field is increasing with time, the electric field repre-
sented by the circular field lines in Fig. 30-11c will be present. If the magnetic
field remains constant with time, there will be no induced electric field and thus
no electric field lines. If the magnetic field is decreasing with time (at a constant
rate), the electric field lines will still be concentric circles as in Fig. 30-11c, but
they will now have the opposite direction. All this is what we have in mind when
we say “A changing magnetic field produces an electric field.”
A Reformulation of Faraday’s Law
Consider a particle of charge q0 moving around the circular path of Fig. 30-11b.
The work W done on it in one revolution by the induced electric field is W ! #q0,
where # is the induced emf-that is, the work done per unit charge in moving the
test charge around the path. From another point of view, the work is
(30-16)
where q0E is the magnitude of the force acting on the test charge and 2pr is the
distance over which that force acts. Setting these two expressions for W equal to
each other and canceling q0, we find that
# ! 2prE.
(30-17)
Next we rewrite Eq. 30-16 to give a more general expression for the work
done on a particle of charge q0 moving along any closed path:
(30-18)
(The loop on each integral sign indicates that the integral is to be taken around
the closed path.) Substituting #q0 for W, we find that
(30-19)
This integral reduces at once to Eq. 30-17 if we evaluate it for the special case of
Fig. 30-11b.
Meaning of emf. With Eq. 30-19, we can expand the meaning of induced emf.
Up to this point, induced emf has meant the work per unit charge done in maintain-
ing current due to a changing magnetic flux, or it has meant the work done per unit
charge on a charged particle that moves around a closed path in a changing mag-
netic flux.However,with Fig.30-11b and Eq.30-19,an induced emf can exist without
the need of a current or particle: An induced emf is the sum-via integration-of
quantities 
around a closed path, where 
is the electric field induced by
a changing magnetic flux and 
is a differential length vector along the path.
ds
:
E
:
E
:!ds
:
# !, E
:!ds
:.
W !, F
:!ds
: ! q0, E
:!ds
:.
W !" F
:!ds
: ! (q0E)(2pr),
876
CHAPTER 30
INDUCTION AND INDUCTANCE
*Arguments of symmetry would also permit the lines of 
around the circular path to be radial,
rather than tangential. However, such radial lines would imply that there are free charges, distributed
symmetrically about the axis of symmetry, on which the electric field lines could begin or end; there
are no such charges.
E
:
If we combine Eq. 30-19 with Faraday’s law in Eq. 30-4 (# ! %d0B/dt), we 
can rewrite Faraday’s law as
(Faraday’s law).
(30-20)
, E
:!ds
: !% d0B
dt

877
30-3 INDUCED ELECTRIC FIELDS
This equation says simply that a changing magnetic field induces an electric field.
The changing magnetic field appears on the right side of this equation, the elec-
tric field on the left.
Faraday’s law in the form of Eq. 30-20 can be applied to any closed path that
can be drawn in a changing magnetic field. Figure 30-11d, for example, shows four
such paths, all having the same shape and area but located in different positions
in the changing field.The induced emfs 
for paths 1 and 2 are equal
because these paths lie entirely in the magnetic field and thus have the same
value of d0B/dt.This is true even though the electric field vectors at points along
these paths are different, as indicated by the patterns of electric field lines in the
figure. For path 3 the induced emf is smaller because the enclosed flux 0B (hence
d0B/dt) is smaller, and for path 4 the induced emf is zero even though the electric
field is not zero at any point on the path.
A New Look at Electric Potential
Induced electric fields are produced not by static charges but by a changing mag-
netic flux.Although electric fields produced in either way exert forces on charged
particles, there is an important difference between them. The simplest evidence
of this difference is that the field lines of induced electric fields form closed loops,
as in Fig. 30-11c. Field lines produced by static charges never do so but must start
on positive charges and end on negative charges.Thus, a field line from a charge
can never loop around and back onto itself as we see for each of the field lines
in Fig. 30-11c.
In a more formal sense, we can state the difference between electric fields
produced by induction and those produced by static charges in these words:
# (! - E
:!ds
:)
Electric potential has meaning only for electric fields that are produced by static
charges; it has no meaning for electric fields that are produced by induction.
You can understand this statement qualitatively by considering what happens
to a charged particle that makes a single journey around the circular path in
Fig. 30-11b. It starts at a certain point and, on its return to that same point, has
experienced an emf # of, let us say, 5 V; that is, work of 5 J/C has been done on the
particle by the electric field, and thus the particle should then be at a point that is
5 V greater in potential. However, that is impossible because the particle is back
at the same point, which cannot have two different values of potential. Thus, po-
tential has no meaning for electric fields that are set up by changing magnetic
fields.
We can take a more formal look by recalling Eq. 24-18, which defines the
potential difference between two points i and f in an electric field 
in terms of
an integration between those points:
(30-21)
In Chapter 24 we had not yet encountered Faraday’s law of induction; so the elec-
tric fields involved in the derivation of Eq. 24-18 were those due to static charges.
If i and f in Eq. 30-21 are the same point, the path connecting them is a closed
loop, Vi and Vf are identical, and Eq. 30-21 reduces to
(30-22)
However, when a changing magnetic flux is present, this integral is not zero but
is %d0B/dt, as Eq. 30-20 asserts. Thus, assigning electric potential to an induced
electric field leads us to a contradiction.We must conclude that electric potential
has no meaning for electric fields associated with induction.
, E
:!ds
: ! 0.
Vf % Vi ! %"
f
i
E
:!ds
:.
E
:

878
CHAPTER 30
INDUCTION AND INDUCTANCE
Checkpoint 4
The figure shows five lettered regions in which a uniform magnetic field extends either
directly out of the page or into the page, with the direction indicated only for region a.
The field is increasing in magnitude at the same steady rate in all five regions; the
regions are identical in area.Also shown are four numbered paths along which 
has the magnitudes given below in terms of a quantity “mag.” Determine whether the
magnetic field is directed into or out of the page for regions b through e.
Path
1
2
3
4
mag
2(mag)
3(mag)
0
- E
:!ds
:
- E
:!ds
:
1
3
2
4
a
b
d
c
e
the minus sign, we find that
or
(Answer)
(30-25)
Equation 30-25 gives the magnitude of the electric field at
any point for which r 2 R (that is, within the magnetic field).
Substituting given values yields, for the magnitude of 
at 
r ! 5.2 cm,
(Answer)
(b) Find an expression for the magnitude E of the induced
electric field at points that are outside the magnetic field, at
radius r from the center of the magnetic field. Evaluate the
expression for r ! 12.5 cm.
KEY IDEAS
Here again an electric field is induced by the changing mag-
netic field, according to Faraday’s law, except that now we
use a circular path of integration with radius r - R because
we want to evaluate E for points outside the magnetic field.
Proceeding as in (a), we again obtain Eq. 30-23. However,
we do not then obtain Eq. 30-24 because the new path of
integration is now outside the magnetic field, and so the
magnetic flux encircled by the new path is only that in the
area pR2 of the magnetic field region.
Calculations: We can now write
0B ! BA ! B(pR2).
(30-26)
! 0.0034 V/m ! 3.4 mV/m.
E ! (5.2 $ 10 %2 m)
2
 (0.13 T/s)
E
:
E ! r
2
dB
dt .
E(2pr) ! (pr2) dB
dt
