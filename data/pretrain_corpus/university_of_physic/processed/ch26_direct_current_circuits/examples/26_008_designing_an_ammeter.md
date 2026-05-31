Example 26.8
Designing an ammeter
What shunt resistance is required to make the 1.00-mA, 
meter described above into an ammeter with a range of 0 to 
50.0 mA?
SOLUTION
IDENTIFY and SET UP: Since the meter is being used as an amme-
ter, its internal connections are as shown in Fig. 26.15a. Our target
variable is the shunt resistance 
, which we will find using 
Eq. (26.7). The ammeter must handle a maximum current
The coil resistance is 
and the
meter shows full-scale deflection when the current through the coil
is
EXECUTE: Solving Eq. (26.7) for 
we find
= 0.408 Æ
Rsh =
IfsRc
Ia
-
Ifs
=
11.00 * 10-3 A2120.0 Æ2
50.0 * 10-3 A - 1.00 * 10-3 A
Rsh,
Ifs = 1.00 * 10-3 A.
Rc = 20.0 Æ,
Ia = 50.0 * 10-3 A.
Rsh
20.0-Æ
EVALUATE: It’s useful to consider the equivalent resistance 
of
the ammeter as a whole. From Eq. (26.2),
The shunt resistance is so small in comparison to the coil resist-
ance that the equivalent resistance is very nearly equal to the shunt
resistance. The result is an ammeter with a low equivalent resist-
ance and the desired 0-50.0-mA range. At full-scale deflection,
the current through the galvanometer is 1.00
mA, the current through the shunt resistor is 49.0 mA, and
If the current I is less than 50.0 mA, the coil cur-
rent and the deflection are proportionally less.
Vab = 0.0200 V.
I = Ia = 50.0 mA,
= 0.400 Æ
Req = a 1
Rc
+
1
Rsh
b
-1
= a
1
20.0 Æ +
1
0.408 Æ b
-1
Req
Application Electromyography
A fine needle containing two electrodes is
being inserted into a muscle in this patient’s
hand. By using a sensitive voltmeter to mea-
sure the potential difference between these
electrodes, a physician can probe the muscle’s
electrical activity. This is an important 
technique for diagnosing neurological and 
neuromuscular diseases.
Voltmeters
This same basic meter may also be used to measure potential difference or
voltage. A voltage-measuring device is called a voltmeter. A voltmeter always
measures the potential difference between two points, and its terminals must be
connected to these points. (Example 25.6 in Section 25.4 described what can hap-
pen if a voltmeter is connected incorrectly.) As we discussed in Section 25.4, an
ideal voltmeter would have infinite resistance, so connecting it between two points
in a circuit would not alter any of the currents. Real voltmeters always have finite
resistance, but a voltmeter should have large enough resistance that connecting it
in a circuit does not change the other currents appreciably.
For the meter described in Example 26.8 the voltage across the meter coil at
full-scale deflection is only 
We
can extend this range by connecting a resistor 
in series with the coil (Fig.
26.15b). Then only a fraction of the total potential difference appears across the
coil itself, and the remainder appears across 
For a voltmeter with full-scale
reading 
we need a series resistor 
in Fig. 26.15b such that
(for a voltmeter)
(26.8)
VV = Ifs1Rc + Rs2  
Rs
VV,
Rs.
Rs
IfsRc = 11.00 * 10-3 A2120.0 Æ2 = 0.0200 V.

862
CHAPTER 26 Direct-Current Circuits
