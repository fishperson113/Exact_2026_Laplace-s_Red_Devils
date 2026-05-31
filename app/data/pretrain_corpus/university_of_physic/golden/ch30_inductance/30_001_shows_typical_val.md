---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.1
example_number: 30.1
subtitle: shows, typical val-
needs_review: true
---

# Example 30.1: shows, typical val-

## Problem
In one form of Tesla coil (a high-voltage generator popular in science museums), a long solenoid with length $l $ and cross-sectional area $A $ is closely wound with $N_1 $ turns of wire. A coil with $N_2 $ turns surrounds it at its center (Fig. 30.3). Find the mutual inductance $M $.

## Setup
Mutual inductance occurs here because a current in either coil sets up a magnetic field that causes a flux through the other coil. From Example 28.9 (Section 28.7) we have an expression [Eq. (28.23)] for the field magnitude $B_1 $ at the center of the solenoid (coil 1) in terms of the solenoid current $i_1 $.

This allows us to determine the flux through a cross section of the solenoid. Since there is no magnetic field outside a very long solenoid, this is also equal to the flux $\Phi_{B2} $ through each turn of the outer coil (2). We then use Eq. (30.5), in the form

$$ 
M = \frac{N_2 \Phi_{B2}}{i_1},
 $$

to determine $M $.

Equation (28.23) is expressed in terms of the number of turns per unit length, which for solenoid (1) is

$$ 
n_1 = \frac{N_1}{l}.
 $$

The flux through a cross section of the solenoid equals

$$ 
\Phi_{B2} = B_1 A.
 $$

As mentioned above, this also equals the flux through each turn of the outer coil, independent of its cross-sectional area.

## Solution
From Eq. (28.23),

$$ 
B_1 = \mu_0 n_1 i_1 = \mu_0 \frac{N_1 i_1}{l}.
 $$

Then

$$ 
\Phi_{B2} = B_1 A = \mu_0 \frac{N_1 i_1}{l} A.
 $$

Using Eq. (30.5),

$$ 
M = \frac{N_2 \Phi_{B2}}{i_1}
  = \frac{N_2}{i_1}\left(\mu_0 \frac{N_1 i_1}{l} A\right)
  = \mu_0 \frac{A N_1 N_2}{l}.
 $$

## Evaluation
The mutual inductance $M $ of any two coils is proportional to the product $N_1N_2 $ of their numbers of turns. Notice that $M $ depends only on the geometry of the two coils, not on the current.

Here’s a numerical example to give you an idea of magnitudes. Suppose

$$ 
l = 0.50\ \text{m}, \quad A = 10\ \text{cm}^2 = 1.0 \times 10^{-3}\ \text{m}^2, \quad N_1 = 1000, \quad N_2 = 10.
 $$

Then

$$ 
M = \mu_0 \frac{A N_1 N_2}{l}
  = (4\pi \times 10^{-7}\ \text{Wb/(A}\cdot\text{m)})\frac{(1.0\times10^{-3}\ \text{m}^2)(1000)(10)}{0.50\ \text{m}}
 $$

$$ 
= 25 \times 10^{-6}\ \text{Wb/A}
= 25 \times 10^{-6}\ \text{H}
= 25\ \text{mH}.
 $$

## Key concepts used
- Mutual inductance between two coils
- Magnetic field inside a long solenoid
- Magnetic flux through a coil
- Definition $M = N_2\Phi_{B2}/i_1 $
- $\Phi_B = BA $ for uniform field over area $A $
- $B = \mu_0 n i $ for a long solenoid
