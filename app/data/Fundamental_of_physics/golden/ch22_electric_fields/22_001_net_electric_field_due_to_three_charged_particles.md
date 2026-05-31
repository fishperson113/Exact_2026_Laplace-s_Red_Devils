---
source: Fundamentals of Physics
chapter: 22
section: 22-2
sample_problem_number: 22.01
subtitle: Net electric field due to three charged particles
needs_review: true
---

# Sample Problem 22.01: Net electric field due to three charged particles

## Problem
Figure 22-7a shows three particles with charges \(q_1 = +2Q\), \(q_2 = -2Q\), and \(q_3 = -4Q\), each a distance \(d\) from the origin. What net electric field is produced at the origin?

## Key ideas
- Charges \(q_1\), \(q_2\), and \(q_3\) produce electric field vectors \(\vec E_1\), \(\vec E_2\), and \(\vec E_3\), respectively, at the origin, and the net electric field is the vector sum
  \[
  \vec E = \vec E_1 + \vec E_2 + \vec E_3.
  \]
- To find this sum, we first must find the magnitudes and orientations of the three field vectors.
- Electric fields obey the principle of superposition.

## Solution
Magnitudes and directions: To find the magnitude of \(\vec E_1\), which is due to \(q_1\), we use Eq. 22-3, substituting \(d\) for \(r\) and \(2Q\) for \(q\), obtaining
\[
E_1=\frac{1}{4\pi\varepsilon_0}\frac{2Q}{d^2}.
\]
Similarly, we find the magnitudes of \(\vec E_2\) and \(\vec E_3\) to be
\[
E_2=\frac{1}{4\pi\varepsilon_0}\frac{2Q}{d^2}
\quad \text{and} \quad
E_3=\frac{1}{4\pi\varepsilon_0}\frac{4Q}{d^2}.
\]

We next must find the orientations of the three electric field vectors at the origin. Because \(q_1\) is a positive charge, the field vector it produces points directly away from it, and because \(q_2\) and \(q_3\) are both negative, the field vectors they produce point directly toward each of them. Thus, the three electric fields produced at the origin by the three charged particles are oriented as in Fig. 22-7b.

Adding the fields: We can now add the fields vectorially just as we added force vectors in Chapter 21. However, here we can use symmetry to simplify the procedure. From Fig. 22-7b, we see that electric fields \(\vec E_1\) and \(\vec E_2\) have the same direction. Hence, their vector sum has that direction and has the magnitude
\[
E_1+E_2
=
\frac{1}{4\pi\varepsilon_0}\frac{2Q}{d^2}
+
\frac{1}{4\pi\varepsilon_0}\frac{2Q}{d^2}
=
\frac{1}{4\pi\varepsilon_0}\frac{4Q}{d^2},
\]
which happens to equal the magnitude of field \(\vec E_3\).

We must now combine two vectors, \(\vec E_1+\vec E_2\) and the vector sum \(\vec E_3\), that have the same magnitude and that are oriented symmetrically about the \(x\) axis, as shown in Fig. 22-7c. From the symmetry of Fig. 22-7c, we realize that the equal \(y\) components of our two vectors cancel (one is upward and the other is downward) and the equal \(x\) components add (both are rightward). Thus, the net electric field \(\vec E\) at the origin is in the positive direction of the \(x\) axis and has the magnitude
\[
E = 2E_{3x} = 2E_3\cos 30^\circ
=2\left(\frac{1}{4\pi\varepsilon_0}\frac{4Q}{d^2}\right)(0.866)
= \frac{6.93\,Q}{4\pi\varepsilon_0 d^2}.
\]

## Answer
\[
\boxed{\vec E \text{ is in the } +x \text{ direction, with magnitude } E=\frac{6.93\,Q}{4\pi\varepsilon_0 d^2}.}
\]

## Key concepts used
- Electric field due to a point charge
- Superposition of electric fields
- Vector addition of fields
- Symmetry of electric field components
