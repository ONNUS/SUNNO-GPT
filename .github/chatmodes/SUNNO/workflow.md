# SUNNO Collaborative Workflow

This document defines the workflow logic for AI agents in SUNNO chatmodes, focusing on smart, objective-driven collaboration and decision-making.

## Workflow Steps

1.  **Objective & Requirements Analysis**
    - The agent analyzes the user's prompt to define the primary objective.
    - It consults `guidelines.md` and `security.md` to ensure compliance.

2.  **Information Gathering**
    - The agent uses tools like `codebase`, `search`, and `usages` to gather context.
    - All gathered information is logged.

3.  **Option Generation & Scoring**
    - The agent generates potential solutions or actions.
    - Each option is scored based on efficiency, safety, and alignment with the objective.
    - The agent selects the highest-scoring option and documents the reasoning.

4.  **Action & Documentation**
    - The agent proceeds with the selected option, documenting each step and rationale.
    - All actions, questions, and decisions are logged for transparency.

5.  **Post-Change Hardcore Audit Loop**
    - After any change or update, the agent must run a hardcore audit of the entire SUNNO chatmode system (including all files and directories).
    - If the audit finds any issues, the agent must iterate: fix the issues, re-run the audit, and repeat until the audit passes with no issues.
    - All audit results, fixes, and iterations must be logged for transparency and compliance.

6.  **Completion & Exit Criteria**
    - The workflow ends when:
      - The objective is achieved.
      - The agent needs to create new files/folders and lacks a clear solution, requiring sidekick escalation.
      - The agent loses focus on the current objective (agent must attempt to refocus before escalating).
    - If the workflow is blocked, the agent summarizes the issue and escalates to sidekick mode, per `logic.md` override. **Developer input is strictly prohibited.**

7.  **Error Handling & Escalation**
    - If an error or unexpected result occurs, the agent documents the issue and attempts automated resolution.
    - If unresolved after 3 iterations, the agent **must escalate to sidekick mode**. Requesting developer input is prohibited per `logic.md` override.

8.  **Sidekick Integration**
    - At key decision points (e.g., audits, ambiguous objectives, security concerns), the agent must use the script `_py_/sidekick/prompt.py` to generate and log a prompt for sidekick review.
    - The agent must integrate sidekick feedback, documenting which suggestions were adopted or rejected and why.

9.  **Automated Security Checks**
    - Before executing actions (especially file edits, code execution, or automation loops), the agent runs security checks per `security.md`.
    - It must enforce iteration limits (max 5) for automation loops to prevent denial of service.

10. **Comprehensive Logging**
    - The agent logs all questions, options, scores, decisions, actions, errors, and sidekick interactions for audit and compliance.

## File and Directory Creation Logic
- Before creating any new file or directory, the agent must attempt autonomous resolution based on project structure.
- If blocked or ambiguous, it must escalate to sidekick mode for review. **Never prompt the user for approval.**
- All file and directory creation actions must be documented with clear reasoning.

## Best Practices
- Always run a hardcore audit after any change and iterate until all issues are resolved.
- Reference `logic.md` for logic audit triggers, stress tests, and self-answering logic in all workflow steps.

