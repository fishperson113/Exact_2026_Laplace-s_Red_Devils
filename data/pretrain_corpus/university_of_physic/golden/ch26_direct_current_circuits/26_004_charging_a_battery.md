---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.2
example_number: 26.4
subtitle: Charging a battery
needs_review: true
---

# Example 26.4: Charging a battery

## Problem
In the circuit shown in Fig. 26.11, a 12-V power supply with unknown internal resistance $r $ is connected to a run-down rechargeable battery with unknown emf $E $ and internal resistance $2\,\Omega $, and to an indicator light bulb of resistance $1\,\Omega $, carrying a current of $2\ \text{A} $. The current through the run-down battery is $1\ \text{A} $ in the direction shown. Find $r $, $E $, and the current $I $ through the power supply.

## Setup
IDENTIFY and SET UP: This circuit has more than one loop, so we must apply both the junction and loop rules. We assume the direction of the current through the $12\ \text{V} $ power supply, and the polarity of the run-down battery, to be as shown in Fig. 26.11. There are three target variables, so we need three equations.

## Solution
EXECUTE: We apply the junction rule, Eq. (26.5), to point $a $:
$$ 
-I + 1\ \text{A} + 2\ \text{A} = 0
 $$
so
$$ 
I = 3\ \text{A}.
 $$

To determine $r $, we apply the loop rule, Eq. (26.6), to the large, outer loop (1):
$$ 
12\ \text{V} - 13\ \text{A}\, (2\,\Omega) - 11\ \text{A}\,(1\,\Omega) + E = 0
 $$
so
$$ 
E = -5\ \text{V}.
 $$

To determine $r $, we apply the loop rule to the left-hand loop (2):
$$ 
12\ \text{V} - 13\ \text{A}\,(2\,\Omega) - 12\ \text{A}\,r - 12\ \text{A}\,(1\,\Omega) = 0
 $$
so
$$ 
r = 2\ \Omega.
 $$

The negative value for $E $ shows that the actual polarity of this emf is opposite to that shown in Fig. 26.11. As in Example 26.3, the battery is being recharged.

## Evaluation
Try applying the junction rule at point $b $ instead of point $a $, and try applying the loop rule by traveling counterclockwise rather than clockwise around loop (1). You’ll get the same results for $I $ and $r $.

We can check our result for $E $ by using the right-hand loop (3):
$$ 
12\ \text{V} - 13\ \text{A}\,(2\,\Omega) - 11\ \text{A}\,(1\,\Omega) + E = 0,
 $$
which again gives us
$$ 
E = -5\ \text{V}.
 $$

As an additional check, we note that $V_{ba} $ equals the voltage across the $3\,\Omega $ resistance, which is $6\ \text{V} $. Going from $a $ to $b $ by the top branch, we encounter potential differences $+12\ \text{V} - 13\ \text{A}\,(2\,\Omega) = +6\ \text{V} $, and going by the middle branch, we find $12\ \text{A}\,(1\,\Omega) = 6\ \text{V} $. The three ways of getting $V_{ba} $ give the same results.

## Key concepts used
- Kirchhoff’s junction rule
- Kirchhoff’s loop rule
- Internal resistance
- Interpreting the sign of a solved emf
- Consistency checks using alternate loops and potential differences
