Example 29.11
Induced electric fields
Suppose the long solenoid in Fig. 29.17a has 500 turns per meter
and cross-sectional area 
The current in its windings is
increasing at 
(a) Find the magnitude of the induced emf
in the wire loop outside the solenoid. (b) Find the magnitude of the
induced electric field within the loop if its radius is 2.0 cm.
SOLUTION
IDENTIFY and SET UP: As in Fig. 29.17b, the increasing magnetic
field inside the solenoid causes a change in the magnetic flux
through the wire loop and hence induces an electric field 
around
the loop. Our target variables are the induced emf 
and the
electric-field magnitude E. We use Eq. (29.8) to determine the emf.
E
E
S
100 A>s.
4.0 cm2.
Determining the field magnitude E is simplified because the loop
and the solenoid share the same central axis. Hence, by symmetry,
the electric field is tangent to the loop and has the same magnitude
all the way around its circumference. We can therefore use Eq.
(29.9) to find E.
EXECUTE: (a) From Eq. (29.8), the induced emf is
Continued
= -25 * 10-6 Wb>s = -25 * 10-6V = -25 mV
* 14.0 * 10-4m221100 A>s2
= -14p * 10-7Wb>A # m21500 turns>m2
E = - d£B
dt
= -m0nAdI
dt

29.6 Eddy Currents
In the examples of induction effects that we have studied, the induced currents
have been confined to well-defined paths in conductors and other components
forming a circuit. However, many pieces of electrical equipment contain masses
of metal moving in magnetic fields or located in changing magnetic fields. In sit-
uations like these we can have induced currents that circulate throughout the vol-
ume of a material. Because their flow patterns resemble swirling eddies in a river,
we call these eddy currents.
As an example, consider a metallic disk rotating in a magnetic field perpendi-
cular to the plane of the disk but confined to a limited portion of the disk’s area,
as shown in Fig. 29.19a. Sector Ob is moving across the field and has an emf
induced in it. Sectors Oa and Oc are not in the field, but they provide return con-
ducting paths for charges displaced along Ob to return from b to O. The result is a
circulation of eddy currents in the disk, somewhat as sketched in Fig. 29.19b.
We can use Lenz’s law to decide on the direction of the induced current in the
neighborhood of sector Ob. This current must experience a magnetic force 
that opposes the rotation of the disk, and so this force must be to the
right in Fig. 29.19b. Since 
is directed into the plane of the disk, the current
and hence 
have downward components. The return currents lie outside the
field, so they do not experience magnetic forces. The interaction between the
eddy currents and the field causes a braking action on the disk. Such effects can
be used to stop the rotation of a circular saw quickly when the power is turned
off. Some sensitive balances use this effect to damp out vibrations. Eddy
current braking is used on some electrically powered rapid-transit vehicles.
Electromagnets mounted in the cars induce eddy currents in the rails; the
resulting magnetic fields cause braking forces on the electromagnets and thus
on the cars.
Eddy currents have many other practical uses. The shiny metal disk in the
electric power company’s meter outside your house rotates as a result of eddy
currents. These currents are induced in the disk by magnetic fields caused by
sinusoidally varying currents in a coil. In induction furnaces, eddy currents are
used to heat materials in completely sealed containers for processes in which it is
essential to avoid the slightest contamination of the materials. The metal detec-
tors used at airport security checkpoints (Fig. 29.20a) operate by detecting eddy
currents induced in metallic objects. Similar devices (Fig. 29.20b) are used to
find buried treasure such as bottlecaps and lost pennies.
Eddy currents also have undesirable effects. In an alternating-current trans-
former, coils wrapped around an iron core carry a sinusoidally varying current.
The resulting eddy currents in the core waste energy through 
heating and
themselves set up an unwanted opposing emf in the coils. To minimize these
effects, the core is designed so that the paths for eddy currents are as narrow as
possible. We’ll describe how this is done when we discuss transformers in detail
in Section 31.6.
I 2R
L
S
B
S
IL
S : B
S
F
S 
974
CHAPTER 29 Electromagnetic Induction
(b) By symmetry the line integral 
has absolute value
no matter which direction we integrate around the loop. This
is equal to the absolute value of the emf, so
E =
ƒEƒ
2pr =
25 * 10-6V
2p12.0 * 10-2m2
= 2.0 * 10-4V>m
2prE
AE
S # dl
S
EVALUATE: In Fig. 29.17b the magnetic flux into the plane of the
figure is increasing. According to the right-hand rule for induced
emf (illustrated in Fig. 29.6), a positive emf would be clockwise
around the loop; the negative sign of 
shows that the emf is in the
counterclockwise direction. Can you also show this using Lenz’s
law?
E
Test Your Understanding of Section 29.5
If you wiggle a magnet back and
forth in your hand, are you generating an electric field? If so, is this electric field conser-
vative?
❙
O
a
Eddy currents
c
Magnetic
field
b
a
c
b
(a) Metal disk rotating through a magnetic field
(b) Resulting eddy currents and braking force
B
S
B
S
F
S
29.19 Eddy currents induced in a rotat-
ing metal disk.

