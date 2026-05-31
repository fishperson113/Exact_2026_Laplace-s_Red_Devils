---
source: Fundamentals of Physics
chapter: 31
section: 31-3
sample_problem_number: 31.02
subtitle: Damped RLC circuit: charge amplitude
needs_review: true
---

# Sample Problem 31.02: Damped RLC circuit: charge amplitude

## Problem
A series RLC circuit has inductance $L = 12\ \text{mH} $, capacitance $C = 1.6\ \text{mF} $, and resistance $R = 1.5\ \Omega $ and begins to oscillate at time $t = 0 $.

(a) At what time $t $ will the amplitude of the charge oscillations in the circuit be 50% of its initial value?  
(Note that we do not know that initial value.)

## Key ideas
The amplitude of the charge oscillations decreases exponentially with time $t $. According to Eq. 31-25, the charge amplitude at any time $t $ is
$$ 
Qe^{-Rt/2L},
 $$
in which $Q $ is the amplitude at time $t = 0 $.

## Solution
We want the time when the charge amplitude has decreased to $0.50Q $, that is, when
$$ 
Qe^{-Rt/2L} = 0.50Q.
 $$
We can cancel $Q $, which also means that we can answer the question without knowing the initial charge.

Taking the natural logarithms of both sides to eliminate the exponential function, we have
$$ 
-\frac{Rt}{2L} = \ln 0.50.
 $$

## Answer
$$ 
t = -\frac{2L}{R}\ln 0.50.
 $$

## Key concepts used
- Exponential decay of charge amplitude in a damped RLC circuit
- Charge amplitude $Qe^{-Rt/2L} $
- Natural logarithms to solve for time
- Cancellation of the unknown initial amplitude $Q $
