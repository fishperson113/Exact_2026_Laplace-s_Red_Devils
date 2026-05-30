---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.3
example_number: 21.3
subtitle: Vector addition of electric forces on a line
needs_review: true
---

# Example 21.3: Vector addition of electric forces on a line

## Problem
Two point charges are located on the x-axis of a coordinate system: \(q_1\) is at \(x = 0\), \(q_2\) is at \(x = +2.0\ \text{cm}\), and \(q_3 = 5.0\ \text{nC}\) is at \(x = +4.0\ \text{cm}\). Also \(q_1 = 1.0\ \text{nC}\) and \(q_2 = -3.0\ \text{nC}\). What is the total electric force exerted by \(q_1\) and \(q_2\) on a charge \(q_3\) at \(x = +4.0\ \text{cm}\)?

## Setup
IDENTIFY and SET UP: Figure 21.13a shows the situation. To find the total force on \(q_3\), we find the vector sum of the two electric forces on it.

Figure 21.13b is a free-body diagram for \(q_3\), which is repelled by \(q_1\) (which has the same sign) and attracted to \(q_2\) (which has the opposite sign): \(F_{1\text{ on }3}\) is in the \(-x\)-direction and \(F_{2\text{ on }3}\) is in the \(+x\)-direction.

## Solution
After unit conversions, we have from Eq. (21.2)
\[
F_{1\text{ on }3}
= \frac{1}{4\pi\varepsilon_0}\frac{|q_1 q_3|}{r_{13}^2}
= (19.0\times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2)
\frac{(1.0\times 10^{-9}\ \text{C})(5.0\times 10^{-9}\ \text{C})}{(0.040\ \text{m})^2}
= 1.12\times 10^{-4}\ \text{N}
= 112\ \text{mN}.
\]
So
\[
\vec F_{1\text{ on }3} = 1.12\times 10^{-4}\ \text{N}\,(-\hat{\mathbf i}).
\]

In the same way,
\[
F_{2\text{ on }3} = 84\ \text{mN},
\]
so
\[
\vec F_{2\text{ on }3} = 84\ \text{mN}\,(\hat{\mathbf i}).
\]

We thus have
\[
\vec F_3 = \vec F_{1\text{ on }3} + \vec F_{2\text{ on }3}
= (-112\ \text{mN})\hat{\mathbf i} + (84\ \text{mN})\hat{\mathbf i}
= (-28\ \text{mN})\hat{\mathbf i}.
\]

## Evaluation
As a check, note that the magnitude of \(q_2\) is three times that of \(q_1\), but \(q_2\) is twice as far from \(q_3\) as \(q_1\). Equation (21.2) then says that \(F_{2\text{ on }3}\) must be \(3/4 = 0.75\) as large as \(F_{1\text{ on }3}\). This agrees with our calculated values:
\[
\frac{F_{2\text{ on }3}}{F_{1\text{ on }3}} = \frac{84\ \text{mN}}{112\ \text{mN}} = 0.75.
\]
Because \(F_{2\text{ on }3}\) is the weaker force, the direction of the net force is that of \(F_{1\text{ on }3}\)—that is, in the negative x-direction.

## Key concepts used
- Coulomb’s law for the magnitude of the electric force between two point charges.
- The electric force is a vector and must be added by direction.
- Like charges repel and unlike charges attract.
- On a line, vector addition reduces to signed arithmetic along the x-axis.
