---
source: Fundamentals of Physics
chapter: 31
section: 31-4
sample_problem_number: 31.06
subtitle: Current amplitude, impedance, and phase constant
needs_review: true
---

# Sample Problem 31.06: Current amplitude, impedance, and phase constant

## Problem
In Fig. 31-7, let \(R = 200 \ \Omega\), \(C = 15.0 \ \text{mF}\), \(L = 230 \ \text{mH}\), \(f_d = 60.0 \ \text{Hz}\), and \(\varepsilon_m = 36.0 \ \text{V}\). (These parameters are those used in the earlier sample problems.)

(a) What is the current amplitude \(I\)?

## Key ideas
The current amplitude \(I\) depends on the amplitude \(\varepsilon_m\) of the driving emf and on the impedance \(Z\) of the circuit, according to Eq. 31-62:

\[
I = \frac{\varepsilon_m}{Z}.
\]

## Solution
To find \(I\), we first need \(Z\), which depends on the resistance \(R\), the capacitive reactance \(X_C\), and the inductive reactance \(X_L\).

The resistance is the given resistance \(R\). From an earlier sample problem, the capacitive reactance is

\[
X_C = 177 \ \Omega,
\]

and from another sample problem, the inductive reactance is

\[
X_L = 86.7 \ \Omega.
\]

Thus, the impedance is

\[
Z = \sqrt{R^2 + (X_L - X_C)^2}
\]

\[
Z = \sqrt{(200 \ \Omega)^2 + (86.7 \ \Omega - 177 \ \Omega)^2}
\]

\[
Z \approx 219 \ \Omega.
\]

Then

\[
I = \frac{\varepsilon_m}{Z} = \frac{36.0 \ \text{V}}{219 \ \Omega}.
\]

This gives

\[
I = 0.164 \ \text{A}.
\]

## Answer
\[
\boxed{I = 0.164 \ \text{A}}
\]

## Key concepts used
- Impedance of a series RLC circuit:
  \[
  Z = \sqrt{R^2 + (X_L - X_C)^2}
  \]
- Current amplitude:
  \[
  I = \frac{\varepsilon_m}{Z}
  \]
