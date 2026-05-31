---
source: Fundamentals of Physics
chapter: 30
section: 30-6
sample_problem_number: 30.05
subtitle: RL circuit, immediately after switching and after a long time
needs_review: true
---

# Sample Problem 30.05: RL circuit, immediately after switching and after a long time

## Problem
A solenoid has an inductance of 53 mH and a resistance of 0.37 Ω. If the solenoid is connected to a battery, how long will the current take to reach half its final equilibrium value? (This is a real solenoid because we are considering its small, but nonzero, internal resistance.)

## Key ideas
We can mentally separate the solenoid into a resistance and an inductance that are wired in series with a battery, as in Fig. 30-16. Then application of the loop rule leads to Eq. 30-39, which has the solution of Eq. 30-41 for the current i in the circuit.

## Solution
According to that solution, current i increases exponentially from zero to its final equilibrium value of ε/R. Let t₀ be the time that current i takes to reach half its equilibrium value. Then Eq. 30-41 gives us

\[
\frac{1}{2}\frac{\varepsilon}{R}=\frac{\varepsilon}{R}\left(1-e^{-t_0/t_L}\right).
\]

We solve for t₀ by canceling ε/R, isolating the exponential, and taking the natural logarithm of each side. We find

\[
t_0=t_L\ln 2=\frac{L}{R}\ln 2
= \frac{53\times 10^{-3}\ \text{H}}{0.37\ \Omega}\ln 2.
\]

## Answer
\[
t_0 \approx 0.10\ \text{s}.
\]

## Key concepts used
- RL circuit
- Inductance in series with resistance
- Exponential current growth
- Time constant \(t_L = L/R\)
- Half-value condition and logarithms
