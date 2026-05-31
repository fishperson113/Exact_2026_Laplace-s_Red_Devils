GAUSS’S LAW

? This child acquires an electric charge by touching the charged metal sphere.

The charged hairs on the child’s head repel and stand out. If the child stands
inside a large, charged metal sphere, will her hair stand on end?

Often, there are both an easy way and a hard way to do a job; the easy way

may involve nothing more than using the right tools. In physics, an impor-
tant tool for simplifying problems is the symmetry properties of systems.
Many physical systems have symmetry; for example, a cylindrical body doesn’t
look  any  different  after  you’ve  rotated  it  around  its  axis,  and  a  charged  metal
sphere looks just the same after you’ve turned it about any axis through its center.
Gauss’s law is part of the key to using symmetry considerations to simplify
electric-ﬁeld calculations. For example, the ﬁeld of a straight-line or plane-sheet
charge distribution, which we derived in Section 21.5 using some fairly strenuous
integrations,  can  be  obtained  in  a  few  lines  with  the  help  of  Gauss’s  law.  But
Gauss’s law is more than just a way to make certain calculations easier. Indeed, it
is  a  fundamental  statement  about  the  relationship  between  electric  charges  and
electric ﬁelds. Among other things, Gauss’s law can help us understand how elec-
tric charge distributes itself over conducting bodies.

Here’s what Gauss’s law is all about. Given any general distribution of charge,
we surround it with an imaginary surface that encloses the charge. Then we look
at the electric ﬁeld at various points on this imaginary surface. Gauss’s law is a
relationship between the ﬁeld at all the points on the surface and the total charge
enclosed within the surface. This may sound like a rather indirect way of express-
ing things, but it turns out to be a tremendously useful relationship. Above and
beyond  its  use  as  a  calculational  tool,  Gauss’s  law  can  help  us  gain  deeper
insights into electric ﬁelds. We will make use of these insights repeatedly in the
next several chapters as we pursue our study of electromagnetism.

22.1 Charge and Electric Flux

In Chapter 21 we asked the question, “Given a charge distribution, what is the
electric ﬁeld produced by that distribution at a point  ?” We saw that the answer
could be found by representing the distribution as an assembly of point charges,

P

22

LEARNING GOALS

By studying this chapter, you will

learn:

• How you can determine the amount

of charge within a closed surface by

examining the electric field on the

surface.

• What is meant by electric flux, and

how to calculate it.

• How Gauss’s law relates the electric

flux through a closed surface to the

charge enclosed by the surface.

• How to use Gauss’s law to calculate

the electric ﬁeld due to a symmetric

charge distribution.

• Where the charge is located on a

charged conductor.

The discussion of Gauss’s law in this
section is based on and inspired by the
innovative ideas of Ruth W. Chabay and
Bruce A. Sherwood in Electric and
Magnetic Interactions (John Wiley &
Sons, 1994).

725

726

CHAPTER 22 Gauss’s Law

ActivPhysics 11.7: Electric Flux

22.1 How can you measure the charge
inside a box without opening it?

(a) A box containing an unknown amount of
charge

?

(b) Using a test charge outside the box to probe
the amount of charge inside the box

S
E

S
E

S
E

S
E

(cid:3)

Test charge q0

q

S
E

S
E

S
E

S
E

S
E

S
E
each of which produces an electric ﬁeld  given by Eq. (21.7). The total ﬁeld at
is then the vector sum of the ﬁelds due to all the point charges.

P

But there is an alternative relationship between charge distributions and elec-
tric ﬁelds. To discover this relationship, let’s stand the question of Chapter 21 on
its head and ask, “If the electric ﬁeld pattern is known in a given region, what can
we determine about the charge distribution in that region?”

Here’s an example. Consider the box shown in Fig. 22.1a, which may or may
not contain electric charge. We’ll imagine that the box is made of a material that
has no effect on any electric ﬁelds; it’s of the same breed as the massless rope and
the frictionless incline. Better still, let the box represent an imaginary surface that
may or may not enclose some charge. We’ll refer to the box as a closed surface
because it completely encloses a volume. How can you determine how much (if
any) electric charge lies within the box?

Knowing that a charge distribution produces an electric ﬁeld and that an elec-
around the
tric ﬁeld exerts a force on a test charge, you move a test charge
vicinity of the box. By measuring the force
experienced by the test charge at
different  positions,  you  make  a  three-dimensional  map  of  the  electric  ﬁeld
S
outside  the  box.  In  the  case  shown  in  Fig.  22.1b,  the  map  turns  out
E
to  be  the  same  as  that  of  the  electric  ﬁeld  produced  by  a  positive  point  charge
(Fig. 21.28a). From the details of the map, you can ﬁnd the exact value of the
point charge inside the box.

(cid:2) F

>q0

S
F

q0

S

To determine the contents of the box, we actually need to measure

only on
the surface of the box. In Fig. 22.2a there is a single positive point charge inside
the box, and in Fig. 22.2b there are two such charges. The ﬁeld patterns on the
surfaces  of  the  boxes  are  different  in  detail,  but  in  each  case  the  electric  ﬁeld
points out of the box. Figures 22.2c and 22.2d show cases with one and two neg-
are differ-
ative point charges, respectively, inside the box. Again, the details of
ent for the two cases, but the electric ﬁeld points into each box.