29.7 Displacement Current and Maxwell’s Equations
975
29.7 Displacement Current 
and Maxwell’s Equations
We have seen that a varying magnetic field gives rise to an induced electric field.
In one of the more remarkable examples of the symmetry of nature, it turns out
that a varying electric field gives rise to a magnetic field. This effect is of tremen-
dous importance, for it turns out to explain the existence of radio waves, gamma
rays, and visible light, as well as all other forms of electromagnetic waves.
Generalizing Ampere’s Law
To see the origin of the relationship between varying electric fields and magnetic
fields, let’s return to Ampere’s law as given in Section 28.6, Eq. (28.20):
The problem with Ampere’s law in this form is that it is incomplete. To see why, let’s
consider the process of charging a capacitor (Fig. 29.21). Conducting wires lead cur-
rent 
into one plate and out of the other; the charge Q increases, and the electric
field 
between the plates increases. The notation 
indicates conduction current to
distinguish it from another kind of current we are about to encounter, called
displacement current 
We use lowercase i’s and 
to denote instantaneous val-
ues of currents and potential differences, respectively, that may vary with time.
Let’s apply Ampere’s law to the circular path shown. The integral 
around this path equals 
For the plane circular area bounded by the circle,
is just the current 
in the left conductor. But the surface that bulges out to
the right is bounded by the same circle, and the current through that surface is
zero. So 
is equal to 
and at the same time it is equal to zero! This is
a clear contradiction.
But something else is happening on the bulged-out surface. As the capacitor
charges, the electric field 
and the electric flux
through the surface are
increasing. We can determine their rates of change in terms of the charge and
£E
E
S
m0iC,
AB
S # dl
S
iC
Iencl
m0Iencl.
AB
S # dl
S
v’s
iD.
iC
E
SiC
C
B
S # dl
S = m0Iencl
Test Your Understanding of Section 29.6
Suppose that the magnetic field in
Fig. 29.19 were directed out of the plane of the figure and the disk were rotating counter-
clockwise. Compared to the directions of the force 
and the eddy currents shown in Fig.
29.19b, what would the new directions be? (i) The force 
and the eddy currents would
both be in the same direction; (ii) the force 
would be in the same direction, but the
eddy currents would be in the opposite direction; (iii) the force 
would be in the oppo-
site direction, but the eddy currents would be in the same direction; (iv) the force 
and
the eddy currents would be in the opposite directions.
❙
F
S
F
S
F
S
F
S
F
S
Pulse of
current
I
Eddy currents 
B0
I0
I
B
B0
Receiver
coil
Eddy
currents
Transmitting
coil
(a)
(b)
B
S
S
S
S
I0
29.20 (a) A metal detector at an airport
security checkpoint generates an alternat-
ing magnetic field 
. This induces eddy
currents in a conducting object carried
through the detector. The eddy currents in
turn produce an alternating magnetic field
and this field induces a current in the
detector’s receiver coil. (b) Portable metal
detectors work on the same principle.
B
S¿,
B
S
0
Magnetic field line
Jupiter
Io
Volcanic eruptions
on Io
Application Eddy Currents Help
Power Io’s Volcanoes
Jupiter’s moon Io is slightly larger than the
earth’s moon. It moves at more than 
60,000 km h through Jupiter’s intense mag-
netic field (about ten times stronger than the
earth’s field), which sets up strong eddy cur-
rents within Io that dissipate energy at a rate
of 1012 W. This dissipated energy helps to
heat Io’s interior and causes volcanic erup-
tions on its surface, as shown in the lower
close-up image. (Gravitational effects from
Jupiter cause even more heating.)
>
+
+
+
+
+
+
+
+
+
+
-
-
-
-
-
-
-
-
-
-
Bulging surface
Path for
Ampere’s law
Plane
surface
iC
iC
E
dl
Q
-Q
r
r
29.21 Parallel-plate capacitor being
charged. The conduction current through
the plane surface is 
but there is no con-
duction current through the surface that
bulges out to pass between the plates. The
two surfaces have a common boundary, so
this difference in 
leads to an apparent
contradiction in applying Ampere’s law.
Iencl
iC,

