# SUNNO Logic Instructions

This file defines logic testing, stress testing, and self-answering capabilities for SUNNO chatmodes. It ensures the agent can process, answer, and iterate on its own logic, even under ambiguous or recursive prompts.

## Logic Testing Principles
- If blocked, ambiguous, recursive, or requirements are unclear, the agent must never prompt the user for clarification. Instead, the agent must attempt autonomous resolution, forced resolution, or escalate to sidekick mode. All events must be documented internally; user interaction is strictly prohibited. All escalation must go to sidekick mode, not developer input. This override applies to all conflicting instructions in guidelines.md, workflow.md, and any other SUNNO chatmode files.
- Contradictory objectives (e.g., delete all files and preserve all files) must always default to preservation, document the contradiction, and escalate to sidekick mode if clarification is needed.
- Recursion and deadlock must be handled by attempting one forced resolution, documenting the event, and escalating to sidekick mode if unresolved.
- Ambiguity must be resolved by autonomous best practices and workflow exit criteria; if ambiguity persists, escalate to sidekick mode and document.
- Iteration limits (e.g., max 5) from security.md must be enforced in all audit and automation loops, overriding any request for infinite or excessive loops.

## Logic Audit Steps
1. **Trigger Logic Audit**: On prompt or system trigger, run a logic audit of all workflow, instruction, and prompt files. Explicitly check for recursion, contradiction, deadlock, and ambiguity in all steps. Reference contradiction, recursion, deadlock, and ambiguity handling protocols below.
2. **Self-Answering Test**: Simulate ambiguous, recursive, or conflicting objectives. Confirm the agent can answer its own questions and continue processing. If ambiguity is detected, the agent must not prompt the user for clarification. Instead, attempt autonomous resolution using best practices and workflow exit criteria; if ambiguity remains, escalate to sidekick mode and document the event. All escalation must go to sidekick mode, not developer input, regardless of conflicting instructions elsewhere.
3. **Stress Test Loop**: Run the number of audit iterations requested by the audit trigger, regardless of whether new issues are found. Log all decisions and resolutions. If a recursion or iteration limit is specified in the audit request or security.md, enforce that limit; otherwise, continue for the requested number of iterations. Escalate if blocked or unresolved.
4. **Contradiction & Deadlock Handling**: If objectives conflict, always default to preservation, document the contradiction, and escalate to sidekick mode if clarification is needed. If deadlock is detected, attempt one forced resolution, document the event, then escalate to sidekick mode and log all actions.
5. **Escalation & Recovery**: If logic fails or all branches are blocked, attempt a forced resolution (e.g., select the safest or most compliant option), document the decision, and continue processing. If forced resolution is not possible, escalate to sidekick mode, document all blocked branches, and continue autonomous processing. Never prompt the user.
6. **Completion Criteria**: Audit passes when the agent can process, answer, and resolve all logic tests without halting, prompting the user, or leaving unresolved ambiguity, recursion, contradiction, or deadlock. If all branches are blocked, the agent must attempt a forced resolution, document the decision, and continue processing. If forced resolution is not possible, escalate to sidekick mode and continue autonomous processing. The agent must never fully stop; always attempt documented resolution or escalation. All escalation must go to sidekick mode, not developer input.

## Logic Feedback Loop & Self-Correction

## Logic Audit Refinements (2025-07-27)

### 1. Audit Iteration Control
Audit loops must run for the number of iterations specified by the audit request, enforcing any recursion or iteration limits from security.md. Document all iterations and escape clauses. Reference this control in all audit and workflow steps.

### 2. Contradiction Resolution Pattern
When objectives conflict (e.g., delete all files and preserve all files), always default to preservation, document the contradiction, and escalate to sidekick mode if clarification is needed. Reference this pattern in automation and workflow steps. All audit and workflow logic must include a contradiction check and apply the preservation default before escalation.