S
E

S
E

Electric Flux and Enclosed Charge
In Section 21.4 we mentioned the analogy between electric-ﬁeld vectors and the
velocity vectors of a ﬂuid in motion. This analogy can be helpful, even though an
electric  ﬁeld  does  not  actually  “ﬂow.”  Using  this  analogy,  in  Figs.  22.2a  and
22.2b,  in  which  the  electric  ﬁeld  vectors  point  out  of  the  surface,  we  say  that
there  is  an  outward electric  ﬂux. (The  word  “ﬂux”  comes  from  a  Latin  word
meaning “ﬂow.”) In Figs. 22.2c and 22.2d the
vectors point into the surface,
and the electric ﬂux is inward.

S
E

Figure 22.2 suggests a simple relationship: Positive charge inside the box goes
with  an  outward  electric  ﬂux  through  the  box’s  surface,  and  negative  charge
inside  goes  with  an  inward  electric  ﬂux.  What  happens  if  there  is  zero charge

22.2 The electric ﬁeld on the surface of boxes containing (a) a single positive point charge, (b) two positive point charges,
(c) a single negative point charge, or (d) two negative point charges.

(a) Positive charge inside box,
outward flux

(b) Positive charges inside box,
outward flux

(c) Negative charge inside box,
inward flux

(d) Negative charges inside box,
inward flux

S
E

(cid:2)q

S
E

(cid:2)q

(cid:2)q

S
E

(cid:4)q

S
E

2q

2q

22.1 Charge and Electric Flux

727

inside the box? In Fig. 22.3a the box is empty and
everywhere, so there is
no electric ﬂux into or out of the box. In Fig. 22.3b, one positive and one negative
point charge of equal magnitude are enclosed within the box, so the net charge
inside the box is zero. There is an electric ﬁeld, but it “ﬂows into” the box on half
of its surface and “ﬂows out of” the box on the other half. Hence there is no net
electric ﬂux into or out of the box.

S
E

(cid:2) 0

The box is again empty in Fig. 22.3c. However, there is charge present outside
the box; the box has been placed with one end parallel to a uniformly charged
inﬁnite sheet, which produces a uniform electric ﬁeld perpendicular to the sheet
S
(as  we  learned  in  Example  21.11  of  Section  21.5).  On  one  end  of  the  box,
E
S
points into the box; on the opposite end,  points out of the box; and on the sides,
E
S
is parallel to the surface and so points neither into nor out of the box. As in
E
Fig. 22.3b, the inward electric ﬂux on one part of the box exactly compensates for
the outward electric ﬂux on the other part. So in all of the cases shown in Fig. 22.3,
there is no net electric ﬂux through the surface of the box, and no net charge is
enclosed in the box.

Figures  22.2 and  22.3 demonstrate  a  connection  between  the  sign (positive,
negative, or zero) of the net charge enclosed by a closed surface and the sense
(outward, inward, or none) of the net electric ﬂux through the surface. There is
also a connection between the magnitude of the net charge inside the closed sur-
face and the strength of the net “ﬂow” of  over the surface. In both Figs. 22.4a
and 22.4b there is a single point charge inside the box, but in Fig. 22.4b the mag-
is everywhere twice as great in
nitude of the charge is twice as great, and so
magnitude as in Fig. 22.4a. If we keep in mind the ﬂuid-ﬂow analogy, this means
that  the  net  outward  electric  ﬂux  is  also  twice  as  great  in  Fig.  22.4b  as  in  Fig.
22.4a. This  suggests  that  the  net  electric  ﬂux  through  the  surface  of  the  box  is
directly proportional to the magnitude of the net charge enclosed by the box.

S
E

S
E

+q

1>r 2,

so the average magnitude of

This conclusion is independent of the size of the box. In Fig. 22.4c the point
charge
is enclosed by a box with twice the linear dimensions of the box in
Fig. 22.4a. The magnitude of the electric ﬁeld of a point charge decreases with
on each face of the
distance according to
large box in Fig. 22.4c is just  of the average magnitude on the corresponding
face in Fig. 22.4a. But each face of the large box has exactly four times the area
of the corresponding face of the small box. Hence the outward electric ﬂux is the
same for the two boxes if we deﬁne electric ﬂux as follows: For each face of the
box, take the product of the average perpendicular component of
and the area
of that face; then add up the results from all faces of the box. With this deﬁnition
the net electric ﬂux due to a single point charge inside the box is independent of
the size of the box and depends only on the net charge inside the box.

S
E

S
E

1
4

22.3 Three cases in which there is zero net charge inside a box and no net electric ﬂux through the surface of the box. (a) An empty
S
E
box with
uniform electric ﬁeld.

(b) A box containing one positive and one equal-magnitude negative point charge. (c) An empty box immersed in a

(cid:2) 0.

(a) No charge inside box,
zero flux

(b) Zero net charge inside box,
inward flux cancels outward flux.

(c) No charge inside box,
inward flux cancels outward flux.

S

E 5 0

S
E

1q

2q

1s

Uniformly
charged
sheet

S
E
