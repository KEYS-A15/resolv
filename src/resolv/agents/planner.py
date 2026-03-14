from __future__ import annotations

from resolv.contracts.hypothesis import Hypothesis
from resolv.contracts.plan import RemediationPlan

def select_best_hypothesis(hypotheses: list[Hypothesis]) -> Hypothesis:
    return max(hypotheses, key=lambda h: h.confidence_percent)

def build_remediation_plan(hypothesis: Hypothesis) -> RemediationPlan:
    if "Retry/backoff" in hypothesis.summary or "configuration" in hypothesis.summary.lower():
        return RemediationPlan(
            plan_id="plan-001",
            selected_hypothesis_id=hypothesis.hypothesis_id,
            action_type="config_patch",
            summary="Patch retry/backoff configuration and add regression coverage.",
            steps=[
                "Reduce aggressive retry count.",
                "Restore exponential backoff values.",
                "Add regression test for timeout storm scenario.",
            ],
            risk_level="low",
            rollback_strategy="Revert generated config patch commit.",
        )
    
    return RemediationPlan(
        plan_id="plan-999",
        selected_hypothesis_id=hypothesis.hypothesis_id,
        action_type="rollback",
        summary="Fallback to safe rollback due to uncertain diagnosis.",
        steps=[
            "Rollback most recent risky service change.",
            "Re-run smoke checks.",
        ],
        risk_level="medium",
        rollback_strategy="Re-apply rollback target revision if needed.",
    )