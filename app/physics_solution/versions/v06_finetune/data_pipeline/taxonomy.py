"""Canonical domain taxonomy for v06 data prep.

The golden CSV uses 8 id prefixes (LD, DT, CH, CHLT, NL, TD, DDT, THCB), but
the competition + classifier work in 6 domains. The prefix->domain map is the
SAME one the router already uses, so we reuse it here rather than redefine:

    LD, DT  -> LDDT   (electrostatics: Coulomb force / E field / potential)
    CHLT    -> CH     (AC/RLC circuits, incl. yes/no resonance)
    DDT     -> DDT    (induction / solenoids)  -- NB distinct from DT!
    CH, NL, TD, THCB  -> themselves

The id-prefix regex is greedy on uppercase, so "DDT142"->"DDT" and "DT098"->"DT"
(and "CHLT015"->"CHLT" vs "CH197"->"CH") disambiguate correctly before aliasing.
"""

from __future__ import annotations

import re

from app.physics_solution.shared.router import _DOMAIN_ALIASES, VALID_DOMAINS

_PREFIX_RE = re.compile(r"^([A-Z]+)")

# Canonical 6 competition domains (re-exported for callers that build splits).
CANONICAL_DOMAINS = tuple(sorted(VALID_DOMAINS))


def id_prefix(qid: str) -> str | None:
    """Leading uppercase prefix of a question id, e.g. 'DT098' -> 'DT'."""
    m = _PREFIX_RE.match(str(qid).strip())
    return m.group(1) if m else None


def domain_from_id(qid: str) -> str | None:
    """Map a question id to its canonical 6-way domain, or None if unknown.

    >>> domain_from_id("DT098"), domain_from_id("LD343"), domain_from_id("CHLT015")
    ('LDDT', 'LDDT', 'CH')
    >>> domain_from_id("DDT142")
    'DDT'
    """
    prefix = id_prefix(qid)
    if prefix is None:
        return None
    domain = _DOMAIN_ALIASES.get(prefix, prefix)
    return domain if domain in VALID_DOMAINS else None


def canonicalize_domain(domain: str) -> str | None:
    """Map any raw domain/prefix string to a canonical domain, or None."""
    d = str(domain).strip()
    d = _DOMAIN_ALIASES.get(d, d)
    return d if d in VALID_DOMAINS else None
