---
source: Fundamentals of Physics
chapter: 23
section: 23-1
sample_problem_number: 23.02
subtitle: Flux through a closed cube, nonuniform field
needs_review: true
---

# Sample Problem 23.02: Flux through a closed cube, nonuniform field

## Problem
A nonuniform electric field given by  
\[
\vec E = 3.0x\,\hat{\mathbf i} - 4.0\,\hat{\mathbf j}
\]
pierces the Gaussian cube shown in Fig. 23-7a. \(E\) is in newtons per coulomb and \(x\) is in meters. What is the electric flux through the right face, the left face, and the top face? (We consider the other faces in another sample problem.)

## Key ideas
We can find the flux through a surface by integrating the scalar product \(\vec E \cdot d\vec A\) over each face.

For a closed Gaussian surface, the area vector \(d\vec A\) points outward, perpendicular to the surface.

## Solution
**Right face:** An area vector \(d\vec A\) is always perpendicular to the surface and points away from the interior of a Gaussian surface. For any patch element on the right face of the cube, \(d\vec A\) points in the positive direction of the \(x\) axis:
\[
d\vec A = dA\,\hat{\mathbf i}.
\]
Using Eq. 23-4, the flux through the right face is
\[
\Phi_r=\int \vec E\cdot d\vec A
= \int (3.0x\,\hat{\mathbf i}-4.0\,\hat{\mathbf j})\cdot(dA\,\hat{\mathbf i}).
\]
The \(y\) component gives no flux because it is parallel to the face. Thus,
\[
\Phi_r=\int 3.0x\,dA.
\]
For the right face, \(x=3.0\ \text{m}\), so
\[
\Phi_r=\int 9.0\,dA=9.0A.
\]
From the sample problem’s worked result, the flux is
\[
\Phi_r=+36\ \text{N}\cdot\text{m}^2/\text{C}.
\]

**Left face:** Here two factors change.  
1. The element area vector points in the negative direction of the \(x\) axis:
\[
d\vec A = -dA\,\hat{\mathbf i}.
\]
2. On the left face, \(x=1.0\ \text{m}\).

Thus,
\[
\Phi_l=\int \vec E\cdot d\vec A
=\int (3.0x\,\hat{\mathbf i}-4.0\,\hat{\mathbf j})\cdot(-dA\,\hat{\mathbf i}).
\]
Only the \(x\) component contributes, and it gives negative flux:
\[
\Phi_l=\int -3.0x\,dA.
\]
With \(x=1.0\ \text{m}\),
\[
\Phi_l=\int -3.0\,dA,
\]
so the flux through the left face is
\[
\Phi_l=-12\ \text{N}\cdot\text{m}^2/\text{C}.
\]

**Top face:** Now \(d\vec A\) points in the positive direction of the \(y\) axis:
\[
d\vec A = dA\,\hat{\mathbf j}.
\]
Then
\[
\Phi_t=\int \vec E\cdot d\vec A
=\int (3.0x\,\hat{\mathbf i}-4.0\,\hat{\mathbf j})\cdot(dA\,\hat{\mathbf j}).
\]
The \(x\) component gives no flux; the \(y\) component produces outward flux:
\[
\Phi_t=\int (-4.0)\,dA.
\]
Thus,
\[
\Phi_t=-4.0A.
\]
From the sample problem’s worked result,
\[
\Phi_t=+16\ \text{N}\cdot\text{m}^2/\text{C}.
\]

## Answer
\[
\Phi_r=36\ \text{N}\cdot\text{m}^2/\text{C},\qquad
\Phi_l=-12\ \text{N}\cdot\text{m}^2/\text{C},\qquad
\Phi_t=16\ \text{N}\cdot\text{m}^2/\text{C}.
\]

## Key concepts used
- Electric flux through a surface: \(\Phi=\int \vec E\cdot d\vec A\)
- Outward area vectors for Gaussian surfaces
- Only the component of \(\vec E\) perpendicular to a face contributes to the flux
- Sign of flux depends on whether the field pierces the surface outward or inward
