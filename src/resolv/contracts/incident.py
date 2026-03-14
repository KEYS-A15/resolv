from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

SEVERITY = Literal["low", "medium", "high", "critical"]

class MetricSnapshot(BaseModel):
    p95_latency_ms: float = Field(..., ge=0)
    error_rate_percent: float = Field(..., ge=0, le=100)
    cpu_percent: float = Field(..., ge=0, le=100)
    memory_percent: float = Field(..., ge=0, le=100)
    timeout_count: int = Field(..., ge=0)

class Incident(BaseModel):
    incident_id: str
    title: str
    service_name: str
    environment: Literal["production", "staging", "development"]
    severity: SEVERITY
    symptom_summary: str
    suspected_category: str | None = None
    recent_change_summary: str | None = None
    logs: list[str] = Field(default_factory=list)
    metric_snapshot: MetricSnapshot