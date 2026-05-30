---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.1
example_number: 23.2
subtitle: A system of point charges
needs_review: true
---

# Example 23.2: A system of point charges

## Problem
Two point charges are located on the x-axis, at \(x = 0\) and \(x = a\), and at \(x = 2a\).  
(a) Find the work that must be done by an external force to bring a third point charge \(q_3 = +e\) from infinity to \(x = 2a\).  
(b) Find the total potential energy of the system of three charges.

## Setup
**IDENTIFY and SET UP:** Figure 23.10 shows the final arrangement of the three charges. In part (a) we need to find the work \(W\) that must be done on \(q_3\) by an external force to bring \(q_3\) in from infinity to \(x = 2a\). We do this by using Eq. (23.10) to find the potential energy associated with \(q_3\) in the presence of \(q_1\) and \(q_2\). In part (b) we use Eq. (23.11), the expression for the potential energy of a collection of point charges, to find the total potential energy of the system.

## Solution
**EXECUTE:**  
(a) The work \(W\) equals the difference between (i) the potential energy \(U\) associated with \(q_3\) when it is at \(x = 2a\) and (ii) the potential energy when it is infinitely far away. The second of these is zero, so the work required is equal to \(U\).

The distances between the charges are \(r_{23} = a\) and \(r_{13} = 2a\), so from Eq. (23.10),

\[
W = U = \frac{1}{4\pi \varepsilon_0}\left(\frac{q_1 q_3}{r_{13}} + \frac{q_2 q_3}{r_{23}}\right)
= \frac{+e}{4\pi \varepsilon_0}\left(\frac{-e}{2a} + \frac{+e}{a}\right)
= \frac{e^2}{8\pi \varepsilon_0 a}.
\]

This is positive, just as we should expect. If we bring \(q_3\) in from infinity along the \(+x\)-axis, it is attracted by \(q_1\) but is repelled more strongly by \(q_2\). Hence we must do positive work to push \(q_3\) to the position at \(x = 2a\).

(b) From Eq. (23.11), the total potential energy of the three-charge system is

\[
U = \frac{1}{4\pi \varepsilon_0}\sum_{i<j}\frac{q_i q_j}{r_{ij}}
= \frac{1}{4\pi \varepsilon_0}\left(\frac{q_1 q_2}{r_{12}} + \frac{q_1 q_3}{r_{13}} + \frac{q_2 q_3}{r_{23}}\right).
\]

Substituting the charges and distances,

\[
U = \frac{1}{4\pi \varepsilon_0}\left(\frac{(-e)(+e)}{a} + \frac{(-e)(+e)}{2a} + \frac{(+e)(+e)}{a}\right)
= -\frac{e^2}{8\pi \varepsilon_0 a}.
\]

## Evaluation
Our negative result in part (b) means that the system has lower potential energy than it would if the three charges were infinitely far apart. An external force would have to do negative work to bring the three charges from infinity to assemble this entire arrangement and would have to do positive work to move the three charges back to infinity.

## Key concepts used
- Electric potential energy of point charges
- Work done by an external force in bringing a charge from infinity
- Superposition of potential energies for a collection of point charges
- Sign of the total potential energy and its physical interpretation
