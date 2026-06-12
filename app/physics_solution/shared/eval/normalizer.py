"""Canonical answer/unit normalizer for the BTC /predict output (Submission Guide §4-5).

The BTC grader matches Type-2 `answer` + `unit` against ground truth in the convention we
declare in notation_mapping.csv (submission/notation_mapping.csv). This module converts the
raw pipeline output (whatever Qwen printed after FINAL ANSWER/UNIT) into that ONE declared
convention:

  value : plain decimal ("0.702562") or e-notation ("1.15e-07"); every ×10^/10^{}/superscript
          variant is reparsed and re-emitted as e-notation. Multi-values joined with "; ".
  unit  : ASCII (Guide §4.2 "unit ... in ASCII"): Ω/Ohm/Ohms -> ohm, µ/μ -> u, ° -> deg,
          unicode superscripts -> ^n. No-unit markers (nan/None/empty/N/A/dimensionless/
          yes_no/...) all collapse to "N/A".

Measured against the actual model output (348 answers in
versions/v07_ensemble_vLLM/output/final_experiment_raw.jsonl) — every rule below maps a form
Qwen really emits, not a hypothetical one.

Pure functions, no I/O — safe to call from the serving path.
"""

from __future__ import annotations

import math
import re

# --------------------------------------------------------------------------- #
#  unit normalization                                                          #
# --------------------------------------------------------------------------- #

# Tokens the model (or the dataset) uses to say "this answer has no unit".
# All collapse to the single canonical no-unit marker NO_UNIT ("N/A").
_NO_UNIT_TOKENS = {
    "", "-", "--", "—", "–", "_", "nan", "none", "null", "n/a", "na",
    "dimensionless", "unitless", "no unit", "nounit", "(factor)", "factor",
    "factor)", "ratio", "times", "fold", "yes_no", "yes/no", "y/n", "boolean",
    "bool", "text", "string", "direction", "relationship", "=", ";",
}

NO_UNIT = "N/A"

# Spelled-out unit words -> ASCII symbol (case-insensitive, whole-token only).
_UNIT_WORDS = {
    "ohm": "ohm", "ohms": "ohm",
    "volt": "V", "volts": "V",
    "ampere": "A", "amperes": "A", "amp": "A", "amps": "A",
    "watt": "W", "watts": "W",
    "joule": "J", "joules": "J",
    "coulomb": "C", "coulombs": "C",
    "farad": "F", "farads": "F",
    "henry": "H", "henries": "H", "henrys": "H",
    "tesla": "T", "teslas": "T",
    "weber": "Wb", "webers": "Wb",
    "newton": "N", "newtons": "N",
    "hertz": "Hz",
    "second": "s", "seconds": "s", "sec": "s",
    "meter": "m", "meters": "m", "metre": "m", "metres": "m",
    "gram": "g", "grams": "g",
    "percent": "%",
    "degree": "deg", "degrees": "deg",
    "radian": "rad", "radians": "rad",
}

_SUP_TRANS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def _normalize_unit_atom(atom: str) -> str:
    """Normalize one '/'-separated piece of a unit (e.g. 'Ohms', 'm³', 'μF')."""
    a = atom.strip()
    if not a:
        return a
    # unicode superscript exponents: m³ -> m^3, m⁻³ -> m^-3
    a = re.sub(
        r"([A-Za-z])([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: m.group(1) + "^" + m.group(2).replace("⁻", "-").translate(_SUP_TRANS),
        a,
    )
    a = a.replace("µ", "u").replace("μ", "u")          # micro sign + greek mu -> ASCII u
    a = a.replace("Ω", "ohm").replace("Ω", "ohm")      # U+03A9 greek + U+2126 ohm sign
    a = a.replace("°", "deg")
    # Spelled-out words -> symbols ('Ohm', 'amperes', 'turns/meter' ...)
    low = a.lower()
    if low in _UNIT_WORDS:
        return _UNIT_WORDS[low]
    # prefixed ohm spelled out: 'mOhm', 'kOhms', 'kohm'
    m = re.fullmatch(r"([pnumkMG]?)[oO]hm[s]?", a)
    if m:
        return m.group(1) + "ohm"
    return a


