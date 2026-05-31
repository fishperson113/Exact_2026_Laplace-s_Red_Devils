---
source: Fundamentals of Physics
chapter: 25
section: 25-6
sample_problem_number: 25.06
subtitle: Dielectric partially filling the gap in a capacitor
needs_review: true
---

# Sample Problem 25.06: Dielectric partially filling the gap in a capacitor

## Problem
Figure 25-17 shows a parallel-plate capacitor of plate area \(A\) and plate separation \(d\). A potential difference \(V_0\) is applied between the plates by connecting a battery between them. The battery is then disconnected, and a dielectric slab of thickness \(b\) and dielectric constant \(k\) is placed between the plates as shown. Assume \(A = 115\ \text{cm}^2\), \(d = 1.24\ \text{cm}\), \(V_0 = 85.5\ \text{V}\), \(b = 0.780\ \text{cm}\), and \(k = 2.61\).

(a) What is the capacitance \(C_0\) before the dielectric slab is inserted?

(b) What free charge appears on the plates?

(c) What is the electric field \(E_0\) in the gaps between the plates and the dielectric slab?

(d) What is the electric field \(E_1\) in the dielectric slab?

(e) What is the potential difference \(V\) between the plates after the slab has been introduced?

(f) What is the capacitance with the slab in place?

## Key ideas
- Use the parallel-plate capacitor formula \(C_0 = \varepsilon_0 A/d\).
- After the battery is disconnected, the free charge \(q\) on the plates remains unchanged.
- Apply Gauss’ law with a dielectric to find the fields:
  - in the gap, \(E_0 = q/(\varepsilon_0 A)\),
  - in the dielectric, \(E_1 = E_0/k\).
- Find the potential difference by integrating the field across the two regions:
  \[
  V = E_0(d-b) + E_1 b.
  \]
- Then use \(C = q/V\).

## Solution
**(a)** From Eq. 25-9,
\[
C_0 = \varepsilon_0 \frac{A}{d}.
\]
With \(A = 115\ \text{cm}^2 = 115\times 10^{-4}\ \text{m}^2\) and \(d = 1.24\ \text{cm} = 1.24\times 10^{-2}\ \text{m}\),
\[
C_0 = (8.85\times 10^{-12}\ \text{F/m})\frac{115\times 10^{-4}\ \text{m}^2}{1.24\times 10^{-2}\ \text{m}}
= 8.21\times 10^{-12}\ \text{F}.
\]

**(b)** From Eq. 25-1,
\[
q = C_0 V_0 = (8.21\times 10^{-12}\ \text{F})(85.5\ \text{V})
= 7.02\times 10^{-10}\ \text{C}.
\]
Because the battery was disconnected before the slab was inserted, the free charge is unchanged.

**(c)** We apply Gauss’ law, in the form of Eq. 25-36, to Gaussian surface I in Fig. 25-17. That surface passes through the gap, and so it encloses only the free charge on the upper capacitor plate. Electric field pierces only the bottom of the Gaussian surface. Because there the area vector and the field vector are both directed downward, the dot product in Eq. 25-36 becomes
\[
\varepsilon_0 \int \vec E_0\cdot d\vec A = q.
\]
The integration gives the plate area \(A\). Thus,
\[
\varepsilon_0 E_0 A = q,
\]
or
\[
E_0 = \frac{q}{\varepsilon_0 A}.
\]
We must put \(k = 1\) here because Gaussian surface I does not pass through the dielectric. Thus,
\[
E_0 = \frac{7.02\times 10^{-10}\ \text{C}}{(8.85\times 10^{-12}\ \text{F/m})(1)(115\times 10^{-4}\ \text{m}^2)}
= 6.90\times 10^3\ \text{V/m}.
\]

**(d)** Now we apply Gauss’ law in the form of Eq. 25-36 to Gaussian surface II in Fig. 25-17. Only the free charge \(q\) is in Eq. 25-36, so
\[
\varepsilon_0 k E_1 A = q.
\]
Thus,
\[
E_1 = \frac{q}{\varepsilon_0 k A} = \frac{E_0}{k}.
\]
With \(k = 2.61\),
\[
E_1 = \frac{6.90\ \text{kV/m}}{2.61} = 2.64\ \text{kV/m}.
\]

**(e)** We find \(V\) by integrating along a straight line directly from the bottom plate to the top plate. Within the dielectric, the path length is \(b\) and the electric field is \(E_1\). Within the two gaps above and below the dielectric, the total path length is \(d-b\) and the electric field is \(E_0\). Equation 25-6 then gives
\[
V = \int \vec E\cdot d\vec s = E_0(d-b) + E_1 b.
\]
So,
\[
V = (6900\ \text{V/m})(0.0124\ \text{m} - 0.00780\ \text{m}) + (2640\ \text{V/m})(0.00780\ \text{m})
= 52.3\ \text{V}.
\]
This is less than the original potential difference of \(85.5\ \text{V}\).

**(f)** The capacitance \(C\) is related to \(q\) and \(V\) via Eq. 25-1:
\[
C = \frac{q}{V}.
\]
Taking \(q\) from (b) and \(V\) from (e),
\[
C = \frac{7.02\times 10^{-10}\ \text{C}}{52.3\ \text{V}}
= 1.34\times 10^{-11}\ \text{F}.
\]

## Answer
\[
C_0 = 8.21\times 10^{-12}\ \text{F} = 8.21\ \text{pF}
\]
\[
q = 7.02\times 10^{-10}\ \text{C} = 702\ \text{pC}
\]
\[
E_0 = 6.90\times 10^3\ \text{V/m} = 6.90\ \text{kV/m}
\]
\[
E_1 = 2.64\times 10^3\ \text{V/m} = 2.64\ \text{kV/m}
\]
\[
V = 52.3\ \text{V}
\]
\[
C = 1.34\times 10^{-11}\ \text{F} = 13.4\ \text{pF}
\]

## Key concepts used
- Capacitance of a parallel-plate capacitor
- Charge on an isolated capacitor after battery disconnection
- Gauss’ law with a dielectric
- Electric field in dielectric and vacuum regions
- Potential difference as a line integral of \(\vec E\)
- Relation \(q = CV\)
