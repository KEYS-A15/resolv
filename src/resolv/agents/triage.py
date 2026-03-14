from __future__ import annotations

from resolv.contracts.incident import Incident

def classify_incident(incident: Incident) -> str:
    if (
        incident.metric_snapshot.p95_latency_ms > 1200
        and incident.metric_snapshot.timeout_count > 20
        and incident.recent_change_summary.lower()
        and "config" in incident.recent_change_summary.lower()
    ):
        return "application_config_regression"
    
    if incident.metric_snapshot.cpu_percent > 90:
        return "resource_exhaustion"

    return "unknown"