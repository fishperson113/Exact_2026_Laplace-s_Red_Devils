# FOL_Z3 Pipeline — Entry point
# Pipeline: FOL Model → Z3 Solver → QA Model → JSON {answer, explanation}
#
# Usage:
#   from models.FOL_Z3 import FOLz3Pipeline
#   pipe = FOLz3Pipeline.from_yaml("configs/fol_z3.yaml")
#   result = pipe.run(premises_nl=[...], question="...")

from .pipeline import FOLz3Pipeline, PipelineResult, TimingLog

__all__ = ["FOLz3Pipeline", "PipelineResult", "TimingLog"]
