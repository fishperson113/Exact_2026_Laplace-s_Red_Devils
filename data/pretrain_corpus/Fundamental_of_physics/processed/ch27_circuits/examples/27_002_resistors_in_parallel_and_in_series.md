Sample Problem 27.02
Resistors in parallel and in series 
Figure 27-11a shows a multiloop circuit containing one ideal
battery and four resistances with the following values:
(a) What is the current through the battery?
KEY IDEA
Noting that the current through the battery must also be
the current through R1, we see that we might find the
current by applying the loop rule to a loop that includes R1
because the current would be included in the potential
difference across R1.
Incorrect method: Either the left-hand loop or the big loop
should do. Noting that the emf arrow of the battery points
upward, so the current the battery supplies is clockwise, we
might apply the loop rule to the left-hand loop, clockwise
from point a. With i being the current through the battery,
we would get
%# # iR1 # iR2 # iR4 ! 0
(incorrect).
However, this equation is incorrect because it assumes
that R1, R2, and R4 all have the same current i. Resistances
R1 and R4 do have the same current, because the current
passing through R4 must pass through the battery and then
through R1 with no change in value. However, that current
splits at junction point b-only part passes through R2, the
rest through R3.
Dead-end method: To distinguish the several currents in
the circuit, we must label them individually as in Fig. 27-11b.
Then, circling clockwise from a, we can write the loop rule
for the left-hand loop as
%# # i1R1 # i2R2 # i1R4 ! 0.
Unfortunately, this equation contains two unknowns, i1 and
i2; we would need at least one more equation to find them.
Successful method: A much easier option is to simplify
the circuit of Fig. 27-11b by finding equivalent resistances.
Note carefully that R1 and R2 are not in series and thus
cannot be replaced with an equivalent resistance.
However, R2 and R3 are in parallel, so we can use either
Eq. 27-24 or Eq. 27-25 to find their equivalent resistance
R23. From the latter,
R23 !
R2R3
R2 % R3
! (20 0)(30 0)
50 0
! 12 0.
R3 ! 30 0,  R4 ! 8.0 0.
R1 ! 20 0,  R2 ! 20 0,  # ! 12 V,
Additional examples, video, and practice available at WileyPLUS

785
27-2 MULTILOOP CIRCUITS
Figure 27-11 (a) A circuit with an ideal battery. (b) Label the currents. (c) Replacing the parallel resistors with their equivalent.
(d)-(g) Working backward to find the currents through the parallel resistors.
R 2
(a)
a
+
-
R 4
R 1
c
b
R 3
R 2
a
+
-
R 4
R 1
c
b
R 3
 i 2
 i 1
 i 1
 i 3
(b)
a
c
+
-
R 4 = 8.0 Ω
R 1 = 20 Ω
b
 i 1
R 23 = 12 Ω
 i 1
 i 1
(c)
The equivalent of parallel
resistors is smaller.
a
+
-
R 4 = 8.0 Ω
R 1 = 20 Ω
b
 i 1 = 0.30 A
 i 1 = 0.30 A
 i 1 = 0.30 A
(d)
R 23 = 12 Ω
= 12 V
a
c
c
c
c
+
-
R 4 = 8.0 Ω
R 1 = 20 Ω
b
 i 1 = 0.30 A
 i 1 = 0.30 A
 i 1 = 0.30 A
(e)
R 23 = 12 Ω
V 23 = 3.6 V
= 12 V
Applying the loop rule
yields the current.
Applying V = iR yields
the potential difference.
+
-
R 4 = 8.0 Ω
R 1 = 20 Ω
 i 1 = 0.30 A
 i 1 = 0.30 A
 i 2
 i 3
(f )
R 2 = 20 Ω
V 2 = 3.6 V
V 3 = 3.6 V
= 12 V
R 3 = 30 Ω
+
-
R 4 = 8.0 Ω
R 1 = 20 Ω
 i 1 = 0.30 A
 i 1 = 0.30 A
(g)
R 2 = 20 Ω
i 2 = 0.18 A
i 3 = 0.12 A
V 2 = 3.6 V
V 3 = 3.6 V
= 12 V
R 3 = 30 Ω
Parallel resistors and
their equivalent have
the same V (“par-V”).
Applying i = V/R
yields the current.
b
b
A

786
CHAPTER 27
CIRCUITS
The total resistance Rrow along a row is the sum of the inter-
nal resistances of the 5000 electroplaques:
Rrow ! 5000r ! (5000)(0.25 0) ! 1250 0.
We can now represent each of the 140 identical rows as hav-
ing a single emf #row and a single resistance Rrow (Fig. 27-12b).
In Fig. 27-12b, the emf between point a and point b on
any row is #row ! 750 V. Because the rows are identical and
because they are all connected together at the left in
Fig. 27-12b, all points b in that figure are at the same electric
potential. Thus, we can consider them to be connected so
that there is only a single point b. The emf between point a
and this single point b is #row ! 750 V, so we can draw the
circuit as shown in Fig. 27-12c.
Between points b and c in Fig. 27-12c are 140 resistances
Rrow ! 1250 0, all in parallel. The equivalent resistance Req
of this combination is given by Eq. 27-24 as
or
Req ! Rrow
140 ! 1250 0
140
! 8.93 0.
1
Req
! '
140
j!1
1
Rj
! 140
1
Rrow
,
