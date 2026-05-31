---
source: Young and Freedman University Physics, 13th ed.
chapter: 27
section: 27.7
example_number: 27.8
subtitle: Magnetic force on a curved conductor
needs_review: true
---

# Example 27.8: Magnetic force on a curved conductor

## Problem
In Fig. 27.30 the magnetic field is uniform and perpendicular to the plane of the figure, pointing out of the page. The conductor, carrying current $I $ to the left, has three segments: (1) a straight segment with length $L $ perpendicular to the plane of the figure, (2) a semicircle with radius $R $, and (3) another straight segment with length $L $ parallel to the $x $-axis. Find the total magnetic force on this conductor.

## Setup
**IDENTIFY and SET UP:** The magnetic field $\mathbf{B} $ is uniform, so we find the forces $\mathbf{F}_1 $ and $\mathbf{F}_3 $ on the straight segments (1) and (3) using Eq. (27.19). We divide the curved segment (2) into infinitesimal straight segments and find the corresponding force $d\mathbf{F}_2 $ on each straight segment using Eq. (27.20). We then integrate to find $\mathbf{F}_2 $.

The total magnetic force on the conductor is then
$$ 
\mathbf{F}=\mathbf{F}_1+\mathbf{F}_2+\mathbf{F}_3.
 $$

## Solution
**EXECUTE:** For segment (1), $\mathbf{L}=L\,\hat{\mathbf{n}} $. Hence from Eq. (27.19),
$$ 
\mathbf{F}_1=I\mathbf{L}\times \mathbf{B}=0.
 $$

For segment (3), $\mathbf{L}=-L\,\hat{\mathbf{n}} $, so
$$ 
\mathbf{F}_3=I\mathbf{L}\times \mathbf{B}=ILB\,\hat{\mathbf{n}}.
 $$

For the curved segment (2), Fig. 27.20 shows a segment $d\mathbf{l} $ with length $dl=R\,du $ at angle $u $. The right-hand rule shows that the direction of $d\mathbf{l}\times \mathbf{B} $ is radially outward from the center; make sure you can verify this. Because $d\mathbf{l} $ and $\mathbf{B} $ are perpendicular, the magnitude $dF_2 $ of the force on the segment is just
$$ 
dF_2=I\,dl\,B=IRB\,du.
 $$
The components of the force on this segment are
$$ 
dF_{2x}=IRB\cos u\,du,\qquad dF_{2y}=IRB\sin u\,du.
 $$

To find the components of the total force, we integrate these expressions with respect to $u $ from $0 $ to $\pi $ to take in the whole semicircle. The results are
$$ 
F_{2x}=IRB\int_0^\pi \cos u\,du=0,
 $$
$$ 
F_{2y}=IRB\int_0^\pi \sin u\,du=2IRB.
 $$
Hence
$$ 
\mathbf{F}_2=2IRB\,\hat{\mathbf{n}}.
 $$

Finally, adding the forces on all three segments, we find that the total force is in the positive $y $-direction:
$$ 
\mathbf{F}=\mathbf{F}_1+\mathbf{F}_2+\mathbf{F}_3
=0+2IRB\,\hat{\mathbf{n}}+ILB\,\hat{\mathbf{n}}
=IB(2R+L)\,\hat{\mathbf{n}}.
 $$

## Evaluation
We could have predicted from symmetry that the $x $-component of $\mathbf{F}_2 $ would be zero: On the right half of the semicircle the $x $-component of the force is positive (to the right) and on the left half it is negative (to the left); the positive and negative contributions to the integral cancel.

The result is that $\mathbf{F}_2 $ is the force that would be exerted if we replaced the semicircle with a straight segment of length $2R $ along the $x $-axis. Do you see why?

## Key concepts used
- Magnetic force on a current-carrying wire segment: $\mathbf{F}=I\mathbf{L}\times \mathbf{B} $
- Force on a curved wire found by integration:
  $$ 
  d\mathbf{F}=I\,d\mathbf{l}\times \mathbf{B}
   $$
- Symmetry can be used to determine that one force component cancels
- Uniform magnetic field allows forces on separate segments to be added vectorially
