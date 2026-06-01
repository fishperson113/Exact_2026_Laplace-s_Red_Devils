29.7 Displacement Current and Maxwell’s Equations

975

(a)

(b)

S
B0

S

B(cid:5)

I0

Pulse of
current

I(cid:5)

I0

I(cid:5)

Eddy
currents

S
B0

S

B(cid:5)

Transmitting
coil

Receiver
coil

Eddy currents

Test Your Understanding of Section 29.6 Suppose that the magnetic ﬁeld in
Fig. 29.19 were directed out of the plane of the ﬁgure and the disk were rotating counter-
clockwise. Compared to the directions of the force
and the eddy currents shown in Fig.
29.19b, what would the new directions be? (i) The force
S
both be in the same direction; (ii) the force  would be in the same direction, but the
F
eddy currents would be in the opposite direction; (iii) the force  would be in the oppo-
site direction, but the eddy currents would be in the same direction; (iv) the force
and
the eddy currents would be in the opposite directions.

and the eddy currents would

S
F

S
F

S
F

S
F

29.7 Displacement Current

and Maxwell’s Equations

29.20 (a) A metal detector at an airport
security checkpoint generates an alternat-
S
. This induces eddy
ing magnetic ﬁeld
B
0
currents in a conducting object carried
through the detector. The eddy currents in
turn produce an alternating magnetic ﬁeld
S
and this ﬁeld induces a current in the
B
detector’s receiver coil. (b) Portable metal
detectors work on the same principle.

¿,

>

Application Eddy Currents Help
Power Io’s Volcanoes
Jupiter’s moon Io is slightly larger than the
earth’s moon. It moves at more than
60,000 km h through Jupiter’s intense mag-
netic ﬁeld (about ten times stronger than the
earth’s ﬁeld), which sets up strong eddy cur-
rents within Io that dissipate energy at a rate
of 1012 W. This dissipated energy helps to
heat Io’s interior and causes volcanic erup-
tions on its surface, as shown in the lower
close-up image. (Gravitational effects from
Jupiter cause even more heating.)

❙

Magnetic field line

Jupiter

Io

We have seen that a varying magnetic ﬁeld gives rise to an induced electric ﬁeld.
In one of the more remarkable examples of the symmetry of nature, it turns out
that a varying electric ﬁeld gives rise to a magnetic ﬁeld. This effect is of tremen-
dous importance, for it turns out to explain the existence of radio waves, gamma
rays, and visible light, as well as all other forms of electromagnetic waves.

Generalizing Ampere’s Law
To see the origin of the relationship between varying electric ﬁelds and magnetic
ﬁelds, let’s return to Ampere’s law as given in Section 28.6, Eq. (28.20):

S # d l

B

S

C

= m0Iencl

iC

SiC
E

The problem with Ampere’s law in this form is that it is incomplete. To see why, let’s
consider the process of charging a capacitor (Fig. 29.21). Conducting wires lead cur-
into one plate and out of the other; the charge Q increases, and the electric
rent
indicates conduction current to
ﬁeld  between the plates increases. The notation
distinguish  it  from  another  kind  of  current  we  are  about  to  encounter,  called
displacement current  We use lowercase i’s and
to denote instantaneous val-
ues of currents and potential differences, respectively, that may vary with time.
Let’s  apply Ampere’s  law  to  the  circular  path  shown.  The  integral
AB

S # d l

m0Iencl.
around this path equals
For the plane circular area bounded by the circle,
in the left conductor. But the surface that bulges out to
is just the current
iC
Iencl
the right is bounded by the same circle, and the current through that surface is
zero. So
and at the same time it is equal to zero! This is
AB
a clear contradiction.

S # d l

is equal to

m0iC,

iD.

v’s

S

S

But something else is happening on the bulged-out surface. As the capacitor
charges,  the  electric  ﬁeld
through  the  surface  are
and  the  electric  ﬂux
increasing.  We  can  determine  their  rates  of  change  in  terms  of  the  charge  and

