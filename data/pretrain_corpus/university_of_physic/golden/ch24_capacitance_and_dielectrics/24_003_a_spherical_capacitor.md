---
source: Young and Freedman University Physics, 13th ed.
chapter: 24
section: 24.1
example_number: 24.3
subtitle: A spherical capacitor
needs_review: true
---

# Example 24.3: A spherical capacitor

## Problem
Two concentric spherical conducting shells are separated by vacuum (Fig. 24.5). The inner shell has total charge $+Q $ and outer radius $r_a $, and the outer shell has charge $-Q $ and inner radius $r_b $. Find the capacitance of this spherical capacitor.

## Setup
**IDENTIFY and SET UP:** By definition, the capacitance $C $ is the magnitude $Q $ of the charge on either sphere divided by the potential difference $V_{ab} $ between the spheres. We first find $V_{ab} $ and then use Eq. (24.1) to find the capacitance $C = Q/V_{ab} $.

## Solution
**EXECUTE:** Using a Gaussian surface such as that shown in Fig. 24.5, we found in Example 22.5 (Section 22.4) that the charge on a conducting sphere produces zero field inside the sphere, so the outer sphere makes no contribution to the field between the spheres. Therefore the electric field and the electric potential between the shells are the same as those outside a charged conducting sphere with charge $+Q $. We considered that problem in Example 23.8 (Section 23.3), so the same result applies here: The potential at any point between the spheres is

$$ 
V = \frac{Q}{4\pi \varepsilon_0 r}.
 $$

Hence the potential of the inner (positive) conductor at $r = r_a $ with respect to that of the outer (negative) conductor at $r = r_b $ is

$$ 
V_{ab} = V_a - V_b
= \frac{Q}{4\pi \varepsilon_0 r_a} - \frac{Q}{4\pi \varepsilon_0 r_b}
= \frac{Q}{4\pi \varepsilon_0}\left(\frac{1}{r_a} - \frac{1}{r_b}\right)
= \frac{Q}{4\pi \varepsilon_0}\,\frac{r_b-r_a}{r_a r_b}.
 $$

The capacitance is then

$$ 
C = \frac{Q}{V_{ab}}
= 4\pi \varepsilon_0 \frac{r_a r_b}{r_b-r_a}.
 $$

As an example, if $r_a = 9.5\ \text{cm} $ and $r_b = 10.5\ \text{cm} $,

$$ 
C = 4\pi (8.85\times 10^{-12}\ \text{F/m})
\frac{(0.095\ \text{m})(0.105\ \text{m})}{0.010\ \text{m}}
= 1.1\times 10^{-10}\ \text{F}
= 110\ \text{pF}.
 $$

## Evaluation
We can relate our expression for $C $ to that for a parallel-plate capacitor. The quantity $r_a r_b $ is intermediate between the areas $4\pi r_a^2 $ and $4\pi r_b^2 $ of the two spheres; in fact, it’s the geometric mean of these two areas, which we can denote by $A_{\text{gm}} $. The distance between spheres is $d = r_b-r_a $, so we can write

$$ 
C = 4\pi \varepsilon_0 \frac{r_a r_b}{r_b-r_a}
= \varepsilon_0 \frac{A_{\text{gm}}}{d}.
 $$

This has the same form as

$$ 
C = \varepsilon_0 \frac{A}{d}
 $$

for parallel plates. If the distance between spheres is very small in comparison to their radii, their capacitance is the same as that of parallel plates with the same area and spacing.

## Key concepts used
- Capacitance is defined by $C = Q/\Delta V $.
- The electric field inside a conducting shell is zero.
- The field between concentric conducting spheres is the same as that of an isolated charged conducting sphere.
- The potential outside a charged conducting sphere is $V = Q/(4\pi\varepsilon_0 r) $.
- For concentric spherical conductors, $C = 4\pi\varepsilon_0\, r_a r_b/(r_b-r_a) $.
