---
source: Young and Freedman University Physics, 13th ed.
chapter: 23
section: 23.2
example_number: 23.6
subtitle: Finding potential by integration
needs_review: true
---

# Example 23.6: Finding potential by integration

## Problem
By integrating the electric field as in Eq. (23.17), find the potential at a distance from a point charge $q $.

## Setup
**IDENTIFY and SET UP:** We let point $a $ in Eq. (23.17) be at distance $r $, and let point $b $ be at infinity (Fig. 23.14). As usual, we choose the potential to be zero at an infinite distance from the charge $q $.

## Solution
**EXECUTE:** To carry out the integral, we can choose any path we like between points $a $ and $b $. The most convenient path is a radial line as shown in Fig. 23.14, so that $\vec{E} $ is in the radial direction and $d\vec{\ell} $ has magnitude $dr $.

Writing $\vec{d\ell} = \hat{r}\,dr $, we have from Eq. (23.17):
$$ 
V - 0 = V = -\int_{r}^{\infty} \vec{E}\cdot d\vec{\ell}
= -\int_{r}^{\infty} \frac{q}{4\pi\varepsilon_0 r^2}\,\hat{r}\cdot \hat{r}\,dr
= -\int_{r}^{\infty} \frac{q}{4\pi\varepsilon_0 r^2}\,dr
 $$
$$ 
V = -\left[-\frac{q}{4\pi\varepsilon_0 r}\right]_{r}^{\infty}
= \frac{q}{4\pi\varepsilon_0 r}
 $$

## Evaluation
**EVALUATE:** Our result agrees with Eq. (23.14) and is correct for positive or negative $q $.

## Key concepts used
- Electric potential difference is found from the line integral of the electric field.
- The electric field of a point charge is radial, so a radial path is the simplest choice.
- Choosing $V(\infty)=0 $ gives the standard potential of a point charge:
  $$ 
  V(r)=\frac{q}{4\pi\varepsilon_0 r}.
   $$
