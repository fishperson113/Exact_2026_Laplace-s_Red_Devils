---
source: Young and Freedman University Physics, 13th ed.
chapter: 25
section: 25.3
example_number: 25.2
subtitle: Electric field, potential difference, and resistance in a wire
needs_review: true
---

# Example 25.2: Electric field, potential difference, and resistance in a wire

## Problem
The 18-gauge copper wire of Example 25.1 has a cross-sectional area of 8.20 × 10^-7 m^2. It carries a current of 1.67 A. Find (a) the electric-field magnitude in the wire; (b) the potential difference between two points in the wire 50.0 m apart; (c) the resistance of a length of this wire.

## Setup
**IDENTIFY and SET UP:** We are given the cross-sectional area $A $ and current $I $. Our target variables are the electric-field magnitude $E $, potential difference $V $, and resistance $R $.

The current density is
$$ 
J = \frac{I}{A}.
 $$

We find $E $ from Eq. (25.5),
$$ 
E = \rho J = \rho \frac{I}{A},
 $$
where Table 25.1 gives the resistivity $\rho $ for copper.

The potential difference is then the product of $E $ and the length $L $ of the wire:
$$ 
V = EL.
 $$

We can use either Eq. (25.10) or Eq. (25.11) to find $R $.

## Solution
**EXECUTE:**

(a) From Table 25.1, for copper,
$$ 
\rho = 1.72 \times 10^{-8}\ \Omega \cdot \text{m}.
 $$
Hence, using Eq. (25.5),
$$ 
E = \rho \frac{I}{A}
= \frac{(1.72 \times 10^{-8}\ \Omega \cdot \text{m})(1.67\ \text{A})}{8.20 \times 10^{-7}\ \text{m}^2}
= 0.0350\ \text{V/m}.
 $$

(b) The potential difference is
$$ 
V = EL = (0.0350\ \text{V/m})(50.0\ \text{m}) = 1.75\ \text{V}.
 $$

(c) From Eq. (25.10), the resistance of 50.0 m of this wire is
$$ 
R = \rho \frac{L}{A}
= \frac{(1.72 \times 10^{-8}\ \Omega \cdot \text{m})(50.0\ \text{m})}{8.20 \times 10^{-7}\ \text{m}^2}
= 1.05\ \Omega.
 $$

Alternatively, we can find $R $ using Eq. (25.11):
$$ 
R = \frac{V}{I} = \frac{1.75\ \text{V}}{1.67\ \text{A}} = 1.05\ \Omega.
 $$

## Evaluation
We emphasize that the resistance of the wire is defined to be the ratio of voltage to current. If the wire is made of nonohmic material, $R $ is different for different values of $V $ but is always given by
$$ 
R = \frac{V}{I}.
 $$
Resistance is also always given by
$$ 
R = \rho \frac{L}{A};
 $$
if the material is nonohmic, $\rho $ is not constant but depends on $V $ (or, equivalently, on $V = EL $).

## Key concepts used
- Current density: $J = I/A $
- Ohm’s law in microscopic form: $E = \rho J $
- Potential difference in a uniform field: $V = EL $
- Resistance of a uniform wire: $R = \rho L/A $
- Equivalent resistance definition: $R = V/I $
