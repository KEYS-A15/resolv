from __future__ import annotations

from pydantic import BaseModel, Field

from resolv.contracts.incident import Incident
from resolv.contracts.hypothesis import Hypothesis
from resolv.contracts.plan import RemediationPlan
from resolv.contracts.verification import VerificationReport

class WorkflowState(BaseModel):
    incident: Incident
    classification: str | None = None
    hypotheses: list[Hypothesis] = Field(default_factory=list)
    selected_hypothesis: Hypothesis | None = None
    remediation_plan: RemediationPlan | None = None
    verification_report: VerificationReport | None = None

