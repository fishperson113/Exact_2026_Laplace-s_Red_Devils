---
source: Young and Freedman University Physics, 13th ed.
chapter: 27
section: 27.9
example_number: 27.12
subtitle: A Hall-effect measurement
needs_review: true
---

# Example 27.12: A Hall-effect measurement

## Problem
You place a strip of copper, 2.0 mm thick and 1.50 cm wide, in a uniform 0.40-T magnetic field as shown in Fig. 27.41a. When you run a 75-A current in the strip, you find that the potential at the bottom of the slab is 0.81 mV higher than at the top. From this measurement, determine the concentration of mobile electrons in copper.

## Setup
This is a Hall-effect experiment. Use Eq. (27.30) to determine the mobile electron concentration.

The current flows in the $x $-direction, the magnetic field is $B_y = 0.40\ \text{T} $, and the Hall electric field is across the thickness of the slab:
$$ 
E_z = \frac{V}{d}
 $$
where $V = 0.81\ \text{mV} $ and $d = 1.5 \times 10^{-2}\ \text{m} $.

The current density is
$$ 
J_x = \frac{I}{A}
 $$
with cross-sectional area
$$ 
A = (2.0 \times 10^{-3}\ \text{m})(1.50 \times 10^{-2}\ \text{m}).
 $$

## Solution
First find the electric field:
$$ 
E_z = \frac{V}{d}
= \frac{0.81\times 10^{-3}\ \text{V}}{1.5\times 10^{-2}\ \text{m}}
= 5.4\times 10^{-5}\ \text{V/m}.
 $$

Then find the current density:
$$ 
J_x = \frac{I}{A}
= \frac{75\ \text{A}}{(2.0\times 10^{-3}\ \text{m})(1.50\times 10^{-2}\ \text{m})}
= 2.5\times 10^{6}\ \text{A/m}^2.
 $$

From Eq. (27.30),
$$ 
E_z = -\frac{J_x B_y}{n q},
 $$
so
$$ 
n = -\frac{J_x B_y}{qE_z}.
 $$

Substitute the values:
$$ 
n
= -\frac{(2.5\times 10^{6}\ \text{A/m}^2)(0.40\ \text{T})}{(-1.60\times 10^{-19}\ \text{C})(5.4\times 10^{-5}\ \text{V/m})}
= 1.16\times 10^{29}\ \text{m}^{-3}.
 $$

## Evaluation
The actual value of $n $ for copper is $8.5\times 10^{28}\ \text{m}^{-3} $. The difference shows that this simple model of the Hall effect, which ignores quantum effects and electron interactions with the ions, must be used with caution.

This example also shows that with good conductors, the Hall emf is very small even with large current densities. In practice, Hall-effect devices for magnetic-field measurements use semiconductor materials, for which moderate current densities give much larger Hall emfs.

## Key concepts used
- Hall effect in a current-carrying conductor
- Relation between Hall electric field, current density, magnetic field, and carrier concentration
- Current density: $J = I/A $
- Hall-field relation for mobile electrons:
  $$ 
  E = -\frac{J B}{n q}
   $$
- Sign of the charge carrier is essential in determining the direction of the Hall field
