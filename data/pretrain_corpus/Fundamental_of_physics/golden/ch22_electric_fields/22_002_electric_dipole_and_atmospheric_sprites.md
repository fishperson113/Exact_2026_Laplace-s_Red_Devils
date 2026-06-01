---
source: Fundamentals of Physics
chapter: 22
section: 22-3
sample_problem_number: 22.02
subtitle: Electric dipole and atmospheric sprites
needs_review: true
---

# Sample Problem 22.02: Electric dipole and atmospheric sprites

## Problem
Sprites (Fig. 22-10a) are huge flashes that occur far above a large thunderstorm. They are believed to be produced when especially powerful lightning occurs between the ground and storm clouds, particularly when the lightning transfers a huge amount of negative charge $-q $ from the ground to the base of the clouds (Fig. 22-10b).

Just after such a transfer, the ground has a complicated distribution of positive charge. However, we can model the electric field due to the charges in the clouds and the ground by assuming a vertical electric dipole that has charge $+q $ at cloud height $h $ and charge $-q $ at below-ground depth $h $ (Fig. 22-10c).

If $q = 200\ \text{C} $ and $h = 6.0\ \text{km} $, what is the magnitude of the dipole’s electric field at altitude $z_1 = 30\ \text{km} $ somewhat above the clouds and altitude $z_2 = 60\ \text{km} $ somewhat above the stratosphere?

## Key ideas
- If an electric field exceeds a certain critical value $E_c $, it can pull electrons out of atoms and cause light emission.
- The value of $E_c $ depends on the density of the air.
- At altitude $z_2 = 60\ \text{km} $, the air density is low enough that the field exceeds $E_c $, so sprites can form.
- At altitude $z_1 = 30\ \text{km} $, the air density is higher and the field does not exceed $E_c $, so no light is emitted.

## Solution
For a point on the axis of a dipole, we use the dipole-field expression for a point located a distance $z $ above the dipole center:

$$ 
E = \frac{1}{4\pi\varepsilon_0}\,\frac{2q h}{z^3}
 $$

However, in this problem the dipole is modeled as charges $+q $ at $z=+h $ and $-q $ at $z=-h $, so the field at altitude $z $ above the ground is found from the difference of the fields from the two charges. The result is

$$ 
E = \frac{1}{4\pi\varepsilon_0}\left(\frac{q}{(z-h)^2} - \frac{q}{(z+h)^2}\right)
 $$

For $z \gg h $, this reduces to the dipole approximation

$$ 
E \approx \frac{1}{4\pi\varepsilon_0}\,\frac{4qh}{z^3}
 $$

Using $q=200\ \text{C} $, $h=6.0\times 10^3\ \text{m} $, and $1/(4\pi\varepsilon_0)=8.99\times10^9\ \text{N}\cdot\text{m}^2/\text{C}^2 $:

### At $z_1 = 30\ \text{km} $
$$ 
E_1 \approx (8.99\times10^9)\frac{4(200)(6.0\times10^3)}{(3.0\times10^4)^3}
 $$

$$ 
E_1 \approx 1.6\times10^3\ \text{N/C}
 $$

### At $z_2 = 60\ \text{km} $
$$ 
E_2 \approx (8.99\times10^9)\frac{4(200)(6.0\times10^3)}{(6.0\times10^4)^3}
 $$

$$ 
E_2 \approx 2.0\times10^2\ \text{N/C}
 $$

Thus the field is much stronger at 30 km than at 60 km. The 60 km field is large enough, in the thin air there, to exceed the critical field for light emission, while the 30 km field is not.

## Answer
$$ 
E(z_1=30\ \text{km}) \approx 1.6\times10^3\ \text{N/C}
 $$

$$ 
E(z_2=60\ \text{km}) \approx 2.0\times10^2\ \text{N/C}
 $$

## Key concepts used
- Electric dipole approximation on the axis
- Superposition of electric fields
- Field magnitude decreases as $1/z^3 $ far from the dipole
- Atmospheric breakdown depends on air density
