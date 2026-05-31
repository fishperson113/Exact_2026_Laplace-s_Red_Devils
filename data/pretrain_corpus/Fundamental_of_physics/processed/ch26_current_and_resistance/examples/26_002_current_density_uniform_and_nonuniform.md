Sample Problem 26.02
Current density, uniform and nonuniform
(a) The current density in a cylindrical wire of radius R
2.0 mm is uniform across a cross section of the wire and is J !
2.0 $ 105 A/m2.What is the current through the outer portion
of the wire between radial distances R/2 and R (Fig.26-6a)?
KEY IDEA
Because the current density is uniform across the cross
section, the current density J, the current i, and the cross-
sectional area A are related by Eq. 26-5 (J ! i/A).
Calculations: We want only the current through a reduced
cross-sectional area A- of the wire (rather than the entire
!
area), where
! 3p
4  (0.0020 m)2 ! 9.424 $ 10 #6 m2.
A- ! pR2 # p #
R
2 $
2
! p #
3R2
4 $
So, we rewrite Eq. 26-5 as
i ! JA-
and then substitute the data to find
(Answer)
! 1.9 A.
i ! (2.0 $ 10 5 A/m2)(9.424 $ 10#6 m2)

751
26-2 CURRENT DENSITY
R/2
R
(a)
R
(e)
R/2
(d)
(b)
dr
(c)
We want the current in the area 
between these two radii.
Our job is to sum the current in 
all rings from this smallest one ...
... to this largest one.
Its area is the product of the 
circumference and the width.
The current within the ring is 
the product of the current density
and the ring’s area.
If the current is nonuniform, we start with a 
ring that is so thin that we can approximate 
the current density as being uniform within it.
Figure 26-6 (a) Cross section of a wire of
radius R. If the current density is uni-
form, the current is just the product of
the current density and the area. (b)-(e)
If the current is nonuniform, we must
first find the current through a thin ring
and then sum (via integration) the cur-
rents in all such rings in the given area.
A
(b) Suppose, instead, that the current density through a
cross section varies with radial distance r as J ! ar2, in which
a ! 3.0 $ 10 11 A/m4 and r is in meters. What now is the
current through the same outer portion of the wire?
KEY IDEA
Because the current density is not uniform across a cross
section of the wire, we must resort to Eq. 26-4 
and integrate the current density over the portion of the
wire from r ! R/2 to r ! R.
Calculations: The current density vector 
(along the
wire’s length) and the differential area vector 
(per-
pendicular to a cross section of the wire) have the same
direction.Thus,
J
: " dA
: ! J dA cos 0 ! J dA.
dA
:
J
:
(i ! " J
: " dA
:)
We need to replace the differential area dA with some-
thing we can actually integrate between the limits r ! R/2
and r ! R.The simplest replacement (because J is given as a
function of r) is the area 2pr dr of a thin ring of circumfer-
ence 2pr and width dr (Fig. 26-6b). We can then integrate
with r as the variable of integration. Equation 26-4 then
gives us
(Answer)
! 15
32 p(3.0 $ 10 11 A/m4)(0.0020 m)4 ! 7.1 A.
! 2pa(
r4
4 )
R
R/2
! pa
2 (R4 # R4
16) ! 15
32  paR4
!"
R
R/2
ar2 2pr dr ! 2pa"
R
R/2
r3 dr
i !"J
: " dA
: !" J dA
Additional examples, video, and practice available at WileyPLUS

752
CHAPTER 26
CURRENT AND RESISTANCE
Taking copper’s molar mass M and density rmass from
Appendix F, we then have (with some conversions of units)
or
n ! 8.49 $ 10 28 m#3.
Next let us combine the first two key ideas by writing
Substituting for A with pr 2 (! 2.54 $ 10 #6 m2) and solving
for vd, we then find
(Answer)
which is only 1.8 mm/h, slower than a sluggish snail.
Lights are fast: You may well ask: “If the electrons drift so
slowly,why do the room lights turn on so quickly when I throw
the switch?” Confusion on this point results from not distin-
guishing between the drift speed of the electrons and the
speed at which changes in the electric field configuration
travel along wires.This latter speed is nearly that of light; elec-
trons everywhere in the wire begin drifting almost at once, in-
cluding into the lightbulbs. Similarly, when you open the valve
on your garden hose with the hose full of water, a pressure
wave travels along the hose at the speed of sound in water.
The speed at which the water itself moves through the hose-
measured perhaps with a dye marker-is much slower.
! 4.9 $ 10 #7 m/s,
!
17 $ 10 #3 A
(8.49 $ 10 28 m#3)(1.6 $ 10 #19 C)(2.54 $ 10 #6 m2)
vd !
i
ne(pr2)
i
A ! nevd.
! 8.49 $ 10 28 electrons/m3
n ! (6.02 $ 10 23 mol#1)(8.96 $ 10 3 kg/m3)
63.54 $ 10 #3 kg/mol
