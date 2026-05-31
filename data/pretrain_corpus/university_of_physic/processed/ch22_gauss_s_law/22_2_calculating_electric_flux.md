728

CHAPTER 22 Gauss’s Law

S
E

22.4 (a) A box enclosing a positive point
+q.
charge
(b) Doubling the charge causes
the magnitude of
to double, and it dou-
bles the electric ﬂux through the surface.
(c) If the charge stays the same but the
dimensions of the box are doubled, the ﬂux
stays the same. The magnitude of  on the
surface decreases by a factor of  but the
S
E
area through which
a factor of 4.

1
4,
“ﬂows” increases by

S
E

(a) A box containing a charge

S
E

1q

(b) Doubling the enclosed charge
doubles the flux.

S
E

12q

(c) Doubling the box dimensions
does not change the flux.

S
E

1q

To summarize, for the special cases of a closed surface in the shape of a rectan-
gular box and charge distributions made up of point charges or inﬁnite charged
sheets, we have found:

1. Whether there is a net outward or inward electric ﬂux through a closed sur-

face depends on the sign of the enclosed charge.

2. Charges outside the surface do not give a net electric ﬂux through the sur-

face.

3. The  net  electric  ﬂux  is  directly  proportional  to  the  net  amount  of  charge
enclosed within the surface but is otherwise independent of the size of the
closed surface.

These observations are a qualitative statement of Gauss’s law.

Do these observations hold true for other kinds of charge distributions and for
closed surfaces of arbitrary shape? The answer to these questions will prove to be
yes. But to explain why this is so, we need a precise mathematical statement of
what we mean by electric ﬂux. We develop this in the next section.

Test Your Understanding of Section 22.1 If all of the dimensions of
the box in Fig. 22.2a are increased by a factor of 3, what effect will this change
have on the electric ﬂux through the box? (i) The ﬂux will be
greater; (ii) the ﬂux will be 3 times greater; (iii) the ﬂux will be unchanged; (iv) the ﬂux
B 2 = 1
1
will be  as great; (v) the ﬂux will be
3
9
given to decide.

as great; (vi) not enough information is

32 = 9

times

A 1
3

❙

22.2 Calculating Electric Flux

In the preceding section we introduced the concept of electric ﬂux. We used this
to give a rough qualitative statement of Gauss’s law: The net electric ﬂux through
a closed surface is directly proportional to the net charge inside that surface. To
be able to make full use of this law, we need to know how to calculate electric
S
E
ﬂux. To do this, let’s again make use of the analogy between an electric ﬁeld
in a ﬂowing ﬂuid. (Again, keep in mind that
and the ﬁeld of velocity vectors
this is only an analogy; an electric ﬁeld is not a ﬂow.)

S
v

Flux: Fluid-Flow Analogy
Figure 22.5 shows a ﬂuid ﬂowing steadily from left to right. Let’s examine the
(in, say, cubic meters per second) through the wire rectan-
volume ﬂow rate
(Fig. 22.5a)
gle with area  When the area is perpendicular to the ﬂow velocity
and the ﬂow velocity is the same at all points in the ﬂuid, the volume ﬂow rate
dV>dt

is the area  multiplied by the ﬂow speed

dV>dt

A.

v:

S
v

A

dV
dt

= vA

f

S
v
,

(Fig. 22.5b) so that its face is not per-
When the rectangle is tilted at an angle
the area that counts is the silhouette area that we see when we
pendicular to
look in the direction of  This area, which is outlined in red and labeled
in
S
v
A
Fig. 22.5b, is the projection of the area  onto a surface perpendicular to  Two
sides of the projected rectangle have the same length as the original one, but the
other two are foreshortened by a factor of
is equal
to

cos f,
A
Then the volume ﬂow rate through

so the projected area
is

A cos f.

A(cid:2)
.

A(cid:2)

S
v
.

dV
dt

= vA cos f

f = 90°,

If
passes through the rectangle.

dV>dt = 0;

the wire rectangle is edge-on to the ﬂow, and no ﬂuid

22.2 Calculating Electric Flux

729

22.5 The volume ﬂow rate of ﬂuid
through the wire rectangle (a) is  when
the area of the rectangle is perpendicular to
S
vA cos f
v
when the rectangle is
tilted at an angle f.

and (b) is

vA

