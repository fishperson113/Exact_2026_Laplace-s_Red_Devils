---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.3
example_number: 24.6
subtitle: A capacitor network
needs_review: true
---

# Example 24.6: A capacitor network

## Problem
Find the equivalent capacitance of the five-capacitor network shown in Fig. 24.10a.

## Setup
**IDENTIFY and SET UP:** These capacitors are neither all in series nor all in parallel. We can, however, identify portions of the arrangement that are either in series or parallel. We combine these as described in Problem-Solving Strategy 24.1 to find the net equivalent capacitance, using Eq. (24.5) for series connections and Eq. (24.7) for parallel connections.

## Solution
**EXECUTE:** The caption of Fig. 24.10 outlines our procedure. We first use Eq. (24.5) to replace the 6-mF and 12-mF series combination by its equivalent capacitance:

$$ 
\frac{1}{C'}=\frac{1}{12\ \text{mF}}+\frac{1}{6\ \text{mF}}
\qquad
C' = 4\ \text{mF}
 $$

This gives us the equivalent combination of Fig. 24.10b. Now we see three capacitors in parallel, and we use Eq. (24.7) to replace them with their equivalent capacitance:

$$ 
C_- = 3\ \text{mF} + 11\ \text{mF} + 4\ \text{mF} = 18\ \text{mF}
 $$

This gives us the equivalent combination of Fig. 24.10c, which has two capacitors in series. We use Eq. (24.5) to replace them with their equivalent capacitance, which is our target variable $C_{\mathrm{eq}} $ (Fig. 24.10d):

$$ 
\frac{1}{C_{\mathrm{eq}}}=\frac{1}{18\ \text{mF}}+\frac{1}{9\ \text{mF}}
\qquad
C_{\mathrm{eq}} = 6\ \text{mF}
 $$

## Evaluation
If the potential difference across the entire network in Fig. 24.10a is $V_{ab} = 9.0\ \text{V} $, the net charge on the network is

$$ 
Q = C_{\mathrm{eq}}V_{ab} = (6\ \text{mF})(9.0\ \text{V}) = 54\ \text{mC}
 $$

Can you find the charge on, and the voltage across, each of the five individual capacitors?

## Key concepts used
- Identify subgroups of capacitors in series or parallel.
- Replace series combinations using Eq. (24.5).
- Replace parallel combinations using Eq. (24.7).
- Repeat reduction steps until a single equivalent capacitance remains.
- Use $Q = C_{\mathrm{eq}}V $ to find the net charge when the potential difference is known.
