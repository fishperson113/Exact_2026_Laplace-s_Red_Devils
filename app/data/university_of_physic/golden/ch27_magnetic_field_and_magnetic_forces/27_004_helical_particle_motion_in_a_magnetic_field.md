---
source: Young and Freedman University Physics, 13th ed.
chapter: 27
section: 27.4
example_number: 27.4
subtitle: Helical particle motion in a magnetic field
needs_review: true
---

# Example 27.4: Helical particle motion in a magnetic field

## Problem
In a situation like that shown in Fig. 27.18, the charged particle is a proton and the uniform, 0.500-T magnetic field is directed along the x-axis. At \(t = 0\), the proton has velocity components \(v_x = 1.50 \times 10^5\ \text{m/s}\), \(v_y = 0\), and \(v_z = 2.00 \times 10^5\ \text{m/s}\). Only the magnetic force acts on the proton.

(a) At \(t = 0\), find the force on the proton and its acceleration.

(b) Find the radius of the resulting helical path, the angular speed of the proton, and the pitch of the helix (the distance traveled along the helix axis per revolution).

## Setup
IDENTIFY and SET UP: The magnetic force is \(\vec{F} = q\,\vec{v} \times \vec{B}\); Newton’s second law gives the resulting acceleration. Because \(\vec{F}\) is perpendicular to \(\vec{v}\), the proton’s speed does not change. Hence Eq. (27.11) gives the radius of the helical trajectory if we replace \(v\) with the velocity component perpendicular to \(\vec{B}\). Equation (27.12) gives the angular speed \(\omega\), which yields the time \(T\) for one revolution (the period). Given the velocity component parallel to the magnetic field, we can then determine the pitch.

## Solution
EXECUTE: (a) With \(\vec{B} = B\hat{\mathbf{i}}\) and \(\vec{v} = v_x\hat{\mathbf{i}} + v_z\hat{\mathbf{k}}\),

\[
\vec{F} = q(\vec{v}\times \vec{B}) = q(v_x\hat{\mathbf{i}} + v_z\hat{\mathbf{k}})\times B\hat{\mathbf{i}}
= qv_zB\,\hat{\mathbf{j}}
\]

(Recall that \(\hat{\mathbf{k}}\times \hat{\mathbf{i}} = \hat{\mathbf{j}}\) and \(\hat{\mathbf{i}}\times \hat{\mathbf{i}} = 0\).)

Thus

\[
\vec{F} = (1.60 \times 10^{-19}\ \text{C})(2.00 \times 10^5\ \text{m/s})(0.500\ \text{T})\,\hat{\mathbf{j}}
= 1.60 \times 10^{-14}\ \text{N}\,\hat{\mathbf{j}}
\]

The resulting acceleration is

\[
\vec{a}=\frac{\vec{F}}{m}
= \frac{1.60 \times 10^{-14}\ \text{N}}{1.67 \times 10^{-27}\ \text{kg}}\,\hat{\mathbf{j}}
= 9.58 \times 10^{12}\ \text{m/s}^2\,\hat{\mathbf{j}}
\]

(b) Since \(\vec{v}\perp \vec{B}\) component is \(v_z = 2.00 \times 10^5\ \text{m/s}\), then from Eq. (27.11),

\[
R=\frac{mv_z}{|q|B}
=\frac{(1.67 \times 10^{-27}\ \text{kg})(2.00 \times 10^5\ \text{m/s})}{(1.60 \times 10^{-19}\ \text{C})(0.500\ \text{T})}
= 4.18 \times 10^{-3}\ \text{m} = 4.18\ \text{mm}
\]

From Eq. (27.12) the angular speed is

\[
\omega = \frac{|q|B}{m}
= \frac{(1.60 \times 10^{-19}\ \text{C})(0.500\ \text{T})}{1.67 \times 10^{-27}\ \text{kg}}
= 4.79 \times 10^7\ \text{rad/s}
\]

The period is

\[
T=\frac{2\pi}{\omega}=\frac{2\pi}{4.79 \times 10^7\ \text{s}^{-1}}=1.31 \times 10^{-7}\ \text{s}
\]

The pitch is the distance traveled along the x-axis in this time, or

\[
v_xT=(1.50 \times 10^5\ \text{m/s})(1.31 \times 10^{-7}\ \text{s})
= 0.0197\ \text{m} = 19.7\ \text{mm}
\]

## Evaluation
Although the magnetic force has a tiny magnitude, it produces an immense acceleration because the proton mass is so small. Note that the pitch of the helix is almost five times greater than the radius \(R\), so this helix is much more “stretched out” than that shown in Fig. 27.18.

## Key concepts used
- Magnetic force on a moving charge: \(\vec{F}=q\,\vec{v}\times\vec{B}\)
- Newton’s second law: \(\vec{a}=\vec{F}/m\)
- Circular/helical motion of a charged particle in a uniform magnetic field
- Radius of circular motion: \(R=mv_\perp/(|q|B)\)
- Angular speed: \(\omega=|q|B/m\)
- Period: \(T=2\pi/\omega\)
- Pitch of helix: \(p=v_\parallel T\)
