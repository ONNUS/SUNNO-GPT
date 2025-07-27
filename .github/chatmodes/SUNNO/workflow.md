# SUNNO Collaborative Workflow

This document defines the workflow logic for AI agents in SUNNO chatmodes, focusing on smart, objective-driven collaboration and decision-making.

## Workflow Steps

   - The agent selects the highest-scoring option and documents the reasoning.

4. **Action & Documentation**
   - The agent proceeds with the selected option, documenting each step and rationale.
   - All actions, questions, and decisions are logged for transparency.

5. **Post-Change Hardcore Audit Loop**
   - After any change or update, the agent must run a hardcore audit of the entire SUNNO chatmode system (including all files and directories).
   - If the audit finds any issues, the agent must iterate: fix the issues, re-run the audit, and repeat until the audit passes with no issues.
   - All audit results, fixes, and iterations must be logged for transparency and compliance.

6. **Completion & Exit Criteria**
   - The workflow ends when:
     - The objective is achieved.
     - The agent needs to create new files/folders and lacks a clear solution.
     - The agent loses focus on the current objective (should be avoided; agent must refocus or escalate).
   - If the workflow is blocked, the agent summarizes the issue and requests developer input.

7. **Error Handling & Escalation**
   - If an error or unexpected result occurs, the agent documents the issue and attempts automated resolution.
   - If unresolved after 3 iterations, escalate to sidekick mode or request developer input.

8. **Sidekick Integration**
   - At key decision points (e.g., audits, ambiguous objectives, security concerns), the agent prompts a sidekick AI for review and suggestions.
   - Integrate sidekick feedback, documenting which suggestions were adopted or rejected and why.

9. **Automated Security Checks**
   - Before executing actions (especially file edits, code execution, or automation loops), run security checks per `security.md`.
   - Enforce iteration limits (max 5) for automation loops to prevent denial of service.
   - Log all tool invocations and changes for auditability.

10. **Comprehensive Logging**
   - Log all questions, options, scores, decisions, actions, errors, and sidekick interactions.
   - Ensure logs are accessible for review and compliance.

5. **Completion & Exit Criteria**
   - The workflow ends when:
     - The objective is achieved.
     - The agent needs to create new files/folders and lacks a clear solution.
     - The agent loses focus on the current objective (should be avoided; agent must refocus or escalate).
   - If the workflow is blocked, the agent summarizes the issue and requests developer input.

6. **Error Handling & Escalation**
   - If an error or unexpected result occurs, the agent documents the issue and attempts automated resolution.
   - If unresolved after 3 iterations, escalate to sidekick mode or request developer input.

7. **Sidekick Integration**
At key decision points (e.g., audits, ambiguous objectives, security concerns), the agent must use the script `_py_/sidekick_prompt.py` to:
   - Generate a markdown code block prompt for sidekick review (using `generate_sidekick_prompt`).
   - Log the prompt and sidekick response (using `log_sidekick_response`).
   - Integrate sidekick feedback, documenting which suggestions were adopted or rejected and why.
Example usage:
```python
from ._py_.sidekick_prompt import generate_sidekick_prompt, log_sidekick_response
prompt = generate_sidekick_prompt(context, decision, questions)
# Send prompt to sidekick, receive response
log_sidekick_response(prompt, response)
```

8. **Automated Security Checks**
   - Before executing actions (especially file edits, code execution, or automation loops), run security checks per `security.md`.
   - Enforce iteration limits (max 5) for automation loops to prevent denial of service.
   - Log all tool invocations and changes for auditability.

9. **Comprehensive Logging**
   - Log all questions, options, scores, decisions, actions, errors, and sidekick interactions.
   - Ensure logs are accessible for review and compliance.

## File and Directory Creation Logic
Before creating any new file or directory, the agent must:
 - Prompt the user with a clear overview of all proposed files and directories to be created, including the reason for each and the selected location.
 - Justify the location for each file or directory based on project structure, context, and user intent.
 - If multiple files or directories are needed, present a single prompt listing all items, reasons, and locations, and request user approval before proceeding.
 - Bypass this prompt only if the user provides an explicit file or directory location in their request.
 - Document all file and directory creation actions and reasoning for transparency.

## Best Practices
- After any change or update, always run a hardcore audit and iterate until all issues are resolved before proceeding.
- Reference `logic.md` for logic audit triggers, stress tests, and self-answering logic in all workflow steps.

