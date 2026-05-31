---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.3
example_number: 26.7
subtitle: A potential difference in a complex network
needs_review: true
---

# Example 26.7: A potential difference in a complex network

## Problem
In the circuit of Example 26.6 (Fig. 26.12), find the potential difference $V_{ab} = V_a - V_b $.

## Setup
**IDENTIFY and SET UP:** Our target variable is the potential at point $a $ with respect to point $b $. To find it, we start at point $b $ and follow a path to point $a $, adding potential rises and drops as we go. We can follow any of several paths from $b $ to $a $; the result must be the same for all such paths, which gives us a way to check our result.

## Solution
**EXECUTE:** The simplest path is through the center resistor. In Example 26.6 we found $I_3 = -1\ \text{A} $, showing that the actual current direction through this resistor is from right to left. Thus, as we go from $b $ to $a $, there is a drop of potential with magnitude
$$ 
|I_3|R = |{-1\ \text{A}}|(1\ \Omega) = 1\ \text{V}.
 $$
Hence
$$ 
V_{ab} = -1\ \text{V},
 $$
and the potential at $a $ is $1\ \text{V} $ less than at point $b $.

## Evaluation
**EVALUATE:** To check our result, let’s try a path from $b $ to $a $ that goes through the lower two resistors. The currents through these are
$$ 
I_1 - I_3 = 6\ \text{A} - (-1\ \text{A}) = 7\ \text{A}
 $$
and
$$ 
I_2 + I_3 = 5\ \text{A} + (-1\ \text{A}) = 4\ \text{A},
 $$
and so
$$ 
V_{ab} = -(14\ \text{A})(2\ \Omega) + (17\ \text{A})(1\ \Omega) = -1\ \text{V}.
 $$
You can confirm this result using some other paths from $b $ to $a $.

## Key concepts used
- Electric potential difference is found by summing potential rises and drops along a path.
- In a circuit with consistent node potentials, the result is path independent.
- A negative current indicates the actual current direction is opposite the assumed direction.
- The potential drop across a resistor is $IR $, with sign determined by traversal direction relative to current.