(a) A wire rectangle in a fluid

A

S
v

(b) The wire rectangle tilted by an angle f

A' 5 A cos f

A

S
A

S
v

f

Application Flux Through a Basking
Shark’s Mouth
Unlike aggressive carnivorous sharks such as
great whites, a basking shark feeds passively
on plankton in the water that passes through
the shark’s gills as it swims. To survive on
these tiny organisms requires a huge ﬂux of
water through a basking shark’s immense
mouth, which can be up to a meter across.
The water ﬂux—the product of the shark’s
speed through the water and the area of its
mouth—can be up to 0.5
5 * 10 5
second, or almost
In a similar way, the ﬂux of electric ﬁeld through
a surface depends on the magnitude of the
ﬁeld and the area of the surface (as well as the
relative orientation of the ﬁeld and surface).

gallons per hour).

(500 liters per

m 3/ s

Also,

v cos f
A.

the area  Calling this component

is the component of the vector

S
v

perpendicular to the plane of

v(cid:2) ,

we can rewrite the volume ﬂow rate as

dV
dt

= v(cid:2) A

,

S
A

We can express the volume ﬂow rate more compactly by using the concept of
a vector quantity with magnitude  and a direction perpendicular to
vector area
A
the plane of the area we are describing. The vector area  describes both the size
of an area and its orientation in space. In terms of  we can write the volume ﬂow
rate of ﬂuid through the rectangle in Fig. 22.5b as a scalar (dot) product:

S
A

S
A

,

S

S # A

= v

dV
dt

Flux of a Uniform Electric Field
Using the analogy between electric ﬁeld and ﬂuid ﬂow, we now deﬁne electric
ﬂux in the same way as we have just deﬁned the volume ﬂow rate of a ﬂuid; we
simply replace the ﬂuid velocity  by the electric ﬁeld  The symbol that we use
for electric ﬂux is
is a reminder
E
perpendicular to a uniform
that this is electric ﬂux). Consider ﬁrst a ﬂat area
(Fig. 22.6a). We deﬁne the electric ﬂux through this area to be the
electric ﬁeld
product of the ﬁeld magnitude  and the area
A:

