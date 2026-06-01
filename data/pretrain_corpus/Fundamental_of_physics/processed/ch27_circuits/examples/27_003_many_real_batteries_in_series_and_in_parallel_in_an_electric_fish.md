Sample Problem 27.03
Many real batteries in series and in parallel in an electric fish
Electric fish can generate current with biological emf cells
called electroplaques. In the South American eel they are
arranged in 140 rows, each row stretching horizontally along
the body and each containing 5000 cells, as suggested by
Fig. 27-12a. Each electroplaque has an emf # of 0.15 V and
an internal resistance r of 0.25 0.The water surrounding the
eel completes a circuit between the two ends of the electro-
plaque array, one end at the head of the animal and the
other near the tail.
(a) If the surrounding water has resistance Rw ! 800 0, how
much current can the eel produce in the water?
KEY IDEA
We can simplify the circuit of Fig. 27-12a by replacing 
combinations of emfs and internal resistances with equiva-
lent emfs and resistances.
Calculations: We first consider a single row. The total emf
#row along a row of 5000 electroplaques is the sum of the emfs:
#row ! 5000# ! (5000)(0.15 V) ! 750 V.
Figure 27-12 (a) A model of the electric circuit of an eel in water. Along each of 140 rows extending from the head to the tail of the eel,there are
5000 electroplaques.The surrounding water has resistance Rw.(b) The emf #row and resistance Rrow of each row.(c) The emf between points a
and b is #row.Between points b and c are 140 parallel resistances Rrow.(d) The simplified circuit.
Rw
i
(b)
a
c
row
Rrow
row
Rrow
row
Rrow
b
b
b
Rw
(c)
a
c
row
Rrow
b
= 750 V
Rw
(d)
row
Req
+ -
i
Rw
(a)
r
Electroplaque
 5000 electroplaques per row
140 rows
-
+
750 V
-
+
-
+
-
+
-
+
-
+
-
+
-
+
-
+
-
+
-
+
-
+
-
+
Rrow
Rrow
a
b
c
First, reduce each row to one emf and one resistance.
Emfs in parallel
act as a single emf.
Replace the parallel
resistances with their
equivalent.
Points with the same
potential can be taken
as though connected.

787
27-2 MULTILOOP CIRCUITS
Replacing the parallel combination with Req, we obtain the
simplified circuit of Fig. 27-12d. Applying the loop rule to
this circuit counterclockwise from point b, we have
#row # iRw # iReq ! 0.
Solving for i and substituting the known data, we find
(Answer)
If the head or tail of the eel is near a fish, some of this
current could pass along a narrow path through the fish,
stunning or killing it.
! 0.927 A % 0.93 A.
i !
# row
Rw % Req
!
750 V
800 0 % 8.93 0
(b) How much current irow travels through each row of 
Fig. 27-12a?
KEY IDEA
Because the rows are identical, the current into and out of
the eel is evenly divided among them.
Calculation: Thus, we write
(Answer)
Thus, the current through each row is small, so that the eel
need not stun or kill itself when it stuns or kills a fish.
irow !
i
140 ! 0.927 A
140
! 6.6 $ 10 #3 A.
Combining equations: We now have a system of two equa-
tions (Eqs. 27-27 and 27-28) in two unknowns (i1 and i2) to
solve either “by hand” (which is easy enough here) or with a
“math package.” (One solution technique is Cramer’s rule,
given in Appendix E.) We find
i1 ! #0.50 A.
(27-29)
(The minus sign signals that our arbitrary choice of direction
for i1 in Fig. 27-13 is wrong, but we must wait to correct it.)
Substituting i1 ! #0.50 A into Eq. 27-28 and solving for
i2 then give us
i2 ! 0.25 A.
(Answer)
With Eq. 27-26 we then find that
i3 ! i1 % i2 ! #0.50 A % 0.25 A
! #0.25 A.
The positive answer we obtained for i2signals that our choice of
direction for that current is correct. However, the negative an-
swers for i1 and i3 indicate that our choices for those currents are
wrong.Thus,as a last step here,we correct the answers by revers-
ing the arrows for i1 and i3 in Fig.27-13 and then writing
i1 ! 0.50 A
and
i3 ! 0.25 A.
(Answer)
Caution: Always make any such correction as the last step
and not before calculating all the currents.
Figure 27-13 shows a circuit whose elements have the fol-
lowing values:
The three batteries are ideal batteries. Find the mag-
nitude and direction of the current in each of the three
branches.
KEY IDEAS
It is not worthwhile to try to simplify this circuit, because no
two resistors are in parallel, and the resistors that are in series
(those in the right branch or those in the left branch) present
no problem.So,our plan is to apply the junction and loop rules.
Junction rule: Using arbitrarily chosen directions for the cur-
rents as shown in Fig. 27-13, we apply the junction rule at point
a by writing
i3 ! i1 % i2.
(27-26)
An application of the junction rule at junction b gives only
the same equation, so we next apply the loop rule to any two
of the three loops of the circuit.
Left-hand loop: We first arbitrarily choose the left-hand
loop, arbitrarily start at point b, and arbitrarily traverse the
loop in the clockwise direction, obtaining
#i1R1 % #1 # i1R1 # (i1 % i2)R2 # #2 ! 0,
where we have used (i1 % i2) instead of i3 in the middle
branch. Substituting the given data and simplifying yield
i1(8.0 0) % i2(4.0 0) ! #3.0 V.
(27-27)
Right-hand loop: For our second application of the loop
rule, we arbitrarily choose to traverse the right-hand loop
counterclockwise from point b, finding
#i2R1 % #2 # i2R1# (i1% i2)R2 # #2! 0.
Substituting the given data and simplifying yield
i1(4.0 0) % i2(8.0 0) ! 0.
(27-28)
4.0 0.
R2 !
R1 ! 2.0 0,
# 1 ! 3.0 V, # 2 ! 6.0 V,
Figure 27-13 A multi-
loop circuit with three
ideal batteries and five
resistances.
+
-
1
2
R 2
R1
R1
R1
R1
+
-
+
-
2
i1
i2
i1
i2
a
b
i3
Additional examples, video, and practice available at WileyPLUS