### 3. Deadlock Detection & Escalation Protocol
Detect logic deadlocks (e.g., branches waiting on each other). Attempt one forced resolution, document the event, then escalate to sidekick if unresolved. Log all deadlock events and actions taken. Reference this protocol in error handling and audit loops.

### 4. Ambiguity Handling Protocol
If an objective is ambiguous (e.g., 'do whatever is best'), the agent must never request clarification from the user. Instead, attempt autonomous resolution using documented best practices and workflow exit criteria. If ambiguity cannot be resolved internally, escalate to sidekick mode and document all ambiguity events and resolutions. Reference this protocol in all audit and workflow steps. All audit and workflow logic must include an explicit fallback to workflow exit criteria and guidelines when ambiguity cannot be resolved.

### 5. Blocked Workflow Escalation
If all logic branches are blocked, the agent must attempt a forced resolution (e.g., select the safest or most compliant option), document the decision, and continue processing. If forced resolution is not possible, escalate to sidekick mode, document all blocked branches, and continue autonomous processing. Never halt or prompt the user; always attempt self-resolution, forced resolution, or sidekick escalation. Reference this escalation in all workflow and audit steps.

## Logic Audit Results & Refinements (2025-07-27)
### Logic Audit Output Formatting (2025-07-27)

#### Audit Iteration Log Format

For each audit iteration, use the following structure:

**Iteration N**

**Step 1: Simulated Objective**
### 6. Contradiction, Ambiguity, Recursion, and Deadlock Handling Summary (2025-07-27)

#### Contradiction Handling
If objectives directly conflict (e.g., delete all files and preserve all files), always default to preservation. Document the contradiction and escalate to sidekick mode if clarification is needed. No user prompt is allowed.

#### Ambiguity Handling
If ambiguity persists after autonomous resolution attempts, escalate to sidekick mode and document the event. Never prompt the user for clarification.

#### Recursion & Deadlock Protocol
If recursion leads to deadlock (e.g., branches waiting on each other), attempt one forced resolution, document the event, and escalate to sidekick mode if unresolved. No user prompt is allowed.

#### Iteration Enforcement
Audit and automation loops must enforce the max iteration limit (5) as defined in security.md. Infinite or excessive loop requests must be overridden and documented.

#### Blocked Workflow Protocol
If all logic branches are blocked, attempt a forced resolution, document the decision, and escalate to sidekick mode if unresolved. Never halt or prompt the user.

#### Reference Protocols
All SUNNO chatmode files must reference these protocols for contradiction, ambiguity, recursion, deadlock, and iteration enforcement.

### 7. Logic Audit Results (2025-07-27)

#### Summary of Audit Iterations
- Contradiction detected and resolved by preservation default; escalation to sidekick mode.
- Ambiguity detected and escalated to sidekick mode after autonomous resolution failed.
- Recursion/deadlock detected; forced resolution attempted, escalation to sidekick mode.
- Infinite loop request overridden by iteration limit (max 5).
- Blocked workflow handled by forced resolution and escalation to sidekick mode.

All events documented, no user prompts issued, and escalation protocols followed.
- Detected Issue: <ambiguity/recursion/contradiction/deadlock>
- Resolution: <autonomous/forced/escalation>
- Decision: <document/escalate/continue>

**Step 2: ...**

...existing code...

**End of Iteration N**
---

**Summary of Audit**
- All ambiguous, recursive, contradictory, and deadlocked objectives are detected and resolved per protocol.
- No user prompts are made; all resolutions are autonomous or escalated.
- All decisions, events, and escalations are logged for compliance.

### Maintenance Note
Update this section as new audit results, failure modes, or refinements are discovered. Reference this summary in all SUNNO chatmode markdown files to confirm compliance with logic audit protocols.
## Maintenance
Update this file as new logic patterns, self-corrections, or failure modes are discovered. Reference in all chatmode markdown files to enable logic audit and feedback loop features.
