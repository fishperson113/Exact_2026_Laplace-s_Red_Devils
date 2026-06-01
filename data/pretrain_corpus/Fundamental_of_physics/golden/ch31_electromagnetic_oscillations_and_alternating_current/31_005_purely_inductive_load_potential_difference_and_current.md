---
source: Fundamentals of Physics
chapter: 31
section: 31-3
sample_problem_number: 31.05
subtitle: Purely inductive load: potential difference and current
needs_review: true
---

# Sample Problem 31.05: Purely inductive load: potential difference and current

## Problem
In Fig. 31-12, inductance $L $ is $230\ \text{mH} $ and the sinusoidal alternating emf device operates at amplitude $\varepsilon_m = 36.0\ \text{V} $ and frequency $f_d = 60.0\ \text{Hz} $.

(a) What are the potential difference $v_L(t) $ across the inductance and the amplitude $V_L $ of $v_L(t) $?

(b) What are the current $i_L(t) $ in the circuit as a function of time and the amplitude $I_L $ of $i_L(t) $?

## Key ideas
In a circuit with a purely inductive load, the potential difference $v_L(t) $ across the inductance is always equal to the potential difference $\varepsilon(t) $ across the emf device.

## Solution
### (a) Potential difference across the inductance
For a purely inductive load,
$$ 
v_L(t)=\varepsilon(t)
 $$
and
$$ 
V_L=\varepsilon_m.
 $$
Since $\varepsilon_m=36.0\ \text{V} $,
$$ 
V_L=36.0\ \text{V}.
 $$

To find $v_L(t) $, use
$$ 
\varepsilon(t)=\varepsilon_m\sin \omega_d t,
 $$
so
$$ 
v_L(t)=\varepsilon(t)=\varepsilon_m\sin \omega_d t.
 $$
With $\varepsilon_m=36.0\ \text{V} $ and
$$ 
\omega_d=2\pi f_d=2\pi(60.0\ \text{Hz})=120\pi\ \text{rad/s},
 $$
we get
$$ 
v_L(t)=(36.0\ \text{V})\sin(120\pi t).
 $$

### (b) Current in the circuit
For a purely inductive circuit, the inductive reactance is
$$ 
X_L=\omega_d L.
 $$
With $L=230\ \text{mH}=0.230\ \text{H} $,
$$ 
X_L=(120\pi)(0.230)\approx 86.7\ \Omega.
 $$
Because the circuit is purely inductive, the impedance is
$$ 
Z=X_L=86.7\ \Omega.
 $$
Thus the current amplitude is
$$ 
I_L=\frac{\varepsilon_m}{Z}=\frac{36.0\ \text{V}}{86.7\ \Omega}=0.415\ \text{A}.
 $$

For a purely inductive load, current lags the emf by $90^\circ $, so the current is
$$ 
i_L(t)=I_L\sin(\omega_d t-\tfrac{\pi}{2}).
 $$
Substituting the values,
$$ 
i_L(t)=(0.415\ \text{A})\sin(120\pi t-\tfrac{\pi}{2}).
 $$

## Answer
$$ 
V_L=36.0\ \text{V}
 $$
$$ 
v_L(t)=(36.0\ \text{V})\sin(120\pi t)
 $$
$$ 
I_L=0.415\ \text{A}
 $$
$$ 
i_L(t)=(0.415\ \text{A})\sin(120\pi t-\tfrac{\pi}{2})
 $$

## Key concepts used
- Purely inductive load: $v_L(t)=\varepsilon(t) $
- Sinusoidal emf: $\varepsilon(t)=\varepsilon_m\sin \omega_d t $
- Driving angular frequency: $\omega_d=2\pi f_d $
- Inductive reactance: $X_L=\omega_d L $
- Purely inductive impedance: $Z=X_L $
- Current amplitude: $I=\varepsilon_m/Z $
- In a purely inductive circuit, current lags emf by $90^\circ $
