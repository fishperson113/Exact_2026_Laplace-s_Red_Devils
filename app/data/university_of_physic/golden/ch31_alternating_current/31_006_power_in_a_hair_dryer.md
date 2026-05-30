---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.4
example_number: 31.6
subtitle: Power in a hair dryer
needs_review: false
---

# Example 31.6: Power in a hair dryer

## Problem
An electric hair dryer is rated at 1500 W (the average power) at 120 V (the rms voltage). Calculate:

(a) the resistance  
(b) the rms current  
(c) the maximum instantaneous power

Assume that the dryer is a pure resistor. The heating element acts as a resistor.

## Setup
**IDENTIFY and SET UP:** We are given \(P_{\text{av}} = 1500\ \text{W}\) and \(V_{\text{rms}} = 120\ \text{V}\). Our target variables are the resistance \(R\), the rms current \(I_{\text{rms}}\), and the maximum value \(p_{\max}\) of the instantaneous power \(p\).

We solve Eq. (31.29) to find \(R\), Eq. (31.28) to find \(I_{\text{rms}}\) from \(P_{\text{av}}\) and \(V_{\text{rms}}\), and Eq. (31.30) to find \(p_{\max}\).

## Solution
**EXECUTE:**  
(a) From Eq. (31.29), the resistance is
\[
R=\frac{V_{\text{rms}}^{2}}{P_{\text{av}}}
=\frac{(120\ \text{V})^{2}}{1500\ \text{W}}
=9.6\ \Omega
\]

(b) From Eq. (31.28),
\[
I_{\text{rms}}=\frac{P_{\text{av}}}{V_{\text{rms}}}
=\frac{1500\ \text{W}}{120\ \text{V}}
=12.5\ \text{A}
\]

(c) For a pure resistor, the voltage and current are in phase and the phase angle \(\phi\) is zero. Hence from Eq. (31.30), the instantaneous power is
\[
p = VI\cos^2 \omega t
\]
and the maximum instantaneous power is
\[
p_{\max}=VI
\]
From Eq. (31.27), this is twice the average power \(P_{\text{av}}\), so
\[
p_{\max}=2P_{\text{av}}=2(1500\ \text{W})=3000\ \text{W}
\]

## Evaluation
We can confirm our result in part (b) by using Eq. (31.7):
\[
\frac{V_{\text{rms}}}{R}=\frac{120\ \text{V}}{9.6\ \Omega}=12.5\ \text{A}
\]

Note that some unscrupulous manufacturers of stereo amplifiers advertise the peak power output rather than the lower average value.

## Key concepts used
- Average power in a resistor: \(P_{\text{av}}=V_{\text{rms}} I_{\text{rms}}\)
- For a pure resistor: \(R=\dfrac{V_{\text{rms}}^2}{P_{\text{av}}}\)
- RMS current: \(I_{\text{rms}}=\dfrac{P_{\text{av}}}{V_{\text{rms}}}\)
- Maximum instantaneous power for a resistor: \(p_{\max}=VI=2P_{\text{av}}\)
