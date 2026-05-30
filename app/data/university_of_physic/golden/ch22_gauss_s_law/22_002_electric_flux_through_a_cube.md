---
source: Young and Freedman University Physics, 13th ed.
chapter: 22
section: 22.2
example_number: 22.2
subtitle: Electric flux through a cube
needs_review: true
---

# Example 22.2: Electric flux through a cube

## Problem
An imaginary cubical surface of side \(L\) is in a region of uniform electric field \(\vec E\). Find the electric flux through each face of the cube and the total flux through the cube when:

(a) it is oriented with two of its faces perpendicular to \(\vec E\) (Fig. 22.8a), and  
(b) the cube is turned by an angle \(\theta\) about a vertical axis (Fig. 22.8b).

## Setup
**IDENTIFY and SET UP:** Since \(\vec E\) is uniform and each of the six faces of the cube is flat, we find the flux \(\Phi_E\) through each face using Eqs. (22.3) and (22.4). The total flux through the cube is the sum of the six individual fluxes.

For a flat surface, the flux is
\[
\Phi_E = \vec E \cdot \vec A = EA\cos\phi
\]
where \(\vec A\) points outward from the closed surface and \(\phi\) is the angle between \(\vec E\) and the outward normal.

## Solution
**EXECUTE:**

### (a) Cube oriented with two faces perpendicular to \(\vec E\)
Figure 22.8a shows the outward unit vectors \(\hat n_1, \hat n_2, \dots, \hat n_6\) for each face; each unit vector points outward from the cube’s closed surface.

The angle between \(\vec E\) and \(\hat n_1\) is \(180^\circ\), the angle between \(\vec E\) and \(\hat n_2\) is \(0^\circ\), and the angle between \(\vec E\) and each of the other four unit vectors is \(90^\circ\).

Each face of the cube has area \(L^2\), so the fluxes through the faces are
\[
\Phi_{E1} = \vec E \cdot \hat n_1 A = EL^2\cos 180^\circ = -EL^2
\]
\[
\Phi_{E2} = \vec E \cdot \hat n_2 A = EL^2\cos 0^\circ = +EL^2
\]
\[
\Phi_{E3} = \Phi_{E4} = \Phi_{E5} = \Phi_{E6} = EL^2\cos 90^\circ = 0
\]

The flux is negative on face 1, where \(\vec E\) is directed into the cube, and positive on face 2, where \(\vec E\) is directed out of the cube. The total flux through the cube is
\[
\Phi_E = \Phi_{E1} + \Phi_{E2} + \Phi_{E3} + \Phi_{E4} + \Phi_{E5} + \Phi_{E6}
\]
\[
\Phi_E = -EL^2 + EL^2 + 0 + 0 + 0 + 0 = 0
\]

### (b) Cube turned by an angle \(\theta\) about a vertical axis
The field \(\vec E\) is directed into faces 1 and 3, so the fluxes through them are negative; \(\vec E\) is directed out of faces 2 and 4, so the fluxes through them are positive. We find
\[
\Phi_{E1} = \vec E \cdot \hat n_1 A = EL^2\cos(180^\circ-\theta) = -EL^2\cos\theta
\]
\[
\Phi_{E2} = \vec E \cdot \hat n_2 A = +EL^2\cos\theta
\]
\[
\Phi_{E3} = \vec E \cdot \hat n_3 A = EL^2\cos(180^\circ+\theta) = -EL^2\sin\theta
\]
\[
\Phi_{E4} = \vec E \cdot \hat n_4 A = EL^2\cos(180^\circ-\theta) = +EL^2\sin\theta
\]
\[
\Phi_{E5} = \Phi_{E6} = EL^2\cos 90^\circ = 0
\]

The total flux \(\Phi_E\) through the surface of the cube is again zero:
\[
\Phi_E = \Phi_{E1} + \Phi_{E2} + \Phi_{E3} + \Phi_{E4} + \Phi_{E5} + \Phi_{E6} = 0
\]

## Evaluation
We came to the same conclusion in our discussion of Fig. 22.3c: There is zero net flux of a uniform electric field through a closed surface that contains no electric charge.

## Key concepts used
- Electric flux through a flat surface: \(\Phi_E = \vec E \cdot \vec A = EA\cos\phi\)
- Outward normals for a closed surface
- Flux is positive where \(\vec E\) points out of the surface and negative where it points inward
- The net flux through a closed surface in a uniform field is zero when no charge is enclosed
