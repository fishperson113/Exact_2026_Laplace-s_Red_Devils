---
source: Young and Freedman University Physics, 13th ed.
chapter: 31
section: 31.2
example_number: 31.2
subtitle: An inductor in an ac circuit
needs_review: true
---

# Example 31.2: An inductor in an ac circuit

## Problem
The current amplitude in a pure inductor in a radio receiver is to be 250 mA when the voltage amplitude is 3.60 V at a frequency of 1.60 MHz (at the upper end of the AM broadcast band).  
(a) What inductive reactance is needed? What inductance?  
(b) If the voltage amplitude is kept constant, what will be the current amplitude through this inductor at 16.0 MHz? At 160 kHz?

## Setup
IDENTIFY and SET UP: There may be other elements of this circuit, but in this example we don’t care: All they do is provide the inductor with an oscillating voltage, so the other elements are lumped into the ac source shown in Fig. 31.8a.

We are given the current amplitude and the voltage amplitude. Our target variables in part (a) are the inductive reactance at 1.60 MHz and the inductance, which we find using Eqs. (31.13) and (31.12). Knowing $L $, we use these equations in part (b) to find $X_L $ and $I $ at any frequency.

## Solution
EXECUTE: (a) From Eq. (31.13),
$$ 
X_L=\frac{V_L}{I}=\frac{3.60\ \text{V}}{250\times 10^{-6}\ \text{A}}=1.44\times 10^{4}\ \Omega=14.4\ \text{k}\Omega
 $$

From Eq. (31.12), with $v=2\pi f $,
$$ 
L=\frac{X_L}{2\pi f}=\frac{1.44\times 10^{4}\ \Omega}{2\pi (1.60\times 10^{6}\ \text{Hz})}=1.43\times 10^{-3}\ \text{H}=1.43\ \text{mH}
 $$

(b) Combining Eqs. (31.12) and (31.13), we find
$$ 
I=\frac{V_L}{X_L}=\frac{V_L}{vL}
 $$
Thus the current amplitude is inversely proportional to the frequency $f $. Since $I=250\ \text{mA} $ at $f=1.60\ \text{MHz} $, the current amplitudes at $16.0\ \text{MHz} $ and $160\ \text{kHz} $ will be, respectively, one-tenth as great and ten times as great.

## Evaluation
In general, the lower the frequency of an oscillating voltage applied across an inductor, the greater the amplitude of the resulting oscillating current.

## Key concepts used
- Inductive reactance: $X_L=vL=2\pi fL $
- Amplitude relation for an inductor: $V_L=IX_L $
- For fixed voltage amplitude, current amplitude in a pure inductor is inversely proportional to frequency
