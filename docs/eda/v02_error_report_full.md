# Error analysis — results_golden

- **Total:** 1352
- **Correct:** 714 (0.528)
- **Wrong:** 638

## 1. Per-answer-type accuracy

| answer_type   |   n |   correct |   accuracy |
|:--------------|----:|----------:|-----------:|
| pure_numeric  | 985 |       601 |      0.61  |
| sci_notation  | 239 |        55 |      0.23  |
| text_only     |  56 |         4 |      0.071 |
| multi_value   |  26 |        21 |      0.808 |
| mixed         |  25 |        13 |      0.52  |
| yes_no        |  21 |        20 |      0.952 |

## 2. Fail-mode breakdown

| Fail mode | Count | % of wrong |
|---|---:|---:|
| `magnitude_wrong` | 187 | 29.3% |
| `off_by_power10` | 167 | 26.2% |
| `numeric_far` | 93 | 14.6% |
| `lexically_wrong` | 56 | 8.8% |
| `formula_off` | 49 | 7.7% |
| `sci_scale_wrong` | 42 | 6.6% |
| `unit_mismatch` | 20 | 3.1% |
| `wrong_subquestion` | 10 | 1.6% |
| `format_no_final` | 5 | 0.8% |
| `count_wrong` | 4 | 0.6% |
| `wrong_sign` | 2 | 0.3% |
| `format_bad_number` | 1 | 0.2% |
| `partial_match` | 1 | 0.2% |
| `wrong_choice` | 1 | 0.2% |

## 3. Per-domain accuracy

| domain   |   n |   correct |   accuracy |
|:---------|----:|----------:|-----------:|
| LD       | 397 |       113 |      0.285 |
| CH       | 290 |       171 |      0.59  |
| NL       | 190 |       149 |      0.784 |
| TD       | 177 |        82 |      0.463 |
| DDT      | 130 |        85 |      0.654 |
| THCB     |  80 |        69 |      0.862 |
| DT       |  68 |        26 |      0.382 |
| CHLT     |  20 |        19 |      0.95  |

## 4. Fail mode × domain

| fail_mode         |   CH |   CHLT |   DDT |   DT |   LD |   NL |   TD |   THCB |
|:------------------|-----:|-------:|------:|-----:|-----:|-----:|-----:|-------:|
| count_wrong       |    0 |      0 |     1 |    0 |    0 |    0 |    2 |      1 |
| format_bad_number |    0 |      0 |     0 |    0 |    1 |    0 |    0 |      0 |
| format_no_final   |    3 |      0 |     0 |    1 |    1 |    0 |    0 |      0 |
| formula_off       |    0 |      0 |     0 |    4 |   43 |    0 |    2 |      0 |
| lexically_wrong   |    0 |      0 |    24 |    0 |    1 |   23 |    4 |      4 |
| magnitude_wrong   |   57 |      0 |     5 |   17 |   92 |    2 |   10 |      4 |
| numeric_far       |   27 |      0 |     2 |   11 |   43 |    2 |    8 |      0 |
| off_by_power10    |   27 |      0 |    12 |    2 |   51 |   10 |   64 |      1 |
| partial_match     |    0 |      0 |     0 |    0 |    0 |    0 |    0 |      1 |
| sci_scale_wrong   |    0 |      0 |     1 |    3 |   37 |    0 |    1 |      0 |
| unit_mismatch     |    0 |      0 |     0 |    1 |   13 |    3 |    3 |      0 |
| wrong_choice      |    0 |      1 |     0 |    0 |    0 |    0 |    0 |      0 |
| wrong_sign        |    0 |      0 |     0 |    2 |    0 |    0 |    0 |      0 |
| wrong_subquestion |    5 |      0 |     0 |    1 |    2 |    1 |    1 |      0 |

## 5. Fail mode × answer type

