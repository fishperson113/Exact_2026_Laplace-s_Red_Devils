---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.4
example_number: 21.7
subtitle: Electron in a uniform field
needs_review: true
---

# Example 21.7: Electron in a uniform field

## Problem
When the terminals of a battery are connected to two parallel conducting plates with a small gap between them, the resulting charges on the plates produce a nearly uniform electric field between the plates. If the plates are 1.0 cm apart and are connected to a 100-volt battery, the field is vertically upward and has magnitude \(E = 1.00 \times 10^4\ \text{N/C}\).

(a) If an electron is released from rest at the upper plate, what is its acceleration?  
(b) What speed and kinetic energy does it acquire while traveling 1.0 cm to the lower plate?  
(c) How long does it take to travel this distance?

## Setup
**IDENTIFY and SET UP:** This example involves the relationship between electric field and electric force. It also involves the relationship between force and acceleration, the definition of kinetic energy, and the kinematic relationships among acceleration, distance, velocity, and time.

The electric field is upward, but the electron has negative charge, so the electric force on it is downward. Because the field is uniform, the force is constant. We use
\[
\vec F = q \vec E
\]
and Newton’s second law to find the acceleration. Then we use the constant-acceleration formulas from Chapter 2 to find the electron’s velocity and travel time. The kinetic energy is found from
\[
K = \frac12 mv^2.
\]

Given:
- Electron charge: \(e = -1.60 \times 10^{-19}\ \text{C}\)
- Electron mass: \(m = 9.11 \times 10^{-31}\ \text{kg}\)
- Electric field: \(E = 1.00 \times 10^4\ \text{N/C}\)

## Solution
**EXECUTE:**

### (a) Acceleration
Although \(\vec E\) is upward in the \(+y\)-direction, \(\vec F\) is downward because the electron’s charge is negative, so \(F_y\) is negative. Since the field is constant, the electron’s acceleration is constant:
\[
a_y = \frac{F_y}{m} = \frac{-eE}{m}
\]
\[
a_y = \frac{(-1.60 \times 10^{-19}\ \text{C})(1.00 \times 10^4\ \text{N/C})}{9.11 \times 10^{-31}\ \text{kg}}
= -1.76 \times 10^{15}\ \text{m/s}^2
\]

### (b) Speed and kinetic energy
The electron starts from rest, so its motion is in the \(y\)-direction only, in the direction of the acceleration. Use the constant-acceleration relation
\[
v_y^2 = v_{0y}^2 + 2a_y(y-y_0).
\]
With
\[
v_{0y}=0,\qquad y_0=0,\qquad y=-1.0\ \text{cm}=-1.0\times10^{-2}\ \text{m},
\]
we get
\[
|v_y| = \sqrt{2a_y y}
= \sqrt{2(-1.76\times10^{15}\ \text{m/s}^2)(-1.0\times10^{-2}\ \text{m})}
= 5.9\times10^6\ \text{m/s}.
\]
The velocity is downward, so
\[
v_y = -5.9 \times 10^6\ \text{m/s}.
\]

The kinetic energy is
\[
K = \frac12 mv^2
= \frac12 (9.11\times10^{-31}\ \text{kg})(5.9\times10^6\ \text{m/s})^2
= 1.6\times10^{-17}\ \text{J}.
\]

### (c) Travel time
From the constant-acceleration equation
\[
v_y = v_{0y} + a_y t,
\]
\[
t = \frac{v_y - v_{0y}}{a_y}
= \frac{-5.9\times10^6\ \text{m/s} - 0}{-1.76\times10^{15}\ \text{m/s}^2}
= 3.4\times10^{-9}\ \text{s}.
\]

## Evaluation
Our results show that in problems involving subatomic particles such as electrons, many quantities—including acceleration, speed, kinetic energy, and time—can have values very different from those typical of everyday objects.

## Key concepts used
- Electric force in a uniform field: \(\vec F = q\vec E\)
- Newton’s second law: \(\vec a = \vec F/m\)
- Constant-acceleration kinematics
- Kinetic energy: \(K = \frac12 mv^2\)
- Direction of force on a negative charge is opposite the electric field
