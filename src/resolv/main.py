from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

from resolv.contracts.incident import Incident
from resolv.orchestration.workflow import run_workflow

app = typer.Typer(help="Resolv MVP CLI")
console = Console()


def load_seed_incident() -> Incident:
    seed_path = (
        Path(__file__).parent / "scenarios" / "latency_spiral" / "incident_seed.json"
    )
    data = json.loads(seed_path.read_text(encoding="utf-8"))
    return Incident.model_validate(data)


@app.command()
def run_scenario(name: str = "latency_spiral") -> None:
    if name != "latency_spiral":
        raise typer.BadParameter("Only 'latency_spiral' is implemented in phase 1.")

    incident = load_seed_incident()
    state = run_workflow(incident)

    console.print(Panel.fit(f"[bold red]Incident[/bold red]\n{incident.title}"))
    console.print(f"[bold]Service:[/bold] {incident.service_name}")
    console.print(f"[bold]Severity:[/bold] {incident.severity}")
    console.print(f"[bold]Classification:[/bold] {state.classification}\n")

    console.print("[bold cyan]Top Hypothesis[/bold cyan]")
    console.print(f"- {state.selected_hypothesis.summary}")
    console.print(f"- Confidence: {state.selected_hypothesis.confidence_percent}")

    console.print("\n[bold green]Remediation Plan[/bold green]")
    console.print(f"- Action: {state.remediation_plan.action_type}")
    console.print(f"- Summary: {state.remediation_plan.summary}")
    for step in state.remediation_plan.steps:
        console.print(f"  • {step}")

    console.print("\n[bold magenta]Verification[/bold magenta]")
    console.print(f"- Unit tests: {state.verification_report.unit_test}")
    console.print(f"- Replay test: {state.verification_report.replay_test}")
    console.print(f"- Staging healthcheck: {state.verification_report.staging_healthcheck}")
    console.print(f"- Resolved: {state.verification_report.incident_resolved}")
    console.print(f"- Confidence: {state.verification_report.confidence_summary}")


if __name__ == "__main__":
    app()