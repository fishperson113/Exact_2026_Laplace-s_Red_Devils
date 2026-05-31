If the field varies with position,
we must integrate to get the
flux through the loop.

y

H

dA

B

dx

W

We start with a strip
so thin that we can
approximate the field as
being uniform within it.

x

Figure 30-7 A closed conducting loop, of width W and height H, lies
in a nonuniform, varying magnetic field that points directly into the
page. To apply Faraday’s law, we use the vertical strip of height H,
width dx, and area dA.

any time t. However, because B is not uniform over the
area enclosed by the loop, we cannot use Eq. 30-2 (0B !
BA) to find that expression; instead we must use Eq. 30-1
:
(0B ! " B

:
! dA
)

.

:
B

Calculations: In Fig. 30-7,
is perpendicular to the plane
of  the  loop  (and  hence  parallel  to  the  differential  area
); so  the  dot  product  in  Eq. 30-1  gives  B  dA.
vector
Because the magnetic field varies with the coordinate x but
not with the coordinate y, we can take the differential area

:
dA

30-2 I N DUCTION  AN D  E N E RGY  TRANSFE RS

871

dA to be the area of a vertical strip of height H and width dx
(as  shown  in  Fig. 30-7). Then  dA ! H  dx, and  the  flux
through the loop is

0B ! " B

:

:
! dA

! " B dA ! " BH dx ! " 4t 2x2H dx.

Treating t as a constant for this integration and inserting the
integration limits x ! 0 and x ! 3.0 m, we obtain

0B ! 4t 2H "3.0

0

x2 dx ! 4t 2H ( x3

3 )0

3.0

! 72t 2,

where we have substituted H ! 2.0 m and 0B is in webers.
Now we can use Faraday’s law to find the magnitude of # at
any time t:

# !

d 0B
dt

!

d(72t 2)
dt

! 144t,

in which # is in volts. At t ! 0.10 s,

# ! (144 V/s)(0.10 s) % 14 V.

(Answer)

:
B

The  flux  of

through  the  loop  is  into  the  page  in
Fig. 30-7  and  is  increasing  in  magnitude  because  B is  in-
creasing in magnitude with time. By Lenz’s law, the field Bind
of  the  induced  current  opposes  this  increase  and  so  is  di-
rected out of the page. The curled – straight right-hand rule
in Fig. 30-5a then tells us that the induced current is counter-
clockwise around the loop, and thus so is the induced emf #.

Additional examples, video, and practice available at WileyPLUS

30-2 INDUCTION AND ENERGY TRANSFERS

Learning Objectives
After reading this module, you should be able to . . .

30.13 For a conducting loop pulled into or out of a magnetic
field, calculate the rate at which energy is transferred to
thermal energy.

30.14 Apply the relationship between an induced current and

the rate at which it produces thermal energy.

30.15 Describe eddy currents.

Key Idea
● The induction of a current by a changing flux means that energy is being transferred to that current. The energy can then be
transferred to other forms, such as thermal energy.

Induction and Energy Transfers
By Lenz’s law, whether you move the magnet toward or away from the loop in
Fig. 30-1, a magnetic force resists the motion, requiring your applied force to do
positive work. At the same time, thermal energy is produced in the material of
the  loop  because  of  the  material’s  electrical  resistance  to  the  current  that  is
induced by the motion. The energy you transfer to the closed loop & magnet sys-
tem via your applied force ends up in this thermal energy. (For now, we neglect
energy that is radiated away from the loop as electromagnetic waves during the

872

CHAPTE R  30 I N DUCTION  AN D  I N DUCTANCE

induction.) The faster you move the magnet, the more rapidly your applied force
does work and the greater the rate at which your energy is transferred to thermal
energy in the loop; that is, the power of the transfer is greater.

Regardless of how current is induced in a loop, energy is always transferred
to thermal energy during the process because of the electrical resistance of the
loop (unless the loop is superconducting). For example, in Fig. 30-2, when switch S
is closed and a current is briefly induced in the left-hand loop, energy is trans-
ferred from the battery to thermal energy in that loop.

Figure 30-8 shows another situation involving induced current. A rectangular
loop of wire of width L has one end in a uniform external magnetic field that is
directed perpendicularly into the plane of the loop. This field may be produced,
for  example, by  a  large  electromagnet. The  dashed  lines  in  Fig. 30-8  show  the
assumed  limits  of  the  magnetic  field; the  fringing  of  the  field  at  its  edges  is
neglected. You are to pull this loop to the right at a constant velocity

v:
.

Flux Change. The situation of Fig. 30-8 does not differ in any essential way
from that of Fig. 30-1. In each case a magnetic field and a conducting loop are in
relative  motion; in  each  case  the  flux  of  the  field  through  the  loop  is  changing
with time. It is true that in Fig. 30-1 the flux is changing because
is changing and
in Fig. 30-8 the flux is changing because the area of the loop still in the magnetic
field is changing, but that difference is not important. The important difference
between the two arrangements is that the arrangement of Fig. 30-8 makes calcu-
lations easier. Let us now calculate the rate at which you do mechanical work as
you pull steadily on the loop in Fig. 30-8.

