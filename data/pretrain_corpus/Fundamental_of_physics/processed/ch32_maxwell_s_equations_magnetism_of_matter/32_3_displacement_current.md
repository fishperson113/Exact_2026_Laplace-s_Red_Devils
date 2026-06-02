946

CHAPTE R  32 MAXWE LL’S  EQUATIONS;  MAG N ETISM  OF  MATTE R

This equation tells us that, inside the capacitor, B increases
linearly with increased radial distance r, from 0 at the cen-
tral axis to a maximum value at plate radius R.

loop in the electric field is not the full area pr 2 of the loop.
Rather, A is only the plate area pR2.

Substituting pR2 for A in Eq. 32-7 and solving the result

(b) Evaluate the field magnitude B for r ! R/5 ! 11.0 mm
and dE/dt ! 1.50 & 1012 V/m (s.

Calculation: From the answer to (a), we have

B !

m0´0r

dE
dt

1
2
! 1
2 (4p & 10’7 T ( m /A)(8.85 & 10’12 C2/N ( m2)
& (11.0 & 10’3 m)(1.50 & 1012 V/m ( s)

! 9.18 & 10’8 T.

(Answer)

(c) Derive an expression for the induced magnetic field for
the case r 4 R.

Calculation: Our procedure is the same as in (a) except we
now  use  an Amperian  loop  with  a  radius  r that  is  greater
than the plate radius R, to evaluate B outside the capacitor.
Evaluating the left and right sides of Eq. 32-6 again leads to
Eq. 32-7. However, we then need this subtle point: The elec-
tric  field  exists  only  between  the  plates, not  outside  the
plates. Thus, the  area  A that  is  encircled  by  the Amperian

for B give us, for r 4 R,

B !

m0´0R2
2r

dE
dt

.

(Answer)

(32-9)

This  equation  tells  us  that, outside  the  capacitor, B
decreases with increased radial distance r, from a maximum
value at the plate edges (where r ! R). By substituting r !
R into Eqs. 32-8 and 32-9, you can show that these equations
are consistent; that is, they give the same maximum value of
B at the plate radius.

The magnitude of the induced magnetic field calculated in
(b) is so small that it can scarcely be measured with simple ap-
paratus. This is in sharp contrast to the magnitudes of induced
electric  fields  (Faraday’s  law), which  can  be  measured  easily.
This  experimental  difference  exists  partly  because  induced
emfs can easily be multiplied by using a coil of many turns. No
technique  of  comparable  simplicity  exists  for  multiplying  in-
duced magnetic fields. In any case, the experiment suggested
by this sample problem has been done, and the presence of the
induced magnetic fields has been verified quantitatively.

Additional examples, video, and practice available at WileyPLUS

32-3 DISPLACEMENT CURRENT

Learning Objectives
After reading this module, you should be able to . . .

32.08 Identify that in the Ampere–Maxwell law, the contribution
to the induced magnetic field by the changing electric flux
can be attributed to a fictitious current (“displacement cur-
rent”) to simplify the expression.

32.09 Identify that in a capacitor that is being charged or

discharged, a displacement current is said to be spread uni-
formly over the plate area, from one plate to the other.

current and identify that the displacement current exists only
when the electric field within the capacitor is changing.
32.12 Mimic the equations for the magnetic field inside and
outside a wire with real current to write (and apply) the
equations for the magnetic field inside and outside a
region of displacement current.

32.13 Apply the Ampere–Maxwell law to calculate the

32.10 Apply the relationship between the rate of change of an

magnetic field of a real current and a displacement current.

electric flux and the associated displacement current.

32.11 For a charging or discharging capacitor, relate

the amount of displacement current to the amount of actual

32.14 For a charging or discharging capacitor with parallel
circular plates, draw the magnetic field lines due to the
displacement current.

32.15 List Maxwell’s equations and the purpose of each.

Key Ideas
● We define the fictitious displacement current due to a
changing electric field as

id ! ´0

d#E
dt

.

● The Ampere–Maxwell law then becomes

:

, B

! d s: ! m0id,enc $ m0ienc

(Ampere – Maxwell law),

where id,enc is the displacement current encircled by the
integration loop.

● The idea of a displacement current allows us to retain the
notion of continuity of current through a capacitor. However,
displacement current is not a transfer of charge.

● Maxwell’s equations, displayed in Table 32-1, summarize
electromagnetism and form its foundation, including optics.

32-3 DISPL ACE M E NT  CU R R E NT

947

Displacement Current
If you compare the two terms on the right side of Eq. 32-5, you will see that the
product ´0(d#E/dt) must have the dimension of a current. In fact, that product has
been treated as being a fictitious current called the displacement current id:

id ! ´0

d#E
dt

(displacement current).

(32-10)

“Displacement” is poorly chosen in that nothing is being displaced, but we are
stuck with the word. Nevertheless, we can now rewrite Eq. 32-5 as

:

, B

! d s: ! m0 id,enc $ m0 ienc

(Ampere – Maxwell law),

(32-11)

in which id,enc is the displacement current that is encircled by the integration loop.
Let  us  again  focus  on  a  charging  capacitor  with  circular  plates, as  in
:
E
Fig. 32-7a. The real current i that is charging the plates changes the electric field
between the plates. The fictitious displacement current  id between the plates is
associated with that changing field

. Let us relate these two currents.

:
E

The charge q on the plates at any time is related to the magnitude E of the

field between the plates at that time and the plate area A by Eq. 25-4:

To get the real current i, we differentiate Eq. 32-12 with respect to time, finding

q ! ´0AE.

(32-12)

dq
dt

! i ! ´0 A

dE
dt

.

(32-13)

To get the displacement current id, we can use Eq. 32-10. Assuming that the elec-
between the two plates is uniform (we neglect any fringing), we can
tric field

:
E

Before charging, there
is no magnetic field.

(a)

During charging, the
right-hand rule works for both
the real and fictional currents.

A

During charging, magnetic
field is created by both
the real and fictional currents.

(b)

i

+

B

id

B

i

–

B

After charging, there
is no magnetic field.

Figure 32-7 (a) Before and (d) after the plates
are charged, there is no magnetic field. (b)
During the charging, magnetic field is created
by both the real current and the (fictional)
displacement current. (c) The same right-
hand rule works for both currents to give the
direction of the magnetic field.

(c)

i

+

i

–

(d)

+

–

B

B

B

948

CHAPTE R  32 MAXWE LL’S  EQUATIONS;  MAG N ETISM  OF  MATTE R

replace the electric flux #E in that equation with EA. Then Eq. 32-10 becomes

id ! ´0

d#E
dt

! ´0

d(EA)
dt

! ´0A

dE
dt

.

(32-14)

Same Value. Comparing Eqs. 32-13 and 32-14, we see that the real current i
charging  the  capacitor  and  the  fictitious  displacement  current  id between  the
plates have the same value:

id ! i

(displacement current in a capacitor).

(32-15)

Thus, we can consider the fictitious displacement current id to be simply a con-
tinuation  of  the  real  current  i from  one  plate, across  the  capacitor  gap, to  the
other  plate. Because  the  electric  field  is  uniformly  spread  over  the  plates,
the same  is  true  of  this  fictitious  displacement  current  id, as  suggested  by  the
spread of current arrows in Fig. 32-7b. Although no charge actually moves across
the  gap  between  the  plates, the  idea  of  the  fictitious  current  id can  help  us  to
quickly find the direction and magnitude of an induced magnetic field, as follows.

Finding the Induced Magnetic Field
In Chapter 29 we found the direction of the magnetic field produced by a real
current i by using the right-hand rule of Fig. 29-5. We can apply the same rule to
find the direction of an induced magnetic field produced by a fictitious displace-
ment current id, as is shown in the center of Fig. 32-7c for a capacitor.

We  can  also  use  id to  find  the  magnitude  of  the  magnetic  field  induced  by
a charging capacitor with parallel circular plates of radius R. We simply consider
the space between the plates to be an imaginary circular wire of radius R carrying
the  imaginary  current  id. Then, from  Eq. 29-20, the  magnitude  of  the  magnetic
field at a point inside the capacitor at radius r from the center is

B ! # m0 id

2pR2 $r

(inside a circular capacitor).

(32-16)

Similarly, from Eq. 29-17, the magnitude of the magnetic field at a point outside
the capacitor at radius r is

B !

m0 id
2pr

(outside a circular capacitor).

(32-17)

Checkpoint 3

The figure is a view of one plate of a parallel-plate
capacitor from within the capacitor. The dashed lines
show four integration paths (path b follows the edge of
the plate). Rank the paths according to the magnitude
of
the capacitor, greatest first.

along the paths during the discharging of

:
- B

! d s:

c

a

b

d

Sample Problem 32.02 Treating a changing electric field as a displacement current

A  circular  parallel-plate  capacitor  with  plate  radius  R is
being charged with a current i.

KEY IDEA

:
- B
(a) Between the plates, what is the magnitude of
terms of m0 and i, at a radius r R/5 from their center?

!

! d s:

, in

A magnetic field can be set up by a current and by induction
due  to  a  changing  electric  flux  (Eq. 32-5). Between  the
plates in Fig. 32-5, the current is zero and we can account for

the changing electric flux with a fictitious displacement cur-
! d s:
rent id. Then  integral
is  given  by  Eq. 32-11, but
because  there  is  no  real  current  i between  the  capacitor
plates, the equation reduces to

:
- B

:

, B

! d s: ! m0id,enc.

(32-18)

!

Calculations: Because  we  want  to  evaluate
at
radius r R/5 (within the capacitor), the integration loop en-
circles only a portion id,enc of the total displacement current id.
Let’s  assume  that  id is  uniformly  spread  over  the  full plate
area. Then the portion of the displacement current encircled
by the loop is proportional to the area encircled by the loop:

! d s:

:
- B

current id,enc

#encircled displacement
#total displacement
$

current id

$

!

encircled area p r 2
full plate area pR2 .

This gives us

id,enc ! id

pr2
pR2 .

Substituting this into Eq. 32-18, we obtain

:

, B

! d s: ! m0 id

pr2
pR2 .

(32-19)

Now  substituting  id ! i (from  Eq. 32-15)  and  r ! R/5  into
Eq. 32-19 leads to

:

, B

! d s: ! m0i

(R/5)2
R2 !

m0i
25

.

(Answer)

32-3 DISPL ACE M E NT  CU R R E NT

949

(b) In terms of the maximum induced magnetic field, what is
the  magnitude  of  the  magnetic  field  induced  at  r ! R/5,
inside the capacitor?

KEY IDEA

Because  the  capacitor  has  parallel  circular  plates, we  can
treat the space between the plates as an imaginary wire of
radius R carrying the imaginary current id. Then we can use
Eq. 32-16 to find the induced magnetic field magnitude B at
any point inside the capacitor.

Calculations: At r ! R/5, Eq. 32-16 yields

B ! # m0id

2pR2 $r !

m0id(R/5)

2pR2 !

m0id
10pR

.

(32-20)

From Eq. 32-16, the maximum field magnitude Bmax within
the capacitor occurs at r ! R. It is

Bmax ! # m0id

2pR2 $R !

m0id
2pR

.

(32-21)

Dividing Eq. 32-20 by Eq. 32-21 and rearranging the result,
we find that the field magnitude at r ! R/5 is

B ! 1

5Bmax.

(Answer)

We should be able to obtain this result with a little rea-
soning and less work. Equation 32-16 tells us that inside the
capacitor, B increases linearly with r. Therefore, a point  the
distance out to the full radius R of the plates, where  Bmax
1
5Bmax
occurs, should have a field B that is
.

1
5

Additional examples, video, and practice available at WileyPLUS

Maxwell’s Equations
Equation 32-5 is the last of the four fundamental equations of electromagnetism,
called Maxwell’s  equations and  displayed  in  Table  32-1. These  four  equations

Table 32-1 Maxwell’s Equationsa

Name

Gauss’ law for electricity

Gauss’ law for magnetism

Faraday’s law

Ampere – Maxwell law

Equation

:
! dA

! qenc/´0

:
! dA

! 0

! d s: ! ’

d#B
dt

Relates net electric flux to net enclosed electric charge

Relates net magnetic flux to net enclosed magnetic charge

Relates induced electric field to changing magnetic flux

! d s: ! m0´0

d#E
dt

$ m0ienc

Relates induced magnetic field to changing electric flux

and to current

:

:

, E
, B
, E
, B

:

:

aWritten on the assumption that no dielectric or magnetic materials are present.
