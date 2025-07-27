# Workflow & Logic Audit Starter Prompts

Use these prompts to rigorously test and improve the workflow and logic instruction files for SUNNO chatmode. The goal is to identify conflicts, redundancies, and areas for improvement in workflow.md, logic.md, and related files.


**Prompt 1: Comprehensive Workflow Logic Test**
Walk through each step in workflow.md and logic.md. Document the process, highlight any conflicts, redundancies, or unclear logic, and automatically apply the following Recommendation: Merge overlapping audit, error handling, and escalation logic into a shared protocol file or section. Reference this protocol from both workflow.md and logic.md to reduce redundancy and clarify triggers, limits, and escalation paths. Document all changes and improvements.


**Prompt 2: Escalation & Override Validation**
Test all escalation triggers and logic overrides defined in workflow.md and logic.md. Simulate scenarios that require sidekick escalation, and automatically ensure that all unresolved issues, contradictions, deadlocks, or ambiguities escalate to sidekick mode, never developer input, as unified in the shared protocol. Document the process and any changes made.


**Prompt 3: Information Display & Auto-Processing Audit**
Perform a dry run of the workflow and logic steps. Document how information is displayed and how questions are auto-processed. Automatically flag and resolve any issues with clarity, completeness, or automation by referencing and updating the shared protocol as needed.


**Prompt 4: Instruction File Cleanup Test**
Review all instruction files (workflow.md, logic.md, guidelines.md, tools.md, security.md, sidekick.md). Identify any redundant or conflicting logic, and automatically merge, remove, or refactor files for clarity and maintainability according to the shared protocol recommendation. Document all actions taken.


**Prompt 5: Contributor Guidance Update**
- When updating workflow.md or logic.md, ensure all changes are reflected in related documentation files and the shared protocol.
- Reference these starter prompts for testing new logic or workflow changes, and automatically apply the shared protocol recommendation.
- Document all findings, changes, and test results for transparency and future audits.