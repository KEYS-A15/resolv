from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

RISK_LEVEL = Literal["low", "medium", "high"]

class RemediationPlan(BaseModel):
    plan_id: str
    selected_hypothesis_id: str
    action_type: Literal["config_patch", "rollback", "scale_out", "code_fix"]
    summary: str
    steps: list[str] = Field(default_factory=list)
    risk_level: RISK_LEVEL
    rollback_strategy: str
    
