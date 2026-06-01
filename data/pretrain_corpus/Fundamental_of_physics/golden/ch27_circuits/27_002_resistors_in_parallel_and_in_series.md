---
source: Fundamentals of Physics
chapter: 27
section: 27-2
sample_problem_number: 27.02
subtitle: Resistors in parallel and in series
needs_review: true
---

# Sample Problem 27.02: Resistors in parallel and in series

## Problem
Figure 27-11a shows a multiloop circuit containing one ideal battery and four resistances with the following values:

(a) What is the current through the battery?

## Key ideas
KEY IDEA

Noting that the current through the battery must also be the current through R1, we see that we might find the current by applying the loop rule to a loop that includes R1 because the current would be included in the potential difference across R1.

Incorrect method: Either the left-hand loop or the big loop should do. Noting that the emf arrow of the battery points upward, so the current the battery supplies is clockwise, we might apply the loop rule to the left-hand loop, clockwise from point a. With i being the current through the battery, we would get

%# # iR1 # iR2 # iR4 ! 0

(incorrect).

However, this equation is incorrect because it assumes that R1, R2, and R4 all have the same current i. Resistances R1 and R4 do have the same current, because the current passing through R4 must pass through the battery and then through R1 with no change in value. However, that current splits at junction point b-only part passes through R2, the rest through R3.

Dead-end method: To distinguish the several currents in the circuit, we must label them individually as in Fig. 27-11b. Then, circling clockwise from a, we can write the loop rule for the left-hand loop as

%# # i1R1 # i2R2 # i1R4 ! 0.

Unfortunately, this equation contains two unknowns, i1 and i2; we would need at least one more equation to find them.

Successful method: A much easier option is to simplify the circuit of Fig. 27-11b by finding equivalent resistances. Note carefully that R1 and R2 are not in series and thus cannot be replaced with an equivalent resistance.

However, R2 and R3 are in parallel, so we can use either Eq. 27-24 or Eq. 27-25 to find their equivalent resistance R23. From the latter,

R23 !
R2R3
R2 % R3
! (20 0)(30 0)
50 0
! 12 0.

## Solution
R3 ! 30 0,  R4 ! 8.0 0.
R1 ! 20 0,  R2 ! 20 0,  # ! 12 V,

The equivalent of parallel resistors is smaller.

We now replace R2 and R3 by their equivalent resistance R23 = 12 Ω. Then the circuit becomes a simple series combination of R1, R23, and R4.

The total resistance is

R = R1 + R23 + R4
= 20 Ω + 12 Ω + 8.0 Ω
= 40 Ω.

Using I = #/R for the battery current,

i = 12 V / 40 Ω = 0.30 A.

Working backward, the potential difference across R23 is

V23 = iR23 = (0.30 A)(12 Ω) = 3.6 V.

Parallel resistors and their equivalent have the same V (“par-V”), so

V2 = V3 = 3.6 V.

Applying i = V/R gives the branch currents:

i2 = V2/R2 = 3.6 V / 20 Ω = 0.18 A,

i3 = V3/R3 = 3.6 V / 30 Ω = 0.12 A.

A check: i2 + i3 = 0.18 A + 0.12 A = 0.30 A, matching the battery current.

## Answer
The current through the battery is **0.30 A**.

## Key concepts used
- Current is the same through elements in series.
- Resistors in parallel have the same potential difference.
- Equivalent resistance for parallel resistors:
  $$ 
  R_{23}=\frac{R_2R_3}{R_2+R_3}
   $$
- Equivalent resistance for series resistors:
  $$ 
  R=R_1+R_{23}+R_4
   $$
- Ohm’s law:
  $$ 
  V=iR
   $$
- Loop rule and current conservation at junctions.
