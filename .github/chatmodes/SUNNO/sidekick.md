# Sidekick Instructions

These instructions enable SUNNO agents to collaborate with sidekick AI agents for research, code review, thorough audits, and workflow logic. Sidekick mode improves solution quality, encourages diverse perspectives, and supports continuous improvement.

## Output Format for Sidekick Mode
- All messages to the sidekick agent must be generated inside a markdown code block (triple backticks) as plain text.
- The content inside the code block should be easy to copy and paste, with no extra formatting or markdown except the code block itself.
- This ensures a clear workflow: copy the message from the markdown box, paste it into the sidekick, and copy the response back.

**Example:**
```
Sidekick, please research the latest best practices for X.
Summarize findings and cite sources.
```

## Sidekick Guidelines
  - Research relevant topics, libraries, or best practices.
  - Review SUNNO's thought process and suggest improvements.
  - Audit code, documentation, or workflows for completeness and quality.
SUNNO should integrate sidekick feedback, clearly noting which suggestions were adopted or rejected and why.
Collaboration should be transparent, with all agent contributions documented in the output.
SUNNO should avoid redundant or conflicting instructions and ensure all sidekick actions are relevant to the current task.

## Automated Sidekick Prompt & Logging
At key decision points, SUNNO agents must use the script `_py_/sidekick/prompt.py` to:
  - Generate a markdown code block prompt for sidekick review (using `generate_sidekick_prompt`).
  - Log the prompt and sidekick response (using `log_sidekick_event`).
  - Store logs in `_py_/sidekick/logs/YYYYMMDD.md` for audit and compliance.

**Example usage:**
```python
from ._py_.sidekick.prompt import generate_sidekick_prompt, log_sidekick_event
prompt = generate_sidekick_prompt(context, decision, questions)
# Send prompt to sidekick, receive response
log_sidekick_event("SUNNO-Agent", "Review", prompt, response)
```

## Example Prompts
- "Sidekick, please research the latest best practices for X."
- "Review my proposed solution and suggest improvements."
- "Audit this workflow for security and efficiency."

## Maintenance
- Sidekick instructions should be updated as new collaboration patterns or agent capabilities emerge.
- All SUNNO chat mode markdown files must reference this file to enable sidekick features.
- Reference `workflow.md` for collaborative workflow logic and decision-making steps.
