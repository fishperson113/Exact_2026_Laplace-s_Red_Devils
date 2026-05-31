---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.3
example_number: 26.9
subtitle: Designing a voltmeter
needs_review: true
---

# Example 26.9: Designing a voltmeter

## Problem
What series resistance is required to make the 1.00-mA meter described above into a voltmeter with a range of 0 to 10.0 V?

## Setup
IDENTIFY and SET UP: Since this meter is being used as a voltmeter, its internal connections are as shown in Fig. 26.15b. Our target variable is the series resistance $R_s $. The maximum allowable voltage across the voltmeter is $V_{ab} = 10.0\ \text{V} $. We want this to occur when the current through the coil is $I_{fs} = 1.00 \times 10^{-3}\ \text{A} $. Our target variable is the series resistance $R_s $, which we find using Eq. (26.8).

## Solution
EXECUTE: From Eq. (26.8),
$$ 
R_s = \frac{V_{ab}}{I_{fs}} - R_c
 $$
$$ 
R_s = \frac{10.0\ \text{V}}{0.00100\ \text{A}} - 20.0\ \Omega = 9980\ \Omega
 $$

## Evaluation
EVALUATE: At full-scale deflection, the voltage across the meter is $0.0200\ \text{V} $, the voltage across $R_s $ is $9.98\ \text{V} $, and the current through the voltmeter is $0.00100\ \text{A} $. Most of the voltage appears across the series resistor. The meter’s equivalent resistance is a desirably high $10{,}000\ \Omega $. Such a meter is called a “1000 ohms-per-volt” meter, referring to the ratio of resistance to full-scale deflection. In normal operation the current through the circuit element being measured ($I $ in Fig. 26.15b) is much greater than $0.00100\ \text{A} $, and the resistance between points $a $ and $b $ in the circuit is much less than $10{,}000\ \Omega $. The voltmeter draws off only a small fraction of the current and thus disturbs the circuit being measured only slightly.

## Key concepts used
- A voltmeter is made by placing a large series resistance with the meter coil.
- At full-scale deflection, the meter current is the specified full-scale current.
- The series resistance is found from the desired voltage range and the meter-coil resistance.
- A high voltmeter resistance minimizes circuit disturbance.
