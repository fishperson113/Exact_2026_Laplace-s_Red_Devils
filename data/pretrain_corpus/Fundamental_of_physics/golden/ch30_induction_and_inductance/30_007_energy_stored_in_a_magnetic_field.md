---
source: Fundamentals of Physics
chapter: 30
section: 30-7
sample_problem_number: 30.07
subtitle: Energy stored in a magnetic field
needs_review: false
---

# Sample Problem 30.07: Energy stored in a magnetic field

## Problem
Consider a length $l $ near the middle of a long solenoid of cross-sectional area $A $ carrying current $i $; the volume associated with this length is $Al $. The energy $U_B $ stored by the length $l $ of the solenoid must lie entirely within this volume because the magnetic field outside such a solenoid is approximately zero. Moreover, the stored energy must be uniformly distributed within the solenoid because the magnetic field is (approximately) uniform everywhere inside.

Thus, the energy stored per unit volume of the field is

$$ 
u_B = \frac{U_B}{Al}.
 $$

Show that the magnetic energy density can be written as

$$ 
u_B = \frac{B^2}{2\mu_0}.
 $$

## Key ideas
- The energy stored in the magnetic field of a solenoid is
  $$ 
  U_B = \frac{1}{2}Li^2.
   $$
- The energy density is energy per unit volume:
  $$ 
  u_B = \frac{U_B}{Al}.
   $$
- Using the inductance of a long solenoid and $B=\mu_0 n i $, the magnetic energy density becomes
  $$ 
  u_B = \frac{B^2}{2\mu_0}.
   $$

## Solution
From the energy stored in an inductor,

$$ 
U_B = \frac{1}{2}Li^2.
 $$

Since this energy is contained in the volume $Al $, the energy density is

$$ 
u_B = \frac{U_B}{Al} = \frac{Li^2}{2Al}.
 $$

Using the inductance of a long solenoid, Eq. 30-31, we substitute for $L/l $ and find

$$ 
u_B = \frac{1}{2}\mu_0 n^2 i^2.
 $$

From Eq. 29-23, $B=\mu_0 n i $. Substituting $ni = B/\mu_0 $ into the previous result gives

$$ 
u_B = \frac{1}{2}\mu_0 \left(\frac{B}{\mu_0}\right)^2
     = \frac{B^2}{2\mu_0}.
 $$

This equation gives the density of stored energy at any point where the magnitude of the magnetic field is $B $. Even though it was derived by considering the special case of a solenoid, it holds for all magnetic fields, no matter how they are generated.

## Answer
$$ 
u_B = \frac{B^2}{2\mu_0}.
 $$

## Key concepts used
- Energy stored in an inductor
- Magnetic energy density
- Long-solenoid inductance
- Magnetic field of a solenoid: $B=\mu_0 n i $
