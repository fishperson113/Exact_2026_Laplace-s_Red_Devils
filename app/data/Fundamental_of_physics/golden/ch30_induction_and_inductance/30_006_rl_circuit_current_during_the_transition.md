---
source: Fundamentals of Physics
chapter: 30
section: 30-6
sample_problem_number: 30.06
subtitle: RL circuit, current during the transition
needs_review: true
---

# Sample Problem 30.06: RL circuit, current during the transition

## Problem
A coil has an inductance of 53 mH and a resistance of 0.35 1.

(a) If a 12 V emf is applied across the coil, how much energy is stored in the magnetic field after the current has built up to its equilibrium value?

(b) After how many time constants will half this equilibrium energy be stored in the magnetic field?

## Key ideas
If an inductor \(L\) carries a current \(i\), the energy stored in its magnetic field is

\[
U_B=\frac{1}{2}Li^2.
\]

For an RL circuit at equilibrium, the current is

\[
i_\infty=\frac{\mathcal{E}}{R}.
\]

## Solution
### (a)
To find the equilibrium magnetic energy, first determine the equilibrium current:

\[
i_\infty=\frac{\mathcal{E}}{R}=\frac{12\ \text{V}}{0.35\ 1}=34.3\ \text{A}.
\]

Then use

\[
U_B=\frac{1}{2}Li^2
\]

with \(L=53\ \text{mH}=53\times10^{-3}\ \text{H}\):

\[
U_B=\frac{1}{2}(53\times10^{-3}\ \text{H})(34.3\ \text{A})^2.
\]

This gives

\[
U_B \approx 31\ \text{J}.
\]

### (b)
We want the time \(t\) when half the equilibrium energy is stored:

\[
U_B=\frac{1}{2}U_{B,\infty}.
\]

Using \(U_B=\frac{1}{2}Li^2\), this means

\[
\frac{1}{2}Li^2=\frac{1}{2}\left(\frac{1}{2}Li_\infty^2\right),
\]

so

\[
i=\frac{1}{\sqrt{2}}\,i_\infty.
\]

For an RL circuit during current growth,

\[
i=i_\infty\left(1-e^{-t/\tau}\right),
\]

where \(\tau=L/R\) is the time constant. Thus,

\[
1-e^{-t/\tau}=\frac{1}{\sqrt{2}}.
\]

So

\[
e^{-t/\tau}=1-\frac{1}{\sqrt{2}}\approx 0.293,
\]

and therefore

\[
-\frac{t}{\tau}=\ln(0.293),
\]

\[
\frac{t}{\tau}=1.23.
\]

Thus,

\[
t\approx 1.2\,\tau.
\]

## Answer
(a) \(31\ \text{J}\)

(b) \(1.2\) time constants

## Key concepts used
- Magnetic energy stored in an inductor: \(U_B=\frac{1}{2}Li^2\)
- Equilibrium current in an RL circuit: \(i_\infty=\mathcal{E}/R\)
- RL current growth: \(i=i_\infty\left(1-e^{-t/\tau}\right)\)
- Time constant: \(\tau=L/R\)
