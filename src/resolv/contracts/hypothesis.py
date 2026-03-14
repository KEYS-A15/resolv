from __future__ import annotations

from pydantic import BaseModel, Field

class Hypothesis(BaseModel):
    hypothesis_id: str
    summary: str
    confidence_percent: float = Field(..., ge=0.0, le=1.0)
    evidence: list[str] = Field(default_factory=list)