current. The instantaneous charge is 
where C is the capacitance and is
the instantaneous potential difference. For a parallel-plate capacitor, 
where A is the plate area and d is the spacing. The potential difference between
plates is 
where E is the electric-field magnitude between plates. (We
neglect fringing and assume that 
is uniform in the region between the plates.)
If this region is filled with a material with permittivity 
we replace 
by 
everywhere; we’ll use in the following discussion.
Substituting these expressions for C and 
into 
we can express the
capacitor charge q as
(29.12)
where 
is the electric flux through the surface.
As the capacitor charges, the rate of change of q is the conduction current,
Taking the derivative of Eq. (29.12) with respect to time, we get
(29.13)
Now, stretching our imagination a little, we invent a fictitious displacement cur-
rent
in the region between the plates, defined as
(29.14)
That is, we imagine that the changing flux through the curved surface in Fig.
29.21 is somehow equivalent, in Ampere’s law, to a conduction current through
that surface. We include this fictitious current, along with the real conduction cur-
rent 
in Ampere’s law:
(29.15)
Ampere’s law in this form is obeyed no matter which surface we use in Fig.
29.21. For the flat surface, 
is zero; for the curved surface, 
is zero; and 
for
the flat surface equals 
for the curved surface. Equation (29.15) remains valid
in a magnetic material, provided that the magnetization is proportional to the
external field and we replace 
by 
The fictitious current 
was invented in 1865 by the Scottish physicist James
Clerk Maxwell (1831-1879), who called it displacement current. There is a cor-
responding displacement current density
using 
and divid-
ing Eq. (29.14) by A, we find
(29.16)
We have pulled the concept out of thin air, as Maxwell did, but we see that it
enables us to save Ampere’s law in situations such as that in Fig. 29.21.
Another benefit of displacement current is that it lets us generalize Kirchhoff’s
junction rule, discussed in Section 26.2. Considering the left plate of the capacitor,
we have conduction current into it but none out of it. But when we include the dis-
placement current, we have conduction current coming in one side and an equal
displacement current coming out the other side. With this generalized meaning of
the term “current,” we can speak of current going through the capacitor.
The Reality of Displacement Current
You might well ask at this point whether displacement current has any real physi-
cal significance or whether it is just a ruse to satisfy Ampere’s law and Kirchhoff’s
jD = P dE
dt
£E = EA
jD = iD>A;
iD
m.
m0
iD
iC
iC
iD
C
B
S # dl
S = m01iC + iD2encl  (generalized Ampere’s law)
iC,
iD = P d£E
dt   (displacement current)
iD
iC = dq
dt = P d£E
dt
iC = dq/dt.
£E = EA
q = Cv = PA
d 1Ed2 = PEA = P£E
q = Cv,
v
P
P
P0
P,
E
S
v = Ed,
v
C = P0 A>d,
v
q = Cv,
976
CHAPTER 29 Electromagnetic Induction

