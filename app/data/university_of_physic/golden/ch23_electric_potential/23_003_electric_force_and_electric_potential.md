---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.2
example_number: 23.3
subtitle: Electric force and electric potential
needs_review: true
---

# Example 23.3: Electric force and electric potential

## Problem
A proton with charge \(+e = 1.602 \times 10^{-19}\,\text{C}\) moves a distance \(d = 0.50\,\text{m}\) in a straight line between points \(a\) and \(b\) in a linear accelerator. The electric field is uniform along this line, with magnitude \(E = 1.5 \times 10^{7}\,\text{V/m} = 1.5 \times 10^{7}\,\text{N/C}\), in the direction from \(a\) to \(b\). Determine:

(a) the force on the proton;  
(b) the work done on it by the field;  
(c) the potential difference \(V_a - V_b\).

## Setup
IDENTIFY and SET UP: This problem uses the relationship between electric field and electric force. It also uses the relationship among force, work, and potential-energy difference. We are given the electric field, so it is straightforward to find the electric force on the proton. Calculating the work is also straightforward because \(E\) is uniform, so the force on the proton is constant. Once the work is known, we find \(V_a - V_b\) using Eq. (23.13).

## Solution
EXECUTE:  
(a) The force on the proton is in the same direction as the electric field, and its magnitude is

\[
F = qE = (1.602 \times 10^{-19}\,\text{C})(1.5 \times 10^{7}\,\text{N/C})
= 2.4 \times 10^{-12}\,\text{N}
\]

(b) The force is constant and in the same direction as the displacement, so the work done on the proton is

\[
W_{a\to b} = Fd = (2.4 \times 10^{-12}\,\text{N})(0.50\,\text{m})
= 1.2 \times 10^{-12}\,\text{J}
\]

\[
= \frac{1.2 \times 10^{-12}\,\text{J}}{1.602 \times 10^{-19}\,\text{J/eV}}
= 7.5 \times 10^{6}\,\text{eV} = 7.5\,\text{MeV}
\]

(c) From Eq. (23.13), the potential difference is the work per unit charge, which is

\[
V_a - V_b = \frac{W_{a\to b}}{q}
= \frac{1.2 \times 10^{-12}\,\text{J}}{1.602 \times 10^{-19}\,\text{C}}
= 7.5 \times 10^{6}\,\text{J/C}
= 7.5 \times 10^{6}\,\text{V}
\]

\[
= 7.5\,\text{MV}
\]

We can get this same result even more easily by remembering that 1 electron volt equals 1 volt multiplied by the charge \(e\). The work done is \(7.5 \times 10^{6}\,\text{eV}\) and the charge is \(e\), so the potential difference is \(7.5 \times 10^{6}\,\text{V}\).

## Evaluation
EVALUATE: We can check our result in part (c) by using Eq. (23.17) or Eq. (23.18). The angle \(\phi\) between the constant field \( \vec E \) and the displacement is zero, so Eq. (23.17) becomes

\[
V_a - V_b = \int_a^b E \cos\phi \, dl = \int_a^b E\, dl = E \int_a^b dl = Ed
\]

The integral of \(dl\) from \(a\) to \(b\) is just the distance \(d\), so we again find

\[
V_a - V_b = (1.5 \times 10^{7}\,\text{V/m})(0.50\,\text{m})
= 7.5 \times 10^{6}\,\text{V}
\]

## Key concepts used
- Electric force on a charge in a uniform electric field: \( \vec F = q \vec E \)
- Work done by a constant force: \( W = Fd \) when force and displacement are parallel
- Relation between work and electric potential difference: \( V_a - V_b = W/q \)
- Line integral form of potential difference in an electric field: \( V_a - V_b = \int_a^b \vec E \cdot d\vec l \)
