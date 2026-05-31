---
source: Fundamentals of Physics
chapter: 31
section: 31-1
sample_problem_number: 31.01
subtitle: LC oscillator: potential change, rate of current change
needs_review: true
---

# Sample Problem 31.01: LC oscillator: potential change, rate of current change

## Problem
A 1.5 mF capacitor is charged to 57 V by a battery, which is then removed. At time $t = 0 $, a 12 mH coil is connected in series with the capacitor to form an LC oscillator (Fig. 31-1).

(a) What is the potential difference $v_L(t) $ across the inductor as a function of time?

(b) What is the maximum rate $(di/dt)_{\max} $ at which the current $i $ changes in the circuit?

## Key ideas
1. The current and potential differences of the circuit (both the potential difference of the capacitor and the potential difference of the coil) undergo sinusoidal oscillations.
2. We can still apply the loop rule to these oscillating potential differences, just as we did for the nonoscillating circuits of Chapter 27.

## Solution
### (a) Potential difference across the inductor

For the capacitor in the LC oscillator, the charge oscillates sinusoidally, so the potential difference across the capacitor is

$$ 
v_C = V_C \cos \omega t,
 $$

where $V_C $ is the amplitude of the oscillating potential difference.

From the loop rule for the LC circuit, the inductor potential difference is

$$ 
v_L = V_C \cos \omega t.
 $$

The amplitude $V_C $ equals the initial potential difference of the charged capacitor:

$$ 
V_C = 57\ \text{V}.
 $$

The angular frequency is

$$ 
\omega = \frac{1}{\sqrt{LC}}
= \frac{1}{\sqrt{(0.012\ \text{H})(1.5 \times 10^{-6}\ \text{F})}}
= 7454\ \text{rad/s} \approx 7500\ \text{rad/s}.
 $$

Thus,

$$ 
v_L(t) = (57\ \text{V}) \cos\!\big[(7500\ \text{rad/s})t\big].
 $$

### (b) Maximum rate of change of current

With the charge oscillating as in Eq. 31-12, the current has the form

$$ 
i = -\omega Q \sin \omega t.
 $$

Taking the derivative,

$$ 
\frac{di}{dt} = -\omega^2 Q \cos \omega t.
 $$

We simplify by substituting $Q = C V_C $ and $\omega^2 = 1/LC $:

$$ 
\frac{di}{dt}
= -\frac{1}{LC} (C V_C)\cos \omega t
= -\frac{V_C}{L}\cos \omega t.
 $$

Thus the current changes at a sinusoidal rate, with maximum magnitude

$$ 
\left(\frac{di}{dt}\right)_{\max} = \frac{V_C}{L}
= \frac{57\ \text{V}}{0.012\ \text{H}}
= 4750\ \text{A/s}
\approx 4800\ \text{A/s}.
 $$

## Answer
$$ 
\boxed{v_L(t) = (57\ \text{V})\cos\!\big[(7500\ \text{rad/s})t\big]}
 $$

$$ 
\boxed{\left(\frac{di}{dt}\right)_{\max} = 4.8 \times 10^3\ \text{A/s}}
 $$

## Key concepts used
- LC oscillations are sinusoidal.
- The loop rule applies to the oscillating voltages in an LC circuit.
- The angular frequency of an LC oscillator is $\omega = 1/\sqrt{LC} $.
- The current is the time derivative of charge.
- The maximum rate of current change is $(di/dt)_{\max} = V_C/L $.
