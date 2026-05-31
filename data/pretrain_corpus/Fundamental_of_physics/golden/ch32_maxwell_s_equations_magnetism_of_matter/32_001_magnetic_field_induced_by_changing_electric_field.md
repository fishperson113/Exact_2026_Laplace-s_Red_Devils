---
source: Fundamentals of Physics
chapter: 32
section: 32-2
sample_problem_number: 32.01
subtitle: Magnetic field induced by changing electric field
needs_review: false
---

# Sample Problem 32.01: Magnetic field induced by changing electric field

## Problem
A parallel-plate capacitor with circular plates of radius $R $ is being charged as in Fig. 32-5a.

(a) Derive an expression for the magnetic field at radius $r $ for the case $r < R $.

(b) Evaluate the field magnitude $B $ for $r = R/5 = 11.0\ \text{mm} $ and $\mathrm{d}E/\mathrm{d}t = 1.50 \times 10^{12}\ \text{V/m}\cdot\text{s} $.

(c) Derive an expression for the induced magnetic field for the case $r > R $.

## Key ideas
A magnetic field can be set up by a current and by induction due to a changing electric flux; both effects are included in Eq. 32-5. There is no current between the capacitor plates of Fig. 32-5, but the electric flux there is changing. Thus, Eq. 32-5 reduces to

$$ 
\oint \vec B \cdot d\vec s = \mu_0 \epsilon_0 \frac{\mathrm{d}\Phi_E}{\mathrm{d}t}.
 $$

We shall separately evaluate the left and right sides of this equation.

## Solution
### (a) Field for $r < R $

Left side of Eq. 32-6: We choose a circular Amperian loop with radius $r < R $ as shown in Fig. 32-5b because we want to evaluate the magnetic field for $r < R $, that is, inside the capacitor. The magnetic field at all points along the loop is tangent to the loop, as is the path element $d\vec s $. Thus, $\vec B $ and $d\vec s $ are either parallel or antiparallel at each point of the loop. For simplicity, assume they are parallel; the choice does not alter our outcome here. Then

$$ 
\oint \vec B \cdot d\vec s = \oint B\,ds = B \oint ds = B(2\pi r).
 $$

For the right side, the electric field exists only between the plates. For $r < R $, the area enclosed by the loop is $\pi r^2 $, so

$$ 
\Phi_E = EA = E(\pi r^2).
 $$

Thus,

$$ 
B(2\pi r) = \mu_0 \epsilon_0 \frac{\mathrm{d}}{\mathrm{d}t}(E\pi r^2).
 $$

Solving for $B $ gives, for $r < R $,

$$ 
B = \frac{1}{2}\mu_0 \epsilon_0 r \frac{\mathrm{d}E}{\mathrm{d}t}.
 $$

This equation tells us that, inside the capacitor, $B $ increases linearly with increased radial distance $r $, from 0 at the central axis to a maximum value at plate radius $R $.

### (b) Field magnitude at $r = R/5 = 11.0\ \text{mm} $

From the answer to (a), we have

$$ 
B = \frac{1}{2}\mu_0 \epsilon_0 r \frac{\mathrm{d}E}{\mathrm{d}t}.
 $$

Substituting the values,

$$ 
B = \frac{1}{2}(4\pi \times 10^{-7}\ \text{T}\cdot\text{m/A})(8.85 \times 10^{-12}\ \text{C}^2/\text{N}\cdot\text{m}^2)(11.0 \times 10^{-3}\ \text{m})(1.50 \times 10^{12}\ \text{V/m}\cdot\text{s})
 $$

$$ 
= 9.18 \times 10^{-8}\ \text{T}.
 $$

### (c) Field for $r > R $

Our procedure is the same as in (a) except we now use an Amperian loop with radius $r $ that is greater than the plate radius $R $, to evaluate $B $ outside the capacitor. Evaluating the left and right sides of Eq. 32-6 again leads to Eq. 32-7. However, we then need this subtle point: the electric field exists only between the plates, not outside the plates. Thus, the area $A $ that is encircled by the Amperian loop in the electric field is not the full area $\pi r^2 $ of the loop. Rather, $A $ is only the plate area $\pi R^2 $.

Substituting $\pi R^2 $ for $A $ in Eq. 32-7 and solving the result for $B $ give us, for $r > R $,

$$ 
B = \frac{\mu_0 \epsilon_0 R^2}{2r}\frac{\mathrm{d}E}{\mathrm{d}t}.
 $$

This equation tells us that, outside the capacitor, $B $ decreases with increased radial distance $r $, from a maximum value at the plate edges, where $r = R $. By substituting $r = R $ into Eqs. 32-8 and 32-9, you can show that these equations are consistent; that is, they give the same maximum value of $B $ at the plate radius.

The magnitude of the induced magnetic field calculated in (b) is so small that it can scarcely be measured with simple apparatus. This is in sharp contrast to the magnitudes of induced electric fields (Faraday’s law), which can be measured easily.

## Answer
For $r < R $:
$$ 
B = \frac{1}{2}\mu_0 \epsilon_0 r \frac{\mathrm{d}E}{\mathrm{d}t}.
 $$

For $r = R/5 = 11.0\ \text{mm} $ and $\mathrm{d}E/\mathrm{d}t = 1.50 \times 10^{12}\ \text{V/m}\cdot\text{s} $:
$$ 
B = 9.18 \times 10^{-8}\ \text{T}.
 $$

For $r > R $:
$$ 
B = \frac{\mu_0 \epsilon_0 R^2}{2r}\frac{\mathrm{d}E}{\mathrm{d}t}.
 $$

## Key concepts used
- Ampere-Maxwell law
- Magnetic field from changing electric flux
- Displacement current
- Circular Amperian loop symmetry
