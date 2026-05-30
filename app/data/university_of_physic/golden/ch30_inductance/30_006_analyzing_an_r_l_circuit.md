---
source: Young and Freedman University Physics, 13th ed.
chapter: 30
section: 30.4
example_number: 30.6
subtitle: Analyzing an R-L circuit
needs_review: true
---

# Example 30.6: Analyzing an R-L circuit

## Problem
A sensitive electronic device of resistance is to be connected to a source of emf (of negligible internal resistance) by a switch. The device is designed to operate with a 36-mA current, but to avoid damage to the device, the current can rise to no more than 4.9 mA in the first after the switch is closed. An inductor is therefore connected in series with the device, as in Fig. 30.11; the switch in question is .

(a) What is the required source emf?  
(b) What is the required inductance \(L\)?  
(c) What is the \(R\)-\(L\) time constant?

## Setup
**IDENTIFY and SET UP:** This problem concerns current and current growth in an \(R\)-\(L\) circuit, so we can use the ideas of this section. Figure 30.12 shows the current \(i\) versus the time \(t\) that has elapsed since closing . The graph shows that the final current is ; we are given \(R\), so the emf is determined by the requirement that the final current be \(I = 36\ \text{mA}\). The other requirement is that the current be no more than at . To satisfy this, we use Eq. (30.14) for the current as a function of time and solve for the inductance, which is the only unknown quantity. Equation (30.16) then tells us the time constant.

## Solution
**EXECUTE:**  
(a) We solve \(I = E/R\) for \(E\):
\[
E = IR = (0.036\ \text{A})(175\ \Omega) = 6.3\ \text{V}
\]

(b) To find the required inductance, we solve Eq. (30.14) for \(L\). First we multiply through by \(E\) and then add 1 to both sides to obtain
\[
1 - \frac{iR}{E} = e^{-(R/L)t}
\]
Then we take natural logs of both sides, solve for \(L\), and insert the numbers:
\[
L = -\frac{Rt}{\ln\!\left(1 - iR/E\right)}
\]
\[
L = -\frac{(175\ \Omega)(58\times 10^{-6}\ \text{s})}{\ln\!\left[1 - (4.9\times 10^{-3}\ \text{A})(175\ \Omega)/(6.3\ \text{V})\right]}
= 69\times 10^{-3}\ \text{H} = 69\ \text{mH}
\]

(c) From Eq. (30.16),
\[
t = \frac{L}{R} = \frac{69\times 10^{-3}\ \text{H}}{175\ \Omega}
= 3.9\times 10^{-4}\ \text{s} = 390\ \text{ms}
\]

## Evaluation
Note that \(58\ \text{ms}\) is much less than the time constant. In \(58\ \text{ms}\), the current builds up from zero to \(4.9\ \text{mA}\), a small fraction of its final value of \(36\ \text{mA}\); after \(58\ \text{ms}\) the current equals \((1 - 1/e)\) of its final value, or about \(23\ \text{mA}\).

## Key concepts used
- Current growth in an \(R\)-\(L\) circuit follows
  \[
  i = \frac{E}{R}\left(1 - e^{-(R/L)t}\right)
  \]
- The final current in a series \(R\)-\(L\) circuit is
  \[
  I = \frac{E}{R}
  \]
- The inductive time constant is
  \[
  \tau = \frac{L}{R}
  \]
- Solving the current-growth equation for \(L\) gives
  \[
  L = -\frac{Rt}{\ln(1 - iR/E)}
  \]