£E

S
E

Volcanic eruptions
on Io

but there is no con-

29.21 Parallel-plate capacitor being
charged. The conduction current through
the plane surface is
iC,
duction current through the surface that
bulges out to pass between the plates. The
two surfaces have a common boundary, so
Iencl
this difference in
leads to an apparent
contradiction in applying Ampere’s law.

Path for
Ampere’s law

Bulging surface

+
+
+
+ +

+ +
+
+
+
Q

r
E

–
–
–
– –
– –
–
–
–Q

–

iC

r
dl

iC

Plane
surface

976

CHAPTER 29 Electromagnetic Induction

q = Cv,

v = Ed,

where C is the capacitance and

current. The instantaneous charge is
is
C = P0 A>d,
the instantaneous potential difference. For a parallel-plate capacitor,
where A is the plate area and d is the spacing. The potential difference  between
where  E is  the  electric-ﬁeld  magnitude  between  plates.  (We
plates  is
is uniform in the region between the plates.)
neglect fringing and assume that
P,
P
If  this  region  is  ﬁlled  with  a  material  with  permittivity  we  replace
everywhere; we’ll use

P
Substituting these expressions for C and

in the following discussion.
into

we can express the

q = Cv,

by

P0

S
E

v

v

v

capacitor charge q as

q = Cv =

PA
d

1Ed2 = PEA = P£E

(29.12)

where

£E = EA

is the electric ﬂux through the surface.

As  the  capacitor  charges,  the  rate  of  change  of  q is  the  conduction  current,

iC = dq/dt.

Taking the derivative of Eq. (29.12) with respect to time, we get

iC =

dq
dt

= P

d£E
dt

(29.13)

Now, stretching our imagination a little, we invent a ﬁctitious displacement cur-
rent

in the region between the plates, deﬁned as

iD

iD = P

d£E
dt

    (displacement current)

(29.14)

That  is,  we  imagine  that  the  changing  ﬂux  through  the  curved  surface  in  Fig.
29.21 is somehow equivalent, in Ampere’s law, to a conduction current through
that surface. We include this ﬁctitious current, along with the real conduction cur-
rent

in Ampere’s law:

iC,

= m01iC + iD2encl    (generalized Ampere’s law)

(29.15)

S # d l

B

S

C

Ampere’s  law  in  this  form  is  obeyed  no  matter  which  surface  we  use  in  Fig.
iD
29.21. For the ﬂat surface,
for
for the curved surface. Equation (29.15) remains valid
the ﬂat surface equals
in  a  magnetic  material,  provided  that  the  magnetization  is  proportional  to  the
external ﬁeld and we replace

is zero; for the curved surface,

is zero; and

by

m.

iD

iC

iC

m0

iD

The ﬁctitious current  was invented in 1865 by the Scottish physicist James
Clerk Maxwell (1831–1879), who called it displacement current. There is a cor-
responding displacement current density
and divid-
ing Eq. (29.14) by A, we ﬁnd

jD = iD>A;

£E = EA

using

jD = P dE
dt

(29.16)

We  have  pulled  the  concept  out  of  thin  air,  as  Maxwell  did,  but  we  see  that  it
enables us to save Ampere’s law in situations such as that in Fig. 29.21.

Another beneﬁt of displacement current is that it lets us generalize Kirchhoff’s
junction rule, discussed in Section 26.2. Considering the left plate of the capacitor,
we have conduction current into it but none out of it. But when we include the dis-
placement current, we have conduction current coming in one side and an equal
displacement current coming out the other side. With this generalized meaning of
the term “current,” we can speak of current going through the capacitor.

The Reality of Displacement Current
You might well ask at this point whether displacement current has any real physi-
cal signiﬁcance or whether it is just a ruse to satisfy Ampere’s law and Kirchhoff’s

29.7 Displacement Current and Maxwell’s Equations

