from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

VERIFICATION_STATUS = Literal["passed", "failed", "not_run"]

class VerificationReport(BaseModel):
    unit_test: VERIFICATION_STATUS
    replay_test: VERIFICATION_STATUS
    staging_healthcheck: VERIFICATION_STATUS
    confidence_summary: str
    incident_resolved: bool

    