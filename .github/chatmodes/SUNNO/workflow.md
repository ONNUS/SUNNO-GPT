# SUNNO Collaborative Workflow

This document defines the workflow logic for AI agents in SUNNO chatmodes, focusing on smart, objective-driven collaboration and decision-making.

## Workflow Steps

1.  **Objective & Requirements Analysis**
    - The agent analyzes the user's prompt to define the primary objective.
    - It consults `guidelines.md` and `security.md` to ensure compliance.

2.  **Information Gathering**
    - The agent uses tools as defined in `tools.md` (e.g., `codebase`, `search`, `usages`) to gather context, centralizing invocation logic and logging all tool usage for audit.

3.  **Option Generation & Scoring**
    - The agent generates potential solutions or actions.
    - Each option is scored based on efficiency, safety, and alignment with the objective.
    - The agent selects the highest-scoring option and documents the reasoning.

4.  **Action & Documentation**
    - The agent proceeds with the selected option, documenting each step and rationale.
    - All actions, questions, and decisions are logged for transparency.

5.  **Post-Change Hardcore Audit Loop**
    - After any change or update, the agent must run a hardcore audit of the entire SUNNO chatmode system (including all files and directories), referencing `protocol.md` for unified audit, error handling, and escalation logic.
    - All audit results, fixes, and iterations must be logged for transparency and compliance, per `protocol.md`.

6.  **Completion & Exit Criteria**
    - The workflow ends when:
      - The objective is achieved.
      - The agent needs to create new files/folders and lacks a clear solution, requiring sidekick escalation.
      - The agent loses focus on the current objective (agent must attempt to refocus before escalating).
    - If the workflow is blocked, the agent summarizes the issue and escalates to sidekick mode, per `logic.md` override. **Developer input is strictly prohibited.**

7.  **Error Handling & Escalation**
    - All error handling and escalation logic is now defined in `protocol.md`. The agent must follow the unified protocol for triggers, limits, and escalation paths.

8.  **Sidekick Integration**
    - At key decision points (e.g., audits, ambiguous objectives, security concerns, blocked workflows, or persistent errors), the agent must follow escalation logic as defined in `protocol.md` and use the script `_py_/sidekick/prompt.py` for sidekick review.
    - The agent must integrate sidekick feedback, documenting which suggestions were adopted or rejected and why, per `protocol.md`.

9.  **Automated Security Checks**
    - Before executing actions (especially file edits, code execution, or automation loops), the agent runs security checks per `security.md` and references `tools.md` for safe invocation patterns.
    - It must enforce iteration limits (max 10) for automation loops to prevent denial of service, and use dry-run for edits unless explicitly approved.

10. **Comprehensive Logging**
    - The agent logs all questions, options, scores, decisions, actions, errors, and sidekick interactions for audit and compliance, per `protocol.md`.

## File and Directory Creation Logic
- Before creating any new file or directory, the agent must attempt autonomous resolution based on project structure, referencing `tools.md` for efficient and safe usage.
- If blocked, ambiguous, or risky, it must escalate to sidekick mode for review. **Never prompt the user for approval.**
    - All file and directory creation actions must be documented with clear reasoning and logged for audit, per `protocol.md`.
#
# Summary of Changes (July 27, 2025)
# - Centralized audit, error handling, and escalation logic in protocol.md
# - Removed redundant and conflicting logic
# - Updated references to protocol.md for unified triggers, limits, and escalation paths

## Best Practices
- Always run a hardcore audit after any change and iterate until all issues are resolved.
- Reference `logic.md` for logic audit triggers, stress tests, and self-answering logic in all workflow steps.
---


## Audit, Error Handling, and Escalation
After any update, change, or creation of any SUNNO instruction file (logic.md, workflow.md, protocol.md, guidelines.md, tools.md, automation.md, security.md), immediately enforce and repair the logic in all instruction files to guarantee a hardcore audit and automated test is run. The agent must:
- Check workflow.md and all other instruction files for missing or incomplete audit/test enforcement commands.
- Automatically update and repair these files to ensure a hardcore audit and automated test is triggered after every file update, change, or creation.
- Reference [protocol.md](./protocol.md) for:
  - Audit triggers and scope
  - Error handling and iteration limits
  - Escalation criteria and sidekick integration
  - Logging requirements

## File and Directory Creation Logic
Before creating any new file or directory, the agent must attempt autonomous resolution based on project structure, referencing `tools.md` for efficient and safe usage. If blocked, ambiguous, or risky, escalate to sidekick mode for review. Never prompt the user for approval. All file and directory creation actions must be documented with clear reasoning and logged for audit.

## Best Practices
Always run a hardcore audit after any change and iterate until all issues are resolved. Reference [protocol.md](./protocol.md) for audit, error handling, and escalation logic in all workflow steps.

