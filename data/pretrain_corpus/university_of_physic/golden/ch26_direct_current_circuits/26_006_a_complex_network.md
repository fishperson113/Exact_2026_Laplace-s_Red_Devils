---
source: Young and Freedman University Physics, 13th ed.
chapter: 26
section: 26.2
example_number: 26.6
subtitle: A complex network
needs_review: true
---

# Example 26.6: A complex network

## Problem
Figure 26.12 shows a “bridge” circuit of the type described at the beginning of this section (see Fig. 26.6b). Find the current in each resistor and the equivalent resistance of the network of five resistors.

## Setup
IDENTIFY and SET UP: This network is neither a series combination nor a parallel combination. Hence we must use Kirchhoff’s rules to find the values of the target variables. There are five unknown currents, but by applying the junction rule to junctions a and b, we can represent them in terms of three unknown currents, $I_1 $, $I_2 $, and $I_3 $, as shown in Fig. 26.12.

## Solution
EXECUTE: We apply the loop rule to the three loops shown:

$$ 
(1)
 $$

$$ 
(2)
 $$

$$ 
(3)
 $$

One way to solve these simultaneous equations is to solve Eq. (3) for $I_2 $, obtaining

$$ 
I_2 = I_1 + I_3,
 $$

and then substitute this expression into Eq. (2) to eliminate $I_2 $. We then have

$$ 
13\ \text{V} - I_1(1\ \Omega) - (I_1 - I_3)(1\ \Omega) = 0
 $$

$$ 
- I_1(1\ \Omega) - I_3(1\ \Omega) + I_2(1\ \Omega) = 0
 $$

Now we can eliminate $I_3 $ by multiplying Eq. (1) by 5 and adding the two equations. We obtain

$$ 
78\ \text{V} = I_1(13\ \Omega)
 $$

so

$$ 
I_1 = 6\ \text{A}.
 $$

We substitute this result into Eq. (2) to obtain $I_2 = 5\ \text{A} $, and from Eq. (3) we find $I_3 = -1\ \text{A} $.

The negative value of $I_3 $ tells us that its direction is opposite to the direction we assumed.

The total current through the network is

$$ 
I_1 + I_2 = 11\ \text{A},
 $$

and the potential drop across it is equal to the battery emf, $13\ \text{V} $. The equivalent resistance of the network is therefore

$$ 
R_{\text{eq}} = \frac{13\ \text{V}}{11\ \text{A}} = 1.2\ \Omega.
 $$

## Evaluation
You can check our results for $I_1 $ and $I_2 $ by substituting them back into Eqs. (1)–(3). What do you find?

## Key concepts used
- Kirchhoff’s junction rule
- Kirchhoff’s loop rule
- Solving simultaneous equations for circuit currents
- Equivalent resistance from $R_{\text{eq}} = V/I $
