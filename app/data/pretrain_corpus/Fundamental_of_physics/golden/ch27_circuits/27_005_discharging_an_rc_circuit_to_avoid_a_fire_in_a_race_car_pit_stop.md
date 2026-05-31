---
source: Fundamentals of Physics
chapter: 27
section: 27-4
sample_problem_number: 27.05
subtitle: Discharging an RC circuit to avoid a fire in a race car pit stop
needs_review: true
---

# Sample Problem 27.05: Discharging an RC circuit to avoid a fire in a race car pit stop

## Problem
As a car rolls along pavement, electrons move from the pavement first onto the tires and then onto the car body. The car stores this excess charge and the associated electric potential energy as if the car body were one plate of a capacitor and the pavement were the other plate (Fig. 27-17a). When the car stops, it discharges its excess charge and energy through the tires, just as a capacitor can discharge through a resistor. If a conducting object comes within a few centimeters of the car before the car is discharged, the remaining energy can be suddenly transferred to a spark between the car and the object. Suppose the conducting object is a fuel dispenser. The spark will not ignite the fuel and cause a fire if the spark energy is less than the critical value $U_{\text{fire}} = 50\ \text{mJ} $.

When the car of Fig. 27-17a stops at time $t = 0 $, the car-ground potential difference is $V_0 = 30\ \text{kV} $. The car-ground capacitance is $C = 500\ \text{pF} $, and the resistance of each tire is $R_{\text{tire}} = 100\ \text{G}\Omega $. How much time does the car take to discharge through the tires to drop below the critical value $U_{\text{fire}} $?

## Key ideas
1. At any time $t $, a capacitor’s stored electric potential energy $U $ is related to its stored charge $q $ according to
   $$ 
   U = \frac{q^2}{2C}.
    $$
2. While a capacitor is discharging, the charge decreases with time according to
   $$ 
   q = q_0 e^{-t/RC}.
    $$

## Solution
We can treat the tires as resistors that are connected to one another at their tops via the car body and at their bottoms via the pavement. Figure 27-17b shows how the four resistors are connected in parallel across the car’s capacitance, and Fig. 27-17c shows their equivalent resistance $R $. From Eq. 27-24, $R $ is given by

$$ 
\frac{1}{R} = \frac{1}{R_{\text{tire}}} + \frac{1}{R_{\text{tire}}} + \frac{1}{R_{\text{tire}}} + \frac{1}{R_{\text{tire}}},
 $$
or
$$ 
R = \frac{R_{\text{tire}}}{4} = \frac{100 \times 10^9\ \Omega}{4} = 25 \times 10^9\ \Omega.
 $$

When the car stops, it discharges its excess charge and energy through $R $. We now use our two Key Ideas to analyze the discharge. Substituting $q = q_0 e^{-t/RC} $ into $U = q^2/2C $ gives

$$ 
U = \frac{q_0^2}{2C} e^{-2t/RC}.
 $$

From Eq. 25-1 ($q = CV $), we can relate the initial charge $q_0 $ on the car to the given initial potential difference $V_0 $:
$$ 
q_0 = CV_0.
 $$
Substituting this into the previous result yields
$$ 
U = \frac{(CV_0)^2}{2C} e^{-2t/RC}
= \frac{CV_0^2}{2} e^{-2t/RC}.
 $$

We set $U = U_{\text{fire}} $:
$$ 
U_{\text{fire}} = \frac{CV_0^2}{2} e^{-2t/RC}.
 $$
Thus,
$$ 
e^{-2t/RC} = \frac{2U_{\text{fire}}}{CV_0^2}.
 $$
Taking natural logarithms,
$$ 
-\frac{2t}{RC} = \ln\!\left(\frac{2U_{\text{fire}}}{CV_0^2}\right),
 $$
so
$$ 
t = -\frac{RC}{2}\ln\!\left(\frac{2U_{\text{fire}}}{CV_0^2}\right).
 $$

Substituting the given data,
$$ 
t = -\frac{(25 \times 10^9\ \Omega)(500 \times 10^{-12}\ \text{F})}{2}
\ln\!\left(\frac{2(50 \times 10^{-3}\ \text{J})}{(500 \times 10^{-12}\ \text{F})(30 \times 10^3\ \text{V})^2}\right).
 $$

## Answer
$$ 
t = 9.4\ \text{s}.
 $$

Fire or no fire: This car requires at least $9.4\ \text{s} $ before fuel can be brought safely near it. A pit crew cannot wait that long. So the tires include some type of conducting material (such as carbon black) to lower the tire resistance and thus increase the discharge rate.

## Key concepts used
- Capacitor energy: $U = q^2/(2C) $
- RC discharge charge law: $q = q_0 e^{-t/RC} $
- Equivalent resistance of four identical resistors in parallel: $R = R_{\text{tire}}/4 $
- Relation between charge and potential difference: $q = CV $