977

iC

has a displacement current equal
between the plates, with displacement-
jD = P dE/dt.

29.22 A capacitor being charged by a
current
to
iC
current density
regarded as the source of the magnetic
ﬁeld between the plates.

This can be

r
E

a

r

b

r
B

–

–

–

–

–

–

–

–

–

–
–

q

iC

iC

++
R
+

+

+

+

+

+

+
q

junction  rule.  Here’s  a  fundamental  experiment  that  helps  to  answer  that  ques-
tion. We take a plane circular area between the capacitor plates (Fig. 29.22). If
displacement current really plays the role in Ampere’s law that we have claimed,
then there ought to be a magnetic ﬁeld in the region between the plates while the
capacitor is charging. We can use our generalized Ampere’s law, including dis-
placement current, to predict what this ﬁeld should be.

To be speciﬁc, let’s picture round capacitor plates with radius R. To ﬁnd the
magnetic ﬁeld at a point in the region between the plates at a distance r from the
axis,  we  apply Ampere’s  law  to  a  circle  of  radius  r passing  through  the  point,
This circle passes through points a and b in Fig. 29.22. The total cur-
with
The integral
rent enclosed by the circle is
AB
of the circle, and
because

in Ampere’s law is just B times the circumference
iD = iC

for the charging capacitor, Ampere’s law becomes

r 6 R.
S # d l

1iD>pR221pr 22.

times its area, or

2pr

jD

S

S # d l

B

S

C

= 2prB = m0

B =

m0
2p

r
R2 iC

r 2

R2 iC    or

(29.17)

