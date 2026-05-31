---
source: Fundamentals of Physics
chapter: 31
section: 31-6
sample_problem_number: 31.08
subtitle: Transformer: turns ratio, average power, rms currents
needs_review: true
---

# Sample Problem 31.08: Transformer: turns ratio, average power, rms currents

## Problem
A transformer on a utility pole operates at $V_p = 8.5\ \text{kV} $ on the primary side and supplies electrical energy to a number of nearby houses at $V_s = 120\ \text{V} $, both quantities being rms values. Assume an ideal step-down transformer, a purely resistive load, and a power factor of unity.

(a) What is the turns ratio $N_p/N_s $ of the transformer?

(b) The average rate of energy consumption (or dissipation) in the houses served by the transformer is 78 kW. What are the rms currents in the primary and secondary of the transformer?

## Key ideas
The turns ratio $N_p/N_s $ is related to the rms primary and secondary voltages via Eq. 31-79:
$$ 
V_s = V_p \frac{N_s}{N_p}.
 $$

For a purely resistive load, the power factor $\cos \phi $ is unity; thus, the average rate at which energy is supplied and dissipated is given by Eq. 31-77:
$$ 
P_{\text{avg}} = I_{\text{rms}} V_{\text{rms}}.
 $$

## Solution
### (a) Turns ratio
We can write Eq. 31-79 as
$$ 
\frac{N_p}{N_s} = \frac{V_p}{V_s}.
 $$

Substituting the given rms voltages,
$$ 
\frac{N_p}{N_s} = \frac{8.5 \times 10^3\ \text{V}}{120\ \text{V}} = 70.83 \approx 71.
 $$

So,
$$ 
\frac{N_p}{N_s} = 71.
 $$

### (b) rms currents in the primary and secondary
For a purely resistive load, the average power is
$$ 
P_{\text{avg}} = I_{\text{rms}} V_{\text{rms}}.
 $$

In the secondary circuit,
$$ 
I_{s,\text{rms}} = \frac{P_{\text{avg}}}{V_s}
= \frac{78\,000\ \text{W}}{120\ \text{V}}
= 650\ \text{A}.
 $$

For an ideal transformer,
$$ 
I_s = I_p \frac{N_p}{N_s},
 $$
so
$$ 
I_p = I_s \frac{N_s}{N_p} = \frac{I_s}{N_p/N_s}.
 $$

Thus,
$$ 
I_{p,\text{rms}} = \frac{650\ \text{A}}{70.83} \approx 9.18\ \text{A} \approx 9.2\ \text{A}.
 $$

## Answer
$$ 
\frac{N_p}{N_s} = 71
 $$

$$ 
I_{s,\text{rms}} = 650\ \text{A}, \qquad I_{p,\text{rms}} = 9.2\ \text{A}
 $$

## Key concepts used
- Ideal transformer voltage ratio
- Ideal transformer current ratio
- Average power in a resistive ac circuit
- rms voltage and rms current
