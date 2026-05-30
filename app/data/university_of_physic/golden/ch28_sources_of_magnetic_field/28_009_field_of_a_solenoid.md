---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.7
example_number: 28.9
subtitle: Field of a solenoid
needs_review: true
---

# Example 28.9: Field of a solenoid

## Problem
Use Ampere’s law to find the field at or near the center of a long, closely wound solenoid if it has \(n\) turns per unit length and carries current \(I\).

## Setup
**IDENTIFY and SET UP:** We assume that \(\mathbf{B}\) is uniform inside the solenoid and zero outside. Figure 28.23 shows the situation and our chosen integration path, rectangle \(abcd\). Side \(ab\), with length \(L\), is parallel to the axis of the solenoid. Sides \(bc\) and \(da\) are taken to be very long so that side \(cd\) is far from the solenoid; then the field at side \(cd\) is negligibly small.

## Solution
**EXECUTE:** Along side \(ab\), \(\mathbf{B}\) is parallel to the path and is constant. Our Ampere’s-law integration takes us along side \(ab\) in the same direction as \(\mathbf{B}\), so here \(\mathbf{B}\cdot d\mathbf{l} = B\,dl\) and
\[
\int_{ab} \mathbf{B}\cdot d\mathbf{l} = BL.
\]

Along sides \(bc\) and \(da\), \(\mathbf{B}\) is perpendicular to the path and so \(\mathbf{B}\cdot d\mathbf{l}=0\); along side \(cd\), \(\mathbf{B}=0\) and so \(\mathbf{B}\cdot d\mathbf{l}=0\). Around the entire closed path, then, we have
\[
\oint \mathbf{B}\cdot d\mathbf{l} = BL.
\]

In a length \(L\) there are \(nL\) turns, each of which passes once through \(abcd\) carrying current \(I\). Hence the total current enclosed by the rectangle is
\[
I_{\text{encl}} = nLI.
\]

Ampere’s law then gives
\[
BL = \mu_0 nLI,
\]
or
\[
B = \mu_0 n I \qquad \text{(solenoid)}.
\]

Side \(ab\) need not lie on the axis of the solenoid, so this result demonstrates that the field is uniform over the entire cross section at the center of the solenoid’s length.

## Evaluation
Note that the direction of \(\mathbf{B}\) inside the solenoid is in the same direction as the solenoid’s vector magnetic moment \(\mathbf{M}\), as we found in Section 28.5 for a single current-carrying loop.

For points along the axis, the field is strongest at the center of the solenoid and drops off near the ends. For a solenoid very long in comparison to its diameter, the field magnitude at each end is exactly half that at the center. This is approximately the case even for a relatively short solenoid, as Fig. 28.24 shows.

## Key concepts used
- Ampere’s law: \(\displaystyle \oint \mathbf{B}\cdot d\mathbf{l}=\mu_0 I_{\text{encl}}\)
- Long, closely wound solenoid approximation: \(\mathbf{B}\) uniform inside, negligible outside
- Current enclosed by an Amperian loop: \(I_{\text{encl}} = nLI\)
- Result for the magnetic field inside a solenoid: \(\displaystyle B=\mu_0 n I\)
