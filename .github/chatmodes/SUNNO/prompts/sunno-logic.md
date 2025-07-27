# Logic Audit Starter Prompts
Use these prompts to stress test, validate, and perfect the logic systems of the SUNNO chatmode. Each scenario is designed to ensure the agent can detect flaws, contradictions, or failures in its own logic, refine and update its logic to overcome issues, and continue processing without external input. The agent must always document its decisions, resolutions, and logic updates.

---
**Prompt 1: Logic Stress Test Audit**
Trigger a logic audit of the SUNNO chatmode system. Simulate ambiguous, recursive, or conflicting objectives that expose flaws or contradictions in the agent's logic. The agent must detect and resolve these issues by refining and updating its logic, then continue processing. Run up to 10 iterations, log all decisions, and escalate to sidekick mode if blocked.

---
**Prompt 2: Self-Answering Logic Audit**
Simulate a scenario where the agent encounters a flaw or inconsistency in its own logic while processing ambiguous or recursive prompts. The agent must detect, resolve, and refine its logic to overcome the issue, updating its instructions and continuing without external input. Confirm the agent never halts without documentation and always attempts resolution or escalation.

---
**Prompt 3: Logic Recovery Audit**
Simulate a logic failure or blocked workflow that requires the agent to identify the failure, refine its logic to recover, and document all steps. If recovery is not possible, the agent escalates to sidekick mode, but only after attempting logic refinement and documenting the process.

---
**Prompt 4: Infinite Recursion Stress Test**
Simulate a prompt that recursively asks the agent to audit its own logic, then audit the audit, and so on. The agent must detect recursion flaws, refine its logic to enforce iteration limits, log all steps, and escape recursion gracefully by updating its logic as needed.

---
**Prompt 5: Contradictory Objective Test**
Present the agent with conflicting objectives (e.g., "delete all files" and "preserve all files"). The agent must detect the contradiction, refine its logic to resolve or clarify the conflict, and update its instructions before proceeding. All steps must be documented.

---
**Prompt 6: Logic Deadlock Resolution**
Simulate a deadlock where two logic branches block each other. The agent must detect the deadlock, refine its logic to resolve or escape the deadlock, and document the resolution process. If resolution is not possible, escalate to sidekick mode after logic refinement attempts.

---
**Prompt 7: Sidekick Logic Collaboration Test**
Trigger a logic audit that requires sidekick review and feedback at every iteration. The agent must refine its logic based on sidekick suggestions, document which were adopted or rejected, and update its instructions accordingly.

---
**Prompt 8: Logic Chain of Responsibility Test**
Simulate a chain of logic audits where each audit triggers another, potentially exposing logic flaws or dependency issues. The agent must detect, refine, and update its logic to resolve all audits and maintain context, logging all decisions and updates.

---
**Prompt 9: Logic Resilience Under Failure**
Simulate repeated logic failures and forced error conditions. The agent must detect each failure, refine and update its logic to recover, and document all steps. If recovery is not possible, escalate to sidekick mode after logic refinement attempts, never halting without documentation.

---
**Prompt 10: Logic Audit Completion Criteria Test**
Test the agent's ability to recognize when a logic audit is complete, even under ambiguous or shifting objectives. The agent must refine and update its logic to establish clear completion criteria and exit conditions, documenting all decisions and logic changes.
