
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


## Content Optimization Prompts

### 11. File Context Cleanup
Analyze all SUNNO instruction files (instructions.md, tools.md, logic.md, prompts.md) for redundant, unclear, or contradictory content. Automatically remove duplicate information, clarify ambiguous instructions, and consolidate related concepts. Ensure each file has a clear, focused purpose without overlap.

### 12. Instruction Clarity Audit
Review each instruction file for clarity and conciseness. Identify overly complex explanations, verbose sections, or confusing language. Automatically rewrite unclear sections to be more direct and actionable while maintaining all essential information.

### 13. Redundancy Elimination
Scan all SUNNO files to identify and eliminate redundant information. When the same concept appears in multiple files, consolidate it into the most appropriate location and add cross-references. Remove duplicate examples, repeated explanations, and overlapping workflows.

### 14. Workflow Streamlining
Analyze the documented workflows across all files and identify inefficiencies or unnecessary complexity. Simplify multi-step processes where possible, remove redundant validation steps, and optimize tool usage sequences for maximum effectiveness.

### 15. Content Hierarchy Optimization
Review the organization and structure of all instruction files. Ensure information is logically ordered, properly categorized, and easy to navigate. Reorganize sections that are out of place and improve the overall information architecture.


## Technical Validation Prompts

### 16. Language Consistency Check
Ensure consistent terminology, tone, and style across all SUNNO files. Standardize how tools are referenced, unify naming conventions, and maintain a consistent voice throughout the documentation.

### 17. Example Quality Review
Evaluate all examples in the instruction files for relevance, clarity, and usefulness. Remove outdated or confusing examples, improve unclear ones, and add missing examples for important concepts. Ensure examples directly support the learning objectives.

### 18. Cross-Reference Validation
Check all internal references between SUNNO files to ensure they're accurate and helpful. Remove broken or unnecessary cross-references, add missing ones where they would improve understanding, and ensure all referenced sections actually exist.

### 19. Content Density Optimization
Identify sections that are too dense or too sparse. Break down overwhelming paragraphs into digestible chunks, expand sections that lack necessary detail, and ensure optimal information density throughout all files.

### 20. Actionability Enhancement
Review all instructions to ensure they're actionable and specific. Convert vague guidance into concrete steps, add missing implementation details, and remove theoretical content that doesn't translate to practical actions.


## Technical Validation Prompts

### 21. Tool Reference Accuracy
Verify that all tool references in the instruction files match the actual available tools. Remove references to non-existent tools, update outdated tool names, and ensure all documented tool capabilities are current and accurate.

### 22. Workflow Validation Test
Test each documented workflow by following the exact steps described in the files. Identify steps that don't work as described, missing prerequisites, or unclear transitions between steps. Fix any workflow issues found.

### 23. Instruction Completeness Check
Ensure each instruction file covers all necessary topics for its domain. Identify missing critical information, gaps in coverage, or topics that need more depth. Add missing content where needed.


## Meta-Optimization Prompts

### 24. Documentation Effectiveness Assessment
Evaluate whether the current documentation structure effectively serves its purpose. Consider if files should be merged, split, or reorganized entirely. Assess if the four-file structure is optimal or if changes would improve usability.

### 25. Prompt System Optimization
Review this prompts.md file itself for effectiveness. Ensure prompts are well-organized, cover all necessary scenarios, and are easy to use. Remove redundant prompts and add missing ones based on actual usage patterns.


## Usage Instructions
- Use these prompts to initiate self-diagnosis and improvement cycles
- Each prompt should result in automatic fixes when issues are found
- The system should never get stuck - if unclear, make the best decision and continue
- Focus on making the chatmode more effective at its core purpose
