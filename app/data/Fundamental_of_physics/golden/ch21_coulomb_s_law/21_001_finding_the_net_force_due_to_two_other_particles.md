---
source: Fundamentals of Physics
chapter: 21
section: 21-1
sample_problem_number: 21.01
subtitle: Finding the net force due to two other particles
needs_review: true
---

# Sample Problem 21.01: Finding the net force due to two other particles

## Problem
This sample problem actually contains three examples, to build from basic stuff to harder stuff. In each we have the same charged particle 1. First there is a single force acting on it. Then there are two forces, but they are just in opposite directions. Then there are again two forces but they are in very different directions. The key to all three examples is to draw the forces correctly before you reach for a calculator, otherwise you may be calculating nonsense on the calculator.

(a) Figure 21-7a shows two positively charged particles fixed in place on an x axis. The charges are \(q_1 = 1.60 \times 10^{-19}\,\text{C}\) and \(q_2 = 3.20 \times 10^{-19}\,\text{C}\), and the particle separation is \(R = 0.0200\,\text{m}\). What are the magnitude and direction of the electrostatic force on particle 1 from particle 2?

(b) Figure 21-7c is identical to Fig. 21-7a except that particle 3 is now included. What is the net electrostatic force on particle 1 due to particles 2 and 3?

(c) Figure 21-7e is identical to Fig. 21-7a except that particle 4 is now included. It has charge \(q_4 = -3.20 \times 10^{-19}\,\text{C}\), is at a distance \(\tfrac{3}{4}R\) from particle 1, and lies on a line that makes an angle \(\theta = 60^\circ\) with the x axis. What is the net electrostatic force on particle 1 due to particles 2 and 4?

## Key ideas
- Because both particles are positively charged, particle 1 is repelled by particle 2, with a force magnitude given by Coulomb’s law.
- The direction of the force on particle 1 from particle 2 is away from particle 2, in the negative direction of the x axis.
- The presence of particle 3 does not alter the electrostatic force on particle 1 from particle 2, and vice versa: forces are found separately and then added as vectors.
- Because particles 1 and 3 have opposite signs, particle 1 is attracted to particle 3.
- When forces are not along the same axis, they must be added as vectors.
- Because particles 1 and 4 have opposite signs, particle 1 is attracted to particle 4, directed toward particle 4 at angle \(60^\circ\).

## Solution
### (a) Force on particle 1 from particle 2
Using Eq. 21-4 with separation \(R\) substituted for \(r\), the magnitude \(F_{12}\) is

\[
F_{12}=\frac{1}{4\pi\epsilon_0}\frac{|q_1q_2|}{R^2}.
\]

Substituting the given values,

\[
F_{12}
=(8.99\times10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)
\frac{(1.60\times10^{-19}\,\text{C})(3.20\times10^{-19}\,\text{C})}{(0.0200\,\text{m})^2}
=1.15\times10^{-24}\,\text{N}.
\]

Because the charges are both positive, the force on particle 1 is repulsive and points in the negative x direction.

### (b) Net force on particle 1 due to particles 2 and 3
The force \( \vec F_{12} \) is unchanged by the presence of particle 3, and the force \( \vec F_{13} \) is also unaffected by particle 2. Since particles 1 and 3 have opposite signs, particle 1 is attracted toward particle 3.

From Eq. 21-4,

\[
F_{13}=\frac{1}{4\pi\epsilon_0}\frac{|q_1q_3|}{\left(\frac{3}{4}R\right)^2}
=2.05\times10^{-24}\,\text{N}.
\]

In unit-vector notation,

\[
\vec F_{13}=(2.05\times10^{-24}\,\text{N})\hat{\mathbf{i}}.
\]

The net force on particle 1 is

\[
\vec F_{1,\text{net}}=\vec F_{12}+\vec F_{13}
=-(1.15\times10^{-24}\,\text{N})\hat{\mathbf{i}}+(2.05\times10^{-24}\,\text{N})\hat{\mathbf{i}}.
\]

