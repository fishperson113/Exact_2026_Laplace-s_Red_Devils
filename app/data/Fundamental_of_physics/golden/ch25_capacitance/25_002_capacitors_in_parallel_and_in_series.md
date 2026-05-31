---
source: Fundamentals of Physics
chapter: 25
section: 25-3
sample_problem_number: 25.02
subtitle: Capacitors in parallel and in series
needs_review: true
---

# Sample Problem 25.02: Capacitors in parallel and in series

## Problem
(a) Find the equivalent capacitance for the combination of capacitances shown in Fig. 25-10a, across which potential difference V is applied. Assume  
\(C_1 = 12.0\ \mu\text{F}\),  
\(C_2 = 5.30\ \mu\text{F}\),  
and  
\(C_3 = 4.50\ \mu\text{F}\).

(b) The potential difference applied to the input terminals in Fig. 25-10a is \(V = 12.5\ \text{V}\). What is the charge on \(C_1\)?

## Key ideas
Any capacitors connected in series can be replaced with their equivalent capacitor, and any capacitors connected in parallel can be replaced with their equivalent capacitor.

We first reduce the circuit to a single capacitor. Next, we work backwards to the desired capacitor.

Series capacitors and their equivalent have the same \(q\) (“seri-q”). Parallel capacitors and their equivalent have the same \(V\) (“par-V”).

Applying \(V = q/C\) yields the potential difference. Applying \(q = CV\) yields the charge.

The equivalent of parallel capacitors is larger. The equivalent of series capacitors is smaller.

We can easily extend this to any number \(n\) of capacitors as
\[
\frac{1}{C_{\rm eq}}=\sum_{j=1}^{n}\frac{1}{C_j}.
\]
Using Eq. 25-20 you can show that the equivalent capacitance of a series of capacitances is always less than the least capacitance in the series.

## Solution
### (a) Equivalent capacitance

Are capacitor 1 and capacitor 2 in parallel? Yes. Their top plates are directly wired together and their bottom plates are directly wired together, and electric potential is applied between the top-plate pair and the bottom-plate pair. Thus, capacitor 1 and capacitor 2 are in parallel, and Eq. 25-19 tells us that their equivalent capacitance \(C_{12}\) is
\[
C_{12}=C_1+C_2=12.0\ \mu\text{F}+5.30\ \mu\text{F}=17.3\ \mu\text{F}.
\]

Is capacitor 12 in series with capacitor 3? Again applying the test for series capacitances, we see that the charge that shifts from the top plate of capacitor 3 must entirely go to the bottom plate of capacitor 12. Thus, capacitor 12 and capacitor 3 are in series, and we can replace them with their equivalent \(C_{123}\) (“one two three”).

From Eq. 25-20,
\[
\frac{1}{C_{123}}=\frac{1}{C_{12}}+\frac{1}{C_3}.
\]
Thus,
\[
\frac{1}{C_{123}}=\frac{1}{17.3\ \mu\text{F}}+\frac{1}{4.50\ \mu\text{F}}
=0.280\ \mu\text{F}^{-1},
\]
from which
\[
C_{123}=3.57\ \mu\text{F}.
\]

### (b) Charge on \(C_1\)

We now need to work backwards from the equivalent capacitance to get the charge on a particular capacitor. We have two techniques for such “backwards work”: (1) Seri-q: Series capacitors have the same charge as their equivalent capacitor. (2) Par-V: Parallel capacitors have the same potential difference as their equivalent capacitor.

Working backwards: To get the charge \(q_1\) on capacitor 1, we work backwards to that capacitor, starting with the equivalent capacitor 123. Because the given potential difference \(V = 12.5\ \text{V}\) is applied across the actual combination of three capacitors in Fig. 25-10a, it is also applied across \(C_{123}\). Thus, Eq. 25-1 (\(q = CV\)) gives us
\[
q_{123}=C_{123}V=(3.57\ \mu\text{F})(12.5\ \text{V})=44.6\ \mu\text{C}.
\]

The series capacitors 12 and 3 each have the same charge as their equivalent capacitor 123. Thus, capacitor 12 has charge
\[
q_{12}=q_{123}=44.6\ \mu\text{C}.
\]

From Eq. 25-1 and the equivalent capacitor \(C_{12}\), the potential difference across capacitor 12 must be
\[
V_{12}=\frac{q_{12}}{C_{12}}=\frac{44.6\ \mu\text{C}}{17.3\ \mu\text{F}}=2.58\ \text{V}.
\]

The parallel capacitors 1 and 2 each have the same potential difference as their equivalent capacitor 12. Thus, capacitor 1 has potential difference
\[
V_1=V_{12}=2.58\ \text{V},
\]
and, from Eq. 25-1 and Fig. 25-10i, the charge on capacitor 1 must be
\[
q_1=C_1V_1=(12.0\ \mu\text{F})(2.58\ \text{V})=31.0\ \mu\text{C}.
\]

As the electric potential across capacitor 1 decreases, that across capacitor 2 increases. Equilibrium is reached when the two potentials are equal because, with no potential difference between connected plates of the capacitors, there

## Answer
(a) \[
C_{123}=3.57\ \mu\text{F}
\]

(b) \[
q_1=31.0\ \mu\text{C}
\]

## Key concepts used
- Capacitors in parallel: \(C_{\rm eq}=C_1+C_2+\cdots\)
- Capacitors in series: \(\displaystyle \frac{1}{C_{\rm eq}}=\sum \frac{1}{C_j}\)
- Series capacitors have the same charge as their equivalent capacitor
- Parallel capacitors have the same potential difference as their equivalent capacitor
- \(q=CV\)