| fail_mode         |   mixed |   multi_value |   pure_numeric |   sci_notation |   text_only |   yes_no |
|:------------------|--------:|--------------:|---------------:|---------------:|------------:|---------:|
| count_wrong       |       0 |             4 |              0 |              0 |           0 |        0 |
| format_bad_number |       0 |             0 |              1 |              0 |           0 |        0 |
| format_no_final   |       0 |             0 |              3 |              2 |           0 |        0 |
| formula_off       |       0 |             0 |              0 |             49 |           0 |        0 |
| lexically_wrong   |       4 |             0 |              0 |              0 |          52 |        0 |
| magnitude_wrong   |       3 |             0 |            112 |             72 |           0 |        0 |
| numeric_far       |       4 |             0 |             85 |              4 |           0 |        0 |
| off_by_power10    |       0 |             0 |            165 |              2 |           0 |        0 |
| partial_match     |       0 |             1 |              0 |              0 |           0 |        0 |
| sci_scale_wrong   |       0 |             0 |              0 |             42 |           0 |        0 |
| unit_mismatch     |       0 |             0 |              8 |             12 |           0 |        0 |
| wrong_choice      |       0 |             0 |              0 |              0 |           0 |        1 |
| wrong_sign        |       0 |             0 |              2 |              0 |           0 |        0 |
| wrong_subquestion |       1 |             0 |              8 |              1 |           0 |        0 |

## 6. Domain × answer type

| domain   |   mixed |   multi_value |   pure_numeric |   sci_notation |   text_only |   yes_no |
|:---------|--------:|--------------:|---------------:|---------------:|------------:|---------:|
| CH       |       1 |             0 |            288 |              1 |           0 |        0 |
| CHLT     |       0 |             0 |              0 |              0 |           0 |       20 |
| DDT      |       4 |             1 |             78 |             21 |          25 |        1 |
| DT       |       6 |             0 |             39 |             23 |           0 |        0 |
| LD       |       5 |             0 |            201 |            190 |           1 |        0 |
| NL       |       8 |             0 |            160 |              0 |          22 |        0 |
| TD       |       1 |             2 |            166 |              4 |           4 |        0 |
| THCB     |       0 |            23 |             53 |              0 |           4 |        0 |

## 7. Top suspect gold cases

Rows where the model's prediction matches a number from the question text,
suggesting the model may have copied a given value instead of computing the answer.

