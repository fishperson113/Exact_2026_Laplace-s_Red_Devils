C H A

P

T

E

R

2

6

Current and Resistance

26-1 ELECTRIC CURRENT

Learning Objectives
After reading this module, you should be able to . . .

26.01 Apply the definition of current as the rate at which

26.03 Identify a junction in a circuit and apply the fact

charge moves through a point, including solving for the
amount of charge that passes the point in a given time
interval.

26.02 Identify that current is normally due to the motion of
conduction electrons that are driven by electric fields
(such as those set up in a wire by a battery).

that (due to conservation of charge) the total current
into a junction must equal the total current out of the
junction.

26.04 Explain how current arrows are drawn in a schematic
diagram of a circuit, and identify that the arrows are not
vectors.

Key Ideas
● An electric current i in a conductor is defined by

i !

dq
dt

,

where dq is the amount of positive charge that passes in
time dt.

● By convention, the direction of electric current is taken
as the direction in which positive charge carriers would
move even though (normally) only conduction electrons
can move.

What Is Physics?
In  the  last  five  chapters  we  discussed  electrostatics — the  physics  of  stationary
charges. In this and the next chapter, we discuss the physics of electric currents —
that is, charges in motion.

Examples of electric currents abound and involve many professions. Mete-
orologists are concerned with lightning and with the less dramatic slow flow of
charge through the atmosphere. Biologists, physiologists, and engineers work-
ing in medical technology are concerned with the nerve currents that control
muscles  and  especially  with  how  those  currents  can  be  reestablished  after
spinal cord injuries. Electrical engineers are concerned with countless electri-
cal  systems, such  as  power  systems, lightning  protection  systems, information
storage  systems, and  music  systems. Space  engineers  monitor  and  study  the
flow of charged particles from our Sun because that flow can wipe out telecom-
munication  systems  in  orbit  and  even  power  transmission  systems  on  the
ground. In  addition  to  such  scholarly  work, almost  every  aspect  of  daily  life
now depends on information carried by electric currents, from stock trades to
ATM transfers and from video entertainment to social networking.

In this chapter we discuss the basic physics of electric currents and why they
can be established in some materials but not in others. We begin with the mean-
ing of electric current.

745

746

CHAPTE R  26 CU R R E NT  AN D  R ESISTANCE

Electric Current
Although  an  electric  current  is  a  stream  of  moving  charges, not  all  moving
charges constitute an electric current. If there is to be an electric current through
a  given  surface, there  must  be  a  net  flow  of  charge  through  that  surface. Two
examples clarify our meaning.

1. The free electrons (conduction electrons) in an isolated length of copper wire are
in random motion at speeds of the order of 106 m/s. If you pass a hypothetical
plane through such a wire, conduction electrons pass through it in both directions
at the rate of many billions per second—but there is no net transport of charge
and thus no current through the wire. However, if you connect the ends of the wire
to a battery, you slightly bias the flow in one direction, with the result that there
now is a net transport of charge and thus an electric current through the wire.
2. The  flow  of  water  through  a  garden  hose  represents  the  directed  flow  of
positive charge (the protons in the water molecules) at a rate of perhaps sev-
eral million coulombs per second. There is no net transport of charge, however,
because there is a parallel flow of negative charge (the electrons in the water
molecules) of exactly the same amount moving in exactly the same direction.

In this chapter we restrict ourselves largely to the study — within the frame-
work  of  classical  physics — of  steady currents  of  conduction  electrons moving
through metallic conductors such as copper wires.

As  Fig. 26-1a reminds  us, any  isolated  conducting  loop — regardless  of
whether it has an excess charge — is all at the same potential. No electric field can
exist within it or along its surface. Although conduction electrons are available,
no net electric force acts on them and thus there is no current.

If, as in Fig. 26-1b, we insert a battery in the loop, the conducting loop is no
longer at a single potential. Electric fields act inside the material making up the
loop, exerting forces on the conduction electrons, causing them to move and thus
establishing a current. After a very short time, the electron flow reaches a con-
stant value and the current is in its steady state (it does not vary with time).

Figure 26-2 shows a section of a conductor, part of a conducting loop in which
current  has  been  established. If  charge  dq passes  through  a  hypothetical  plane
(such as aa-) in time dt, then the current i through that plane is defined as

i !

dq
dt

(definition of current).

(26-1)

We  can  find  the  charge  that  passes  through  the  plane  in  a  time  interval

