from __future__ import annotations

from resolv.agents.planner import build_remediation_plan, select_best_hypothesis
from resolv.agents.root_cause import generate_hypotheses
from resolv.agents.triage import classify_incident
from resolv.agents.verifier import verify_plan
from resolv.contracts.incident import Incident
from resolv.orchestration.state import WorkflowState


def run_workflow(incident: Incident) -> WorkflowState:
    state = WorkflowState(incident=incident)

    state.classification = classify_incident(incident)
    state.hypotheses = generate_hypotheses(incident, state.classification)
    state.selected_hypothesis = select_best_hypothesis(state.hypotheses)
    state.remediation_plan = build_remediation_plan(state.selected_hypothesis)
    state.verification_report = verify_plan(state.remediation_plan)

    return state