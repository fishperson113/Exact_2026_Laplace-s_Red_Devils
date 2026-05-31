---
source: Fundamentals of Physics
chapter: 30
section: 30-1
sample_problem_number: 30.01
subtitle: Induced emf in coil due to a solenoid
needs_review: false
---

# Sample Problem 30.01: Induced emf in coil due to a solenoid

## Problem
The long solenoid S shown in cross section in Fig. 30-3 has 220 turns/cm and carries a current $i = 1.5\ \text{A} $; its diameter $D $ is 3.2 cm. At its center we place a 130-turn closely packed coil C of diameter $d = 2.1\ \text{cm} $. The current in the solenoid is reduced to zero at a steady rate in 25 ms. What is the magnitude of the emf that is induced in coil C while the current in the solenoid is changing?

## Key ideas
For coil C, which has more than one turn, Faraday’s law is used in the form

$$ 
\mathcal{E} = -N \frac{d\Phi_B}{dt},
 $$

where $N $ is the number of turns and $\frac{d\Phi_B}{dt} $ is the rate of change of magnetic flux through each turn. Because the current in the solenoid decreases steadily, the flux also decreases steadily. The magnetic flux is

$$ 
\Phi_B = BA,
 $$

with

$$ 
B = \mu_0 n i.
 $$

We are interested only in the magnitude.

## Solution
Because coil C consists of more than one turn, we apply Faraday’s law in the form

$$ 
\mathcal{E} = -N \frac{d\Phi_B}{dt},
 $$

where $N = 130 $ and $\frac{d\Phi_B}{dt} $ is the rate at which the flux changes.

Because the current in the solenoid decreases at a steady rate, the flux $\Phi_B $ also decreases at a steady rate, so we write

$$ 
\frac{d\Phi_B}{dt} = \frac{\Delta \Phi_B}{\Delta t}.
 $$

To find $\Delta \Phi_B $, we need the initial and final flux values.

The final flux is zero because the final current in the solenoid is zero. To find the initial flux, we use

$$ 
\Phi_{B,i} = BA = (\mu_0 n i)A.
 $$

Here the area is

$$ 
A = \pi d^2/4 = 3.464 \times 10^{-4}\ \text{m}^2,
 $$

and the turn density is

$$ 
n = 220\ \text{turns/cm} = 22\,000\ \text{turns/m}.
 $$

Thus

$$ 
\Phi_{B,i} = (4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})(1.5\ \text{A})(22\,000\ \text{turns/m})(3.464 \times 10^{-4}\ \text{m}^2)
 $$

which gives

$$ 
\Phi_{B,i} = 1.44 \times 10^{-5}\ \text{Wb}.
 $$

So

$$ 
\Delta \Phi_B = \Phi_{B,f} - \Phi_{B,i} = 0 - 1.44 \times 10^{-5}\ \text{Wb}
= -1.44 \times 10^{-5}\ \text{Wb}.
 $$

Over the time interval

$$ 
\Delta t = 25 \times 10^{-3}\ \text{s},
 $$

we have

$$ 
\frac{\Delta \Phi_B}{\Delta t}
= \frac{-1.44 \times 10^{-5}\ \text{Wb}}{25 \times 10^{-3}\ \text{s}}
= -5.76 \times 10^{-4}\ \text{Wb/s}.
 $$

Then

$$ 
\mathcal{E} = -N \frac{d\Phi_B}{dt}
 $$

so, in magnitude,

$$ 
|\mathcal{E}| = (130)(5.76 \times 10^{-4}\ \text{V})
= 7.5 \times 10^{-2}\ \text{V}.
 $$

We are interested only in magnitudes, so we ignore the minus signs.

## Answer
$$ 
\boxed{7.5 \times 10^{-2}\ \text{V} = 75\ \text{mV}}
 $$

## Key concepts used
- Faraday’s law of induction: $\mathcal{E} = -N\, d\Phi_B/dt $
- Magnetic flux through a loop: $\Phi_B = BA $
- Solenoid field: $B = \mu_0 n i $
- Flux change from a steadily decreasing current
- Unit conversion: turns/cm to turns/m
