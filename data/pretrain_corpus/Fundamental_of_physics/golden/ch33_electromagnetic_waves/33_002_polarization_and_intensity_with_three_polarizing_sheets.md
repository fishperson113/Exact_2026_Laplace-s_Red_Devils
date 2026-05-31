---
source: Fundamentals of Physics
chapter: 33
section: 33-4
sample_problem_number: 33.02
subtitle: Polarization and intensity with three polarizing sheets
needs_review: false
---

# Sample Problem 33.02: Polarization and intensity with three polarizing sheets

## Problem
Figure 33-15a shows a system of three polarizing sheets in the path of initially unpolarized light. The polarizing direction of the first sheet is parallel to the y axis, that of the second sheet is at an angle of 60° counterclockwise from the y axis, and that of the third sheet is parallel to the x axis. What fraction of the initial intensity $I_0 $ of the light emerges from the three-sheet system, and in which direction is that emerging light polarized?

## Key ideas
1. We work through the system sheet by sheet, from the first one encountered by the light to the last one.
2. To find the intensity transmitted by any sheet, we apply either the one-half rule or the cosine-squared rule, depending on whether the light reaching the sheet is unpolarized or already polarized.
3. The light that is transmitted by a polarizing sheet is always polarized parallel to the polarizing direction of the sheet.

## Solution
First sheet: Because the light is initially unpolarized, the intensity $I_1 $ of the light transmitted by the first sheet is given by the one-half rule:
$$ 
I_1 = \frac{1}{2} I_0.
 $$

Because the polarizing direction of the first sheet is parallel to the y axis, the polarization of the light transmitted by it is also parallel to the y axis.

Second sheet: Because the light reaching the second sheet is polarized, the intensity $I_2 $ of the light transmitted by that sheet is given by the cosine-squared rule. The angle $u $ in the rule is the angle between the polarization direction of the entering light (parallel to the y axis) and the polarizing direction of the second sheet (60° counterclockwise from the y axis), so $u = 60^\circ $. Thus,
$$ 
I_2 = I_1 \cos^2 60^\circ.
 $$

The polarization of this transmitted light is parallel to the polarizing direction of the sheet transmitting it, that is, 60° counterclockwise from the y axis.

Third sheet: Because the light reaching the third sheet is polarized, the intensity $I_3 $ of the light transmitted by that sheet is given by the cosine-squared rule. The angle $u $ is now the angle between the polarization direction of the entering light and the polarizing direction of the third sheet (parallel to the x axis), so $u = 30^\circ $. Thus,
$$ 
I_3 = I_2 \cos^2 30^\circ.
 $$

This final transmitted light is polarized parallel to the x axis.

Substituting for $I_2 $ and then for $I_1 $,
$$ 
I_3 = (I_1 \cos^2 60^\circ)\cos^2 30^\circ
     = \left(\frac{1}{2} I_0\right)\cos^2 60^\circ \cos^2 30^\circ.
 $$

Therefore,
$$ 
\frac{I_3}{I_0} = 0.094.
 $$

## Answer
$$ 
\boxed{\frac{I_3}{I_0} = 0.094}
 $$
So $9.4\% $ of the initial intensity emerges, and the emerging light is polarized parallel to the x axis.

## Key concepts used
- Unpolarized light transmitted by a polarizing sheet loses half its intensity.
- Polarized light transmitted by a polarizing sheet follows Malus’s law:
  $$ 
  I_{\text{emerge}} = I_{\text{incident}} \cos^2 u
   $$
  where $u $ is the angle between the light’s polarization direction and the sheet’s transmission axis.
- The transmitted light is polarized parallel to the sheet’s polarizing direction.
