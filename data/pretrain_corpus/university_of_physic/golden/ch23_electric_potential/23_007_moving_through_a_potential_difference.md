---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.2
example_number: 23.7
subtitle: Moving through a potential difference
needs_review: true
---

# Example 23.7: Moving through a potential difference

## Problem
In Fig. 23.15 a dust particle with mass $m = 5.0 \times 10^{-9}\,\text{kg} $ and charge $q_0 = 2.0\,\text{nC} $ starts from rest and moves in a straight line from point $a $ to point $b $. What is its speed at point $b $?

## Setup
**IDENTIFY and SET UP:** Only the conservative electric force acts on the particle, so mechanical energy is conserved:

$$ 
K_a + U_a = K_b + U_b.
 $$

We get the potential energies from the corresponding potentials using Eq. (23.12):

$$ 
U_a = q_0 V_a, \qquad U_b = q_0 V_b.
 $$

The figure gives the distances and charges needed to calculate the potentials at $a $ and $b $ using Eq. (23.15).

## Solution
**EXECUTE:** We have

$$ 
K_a = 0, \qquad K_b = \frac{1}{2}mv^2.
 $$

Substitute these and the expressions for $U_a $ and $U_b $ into the energy-conservation equation, then solve for $v $:

$$ 
0 + q_0 V_a = \frac{1}{2}mv^2 + q_0 V_b
 $$

$$ 
v = \sqrt{\frac{2q_0 (V_a - V_b)}{m}}.
 $$

Calculate the potentials using Eq. (23.15):

$$ 
V_a = (19.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)\left(\frac{3.0 \times 10^{-9}\,\text{C}}{0.010\,\text{m}}\right) + \left(\frac{-3.0 \times 10^{-9}\,\text{C}}{0.020\,\text{m}}\right)
= 1350\,\text{V}
 $$

$$ 
V_b = (19.0 \times 10^9\,\text{N}\cdot\text{m}^2/\text{C}^2)\left(\frac{3.0 \times 10^{-9}\,\text{C}}{0.020\,\text{m}}\right) + \left(\frac{-3.0 \times 10^{-9}\,\text{C}}{0.010\,\text{m}}\right)
= -1350\,\text{V}
 $$

Thus,

$$ 
V_a - V_b = 1350\,\text{V} - (-1350\,\text{V}) = 2700\,\text{V}.
 $$

So

$$ 
v = \sqrt{\frac{2(2.0 \times 10^{-9}\,\text{C})(2700\,\text{V})}{5.0 \times 10^{-9}\,\text{kg}}}
= 46\,\text{m/s}.
 $$

## Evaluation
Our result makes sense: the positive test charge speeds up as it moves away from the positive charge and toward the negative charge.

To check unit consistency in the final line of the calculation, note that

$$ 
1\,\text{V} = 1\,\text{J/C},
 $$

so the numerator under the radical has units of joules, or $ \text{kg}\cdot\text{m}^2/\text{s}^2  $.

## Key concepts used
- Conservation of mechanical energy for a particle acted on only by the electric force
- Electric potential energy: $U = qV $
- Electric potential of point charges: $V = \dfrac{q}{4\pi\epsilon_0 r} $
- Solving for speed from energy conservation
- Unit check using $1\,\text{V} = 1\,\text{J/C} $
