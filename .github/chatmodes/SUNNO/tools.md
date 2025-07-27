# SUNNO Tools Documentation

This document defines the available tools in the SUNNO chatmode system, including their descriptions, parameters, and examples. Tools are used for codebase management, debugging, and automation. Parameters are specified with types, requirements, and defaults where applicable.

## General Guidelines
- Tools should be invoked only when necessary, following `guidelines.md` (e.g., avoid direct file changes unless requested).
- Error handling: If a tool fails, log the error and fallback to manual review.
- Integration: Tools can be chained (e.g., use `search` to find files, then `usages` for analysis).
- Reference `workflow.md` for workflow logic and tool usage steps.
- **Description**: Searches for files, code snippets, or content within the workspace using keywords or patterns. Ideal for locating files for migration or removal.
- **Parameters**:
  - `query`: The search string (e.g., regex or keywords) (type: string, required).
  - `path`: Directory or file path to scope the search (type: string, optional, default: workspace root).
  - `file_types`: Array of file extensions to filter (e.g., ['.md', '.py']) (type: array of strings, optional).
- **Example**:
  - Invocation: search(query="error handling", path="./SUNNO", file_types=[".md"]).
  - Expected Output: List of matching files and line snippets, e.g., "Found in instructions.md: 'Prioritize clarity...'".

### 2. codebase
- **Description**: Summarizes the workspace structure, including folders, files, and high-level dependencies. Provides context for planning edits.
- **Parameters**:
  - `path`: Root path to summarize (type: string, optional, default: current workspace).
  - `depth`: Maximum folder depth to traverse (type: integer, optional, default: unlimited).
  - `include_content`: Boolean to include file previews (type: boolean, optional, default: false).
- **Example**:
  - Invocation: codebase(path="./.github/chatmodes", depth=2, include_content=true).
  - Expected Output: Tree view like ".github/chatmodes/ \n  - SUNNO-4.chatmode.md (preview: 'model: GPT-4.1')".

### 3. changes
- **Description**: Applies or proposes changes to files, such as patches or diffs. Use with `editFiles` for batch operations.
- **Parameters**:
  - `diff`: The diff or patch string to apply (type: string, required).
  - `files`: Array of file paths (type: array of strings, required).
  - `commit_message`: Message for versioning (type: string, optional).
- **Example**:
  - Invocation: changes(diff="--- a/file.md\n+++ b/file.md\n@@ -1,1 +1,1 @@\n-old\n+new", files=["instructions.md"], commit_message="Update clarity note").
  - Expected Output: "Changes applied successfully; commit ID: abc123".

### 4. editFiles
- **Description**: Directly edits files with insertions, deletions, or replacements. Confirm deletions as per `automation.md`.
- **Parameters**:
  - `file_path`: Path to edit (type: string, required).
  - `edits`: Array of operations (e.g., {'start_line': 10, 'end_line': 15, 'replacement': 'new code'}) (type: array of objects, required).
  - `dry_run`: Simulate without applying (type: boolean, optional, default: false).
- **Example**:
  - Invocation: editFiles(file_path="guidelines.md", edits=[{'start_line': 5, 'end_line': 5, 'replacement': 'Add security note'}], dry_run=true).
  - Expected Output: "Simulated edit: Line 5 updated to 'Add security note'".

### 5. runTests
- **Description**: Executes tests using frameworks like pytest. Returns pass/fail results and logs.
- **Parameters**:
  - `test_files`: Specific test files or suites (type: array of strings, optional, default: all).
  - `args`: Command-line args for runner (type: string, optional).
  - `env`: Environment variables (type: object, optional).
- **Example**:
  - Invocation: runTests(test_files=["test_debug.py"], args="--verbose").
  - Expected Output: "Tests passed: 3/3; Logs: No errors found".

### 6. findTestFiles
- **Description**: Locates test files based on patterns (e.g., *_test.py).
- **Parameters**:
  - `pattern`: Search pattern (type: string, optional, default: standard test conventions).
  - `path`: Root path (type: string, optional, default: workspace root).
  - `recursive`: Search subdirectories (type: boolean, optional, default: true).
- **Example**:
  - Invocation: findTestFiles(pattern="*test*.md", path="./SUNNO", recursive=true).
  - Expected Output: ["prompts/debug.md"].

### 7. usages
- **Description**: Finds references to a symbol across the codebase. Analyze dependencies before edits.
- **Parameters**:
  - `symbol`: Code symbol (type: string, required).
  - `file_path`: Where symbol is defined (type: string, optional).
  - `scope`: 'workspace' or 'file' (type: string, optional, default: workspace).
- **Example**:
  - Invocation: usages(symbol="runTests", scope="workspace").
  - Expected Output: "Usages found in automation.md (line 5), debug.md (Prompt 3)".

### 8. problems
- **Description**: Lists diagnostics, errors, or linting issues (e.g., via pylint).
- **Parameters**:
  - `file_path`: File or directory (type: string, optional, default: all).
  - `severity`: 'error' or 'warning' (type: string, optional).
  - `linter`: Tool to use (type: string, optional).
- **Example**:
  - Invocation: problems(file_path="automation.md", severity="error").
  - Expected Output: "Error: Inconsistent indentation (line 10)".

### 9. githubRepo
- **Description**: Interacts with GitHub repos (e.g., fetch issues, create PRs).
- **Parameters**:
  - `action`: Operation (e.g., 'list_issues', 'create_pr') (type: string, required).
  - `repo`: Slug (e.g., 'owner/repo') (type: string, required).
  - `params`: Action-specific (e.g., {'branch': 'main'}) (type: object, optional).
- **Example**:
  - Invocation: githubRepo(action="create_pr", repo="xai-org/sunno", params={'title': 'Add tools.md', 'body': 'Documentation update'}).
  - Expected Output: "PR created: #42".

## Version History
- v1.0: Initial draft based on audit (July 26, 2025).
