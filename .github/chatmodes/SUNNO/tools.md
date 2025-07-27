# SUNNO Tools Documentation (Revised)

# SUNNO Tools Documentation (edited)


> **Compliance Reminder:**
> After any change to this file, immediately audit and test all workflow, instruction, and prompt files as specified in logic.md. Document audit results and ensure workflow continuity.

This document defines the available tools in the SUNNO chatmode system, including their descriptions, parameters, and examples. For file operations (create, edit, delete, move, copy), use VS Code API tools when available. If unavailable or insufficient, use terminal commands. Always log the tool or command used and its result for audit and compliance.
## Audit Findings & Guidance (2025-07-27)

SUNNO tools are designed to use both VS Code APIs and terminal commands, depending on feature and environment. Terminal commands are required for some file operations, but VS Code tools (API-based) are preferred for search, code analysis, and diagnostics. Do not install new packages or tools unless you have explicitly prompted the user and received approval. If a required feature cannot be performed with available VS Code tools, always prompt the user for approval before installing any package, tool, or running external commands. The user must control what is added to the repo.


**Best Practice:**
- Prefer VS Code tools for file listing, search, code usage, and diagnostics.
- Use terminal commands only when VS Code tools cannot perform the required file operation.
- For test running, use VS Code's built-in Python/Test Runner if available; otherwise, prompt the user before installing packages (e.g., pytest).
- Log every tool invocation and terminal command, including the result, for audit and compliance.


**If a tool or workflow is blocked:**
- Attempt all available VS Code tool options first.
- If no solution is possible, prompt the user for approval to install packages or run external commands.


**Example:**
- If 'pytest' is missing, prompt: "Pytest is not installed. Would you like to install it to enable test running?"


## General Guidelines
- Use VS Code tools for file search, code analysis, and diagnostics where possible.
- Use terminal commands for file changes only if VS Code tools cannot perform the required operation.
- Log all actions (VS Code tool or terminal) and their results for compliance and audit.
- Reference `workflow.md` for usage patterns and escalation logic.

### 2. codebase
  - `symbol`: Code symbol (function, class, variable; type: string, required). Only finds code symbols, not markdown references.
  - `file_path`: Where symbol is defined (type: string, optional).
  - `scope`: 'workspace' or 'file' (type: string, optional, default: workspace).
  - Invocation: usages(symbol="runTests", scope="workspace") using VS Code semantic search tools.
  - Expected Output: "Usages found in automation.py (line 5)" or similar output. If symbol is not found, log the result and escalate per workflow.md.
- **Example**:
**Description**: Executes tests using VS Code's built-in test runner if available. If no runner is available or the test file is not supported, log the result and escalate per workflow.md. If not, prompt the user before installing or running external test frameworks (e.g., pytest). Returns pass/fail results and logs.
  - Expected Output: Directory and file list using VS Code tools (e.g., list_dir, file_search).
  - `severity`: 'error' or 'warning' (type: string, optional).
  - `linter`: Tool to use (type: string, optional).
**Example**:
  - Invocation: problems(file_path="automation.md", severity="error") using VS Code grep_search or get_errors tools.
  - Expected Output: List of errors or warnings found, or "No errors found". Always log results for audit.

### 9. githubRepo
**Description**: Interacts with GitHub repos (e.g., fetch issues, create PRs) using VS Code GitHub integration if available. If unavailable, log the result and escalate per workflow.md.
**Parameters**:
  - `action`: Operation (e.g., 'list_issues', 'create_pr') (type: string, required).
  - `repo`: Slug (e.g., 'owner/repo') (type: string, required).
  - `params`: Additional parameters for the action (type: object, optional).
  - Invocation: githubRepo(action="create_pr", repo="xai-org/sunno", params={'title': 'Add tools.md', 'body': 'Documentation update'}) using VS Code GitHub tools or prompt user for approval if unavailable.
  - Expected Output: "PR created: #42" or prompt for user approval if required. Always log actions and results for audit.
  - Invocation: Use VS Code file edit tools for supported operations. If blocked, run_in_terminal(command="sed -i '' '5s/.*/Add security note/' guidelines.md", explanation="Update line 5 in guidelines.md", isBackground=false).
* Use VS Code tools for file search, code analysis, and diagnostics where possible.
* Use terminal commands for file changes only if VS Code tools cannot perform the required operation.
* Log all actions (VS Code tool or terminal) and their results for compliance and audit.
* Always validate output of terminal commands and log any errors or unexpected results.
* Reference `workflow.md` for usage patterns and escalation logic.
- **Parameters**:
  - `test_files`: Specific test files or suites (type: array of strings, optional, default: all).
  - `args`: Command-line args for runner (type: string, optional).
  - `env`: Environment variables (type: object, optional).
- **Example**:
  - Invocation: runTests(test_files=["test_debug.py"], args="--verbose").
  - Expected Output: "Tests passed: 3/3; Logs: No errors found" or prompt for package installation if required.

### 6. findTestFiles
-  - `pattern`: Search pattern (type: string, optional, default: standard test conventions).
  - `path`: Root path (type: string, optional, default: workspace root).
  - `recursive`: Search subdirectories (type: boolean, optional, default: true).
  - Invocation: findTestFiles(pattern="*test*.md", path="./SUNNO", recursive=true) using VS Code file search tools.
  - Expected Output: ["prompts/diagnostic.md"] or empty if no matches.

### 7. usages
-  - `symbol`: Code symbol (type: string, required).
  - `file_path`: Where symbol is defined (type: string, optional).
  - `scope`: 'workspace' or 'file' (type: string, optional, default: workspace).
  - Invocation: usages(symbol="runTests", scope="workspace") using VS Code semantic search tools.
  - Expected Output: "Usages found in automation.md (line 5), diagnostic.md (Prompt 3)" or similar output.

### 8. problems
-  - `severity`: 'error' or 'warning' (type: string, optional).
  - `linter`: Tool to use (type: string, optional).
- **Example**:
  - Invocation: problems(file_path="automation.md", severity="error") using VS Code grep_search or get_errors tools.
- **Description**: Interacts with GitHub repos (e.g., fetch issues, create PRs) using VS Code GitHub integration if available.
- **Parameters**:
  - `action`: Operation (e.g., 'list_issues', 'create_pr') (type: string, required).
  - `repo`: Slug (e.g., 'owner/repo') (type: string, required).
  - Invocation: githubRepo(action="create_pr", repo="xai-org/sunno", params={'title': 'Add tools.md', 'body': 'Documentation update'}) using VS Code GitHub tools or prompt user for approval if unavailable.
  - Expected Output: "PR created: #42" or prompt for user approval if required.


## Patch & Edit Protocol
- For documentation and logic changes in SUNNO chatmode markdown files, use the insert_edit_into_file tool. For code changes, use the apply_patch tool. Choose the tool that best matches the file type and change required.
- If tools.md guidance conflicts with logic.md protocols, logic.md must attempt autonomous resolution or document a workaround, ensuring workflow continuity. Tools.md should guide tool usage but must not block logic.md from finding or implementing a solution.

## Version History
- v1.0: Initial draft based on audit (July 26, 2025).
- v1.1: Updated to require terminal-only file operations (July 27, 2025).
