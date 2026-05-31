---
source: Fundamentals of Physics
chapter: 28
section: 28-5
sample_problem_number: 28.04
subtitle: Uniform circular motion of a charged particle in a magnetic field
needs_review: true
---

# Sample Problem 28.04: Uniform circular motion of a charged particle in a magnetic field

## Problem
Figure 28-12 shows the essentials of a mass spectrometer, which can be used to measure the mass of an ion; an ion of mass \(m\) (to be measured) and charge \(q\) is produced in source \(S\). The initially stationary ion is accelerated by the electric field due to a potential difference \(V\). The ion leaves \(S\) and enters a separator chamber in which a uniform magnetic field is perpendicular to the path of the ion. A wide detector lines the bottom wall of the chamber, and the magnetic field causes the ion to move in a semicircle and thus strike the detector. Suppose that \(B = 80.000\ \text{mT}\), \(V = 1000.0\ \text{V}\), and ions of charge \(q = +1.6022 \times 10^{-19}\ \text{C}\) strike the detector at a point that lies at \(x = 1.6254\ \text{m}\). What is the mass \(m\) of the individual ions, in atomic mass units \((1\ \text{u} = 1.6605 \times 10^{-27}\ \text{kg})\)?

## Key ideas
1. Because the uniform magnetic field causes the charged ion to follow a circular path, we can relate the ion’s mass \(m\) to the path’s radius \(r\) with Eq. 28-16:
   \[
   r=\frac{mv}{Bq}.
   \]
2. From Fig. 28-12, \(r=x/2\) because the ion travels in a semicircle.
3. To find the speed \(v\), use conservation of mechanical energy during the acceleration through the potential difference \(V\).

## Solution
When the ion emerges from the source, its kinetic energy is approximately zero. After acceleration through the potential difference \(V\), its kinetic energy is

\[
K=\frac{1}{2}mv^2.
\]

Because the ion is positively charged, its potential energy changes by \(-qV\). Writing conservation of mechanical energy as

\[
\Delta K+\Delta U=0,
\]

gives

\[
\frac{1}{2}mv^2=qV.
\]

Thus,

\[
v=\sqrt{\frac{2qV}{m}}.
\]

The ion then moves in a semicircle in the magnetic field. From Fig. 28-12,

\[
r=\frac{x}{2}.
\]

Using the magnetic-force relation for uniform circular motion,

\[
r=\frac{mv}{Bq},
\]

we solve for \(m\) by substituting \(v\) from energy conservation:

\[
r=\frac{m}{Bq}\sqrt{\frac{2qV}{m}}
\]

\[
r=\frac{1}{B}\sqrt{\frac{2mV}{q}}.
\]

Squaring both sides,

\[
r^2B^2=\frac{2mV}{q},
\]

so

\[
m=\frac{qB^2r^2}{2V}.
\]

With \(r=x/2\),

\[
m=\frac{qB^2x^2}{8V}.
\]

Substituting the given values,

\[
m=\frac{(1.6022\times10^{-19}\ \text{C})(0.080000\ \text{T})^2(1.6254\ \text{m})^2}{8(1000.0\ \text{V})}.
\]

Converting to atomic mass units using \(1\ \text{u}=1.6605\times10^{-27}\ \text{kg}\) gives the mass in u.

## Answer
The ion mass is

\[
m \approx 3.99\times10^{-27}\ \text{kg} \approx 2.40\ \text{u}.
\]

## Key concepts used
- Magnetic force provides uniform circular motion: \(r=\dfrac{mv}{Bq}\)
- Electric potential energy becomes kinetic energy: \(qV=\dfrac{1}{2}mv^2\)
- Semicircle geometry in the spectrometer: \(r=x/2\)
- Unit conversion from kilograms to atomic mass units
