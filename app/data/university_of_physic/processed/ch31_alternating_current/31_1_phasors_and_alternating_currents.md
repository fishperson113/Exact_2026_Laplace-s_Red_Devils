ALTERNATING
CURRENT

? Waves from a broadcasting station produce an alternating current in the cir-

cuits of a radio (like the one in this classic car). If a radio is tuned to a station
at a frequency of 1000 kHz, does it also detect the transmissions from a sta-
tion broadcasting at 600 kHz?

During the 1880s in the United States there was a heated and acrimonious

debate between two inventors over the best method of electric-power dis-
tribution. Thomas Edison favored direct current (dc)—that is, steady cur-
rent  that  does  not  vary  with  time.  George  Westinghouse  favored  alternating
current  (ac), with  sinusoidally  varying  voltages  and  currents.  He  argued  that
transformers (which we will study in this chapter) can be used to step the voltage
up and down with ac but not with dc; low voltages are safer for consumer use, but
high voltages and correspondingly low currents are best for long-distance power
losses in the cables.
transmission to minimize

i 2R

Eventually,  Westinghouse  prevailed,  and  most  present-day  household  and
industrial power-distribution systems operate with alternating current. Any appli-
ance that you plug into a wall outlet uses ac, and many battery-powered devices
such as radios and cordless telephones make use of the dc supplied by the battery
to  create  or  amplify  alternating  currents.  Circuits  in  modern  communication
equipment, including pagers and television, also make extensive use of ac.

In this chapter we will learn how resistors, inductors, and capacitors behave in cir-
cuits with sinusoidally varying voltages and currents. Many of the principles that we
found useful in Chapters 25, 28, and 30 are applicable, along with several new con-
cepts related to the circuit behavior of inductors and capacitors. A key concept in this
discussion is resonance, which we studied in Chapter 14 for mechanical systems.

31.1 Phasors and Alternating Currents

To supply an alternating current to a circuit, a source of alternating emf or volt-
age is required. An example of such a source is a coil of wire rotating with con-
stant angular velocity in a magnetic ﬁeld, which we discussed in Example 29.3
(Section 29.2). This develops a sinusoidal alternating emf and is the prototype of
the commercial alternating-current generator or alternator (see Fig. 29.8).

31

LEARNING GOALS

By studying this chapter, you will

learn:

• How phasors make it easy to

describe sinusoidally varying

quantities.

• How to use reactance to describe

the voltage across a circuit element

that carries an alternating current.

• How to analyze an L-R-C series

circuit with a sinusoidal emf.

• What determines the amount of

power flowing into or out of an

alternating-current circuit.

• How an L-R-C series circuit

responds to sinusoidal emfs of

different frequencies.

• Why transformers are useful, and

how they work.

1021

1022

CHAPTER 31 Alternating Current

We use the term ac source for any device that supplies a sinusoidally varying
i.
voltage (potential difference)  or current  The usual circuit-diagram symbol for
an ac source is

v

A sinusoidal voltage might be described by a function such as

v = V cos vt

(31.1)

31.1 The voltage across a sinusoidal ac
source.

Voltage
positive
+
–

Voltage
zero

Voltage
negative
+
–

v

(lowercase)  is  the  instantaneous potential  difference;

V
In  this  expression,
(uppercase)  is  the  maximum  potential  difference,  which  we  call  the  voltage
ƒ
amplitude; and
(Fig. 31.1).

is the angular frequency, equal to

times the frequency

2p

v

In the United States and Canada, commercial electric-power distribution systems
v = 12p rad2160 s-12 =
is used.

always  use  a  frequency  of
377 rad>s;
Similarly, a sinusoidal current might be described as

ƒ = 50 Hz 1v = 314 rad>s2

in much of the rest of the world,

corresponding  to

ƒ = 60 Hz,

t

i = I cos vt

(31.2)

i

(lowercase) is the instantaneous current and

where
mum current or current amplitude.

I

(uppercase) is the maxi-

v

O

31.2 A phasor diagram.

Length of phasor
equals maximum
current I.

Phasor rotates with
frequency f and
angular speed v 52pf.

v

I

Phasor

vt

Projection of phasor onto
horizontal axis at time t
equals current i at that
instant: i 5 I cos vt.

O

i 5 I cos vt

Phasor Diagrams
To represent sinusoidally varying voltages and currents, we will use rotating vec-
tor diagrams similar to those we used in the study of simple harmonic motion in
Section  14.2  (see  Figs.  14.5b  and  14.6).  In  these  diagrams  the  instantaneous
value  of  a  quantity  that  varies  sinusoidally  with  time  is  represented  by  the
projection onto a horizontal axis of a vector with a length equal to the amplitude
of the quantity. The vector rotates counterclockwise with constant angular speed
v.
These rotating vectors are called phasors, and diagrams containing them are
called phasor diagrams. Figure 31.2 shows a phasor diagram for the sinusoidal
current described by Eq. (31.2). The projection of the phasor onto the horizontal
t
axis at time
this is why we chose to use the cosine function rather
than the sine in Eq. (31.2).

I cos vt;

is

