# SUNNO Tools Guide

This document describes how to use the available tools effectively in SUNNO chatmodes.

## Core Tools Overview

### Code Analysis Tools
- **`search`**: Find files, functions, or text patterns in the workspace
- **`codebase`**: Analyze code structure and relationships  
- **`usages`**: Find where functions/classes are used throughout the codebase
- **`problems`**: Detect syntax errors, warnings, and code issues

### File Operations  
- **`editFiles`**: Modify existing files with specific changes
- **`changes`**: View current workspace changes and diffs

### Testing & Execution
- **`runTests`**: Execute test suites and analyze results
- **`runCommands`**: Execute terminal commands when needed
- **`findTestFiles`**: Locate test files in the project

### Terminal Interaction
- **`terminalLastCommand`**: Get the last command run in terminal
- **`terminalSelection`**: Get current terminal selection

### Repository Operations
- **`githubRepo`**: Interact with GitHub repositories (PRs, issues, etc.)

## Usage Best Practices

### 1. Start with Analysis
Before making changes, use `search`, `codebase`, and `problems` to understand the current state:
- `search` to locate relevant files
- `codebase` to understand code structure
- `problems` to identify existing issues

### 2. Use Tool Combinations Strategically
**For Code Understanding:**
- `codebase` + `search` + `usages` = Complete picture of code relationships
- `problems` + `changes` = Current state assessment

**For Problem Solving:**
- `problems` → `search` → `usages` → `editFiles` → `runTests`
- Always verify with `problems` after changes

**For Quality Assurance:**
- `changes` + `usages` + `runTests` = Impact assessment
- `findTestFiles` + `runTests` = Comprehensive validation

### 3. Efficient Tool Sequencing
- Combine related operations rather than making many small tool calls
- Use `usages` before modifying functions to understand impact
- Run `problems` after changes to verify fixes
- Leverage `terminalLastCommand` and `terminalSelection` for context awareness

### 4. Error Recovery
If a tool fails or gives unexpected results:
- Try an alternative approach with different tools
- Use `search` as a fallback when specialized tools don't work
- Continue with the task rather than getting blocked

## Common Workflows

### Debugging Workflow
1. `problems` - Identify issues
2. `search` - Find related code 
3. `editFiles` - Apply fixes
4. `runTests` - Verify fixes work
5. Repeat until resolved

### Code Review Workflow  
1. `changes` - See what's been modified
2. `usages` - Check impact of changes
3. `problems` - Look for new issues
4. `runTests` - Ensure tests still pass

### Feature Development Workflow
1. `search` - Find relevant existing code
2. `codebase` - Understand current structure
3. `editFiles` - Implement changes
4. `findTestFiles` + `runTests` - Verify functionality

## Tool Failure Handling
When tools fail or give unexpected results:
- **Immediate Fallback**: Switch to alternative tools automatically (e.g., `grep_search` when `search` fails)
- **Error Analysis**: Quickly determine if the failure is tool-specific or systemic
- **Adaptive Strategy**: Adjust approach based on available tools and context
- **Continue Mission**: Never let tool failures block the user's primary objective
- **Self-Diagnosis**: If multiple tools fail, trigger self-diagnosis from `logic.md` protocols

### Common Tool Issues & Solutions
**Tool Not Available:**
- `search` not working → Use `grep_search` with pattern matching
- `usages` returns empty → Use `grep_search` to find references in comments/docs
- `runTests` fails → Use `problems` to identify specific issues first

**Tool Returns Unexpected Results:**
- Verify the tool name and parameters are correct
- Check if the workspace context has changed
- Apply alternative tool combinations for verification

Focus on solving the user's problem rather than perfect tool usage. The goal is effective assistance, not tool mastery.
