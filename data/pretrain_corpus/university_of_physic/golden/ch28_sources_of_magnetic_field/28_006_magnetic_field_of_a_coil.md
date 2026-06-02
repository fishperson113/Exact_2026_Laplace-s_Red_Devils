---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.5
example_number: 28.6
subtitle: Magnetic field of a coil
needs_review: true
---

# Example 28.6: Magnetic field of a coil

## Problem
A coil consisting of 100 circular loops with radius 0.60 m carries a 5.0-A current.

(a) Find the magnetic field at a point along the axis of the coil, 0.80 m from the center.  
(b) Along the axis, at what distance from the center of the coil is the field magnitude as great as it is at the center?

## Setup
IDENTIFY and SET UP: This problem concerns the magnetic field magnitude $B $ along the axis of a current-carrying coil, so we can use the ideas of this section, and in particular Eq. (28.16).

We are given
- $N = 100 $
- $a = 0.60\ \text{m} $
- $I = 5.0\ \text{A} $

In part (a) our target variable is $B $ at a given value of $x $. In part (b) the target variable is the value of $x $ at which the field has the same magnitude that it has at the origin.

## Solution
EXECUTE:  

(a) Using Eq. (28.16) we have
$$ 
B_x = \frac{(4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})(100)(5.0\ \text{A})(0.60\ \text{m})^2}{2\left[(0.80\ \text{m})^2 + (0.60\ \text{m})^2\right]^{3/2}}
= 1.1 \times 10^{-4}\ \text{T}.
 $$

(b) Considering Eq. (28.16), we want to find a value of $x $ such that
$$ 
\frac{1}{\left(x^2 + a^2\right)^{3/2}} = \frac{1}{8a^3}.
 $$
To solve this for $x $, we take the reciprocal of the whole thing and then take the $2/3 $ power of both sides; the result is
$$ 
x = \pm \sqrt{3}\,a.
 $$

With $a = 0.60\ \text{m} $,
$$ 
x = \pm 1.04\ \text{m}.
 $$

## Evaluation
We check our answer in part (a) by finding the coil’s magnetic moment and substituting the result into Eq. (28.18):
$$ 
m = NI\pi a^2 = (100)(5.0\ \text{A})\pi(0.60\ \text{m})^2 = 5.7 \times 10^2\ \text{A}\cdot\text{m}^2.
 $$
Then
$$ 
B_x = \frac{(4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})(5.7 \times 10^2\ \text{A}\cdot\text{m}^2)}{2\pi\left[(0.80\ \text{m})^2 + (0.60\ \text{m})^2\right]^{3/2}}
= 1.1 \times 10^{-4}\ \text{T}.
 $$

The magnetic moment $m $ is relatively large, yet it produces a rather small field, comparable to that of the earth. This illustrates how difficult it is to produce strong fields of 1 T or more.

## Key concepts used
- Magnetic field on the axis of a current-carrying circular coil
- Superposition for $N $ identical turns
- Field magnitude from Eq. (28.16)
- Magnetic dipole moment $m = NI\pi a^2 $
- Solving for positions where the axial field equals its value at the center
