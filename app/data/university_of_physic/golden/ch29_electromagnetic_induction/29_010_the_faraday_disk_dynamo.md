---
source: Young and Freedman University Physics, 13th ed.
chapter: 29
section: 29.5
example_number: 29.10
subtitle: The Faraday disk dynamo
needs_review: true
---

# Example 29.10: The Faraday disk dynamo

## Problem
Figure 29.16 shows a conducting disk with radius \(R\) that lies in the \(xy\)-plane and rotates with constant angular velocity \(\omega\) about the \(z\)-axis. The disk is in a uniform, constant magnetic field \(\mathbf{B}\) in the \(z\)-direction. Find the induced emf between the center and the rim of the disk.

## Setup
**IDENTIFY and SET UP:** A motional emf arises because the conducting disk moves relative to the magnetic field \(\mathbf{B}\). The complication is that different parts of the disk move at different speeds depending on their distance from the rotation axis. We address this by considering small segments of the disk and integrating their contributions to determine the emf between the center and the rim.

Consider the small segment of the disk shown in Fig. 29.16 and labeled by its velocity vector \(\mathbf{v}\). The magnetic force per unit charge on this segment is \(\mathbf{v} \times \mathbf{B}\), which points radially outward from the center of the disk. Hence the induced emf tends to make a current flow radially outward, which tells us that the moving conducting path to think about here is a straight line from the center to the rim. We can find the emf from each small disk segment along this line using
\[
d\mathcal{E} = (\mathbf{v}\times \mathbf{B})\cdot d\mathbf{l}
\]
and then integrate to find the total emf.

## Solution
**EXECUTE:** The length vector \(d\mathbf{l}\) (of length \(dr\)) associated with the segment points radially outward, in the same direction as \(\mathbf{v}\times \mathbf{B}\). The vectors \(\mathbf{v}\) and \(\mathbf{B}\) are perpendicular, and the magnitude of \(\mathbf{v}\times \mathbf{B}\) is \(vB\).

The emf from the segment is then
\[
d\mathcal{E} = vB\,dr.
\]
Since the speed of a point on the disk at radius \(r\) is
\[
v=\omega r,
\]
the segment emf becomes
\[
d\mathcal{E} = \omega r B\,dr.
\]

The total emf is the integral of \(d\mathcal{E}\) from the center \((r=0)\) to the rim \((r=R)\):
\[
\mathcal{E}=\int_0^R \omega r B\,dr
= \omega B \int_0^R r\,dr
= \frac{1}{2}\omega BR^2.
\]

## Evaluation
We can use this device as a source of emf in a circuit by completing the circuit through two stationary brushes (labeled \(b\) in the figure) that contact the disk and its conducting shaft as shown. Such a disk is called a Faraday disk dynamo or a homopolar generator. Unlike the alternator in Example 29.3, the Faraday disk dynamo is a direct-current generator; it produces an emf that is constant in time.

Can you use Lenz’s law to show that for the direction of rotation in Fig. 29.16, the current in the external circuit must be in the direction shown?

## Key concepts used
- Motional emf in a moving conductor: \(d\mathcal{E}=(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}\)
- Speed of a point on a rotating disk: \(v=\omega r\)
- Integration over the radius of the disk
- Faraday disk dynamo as a direct-current generator
- Lenz’s law for current direction
