---
source: Young and Freedman University Physics, 13th ed.
chapter: 25
section: 25.5
example_number: 25.9
subtitle: Increasing the resistance
needs_review: true
---

# Example 25.9: Increasing the resistance

## Problem
Suppose we replace the external resistor in Fig. 25.24 with a resistor. How does this affect the electrical power dissipated in this resistor?

## Setup
**IDENTIFY and SET UP:** Our target variable is the power dissipated in the resistor to which the battery is connected. The situation is the same as in Example 25.8, but with a higher external resistance.

## Solution
**EXECUTE:** According to Eq. (25.18), the power dissipated in the resistor is

$$ 
P = I^2 R.
 $$

You might conclude that making the resistance twice as great as in Example 25.8 should also make the power twice as great, or

$$ 
P = \frac{V_{ab}^2}{R}.
 $$

If instead you used the formula

$$ 
P = \frac{V_{ab}^2}{R},
 $$

you might conclude that the power should be one-half as great as in the preceding example, or

$$ 
P = \frac{1}{2}(12\ \text{W}) = 6\ \text{W}.
 $$

Which answer is correct?

In fact, both of these answers are incorrect. The first is wrong because changing the resistance also changes the current in the circuit (remember, a source of emf does not generate the same current in all situations). The second answer is wrong because the potential difference $V_{ab} $ across the resistor changes when the current changes. To get the correct answer, we first find the current just as we did in Example 25.5:

$$ 
I = \frac{\mathcal{E}}{R + r} = \frac{12\ \text{V}}{8\ \Omega + 2\ \Omega} = 1.2\ \text{A}.
 $$

The greater resistance causes the current to decrease. The potential difference across the resistor is

$$ 
V_{ab} = IR = (1.2\ \text{A})(8\ \Omega) = 9.6\ \text{V},
 $$

which is greater than that with the $4\ \Omega $ resistor. We can then find the power dissipated in the resistor in either of two ways:

$$ 
P = I^2 R = (1.2\ \text{A})^2(8\ \Omega) = 12\ \text{W},
 $$

or

$$ 
P = \frac{V_{ab}^2}{R} = \frac{(9.6\ \text{V})^2}{8\ \Omega} = 12\ \text{W}.
 $$

## Evaluation
**EVALUATE:** Increasing the resistance causes a reduction in the power input to the resistor. In the expression $P = I^2R $, the decrease in current is more important than the increase in resistance; in the expression $P = V_{ab}^2/R $, the increase in resistance is more important than the increase in $V_{ab} $. This same principle applies to ordinary light bulbs; a $100\ \text{W} $ light bulb has a greater resistance than does a $50\ \text{W} $ light bulb.

Can you show that replacing the $4\ \Omega $ resistor with an $8\ \Omega $ resistor decreases both the rate of energy conversion (chemical to electrical) in the battery and the rate of energy dissipation in the battery?

## Key concepts used
- The current in a circuit depends on the total resistance, including internal resistance $r $.
- Power can be written as $P = I^2R $ or $P = V_{ab}^2/R $, but $I $ and $V_{ab} $ change when the resistance changes.
- Increasing the external resistance reduces the current and can reduce the power dissipated in the external resistor.
- The terminal voltage across the resistor is $V_{ab} = IR $.
