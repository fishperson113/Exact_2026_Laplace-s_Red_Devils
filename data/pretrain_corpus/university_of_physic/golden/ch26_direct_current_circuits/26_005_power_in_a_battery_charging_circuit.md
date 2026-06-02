---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.2
example_number: 26.5
subtitle: Power in a battery-charging circuit
needs_review: true
---

# Example 26.5: Power in a battery-charging circuit

## Problem
In the circuit of Example 26.4 (shown in Fig. 26.11), find the power delivered by the 12-V power supply and by the battery being recharged, and find the power dissipated in each resistor.

## Setup
**IDENTIFY and SET UP:** We use the results of Section 25.5, in which we found that the power delivered from an emf to a circuit is

$$ 
P_{\text{emf}} = \mathcal{E} I
 $$

and the power delivered to a resistor from a circuit is

$$ 
P = I^2 R
 $$

We know the values of all relevant quantities from Example 26.4.

## Solution
**EXECUTE:** The power output from the emf of the power supply is

$$ 
P_{\text{supply}} = \mathcal{E}_{\text{supply}} I_{\text{supply}} = (12\ \text{V})(3\ \text{A}) = 36\ \text{W}
 $$

The power dissipated in the power supply’s internal resistance $r $ is

$$ 
P_{r\text{-supply}} = I_{\text{supply}}^2 r_{\text{supply}} = (3\ \text{A})^2(2\ \Omega) = 18\ \text{W}
 $$

so the power supply’s net power output is

$$ 
P_{\text{net}} = 36\ \text{W} - 18\ \text{W} = 18\ \text{W}
 $$

Alternatively, from Example 26.4 the terminal voltage of the battery is

$$ 
V_{ba} = 6\ \text{V}
 $$

so the net power output is

$$ 
P_{\text{net}} = V_{ba} I_{\text{supply}} = (6\ \text{V})(3\ \text{A}) = 18\ \text{W}
 $$

The power output of the emf of the battery being charged is

$$ 
P_{\text{emf}} = \mathcal{E} I_{\text{battery}} = (-5\ \text{V})(1\ \text{A}) = -5\ \text{W}
 $$

This is negative because the $1\ \text{A} $ current runs through the battery from the higher-potential side to the lower-potential side. (As we mentioned in Example 26.4, the polarity assumed for this battery in Fig. 26.11 was wrong.) We are storing energy in the battery as we charge it. Additional power is dissipated in the battery’s internal resistance; this power is

$$ 
P_{r\text{-battery}} = I_{\text{battery}}^2 r_{\text{battery}} = (1\ \text{A})^2(1\ \Omega) = 1\ \text{W}
 $$

The total power input to the battery is thus

$$ 
-5\ \text{W} + 1\ \text{W} = -4\ \text{W}
 $$

Of this, $5\ \text{W} $ represents useful energy stored in the battery; the remainder is wasted in its internal resistance.

The power dissipated in the light bulb is

$$ 
P_{\text{bulb}} = I_{\text{bulb}}^2 R_{\text{bulb}} = (2\ \text{A})^2(3\ \Omega) = 12\ \text{W}
 $$

## Evaluation
As a check, note that all of the power from the supply is accounted for. Of the $18\ \text{W} $ of net power from the power supply, $5\ \text{W} $ goes to recharge the battery, $1\ \text{W} $ is dissipated in the battery’s internal resistance, and $12\ \text{W} $ is dissipated in the light bulb.

## Key concepts used
- Power delivered by an emf: $P_{\text{emf}} = \mathcal{E} I $
- Power dissipated in a resistor: $P = I^2 R $
- Net power output of a source equals emf power minus internal-resistance loss
- Negative power indicates power absorbed by the battery rather than delivered by it