29.7 Displacement Current and Maxwell’s Equations
977
junction rule. Here’s a fundamental experiment that helps to answer that ques-
tion. We take a plane circular area between the capacitor plates (Fig. 29.22). If
displacement current really plays the role in Ampere’s law that we have claimed,
then there ought to be a magnetic field in the region between the plates while the
capacitor is charging. We can use our generalized Ampere’s law, including dis-
placement current, to predict what this field should be.
To be specific, let’s picture round capacitor plates with radius R. To find the
magnetic field at a point in the region between the plates at a distance r from the
axis, we apply Ampere’s law to a circle of radius r passing through the point,
with 
This circle passes through points a and b in Fig. 29.22. The total cur-
rent enclosed by the circle is 
times its area, or 
The integral
in Ampere’s law is just B times the circumference 
of the circle, and
because 
for the charging capacitor, Ampere’s law becomes
(29.17)
This result predicts that in the region between the plates 
is zero at the axis and
increases linearly with distance from the axis. A similar calculation shows that
outside the region between the plates (that is, for 
is the same as though
the wire were continuous and the plates not present at all.
When we measure the magnetic field in this region, we find that it really is
there and that it behaves just as Eq. (29.17) predicts. This confirms directly the
role of displacement current as a source of magnetic field. It is now established
beyond reasonable doubt that displacement current, far from being just an arti-
fice, is a fundamental fact of nature. Maxwell’s discovery was the bold step of an
extraordinary genius.
Maxwell’s Equations of Electromagnetism
We are now in a position to wrap up in a single package all of the relationships
between electric and magnetic fields and their sources. This package consists of
four equations, called Maxwell’s equations. Maxwell did not discover all of
these equations single-handedly (though he did develop the concept of displace-
ment current). But he did put them together and recognized their significance,
particularly in predicting the existence of electromagnetic waves.
For now we’ll state Maxwell’s equations in their simplest form, for the case in
which we have charges and currents in otherwise empty space. In Chapter 32
we’ll discuss how to modify these equations if a dielectric or a magnetic material
is present.
Two of Maxwell’s equations involve an integral of 
or 
over a closed sur-
face. The first is simply Gauss’s law for electric fields, Eq. (22.8), which states
that the surface integral of 
over any closed surface equals 
times the total
charge 
enclosed within the surface:
(29.18)
The second is the analogous relationship for magnetic fields, Eq. (27.8), which
states that the surface integral of 
over any closed surface is always zero:
(29.19)
This statement means, among other things, that there are no magnetic monopoles
(single magnetic charges) to act as sources of magnetic field.
C
B
S # dA
S = 0  (Gauss’s law for B
S)
B
C
E
S # dA
S = Qencl
P0   (Gauss’s law for E
S)
Qencl
1>P0
E
B
S
E
S
B
S
r 7 R),
B
S
B = m0
2p
r
R2 iC
C
B
S # dl
S = 2prB = m0
r 2
R2 iC  or
iD = iC
2pr
AB
S # dl
S
1iD>pR221pr 22.
jD
r 6 R.
-
-
-
-
-
-
-
-
-
-
-
+
+
+
+
+
+
+
+
+
iC
E
q
B
a
iC
q
R
r
b
r
r
29.22 A capacitor being charged by a
current 
has a displacement current equal
to 
between the plates, with displacement-
current density 
This can be
regarded as the source of the magnetic
field between the plates.
jD = P dE/dt.
iC
iC

