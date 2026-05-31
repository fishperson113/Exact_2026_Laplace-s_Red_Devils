---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.3
example_number: 26.10
subtitle: Measuring resistance I
needs_review: true
---

# Example 26.10: Measuring resistance I

## Problem
The voltmeter in the circuit of Fig. 26.16a reads 12.0 V and the ammeter reads 0.100 A. The meter resistances are $R_A = 2.00\ \Omega $ for the ammeter and $R_V = 10{,}000\ \Omega $ for the voltmeter. What are the resistance $R $ and the power dissipated in the resistor?

## Setup
IDENTIFY and SET UP: The ammeter reads the current $I = 0.100\ \text{A} $ through the resistor, and the voltmeter reads the potential difference between $a $ and $c $, $V = 12.0\ \text{V} $.

If the ammeter were ideal ($R_A = 0 $), there would be zero potential difference between $b $ and $c $, the voltmeter reading would be equal to the potential difference across the resistor, and the resistance would simply be $R = V/I $.

The ammeter is not ideal, however (its resistance is $R_A = 2.00\ \Omega $), so the voltmeter reading $V $ is actually the sum of the potential differences $V_{ab} $ (across the ammeter) and $V_{bc} $ (across the resistor).

## Solution
We use Ohm’s law to find the voltage $V_{ab} $ from the known current and the ammeter resistance:
$$ 
V_{ab} = IR_A = (0.100\ \text{A})(2.00\ \Omega) = 0.200\ \text{V}.
 $$

Then the voltage across the resistor is
$$ 
V_{bc} = V - V_{ab} = 12.0\ \text{V} - 0.200\ \text{V} = 11.8\ \text{V}.
 $$

Now the resistance is
$$ 
R = \frac{V_{bc}}{I} = \frac{11.8\ \text{V}}{0.100\ \text{A}} = 118\ \Omega.
 $$

The power dissipated in the resistor is
$$ 
P = IV_{bc} = (0.100\ \text{A})(11.8\ \text{V}) = 1.18\ \text{W}.
 $$

## Evaluation
If the ammeter were ideal, the resistance would be $12.0\ \text{V}/0.100\ \text{A} = 120\ \Omega $. Because the ammeter has a small resistance, the actual resistance is slightly smaller: $118\ \Omega $.

## Key concepts used
- Ideal and nonideal ammeter behavior
- Voltmeter measures potential difference between two points in a circuit
- Ohm’s law, $V = IR $
- Electric power, $P = IV $