def normalize_unit(unit: object) -> str:
    """Canonical ASCII unit string; every no-unit spelling collapses to 'N/A'.

    >>> normalize_unit(None);  normalize_unit("nan");  normalize_unit("-")
    'N/A', 'N/A', 'N/A'
    >>> normalize_unit("Ohm"); normalize_unit("Ω");    normalize_unit("µF")
    'ohm', 'ohm', 'uF'
    """
    if unit is None:
        return NO_UNIT
    u = str(unit).strip()
    if isinstance(unit, float) and math.isnan(unit):
        return NO_UNIT
    if u.lower() in _NO_UNIT_TOKENS:
        return NO_UNIT
    # multi-value units: "C; J" / "N/A; μF" — normalize each part IN PLACE (positional
    # alignment with the multi-value answer matters); drop only trailing empties ("Ohm;").
    if ";" in u:
        raw_parts = u.split(";")
        while raw_parts and not raw_parts[-1].strip():   # stray trailing ';' ("Ohm;")
            raw_parts.pop()
        parts = [_compound(p).strip() or NO_UNIT for p in raw_parts]
        if not parts or all(p == NO_UNIT for p in parts):
            return NO_UNIT
        return "; ".join(parts)
    out = _compound(u)
    return out if out else NO_UNIT


_NUM_TOKEN_RE = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def _compound(u: str) -> str:
    """Normalize a (possibly '/'-compound) unit: 'turns/meter' -> 'turns/m'.

    Also drops echoed numbers — the model sometimes prints 'UNIT: 120 Ohms' — a real unit
    never contains a bare number token."""
    u = u.strip()
    if u.lower() in _NO_UNIT_TOKENS:
        return NO_UNIT
    tokens = [t for t in u.split() if not _NUM_TOKEN_RE.fullmatch(t)]
    if not tokens:
        return NO_UNIT
    u = " ".join(tokens)
    return "/".join(_normalize_unit_atom(p) for p in u.split("/"))


# --------------------------------------------------------------------------- #
#  answer (value) normalization                                                #
# --------------------------------------------------------------------------- #

_PLAIN_NUM_RE = re.compile(r"^[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?$")

# every "mantissa times ten-to-the" spelling seen in the wild:
#   3 × 10^-6 | 3 x 10^{-6} | 3 * 10^(-6) | 3 \times 10^-6 | 3 · 10^-6 | 3 × 10⁻⁶
_SCI_ANY_RE = re.compile(
    r"^([-+]?\d+(?:\.\d+)?)\s*(?:[x×·*]|\\times)\s*10\s*"
    r"(?:\^?\s*[\{(]?\s*([-+]?\d+)\s*[\})]?|([⁻⁺⁰¹²³⁴⁵⁶⁷⁸⁹]+))\s*$"
)
_BARE_POW_RE = re.compile(r"^([-+]?)\s*10\s*\^\s*[\{(]?\s*([-+]?\d+)\s*[\})]?\s*$")
_SUP_SIGN_TRANS = str.maketrans("⁻⁺⁰¹²³⁴⁵⁶⁷⁸⁹", "-+0123456789")


def _fmt(v: float) -> str:
    """Float -> canonical string: trim trailing zeros, e-notation kept as Python gives it."""
    s = f"{v:.6g}"
    return s


def _normalize_scalar(part: str) -> str:
    """Normalize one scalar answer: numbers -> plain/e-notation, Yes/No cased, text as-is."""
    p = part.strip()
    if not p:
        return p
    # strip $...$ math wrapper
    if p.startswith("$") and p.endswith("$"):
        p = p[1:-1].strip()
    low = p.lower()
    if low in ("yes", "y"):
        return "Yes"
    if low in ("no", "n"):
        return "No"
    # '%' glued onto the value ("3.57143%"): the percent belongs in the unit field
    if p.endswith("%") and _PLAIN_NUM_RE.match(p[:-1].strip()):
        p = p[:-1].strip()
    if _PLAIN_NUM_RE.match(p):
        try:
            return _fmt(float(p))
        except ValueError:
            return p
    m = _SCI_ANY_RE.match(p)
    if m:
        mantissa = float(m.group(1))
        exp = int(m.group(2)) if m.group(2) is not None \
            else int(m.group(3).translate(_SUP_SIGN_TRANS))
        return _fmt(mantissa * 10.0 ** exp)
    m = _BARE_POW_RE.match(p)
    if m:
        sign = -1.0 if m.group(1) == "-" else 1.0
        return _fmt(sign * 10.0 ** int(m.group(2)))
    return p  # free text — leave untouched


