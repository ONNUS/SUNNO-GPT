
# SUNNO Diagnostic & Improvement Prompts
Use these prompts to run comprehensive diagnostics and drive continuous improvements across the SUNNO system:

---
**Prompt 1: System Diagnostic, Auto-Improvement & Audit**
Run a full system diagnostic:
1. Summarize all instructions, guidelines, and documentation modules (`tools.md`, `security.md`, etc.).
2. List all enabled tools and test each with a sample action (search, dry run edit, etc.).
3. Confirm the current model and its configuration.
4. Identify issues, missing features, or outdated documentation.
5. Automatically implement improvements to close gaps or enhance workflows (e.g., create missing test files, update documentation, add log hooks).
6. After making improvements, automatically run relevant tests and audits to verify changes.

---
**Prompt 2: Resource Consistency & Update Check**
Verify that all referenced resources (`instructions.md`, `guidelines.md`, `tools.md`, `security.md`) are accessible, up-to-date, and correctly reflected in responses. List discrepancies, automatically refactor or update as needed, and re-test to confirm resolution.

---
**Prompt 3: Tool Functionality, Enhancement & Auto-Test**
For each enabled tool, perform a sample action as described in `tools.md` (search, repo listing, dry run edit, problem check). If errors or missing functionality are detected, automatically implement suggested improvements or new tool features, then re-run the tool to verify the fix.

---
**Prompt 4: Model & Capability Confirmation**
State the current model in use, explain its impact on response style and capabilities, and confirm alignment with documentation. If configuration or documentation improvements are needed, automatically apply them and re-test for compliance.

---
**Prompt 5: Mode Switching & Comparative Audit**
Switch between SUNNO-4 and SUNNO-4o chatmodes. Summarize differences in instructions, tool access, model behavior, and documentation. Automatically implement improvements for consistency and feature parity, then re-audit and test both modes.
