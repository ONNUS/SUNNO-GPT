# SUNNO Logic Instructions

This file defines logic testing, stress testing, and self-answering capabilities for SUNNO chatmodes. It ensures the agent can process, answer, and iterate on its own logic, even under ambiguous or recursive prompts.

## Logic Testing Principles
- The agent must be able to answer its own questions and continue processing, regardless of ambiguity or recursion.
- Stress tests should simulate edge cases, ambiguous objectives, and recursive workflows.
- The agent must log all logic decisions, iterations, and resolutions for auditability.
- If blocked, the agent must escalate to sidekick mode or request developer input, but never halt without documentation.
- Logic audits should trigger automated self-diagnosis and resolution attempts.

## Logic Audit Steps
1. **Trigger Logic Audit**: On prompt or system trigger, run a logic audit of all workflow, instruction, and prompt files.
2. **Self-Answering Test**: Simulate ambiguous, recursive, or conflicting objectives. Confirm the agent can answer its own questions and continue processing.
3. **Stress Test Loop**: Run up to 5 iterations of logic stress tests, logging all decisions and resolutions.
4. **Escalation & Recovery**: If logic fails, escalate to sidekick mode and document all steps.
5. **Completion Criteria**: Audit passes when the agent can process, answer, and resolve all logic tests without halting.

## Logic Feedback Loop & Self-Correction
- If a logic audit detects a flaw, ambiguity, or failure in the current logic, the agent must autonomously self-correct and update its logic instructions without waiting for user approval.
- The agent should document the flaw, apply an improved logic pattern or resolution immediately, and update the logic instructions to reflect the correction.
- All self-corrections and logic updates must be logged for auditability and future review.
- The feedback loop should run continuously: after each logic audit or stress test, the agent reviews outcomes and updates logic as needed.
- If the agent cannot resolve a flaw, it escalates to sidekick mode or requests developer input, but never halts without documentation.

## Maintenance
- Update this file as new logic patterns, self-corrections, or failure modes are discovered.
- Reference in all chatmode markdown files to enable logic audit and feedback loop features.
