---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.1
example_number: 23.1
subtitle: Conservation of energy with electric forces
needs_review: true
---

# Example 23.1: Conservation of energy with electric forces

## Problem
A positron has mass and charge $q_0 = +e = +1.60 \times 10^{-19}\,\text{C} $. It moves in the vicinity of an alpha particle, which has charge $q = +2e = 3.20 \times 10^{-19}\,\text{C} $ and mass $6.64 \times 10^{-27}\,\text{kg} $. The alpha particle’s mass is more than 7000 times that of the positron, so it is assumed to remain at rest.

When the positron is $r_a = 1.00 \times 10^{-10}\,\text{m} $ from the alpha particle, it is moving directly away from the alpha particle at $v_a = 3.00 \times 10^6\,\text{m/s} $.

(a) What is the positron’s speed when the particles are $r_b = 2.00 \times 10^{-10}\,\text{m} $ apart?  
(b) What is the positron’s speed when it is very far from the alpha particle?  
(c) Suppose the initial conditions are the same but the moving particle is an electron (with the same mass as the positron but charge $-e $). Describe the subsequent motion.

## Setup
IDENTIFY and SET UP: The electric force between a positron (or an electron) and an alpha particle is conservative, so mechanical energy (kinetic plus potential) is conserved. Equation (23.9) gives the potential energy $U $ at any separation $r $.

The potential-energy function for parts (a) and (b) looks like that of Fig. 23.7a, and the function for part (c) looks like that of Fig. 23.7b. We are given the positron speed when the separation between the particles is $r_a = 1.00 \times 10^{-10}\,\text{m} $. In parts (a) and (b) we use Eqs. (23.3) and (23.9) to find the speed for $r = r_b $ and $r \to \infty $, respectively. In part (c) we replace the positron with an electron and reconsider the problem.

Use:
$$ 
K = \frac{1}{2}mv^2
 $$
$$ 
U = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r}
 $$

Initial data:
- $m = 9.11 \times 10^{-31}\,\text{kg} $
- $q = +2e = 3.20 \times 10^{-19}\,\text{C} $
- $q_0 = +e = +1.60 \times 10^{-19}\,\text{C} $
- $r_a = 1.00 \times 10^{-10}\,\text{m} $
- $v_a = 3.00 \times 10^6\,\text{m/s} $
- $r_b = 2.00 \times 10^{-10}\,\text{m} $

## Solution
(a) Both particles have positive charge, so the positron speeds up as it moves away from the alpha particle.

From energy conservation:
$$ 
K_b = K_a + U_a - U_b
 $$

Compute the initial kinetic energy:
$$ 
K_a = \frac{1}{2}mv_a^2
= \frac{1}{2}(9.11 \times 10^{-31}\,\text{kg})(3.00 \times 10^6\,\text{m/s})^2
= 4.10 \times 10^{-18}\,\text{J}
 $$

Compute the initial potential energy:
$$ 
U_a = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r_a}
= (9.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)
\frac{(3.20 \times 10^{-19}\,\text{C})(1.60 \times 10^{-19}\,\text{C})}{1.00 \times 10^{-10}\,\text{m}}
= 4.61 \times 10^{-18}\,\text{J}
 $$

Compute the potential energy at $r_b $:
$$ 
U_b = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r_b}
= (9.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)
\frac{(3.20 \times 10^{-19}\,\text{C})(1.60 \times 10^{-19}\,\text{C})}{2.00 \times 10^{-10}\,\text{m}}
= 2.30 \times 10^{-18}\,\text{J}
 $$

Then:
$$ 
K_b = 4.10 \times 10^{-18}\,\text{J} + 4.61 \times 10^{-18}\,\text{J} - 2.30 \times 10^{-18}\,\text{J}
= 6.41 \times 10^{-18}\,\text{J}
 $$

So:
$$ 
v_b = \sqrt{\frac{2K_b}{m}}
= \sqrt{\frac{2(6.41 \times 10^{-18}\,\text{J})}{9.11 \times 10^{-31}\,\text{kg}}}
= 3.8 \times 10^6\,\text{m/s}
 $$

(b) When the positron and alpha particle are very far apart, the final potential energy approaches zero:
$$ 
U \to 0
 $$

Again from energy conservation:
$$ 
K_b = K_a + U_a - 0
 $$
$$ 
K_b = 4.10 \times 10^{-18}\,\text{J} + 4.61 \times 10^{-18}\,\text{J}
= 8.71 \times 10^{-18}\,\text{J}
 $$

Then:
$$ 
v_b = \sqrt{\frac{2K_b}{m}}
= \sqrt{\frac{2(8.71 \times 10^{-18}\,\text{J})}{9.11 \times 10^{-31}\,\text{kg}}}
= 4.4 \times 10^6\,\text{m/s}
 $$

(c) The electron and alpha particle have opposite charges, so the force is attractive and the electron slows down as it moves away.

Changing the moving particle’s sign from $+e $ to $-e $ means that the initial potential energy is now:
$$ 
U_a = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r_a}
= (9.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)
\frac{(3.20 \times 10^{-19}\,\text{C})(-1.60 \times 10^{-19}\,\text{C})}{1.00 \times 10^{-10}\,\text{m}}
= -4.61 \times 10^{-18}\,\text{J}
 $$

Thus the total mechanical energy is negative:
$$ 
K_a + U_a = (4.10 \times 10^{-18}\,\text{J}) + (-4.61 \times 10^{-18}\,\text{J})
= -0.51 \times 10^{-18}\,\text{J}
 $$

The total mechanical energy would have to be positive for the electron to move infinitely far away from the alpha particle. Like a rock thrown upward at low speed from the earth’s surface, it reaches a maximum separation $r_d $ from the alpha particle before reversing direction. At this point its speed and kinetic energy are zero, so at separation $r_d $:
$$ 
K_d = 0
 $$
$$ 
U_d = K_a + U_a - K_d = -0.51 \times 10^{-18}\,\text{J}
 $$

For $r = r_d $:
$$ 
U_d = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r_d}
 $$
so
$$ 
r_d = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{U_d}
= \frac{(9.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)(3.20 \times 10^{-19}\,\text{C})(-1.60 \times 10^{-19}\,\text{C})}{-0.51 \times 10^{-18}\,\text{J}}
= 9.0 \times 10^{-10}\,\text{m}
 $$

## Evaluation
Both particles behave as expected as they move away from the alpha particle: the positron speeds up, and the electron slows down and eventually turns around.

How fast would an electron have to be moving at $r_a = 1.00 \times 10^{-10}\,\text{m} $ to travel infinitely far from the alpha particle? The condition would be that the total mechanical energy is zero.

## Key concepts used
- Electric forces between point charges are conservative.
- Mechanical energy $K + U $ is conserved.
- For point charges, $U = \dfrac{1}{4\pi\varepsilon_0}\dfrac{qq_0}{r} $, with $U \to 0 $ as $r \to \infty $.
- Like charges repel; opposite charges attract.
- A particle can escape to infinity only if its total mechanical energy is nonnegative.
