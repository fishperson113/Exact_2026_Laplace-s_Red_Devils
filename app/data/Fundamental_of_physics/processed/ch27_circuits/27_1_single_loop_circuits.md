C H A

P

T

E

R

2

7

Circuits

27-1 SINGLE-LOOP CIRCUITS

Learning Objectives
After reading this module, you should be able to . . .

27.01 Identify the action of an emf source in terms of the work

it does.

series is equal to the sum of the potentials across the
individual resistors.

27.02 For an ideal battery, apply the relationship between

27.10 Calculate the potential difference between any two

the emf, the current, and the power (rate of energy transfer).

points in a circuit.

27.03 Draw a schematic diagram for a single-loop circuit

containing a battery and three resistors.

27.04 Apply the loop rule to write a loop equation that relates
the potential differences of the circuit elements around a
(complete) loop.

27.05 Apply the resistance rule in crossing through a resistor.
27.06 Apply the emf rule in crossing through an emf.
27.07 Identify that resistors in series have the same cur-
rent, which is the same value that their equivalent
resistor has.

27.08 Calculate the equivalent of series resistors.
27.09 Identify that a potential applied to resistors wired in

27.11 Distinguish a real battery from an ideal battery and, in a
circuit diagram, replace a real battery with an ideal battery
and an explicitly shown resistance.

27.12 With a real battery in a circuit, calculate the potential dif-
ference between its terminals for current in the direction of
the emf and in the opposite direction.

27.13 Identify what is meant by grounding a circuit, and draw a

schematic diagram for such a connection.

27.14 Identify that grounding a circuit does not affect the

current in a circuit.

27.15 Calculate the dissipation rate of energy in a real battery.
27.16 Calculate the net rate of energy transfer in a real battery for
current in the direction of the emf and in the opposite direction.

Key Ideas
● An emf device does work on charges to maintain a potential dif-
ference between its output terminals. If dW is the work the device
does to force positive charge dq from the negative to the positive
terminal, then the emf (work per unit charge) of the device is

# !

dW
dq

