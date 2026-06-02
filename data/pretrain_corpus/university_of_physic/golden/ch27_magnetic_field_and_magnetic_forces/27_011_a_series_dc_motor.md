---
source: Young and Freedman University Physics, 13th ed.
chapter: 27
section: 27.8
example_number: 27.11
subtitle: A series dc motor
needs_review: true
---

# Example 27.11: A series dc motor

## Problem
A dc motor with its rotor and field coils connected in series has an internal resistance of 2.00 Ω. When running at full load on a 120-V line, it draws a 4.00-A current.  
(a) What is the emf in the rotor?  
(b) What is the power delivered to the motor?  
(c) What is the rate of dissipation of energy in the internal resistance?  
(d) What is the mechanical power developed?  
(e) What is the motor’s efficiency?  
(f) What happens if the machine being driven by the motor jams, so that the rotor suddenly stops turning?

## Setup
This problem uses the ideas of power and potential drop in a series dc motor. We are given the internal resistance $r = 2.00\ \Omega $, the voltage across the motor $V_{ab} = 120\ \text{V} $, and the current through the motor $I = 4.00\ \text{A} $. We use Eq. (27.29) to determine the emf $E $ from these quantities.

The power delivered to the motor is $P_{\text{input}} = V_{ab} I $, the rate of energy dissipation is $P_{\text{dissipated}} = I^2 r $, and the power output by the motor is the difference between the power input and the power dissipated. The efficiency is the ratio of mechanical power output to electric power input.

## Solution
### (a)
From Eq. (27.29),
$$ 
V_{ab} = E + Ir
 $$
so
$$ 
120\ \text{V} = E + (4.00\ \text{A})(2.00\ \Omega)
 $$
and therefore
$$ 
E = 112\ \text{V}.
 $$

Because the magnetic force is proportional to velocity, $E $ is not constant but is proportional to the speed of rotation of the rotor.

### (b)
The power delivered to the motor from the source is
$$ 
P_{\text{input}} = V_{ab}I = (120\ \text{V})(4.00\ \text{A}) = 480\ \text{W}.
 $$

### (c)
The power dissipated in the resistance is
$$ 
P_{\text{dissipated}} = I^2 r = (4.00\ \text{A})^2(2.00\ \Omega) = 32\ \text{W}.
 $$

### (d)
The mechanical power output is the electric power input minus the rate of dissipation of energy in the motor’s resistance:
$$ 
P_{\text{output}} = P_{\text{input}} - P_{\text{dissipated}} = 480\ \text{W} - 32\ \text{W} = 448\ \text{W}.
 $$

### (e)
The efficiency is the ratio of mechanical power output to electric power input:
$$ 
\eta = \frac{P_{\text{output}}}{P_{\text{input}}}
= \frac{448\ \text{W}}{480\ \text{W}} = 0.93 = 93\%.
 $$

### (f)
With the rotor stalled, the back emf $E $ (which is proportional to rotor speed) goes to zero. From Eq. (27.29), the current becomes
$$ 
I = \frac{V_{ab}}{r} = \frac{120\ \text{V}}{2.00\ \Omega} = 60\ \text{A},
 $$
and the power dissipated in the resistance becomes
$$ 
P_{\text{dissipated}} = I^2 r = (60\ \text{A})^2(2.00\ \Omega) = 7200\ \text{W}.
 $$

## Evaluation
If this massive overload doesn’t blow a fuse or trip a circuit breaker, the coils will quickly melt. When the motor is first turned on, there’s a momentary surge of current until the motor picks up speed. This surge causes greater-than-usual voltage drops in the power lines supplying the current. Similar effects are responsible for the momentary dimming of lights in a house when an air conditioner or dishwasher motor starts.

## Key concepts used
- Series dc motor relation: $V_{ab} = E + Ir $
- Back emf $E $ is proportional to rotor speed
- Electric input power: $P = VI $
- Resistive loss: $P = I^2 r $
- Mechanical output power: $P_{\text{out}} = P_{\text{in}} - P_{\text{loss}} $
- Efficiency: $\eta = P_{\text{out}}/P_{\text{in}} $
