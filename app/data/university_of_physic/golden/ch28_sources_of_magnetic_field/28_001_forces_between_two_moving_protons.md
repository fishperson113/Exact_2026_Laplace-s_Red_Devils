---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.1
example_number: 28.1
subtitle: Forces between two moving protons
needs_review: true
---

# Example 28.1: Forces between two moving protons

## Problem
Two protons move parallel to the x-axis in opposite directions (Fig. 28.2) at the same speed, small compared to the speed of light \(c\). At the instant shown, find the electric and magnetic forces on the upper proton and compare their magnitudes.

## Setup
IDENTIFY and SET UP: Coulomb’s law [Eq. (21.2)] gives the electric force on the upper proton. The magnetic force law [Eq. (27.2)] gives the magnetic force on the upper proton; to use it, we must first use Eq. (28.2) to find the magnetic field that the lower proton produces at the position of the upper proton.

The unit vector from the lower proton (the source) to the position of the upper proton is not fully recoverable from the OCR, but the figure indicates the separation is along the \(+y\)-direction. The upper proton is located a distance \(r\) above the lower proton.

## Solution
From Coulomb’s law, the magnitude of the electric force on the upper proton is

\[
F_E=\frac{1}{4\pi\varepsilon_0}\frac{q^2}{r^2}.
\]

The forces are repulsive, and the force on the upper proton is vertically upward (in the \(+y\)-direction).

The velocity of the lower proton is \(-v\hat{\mathbf{i}}\). From the right-hand rule for the cross product in Eq. (28.2), the magnetic field due to the lower proton at the position of the upper proton is in the \(+z\)-direction (see Fig. 28.2). From Eq. (28.2), the field is

\[
\mathbf{B}=\frac{\mu_0}{4\pi}\frac{qv}{r^2}\,\hat{\mathbf{k}}.
\]

The velocity of the upper proton is \(+v\hat{\mathbf{i}}\), so the magnetic force on it is

\[
\mathbf{F}_B=q\mathbf{v}\times\mathbf{B}
=\frac{\mu_0}{4\pi}\frac{q^2v^2}{r^2}\,\hat{\mathbf{j}}.
\]

The magnetic interaction in this situation is also repulsive.

The ratio of the force magnitudes is

\[
\frac{F_B}{F_E}
=
\frac{\mu_0 q^2 v^2/(4\pi r^2)}{q^2/(4\pi\varepsilon_0 r^2)}
=
\mu_0\varepsilon_0 v^2
=
\frac{v^2}{c^2},
\]

where \( \mu_0\varepsilon_0 = 1/c^2 \). When \(v\) is small in comparison to the speed of light, the magnetic force is much smaller than the electric force.

## Evaluation
We have described the velocities, fields, and forces as they are measured by an observer who is stationary in the coordinate system of Fig. 28.2. In a coordinate system that moves with one of the charges, one of the velocities would be zero, so there would be no magnetic force. The explanation of this apparent paradox provided one of the paths that led to the special theory of relativity.

## Key concepts used
- Coulomb’s law for the electric force between two charges
- Magnetic field of a moving point charge
- Magnetic force on a moving charge, \(\mathbf{F}=q\mathbf{v}\times\mathbf{B}\)
- Right-hand rule for cross products
- Relation \(\mu_0\varepsilon_0=1/c^2\)
- Comparison of electric and magnetic force magnitudes
