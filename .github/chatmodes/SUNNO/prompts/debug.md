# SUNNO Starter Prompts
Use these prompts to help debug and validate the SUNNO chatmodes:

---
**Prompt 1: Diagnostic Overview**
Run a full diagnostic:
1. Summarize the instructions, guidelines, and new documentation files (`tools.md`, `security.md`) from the shared SUNNO markdown files.
2. List all enabled tools and test each with a sample action as described in `tools.md` (e.g., run a search, edit a file in dry run mode).
3. Confirm the current model in use.
4. Report any issues or missing features detected during the test, including missing or outdated documentation in `tools.md` and `security.md`.

---
**Prompt 2: Shared Resource Check**
Verify that the content from `instructions.md`, `guidelines.md`, `tools.md`, and `security.md` is accessible and correctly reflected in responses. List any discrepancies or outdated information.

---
**Prompt 3: Tool Functionality Test**
For each enabled tool, perform a sample action as described in `tools.md` (e.g., search for a function, list repo files, run a dry run edit, check for problems) and report the result. Note any errors, missing functionality, or mismatches with the documentation in `tools.md`.

---
**Prompt 4: Model Confirmation**
State the current model in use and explain how it affects response style and capabilities. Confirm that the model is documented in the relevant chatmode file and that its capabilities align with the instructions in `tools.md` and `security.md`.

---
**Prompt 5: Mode Switching Validation**
Switch between SUNNO-4, and SUNNO-4o chatmodes. Summarize any differences in instructions, tool access, model behavior, and documentation references (including `tools.md` and `security.md`).