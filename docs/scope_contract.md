Project Aion — Scope Contract (v1.0)
1) Purpose

Build a repeatable, auditable simulated trading system and operating process that produces a credible track record and supports a go/no-go decision by end of Q2 2026:

Path A: continue building standalone track record

Path B: progress to bankroll partner pathway (DD-ready)

2) Success Criteria (Definition of “Working”)

By the decision gate date, Aion must demonstrate:

Repeatability: same inputs + same configuration → same outputs (reproducible runs)

Auditability: every decision and trade is logged with timestamped lineage (data → labels → logic → output)

Risk Controls: enforced limits and stop conditions with clear breach handling

Operational Readiness: runbook + monitoring + incident tracking exist and are used

Reporting Standard: weekly performance + risk report suitable for external review

3) In Scope (Build Now)

A. Simulated Trading Track Record

Trade generation pipeline (signals → trade candidates → final selections)

Simulation engine (consistent rules, timestamps, market assumptions explicitly stated)

Trade log format that supports audit and later DD review

Performance metrics (ROI, strike rate, drawdown, volatility, exposure, hit-rate by segment)

B. Hidden Merit / VDL Workflow

Capture and maintain “Hidden Merit” / VDL criteria definitions

Manual + semi-automated pipeline for compiling VDL-driven trade candidates

Versioned criteria updates with impact notes

C. Data + Labeling Pipeline (Sri Lanka BPO)

Clear labeling schema + definitions + QA rules

Sampling and spot-check process (accuracy targets and review cadence)

Data lineage: replay source → labeler → timestamp → schema version

D. Expert Systems Layer

Rule/logic modules that consume labeled inputs and produce decision outputs

Version control of decision logic

Evaluation protocol (baseline comparisons, regression checks)

E. Dash PM + Operating Console (MVP-level)

Task/epic tracking, status, owners, dependencies

Artifact linking (reports/logs/versions)

Simple KPI surfaces (runs completed, incidents, weekly metrics)

F. Governance + Controls

Change control log (what changed, why, expected impact)

Incident log (failures, near misses, anomalies)

Access/control notes (who can change logic, who approves changes)

G. Reporting Pack

Weekly performance report (standard template)

Weekly risk report (limits, breaches, exposures, drawdown)

Monthly summary suitable for partner DD “preview”

4) Out of Scope (Not Now)

These are explicitly deferred until after the decision gate unless required for safety/compliance:

Live trading execution at scale (broker integration, live order routing)

High-frequency or latency-optimised systems

Multi-market expansion beyond the initial target markets

Complex UI polish not tied to decision-making or auditability

“Perfect model” optimisation beyond what is needed for repeatable results

Full automation of every workflow (manual steps allowed if logged + controlled)

5) Key Assumptions

Simulated conditions will be transparently defined (timing, prices, slippage assumptions, constraints).

Manual components are acceptable only if logged, versioned, and reviewable.

“If it isn’t logged, it didn’t happen” applies to decisions, trades, and changes.

6) Constraints

Delivery must support credible DD (track record + governance) by end of Q2 2026.

Prefer simplicity and reliability over feature breadth.

Every module must have a Definition of Done and a measurable output.

7) Deliverables (Minimum “Partner-Ready” Set)

Track record pack (method + logs + results + limitations)

Risk policy (limits, stop conditions, breach workflow)

Runbook (daily/weekly operations, roles, escalation)

Architecture diagram (data → labels → expert layer → output → reporting)

Model/governance notes (versions, datasets, evaluation protocol)

8) Decision Gate (End of Q2 2026)

At the gate, we choose:

A: continue extending track record + incremental automation

B: initiate bankroll partner DD process using deliverables above
