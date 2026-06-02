Sample Problem 26.05
Mean free time and mean free distance
(a) What is the mean free time t between collisions for the
conduction electrons in copper?
KEY IDEAS
The mean free time t of copper is approximately constant,
and in particular does not depend on any electric field that
might be applied to a sample of the copper. Thus, we need
not consider any particular value of applied electric field.
However, because the resistivity r displayed by copper
under an electric field depends on t, we can find the mean
free time t from Eq. 26-22 (r ! m/e2nt).
Calculations: That equation gives us
(26-23)
The number of conduction electrons per unit volume in cop-
per is 8.49 $ 1028 m#3.We take the value of r from Table 26-1.
The denominator then becomes
where we converted units as
C2&0
m2
! C2&V
m2&A ! C2&J/C
m2&C/s ! kg&m2/s2
m2/s
! kg
s .
! 3.67 $ 10 #17 C2&0/m2 ! 3.67 $ 10 #17 kg/s,
(8.49 $ 10 28 m#3)(1.6 $ 10 #19 C)2(1.69 $ 10 #8 0&m)
t !
m
ne2r .
Additional examples, video, and practice available at WileyPLUS

760
CHAPTER 26
CURRENT AND RESISTANCE
26-5 POWER, SEMICONDUCTORS, SUPERCONDUCTORS
After reading this module, you should be able to . . .
26.27 Explain how conduction electrons in a circuit lose
energy in a resistive device.
26.28 Identify that power is the rate at which energy is
transferred from one type to another.
26.29 For a resistive device, apply the relationships 
between power P, current i, voltage V, and 
resistance R.
26.30 For a battery, apply the relationship between power P,
current i, and potential difference V.
26.31 Apply the conservation of energy to a circuit with a
battery and a resistive device to relate the energy transfers
in the circuit.
26.32 Distinguish conductors, semiconductors, and
superconductors.
Learning Objectives
●The power P, or rate of energy transfer, in an electrical
device across which a potential difference V is maintained is
P ! iV.
●If the device is a resistor, the power can also be written as
●In a resistor, electric potential energy is converted to internal
P ! i2R ! V2
R .
thermal energy via collisions between charge carriers and atoms.
●Semiconductors are materials that have few conduction
electrons but can become conductors when they are doped
with other atoms that contribute charge carriers.
●Superconductors are materials that lose all electrical resis-
tance. Most such materials require very low temperatures,
but some become superconducting at temperatures as high
as room temperature.
Key Ideas
Power in Electric Circuits
Figure 26-13 shows a circuit consisting of a battery B that is connected by
wires, which we assume have negligible resistance, to an unspecified conducting
device.The device might be a resistor, a storage battery (a rechargeable battery),
a motor, or some other electrical device. The battery maintains a potential
difference of magnitude V across its own terminals and thus (because of the
wires) across the terminals of the unspecified device, with a greater potential at
terminal a of the device than at terminal b.
Because there is an external conducting path between the two terminals of the
battery, and because the potential differences set up by the battery are maintained,
a steady current i is produced in the circuit, directed from terminal a to terminal b.
The amount of charge dq that moves between those terminals in time interval dt is
equal to i dt.This charge dq moves through a decrease in potential of magnitude V,
and thus its electric potential energy decreases in magnitude by the amount
dU ! dq V ! i dt V.
(26-25)
The principle of conservation of energy tells us that the decrease in electric
potential energy from a to b is accompanied by a transfer of energy to some other
form. The power P associated with that transfer is the rate of transfer dU/dt,
which is given by Eq. 26-25 as
P ! iV
(rate of electrical energy transfer).
(26-26)
Moreover, this power P is also the rate at which energy is transferred from the
battery to the unspecified device. If that device is a motor connected to a me-
chanical load, the energy is transferred as work done on the load. If the device is a
storage battery that is being charged, the energy is transferred to stored chemical
energy in the storage battery. If the device is a resistor, the energy is transferred
to internal thermal energy, tending to increase the resistor’s temperature.
Figure 26-13 A battery B sets up a current i
in a circuit containing an unspecified
conducting device.
+
-
i
B
i
?
a
b
i
i
i
i
The battery at the left
supplies energy to the
conduction electrons
that form the current.

The unit of power that follows from Eq. 26-26 is the volt-ampere (V&A).
We can write it as
As an electron moves through a resistor at constant drift speed, its average
kinetic energy remains constant and its lost electric potential energy appears as
thermal energy in the resistor and the surroundings. On a microscopic scale this
energy transfer is due to collisions between the electron and the molecules of the
resistor, which leads to an increase in the temperature of the resistor lattice.
The mechanical energy thus transferred to thermal energy is dissipated (lost)
because the transfer cannot be reversed.
For a resistor or some other device with resistance R, we can combine
Eqs. 26-8 (R ! V/i) and 26-26 to obtain, for the rate of electrical energy dissipa-
tion due to a resistance, either
P ! i2R
(resistive dissipation)
(26-27)
or
(resistive dissipation).
(26-28)
Caution: We must be careful to distinguish these two equations from Eq. 26-26:
P ! iV applies to electrical energy transfers of all kinds; P ! i2R and P ! V 2/R
apply only to the transfer of electric potential energy to thermal energy in a
device with resistance.
P ! V 2
R
1 V&A !#1 J
C$#1 C
s $ ! 1 J
s ! 1 W.
761
26-5 POWER, SEMICONDUCTORS, SUPERCONDUCTORS
Checkpoint 5
A potential difference V is connected across a device with resistance R, causing cur-
rent i through the device. Rank the following variations according to the change in the
rate at which electrical energy is converted to thermal energy due to the resistance,
greatest change first: (a) V is doubled with R unchanged, (b) i is doubled with R
unchanged, (c) R is doubled with V unchanged, (d) R is doubled with i unchanged.
(Answer)
In situation 2, the resistance of each half of the wire is
(72 0)/2, or 36 0.Thus, the dissipation rate for each half is
and that for the two halves is
P ! 2P- ! 800 W.
(Answer)
This is four times the dissipation rate of the full length of
wire.Thus, you might conclude that you could buy a heating
coil, cut it in half, and reconnect it to obtain four times the
heat output.Why is this unwise? (What would happen to the
amount of current in the coil?)
P- ! (120 V)2
36 0
! 400 W,
P ! V 2
R ! (120 V)2
72 0
! 200 W.