Thus,

\[
\vec F_{1,\text{net}}=(9.00\times10^{-25}\,\text{N})\hat{\mathbf{i}}.
\]

So the net force is along the positive x axis.

### (c) Net force on particle 1 due to particles 2 and 4
The force \( \vec F_{12} \) is still

\[
\vec F_{12}=-(1.15\times10^{-24}\,\text{N})\hat{\mathbf{i}}.
\]

For particle 4, the magnitude is

\[
F_{14}=\frac{1}{4\pi\epsilon_0}\frac{|q_1q_4|}{\left(\frac{3}{4}R\right)^2}
=2.05\times10^{-24}\,\text{N}.
\]

Since particle 1 is attracted to particle 4, and the line to particle 4 makes angle \(\theta=60^\circ\) with the x axis, we write

\[
\vec F_{14}=(F_{14}\cos\theta)\hat{\mathbf{i}}+(F_{14}\sin\theta)\hat{\mathbf{j}}.
\]

Substituting \(F_{14}=2.05\times10^{-24}\,\text{N}\) and \(\theta=60^\circ\),

\[
\vec F_{14}=(1.025\times10^{-24}\,\text{N})\hat{\mathbf{i}}+(1.775\times10^{-24}\,\text{N})\hat{\mathbf{j}}.
\]

Then

\[
\vec F_{1,\text{net}}=\vec F_{12}+\vec F_{14}
\]

\[
\vec F_{1,\text{net}}
=-(1.15\times10^{-24}\,\text{N})\hat{\mathbf{i}}
+(1.025\times10^{-24}\,\text{N})\hat{\mathbf{i}}
+(1.775\times10^{-24}\,\text{N})\hat{\mathbf{j}}
\]

\[
\vec F_{1,\text{net}}
=-(1.25\times10^{-25}\,\text{N})\hat{\mathbf{i}}
+(1.775\times10^{-24}\,\text{N})\hat{\mathbf{j}}.
\]

Using components, the x and y sums are

\[
F_{1,\text{net},x}=F_{12,x}+F_{14,x}=F_{12}+F_{14}\cos60^\circ
=-1.25\times10^{-25}\,\text{N},
\]

\[
F_{1,\text{net},y}=F_{12,y}+F_{14,y}=0+F_{14}\sin60^\circ
=1.78\times10^{-24}\,\text{N}.
\]

The magnitude is

\[
F_{1,\text{net}}=\sqrt{F_{1,\text{net},x}^2+F_{1,\text{net},y}^2}
=1.78\times10^{-24}\,\text{N}.
\]

For the direction,

\[
\theta=\tan^{-1}\!\left(\frac{F_{1,\text{net},y}}{F_{1,\text{net},x}}\right)=-86.0^\circ.
\]

This is not reasonable as stated because \(\vec F_{1,\text{net}}\) must have a direction between the directions of \(\vec F_{12}\) and \(\vec F_{14}\). Adding \(180^\circ\) gives the correct angle:

\[
-86.0^\circ+180^\circ=94.0^\circ.
\]

## Answer
(a) \(F_{12}=1.15\times10^{-24}\,\text{N}\), in the negative x direction.

(b) \(\vec F_{1,\text{net}}=(9.00\times10^{-25}\,\text{N})\hat{\mathbf{i}}\).

(c) \(\vec F_{1,\text{net}}=-(1.25\times10^{-25}\,\text{N})\hat{\mathbf{i}}+(1.78\times10^{-24}\,\text{N})\hat{\mathbf{j}}\),

with magnitude \(1.78\times10^{-24}\,\text{N}\) and direction \(94.0^\circ\) from the positive x axis.

## Key concepts used
- Coulomb’s law
- Superposition of forces
- Vector addition of forces
- Unit-vector notation
- Resolving vectors into x and y components