(the capital Greek letter phi; the subscript

£E

S
E

S
E

S
v

A

E

.

£E = EA
£E

in terms of the ﬁeld lines passing through
Increasing the area means that more lines of  pass through the area, increas-
and therefore

Roughly speaking, we can picture
A.
ing the ﬂux; a stronger ﬁeld means more closely spaced lines of
more lines per unit area, so again the ﬂux increases.

S
E

S
E

A

If the area

is ﬂat but not perpendicular to the ﬁeld

then fewer ﬁeld lines
pass through it. In this case the area that counts is the silhouette area that we see
in Fig. 22.6b and is equal
when looking in the direction of  This is the area
to
(compare to Fig. 22.5b). We generalize our deﬁnition of electric ﬂux
for a uniform electric ﬁeld to

A cos f

A(cid:2)

S
E

.

S
,
E

£E = EA cos f

(electric ﬂux for uniform

S
,
E

ﬂat surface)

(22.1)

is  the  component  of

S
E

perpendicular  to  the  area,  we  can  rewrite

E cos f
Since
Eq. (22.1) as

In terms of the vector area  perpendicular to the area, we can write the elec-
S
:
A

tric ﬂux as the scalar product of

£E = E(cid:2) A    (electric flux for uniform E
SA
E

and

S

S

S # A

S    (electric flux for uniform E

S

£E = E

, flat surface)

(22.2)

, flat surface)

(22.3)

S
E

1 N # m2>C.

pendicular to the area;

Equations (22.1), (22.2), and (22.3) express the electric ﬂux for a ﬂat surface and
a uniform electric ﬁeld in different but equivalent ways. The SI unit for electric
are per-
Note that if the area is edge-on to the ﬁeld,
ﬂux is
pendicular and the ﬂux is zero (Fig. 22.6c).

S
A
We can represent the direction of a vector area  by using a unit vector
stands for “normal.” Then
S
A

(22.4)
S
.
and  We
A
A surface  has  two  sides,  so  there  are  two  possible  directions  for
must always specify which direction we choose. In Section 22.1 we related the
charge  inside  a  closed surface  to  the  electric  ﬂux  through  the  surface.  With  a
to be outward, and we
closed surface we will always choose the direction of

(cid:2) AnN

and

per-

S
A

nN

nN

nN

nN

730

CHAPTER 22 Gauss’s Law

22.6 A ﬂat surface in a uniform electric ﬁeld. The electric ﬂux
and the area vector

S
.A

£E

through the surface equals the scalar product of the electric ﬁeld

S
E

S

S

(a) Surface is face-on to electric field:

S
• E and A are parallel (the angle between E
   and A is f 50).
•  The flux F

5 E • A 5 EA.

S S

S

E

(b) Surface is tilted from a face-on
(b)

   orientation by an angle f:
•  The angle between E and A is f.
•  The flux F

5 E • A 5 EA cos f.

S S

S

S

E

(c) Surface is edge-on to electric field:

S

S

S

• E and A are perpendicular (the angle
S
   between E and A is f 5 90°).
•  The flux F
E

5 E • A 5 EA cos 90° 5 0.

S S

S
E

A

f 50

S
A

S
E

f

A(cid:2)

A

S
A

f

S
E

S
A

f 590°

A

will speak of the ﬂux out of a closed surface. Thus what we called “outward elec-
tric  ﬂux”  in  Section  22.1  corresponds  to  a  positive value  of
and  what  we
called “inward electric ﬂux” corresponds to a negative value of

£E,
£E.

Flux of a Nonuniform Electric Field
What happens if the electric ﬁeld
A
over the area  ? Or what if
many small elements
and a vector area
and integrate the results to obtain the total ﬂux:

dA,
(cid:2) nN dA.

S
dA

S
E

A

is part of a curved surface? Then we divide

isn’t uniform but varies from point to point
into
perpendicular to it
We calculate the electric ﬂux through each element

each of which has a unit vector

nN

A

£E =

L

E cos f dA =

E(cid:2) dA =

L

L

S # dA
E

S

(general deﬁnition
of electric ﬂux)

(22.5)

S

E(cid:2)

S # dA
E

We call this integral the surface integral of the component
over the area, or
.
the  surface  integral  of
In  speciﬁc  problems,  one  form  of  the  integral  is
sometimes more convenient than another. Example 22.3 at the end of this section
illustrates the use of Eq. (22.5).
In Eq. (22.5) the electric ﬂux

is equal to the average value of the per-
pendicular component of the electric ﬁeld, multiplied by the area of the surface.
This is the same deﬁnition of electric ﬂux that we were led to in Section 22.1,
now expressed more mathematically. In the next section we will see the connec-
tion between the total electric ﬂux through any closed surface, no matter what its
shape, and the amount of charge enclosed within that surface.

1E(cid:2) dA

Example 22.1

Electric flux through a disk

S
E

30°

to a uniform electric field  of magnitude

nN
A disk of radius 0.10 m is oriented with its normal unit vector
2.0 * 103 N>C
at
(Fig. 22.7). (Since this isn’t a closed surface, it has no “inside”
nN
or  “outside.” That’s  why  we  have  to  specify  the  direction  of
in  the  figure.)  (a)  What  is  the  electric  flux  through  the  disk?
is
(b) What is the flux through the disk if it is turned so that
perpendicular to
is
(c) What is the flux through the disk if
S
parallel to E
?

S
?
E

nN
nN

22.7 The electric ﬂux
S
between its normal  and the electric ﬁeld E

nN

.

through a disk depends on the angle

£E

r 5 0.10 m

n^

30°

S
E

SOLUTION

IDENTIFY  and SET  UP: This  problem  is  about  a  ﬂat  surface  in  a
uniform electric ﬁeld, so we can apply the ideas of this section. We
calculate the electric ﬂux using Eq. (22.1).

EXECUTE: (a)  The  area  is
angle between

and

S
E

S
A

(cid:2) AnN

is
so from Eq. (22.1),
£E = EA cos f = 12.0 * 103 N>C210.0314 m221cos 30°2

f = 30°,

A = p10.10 m22 = 0.0314 m2

and  the

= 54 N # m2>C

(b) The normal to the disk is now perpendicular to
cos f = 0,

and £E = 0.

90°,

S
,
E

f =

so

Example 22.2

Electric flux through a cube

.

S
E

is in a region of uniform
An imaginary cubical surface of side
electric ﬁeld
Find the electric ﬂux through each face of the cube
and the total ﬂux through the cube when (a) it is oriented with two
of  its  faces  perpendicular  to
(Fig.  22.8a)  and  (b)  the  cube  is
turned by an angle  about a vertical axis (Fig. 22.8b).

S
E

L

u

SOLUTION

IDENTIFY  and SET  UP:  Since
is  uniform  and  each  of  the  six
faces  of  the  cube  is  ﬂat,  we  ﬁnd  the  ﬂux
through  each  face
using Eqs. (22.3) and (22.4). The total ﬂux through the cube is the
sum of the six individual ﬂuxes.

£Ei

S
E

EXECUTE: (a) Figure 22.8a shows the unit vectors
for
each face; each unit vector points outward from the cube’s closed
S
is 180°, the angle between E
and
surface. The angle between

S
E

nN

6

1

nN

nN
through

1

22.8 Electric ﬂux of a uniform ﬁeld
side

in two orientations.

L

S
E

through a cubical box of

(a)

^n3

^n5

^n4

^n1

^n6

r
E

^n2

(b)

^n3

^n5

^n2

r
E

90° 2 u

u

^n1

^n4

^n6

Example 22.3

Electric flux through a sphere

q = + 3.0 mC
A point  charge
r = 0.20 m
sphere  of  radius
Find the resulting electric ﬂux through the sphere.

is  surrounded  by  an  imaginary
centered  on  the  charge  (Fig.  22.9).

SOLUTION

IDENTIFY and SET UP: The surface is not ﬂat and the electric ﬁeld
is not uniform, so to calculate the electric ﬂux (our target variable)

22.2 Calculating Electric Flux

731

(c)  The  normal  to  the  disk  is  parallel  to

S
,
E

so

f = 0

and

cos f = 1:

£E = EA cos f = 12.0 * 103 N>C210.0314 m22112
= 63 N # m2>C

EVALUATE: As a check on our results, note that our answer to part
(b) is smaller than that to part (a), which is in turn smaller than that
to part (c). Is all this as it should be?

nN

2

is 0°, and the angle between

and
unit vectors is 90°. Each face of the cube has area
through the faces are

and each of the other four
L2,
so the ﬂuxes

S
E

S # nN
S # nN

1A = EL2cos 180° = - EL2

£E1 = E
£E2 = E
2A = EL2cos 0° = + EL2
£E3 = £E4 = £E5 = £E6 = EL2cos 90° = 0

The ﬂux is negative on face 1, where
and  positive  on  face  2,  where
total ﬂux through the cube is

S
E

S
E

is directed into the cube,
is  directed  out  of  the  cube. The

£E = £E1 + £E2 + £E3 + £E4 + £E5 + £E6
= - EL2 + EL2 + 0 + 0 + 0 + 0 = 0

(b)  The  ﬁeld

S
E

through them are negative;
ﬂuxes through them are positive. We ﬁnd

is  directed  into  faces  1  and  3,  so  the  ﬂuxes
is directed out of faces 2 and 4, so the

S
E

S # nN
S # nN
S # nN
S # nN

£E1 = E
£E2 = E
£E3 = E
£E4 = E
£E5 = £E6 = EL2cos 90° = 0

1A = EL2cos 1180° - u2 = - EL2cos u
2 A = + EL2cos u
3 A = EL2cos 190° + u2 = - EL2 sin u
4 A = EL2cos 190° - u2 = + EL2 sin u

The  total  ﬂux
through the surface of the cube is again zero.

£E = £E1 + £E2 + £E3 + £E4 + £E5 + £E6

EVALUATE:  We came to the same conclusion in our discussion of
Fig. 22.3c: There is zero net ﬂux of a uniform electric ﬁeld through
a closed surface that contains no electric charge.

we must use the general deﬁnition, Eq. (22.5). We use Eq. (22.5) to
calculate the electric ﬂux (our target variable). Because the sphere
is centered on the point charge, at any point on the spherical sur-
is directed out of the sphere perpendicular to the surface.
face,
E(cid:2) = E
The  positive  direction  for  both
and
E(cid:2)
dA
This
and the ﬂux through a surface element
greatly simpliﬁes the integral in Eq. (22.5).

is  outward,  so
S # dA
S
is
E

= E dA.

S
E

nN

Continued