extending from 0 to t by integration:

q ! " dq ! "t

0

i dt,

(26-2)

in which the current i may vary with time.

Under steady-state conditions, the current is the same for planes aa-, bb-, and
cc- and  indeed  for  all  planes  that  pass  completely  through  the  conductor, no
matter what their location or orientation. This follows from the fact that charge is
conserved. Under  the  steady-state  conditions  assumed  here, an  electron  must
pass through plane  aa- for every electron that passes through plane  cc-. In the
same  way, if  we  have  a  steady  flow  of  water  through  a  garden  hose, a  drop  of
water must leave the nozzle for every drop that enters the hose at the other end.
The amount of water in the hose is a conserved quantity.

The SI unit for current is the coulomb per second, or the ampere (A), which

is an SI base unit:

1 ampere ! 1 A ! 1 coulomb per second ! 1 C/s.

The formal definition of the ampere is discussed in Chapter 29.

(a )

i

i

Battery

i

i

+

–

i

(b )

Figure 26-1 (a) A loop of copper in electro-
static equilibrium.The entire loop is at a
single potential, and the electric field is zero
at all points inside the copper. (b) Adding a
battery imposes an electric potential differ-
ence between the ends of the loop that are
connected to the terminals of the battery.
The battery thus produces an electric field
within the loop, from terminal to terminal,
and the field causes charges to move
around the loop.This movement of charges
is a current i.

The current is the same in
any cross section.

a

b

c

i

i

c'

a'

b'

Figure 26-2 The current i through the con-
ductor has the same value at planes aa-,
bb-, and cc-.

26-1 E LECTR IC  CU R R E NT

747

The current into the
junction must equal
the current out
(charge is conserved).

i 0

i 0

i 1

a

i 2

(a )

i 2

i 1

a

(b )
%!
i1

Figure 26-3 The relation i0
junction a no matter what the orientation
in space of the three wires. Currents are
scalars, not vectors.

i2 is true at

Current, as defined by Eq. 26-1, is a scalar because both charge and time in
that equation are scalars. Yet, as in Fig. 26-1b, we often represent a current with
an arrow to indicate that charge is moving. Such arrows are not vectors, however,
and  they  do  not  require  vector  addition. Figure  26-3a shows  a  conductor  with
current i0 splitting at a junction into two branches. Because charge is conserved,
the magnitudes of the currents in the branches must add to yield the magnitude
of the current in the original conductor, so that

i0 ! i1 % i2.

(26-3)

As Fig. 26-3b suggests, bending or reorienting the wires in space does not change
the validity of Eq. 26-3. Current arrows show only a direction (or sense) of flow
along a conductor, not a direction in space.

The Directions of Currents
In  Fig. 26-1b we  drew  the  current  arrows  in  the  direction  in  which  positively
charged particles would be forced to move through the loop by the electric field.
Such positive charge carriers, as they are often called, would move away from the
positive  battery  terminal  and  toward  the  negative  terminal. Actually, the  charge
carriers  in  the  copper  loop  of  Fig. 26-1b are  electrons  and  thus  are  negatively
charged.The electric field forces them to move in the direction opposite the current
arrows, from the negative terminal to the positive terminal. For historical reasons,
however, we use the following convention:

A current arrow is drawn in the direction in which positive charge carriers would
move, even if the actual charge carriers are negative and move in the opposite
direction.

We can use this convention because in most situations, the assumed motion
of  positive  charge  carriers  in  one  direction  has  the  same  effect  as  the  actual
motion of negative charge carriers in the opposite direction. (When the effect is
not the same, we shall drop the convention and describe the actual motion.)

Checkpoint 1

The figure here shows a portion of a circuit.
What are the magnitude and direction of the
current i in the lower right-hand wire?

2 A

1 A

3 A

4 A

2 A

2 A

i

Sample Problem 26.01 Current is the rate at which charge passes a point

Water  flows  through  a  garden  hose  at  a  volume  flow  rate
dV/dt of 450 cm3/s. What is the current of negative charge?

Calculations: We can write the current in terms of the num-
ber of molecules that pass through such a plane per second as

KEY IDEAS

The  current  i of  negative  charge  is  due  to  the  electrons  in
the water molecules moving through the hose. The current is
the  rate  at  which  that  negative  charge  passes through  any
plane that cuts completely across the hose.

or

i ! # charge

electron$#electrons

molecule$#molecules
second $

per

per

per

i ! (e)(10)

dN
dt

.
