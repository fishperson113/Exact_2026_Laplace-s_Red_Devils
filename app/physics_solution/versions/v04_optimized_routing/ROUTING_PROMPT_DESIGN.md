# v03 Routing Prompt Design

## Goal

Classify each physics question into `(domain, answer_type)` using the same Qwen 3.5 4B model,
so we can select a domain-specific system prompt and matched few-shot examples for the solving pass.

## Methodology

### Step 1: Stop word filtering and tokenisation

Before computing keyword statistics, we applied standard text preprocessing:

1. **Tokenisation**: extract all alphabetic tokens of 3+ characters via regex `[a-zA-Z]{3,}`,
   lowercased.
2. **Stop word removal**: a manually curated list of ~60 English function words and
   generic physics-problem vocabulary that appear across ALL domains equally. These carry
   no domain-discriminating information and would dominate the frequency tables otherwise.

Stop word categories:
- **English function words**: the, a, an, of, is, in, to, and, at, by, are, with, that,
  from, for, on, it, its, has, be, as, or, if, this, when, what, how, which, between, ...
- **Generic problem verbs**: find, calculate, determine, given, placed, connected, ...
- **Common shared nouns**: value, answer, result, point, total, circuit (appears in 5/8 domains), ...

The full list is in `_analyze_domains.py` (one-off analysis script, not shipped).

We did NOT remove domain-relevant physics terms at this stage — only words that are
genuinely non-discriminating across all 8 domains.

### Step 2: Keyword frequency analysis

We extracted unigram and bigram frequencies per domain from `full_test.csv` (1352 questions),
then computed a **distinctiveness ratio**: `freq_in_domain / freq_in_other_domains`.
Words with high ratio AND high count are strong domain signals.

Thresholds used: `count >= 5` and `ratio > 1.5x`.

Raw statistical results (top keywords by distinctiveness ratio):

| Domain | Top distinctive words (count, ratio) |
|--------|--------------------------------------|
| **LD** (397) | forces (99, 164x), acting (198, 82x), angle (118, 49x), net (171, 28x), resultant (125, 26x), force (250, 16x), perpendicular (71, 15x) |
| **DT** (68) | vector (18, 30x), magnitude (35, 7x), strength (41, 5x), field (82, 3x), distance (28, 4x), charges (63, 2x) |
| **CH** (290) | phase (32, 151x), rms (102, 53x), resonance (115, 34x), reactance (56, 33x), consumed (43, 34x), angular (47, 74x), inductive (31, 37x) |
| **NL** (190) | coil (28, 112x), instantaneous (12, 96x), energy (221, 20x), inductance (59, 12x), magnetic (84, 10x), stored (41, 4x) |
| **TD** (177) | filled (36, 201x), plate (199, 139x), separation (36, 100x), parallel (124, 30x), capacitance (152, 8x), capacitor (301, 8x) |
| **DDT** (130) | solenoid (85, 1205x), turns (38, 539x), flux (23, 326x), induced (17, 241x), electromotive (17, 241x), self (7, 99x) |
| **THCB** (80) | error (68, 1631x), absolute (30, 719x), student (15, 360x), percentage (31, 106x), relative (44, 70x), measured (37, 52x) |
| **CHLT** (20) | occur (8, 155x), consists (6, 18x), resonance (14, 14x), frequency (16, 14x) |

### Step 3: Artifact filtering

Not all statistically distinctive words reflect genuine domain physics. We classified each
keyword into one of three categories:

| Category | Example | Action |
|----------|---------|--------|
| **Genuine physics term** | "force", "field strength", "solenoid", "impedance", "capacitance", "error" | Keep — these reflect the domain's actual subject matter |
| **Dataset style artifact** | "triangle", "vertices", "equilateral", "isosceles" (LD) | Drop from prompt — these are common in this dataset's geometry-style problems but not intrinsic to electrostatics. A force problem could have any charge arrangement. |
| **Overlapping term** | "charges" (appears in both LD and DT), "capacitor" (TD, NL, CH) | Keep but add disambiguation rule — the term alone doesn't determine domain; the TARGET quantity does. |

Key artifacts identified and removed:
- **LD**: "triangle", "vertices", "equilateral", "isosceles", "legs", "side" — geometry of charge placement, not physics content
- **DT**: "axis", "metal", "four", "square" — problem setup specifics
- **NL**: "round", "shape", "graph", "unit" — formatting artifacts
- **THCB**: "lamp", "bulb", "student", "temperature" — problem scenario details

### Step 4: Domain-knowledge augmentation

After removing artifacts, we added physics terms that are genuinely characteristic of each
domain but might not appear frequently in this particular dataset:

| Domain | Added terms (from physics knowledge) |
|--------|--------------------------------------|
| **LD** | "Coulomb", "repulsive", "attractive", "interaction between charges", "equilibrium position" |
| **DT** | "potential difference", "equipotential", "where the field is zero" |
| **CH** | "voltage across", "AC source", "power factor" |
| **NL** | "LC oscillation", "oscillation period", "maximum current", "conservation of energy" |
| **TD** | "equivalent capacitance", "series/parallel capacitors", "disconnected from source" |
| **DDT** | "Faraday", "Lenz", "mutual inductance", "rate of change of current" |
| **THCB** | "uncertainty", "ammeter", "voltmeter", "battery", "internal resistance" |
| **CHLT** | (defined by question format, not physics terms) |

### Step 5: Disambiguation rules

The main confusion pairs identified from the v03-initial run (66.5% routing accuracy):

| Misroute | Count | Root cause | Rule added |
|----------|-------|------------|------------|
| LD -> DT (209) | Both involve charges. LD asks for force, DT asks for field/potential. | "asks for FORCE -> LD, asks for FIELD or POTENTIAL -> DT" |
| NL -> TD (77) | Both involve capacitors. NL asks about energy, TD about capacitance/geometry. | "energy in a capacitor -> NL, capacitance/charge/geometry -> TD" |
| CH -> NL (48) | Both involve circuits. CH asks for I/U/Z/f, NL asks for energy. | "circuit I/U/Z/f -> CH, energy stored -> NL" |
| NL -> DDT (37) | NL inductor problems confused with DDT solenoid. | "solenoid/flux/induced EMF -> DDT, energy in inductor -> NL" |
| DDT -> CH (25) | DDT impedance problems confused with CH circuits. | "solenoid properties -> DDT" |
| THCB -> CH (19) | Basic DC confused with AC circuits. | "measurement/error/basic DC -> THCB" |

### Step 6: Few-shot examples

We wrote **synthetic examples** (not copied from the test set) for each domain. Each example
is a minimal representative question that captures the domain's core pattern:
- Uses the domain's characteristic physics setup
- Asks for the domain's characteristic target quantity
- Is short enough to not bloat the classification prompt

## Prompt structure

```
System: domain descriptions + answer types + disambiguation rules
[8 few-shot pairs: user question -> assistant JSON]
User: {actual question}
```

Total prompt size: ~800 tokens system + ~400 tokens few-shot = ~1200 tokens input.
Output: ~20 tokens (JSON object).

## Classification parameters

- `max_new_tokens=50` (JSON is ~20 tokens, buffer for formatting)
- `temperature=0.0` (deterministic classification)
- Same model instance as solving pass (no extra load time)
- Fallback on JSON parse failure: `domain="LD"`, `answer_type="pure_numeric"` (most common)
