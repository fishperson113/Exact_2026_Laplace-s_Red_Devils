"""Cài đặt editable: pip install -e . (thêm package dưới src/)."""
from setuptools import find_packages, setup

setup(
    name="logic-based-educational-queries",
    version="0.1.0",
    description="EXACT 2026 — Logic_Based_Educational_Queries (EDA + SFT)",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
)
