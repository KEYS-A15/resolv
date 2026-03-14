from __future__ import annotations

import json
from pathlib import Path

from resolv.contracts.incident import Incident
from resolv.orchestration.workflow import run_workflow

def test_latency_spiral_workflow() -> None:
    seed_path = Path(__file__).parent.parent / "src" / "resolv" / "scenarios" / "latency_spiral" / "incident_seed.json"
    
    incident = Incident.model_validate(json.loads(seed_path.read_text(encoding="utf-8")))
    state = run_workflow(incident)

    assert state.classification == "application_config_regression"
    assert state.selected_hypothesis is not None
    assert state.remediation_plan is not None
    assert state.verification_report is not None
    assert state.verification_report.incident_resolved is True