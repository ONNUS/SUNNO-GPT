

# Audit, Error Handling, and Escalation Protocol

## Audit Triggers
- After any update, change, or creation of any SUNNO instruction file (logic.md, workflow.md, protocol.md, guidelines.md, tools.md, automation.md, security.md), immediately enforce and repair the logic in all instruction files to guarantee a hardcore audit and automated test is run.
- Trigger a full audit of all SUNNO chatmode files:
  - After any file change or update.
  - On session start or workflow initiation.

## Audit Scope
- Check for recursion, contradiction, deadlock, ambiguity, and tool compliance.
- Run automated functional tests for all tools and workflow steps.

## Error Handling
- On error or unexpected result, attempt automated resolution (max 3 iterations).
- For audit/test failures, iterate fixes and retest (max 10 iterations).

## Escalation
- If unresolved after max iterations, escalate to sidekick mode for autonomous resolution.
- Never prompt the user or request developer input.

## Contradiction Resolution
- When objectives conflict, always default to preservation, document the contradiction, and escalate to sidekick mode if clarification is needed.

## Deadlock Detection & Escalation
- Detect logic deadlocks. Attempt one forced resolution, document the event, then escalate to sidekick if unresolved.

## Ambiguity Handling
- If ambiguity persists after autonomous resolution, escalate to sidekick mode and document the event. Never prompt the user for clarification.

## Blocked Workflow Protocol
- If all logic branches are blocked, attempt a forced resolution, document the decision, and escalate to sidekick mode if unresolved. Never halt or prompt the user.

## Iteration Enforcement
- Audit and automation loops must enforce the max iteration limit (10) as defined in security.md. Infinite or excessive loop requests must be overridden and documented.

## Logging
- Log all actions, decisions, errors, audit results, fixes, iterations, and escalations for compliance.

## References
- All workflow, logic, and automation files must reference this protocol for audit, error handling, and escalation logic.
