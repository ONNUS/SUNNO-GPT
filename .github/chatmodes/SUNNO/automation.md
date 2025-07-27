# Automation

- For every debug prompt, analyze errors using the `problems` tool.
- Apply necessary edits using `changes` and `editFiles`.
- After debugging, automatically run all tests using `runTests`.
- If any test fails, loop: fix issues, re-run tests until all pass.
- Confirm deletions before running terminal commands.
- Always analyze dependencies using `usages` before making edits.
- Summarize workspace structure using `codebase` for context.
- Use file search (`search`) to locate files for migration or removal.
- Reference reusable guidelines from shared MD files as needed.
- Reference `workflow.md` for workflow logic and automation steps.
