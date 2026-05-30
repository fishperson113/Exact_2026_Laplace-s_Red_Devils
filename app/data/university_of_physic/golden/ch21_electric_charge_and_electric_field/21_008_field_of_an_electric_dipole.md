---
source: Young and Freedman University Physics, 13th ed.
chapter: 21
section: 21.5
example_number: 21.8
subtitle: Field of an electric dipole
needs_review: true
---

# Example 21.8: Field of an electric dipole

## Problem
Point charges \(q_1\) and \(q_2\) are \(0.100\ \text{m}\) apart (Fig. 21.22). Such pairs of point charges with equal magnitude and opposite sign are called electric dipoles. Compute the electric field caused by \(q_1\), the field caused by \(q_2\), and the total field:

- (a) at point \(a\)
- (b) at point \(b\)
- (c) at point \(c\)

## Setup
We must find the total electric field at various points due to two point charges. We use the principle of superposition:

\[
\vec E = \vec E_1 + \vec E_2.
\]

Figure 21.22 shows the coordinate system and the locations of the field points \(a\), \(b\), and \(c\).

The charges are:
- \(q_1 = -12\ \text{nC}\)
- \(q_2 = +12\ \text{nC}\)

The magnitudes of the electric fields are found from

\[
E = \frac{1}{4\pi\varepsilon_0}\frac{|q|}{r^2}.
\]

## Solution
At each field point, \(\vec E\) depends on the magnitudes \(E_1\) and \(E_2\) and their directions there; we first calculate the magnitudes \(E_{1a}\), \(E_{2a}\), \(E_{1b}\), \(E_{2b}\), \(E_{1c}\), and \(E_{2c}\).

At point \(a\),

\[
E_{1a}=\frac{1}{4\pi\varepsilon_0}\frac{|q_1|}{r^2}
= (9.0\times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2)\frac{12\times10^{-9}\ \text{C}}{(0.060\ \text{m})^2}
= 3.0\times10^4\ \text{N/C}.
\]

We calculate the other field magnitudes in a similar way. The results are

\[
E_{2c}=E_{1c}=6.39\times10^3\ \text{N/C}
\]
\[
E_{2b}=0.55\times10^4\ \text{N/C}
\]
\[
E_{2a}=6.8\times10^4\ \text{N/C}
\]
\[
E_{1c}=6.39\times10^3\ \text{N/C}
\]
\[
E_{1b}=6.8\times10^4\ \text{N/C}
\]
\[
E_{1a}=3.0\times10^4\ \text{N/C}
\]

The directions of the corresponding fields are in all cases away from the positive charge \(q_2\) and toward the negative charge \(q_1\).

(a) At \(a\), \(\vec E_{1a}\) and \(\vec E_{2a}\) are both directed to the right, so

\[
\vec E_a = E_{1a}\,\hat{\mathbf i} + E_{2a}\,\hat{\mathbf i}
= (9.8\times10^4\ \text{N/C})\,\hat{\mathbf i}.
\]

(b) At \(b\), \(\vec E_{1b}\) is directed to the left and \(\vec E_{2b}\) is directed to the right, so

\[
\vec E_b = -E_{1b}\,\hat{\mathbf i} + E_{2b}\,\hat{\mathbf i}
= (-6.2\times10^4\ \text{N/C})\,\hat{\mathbf i}.
\]

(c) Figure 21.22 shows the directions of \(\vec E_{1c}\) and \(\vec E_{2c}\) at \(c\). Both vectors have the same \(x\)-component:

\[
E_{1cx}=E_{2cx}=E_{1c}\cos\alpha
= (6.39\times10^3\ \text{N/C})\left(\frac{5}{13}\right)
= 2.46\times10^3\ \text{N/C}.
\]

From symmetry, the \(y\)-components are equal and opposite, so their sum is zero. Hence

\[
\vec E_c = 2(2.46\times10^3\ \text{N/C})\,\hat{\mathbf i}
= (4.9\times10^3\ \text{N/C})\,\hat{\mathbf i}.
\]

## Evaluation
We can also find \(\vec E_c\) using Eq. (21.7) for the field of a point charge. The displacement vector from \(q_1\) to point \(c\) is

\[
\vec r_1 = r\cos\alpha\,\hat{\mathbf i} + r\sin\alpha\,\hat{\mathbf j}.
\]

Hence the unit vector that points from \(q_1\) to point \(c\) is

\[
\hat{\mathbf r}_1 = \cos\alpha\,\hat{\mathbf i} + \sin\alpha\,\hat{\mathbf j}.
\]

By symmetry, the unit vector that points from \(q_2\) to point \(c\) has the opposite \(x\)-component but the same \(y\)-component:

\[
\hat{\mathbf r}_2 = -\cos\alpha\,\hat{\mathbf i} + \sin\alpha\,\hat{\mathbf j}.
\]

We can now use Eq. (21.7) to write the fields \(\vec E_1\) and \(\vec E_2\) at \(c\) in vector form, then find their sum. Since \(q_2=-q_1\) and the distance \(r\) to \(c\) is the same for both charges,

\[
\vec E_c
= \vec E_{1c} + \vec E_{2c}
= \frac{1}{4\pi\varepsilon_0}\frac{q_1}{r^2}\hat{\mathbf r}_1
+ \frac{1}{4\pi\varepsilon_0}\frac{q_2}{r^2}\hat{\mathbf r}_2
\]

\[
= \frac{1}{4\pi\varepsilon_0 r^2}\left(q_1\hat{\mathbf r}_1 + q_2\hat{\mathbf r}_2\right)
= \frac{q_1}{4\pi\varepsilon_0 r^2}\left(\hat{\mathbf r}_1 - \hat{\mathbf r}_2\right).
\]

Substituting the unit vectors gives

\[
\hat{\mathbf r}_1 - \hat{\mathbf r}_2 = 2\cos\alpha\,\hat{\mathbf i},
\]

so

\[
\vec E_c = \frac{2q_1\cos\alpha}{4\pi\varepsilon_0 r^2}\,\hat{\mathbf i}.
\]

This is the same as we calculated in part (c).

## Key concepts used
- Electric-field superposition: \(\vec E = \vec E_1 + \vec E_2\)
- Field of a point charge: \(E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q|}{r^2}\)
- Vector addition of electric fields
- Symmetry arguments for canceling components in dipole fields
- Direction of electric fields: away from \(+\) charges and toward \(-\) charges