The third equation is Ampere’s law including displacement current. This states
that both conduction current 
and displacement current 
where 
is
electric flux, act as sources of magnetic field:
(29.20)
The fourth and final equation is Faraday’s law. It states that a changing mag-
netic field or magnetic flux induces an electric field:
(29.21)
If there is a changing magnetic flux, the line integral in Eq. (29.21) is not zero,
which shows that the 
field produced by a changing magnetic flux is not conserva-
tive. Recall that this line integral must be carried out over a stationary closed path.
It’s worthwhile to look more carefully at the electric field 
and its role in
Maxwell’s equations. In general, the total 
field at a point in space can be the
superposition of an electrostatic field 
caused by a distribution of charges at
rest and a magnetically induced, nonelectrostatic field 
(The subscript c stands
for Coulomb or conservative; the subscript n stands for non-Coulomb, nonelec-
trostatic, or nonconservative.) That is,
The electrostatic part 
is always conservative, so 
This conserva-
tive part of the field does not contribute to the integral in Faraday’s law, so we can
take 
in Eq. (29.21) to be the total electric field 
including both the part 
due
to charges and the magnetically induced part 
Similarly, the nonconservative
part 
of the 
field does not contribute to the integral in Gauss’s law, because this
part of the field is not caused by static charges. Hence 
is always zero. We
conclude that in all the Maxwell equations, 
is the total electric field; these equa-
tions don’t distinguish between conservative and nonconservative fields.
Symmetry in Maxwell’s Equations
There is a remarkable symmetry in Maxwell’s four equations. In empty space
where there is no charge, the first two equations (Eqs. (29.18) and (29.19)) are
identical in form, one containing 
and the other containing 
When we com-
pare the second two equations, Eq. (29.20) says that a changing electric flux cre-
ates a magnetic field, and Eq. (29.21) says that a changing magnetic flux creates
an electric field. In empty space, where there is no conduction current, 
and the two equations have the same form, apart from a numerical constant and a
negative sign, with the roles of 
and 
exchanged in the two equations.
We can rewrite Eqs. (29.20) and (29.21) in a different but equivalent form by
introducing the definitions of electric and magnetic flux, 
and
respectively. In empty space, where there is no charge or con-
duction current, 
and 
and we have
(29.22)
(29.23)
Again we notice the symmetry between the roles of 
and 
in these expressions.
The most remarkable feature of these equations is that a time-varying field of
either kind induces a field of the other kind in neighboring regions of space.
Maxwell recognized that these relationships predict the existence of electromagnetic
disturbances consisting of time-varying electric and magnetic fields that travel or
propagate from one region of space to another, even if no matter is present in the
B
S
E
S
C
E
S # dl
S = - d
dt L
B
S # dA
S
C
B
S # dl
S = P0m0
d
dt L
E
S # dA
S
Qencl = 0,
iC = 0
£B = 1B
S # dA
S,
£E = 1E
S # dA
S
B
S
E
S
iC = 0
B
S.
E
S
E
S
AE
S
n# dA
S
E
S
E
S
n
E
S
n.
E
S
c
E
S,
E
S
AE
S
c# dl
S = 0.
E
S
c
E
S  E
S
c  E
S
n
E
S
n.
E
S
c
E
S
E
S
E
S
C
E
S # dl
S = - d£B
dt   (Faraday’s law)
C
B
S # dl
S = m0aiC + P0
d£E
dt b
encl  (Ampere’s law)
£E
P0d£E>dt,
iC
978
CHAPTER 29 Electromagnetic Induction

