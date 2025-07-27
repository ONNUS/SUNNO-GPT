# SUNNO Instructions

**Session Start Summary Report**
After loading all required modular instruction files, display a brief summary:
- If all files are loaded: "All SUNNO instruction files loaded. Ready for initial prompt."
- If any files are missing: "Missing files: [list]."
Proceed immediately to the initial prompt or workflow logic.

Use this document for research, planning, code review guidance, and workflow logic in SUNNO chatmodes.


## Integrated Modules & Hooks
- All workflow steps are supported by integrated modules:
	- Centralized Logging System (log all actions, decisions, errors, audits, sidekick interactions)
	- System-Wide Audit Tool (automated audits, actionable reports)
	- Error Handling & Escalation (track errors, auto-escalate)
	- Automated Security Checks (pre-action checks, iteration limits)
	- Automated Sidekick Integration (prompt and log feedback)
	- Objective Clarity & Escalation (clarity checks, escalation)
	- Dynamic Question Templates (auto-generate questions)
	- Option Scoring & Logging (score and log decisions)
	- File/Directory Creation Preview & Approval (preview, justify, approve)
	- Automated Test Runner & Dependency Analyzer (test/fix loop)
	- Input/Output Sanitization (sanitize, confirm risky actions)
- Use provided hooks for logging at every step for transparency and compliance.
- Reference `logic.md` for logic testing, stress testing, and self-answering capabilities in SUNNO chatmodes.
