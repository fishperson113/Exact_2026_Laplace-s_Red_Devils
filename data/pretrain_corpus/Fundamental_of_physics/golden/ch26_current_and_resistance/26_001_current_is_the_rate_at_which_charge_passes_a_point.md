---
source: Fundamentals of Physics
chapter: 26
section: 26-1
sample_problem_number: 26.01
subtitle: Current is the rate at which charge passes a point
needs_review: false
---

# Sample Problem 26.01: Current is the rate at which charge passes a point

## Problem
Water flows through a garden hose at a volume flow rate $dV/dt $ of $450\ \text{cm}^3/\text{s} $. What is the current of negative charge?

## Key ideas
The current $i $ of negative charge is due to the electrons in the water molecules moving through the hose. The current is the rate at which that negative charge passes through any plane that cuts completely across the hose.

## Solution
We substitute 10 electrons per molecule because a water $(\mathrm{H_2O}) $ molecule contains 8 electrons in the single oxygen atom and 1 electron in each of the two hydrogen atoms.

We can express the rate $dN/dt $ in terms of the given volume flow rate $dV/dt $ by first writing
$$ 
\frac{dN}{dt}
=
N_A
\left(\frac{1}{M}\right)
\rho_{\text{mass}}
\frac{dV}{dt}
=
\frac{N_A \rho_{\text{mass}}}{M}\frac{dV}{dt}.
 $$
“Molecules per mole” is Avogadro’s number $N_A $. “Moles per unit mass” is the inverse of the mass per mole, which is the molar mass $M $ of water. “Mass per unit volume” is the density $\rho_{\text{mass}} $ of water. The volume per second is the volume flow rate $dV/dt $. Thus,
$$ 
\frac{dN}{dt}
=
\left(\frac{\text{molecules}}{\text{mole}}\right)
\left(\frac{\text{moles}}{\text{unit mass}}\right)
\left(\frac{\text{mass}}{\text{unit volume}}\right)
\left(\frac{\text{volume}}{\text{second}}\right).
 $$

Substituting this into the equation for $i $, we find
$$ 
i = 10 e N_A M^{-1} \rho_{\text{mass}} \frac{dV}{dt}.
 $$

We know that Avogadro’s number $N_A $ is $6.02 \times 10^{23}\ \text{mol}^{-1} $, and from Table 15-1 we know that the density of water $\rho_{\text{mass}} $ under normal conditions is $1000\ \text{kg/m}^3 $. We can get the molar mass of water from the molar masses listed in Appendix F (in grams per mole): we add the molar mass of oxygen $(16\ \text{g/mol}) $ to twice the molar mass of hydrogen $(1\ \text{g/mol}) $, obtaining $18\ \text{g/mol} = 0.018\ \text{kg/mol} $.

So, the current of negative charge due to the electrons in the water is
$$ 
i
=
(10)(1.6 \times 10^{-19}\ \text{C})(6.02 \times 10^{23}\ \text{mol}^{-1})
(0.018\ \text{kg/mol})^{-1}
(1000\ \text{kg/m}^3)
(450 \times 10^{-6}\ \text{m}^3/\text{s}).
 $$

## Answer
$$ 
i = 2.41 \times 10^{7}\ \text{A}
 $$
or
$$ 
i \approx 24.1\ \text{MA}.
 $$

This current of negative charge is exactly compensated by a current of positive charge associated with the nuclei of the three atoms that make up the water molecule. Thus, there is no net flow of charge through the hose.

## Key concepts used
- Current is the rate at which charge passes through a cross section.
- Water molecules contain electrons that contribute to negative charge transport.
- Avogadro’s number, molar mass, and mass density can be used to convert a volume flow rate into a charge flow rate.
- The current from negative charge is balanced by the positive charge of the nuclei, so the net charge flow is zero.
