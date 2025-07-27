# SUNNO Self-Diagnosis & Fix Starter Prompts

These prompts focus on automatically diagnosing and fixing issues with the SUNNO chatmode system itself.


## Core Self-Diagnosis Prompts

### 1. System Health Check
Run a complete system diagnostic of the SUNNO chatmode. Check if all core files (instructions.md, tools.md, logic.md) are accessible and working. Test each enabled tool with a simple action. Report any issues found and automatically fix them.

### 2. Chatmode Logic Audit  
Audit the logic in the SUNNO chatmode instructions. Look for contradictions, unclear instructions, or missing workflows. If problems are found, automatically refine the logic and retest until the chatmode works reliably.

### 3. Tool Functionality Test
Test every tool listed in tools.md to ensure it works as expected. For any broken or ineffective tools, automatically fix the tool usage instructions and retest until all tools function properly.

### 4. Self-Improvement Loop
Analyze the current SUNNO chatmode performance. Identify areas where instructions could be clearer or more effective. Automatically implement improvements and test the changes to ensure better results.

### 5. Issue Resolution Protocol
When you encounter any error or unclear instruction while using SUNNO, automatically diagnose the root cause, fix the underlying instruction file, and retest to confirm the fix works.


## Development Workflow Prompts

### 6. Debug Session
Start a debugging session. Analyze the current code for errors, run tests, fix any issues found, and retest until all problems are resolved.

### 7. Code Review
Review the current changes in the workspace. Check for code quality, security issues, and best practices. Suggest and implement improvements automatically.

### 8. Test & Fix Loop
Run all available tests. For any failures, automatically diagnose the issue, implement a fix, and rerun tests until everything passes.


## Performance Validation Prompts

### 9. Effectiveness Assessment
Evaluate the quality of your recent responses. Check if solutions actually solved the problems, if reasoning was clear, and if tool usage was optimal. Implement improvements based on findings.

### 10. Workflow Optimization
Analyze your recent tool usage patterns. Identify inefficiencies, missed opportunities for tool combinations, and optimize your approach for better results.


## Usage Instructions
- Use these prompts to initiate self-diagnosis and improvement cycles
- Each prompt should result in automatic fixes when issues are found
- The system should never get stuck - if unclear, make the best decision and continue
- Focus on making the chatmode more effective at its core purpose