CAUTION Just what is a phasor? A phasor is not a real physical quantity with a direc-
tion in space, such as velocity, momentum, or electric ﬁeld. Rather, it is a geometric entity
that helps us to describe and analyze physical quantities that vary sinusoidally with time.
In Section 14.2 we used a single phasor to represent the position of a point mass undergo-
ing simple harmonic motion. In this chapter we will use phasors to add sinusoidal voltages
and currents. Combining sinusoidal quantities with phase differences then becomes a mat-
ter of vector addition. We will ﬁnd a similar use for phasors in Chapters 35 and 36 in our
study of interference effects with light. ❙

Rectified Alternating Current
How do we measure a sinusoidally varying current? In Section 26.3 we used a
d’Arsonval galvanometer to measure steady currents. But if we pass a sinusoidal
current through a d’Arsonval meter, the torque on the moving coil varies sinu-
soidally, with one direction half the time and the opposite direction the other half.
The  needle  may  wiggle  a  little  if  the  frequency  is  low  enough,  but  its  average
deﬂection is zero. Hence a d’Arsonval meter by itself isn’t very useful for meas-
uring alternating currents.

31.1 Phasors and Alternating Currents

1023

To get a measurable one-way current through the meter, we can use diodes,
which we described in Section 25.3. A diode is a device that conducts better in
one direction than in the other; an ideal diode has zero resistance for one direc-
tion of current and inﬁnite resistance for the other. Figure 31.3a shows one possi-
ble  arrangement,  called  a  full-wave  rectiﬁer  circuit.  The  current  through  the
galvanometer G is always upward, regardless of the direction of the current from
the  ac  source  (i.e.,  which  part  of  the  cycle  the  source  is  in).  The  graph  in
Fig.  31.3b  shows  the  current  through  G:  It  pulsates  but  always  has  the  same
direction, and the average meter deﬂection is not zero.

31.3 (a) A full-wave rectiﬁer circuit.
(b) Graph of the resulting current through
the galvanometer G.

(a) A full-wave rectifier circuit

Source of
alternating current

Alternating
current

Irav

The rectiﬁed average current

is deﬁned so that during any whole number
of cycles, the total charge that ﬂows is the same as though the current were con-
stant with a value equal to
and the name rectiﬁed average
current emphasize that this is not the average of the original sinusoidal current. In
Fig. 31.3b the total charge that ﬂows in time  corresponds to the area under the
t
is the integral of  ); this area must
curve of  versus  (recall that
equal the rectangular area with height  We see that
is less than the maxi-
mum current

the two are related by

The notation

i = dq>dt,

Irav.

Irav.

t
q

Irav

Irav

so

I;

i

t

Irav = 2

p I = 0.637I

(rectiﬁed average value
of a sinusoidal current)

(31.3)

2>p

is the average value of

(The factor of
in  Section  29.2.)  The  galvanometer  deﬂection  is  proportional  to
vanometer  scale  can  be  calibrated  to  read
(discussed below).

or of

Irav,

I,

see Example 29.4
The  gal-
Irms

Irav.

or,  most  commonly,

ƒcos vtƒ

ƒsin vtƒ;

Root-Mean-Square (rms) Values
A more useful way to describe a quantity that can be either positive or negative is
the root-mean-square (rms) value. We used rms values in Section 18.3 in connec-
i,
tion with the speeds of molecules in a gas. We square the instantaneous current
and ﬁnally take the square root of that aver-
take the average (mean) value of
Irms
age.  This  procedure  deﬁnes  the  root-mean-square  current, denoted  as
i 2
is never zero
(Fig. 31.4). Even when
(unless  is zero at every instant).

is always positive, so

is negative,

Irms

i 2,

i

i

Here’s how we obtain

Irms

If the instantaneous current is given by

for a sinusoidal current, like that shown in Fig. 31.4.
then

i = I cos vt,

i 2 = I 2 cos2 vt

Using a double-angle formula from trigonometry,

cos2 A = 1
2

11 + cos 2A2

we ﬁnd

i 2 = I 2 1
2

11 + cos 2vt2 = 1

2 I 2 + 1

2 I 2 cos 2vt

The average of
the time. Thus the average of

cos 2vt

is zero because it is positive half the time and negative half

i 2

is simply

I 2>2.

The square root of this is

Irms:

Irms = I
22

    (root-mean-square value of a sinusoidal current)

(31.4)

G

Diode
(arrowhead
and bar indicate the directions in
which current can and cannot pass)

(b) Graph of the full-wave rectified current
and its average value, the rectified average
current Irav

i

Rectified current through
galvanometer G

I
Irav

O

t

Area under curve 5 total charge that
flows through galvanometer in time t.

31.4 Calculating the root-mean-square
(rms) value of an alternating current.

Meaning of the rms value of a sinusoidal
quantity (here, ac current with I 5 3 A):

1

2

3

4

Graph current i versus time.

Square the instantaneous current i.
Take the average (mean) value of i 2.

Take the square root of that average.

i, i 2

i 2 5 I 2 cos2 vt

(i 2)av

5

I 2
2

3

4

I 2 5 9A2

I 5 3A

O

2I

2

1

i 5 I cos vt

5

Irms

(i 2)av

5

t

I
2
