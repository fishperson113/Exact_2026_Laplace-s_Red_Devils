# Error analysis — v02_fewshot

- **Total:** 973
- **Correct:** 453 (0.466)
- **Wrong:** 520

## Fail-mode breakdown

| Fail mode | Count | % of wrong |
|---|---:|---:|
| `numeric_far` | 170 | 32.7% |
| `magnitude_wrong` | 169 | 32.5% |
| `off_by_power10` | 165 | 31.7% |
| `format_no_final` | 10 | 1.9% |
| `unit_mismatch` | 4 | 0.8% |
| `format_bad_number` | 2 | 0.4% |

## Per-domain accuracy

| domain   |   n |   correct |   accuracy |
|:---------|----:|----------:|-----------:|
| CH       | 289 |       138 |      0.478 |
| LD       | 201 |        50 |      0.249 |
| TD       | 167 |        37 |      0.222 |
| NL       | 160 |       119 |      0.744 |
| DDT      |  78 |        63 |      0.808 |
| DT       |  39 |        11 |      0.282 |
| THCB     |  39 |        35 |      0.897 |

## Fail mode × domain

| fail_mode         |   CH |   DDT |   DT |   LD |   NL |   TD |   THCB |
|:------------------|-----:|------:|-----:|-----:|-----:|-----:|-------:|
| format_bad_number |    2 |     0 |    0 |    0 |    0 |    0 |      0 |
| format_no_final   |    8 |     0 |    0 |    1 |    0 |    1 |      0 |
| magnitude_wrong   |   95 |     3 |   12 |   31 |   12 |   14 |      2 |
| numeric_far       |   31 |     2 |   15 |  108 |    6 |    8 |      0 |
| off_by_power10    |   15 |    10 |    1 |   11 |   23 |  105 |      0 |
| unit_mismatch     |    0 |     0 |    0 |    0 |    0 |    2 |      2 |

## Sample wrong rows per mode

### `format_bad_number`

- **CH259** gold=`180.0` pred=`nan` unit_gold=`V` unit_pred=`V`
  - Q: A circuit has XL = 35 Ω, XC = 140 Ω, and a source voltage U = 180 V. If the frequency is doubled, what is the voltage across R?
- **CH256** gold=`200.0` pred=`nan` unit_gold=`V` unit_pred=`nan`
  - Q: An RLC circuit has an inductive reactance XL = 18 Ω, a capacitive reactance XC = 72 Ω, and the total voltage U = 200 V. When the frequency is doubled, what is the RMS voltage across the resistor R?

### `format_no_final`

- **CH228** gold=`50.0` pred=`0.0` unit_gold=`Ω` unit_pred=`nan`
  - Q: The circuit AB consists of R1 = 50 Ω and a segment MB (containing R2 and an inductor L), satisfying the condition LCω² = 1. The voltage uAM and uMB are in quadrature (90 degrees out of phase). When an
- **CH219** gold=`67.5` pred=`90.0` unit_gold=`W` unit_pred=`nan`
  - Q: Circuit AB comprises two segments connected in series: AM and MB. Segment AM consists of resistor R1 = 40 Ω in series with capacitor C. Segment MB consists of resistor R2 = 80 Ω in series with inducto
- **CH141** gold=`84.85` pred=`2.0` unit_gold=`V` unit_pred=`nan`
  - Q: An AC series circuit consists of a pure resistor R, a capacitor C, and an inductor L with internal resistance r. An AC voltage of 120V – 50Hz is applied across the entire circuit. The RMS voltage acro
- **CH258** gold=`75.0` pred=`108.0` unit_gold=`V` unit_pred=`nan`
  - Q: An RLC circuit has XL = 12 Ω, XC = 108 Ω, and a total (RMS) voltage U = 75 V. When the frequency is tripled (increased by a factor of three), what is the RMS voltage across the resistor?
- **CH233** gold=`60.0` pred=`3.0` unit_gold=`Ω` unit_pred=`nan`
  - Q: The circuit AB consists of segment MB, where R2 = 90 Ω is connected in series with an inductor L. We are given LCω² = 1, and the voltage U_AM is 90 degrees out of phase with U_MB. When a voltage U = 1

### `magnitude_wrong`

- **CH085** gold=`5.07` pred=`25.33` unit_gold=`μF` unit_pred=`μF`
  - Q: A circuit needs to resonate at 1000 Hz. Given an inductor L=0.005 H, what capacitance C is needed?