:
B

Rate of Work. As you will see, to pull the loop at a constant velocity

, you
must apply a constant force
to the loop because a magnetic force of equal mag-
nitude but opposite direction acts on the loop to oppose you. From Eq. 7-48, the
rate at which you do work — that is, the power — is then

:
F

v:

P ! Fv,

(30-6)

where F is the magnitude of your force. We wish to find an expression for P in
terms  of  the  magnitude  B of  the  magnetic  field  and  the  characteristics  of  the
loop — namely, its resistance R to current and its dimension L.

As you move the loop to the right in Fig. 30-8, the portion of its area within
the magnetic field decreases. Thus, the flux through the loop also decreases and,
according to Faraday’s law, a current is produced in the loop. It is the presence of
this current that causes the force that opposes your pull.

Induced emf. To find the current, we first apply Faraday’s law. When x is the
length of the loop still in the magnetic field, the area of the loop still in the field is
Lx. Then from Eq. 30-2, the magnitude of the flux through the loop is

0B ! BA ! BLx.

(30-7)

x

F2

B

F1

F3

b

Decreasing the area
decreases the flux,
inducing a current.

i

L

v

Figure 30-8 You pull a closed conduct-
ing loop out of a magnetic field at
v:
constant velocity . While the loop
is moving, a clockwise current i is
induced in the loop, and the loop seg-
ments still within the magnetic field
:
F
experience forces
,
1

:
F
, and
2

:
.F
3

30-2 I N DUCTION  AN D  E N E RGY  TRANSFE RS

873

i

i

R

Figure 30-9 A circuit diagram for the loop of
Fig. 30-8 while the loop is moving.

As x decreases, the  flux  decreases. Faraday’s  law  tells  us  that  with  this  flux
decrease, an emf is induced in the loop. Dropping the minus sign in Eq. 30-4 and
using Eq. 30-7, we can write the magnitude of this emf as

# !

d0B
dt

!

d
dt

BLx ! BL

dx
dt

! BLv,

(30-8)

in which we have replaced dx/dt with v, the speed at which the loop moves.

Figure 30-9 shows the loop as a circuit: induced emf # is represented on the
left, and  the  collective  resistance  R of  the  loop  is  represented  on  the  right.
The direction  of  the  induced  current  i is  obtained  with  a  right-hand  rule  as  in
Fig. 30-5b for decreasing flux; applying the rule tells us that the current must be
clockwise, and # must have the same direction.

Induced Current. To find the magnitude of the induced current, we cannot
apply the loop rule for potential differences in a circuit because, as you will see in
Module  30-3, we  cannot  define  a  potential  difference  for  an  induced  emf.
However, we can apply the equation i ! #/R. With Eq. 30-8, this becomes

i !

BLv
R

.

(30-9)

Because three segments of the loop in Fig. 30-8 carry this current through the
magnetic field, sideways deflecting forces act on those segments. From Eq. 28-26
we know that such a deflecting force is, in general notation,

:
:
d ! iL
F

:
$ B
.

(30-10)

:
F
1,

:
F
2,

and

In  Fig. 30-8, the  deflecting  forces  acting  on  the  three  segments  of  the  loop  are
:
:
F
F
marked
2
3
:
F
, which  is  directed
are equal  in  magnitude  and  cancel. This  leaves  only  force
1
:
:
! %F
F
.
opposite your force  on the loop and thus is the force opposing you. So,
1
and  noting  that  the  angle

:
F
. Note, however, that  from  the  symmetry, forces
3

Using  Eq. 30-10  to  obtain  the  magnitude  of

and

:
F

:
F
1
for the left segment is 90 , we write

"

:
L

between  and the length vector

:
B

Substituting Eq. 30-9 for i in Eq. 30-11 then gives us

F ! F1 ! iLB sin 90" ! iLB.

(30-11)

F !

B2L2v
R

.

(30-12)

Because B, L, and R are constants, the speed v at which you move the loop is con-
stant if the magnitude F of the force you apply to the loop is also constant.

Rate  of Work. By  substituting  Eq. 30-12  into  Eq. 30-6, we  find  the  rate  at

which you do work on the loop as you pull it from the magnetic field:

P ! Fv !

B2L2v2
R

(rate of doing work).

(30-13)

Thermal  Energy. To  complete  our  analysis, let  us  find  the  rate  at  which
thermal  energy  appears  in  the  loop  as  you  pull  it  along  at  constant  speed. We
calculate it from Eq. 26-27,

P ! i 2R.

(30-14)

Substituting for i from Eq. 30-9, we find

2

P ! # BLv
R $

R !

B2L2v2
R

(thermal energy rate),

(30-15)

which  is  exactly  equal  to  the  rate  at  which  you  are  doing  work  on  the  loop
(Eq. 30-13). Thus, the work that you do in pulling the loop through the magnetic
field appears as thermal energy in the loop.