(definition of #).

● An ideal emf device is one that lacks any internal resistance.
The potential difference between its terminals is equal to the emf.

● A real emf device has internal resistance. The potential
difference between its terminals is equal to the emf only if there
is no current through the device.
● The change in potential in traversing a resistance R in the di-
rection of the current is #iR; in the opposite direction it is %iR
(resistance rule).

● The change in potential in traversing an ideal emf device in
the direction of the emf arrow is %#; in the opposite direction it
is ## (emf rule).
● Conservation of energy leads to the loop rule:
Loop Rule. The algebraic sum of the changes in potential encoun-

tered in a complete traversal of any loop of a circuit must be zero.

Conservation of charge leads to the junction rule (Chapter 26):
Junction Rule.
The sum of the currents entering any junction
must be equal to the sum of the currents leaving that junction.
● When a real battery of emf # and internal resistance r does
work on the charge carriers in a current i through the battery,
the rate P of energy transfer to the charge carriers is

P ! iV,

where V is the potential across the terminals of the battery.
● The rate Pr at which energy is dissipated as thermal energy
in the battery is
Pr ! i2r.

● The rate Pemf at which the chemical energy in the battery
changes is

Pemf ! i#.
● When resistances are in series, they have the same current. The
equivalent resistance that can replace a series combination of re-
sistances is

n

Req ! ’

j!1

Rj

(n resistances in series).

771

772

CHAPTE R  27 CI RCU ITS

Courtesy Southern California Edison Company

The world’s largest battery energy storage
plant (dismantled in 1996) connected over
8000 large lead-acid batteries in 8 strings at
1000 V each with a capability of 10 MW of
power for 4 hours. Charged up at night, the
batteries were then put to use during peak
power demands on the electrical system.

What Is Physics?
You are surrounded by electric circuits. You might take pride in the number of
electrical devices you own and might even carry a mental list of the devices you
wish  you  owned. Every  one  of  those  devices, as  well  as  the  electrical  grid  that
powers your home, depends on modern electrical engineering. We cannot easily
estimate the current financial worth of electrical engineering and its products, but
we can be certain that the financial worth continues to grow yearly as more and
more tasks are handled electrically. Radios are now tuned electronically instead
of  manually. Messages  are  now  sent  by  email  instead  of  through  the  postal
system. Research  journals  are  now  read  on  a  computer  instead  of  in  a  library
building, and research papers are now copied and filed electronically instead of
photocopied and tucked into a filing cabinet. Indeed, you may be reading an elec-
tronic version of this book.

The  basic  science  of  electrical  engineering  is  physics. In  this  chapter  we
cover the physics of electric circuits that are combinations of resistors and bat-
teries  (and, in  Module  27-4, capacitors). We  restrict  our  discussion  to  circuits
through  which  charge  flows  in  one  direction, which  are  called  either  direct-
current  circuits or DC  circuits. We  begin  with  the  question: How  can  you  get
charges to flow?

“Pumping” Charges
If you want to make charge carriers flow through a resistor, you must establish a
potential difference between the ends of the device. One way to do this is to con-
nect each end of the resistor to one plate of a charged capacitor. The trouble with
this  scheme  is  that  the  flow  of  charge  acts  to  discharge  the  capacitor, quickly
bringing the plates to the same potential. When that happens, there is no longer
an electric field in the resistor, and thus the flow of charge stops.

To  produce  a  steady  flow  of  charge, you  need  a  “charge  pump,” a  device
that — by  doing  work  on  the  charge  carriers — maintains  a  potential  difference
between a pair of terminals. We call such a device an emf device, and the device is
said  to  provide  an  emf #, which  means  that  it  does  work  on  charge  carriers.
An emf device is sometimes called a seat of emf. The term emf comes from the
outdated phrase electromotive force, which was adopted before scientists clearly
understood the function of an emf device.

In Chapter 26, we discussed the motion of charge carriers through a circuit in
terms  of  the  electric  field  set  up  in  the  circuit — the  field  produces  forces  that
move the charge carriers. In this chapter we take a different approach: We discuss
the motion of the charge carriers in terms of the required energy — an emf device
supplies the energy for the motion via the work it does.

A  common  emf  device  is  the  battery, used  to  power  a  wide  variety  of
machines from wristwatches to submarines. The emf device that most influences
our  daily  lives, however, is  the  electric  generator, which, by  means  of  electrical
connections (wires) from a generating plant, creates a potential difference in our
homes and workplaces. The emf devices known as solar cells, long familiar as the
wing-like panels on spacecraft, also dot the countryside for domestic applications.
Less familiar emf devices are the fuel cells that powered the space shuttles and
the thermopiles that provide onboard electrical power for some spacecraft and
for remote stations in Antarctica and elsewhere. An emf device does not have to
be an instrument — living systems, ranging from electric eels and human beings to
plants, have physiological emf devices.

Although the devices we have listed differ widely in their modes of opera-
tion, they all perform the same basic function — they do work on charge carriers
and thus maintain a potential difference between their terminals.

27-1 SI NG LE-LOOP  CI RCU ITS

773

Work, Energy, and Emf
Figure  27-1  shows  an  emf  device  (consider  it  to  be  a  battery)  that  is  part  of  a
simple circuit containing a single resistance R (the symbol for resistance and a
resistor is
). The emf device keeps one of its terminals (called the positive
terminal and often labeled %) at a higher electric potential than the other termi-
nal (called the negative terminal and labeled #). We can represent the emf of the
device with an arrow that points from the negative terminal toward the positive
terminal as in Fig. 27-1. A small circle on the tail of the emf arrow distinguishes it
from the arrows that indicate current direction.

When an emf device is not connected to a circuit, the internal chemistry of
the  device  does  not  cause  any  net  flow  of  charge  carriers  within  it. However,
when it is connected to a circuit as in Fig. 27-1, its internal chemistry causes a net
flow of positive charge carriers from the negative terminal to the positive termi-
nal, in the direction of the emf arrow. This flow is part of the current that is set up
around the circuit in that same direction (clockwise in Fig. 27-1).

Within  the  emf  device, positive  charge  carriers  move  from  a  region  of  low
electric potential and thus low electric potential energy (at the negative terminal)
to  a  region  of  higher  electric  potential  and  higher  electric  potential  energy  (at
the positive terminal). This motion is just the opposite of what the electric field
between the terminals (which is directed from the positive terminal toward the
negative terminal) would cause the charge carriers to do.

Thus, there must be some source of energy within the device, enabling it to
do work on the charges by forcing them to move as they do. The energy source
may be chemical, as in a battery or a fuel cell. It may involve mechanical forces, as
in an electric generator. Temperature differences may supply the energy, as in a
thermopile; or the Sun may supply it, as in a solar cell.

Let us now analyze the circuit of Fig. 27-1 from the point of view of work and
energy transfers. In any time interval dt, a charge dq passes through any cross sec-
tion of this circuit, such as aa-. This same amount of charge must enter the emf
device  at  its  low-potential  end  and  leave  at  its  high-potential  end. The  device
must do an amount of work dW on the charge dq to force it to move in this way.
We define the emf of the emf device in terms of this work:

# !

dW
dq

(definition of #).

(27-1)

In words, the emf of an emf device is the work per unit charge that the device
does in moving charge from its low-potential terminal to its high-potential termi-
nal. The SI unit for emf is the joule per coulomb; in Chapter 24 we defined that
unit as the volt.

An ideal emf device is one that lacks any internal resistance to the internal
movement of charge from terminal to terminal. The potential difference between
the terminals of an ideal emf device is equal to the emf of the device. For exam-
ple, an ideal battery with an emf of 12.0 V always has a potential difference of
12.0 V between its terminals.

A real  emf  device, such  as  any  real  battery, has  internal  resistance  to  the
internal  movement  of  charge. When  a  real  emf  device  is  not  connected  to  a
circuit, and  thus  does  not  have  current  through  it, the  potential  difference
between its terminals is equal to its emf. However, when that device has current
through it, the potential difference between its terminals differs from its emf. We
shall discuss such real batteries near the end of this module.

When an emf device is connected to a circuit, the device transfers energy to
the charge carriers passing through it. This energy can then be transferred from
the  charge  carriers  to  other  devices  in  the  circuit, for  example, to  light  a  bulb.
Figure 27-2a shows a circuit containing two ideal rechargeable (storage) batteries
A and B, a resistance R, and an electric motor M that can lift an object by using

+

–

a

a'

R

i

i

i

Figure 27-1 A simple electric circuit, in which
a device of emf # does work on the charge
carriers and maintains a steady current i in
a resistor of resistance R.

i

R

i

  A

+–

A

M

i

B
+–

   B

m

(a)

Work done
by motor
on mass m

Chemical
energy lost
by B

Thermal energy
produced
by resistance R

Chemical
energy stored
in A

(b)

Figure 27-2 (a) In the circuit, #B ( #A; so bat-
tery B determines the direction of the cur-
rent. (b) The energy transfers in the circuit.

774

CHAPTE R  27 CI RCU ITS

The battery drives current
through the resistor, from
high potential to low potential.

i

Higher
potential

R

i

Lower
potential

+
–

B

a

i
Figure 27-3 A single-loop circuit in which a
resistance R is connected across an ideal
battery B with emf #. The resulting current
i is the same throughout the circuit.

energy it obtains from charge carriers in the circuit. Note that the batteries are
connected so that they tend to send charges around the circuit in opposite direc-
tions. The  actual  direction  of  the  current  in  the  circuit  is  determined  by  the
battery  with  the  larger  emf, which  happens  to  be  battery  B, so  the  chemical
energy  within  battery  B  is  decreasing  as  energy  is  transferred  to  the  charge
carriers  passing  through  it. However, the  chemical  energy  within  battery  A  is
increasing because the current in it is directed from the positive terminal to the
negative terminal. Thus, battery B is charging battery A. Battery B is also pro-
viding  energy  to  motor  M  and  energy  that  is  being  dissipated  by  resistance  R.
Figure 27-2b shows all three energy transfers from battery B; each decreases that
battery’s chemical energy.

Calculating the Current in a Single-Loop Circuit
We discuss here two equivalent ways to calculate the current in the simple single-
loop circuit of Fig. 27-3; one method is based on energy conservation considerations,
and the other on the concept of potential. The circuit consists of an ideal battery B
with emf #, a resistor of resistance R, and two connecting wires. (Unless otherwise
indicated, we assume that wires in circuits have negligible resistance. Their function,
then, is merely to provide pathways along which charge carriers can move.)

Energy Method
Equation 26-27 (P ! i 2R) tells us that in a time interval dt an amount of energy
given by i2R dt will appear in the resistor of Fig. 27-3 as thermal energy. As noted
in Module 26-5, this energy is said to be dissipated. (Because we assume the wires
to have negligible resistance, no thermal energy will appear in them.) During the
same  interval, a  charge  dq ! i dt will  have  moved  through  battery  B, and  the
work that the battery will have done on this charge, according to Eq. 27-1, is

dW ! # dq ! #i dt.

From the principle of conservation of energy, the work done by the (ideal) bat-
tery must equal the thermal energy that appears in the resistor:

This gives us

#i dt ! i2R dt.

# ! iR.

The emf # is the energy per unit charge transferred to the moving charges by the
battery. The quantity iR is the energy per unit charge transferred from the mov-
ing charges to thermal energy within the resistor. Therefore, this equation means
that the energy per unit charge transferred to the moving charges is equal to the
energy per unit charge transferred from them. Solving for i, we find

i !

#
R

.

(27-2)

Potential Method
Suppose  we  start  at  any  point  in  the  circuit  of  Fig. 27-3  and  mentally  proceed
around  the  circuit  in  either  direction, adding  algebraically  the  potential  differ-
ences  that  we  encounter. Then  when  we  return  to  our  starting  point, we  must
also have  returned  to  our  starting  potential. Before  actually  doing  so, we  shall
formalize this idea in a statement that holds not only for single-loop circuits such
as that of Fig. 27-3 but also for any complete loop in a multiloop circuit, as we
shall discuss in Module 27-2:

27-1 SI NG LE-LOOP  CI RCU ITS

775

LOOP RULE: The algebraic sum of the changes in potential encountered in a
complete traversal of any loop of a circuit must be zero.

This is often referred to as Kirchhoff’s loop rule (or Kirchhoff’s voltage law), after
German physicist Gustav Robert Kirchhoff. This rule is equivalent to saying that
each  point  on  a  mountain  has  only  one  elevation  above  sea  level. If  you  start
from any point and return to it after walking around the mountain, the algebraic
sum of the changes in elevation that you encounter must be zero.

In Fig. 27-3, let us start at point a, whose potential is Va, and mentally walk
clockwise  around  the  circuit  until  we  are  back  at  a, keeping  track  of  potential
changes as we move. Our starting point is at the low-potential terminal of the bat-
tery. Because the battery is ideal, the potential difference between its terminals is
equal to #. When we pass through the battery to the high-potential terminal, the
change in potential is %#.

As  we  walk  along  the  top  wire  to  the  top  end  of  the  resistor, there  is  no
potential  change  because  the  wire  has  negligible  resistance; it  is  at  the  same
potential as the high-potential terminal of the battery. So too is the top end of the
resistor. When  we  pass  through  the  resistor, however, the  potential  changes
according to Eq. 26-8 (which we can rewrite as V ! iR). Moreover, the potential
must decrease because we are moving from the higher potential side of the resis-
tor. Thus, the change in potential is #iR.

We return to point a by moving along the bottom wire. Because this wire also has
negligible resistance, we again find no potential change. Back at point a, the potential
is again Va. Because we traversed a complete loop, our initial potential, as modified
for potential changes along the way, must be equal to our final potential; that is,

Va % # # iR ! Va.

The value of Va cancels from this equation, which becomes

# # iR ! 0.
Solving this equation for i gives us the same result, i ! #/R, as the energy method
(Eq. 27-2).

If  we  apply  the  loop  rule  to  a  complete  counterclockwise walk  around  the

circuit, the rule gives us

## % iR ! 0

and  we  again  find  that  i ! #/R. Thus, you  may  mentally  circle  a  loop  in  either
direction to apply the loop rule.

To prepare for circuits more complex than that of Fig. 27-3, let us set down

two rules for finding potential differences as we move around a loop:

RESISTANCE RULE: For a move through a resistance in the direction of the
current, the change in potential is #iR; in the opposite direction it is %iR.

EMF RULE: For a move through an ideal emf device in the direction of the emf
arrow, the change in potential is %#; in the opposite direction it is ##.

Checkpoint 1

i

The figure shows the current i in a single-loop circuit
with a battery B and a resistance R (and wires of neg-
ligible resistance). (a) Should the emf arrow at B be
drawn pointing leftward or rightward? At points a, b,
and c, rank (b) the magnitude of the current, (c) the electric potential, and (d) the
electric potential energy of the charge carriers, greatest first.

R

B

a

b

c

776

CHAPTE R  27 CI RCU ITS

Other Single-Loop Circuits
Next we extend the simple circuit of Fig. 27-3 in two ways.

Internal Resistance
Figure 27-4a shows a real battery, with internal resistance r, wired to an external
resistor of resistance R. The internal resistance of the battery is the electrical
resistance of the conducting materials of the battery and thus is an unremov-
able feature of the battery. In Fig. 27-4a, however, the battery is drawn as if it
could be separated into an ideal battery with emf # and a resistor of resistance
r. The order in which the symbols for these separated parts are drawn does not
matter.

i

i

b +

r

a

–

R

i

a

)
V
(

l
a
i
t
n
e
t
o
P

Va

r

ir

b

Vb

i

R

a

iR

Va

Real battery

i
(a )

Emf device

Resistor

(b )

Figure 27-4 (a) A single-loop circuit containing a real battery having internal resistance
r and emf #. (b) The same circuit, now spread out in a line. The potentials encountered
in traversing the circuit clockwise from a are also shown. The potential Va is arbitrarily
assigned a value of zero, and other potentials in the circuit are graphed relative to Va.

If  we  apply  the  loop  rule  clockwise  beginning  at  point  a, the  changes in

potential give us

R 2

i

Solving for the current, we find

# # ir # iR ! 0.

i !

#
R % r

.

(27-3)

(27-4)

+
–

b

a

i

R1

R3

i

Series resistors
and their
equivalent have
the same
current (“ser-i”).

R eq

i

(a )

b

a
(b )

+
–

Figure 27-5 (a) Three resistors are connected
in series between points a and b. (b) An
equivalent circuit, with the three resistors
replaced with their equivalent resistance Req.

Note that this equation reduces to Eq. 27-2 if the battery is ideal — that is, if r ! 0.
Figure 27-4b shows graphically the changes in electric potential around the
circuit. (To  better  link  Fig. 27-4b with  the  closed  circuit in  Fig. 27-4a, imagine
curling the graph into a cylinder with point a at the left overlapping point a at
the right.)  Note  how  traversing  the  circuit  is  like  walking  around  a  (potential)
mountain back to your starting point — you return to the starting elevation.

In this book, when a battery is not described as real or if no internal resist-
ance is indicated, you can generally assume that it is ideal — but, of course, in the
real world batteries are always real and have internal resistance.

Resistances in Series
Figure 27-5a shows three resistances connected in series to an ideal battery with
emf #. This  description  has  little  to  do  with  how  the  resistances  are  drawn.
Rather, “in  series” means  that  the  resistances  are  wired  one  after  another  and
that  a  potential  difference  V is  applied  across  the  two  ends  of  the  series. In
Fig. 27-5a, the resistances are connected one after another between a and b, and a
potential  difference  is  maintained  across  a and b by  the  battery. The  potential
differences that then exist across the resistances in the series produce identical
currents i in them. In general,

27-1 SI NG LE-LOOP  CI RCU ITS

777

When a potential difference V is applied across resistances connected in series,
the resistances have identical currents i. The sum of the potential differences
across the resistances is equal to the applied potential difference V.

Note that charge moving through the series resistances can move along only a
single route. If there are additional routes, so that the currents in different resis-
tances are different, the resistances are not connected in series.

Resistances connected in series can be replaced with an equivalent resistance Req
that has the same current i and the same total potential difference V as the actual
resistances.

You might remember that Req and all the actual series resistances have the same
current i with the nonsense word “ser-i.” Figure 27-5b shows the equivalent resis-
tance Req that can replace the three resistances of Fig. 27-5a.

To derive an expression for Req in Fig. 27-5b, we apply the loop rule to both
circuits. For Fig. 27-5a, starting at a and going clockwise around the circuit, we
find

or

# # iR1 # iR2 # iR3 ! 0,

i !

#
R1 % R2 % R3

.

(27-5)

For Fig. 27-5b, with the three resistances replaced with a single equivalent resist-
ance Req, we find

or

# # iReq ! 0,

i !

#
Req

.

(27-6)

Comparison of Eqs. 27-5 and 27-6 shows that

The extension to n resistances is straightforward and is

Req ! R1 % R2 % R3.

n

Req ! ’

j!1

Rj

(n resistances in series).

(27-7)

Note  that  when  resistances  are  in  series, their  equivalent  resistance  is  greater
than any of the individual resistances.

Checkpoint 2

In Fig. 27-5a, if R1 ( R2 ( R3, rank the three resistances according to (a) the current
through them and (b) the potential difference across them, greatest first.

Potential Difference Between Two Points
We often want to find the potential difference between two points in a circuit. For
example, in Fig. 27-6, what is the potential difference Vb # Va between points a
and b? To find out, let’s start at point a (at potential Va) and move through the
battery to point b (at potential Vb) while keeping track of the potential changes
we encounter. When we pass through the battery’s emf, the potential increases
by #. When we pass through the battery’s internal resistance r, we move in the
direction of the current and thus the potential decreases by ir. We are then at the

The internal resistance reduces
the potential difference between
the terminals.

b +

i

r = 2.0 Ω

 = 12 V

a

–

i

R = 4.0 Ω

Figure 27-6 Points a and b, which are at the
terminals of a real battery, differ in potential.

778

CHAPTE R  27 CI RCU ITS

potential of point b and we have

or

Va % # # ir ! Vb,
Vb # Va ! # # ir.
To  evaluate  this  expression, we  need  the  current  i. Note  that  the  circuit  is  the
same as in Fig. 27-4a, for which Eq. 27-4 gives the current as

(27-8)

Substituting this equation into Eq. 27-8 gives us

i !

#
R % r

.

Vb # Va ! # #

#
R % r

r

!

#
R % r

R.

(27-9)

(27-10)

Now substituting the data given in Fig. 27-6, we have

Vb # Va !

12 V
4.0 0 % 2.0 0

 4.0 0 ! 8.0 V.

(27-11)

Suppose, instead, we  move  from  a to b counterclockwise, passing  through
resistor R rather  than  through  the  battery. Because  we  move  opposite  the
current, the potential increases by iR. Thus,

or

Va % iR ! Vb

Vb # Va ! iR.

(27-12)

Substituting for i from Eq. 27-9, we again find Eq. 27-10. Hence, substitution of
the data in Fig. 27-6 yields the same result, Vb # Va ! 8.0 V. In general,

To find the potential between any two points in a circuit, start at one point and
traverse the circuit to the other point, following any path, and add algebraically
the changes in potential you encounter.

Potential Difference Across a Real Battery
In Fig. 27-6, points a and b are located at the terminals of the battery. Thus, the
potential  difference  Vb # Va is  the  terminal-to-terminal  potential  difference  V
across the battery. From Eq. 27-8, we see that

V ! # # ir.

(27-13)

If the internal resistance r of the battery in Fig. 27-6 were zero, Eq. 27-13 tells
us that V would be equal to the emf # of the battery — namely, 12 V. However,
because r ! 2.0 0, Eq. 27-13  tells  us  that  V is  less  than  #. From  Eq. 27-11, we
know that V is only 8.0 V. Note that the result depends on the value of the current
through  the  battery. If  the  same  battery  were  in  a  different  circuit  and  had  a
different current through it, V would have some other value.

Grounding a Circuit
Figure 27-7a shows the same circuit as Fig. 27-6 except that here point a is directly
connected to ground, as indicated by the common symbol
. Grounding a cir-
cuit usually means connecting the circuit to a conducting path to Earth’s surface
(actually to the electrically conducting moist dirt and rock below ground). Here,
such  a  connection  means  only  that  the  potential  is  defined  to  be  zero  at  the
grounding point in the circuit. Thus in Fig. 27-7a, the potential at a is defined to
be Va ! 0. Equation 27-11 then tells us that the potential at b is Vb ! 8.0 V.

27-1 SI NG LE-LOOP  CI RCU ITS

779

b +

i

r = 2.0 Ω

 = 12 V

a

–

i

R = 4.0 Ω

(a)

Ground is taken
to be zero potential.

b +

i

r = 2.0 Ω

 = 12 V

a

–

i

(b)

R = 4.0 Ω

Figure 27-7 (a) Point a is directly connected to ground. (b) Point b is directly connected to
ground.

Figure 27-7b is the same circuit except that point b is now directly connected
to ground. Thus, the potential there is defined to be Vb ! 0. Equation 27-11 now
tells us that the potential at a is Va ! #8.0 V.

Power, Potential, and Emf
When a battery or some other type of emf device does work on the charge car-
riers to establish a current i, the device transfers energy from its source of en-
ergy (such as the chemical source in a battery) to the charge carriers. Because a
real emf device has an internal resistance r, it also transfers energy to internal
thermal  energy  via  resistive  dissipation  (Module  26-5). Let  us  relate  these
transfers.

The net rate P of energy transfer from the emf device to the charge carriers is

given by Eq. 26-26:

P ! iV,

(27-14)

where V is the potential across the terminals of the emf device. From Eq. 27-13,
we can substitute V ! # # ir into Eq. 27-14 to find

P ! i(# # ir) ! i# # i2r.

(27-15)

From Eq. 26-27, we recognize the term i2r in Eq. 27-15 as the rate Pr of energy
transfer to thermal energy within the emf device:

Pr ! i2r

(internal dissipation rate).

(27-16)

Then  the  term  i# in  Eq. 27-15  must  be  the  rate  Pemf at  which  the  emf  device
transfers  energy  both to  the  charge  carriers  and  to  internal  thermal  energy.
Thus,

Pemf ! i# (power of emf device).

(27-17)

If  a  battery  is  being  recharged, with  a “wrong  way” current  through  it, the
energy  transfer  is  then  from the  charge  carriers  to the  battery — both  to  the
battery’s chemical energy and to the energy dissipated in the internal resistance r.
The rate of change of the chemical energy is given by Eq. 27-17, the rate of dissi-
pation is given by Eq. 27-16, and the rate at which the carriers supply energy is
given by Eq. 27-14.

Checkpoint 3

A battery has an emf of 12 V and an internal resistance of 2 0. Is the terminal-to-
terminal potential difference greater than, less than, or equal to 12 V if the current in
the battery is (a) from the negative to the positive terminal, (b) from the positive to
the negative terminal, and (c) zero?

780

CHAPTE R  27 CI RCU ITS

Sample Problem 27.01 Single-loop circuit with two real batteries

The emfs and resistances in the circuit of Fig. 27-8a have the
following values:

#1 ! 4.4 V, #2 ! 2.1 V,

r1 ! 2.3 0,

r2 ! 1.8 0, R ! 5.5 0.

(a) What is the current i in the circuit?

KEY IDEA

two batteries. Because #1 is greater than #2, battery 1 con-
trols the direction of i, so the direction is clockwise. Let us
then  apply  the  loop  rule  by  going  counterclockwise —
against  the  current — and  starting  at  point  a. (These  deci-
sions  about  where  to  start  and  which  way  you  go  are
arbitrary  but, once  made, you  must  be  consistent  with
decisions about the plus and minus signs.) We find

##1 % ir1 % iR % ir2 % #2 ! 0.

We  can  get  an  expression  involving  the  current  i in  this
single-loop  circuit  by  applying  the  loop  rule, in  which  we
sum the potential changes around the full loop.

Calculations: Although  knowing  the  direction  of  i is  not
necessary, we can easily determine it from the emfs of the

Check that this equation also results if we apply the loop
rule  clockwise  or  start  at  some  point  other  than a. Also,
take the time to compare this equation term by term with
Fig. 27-8b, which shows the potential changes graphically
(with the potential at point a arbitrarily taken to be zero).
Solving the above loop equation for the current i, we

Battery 1

1

r1

b

a

i

i
R

(a)

Battery 2

2

r2

c

a

Va

0

–1

–2

–3

–4

–5

)
V
(

l
a
i
t
n
e
t
o
P

1

r1

b

i

R

r2

c

2

a

Va

2 = 2.1 V

ir2

Vc

iR

1 = 4.4 V

Vb
ir1

Battery 1

Resistor

Battery 2

obtain

i !

# 1 # # 2
R % r1 % r2

!

4.4 V # 2.1 V
5.5 0 % 2.3 0 % 1.8 0

! 0.2396 A % 240 mA.

(Answer)

(b) What is the potential difference between the terminals
of battery 1 in Fig. 27-8a?

KEY IDEA

We need to sum the potential differences between points a
and b.

Calculations: Let us start at point b (effectively the nega-
tive  terminal  of  battery  1)  and  travel  clockwise  through
battery  1  to  point  a (effectively  the  positive  terminal),
keeping track of potential changes. We find that

Vb # ir1 % #1 ! Va,

which gives us

Va # Vb ! #ir1 % # 1

! #(0.2396 A)(2.3 0) % 4.4 V

! %3.84 V % 3.8 V,

(Answer)

(b)

Figure 27-8 (a) A single-loop circuit containing two real batteries
and a resistor. The batteries oppose each other; that is, they tend to
send current in opposite directions through the resistor. (b) A
graph of the potentials, counterclockwise from point a, with the
potential at a arbitrarily taken to be zero. (To better link the circuit
with the graph, mentally cut the circuit at a and then unfold the left
side of the circuit toward the left and the right side of the circuit
toward the right.)

which is less than the emf of the battery. You can verify this
result by starting at point b in Fig. 27-8a and traversing the
circuit  counterclockwise  to  point  a. We  learn  two  points
here. (1) The  potential  difference  between  two  points  in  a
circuit is independent of the path we choose to go from one
to  the  other. (2) When  the  current  in  the  battery  is  in  the
“proper” direction, the  terminal-to-terminal  potential  dif-
ference is low, that is, lower than the stated emf for the bat-
tery that you might find printed on the battery.

Additional examples, video, and practice available at WileyPLUS
