# AgentEval Mini — Functional Demo
This repository contains a lightweight, end-to-end evaluation demo for AI agents, focused on identifying subtle failure modes such as missed context, hallucinations, and inappropriate confidence.
The demo reflects real-world agent evaluation practices: defining success criteria by agent type, designing failure-mode–based tests, combining multiple graders, and producing actionable quality reports.
## What this demo shows
- How to define what “good” means for different agent types (e.g., research advisor vs. interview agent)
- Evaluation tasks designed around realistic failure modes, not just happy paths
- Multiple grader types:
  - Rule-based checks
  - Confidence and groundedness heuristics
  - LLM-as-judge stub (with clear calibration hooks)
- Transcript-level review and failure pattern identification
- Clear, human-readable quality reports
## Repository structure
