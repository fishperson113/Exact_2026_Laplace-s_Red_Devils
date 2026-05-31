---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.2
example_number: 26.3
subtitle: A single-loop circuit
needs_review: true
---

# Example 26.3: A single-loop circuit

## Problem
The circuit shown in Fig. 26.10a contains two batteries, each with an emf and an internal resistance, and two resistors. Find:

(a) the current in the circuit  
(b) the potential difference $V_{ab} $  
(c) the power output of the emf of each battery

## Setup
IDENTIFY and SET UP: There are no junctions in this single-loop circuit, so Kirchhoff’s junction rule is not needed. To apply Kirchhoff’s loop rule, assume a direction for the current; here, the current is assumed to be counterclockwise as shown in Fig. 26.10a.

## Solution
EXECUTE:

### (a) Current in the circuit
Starting at point $a $ and traveling counterclockwise with the current, add potential increases and decreases around the loop and set the sum equal to zero:

$$ 
8\ \text{V} = I(16\ \Omega)
 $$

equivalently,

$$ 
- I(14\ \Omega) - 4\ \text{V} - I(7\ \Omega) + 12\ \text{V} - I(2\ \Omega) - I(3\ \Omega) = 0
 $$

Collecting like terms and solving for $I $,

$$ 
I = 0.5\ \text{A}
 $$

The positive result shows that the assumed current direction is correct.

### (b) Potential difference $V_{ab} $
To find the potential at $a $ with respect to $b $, start at $b $ and add potential changes moving toward $a $. There are two paths from $b $ to $a $.

Using the lower path:

$$ 
V_{ab} = 12\ \text{V} - 10.5\ \text{A}(2\ \Omega) - 10.5\ \text{A}(3\ \Omega) = 9.5\ \text{V}
 $$

Using the upper path:

$$ 
V_{ab} = 10.5\ \text{A}(7\ \Omega) + 4\ \text{V} + 10.5\ \text{A}(14\ \Omega) = 9.5\ \text{V}
 $$

Point $a $ is at $9.5\ \text{V} $ higher potential than $b $. The two paths give the same value for $V_{ab} $, as they must.

### (c) Power output of each battery
The power outputs of the emf of the 12-V and 4-V batteries are

$$ 
P_{12\text{V}} = EI = (12\ \text{V})(0.5\ \text{A}) = 6\ \text{W}
 $$

$$ 
P_{4\text{V}} = EI = (-4\ \text{V})(0.5\ \text{A}) = -2\ \text{W}
 $$

The negative sign for $P_{4\text{V}} $ appears because the current actually runs from the higher-potential side of the battery to the lower-potential side. A negative value of $P $ means energy is being stored in that battery; the 12-V battery is recharging it.

## Evaluation
By applying $P = I^2R $ to each of the four resistors in Fig. 26.10a, the total power dissipated in all four resistors is $4\ \text{W} $. Of the $6\ \text{W} $ provided by the emf of the 12-V battery, $2\ \text{W} $ goes into storing energy in the 4-V battery and $4\ \text{W} $ is dissipated in the resistances.

This circuit is analogous to using a fully charged 12-V storage battery to jump-start a car with a run-down battery. The run-down battery is slightly recharged in the process. The $7\ \Omega $ and $3\ \Omega $ resistors represent the resistances of the jumper cables and the conducting path through the automobile with the run-down battery.

## Key concepts used
- Kirchhoff’s loop rule
- Single-loop circuit analysis
- Assumed current direction and sign convention
- Potential difference between two points
- Electrical power of an emf: $P = EI $
- Power dissipated in resistors: $P = I^2R $
