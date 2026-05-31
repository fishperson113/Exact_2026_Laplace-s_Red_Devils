---
source: Fundamentals of Physics
chapter: 29
section: 29-1
sample_problem_number: 29.01
subtitle: Magnetic field at the center of a circular arc of current
needs_review: true
---

# Sample Problem 29.01: Magnetic field at the center of a circular arc of current

## Problem
The wire in Fig. 29-8a carries a current \(i\) and consists of a circular arc of radius \(R\) and central angle \(\pi/2\) rad, and two straight sections whose extensions intersect the center \(C\) of the arc. What magnetic field (magnitude and direction) does the current produce at \(C\)?

## Key ideas
We can find the magnetic field at point \(C\) by applying the Biot-Savart law of Eq. 29-3 to the wire, point by point along the full length of the wire. However, the application of Eq. 29-3 can be simplified by evaluating separately for the three distinguishable sections of the wire—namely, the two straight sections and the circular arc.

## Solution
For the two straight sections, the current-length element \(d\vec{s}\) is directed along the line from the section toward \(C\), so the angle between \(d\vec{s}\) and \(\hat{r}\) is zero for one section and \(180^\circ\) for the other. In either case, \(\sin \theta = 0\), so the magnetic field contribution from each straight section is zero:

\[
\vec{B}_1 = 0, \qquad \vec{B}_2 = 0.
\]

Thus only the circular arc contributes to the field at \(C\). For a circular arc of central angle \(\phi\), Eq. 29-9 gives

\[
B = \frac{\mu_0 i \phi}{4\pi R}.
\]

Here \(\phi = \pi/2\), so

\[
B_3 = \frac{\mu_0 i (\pi/2)}{4\pi R} = \frac{\mu_0 i}{8R}.
\]

To determine the direction of \(\vec{B}_3\), use the right-hand rule for the circular arc. Curl the fingers of your right hand in the direction of the current around the arc; your thumb then points in the direction of the magnetic field at the center. In this case the field at \(C\) is into the plane of the page.

Because the straight sections contribute no field, the net magnetic field is just the field of the arc:

\[
\vec{B} = \vec{B}_1 + \vec{B}_2 + \vec{B}_3 = 0 + 0 + \vec{B}_3.
\]

## Answer
\[
B = \frac{\mu_0 i}{8R},
\]
directed into the plane of Fig. 29-8.

## Key concepts used
- Biot-Savart law
- Magnetic field of a circular arc
- Superposition of magnetic fields
- Right-hand rule for current-carrying conductors
