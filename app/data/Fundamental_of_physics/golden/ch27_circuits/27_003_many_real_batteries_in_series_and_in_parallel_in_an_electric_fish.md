---
source: Fundamentals of Physics
chapter: 27
section: 27-2
sample_problem_number: 27.03
subtitle: Many real batteries in series and in parallel in an electric fish
needs_review: true
---

# Sample Problem 27.03: Many real batteries in series and in parallel in an electric fish

## Problem
Electric fish can generate current with biological emf cells called electroplaques. In the South American eel they are arranged in 140 rows, each row stretching horizontally along the body and each containing 5000 cells, as suggested by Fig. 27-12a. Each electroplaque has an emf of 0.15 V and an internal resistance of 0.25 Ω. The water surrounding the eel completes a circuit between the two ends of the electroplaque array, one end at the head of the animal and the other near the tail.

(a) If the surrounding water has resistance $R_w = 800\ \Omega $, how much current can the eel produce in the water?

(b) How much current $i_{\text{row}} $ travels through each row of Fig. 27-12a?

## Key ideas
We can simplify the circuit of Fig. 27-12a by replacing combinations of emfs and internal resistances with equivalent emfs and resistances.

Because the rows are identical, the current into and out of the eel is evenly divided among them.

## Solution
### (a)
We first consider a single row. The total emf $\mathcal{E}_{\text{row}} $ along a row of 5000 electroplaques is the sum of the emfs:

$$ 
\mathcal{E}_{\text{row}} = 5000\mathcal{E} = (5000)(0.15\ \text{V}) = 750\ \text{V}.
 $$

First, reduce each row to one emf and one resistance. Emfs in parallel act as a single emf. Replace the parallel resistances with their equivalent. Points with the same potential can be taken as though connected.

Replacing the parallel combination with $R_{\text{eq}} $, we obtain the simplified circuit of Fig. 27-12d. Applying the loop rule to this circuit counterclockwise from point $b $, we have

$$ 
\mathcal{E}_{\text{row}} - iR_w - iR_{\text{eq}} = 0.
 $$

Solving for $i $ and substituting the known data, we find

$$ 
i = \frac{\mathcal{E}_{\text{row}}}{R_w + R_{\text{eq}}}
= \frac{750\ \text{V}}{800\ \Omega + 8.93\ \Omega}
= 0.927\ \text{A} \approx 0.93\ \text{A}.
 $$

If the head or tail of the eel is near a fish, some of this current could pass along a narrow path through the fish, stunning or killing it.

### (b)
Because the rows are identical, the current into and out of the eel is evenly divided among them. Thus, we write

$$ 
i_{\text{row}} = \frac{i}{140} = \frac{0.927\ \text{A}}{140} = 6.6 \times 10^{-3}\ \text{A}.
 $$

Thus, the current through each row is small, so that the eel need not stun or kill itself when it stuns or kills a fish.

## Answer
$$ 
\boxed{i = 0.93\ \text{A}}
 $$

$$ 
\boxed{i_{\text{row}} = 6.6 \times 10^{-3}\ \text{A}}
 $$

## Key concepts used
- Replace series combinations of emfs and resistances with equivalent values.
- Replace parallel resistances with an equivalent resistance.
- Apply the loop rule to the simplified circuit.
- For identical parallel rows, divide the total current evenly among the rows.