### 1. `CH104`
- **Gold:** `28.87` (unit: `Ω`)
- **Pred:** `25.0`
- **Explain:** pred 25.0 matches question number 25.0
- **Q:** Given R=25Ω. At a frequency f=120Hz, the circuit is in resonance, and the current I=5A. When the frequency is doubled, the current becomes I=2.5A. What is ZL (the inductive reactance at the initial fr

### 2. `CH108`
- **Gold:** `15` (unit: `Ω`)
- **Pred:** `30.0`
- **Explain:** pred 30.0 matches question number 30.0
- **Q:** Given an RLC series circuit with a resistance R=30Ω. At its resonant frequency f=50Hz, the current flowing through the circuit is I=2A. If the frequency is then changed to f=100Hz, the current becomes

### 3. `CH154`
- **Gold:** `141.4` (unit: `V`)
- **Pred:** `100.0`
- **Explain:** pred 100.0 matches question number 100.0
- **Q:** A voltage u = 200√2 cos 100πt (V) is applied to a series RLC circuit with R = 100 Ω, L = 1/π H, C = 10⁻⁴/(2π) F. Calculate the RMS voltage across the inductor, UL

### 4. `CH155`
- **Gold:** `282.8` (unit: `V`)
- **Pred:** `200.0`
- **Explain:** pred 200.0 matches question number 200.0
- **Q:** A voltage u = 200√2 cos 100πt (V) is applied to a series RLC circuit with R = 100 Ω, L = 1/π H, C = 10⁻⁴/(2π) F. Calculate the RMS voltage across the capacitor, $U_C$.

### 5. `CH245`
- **Gold:** `64.0` (unit: `W`)
- **Pred:** `2.0`
- **Explain:** pred 2.0 matches question number 2.0
- **Q:** Consider a circuit AB with R1 = 60 Ω, R2 = 30 Ω, satisfying LCω² = 1, and uAM is in quadrature (90° out of phase) with uMB. The total power consumed by the circuit when U = 80 V is applied across AB i

### 6. `CH370`
- **Gold:** `948.68` (unit: `V`)
- **Pred:** `89.96`
- **Explain:** pred 89.96 matches question number 90.0
- **Q:** At resonance, U = 90 V, R = 15 Ω, L = 0.25 H, C = 10 µF. Calculate UL.

### 7. `DT030`
- **Gold:** `48` (unit: `cm`)
- **Pred:** `9.0`
- **Explain:** pred 9.0 matches question number 9.0
- **Q:** Given two electric charges q1 = 9 x 10^-8 C and q2 = -16 x 10^-8 C are placed at two points A and B in air, separated by 12cm. Find the point where the electric field vector is zero, and calculate its

### 8. `DT062`
- **Gold:** `-2.7 * 10^{-8}` (unit: `C`)
- **Pred:** `3.0`
- **Explain:** pred 3.0 matches question number 3.0
- **Q:** Four points A, B, C, D in air form a rectangle ABCD with sides AD = 3 cm and AB = 4 cm. Charges q1, q2, q3 are placed at A, B, and C respectively. Let vector E2 be the electric field vector produced b

### 9. `LD076`
- **Gold:** `-4 * 10^{-7}` (unit: `C`)
- **Pred:** `2.0`
- **Explain:** pred 2.0 matches question number 2.0
- **Q:** At the three vertices A, B, and C of a square ABCD with side length 6 cm in a vacuum, three point charges are placed: q1 = q3 = 2 × 10^-7 C and q2 = -4 × 10^-7 C. Determine the charge q4 placed at D s

### 10. `LD085`
- **Gold:** `4 * k * q / a^2` (unit: `-`)
- **Pred:** `2.0`
- **Explain:** pred 2.0 matches question number 2.0
- **Q:** At the three vertices of a right isosceles triangle ABC, with AB = AC = a, three positive charges qA = qB = q and qC = 2q are placed in a vacuum. What is the expression for the electric field intensit

### 11. `LD117`
- **Gold:** `0.734 * 10^{-3}` (unit: `N`)
- **Pred:** `0.999`
- **Explain:** pred 0.999 matches question number 1.0
- **Q:** Two electric charges, q1 = -3 × 10^-8 C and q2 = -6 × 10^-8 C, are placed at points A and B, separated by 17 cm in the air. A third charge, q3 = +3 × 10^-8 C, is placed at point C. Given that the dist

### 12. `NL383`
- **Gold:** `0.00075` (unit: `J`)
- **Pred:** `0.00102`
- **Explain:** pred 0.00102 matches question number 0.001
- **Q:** In an LC circuit, a capacitor has a capacitance of 30 µF, and the voltage at time t is 100cos(1500t). Calculate the electric field energy at t = 0.001 s.

### 13. `TD387`
- **Gold:** `2.140` (unit: `μF`)
- **Pred:** `5.0`
- **Explain:** pred 5.0 matches question number 5.0
- **Q:** A capacitor C = 5 μF is charged to 20 V. It is then connected in series with an uncharged capacitor C'. The entire circuit has a total voltage of 20 V. If the final charge on C is 30 μC, find C'.

### 14. `THCB128`
- **Gold:** `200.3; 0.133` (unit: `g; g`)
- **Pred:** `200.33`
- **Explain:** pred 200.33 matches question number 200.5
- **Q:** Three mass measurements were taken: 200.5 g, 200.3 g, and 200.2 g. Calculate the average mass and the average absolute error.


## 8. Sample wrong rows per mode

### `count_wrong`

- **TD374** gold=`0; 0` pred=`0.0` unit_gold=`μC; μJ` unit_pred=`C`
  - Q: A capacitor C = 3 μF, is charged at 12 V, then its two plates are short-circuited. Calculate the charge and energy after short-circuiting.
- **TD376** gold=`36;12` pred=`3.6e-05` unit_gold=`μJ; μC` unit_pred=`J`
  - Q: A capacitor with C = 2 μF is connected to a voltage of 6 V. Calculate the energy and the charge.
- **DDT340** gold=`38.16; 0.30` pred=`0.3` unit_gold=`—` unit_pred=`—`
  - Q: Given a series circuit with R = 12 Ω, C = 80 μF, and a frequency of 60 Hz, determine the capacitive reactance and the power factor if the impedance Z = 40 Ω.

### `format_bad_number`

- **LD026** gold=`0.18` pred=`nan` unit_gold=`N` unit_pred=`-`
  - Q: Two electric charges, q1 = 8 × 10^-8 C and q2 = -8 × 10^-8 C, are placed at points A and B respectively, in air (AB = 6 cm). Determine the force acting on a third charge q3 = 8 × 10^-8 C, given that: 

### `format_no_final`

- **LD076** gold=`-4 * 10^{-7}` pred=`2.0` unit_gold=`C` unit_pred=`nan`
  - Q: At the three vertices A, B, and C of a square ABCD with side length 6 cm in a vacuum, three point charges are placed: q1 = q3 = 2 × 10^-7 C and q2 = -4 × 10^-7 C. Determine the charge q4 placed at D s
- **CH212** gold=`0.707` pred=`2.0` unit_gold=`-` unit_pred=`nan`
  - Q: In an RLC series circuit, at an angular frequency of ω0, the inductor has an inductive reactance of 66 Ω and the capacitor has a capacitive reactance of 33 Ω. To what multiple of ω0 must the angular f
- **CH213** gold=`2.0` pred=`0.0` unit_gold=`-` unit_pred=`nan`
  - Q: For an RLC series circuit with constant components, when the angular frequency is ω0, X_L = 54 Ω and X_C = 216 Ω. By what factor must the angular frequency be multiplied (from ω0) for resonance to occ

### `formula_off`

- **LD098** gold=`1.152 * 10^{7}` pred=`864000.0` unit_gold=`V/m` unit_pred=`N/C`
  - Q: Two point charges q1 = −2 × 10^-6 C and q2 = −2 × 10^-6 C are placed at points A and B, 6 cm apart. Calculate the resultant electric field strength at point C, which lies on the perpendicular bisector
- **LD056** gold=`33.6 * 10^{5}` pred=`0.148` unit_gold=`V/m` unit_pred=`N`
  - Q: At two points A and B, separated by 20 cm in air, two point charges q1 = 4 × 10^-6 C and q2 = -6.4 × 10^-6 C are placed. Determine the electric field strength caused by these two point charges at poin
- **LD269** gold=`3.62 * 10^{-3}` pred=`0.236` unit_gold=`N` unit_pred=`N`
  - Q: Three identical charges q = -8 × 10^-8 C are placed at the three vertices of an isosceles right triangle with 15 cm legs. Calculate the net force acting on the charge at the right angle vertex.

### `lexically_wrong`

- **LD047** gold=`Hướng về phía q₂` pred=`nan` unit_gold=`-` unit_pred=`-`
  - Q: A test charge is placed at a point whose distances to the two charges q1 = +2 μC and q2 = -3 μC are 3 cm and 4 cm, respectively. The two charges are fixed and separated by 7 cm. What is the direction 
- **NL095** gold=`all the energy is stored in the electric field of the capacitor.` pred=`nan` unit_gold=`—` unit_pred=`-`
  - Q: An LC circuit oscillates with current i(t) = I₀cos(ωt). When i = 0, where is the energy stored?
- **NL120** gold=`maximum` pred=`nan` unit_gold=`—` unit_pred=`A`
  - Q: An LC circuit is oscillating, and the electric field energy is zero. Calculate the instantaneous current.

### `magnitude_wrong`

- **LD110** gold=`0.023` pred=`0.004423` unit_gold=`N` unit_pred=`N`
  - Q: Two charges q1 = +7 × 10^-8 C and q2 = -6 × 10^-8 C are placed at points A and B, 10 cm apart in air. A third charge q3 = +8 × 10^-8 C is placed at point C, such that the distance from C to A is 7 cm 
- **LD377** gold=`8.44 * 10^{6}` pred=`10400000.0` unit_gold=`V/m` unit_pred=`V/m`
  - Q: Three charges, q1 = q2 = 3.32 × 10^-6 C and q3 = 3.64 × 10^-6 C, are placed at the three vertices of an equilateral triangle with a side length of 7.83 cm. Calculate the resultant electric field at th
- **LD385** gold=`3.50 * 10^{6}` pred=`2830000.0` unit_gold=`V/m` unit_pred=`V/m`
  - Q: Three charges q1 = q2 = 2.15 × 10^-6 C and q3 = 4.76 × 10^-6 C are placed at the three vertices of an equilateral triangle with a side length of 9.78 cm. Calculate the net electric field strength at t

### `numeric_far`

- **LD274** gold=`36.32` pred=`2.1176` unit_gold=`N` unit_pred=`N`
  - Q: Two point charges, q1 = +8 × 10^-6 C and q2 = -8 × 10^-6 C, are placed at points A and B, separated by 10 cm. A test charge q with a magnitude of 10^-6 C is placed at point M, which lies on the perpen
- **LD087** gold=`-2\sqrt{2} q` pred=`0.0` unit_gold=`-` unit_pred=`C`
  - Q: Given a square ABCD with side length 'a'. Charges q1 = q3 = q are placed at A and C. What charge must be placed at B so that the electric field at D is zero?
- **LD054** gold=`0.094` pred=`0.0` unit_gold=`N` unit_pred=`N`
  - Q: Two point charges, q1 = 6 × 10^-6 C and q2 = -6 × 10^-6 C, are placed in air at points A and B, separated by 10 cm.
 Calculate the electric force exerted on a charge q3 = -3 × 10^-8 C placed at C.

### `off_by_power10`

- **LD248** gold=`0.495` pred=`0.0495` unit_gold=`N` unit_pred=`N`
  - Q: Two electric charges q1 = +7 × 10^-6 C and q2 = -7 × 10^-6 C are placed at points A and B, separated by 6 cm. A test charge q = 10^-8 C is placed at point M, which lies on the perpendicular bisector o
- **LD049** gold=`14.34` pred=`1.51` unit_gold=`N` unit_pred=`N`
  - Q: Two charges, q1 = +5 μC and q2 = +5 μC, are placed at points A and B, 10 cm apart. Calculate the magnitude of the force acting on a test charge q0 = +1 μC placed at a point 6 cm from A and 8 cm from B
- **LD073** gold=`937.5` pred=`93750.0` unit_gold=`V/m` unit_pred=`V/m`
  - Q: There are two point charges, q1 = 0.5 nC and q2 = −0.5 nC, respectively placed at points A and B, separated by a distance a = 6 cm in the air. Determine the electric field strength E at point C, which

### `partial_match`

- **THCB128** gold=`200.3; 0.133` pred=`200.33` unit_gold=`g; g` unit_pred=`g; g`
  - Q: Three mass measurements were taken: 200.5 g, 200.3 g, and 200.2 g. Calculate the average mass and the average absolute error.

### `sci_scale_wrong`

- **LD343** gold=`2.027 * 10^{6}` pred=`19440000.0` unit_gold=`V/m` unit_pred=`N/C`
  - Q: Two charges, q1 = -2.4 × 10^-6 C and q2 = -2.1 × 10^-6 C, are separated by 7.5 cm. Point M lies on the line connecting the two charges but outside the segment between them, and is located 11.9 cm to t
- **LD151** gold=`5.09 * 10^{-4}` pred=`5.091` unit_gold=`N` unit_pred=`N`
  - Q: Three identical charges, q = -2 × 10^-8 C, are placed at the three vertices of an isosceles right triangle with legs of length a = 10 cm. Calculate the net force acting on the charge at the right-angl
- **LD315** gold=`7.6 * 10^{6}` pred=`71000000.0` unit_gold=`V/m` unit_pred=`V/m`
  - Q: Three identical charges, q = 2.6 × 10^-6 C, are placed at the three vertices of an isosceles right triangle with legs measuring 6.6 cm. Calculate the net electric field strength at the right-angle ver

### `unit_mismatch`

- **LD251** gold=`0.023` pred=`0.022627` unit_gold=`N` unit_pred=`N`
  - Q: Three identical charges q = -2 × 10^-7 C are placed at the three vertices of an isosceles right triangle with legs of 15 cm. Calculate the net force acting on the charge at the right-angled vertex.
- **LD398** gold=`11.41 * 10^{6}` pred=`11600000.0` unit_gold=`V/m` unit_pred=`N/C`
  - Q: Two electric charges, q1 = 4.64 × 10^-6 C and q2 = 2.36 × 10^-6 C, are placed at the ends of a straight line segment of length 8.48 cm. Calculate the electric field strength at the midpoint of that li
- **LD296** gold=`7.05 * 10^{6}` pred=`6930000.0` unit_gold=`V/m` unit_pred=`V/m`
  - Q: Three electric charges, q1 = q2 = q3 = 4.8 × 10^-6 C, are placed at the three vertices of an equilateral triangle with a side length of 10.3 cm. Calculate the resultant electric field strength at the 

### `wrong_choice`

- **CHLT006** gold=`Yes` pred=`nan` unit_gold=`-` unit_pred=`-`
  - Q: An RLC series circuit consists of a resistor with R=100 Ω, an inductor with L=0.02 H, and a capacitor with C=200 μF. Is it in resonance at a frequency of 80 Hz?

### `wrong_sign`

- **DT005** gold=`0.094` pred=`-0.507` unit_gold=`N` unit_pred=`N`
  - Q: At two points A and B, 10 cm apart in the air, two point charges are placed: q1 = 6 x 10^-6 C and q2 = -6 x 10^-6 C. Determine the electric field strength caused by these two charges at point C, given
- **DT025** gold=`60` pred=`-0.115` unit_gold=`cm` unit_pred=`m`
  - Q: Given two point charges located along the Ox axis: charge q1 = -9 x 10^-6 C is placed at the origin O, and charge q2 = 4 x 10^-6 C is located 20 cm from the origin. What is the coordinate on the Ox ax

### `wrong_subquestion`

- **LD117** gold=`0.734 * 10^{-3}` pred=`0.999` unit_gold=`N` unit_pred=`N`
  - Q: Two electric charges, q1 = -3 × 10^-8 C and q2 = -6 × 10^-8 C, are placed at points A and B, separated by 17 cm in the air. A third charge, q3 = +3 × 10^-8 C, is placed at point C. Given that the dist
- **LD085** gold=`4 * k * q / a^2` pred=`2.0` unit_gold=`-` unit_pred=`V/m`
  - Q: At the three vertices of a right isosceles triangle ABC, with AB = AC = a, three positive charges qA = qB = q and qC = 2q are placed in a vacuum. What is the expression for the electric field intensit
- **CH154** gold=`141.4` pred=`100.0` unit_gold=`V` unit_pred=`V`
  - Q: A voltage u = 200√2 cos 100πt (V) is applied to a series RLC circuit with R = 100 Ω, L = 1/π H, C = 10⁻⁴/(2π) F. Calculate the RMS voltage across the inductor, UL


## 9. Conclusions

### Route priority for Stage 2+

Based on per-answer-type accuracy, prioritize routing for types with lowest accuracy.

- **yes_no / text_only:** Likely 0% with current numeric pipeline — needs dedicated classifier.
- **sci_notation:** May benefit from notation-aware extraction.
- **multi_value:** Requires structured output parsing.
- **pure_numeric:** Baseline established — focus on reducing magnitude_wrong and off_by_power10.