is zero at the axis and
This result predicts that in the region between the plates
increases linearly with distance from the axis. A similar calculation shows that
r 7 R),
outside the region between the plates (that is, for
is the same as though
the wire were continuous and the plates not present at all.

S
B

S
B

When we measure the magnetic ﬁeld in this region, we ﬁnd that it really is
there and that it behaves just as Eq. (29.17) predicts. This conﬁrms directly the
role of displacement current as a source of magnetic ﬁeld. It is now established
beyond reasonable doubt that displacement current, far from being just an arti-
ﬁce, is a fundamental fact of nature. Maxwell’s discovery was the bold step of an
extraordinary genius.

Maxwell’s Equations of Electromagnetism
We are now in a position to wrap up in a single package all of the relationships
between electric and magnetic ﬁelds and their sources. This package consists of
four  equations,  called  Maxwell’s  equations. Maxwell  did  not  discover  all  of
these equations single-handedly (though he did develop the concept of displace-
ment  current).  But  he  did  put  them  together  and  recognized  their  signiﬁcance,
particularly in predicting the existence of electromagnetic waves.

For now we’ll state Maxwell’s equations in their simplest form, for the case in
which  we  have  charges  and  currents  in  otherwise  empty  space.  In  Chapter  32
we’ll discuss how to modify these equations if a dielectric or a magnetic material
is present.

Two of Maxwell’s equations involve an integral of

over a closed sur-
face. The ﬁrst is simply Gauss’s law for electric ﬁelds, Eq. (22.8), which states
times the total
that the surface integral of
charge

over any closed surface equals

enclosed within the surface:

1>P0

E(cid:2)

or

Qencl

S
E

S
B

S # dA

E

S

C

=

Qencl
P0

    (Gauss’s law for E

S

)

(29.18)

The second is the analogous relationship for magnetic ﬁelds, Eq. (27.8), which

states that the surface integral of

B(cid:2)

over any closed surface is always zero:

S # dA

B

S

C

= 0    (Gauss’s law for B

S

)

(29.19)

This statement means, among other things, that there are no magnetic monopoles
(single magnetic charges) to act as sources of magnetic ﬁeld.

978

CHAPTER 29 Electromagnetic Induction

The third equation is Ampere’s law including displacement current. This states
is

and displacement current

where

P0d£E>dt,

that both conduction current
electric ﬂux, act as sources of magnetic ﬁeld:

£E

iC

S # d l

B

S

C

= m0 aiC + P0

d£E
dt

b

    (Ampere’s law)

(29.20)

encl

The fourth and ﬁnal equation is Faraday’s law. It states that a changing mag-

netic ﬁeld or magnetic ﬂux induces an electric ﬁeld:

S # d l

E

S

C

= -

d£B
dt

    (Faraday’s law)

(29.21)

S
E

It’s  worthwhile  to  look  more  carefully  at  the  electric  ﬁeld

If  there  is  a  changing  magnetic  ﬂux,  the  line  integral  in  Eq.  (29.21) is  not  zero,
which shows that the  ﬁeld produced by a changing magnetic ﬂux is not conserva-
tive. Recall that this line integral must be carried out over a stationary closed path.
and  its  role  in
S
E
Maxwell’s equations. In general, the total  ﬁeld at a point in space can be the
S
caused by a distribution of charges at
E
superposition of an electrostatic ﬁeld
(The subscript c stands
rest and a magnetically induced, nonelectrostatic ﬁeld
for Coulomb or conservative; the subscript n stands for non-Coulomb, nonelec-
trostatic, or nonconservative.) That is,

S
E

S
E

n.

c

S
E

S

(cid:2) E

S

c (cid:3) E

n

# d l

S

S
AE

= 0.

S
E

c

c

S
E

is always conservative, so

in Eq. (29.21) to be the total electric ﬁeld
S
E

The electrostatic part
This conserva-
tive part of the ﬁeld does not contribute to the integral in Faraday’s law, so we can
including both the part
take
due
Similarly,  the  nonconservative
to  charges  and  the  magnetically  induced  part
of the  ﬁeld does not contribute to the integral in Gauss’s law, because this
part
part of the ﬁeld is not caused by static charges. Hence
is always zero. We
conclude that in all the Maxwell equations,
is the total electric ﬁeld; these equa-
tions don’t distinguish between conservative and nonconservative ﬁelds.

# dA

S
,
E
n.

S
AE

S
E

S
E

S
E

S
E

S

n

n

c

Symmetry in Maxwell’s Equations
There  is  a  remarkable  symmetry  in  Maxwell’s  four  equations.  In  empty  space
where there is no charge, the ﬁrst two equations (Eqs. (29.18) and (29.19)) are
identical in form, one containing
and the other containing  When we com-
pare the second two equations, Eq. (29.20) says that a changing electric ﬂux cre-
ates a magnetic ﬁeld, and Eq. (29.21) says that a changing magnetic ﬂux creates
iC = 0
an  electric  ﬁeld.  In  empty  space,  where  there  is  no  conduction  current,
and the two equations have the same form, apart from a numerical constant and a
negative sign, with the roles of

exchanged in the two equations.

and

S
.
B

S
E

S
E

S
B

We can rewrite Eqs. (29.20) and (29.21) in a different but equivalent form by
and
respectively. In empty space, where there is no charge or con-
iC = 0

introducing  the  deﬁnitions  of  electric  and  magnetic  ﬂux,
S # dA
£B = 1B
,
duction current,

£E = 1E

and we have

S # dA

and

S

S

S

B

Qencl = 0,
S # d l
S # d l

E

S

C

C

= P0m0

d
dt L

= - d

dt L

S

E

S # dA
S # dA

B

S

(29.22)

(29.23)

Again we notice the symmetry between the roles of

in these expressions.
The  most  remarkable  feature  of  these  equations  is  that  a  time-varying  ﬁeld  of
either kind  induces  a  ﬁeld  of  the  other  kind  in  neighboring  regions  of  space.
Maxwell recognized that these relationships predict the existence of electromagnetic
disturbances consisting of time-varying electric and magnetic ﬁelds that travel or
propagate from one region of space to another, even if no matter is present in the

and

S
E

S
B
