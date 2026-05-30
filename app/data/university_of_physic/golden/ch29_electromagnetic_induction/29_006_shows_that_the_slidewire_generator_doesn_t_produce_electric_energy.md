---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.6
subtitle: shows that the slidewire generator doesn’t produce electric energy
needs_review: true
---

# Example 29.6: shows that the slidewire generator doesn’t produce electric energy

## Problem
In the slidewire generator of Example 29.5, energy is dissipated in the circuit owing to its resistance. Let the resistance of the circuit (made up of the moving slidewire and the U-shaped conductor that connects the ends of the slidewire) at a given point in the slidewire’s motion be \(R\). Find the rate at which energy is dissipated in the circuit and the rate at which work must be done to move the rod through the magnetic field.

## Setup
**IDENTIFY and SET UP:** The target variables are the rates at which energy is dissipated and at which work is done.

Energy is dissipated in the circuit at the rate
\[
P_{\text{dissipated}} = I^2 R.
\]

The current \(I\) in the circuit equals
\[
I = \frac{|\mathcal{E}|}{R}.
\]

From Example 29.5, the induced emf in this circuit is
\[
\mathcal{E} = -BLv.
\]

There is a magnetic force on the rod,
\[
\mathbf{F} = I\,\mathbf{L} \times \mathbf{B},
\]
where \(\mathbf{L}\) points along the rod in the direction of the current. Figure 29.12 shows that this force is opposite to the rod velocity \(\mathbf{v}\). To maintain the motion, whoever is pushing the rod must apply a force of equal magnitude in the direction of \(\mathbf{v}\). This force does work at the rate
\[
P_{\text{applied}} = Fv.
\]

## Solution
**EXECUTE:** First calculate the current:
\[
I = \frac{|\mathcal{E}|}{R} = \frac{BLv}{R}.
\]

Hence
\[
P_{\text{dissipated}} = I^2 R
= \left(\frac{BLv}{R}\right)^2 R
= \frac{B^2 L^2 v^2}{R}.
\]

To calculate \(P_{\text{applied}}\), first calculate the magnitude of the magnetic force:
\[
F = ILB.
\]

Since \(\mathbf{L}\) and \(\mathbf{B}\) are perpendicular, this magnitude is
\[
F = BL\left(\frac{BLv}{R}\right)
= \frac{B^2 L^2 v}{R}.
\]

The applied force has the same magnitude and does work at the rate
\[
P_{\text{applied}} = Fv = \frac{B^2 L^2 v^2}{R}.
\]

## Evaluation
The rate at which work is done is exactly equal to the rate at which energy is dissipated in the resistance.

The emf of a slidewire generator is constant if \(v\) is constant. Hence the slidewire generator is a direct-current generator. It’s not a very practical device because the rod eventually moves beyond the U-shaped conductor and loses contact, after which the current stops.

## Key concepts used
- Induced emf in a moving rod: \(\mathcal{E} = -BLv\)
- Ohm’s law for the circuit: \(I = |\mathcal{E}|/R\)
- Power dissipated in resistance: \(P = I^2R\)
- Magnetic force on a current-carrying rod: \(\mathbf{F} = I\,\mathbf{L} \times \mathbf{B}\)
- Mechanical power supplied: \(P = Fv\)
- Energy conservation: mechanical power input equals electrical power dissipated
