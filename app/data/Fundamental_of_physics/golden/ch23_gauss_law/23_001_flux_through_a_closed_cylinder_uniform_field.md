---
source: Fundamentals of Physics
chapter: 23
section: 23-1
sample_problem_number: 23.01
subtitle: Flux through a closed cylinder, uniform field
needs_review: true
---

# Sample Problem 23.01: Flux through a closed cylinder, uniform field

## Problem
Figure 23-6 shows a Gaussian surface in the form of a closed cylinder (a Gaussian cylinder or G-cylinder) of radius $R $. It lies in a uniform electric field $\vec E $ with the cylinder’s central axis (along the length of the cylinder) parallel to the field. What is the net flux $\Phi $ of the electric field through the cylinder?

## Key ideas
We can find the net flux $\Phi $ with Eq. 23-4 by integrating the dot product $\vec E \cdot d\vec A $ over the cylinder’s surface. However, we cannot write out functions so that we can do that with one integral. Instead, we need to be a bit clever: We break up the surface into sections with which we can actually evaluate an integral.

## Solution
Calculations: We break the integral of Eq. 23-4 into three terms: integrals over the left cylinder cap $a $, the curved cylindrical surface $b $, and the right cap $c $:

$$ 
\Phi = \int_a \vec E \cdot d\vec A + \int_b \vec E \cdot d\vec A + \int_c \vec E \cdot d\vec A .
 $$

Pick a patch element on the left cap. Its area vector $d\vec A $ must be perpendicular to the patch and pointing away from the interior of the cylinder. In Fig. 23-6, that means the angle between it and the field piercing the patch is $180^\circ $. Also, note that the electric field through the end cap is uniform and thus $\vec E $ can be pulled out of the integration.

We are about to integrate over the right face, but we note that $x $ has the same value everywhere on that face—namely, $x = 3.0\ \text{m} $. This means we can substitute that constant value for $x $. This can be a confusing argument. Although $x $ is certainly a variable as we move left to right across the figure, because the right face is perpendicular to the $x $ axis, every point on the face has the same $x $ coordinate. (The $y $ and $z $ coordinates do not matter in our integral.) Thus, we have

$$ 
\Phi_r = (9.0\ \text{N/C})(4.0\ \text{m}^2).
 $$

The integral merely gives us the area $A = 4.0\ \text{m}^2 $ of the right face, so

$$ 
\Phi_r = 36\ \text{N}\cdot \text{m}^2/\text{C}.
 $$

Left face: We repeat this procedure for the left face. However,

$$ 
\Phi_l = \int \vec E \cdot d\vec A = \int (3.0x\,\hat{\mathbf i} - 4.0\,\hat{\mathbf j}) \cdot (dA\,\hat{\mathbf i}).
 $$

Since on that face $x = 0 $, this becomes

$$ 
\Phi_l = \int (3.0\cdot 0)\, dA = 0.
 $$

The curved surface contributes no flux because its area vectors are perpendicular to the uniform field, so $\vec E \cdot d\vec A = 0 $ there.

Thus the net flux through the closed cylinder is the sum of the fluxes through the three parts:

$$ 
\Phi = \Phi_l + \Phi_b + \Phi_r = 0 + 0 + 36\ \text{N}\cdot \text{m}^2/\text{C}.
 $$

## Answer
$$ 
\Phi = 36\ \text{N}\cdot \text{m}^2/\text{C}
 $$

## Key concepts used
- Electric flux through a closed surface: $\Phi = \oint \vec E \cdot d\vec A $
- Decompose a closed surface into parts and sum the flux through each part
- For a uniform field, $\vec E $ can be taken outside the integral on a flat surface where it is constant
- On a surface where $\vec E $ is perpendicular to $d\vec A $, the flux is zero
