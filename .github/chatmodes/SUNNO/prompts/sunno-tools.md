# VS Code Tools Effectiveness & Resilience Prompts

These prompts are designed to rigorously test every tool call defined in `.github/chatmodes/SUNNO/tools.md`, ensuring that instructions are effective and that no tool failure can halt the workflow. If any tool stops the workflow, the prompts must trigger automatic fixes and retest until all tools work reliably and the workflow is never blocked.

---

## Resilient Tool Testing & Auto-Fix Prompts

### 1. Full Tool Call Test & Recovery
- "Test every tool call defined in .github/chatmodes/SUNNO/tools.md for expected input/output and workflow continuity. If any tool fails or blocks the workflow, automatically diagnose the issue, apply a fix, and retest until the tool works and the workflow continues. Log each failure, fix, and retest result."

### 2. Workflow Blockage Detection & Resolution
- "Simulate workflow execution using all tools in .github/chatmodes/SUNNO/tools.md. If any tool invocation halts or blocks the workflow, automatically update the tool instructions or invocation pattern, then retest until the workflow proceeds without interruption. Log all blockage events and resolutions."

### 3. Instruction Effectiveness Audit
- "Audit the instructions in .github/chatmodes/SUNNO/tools.md for clarity and effectiveness. For any unclear or ineffective instruction, automatically rewrite and retest until all instructions enable reliable tool usage and workflow continuity. Log all rewrites and test results."

### 4. Persistent Tool Improvement Loop
- "Continuously run automated tests for all tools and workflow steps. If any tool or instruction fails, automatically apply fixes and retest until all tools and instructions are fully functional and resilient. Log all changes, fixes, and test results."

---

## Workflow
1. Use these prompts to initiate resilient, self-healing tool testing and improvement cycles.
2. Log all failures, fixes, and retest results.
3. Automatically update .github/chatmodes/SUNNO/tools.md and related files after each successful fix or improvement.
4. Retest after every change; repeat until all tools and workflows are fully functional and cannot be blocked by tool failures.

---

## Example Automation Prompt
- "Run all resilient tool testing prompts in this file. For every tool or instruction failure, automatically apply fixes and retest until all tools and workflows are robust and unbreakable. Log all changes, fixes, and test results."

---

*Add additional prompts below to expand the resilience and effectiveness testing suite.*
