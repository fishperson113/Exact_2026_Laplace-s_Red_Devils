---
source: Fundamentals of Physics
chapter: 31
section: 31-3
sample_problem_number: 31.04
subtitle: Purely capacitive load: potential difference and current
needs_review: true
---

# Sample Problem 31.04: Purely capacitive load: potential difference and current

## Problem
In Fig. 31-10, capacitance \(C\) is 15.0 mF and the sinusoidal alternating emf device operates at amplitude \(\mathcal{E}_m = 36.0\ \text{V}\) and frequency \(f_d = 60.0\ \text{Hz}\).

(a) What are the potential difference \(v_C(t)\) across the capacitance and the amplitude \(V_C\) of \(v_C(t)\)?

(b) What are the current \(i_C(t)\) in the circuit as a function of time and the amplitude \(I_C\) of \(i_C(t)\)?

## Key ideas
In a circuit with a purely capacitive load, the potential difference \(v_C(t)\) across the capacitance is always equal to the potential difference \(\mathcal{E}(t)\) across the emf device.

In a purely capacitive ac circuit, the current leads the potential difference by \(90^\circ\).

## Solution
### (a) Potential difference across the capacitance
We have
\[
v_C(t)=\mathcal{E}(t)
\]
and
\[
V_C=\mathcal{E}_m.
\]
Since \(\mathcal{E}_m\) is given,
\[
V_C = \mathcal{E}_m = 36.0\ \text{V}.
\]

To find \(v_C(t)\), we use Eq. 31-28:
\[
v_C(t)=\mathcal{E}(t)=\mathcal{E}_m \sin \omega_d t.
\]
With
\[
\omega_d = 2\pi f_d = 2\pi(60.0\ \text{Hz}) = 120\pi\ \text{rad/s},
\]
we get
\[
v_C(t)=(36.0\ \text{V})\sin(120\pi t).
\]

### (b) Current in the circuit
For a purely capacitive load, the current leads the potential difference by \(90^\circ\). Thus, with phase constant \(-90^\circ\),
\[
i_C(t)=I_C \sin(\omega_d t + \pi/2).
\]

To find the amplitude \(I_C\), use the capacitive reactance relation
\[
V_C = I_C X_C,
\]
where
\[
X_C = \frac{1}{\omega_d C}.
\]
Then
\[
I_C = \frac{V_C}{X_C} = V_C \omega_d C.
\]

The source text appears to omit the numerical substitution for \(C\) in the OCR, so the current amplitude cannot be reliably completed from the provided excerpt alone. The functional form, however, is determined by the phase relation above.

## Answer
\[
V_C = 36.0\ \text{V}
\]

\[
v_C(t)=(36.0\ \text{V})\sin(120\pi t)
\]

For the current,
\[
i_C(t)=I_C\sin(\omega_d t+\pi/2)
\]
with \(I_C = V_C/X_C\) and \(X_C=1/(\omega_d C)\).

## Key concepts used
- In a purely capacitive ac circuit, \(v_C(t)=\mathcal{E}(t)\).
- The current in a capacitor leads the voltage by \(90^\circ\).
- Angular frequency: \(\omega_d=2\pi f_d\).
- Capacitive reactance: \(X_C=1/(\omega_d C)\).
- Amplitude relation: \(V_C=I_C X_C\).
