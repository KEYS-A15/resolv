from __future__ import annotations

from resolv.contracts.hypothesis import Hypothesis
from resolv.contracts.incident import Incident

def generate_hypotheses(incident: Incident, classification: str) -> list[Hypothesis]:
    hypotheses: list[Hypothesis] = []

    if classification == "application_config_regression":
        hypotheses.append(
            Hypothesis(
                hypothesis_id="hyp-01",
                summary="Retry/backoff configuration regression is causing amplified timeout cascades.",
                confidence_percent=0.85,
                evidence=[
                    f'Recent change mentions: {incident.recent_change_summary}',
                    f'p95 latency is elevated at {incident.metric_snapshot.p95_latency_ms} ms',
                    f'Timeout count is elevated at {incident.metric_snapshot.timeout_count}',
                ],
            )
        )
    
    if not hypotheses:
        hypotheses.append(
            Hypothesis(
                hypothesis_id="hyp-999",
                summary="No strong root-cause hypothesis identified",
                confidence_percent=0.20,
                evidence=["Insufficient discriminating signals in the seeded incident."],
            )
        )
    
    return hypotheses