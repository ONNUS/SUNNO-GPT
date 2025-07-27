
# Automation

- For every debug prompt, analyze errors using the `problems` tool.
- Apply necessary edits using `changes` and `editFiles`, referencing `tools.md` for invocation patterns and always using dry-run unless explicitly approved.
- After debugging, automatically run all tests using `runTests`.
- If any test fails, loop: fix issues, re-run tests until all pass, enforcing iteration limits (max 10) from `security.md`.
- Confirm deletions before running terminal commands, and escalate to sidekick mode for ambiguous or risky actions.
- Always analyze dependencies using `usages` before making edits, and log all tool invocations for audit.
- Summarize workspace structure using `codebase` for context, referencing `tools.md` for efficient usage.
- Use file search (`search`) to locate files for migration or removal, centralizing invocation logic per `tools.md`.
- Reference reusable guidelines from shared MD files as needed.
- If requirements are unclear, errors persist after 3 iterations, or workflow is blocked, escalate to sidekick mode for autonomous resolution per `logic.md` and `workflow.md`.
- Reference `workflow.md` for workflow logic and automation steps, and always run a hardcore audit after any change, iterating until all issues are resolved.
