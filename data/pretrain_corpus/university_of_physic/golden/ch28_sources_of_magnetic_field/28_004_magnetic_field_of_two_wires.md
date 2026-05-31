---
source: Young and Freedman University Physics, 13th ed.
chapter: 28
section: 28.3
example_number: 28.4
subtitle: Magnetic field of two wires
needs_review: true
---

# Example 28.4: Magnetic field of two wires

## Problem
Figure 28.7a is an end-on view of two long, straight, parallel wires perpendicular to the $xy$-plane, each carrying a current $I$ but in opposite directions.

(a) Find the magnetic field at points $P_1$, $P_2$, and $P_3$.

(b) Find an expression for the magnetic field at any point on the $x$-axis to the right of wire 2.

## Setup
We can find the magnetic fields $\vec B_1$ and $\vec B_2$ due to wires 1 and 2 at each point using the ideas of this section. By the superposition principle, the magnetic field at each point is then

$$ 
\vec B_{\text{total}}=\vec B_1+\vec B_2.
 $$

We use Eq. (28.9) to find the magnitudes of these fields and the right-hand rule to find the corresponding directions. Figure 28.7a shows $\vec B_1$ and $\vec B_2$ at each point; you should confirm that the directions and relative magnitudes shown are correct.

## Solution
### (a)
Since point $P_1$ is a distance $2d$ from wire 1 and a distance $4d$ from wire 2,

$$ 
B_1=\frac{\mu_0 I}{2\pi(2d)}=\frac{\mu_0 I}{4\pi d},
\qquad
B_2=\frac{\mu_0 I}{2\pi(4d)}=\frac{\mu_0 I}{8\pi d}.
 $$

The right-hand rule shows that $\vec B_2$ is in the negative $y$-direction and $\vec B_1$ is in the positive $y$-direction, so

$$ 
\vec B_{\text{total}}=\vec B_1+\vec B_2
= -\frac{\mu_0 I}{4\pi d}\,\hat{\mathbf j}
+\frac{\mu_0 I}{8\pi d}\,\hat{\mathbf j}
= -\frac{\mu_0 I}{8\pi d}\,\hat{\mathbf j}
\qquad (\text{point } P_1).
 $$

At point $P_2$, a distance $d$ from both wires,

$$ 
B_1=B_2=\frac{\mu_0 I}{2\pi d}.
 $$

Both $\vec B_1$ and $\vec B_2$ are in the positive $y$-direction, and both have the same magnitude. Hence

$$ 
\vec B_{\text{total}}=\vec B_1+\vec B_2
=\frac{\mu_0 I}{2\pi d}\,\hat{\mathbf j}
+\frac{\mu_0 I}{2\pi d}\,\hat{\mathbf j}
=\frac{\mu_0 I}{\pi d}\,\hat{\mathbf j}
\qquad (\text{point } P_2).
 $$

Finally, at point $P_3$ the right-hand rule shows that $\vec B_2$ is in the positive $y$-direction and $\vec B_1$ is in the negative $y$-direction. This point is a distance $3d$ from wire 1 and a distance $d$ from wire 2, so

$$ 
B_1=\frac{\mu_0 I}{2\pi(3d)}=\frac{\mu_0 I}{6\pi d},
\qquad
B_2=\frac{\mu_0 I}{2\pi d}.
 $$

The total field at $P_3$ is

$$ 
\vec B_{\text{total}}=\vec B_1+\vec B_2
= -\frac{\mu_0 I}{6\pi d}\,\hat{\mathbf j}
+\frac{\mu_0 I}{2\pi d}\,\hat{\mathbf j}
=\frac{\mu_0 I}{3\pi d}\,\hat{\mathbf j}
\qquad (\text{point } P_3).
 $$

The same technique can be used to find $\vec B_{\text{total}}$ at any point; for points off the $x$-axis, caution must be taken in vector addition, since $\vec B_1$ and $\vec B_2$ need no longer be simply parallel or antiparallel.

### (b)
At any point on the $x$-axis to the right of wire 2, that is, for $x>d$, $\vec B_1$ and $\vec B_2$ are in the same directions as at $P_3$. Such a point is a distance $x+d$ from wire 1 and a distance $x-d$ from wire 2, so the total field is

$$ 
\vec B_{\text{total}}=\vec B_1+\vec B_2
=
\frac{\mu_0 I}{2\pi(x+d)}\,\hat{\mathbf j}
-
\frac{\mu_0 I}{2\pi(x-d)}\,\hat{\mathbf j}.
 $$

Combining the two terms using a common denominator gives

$$ 
\vec B_{\text{total}}
=
-\frac{\mu_0 I d}{\pi(x^2-d^2)}\,\hat{\mathbf j}.
 $$

## Evaluation
Consider the result from part (b) at a point very far from the wires, so that $x$ is much larger than $d$. Then the $d^2$ term in the denominator can be neglected, and the magnitude of the total field is approximately

$$ 
B_{\text{total}} \approx \frac{\mu_0 I d}{\pi x^2}.
 $$

For a single wire, Eq. (28.9) shows that the magnetic field decreases with distance in proportion to $1/x$; for two wires carrying opposite currents, $\vec B_1$ and $\vec B_2$ partially cancel each other, and so $B_{\text{total}}$ decreases more rapidly, in proportion to $1/x^2$.

This effect is used in communication systems such as telephone or computer networks. The wiring is arranged so that a conductor carrying a signal in one direction and the conductor carrying the return signal are side by side, as in Fig. 28.7a, or twisted around each other. As a result, the magnetic field due to these signals outside the conductors is very small, making it less likely to exert unwanted forces on other information-carrying currents.

## Key concepts used
- Magnetic field of a long, straight current-carrying wire:  
  $$ 
  B=\frac{\mu_0 I}{2\pi r}
   $$
- Right-hand rule for the direction of $\vec B$
- Superposition principle for magnetic fields
- Vector addition of fields
- Cancellation of fields from opposite currents
- Far-field behavior of a wire pair with opposite currents, leading to a $1/x^2$ dependence
