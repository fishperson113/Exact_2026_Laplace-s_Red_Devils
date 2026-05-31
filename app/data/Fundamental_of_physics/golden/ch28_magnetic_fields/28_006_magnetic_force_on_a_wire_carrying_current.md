---
source: Fundamentals of Physics
chapter: 28
section: 28-7
sample_problem_number: 28.06
subtitle: Magnetic force on a wire carrying current
needs_review: true
---

# Sample Problem 28.06: Magnetic force on a wire carrying current

## Problem
A straight, horizontal length of copper wire has a current \(i = 28\ \text{A}\) through it. What are the magnitude and direction of the minimum magnetic field needed to suspend the wire—that is, to balance the gravitational force on it? The linear density (mass per unit length) of the wire is \(46.6\ \text{g/m}\).

## Key ideas
1. Because the wire carries a current, a magnetic force can act on the wire if we place it in a magnetic field. To balance the downward gravitational force on the wire, we want the magnetic force to be directed upward.
2. The direction of \(\vec{F}_B\) is related to the directions of \(\vec{B}\) and the wire’s length vector \(\vec{L}\) by Eq. 28-26:
   \[
   \vec{F}_B = i\,\vec{L} \times \vec{B}.
   \]

## Solution
Because \(\vec{L}\) is directed horizontally (and the current is taken to be positive), Eq. 28-26 and the right-hand rule for cross products tell us that \(\vec{B}\) must be horizontal and rightward to give the required upward \(\vec{F}_B\).

The magnitude of the magnetic force is
\[
F_B = iLB\sin\phi
\]
(Eq. 28-27). Because we want \(F_B\) to balance \(F_g\), we want
\[
iLB\sin\phi = mg.
\]
To minimize the required magnetic field magnitude \(B\), we maximize \(\sin\phi\). Thus we set
\[
\phi = 90^\circ,
\]
so that \(\vec{B}\) is perpendicular to the wire.

For a wire of unit length, \(L = 1.0\ \text{m}\), and the mass is given by the linear density:
\[
m = (46.6\ \text{g/m})(1.0\ \text{m}) = 46.6\ \text{g} = 4.66\times 10^{-2}\ \text{kg}.
\]
Thus,
\[
B = \frac{mg}{iL}
= \frac{(4.66\times 10^{-2}\ \text{kg})(9.8\ \text{m/s}^2)}{(28\ \text{A})(1.0\ \text{m})}
\approx 1.6\times 10^{-2}\ \text{T}.
\]

## Answer
\[
B_{\min} \approx 1.6\times 10^{-2}\ \text{T}
\]
directed horizontally and rightward, so that \(\vec{F}_B\) is upward and balances the weight of the wire.

## Key concepts used
- Magnetic force on a current-carrying wire: \(\vec{F}_B = i\,\vec{L}\times \vec{B}\)
- Magnitude: \(F_B = iLB\sin\phi\)
- Force balance: \(F_B = mg\)
- Minimum field occurs when \(\phi = 90^\circ\)
