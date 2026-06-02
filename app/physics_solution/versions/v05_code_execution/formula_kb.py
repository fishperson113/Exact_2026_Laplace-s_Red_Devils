"""v05 Formula Knowledge Base — loads formulas.yaml and returns formatted hints per domain."""

from __future__ import annotations

from pathlib import Path

import yaml

_FORMULAS_PATH = Path(__file__).parent / "input" / "formulas.yaml"
_cache: dict | None = None


def _load() -> dict:
    global _cache
    if _cache is None:
        with open(_FORMULAS_PATH, encoding="utf-8") as f:
            _cache = yaml.safe_load(f)
    return _cache


_FORMULA_DOMAIN_MAP = {
    "LDDT": ["LD", "DT"],
    "CH": ["CH", "CHLT"],
}


def get_formula_hints(domain: str) -> str:
    """Return a formatted string of formula hints for the given domain.

    This string will be injected into the code-generation prompt.
    Merged domains (LDDT, CH) combine hints from their constituent YAML keys.
    If domain is unknown, return hints for LD.
    """
    data = _load()

    yaml_keys = _FORMULA_DOMAIN_MAP.get(domain, [domain])
    merged: dict = {}
    for key in yaml_keys:
        section = data.get(key, {})
        for field in ("unit_conversions", "formulas"):
            merged.setdefault(field, [])
            merged[field].extend(section.get(field, []))
    if not merged.get("formulas"):
        merged = data.get("LD", {})

    domain_data = merged

    parts: list[str] = []

    # Unit conversions
    conversions = domain_data.get("unit_conversions", [])
    if conversions:
        parts.append("\nUnit conversions:")
        parts.append("  " + ", ".join(conversions))

    # Formulas
    formulas = domain_data.get("formulas", [])
    if formulas:
        parts.append("\nFormulas:")
        for i, f in enumerate(formulas, 1):
            line = f"  {i}. {f['name']}: {f['formula']}"
            if f.get("result_unit"):
                line += f" -> result in {f['result_unit']}"
            if f.get("notes"):
                line += f"  ({f['notes']})"
            parts.append(line)

    return "\n".join(parts)


if __name__ == "__main__":
    data = _load()
    for domain in data:
        print(f"\n{'='*60}")
        print(f"  Domain: {domain}")
        print(f"{'='*60}")
        print(get_formula_hints(domain))