- **CH245** gold=`64.0` pred=`16.0` unit_gold=`W` unit_pred=`W`
  - Q: Consider a circuit AB with R1 = 60 Ω, R2 = 30 Ω, satisfying LCω² = 1, and uAM is in quadrature (90° out of phase) with uMB. The total power consumed by the circuit when U = 80 V is applied across AB i
- **CH109** gold=`46.19` pred=`12.57` unit_gold=`Ω` unit_pred=`Ω`
  - Q: R = 40Ω, resonance frequency f = 60Hz. The current is halved when f = 120Hz. What is ZL?
- **CH261** gold=`130.0` pred=`104.5` unit_gold=`V` unit_pred=`V`
  - Q: Given XL = 28 Ω, XC = 112 Ω, and the total supply voltage U = 130 V. If the frequency is doubled, what is the RMS voltage across the resistor?
- **CH144** gold=`63.3` pred=`110.0` unit_gold=`V` unit_pred=`V`
  - Q: A series RLC circuit at resonance is connected to an AC supply with an RMS voltage of 90 V. The RMS voltage measured across the R-C section and across the C-L section are both 110 V. Calculate the RMS

### `numeric_far`

- **CH079** gold=`58.63` pred=`0.000177` unit_gold=`mH` unit_pred=`H`
  - Q: What inductance L is required for a circuit with C=30 μF to resonate at 120 Hz?
- **CH091** gold=`46.9` pred=`0.000289` unit_gold=`μF` unit_pred=`F`
  - Q: Determine the capacitance C required for resonance with an inductor of L=0.6 H at a frequency of f=30 Hz.
- **CH066** gold=`63.33` pred=`0.0159` unit_gold=`mH` unit_pred=`H`
  - Q: A capacitor with C=40 μF. To resonate at f=100 Hz, what inductor L is needed?
- **CH278** gold=`400.0` pred=`1.02` unit_gold=`W` unit_pred=`W`
  - Q: A circuit has XL = 15 Ω, XC = 135 Ω, R = 25 Ω, and U = 100 V. If the frequency is increased by 3 times, what is the power consumed by R?
- **CH082** gold=`1.58` pred=`6.33e-07` unit_gold=`μF` unit_pred=`F`
  - Q: 1. **"If L = 0.1 H, what capacitance C should be chosen to achieve resonance at f = 400 Hz?"**
2. **"Given L = 0.1 H, what value of capacitor C is needed to resonate at f = 400 Hz?"**
3. **"What capac

### `off_by_power10`

- **CH355** gold=`162.11` pred=`1.59` unit_gold=`µF` unit_pred=`μF`
  - Q: L = 0.25 H. If it resonates at 25 Hz, what is C?
- **CH071** gold=`15.83` pred=`159.15` unit_gold=`μF` unit_pred=`μF`
  - Q: What value of C is needed for a circuit to resonate at 400 Hz with L=0.01 H?
- **CH094** gold=`0.0405` pred=`0.000405` unit_gold=`H` unit_pred=`H`
  - Q: What inductance L is required for a circuit to resonate at f=250 Hz, given a 10 μF capacitor?
- **CH081** gold=`633.26` pred=`0.00633` unit_gold=`mH` unit_pred=`H`
  - Q: Given a 4 μF capacitor, what inductance (L) is needed for resonance at 100 Hz?
- **CH062** gold=`12.67` pred=`1.266e-05` unit_gold=`μF` unit_pred=`F`
  - Q: What capacitance must the capacitor have for an L-C circuit with L = 0.2 H to resonate at 100 Hz?

### `unit_mismatch`

- **TD098** gold=`4.57` pred=`4.5` unit_gold=`—` unit_pred=`-`
  - Q: A capacitor has a capacitance of 6.3 nF, a plate area of 14 cm², and a plate separation of 9.0×10⁻⁶ m. Calculate the dielectric constant of the dielectric material in the capacitor.
- **TD099** gold=`196.67` pred=`200.0` unit_gold=`V` unit_pred=`V`
  - Q: Two capacitors, C1 = 2.5 μF and C2 = 3.5 μF, are charged to U1 = 220 V and U2 = 180 V, respectively. They are then connected with their like-polarity terminals joined (i.e., positive to positive and n
- **THCB134** gold=`1.67` pred=`1.7` unit_gold=`%` unit_pred=`%`
  - Q: The measured current is 3.00 ± 0.05 A. Calculate the percent relative uncertainty.
- **THCB119** gold=`1.67` pred=`1.7` unit_gold=`%` unit_pred=`%`
  - Q: The resistance measurement result is: 12.0 ± 0.2 Ω. Calculate the percentage relative uncertainty.
