---
source: Fundamentals of Physics
chapter: 30
section: 30-1
sample_problem_number: 30.03
subtitle: Induced emf due to a changing nonuniform B field
needs_review: true
---

# Sample Problem 30.03: Induced emf due to a changing nonuniform B field

## Problem
Figure 30-7 shows a rectangular loop of wire immersed in a nonuniform and varying magnetic field that is perpendicular to and directed into the page. The field’s magnitude is given by

$$ 
B = 4t^2x^2,
 $$

with $B $ in teslas, $t $ in seconds, and $x $ in meters. (Note that the function depends on both time and position.) The loop has width $W = 3.0\ \text{m} $ and height $H = 2.0\ \text{m} $. What are the magnitude and direction of the induced emf $\mathcal{E} $ around the loop at $t = 0.10\ \text{s} $?

## Key ideas
- Because the magnetic field is not uniform over the area enclosed by the loop, we cannot use $ \Phi_B = BA  $; we must integrate the magnetic flux.
- The field is perpendicular to the loop, so $ \vec B \cdot d\vec A = B\,dA  $.
- Use a thin vertical strip of area $dA = H\,dx $.
- Faraday’s law gives the induced emf:
  $$ 
  \mathcal{E} = -\frac{d\Phi_B}{dt}.
   $$
- The direction of the induced emf is found from Lenz’s law.

## Solution
In Fig. 30-7, $\vec B $ is perpendicular to the plane of the loop and thus parallel to the differential area vector $d\vec A $; so the dot product in Eq. 30-1 gives $B\,dA $.

Because the magnetic field varies with the coordinate $x $ but not with $y $, we can take the differential area $dA $ to be the area of a vertical strip of height $H $ and width $dx $, so

$$ 
dA = H\,dx.
 $$

Then the flux through the loop is

$$ 
\Phi_B = \int B\,dA = \int 4t^2x^2(H\,dx).
 $$

Treating $t $ as a constant for this integration and inserting the limits $x = 0 $ and $x = 3.0\ \text{m} $, we obtain

$$ 
\Phi_B = 4t^2H \int_0^{3.0} x^2\,dx
= 4t^2H \left(\frac{x^3}{3}\right)_0^{3.0}
= 72t^2,
 $$

where we have substituted $H = 2.0\ \text{m} $ and $\Phi_B $ is in webers.

Now we can use Faraday’s law to find the magnitude of $\mathcal{E} $ at any time $t $:

$$ 
\mathcal{E} = \left|\frac{d\Phi_B}{dt}\right|
= \frac{d(72t^2)}{dt}
= 144t.
 $$

At $t = 0.10\ \text{s} $,

$$ 
\mathcal{E} = (144\ \text{V/s})(0.10\ \text{s}) = 14\ \text{V}.
 $$

The flux of $\vec B $ through the loop is into the page in Fig. 30-7 and is increasing in magnitude because $B $ is increasing in magnitude with time. By Lenz’s law, the field $\vec B_{\text{ind}} $ of the induced current opposes this increase and so is directed out of the page. The curled-straight right-hand rule then tells us that the induced current is counterclockwise around the loop, and thus so is the induced emf $\mathcal{E} $.

## Answer
$$ 
\boxed{\mathcal{E} = 14\ \text{V}}
 $$

Direction: counterclockwise around the loop.

## Key concepts used
- Magnetic flux through a nonuniform field must be found by integration.
- Faraday’s law: $\mathcal{E} = -d\Phi_B/dt $.
- Lenz’s law determines the direction of the induced emf/current.
- Right-hand rule for the direction of induced current/emf.
