---
source: Fundamentals of Physics
chapter: 22
section: 22-4
sample_problem_number: 22.03
subtitle: Electric field of a charged circular rod
needs_review: true
---

# Sample Problem 22.03: Electric field of a charged circular rod

## Problem
A plastic rod of charge \(-Q\) is a circular section of radius \(r\) and central angle \(120^\circ\), symmetrically placed across an \(x\) axis with the origin at the center of curvature \(P\) of the rod. In terms of \(Q\) and \(r\), what is the electric field \(\vec E\) due to the rod at point \(P\)?

## Key ideas
Because the rod has a continuous charge distribution, we must find an expression for the electric fields due to differential elements of the rod and then sum those fields via calculus.

## Solution
An element: Consider a differential element having arc length \(ds\) and located at an angle \(u\) above the \(x\) axis. If we let \(l\) represent the linear charge density of the rod, our element \(ds\) has a differential charge of magnitude
\[
dq = l\,ds.
\]

The element’s field: Our element produces a differential electric field \(\mathrm{d}\vec E\) at point \(P\), which is a distance \(r\) from the element. Treating the element as a point charge, we can rewrite Eq. 22-3 to express the magnitude of \(\mathrm{d}\vec E\) as
\[
dE = \frac{1}{4\pi\varepsilon_0}\frac{dq}{r^2}
= \frac{1}{4\pi\varepsilon_0}\frac{l\,ds}{r^2}.
\]
The direction of \(\mathrm{d}\vec E\) is toward \(ds\) because charge \(dq\) is negative.

Symmetric partner: Our element has a symmetrically located (mirror image) element \(ds'\) in the bottom half of the rod. The electric field \(\mathrm{d}\vec E'\) set up at \(P\) by \(ds'\) also has the magnitude given by Eq. 22-19, but the field vector points toward \(ds'\). If we resolve the electric field vectors of \(ds\) and \(ds'\) into \(x\) and \(y\) components, their \(y\) components cancel because they have equal magnitudes and are in opposite directions. Their \(x\) components have equal magnitudes and are in the same direction.

Summing: Thus, to find the electric field set up by the rod, we need sum (via integration) only the \(x\) components of the differential electric fields set up by all the differential elements of the rod. From Fig. 22-13f and Eq. 22-19, we can write the component \(dE_x\) set up by \(ds\) as
\[
dE_x = dE\cos u
= \frac{1}{4\pi\varepsilon_0}\frac{l}{r^2}\cos u\,ds.
\]

Equation 22-20 has two variables, \(u\) and \(s\). Before we can integrate it, we must eliminate one variable. We do so by replacing \(ds\), using the relation
\[
ds = r\,du,
\]
in which \(du\) is the angle at \(P\) that includes arc length \(ds\). With this replacement, we can integrate Eq. 22-20 over the angle made by the rod at \(P\), from \(u=-60^\circ\) to \(u=60^\circ\); that will give us the field magnitude at \(P\):
\[
E=\int dE_x
=\int_{-60^\circ}^{60^\circ}\frac{1}{4\pi\varepsilon_0}\frac{l}{r^2}\cos u\, r\,du
=\frac{l}{4\pi\varepsilon_0 r}\int_{-60^\circ}^{60^\circ}\cos u\,du.
\]
\[
=\frac{l}{4\pi\varepsilon_0 r}\,[\sin u]_{-60^\circ}^{60^\circ}
=\frac{l}{4\pi\varepsilon_0 r}\,[\sin 60^\circ-\sin(-60^\circ)]
=\frac{l}{4\pi\varepsilon_0 r}(1.73).
\]

(If we had reversed the limits on the integration, we would have gotten the same result but with a minus sign. Since the integration gives only the magnitude of \(\vec E\), we would then have discarded the minus sign.)

Charge density: To evaluate \(l\), we note that the full rod subtends an angle of \(120^\circ\) and so is one-third of a full circle. Its arc length is then \(2\pi r/3\), and its linear charge density must be
\[
l=\frac{\text{charge}}{\text{length}}=\frac{Q}{2\pi r/3}=0.477\,\frac{Q}{r}.
\]

Substituting this into the expression for \(E\) and simplifying gives
\[
E=(1.73)(0.477)\frac{Q}{4\pi\varepsilon_0 r^2}
=0.83\,\frac{Q}{4\pi\varepsilon_0 r^2}.
\]

The direction of \(\vec E\) is toward the rod, along the axis of symmetry of the charge distribution. We can write \(\vec E\) in unit-vector notation as
\[
\vec E = 0.83\,\frac{Q}{4\pi\varepsilon_0 r^2}\,\hat{\mathbf i}.
\]

## Answer
\[
\boxed{\vec E = 0.83\,\frac{Q}{4\pi\varepsilon_0 r^2}\,\hat{\mathbf i}}
\]
The field points toward the rod, along the axis of symmetry.

## Key concepts used
- Continuous charge distributions require calculus.
- Treat a small arc element \(ds\) as carrying charge \(dq=l\,ds\).
- Use symmetry to cancel the \(y\) components of paired elements.
- Integrate only the adding components.
- For a circular arc centered at \(P\), use \(ds=r\,du\).
- Use the rod’s arc length to find the linear charge density \(l\).
