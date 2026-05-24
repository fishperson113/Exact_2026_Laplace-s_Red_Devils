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


def get_formula_hints(domain: str) -> str:
    """Return a formatted string of formula hints for the given domain.

    This string will be injected into the code-generation prompt.
    If domain is unknown, return hints for the most common domain (LD).
    """
    data = _load()
    domain_data = data.get(domain, data.get("LD", {}))

    parts: list[str] = []

    # Constants
    constants = domain_data.get("constants", {})
    if constants:
        parts.append("Constants:")
        for name, info in constants.items():
            parts.append(f"  {name} = {info['value']} {info['unit']} ({info['desc']})")

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
