---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.6
example_number: 31.9
subtitle: “Wake up and smell the (transformer)!”
needs_review: true
---

# Example 31.9: “Wake up and smell the (transformer)!”

## Problem
A friend returns to the United States from Europe with a 960-W coffeemaker, designed to operate from a 240-V line.  
(a) What can she do to operate it at the USA-standard 120 V?  
(b) What current will the coffeemaker draw from the 120-V line?  
(c) What is the resistance of the coffeemaker?  
The voltages are rms values.

## Setup
**IDENTIFY and SET UP:** Our friend needs a step-up transformer to convert 120-V ac to the 240-V ac that the coffeemaker requires. We use Eq. (31.35) to determine the transformer turns ratio, the relation for a resistor to find the current draw, and Eq. (31.37) to calculate the resistance.

## Solution
**EXECUTE:**  
(a) To get the required turns ratio,
$$ 
\frac{N_2}{N_1}=\frac{V_2}{V_1}=\frac{240\ \text{V}}{120\ \text{V}}=2.
 $$
That is, the secondary coil (connected to the coffeemaker) should have twice as many turns as the primary coil (connected to the 120-V line).

(b) We find the rms current in the 120-V primary by using
$$ 
P_{\text{av}}=V_{\text{rms}} I_{\text{rms}},
 $$
where $P_{\text{av}} $ is the average power drawn by the coffeemaker and hence the power supplied by the 120-V line. Assuming no energy is lost in the transformer,
$$ 
I_1=\frac{P_{\text{av}}}{V_1}=\frac{960\ \text{W}}{120\ \text{V}}=8.0\ \text{A}.
 $$
The secondary current is then
$$ 
I_2=\frac{P_{\text{av}}}{V_2}=\frac{960\ \text{W}}{240\ \text{V}}=4.0\ \text{A}.
 $$

(c) We have
$$ 
V_1=120\ \text{V}, \qquad I_1=8.0\ \text{A},
 $$
so
$$ 
R=\frac{V_1}{I_1}=\frac{120\ \text{V}}{8.0\ \text{A}}=15\ \Omega.
 $$
From Eq. (31.37),
$$ 
R=\frac{V_2^2}{P_{\text{av}}}=\frac{(240\ \text{V})^2}{960\ \text{W}}=60\ \Omega.
 $$

## Evaluation
As a check, using the secondary values gives the same resistance:
$$ 
R=\frac{V_2}{I_2}=\frac{240\ \text{V}}{4.0\ \text{A}}=60\ \Omega.
 $$
You can also check this result for $R $ by using the expression
$$ 
P_{\text{av}}=\frac{V^2}{R}
 $$
for the power drawn by the coffeemaker.

## Key concepts used
- Transformer voltage ratio:
  $$ 
  \frac{N_2}{N_1}=\frac{V_2}{V_1}
   $$
- Power relation for rms values:
  $$ 
  P_{\text{av}}=V_{\text{rms}} I_{\text{rms}}
   $$
- Ohm’s law:
  $$ 
  R=\frac{V}{I}
   $$
- Resistive power relation:
  $$ 
  P_{\text{av}}=\frac{V^2}{R}
   $$
