---
source: Fundamentals of Physics
chapter: 31
section: 31-5
sample_problem_number: 31.07
subtitle: Driven RLC circuit: power factor and average power
needs_review: true
---

# Sample Problem 31.07: Driven RLC circuit: power factor and average power

## Problem
A series RLC circuit, driven with frequency $f_d = 60.0\ \text{Hz} $, contains a resistance $R = 200\ \Omega $, an rms driving emf $\varepsilon_{\text{rms}} = 120\ \text{V} $, an inductance with inductive reactance $X_L = 80.0\ \Omega $, and a capacitance with capacitive reactance $X_C = 150\ \Omega $.

(a) What are the power factor $\cos \phi $ and phase constant $\phi $ of the circuit?

(b) What is the average rate $P_{\text{avg}} $ at which energy is dissipated in the resistance?

## Key ideas
The power factor $\cos \phi $ can be found from the resistance $R $ and impedance $Z $ via Eq. 31-75:
$$ 
\cos \phi = \frac{R}{Z}.
 $$

There are two ways and two ideas to use for part (b):
1. Because the circuit is assumed to be in steady-state operation, the rate at which energy is dissipated in the resistance is equal to the rate at which energy is supplied to the circuit:
$$ 
P_{\text{avg}} = \varepsilon_{\text{rms}} I_{\text{rms}} \cos \phi.
 $$
2. The rate at which energy is dissipated in a resistance $R $ depends on the square of the rms current through it:
$$ 
P_{\text{avg}} = I_{\text{rms}}^{2} R.
 $$

## Solution
### (a) Power factor and phase constant

To calculate $Z $, we use Eq. 31-61:
$$ 
Z = \sqrt{R^{2} + (X_L - X_C)^{2}}.
 $$
Thus,
$$ 
Z = \sqrt{(200\ \Omega)^{2} + (80.0\ \Omega - 150\ \Omega)^{2}}
= 211.90\ \Omega.
 $$

Equation 31-75 then gives
$$ 
\cos \phi = \frac{R}{Z} = \frac{200\ \Omega}{211.90\ \Omega} = 0.9438 \approx 0.944.
 $$

Taking the inverse cosine then yields
$$ 
\phi = \cos^{-1}(0.944) = 19.3^\circ.
 $$

The inverse cosine on a calculator gives only the positive answer here, but both $19.3^\circ $ and $-19.3^\circ $ have a cosine of $0.944 $. To determine which sign is correct, we must consider whether the current leads or lags the driving emf. Because $X_C > X_L $, this circuit is mainly capacitive, with the current leading the emf. Thus, $\phi $ must be negative:
$$ 
\phi = -19.3^\circ.
 $$

We could, instead, have found $\phi $ with Eq. 31-65. A calculator would then have given us the answer with the minus sign.

### (b) Average rate of energy dissipation

First way: We are given the rms driving emf $\varepsilon_{\text{rms}} $ and we already know $\cos \phi $ from part (a). The rms current is
$$ 
I_{\text{rms}} = \frac{\varepsilon_{\text{rms}}}{Z}
= \frac{120\ \text{V}}{211.90\ \Omega}
= 0.566\ \text{A}.
 $$

Then
$$ 
P_{\text{avg}} = \varepsilon_{\text{rms}} I_{\text{rms}} \cos \phi
= (120\ \text{V})(0.566\ \text{A})(0.944)
\approx 64.1\ \text{W}.
 $$

Second way:
$$ 
P_{\text{avg}} = I_{\text{rms}}^{2} R
= (0.566\ \text{A})^{2}(200\ \Omega)
\approx 64.1\ \text{W}.
 $$

## Answer
(a)
$$ 
\cos \phi = 0.944, \qquad \phi = -19.3^\circ.
 $$

(b)
$$ 
P_{\text{avg}} \approx 64.1\ \text{W}.
 $$

## Key concepts used
- Impedance of a series RLC circuit:
  $$ 
  Z = \sqrt{R^{2} + (X_L - X_C)^{2}}.
   $$
- Power factor:
  $$ 
  \cos \phi = \frac{R}{Z}.
   $$
- Average power in a driven AC circuit:
  $$ 
  P_{\text{avg}} = \varepsilon_{\text{rms}} I_{\text{rms}} \cos \phi = I_{\text{rms}}^{2} R.
   $$