def normalize_answer(answer: object) -> str:
    """Canonical answer string for the BTC `answer` field (value only, no unit).

    >>> normalize_answer("5.07 × 10^-6");  normalize_answer("3 * 10^{4}")
    '5.07e-06', '30000'
    >>> normalize_answer("0.6; 1.2");      normalize_answer("yes")
    '0.6; 1.2', 'Yes'
    """
    if answer is None:
        return ""
    if isinstance(answer, float) and math.isnan(answer):
        return ""
    s = str(answer).strip()
    if not s or s.lower() in ("nan", "none", "null"):
        return ""
    if ";" in s:
        parts = [_normalize_scalar(x) for x in s.split(";")]
        return "; ".join(x for x in (x.strip() for x in parts) if x)
    return _normalize_scalar(s)


# --------------------------------------------------------------------------- #
#  inline tests                                                                #
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    cases_unit = [
        (None, "N/A"), ("", "N/A"), ("nan", "N/A"), ("None", "N/A"), ("N/A", "N/A"),
        ("—", "N/A"), ("-", "N/A"), ("dimensionless", "N/A"), ("yes_no", "N/A"),
        ("Yes/No", "N/A"), ("boolean", "N/A"), ("(factor)", "N/A"), ("ratio", "N/A"),
        (";", "N/A"), ("direction", "N/A"),
        ("Ohm", "ohm"), ("Ohms", "ohm"), ("Ω", "ohm"), ("kΩ", "kohm"),
        ("mOhm", "mohm"), ("ohm", "ohm"),
        ("µF", "uF"), ("μC", "uC"), ("uF", "uF"),
        ("V/m", "V/m"), ("N/C", "N/C"), ("mJ", "mJ"), ("kV", "kV"),
        ("J/m³", "J/m^3"), ("J/m^3", "J/m^3"), ("m/s²", "m/s^2"),
        ("turns/meter", "turns/m"), ("turns/m", "turns/m"),
        ("amperes", "A"), ("°C", "degC"), ("°", "deg"),
        ("C; J", "C; J"), ("Ohm;", "ohm"), ("dimensionless; F", "N/A; F"),
        ("N/A; μF", "N/A; uF"), ("N/A; N/A", "N/A"),
    ]
    cases_ans = [
        ("0.702562", "0.702562"), ("512000", "512000"),
        ("3.16228e-05", "3.16228e-05"), ("1e-12", "1e-12"),
        ("5.07 × 10^-6", "5.07e-06"), ("5.07 x 10^{-6}", "5.07e-06"),
        ("3 * 10^{4}", "30000"), ("4 \\times 10^(-3)", "0.004"),
        ("2.5 × 10⁻⁶", "2.5e-06"), ("10^4", "10000"), ("-10^3", "-1000"),
        ("$5.07 \\times 10^{-6}$", "5.07e-06"),
        ("yes", "Yes"), ("No", "No"),
        ("0.6; 1.2", "0.6; 1.2"), ("2.00; 4.00 * 10^-9", "2; 4e-09"),
        ("nan", ""), (None, ""), ("doubled", "doubled"),
        ("0.30000000000004", "0.3"),
    ]
    bad = 0
    for raw, want in cases_unit:
        got = normalize_unit(raw)
        ok = got == want
        bad += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] unit {raw!r} -> {got!r} (want {want!r})")
    for raw, want in cases_ans:
        got = normalize_answer(raw)
        ok = got == want
        bad += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] ans  {raw!r} -> {got!r} (want {want!r})")
    print(f"\n{'ALL PASS' if not bad else f'{bad} FAILURES'}")
