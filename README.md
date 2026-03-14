# Resolv

**Resolv** is an agentic AI DevOps and SRE system that turns incidents into safe, reviewable, and verifiable fixes.

*Built for **Azure AI Dev Days 2026**, Resolv detects an incident, diagnoses the likely root cause, proposes a remediation plan, generates a patch artifact, verifies the fix through replayable evidence, and produces an audit-ready incident summary.*

## Why this project exists

Modern incident response is slow, manual, and hard to verify. Resolv is disigned to reduce mean time to resolution (MTTR) by combining agentic reasoning, strucutred planning, verification loops, and Azure-Native deployment patterns.

## Core Flow

1. Detect incident signals
2. Classify and triage the failure
3. Rank root-cause hypothesis
4. Generate a remediation plan
5. Produce a patch artifact / PR-ready change set
6. Run verification and replay checks
7. Generate an audit trail and postmortem summary

## Run locally
*Built using uv*

`uv run resolv`
`uv run pytest`