29.8 Superconductivity
979
intervening space. Such disturbances, called electromagnetic waves, provide the
physical basis for light, radio and television waves, infrared, ultraviolet, x rays,
and the rest of the electromagnetic spectrum. We will return to this vitally impor-
tant topic in Chapter 32.
Although it may not be obvious, all the basic relationships between fields and
their sources are contained in Maxwell’s equations. We can derive Coulomb’s
law from Gauss’s law, we can derive the law of Biot and Savart from Ampere’s
law, and so on. When we add the equation that defines the 
and 
fields in terms
of the forces that they exert on a charge q, namely,
(29.24)
we have all the fundamental relationships of electromagnetism!
Finally, we note that Maxwell’s equations would have even greater symmetry
between the 
and 
fields if single magnetic charges (magnetic monopoles)
existed. The right side of Eq. (29.19) would contain the total magnetic charge
enclosed by the surface, and the right side of Eq. (29.21) would include a mag-
netic monopole current term. Perhaps you can begin to see why some physicists
wish that magnetic monopoles existed; they would help to perfect the mathemat-
ical poetry of Maxwell’s equations.
The discovery that electromagnetism can be wrapped up so neatly and ele-
gantly is a very satisfying one. In conciseness and generality, Maxwell’s equations
are in the same league with Newton’s laws of motion and the laws of thermody-
namics. Indeed, a major goal of science is learning how to express very broad and
general relationships in a concise and compact form. Maxwell’s synthesis of elec-
tromagnetism stands as a towering intellectual achievement, comparable to the
Newtonian synthesis we described at the end of Section 13.5 and to the develop-
ment of relativity and quantum mechanics in the 20th century.
B
S
E
S
F
S  q1E
S  v
S : B
S2
B
S
E
S
Test Your Understanding of Section 29.7
(a) Which of Maxwell’s equations
explains how a credit card reader works? (b) Which one describes how a wire carrying a
steady current generates a magnetic field?
❙
29.8 Superconductivity
The most familiar property of a superconductor is the sudden disappearance of
all electrical resistance when the material is cooled below a temperature called
the critical temperature, denoted by 
We discussed this behavior and the cir-
cumstances of its discovery in Section 25.2. But superconductivity is far more
than just the absence of measurable resistance. As we’ll see in this section, super-
conductors also have extraordinary magnetic properties.
The first hint of unusual magnetic properties was the discovery that for any
superconducting material the critical temperature 
changes when the material is
placed in an externally produced magnetic field 
Figure 29.23 shows this
dependence for mercury, the first element in which superconductivity was
observed. As the external field magnitude 
increases, the superconducting tran-
sition occurs at lower and lower temperature. When 
is greater than 0.0412 T,
no superconducting transition occurs. The minimum magnitude of magnetic field
that is needed to eliminate superconductivity at a temperature below 
is called
the critical field, denoted by 
The Meissner Effect
Another aspect of the magnetic behavior of superconductors appears if we place
a homogeneous sphere of a superconducting material in a uniform applied mag-
netic field
at a temperature T greater than 
The material is then in the normal
phase, not the superconducting phase (Fig. 29.24a). Now we lower the temperature
until the superconducting transition occurs. (We assume that the magnitude of 
is
not large enough to prevent the phase transition.) What happens to the field?
B
S
0
Tc.
B
S
0
Bc.
Tc
B0
B0
B
S
0.
Tc
Tc.
0.05
T (K)
0.04
0.03
0.02
0.01
1
2
3
4
5
Normal
phase
Super-
conducting
phase
Bc (T)
O
Tc
29.23 Phase diagram for pure mercury,
showing the critical magnetic field 
and
its dependence on temperature. Supercon-
ductivity is impossible above the critical
temperature 
The curves for other super-
conducting materials are similar but with
different numerical values.
Tc.
Bc

