---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.2
example_number: 29.5
subtitle: Generator III: The slidewire generator
needs_review: true
---

# Example 29.5: Generator III: The slidewire generator

## Problem
Figure 29.11 shows a U-shaped conductor in a uniform magnetic field directed into the page and perpendicular to the plane of the figure. A metal rod (“slidewire”) of length \(L\) spans the two arms of the conductor, forming a circuit, and is moved to the right with constant velocity \(v\). This induces an emf and a current.

Find the magnitude and direction of the resulting induced emf.

## Setup
**IDENTIFY and SET UP:** The magnetic flux changes because the area of the loop—bounded on the right by the moving rod—is increasing.

The target variable is the emf induced in this expanding loop. The magnetic field is uniform over the area of the loop, so the flux can be found using
\[
\Phi_B = BA\cos\phi.
\]

We choose the area vector \(\vec A\) to point straight into the page, in the same direction as \(\vec B\). With this choice, a positive emf will be one that is directed clockwise around the loop.

## Solution
**EXECUTE:** Since \(\vec B\) and \(\vec A\) point in the same direction, the angle is
\[
\phi = 0,
\]
so
\[
\cos\phi = 1.
\]

The magnetic field magnitude \(B\) is constant, so the induced emf is
\[
\mathcal{E} = -\frac{d\Phi_B}{dt}
= -\frac{d(BA)}{dt}
= -B\frac{dA}{dt}.
\]

To calculate \(\frac{dA}{dt}\), note that in a time \(dt\) the sliding rod moves a distance \(v\,dt\), and the loop area increases by an amount
\[
dA = L\,v\,dt.
\]
Hence,
\[
\frac{dA}{dt} = Lv,
\]
and the induced emf is
\[
\mathcal{E} = -BLv.
\]

The minus sign tells us that the emf is directed counterclockwise around the loop. The induced current is also counterclockwise, as shown in the figure.

## Evaluation
The magnitude of the induced emf is
\[
|\mathcal{E}| = BLv.
\]
Its direction is counterclockwise, which is consistent with Lenz’s law: the increasing flux into the page is opposed by a current that produces a field out of the page.

## Key concepts used
- Magnetic flux through a loop: \(\Phi_B = BA\cos\phi\)
- Faraday’s law of induction: \(\mathcal{E} = -\,d\Phi_B/dt\)
- Area change from a sliding conductor: \(dA = L\,v\,dt\)
- Lenz’s law gives the sign and current direction