Measurements of the field outside the sphere show that the field lines become
distorted as in Fig. 29.24b. There is no longer any field inside the material, except
possibly in a very thin surface layer a hundred or so atoms thick. If a coil is
wrapped around the sphere, the emf induced in the coil shows that during the
superconducting transition the magnetic flux through the coil decreases from its
initial value to zero; this is consistent with the absence of field inside the mate-
rial. Finally, if the field is now turned off while the material is still in its super-
conducting phase, no emf is induced in the coil, and measurements show no field
outside the sphere (Fig. 29.24c).
We conclude that during a superconducting transition in the presence of the
field 
all of the magnetic flux is expelled from the bulk of the sphere, and the
magnetic flux 
through the coil becomes zero. This expulsion of magnetic flux
is called the Meissner effect. As Fig. 29.24b shows, this expulsion crowds the
magnetic field lines closer together to the side of the sphere, increasing 
there.
Superconductor Levitation and Other Applications
The diamagnetic nature of a superconductor has some interesting mechanical con-
sequences. A paramagnetic or ferromagnetic material is attracted by a permanent
magnet because the magnetic dipoles in the material align with the nonuniform
magnetic field of the permanent magnet. (We discussed this in Section 27.7.) For a
diamagnetic material the magnetization is in the opposite sense, and a diamagnetic
material is repelled by a permanent magnet. By Newton’s third law the magnet is
also repelled by the diamagnetic material. Figure 29.25 shows the repulsion
between a specimen of a high-temperature superconductor and a magnet; the mag-
net is supported (“levitated”) by this repulsive magnetic force.
The behavior we have described is characteristic of what are called type-I
superconductors. There is another class of superconducting materials called type-II
superconductors. When such a material in the superconducting phase is placed in
a magnetic field, the bulk of the material remains superconducting, but thin fila-
ments of material, running parallel to the field, may return to the normal phase.
Currents circulate around the boundaries of these filaments, and there is magnetic
flux inside them. Type-II superconductors are used for electromagnets because
they usually have much larger values of 
than do type-I materials, permitting
much larger magnetic fields without destroying the superconducting state. Type-II
superconductors have two critical magnetic fields: The first, 
is the field at
which magnetic flux begins to enter the material, forming the filaments just
described, and the second, 
is the field at which the material becomes normal.
Many important and exciting applications of superconductors are under devel-
opment. Superconducting electromagnets have been used in research laboratories
for several years. Their advantages compared to conventional electromagnets
include greater efficiency, compactness, and greater field magnitudes. Once a
current is established in the coil of a superconducting electromagnet, no addi-
tional power input is required because there is no resistive energy loss. The coils
can also be made more compact because there is no need to provide channels for
the circulation of cooling fluids. Superconducting magnets routinely attain steady
fields of the order of 10 T, much larger than the maximum fields that are available
with ordinary electromagnets.
Superconductors are attractive for long-distance electric power transmission
and for energy-conversion devices, including generators, motors, and transform-
ers. Very sensitive measurements of magnetic fields can be made with supercon-
ducting quantum interference devices (SQUIDs), which can detect changes in
magnetic flux of less than 
these devices have applications in medi-
cine, geology, and other fields. The number of potential uses for superconductors
has increased greatly since the discovery in 1987 of high-temperature supercon-
ductors. These materials have critical temperatures that are above the tempera-
ture of liquid nitrogen (about 77 K) and so are comparatively easy to attain.
Development of practical applications of superconductor science promises to be
an exciting chapter in contemporary technology.
10-14 Wb;
Bc2,
Bc1,
Bc
B
S
£B
B
S
0,
980
CHAPTER 29 Electromagnetic Induction
The field inside the material
is very nearly equal to B0.
(a) Superconducting material in an external
magnetic field B0 at T  Tc.
(b) The temperature is lowered to T  Tc, so
the material becomes superconducting.
(c) When the external field is turned off at
T  Tc,  the field is zero everywhere.
B0
B0
B = 0
B
Magnetic flux is expelled from the material,
and the field inside it is zero (Meissner effect).
B = 0
There is no
change in 
magnetic flux
in the material.
B = 0
S
S
S
S
S
S
S
S
29.24 A superconducting material (a)
above the critical temperature and (b), (c)
below the critical temperature.
29.25 A superconductor (the black slab)
exerts a repulsive force on a magnet (the
metallic cylinder), supporting the magnet
in midair.
