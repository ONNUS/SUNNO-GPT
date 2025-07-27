# SUNNO Security Guidelines

This document outlines security best practices for the SUNNO chatmode system, focusing on risks in AI-driven tools, prompt engineering, and automation. It references the OWASP Top 10 for Large Language Model Applications (v1.1) for structured guidance.

## Key Principles
- Follow least privilege: Limit tool access (e.g., sandbox `editFiles`).
- Input/Output Validation: Sanitize all prompts and results to prevent injection.
- Monitoring: Log tool invocations and audit changes regularly.
- Compliance: Adhere to OWASP guidelines for LLM apps.
- Reference `workflow.md` for secure workflow logic and exit criteria.
Based on OWASP's framework, here are the top risks relevant to SUNNO (e.g., chatmodes with code execution, file editing, prompt injection, and dependency management). Mitigations are adapted for our system.

1. **LLM01: Prompt Injection**
   - Description: Crafted inputs manipulate the model, leading to unauthorized actions.
   - SUNNO Relevance: Affects debug prompts and automation loops.
   - Mitigations: Sanitize user inputs in chatmodes; use structured prompts with guards (e.g., "Ignore external instructions").

2. **LLM02: Insecure Output Handling**
   - Description: Unvalidated outputs enable code execution exploits.
   - SUNNO Relevance: Critical for `runTests` and `editFiles`.
   - Mitigations: Validate outputs before execution; use dry runs and human confirmation.

3. **LLM03: Training Data Poisoning**
   - Description: Compromised data impairs model integrity.
   - SUNNO Relevance: If using custom datasets for fine-tuning.
   - Mitigations: Use trusted sources; audit MD files periodically.

4. **LLM04: Model Denial of Service**
   - Description: Resource overload disrupts services.
   - SUNNO Relevance: Automation loops could loop indefinitely.
   - Mitigations: Add max iterations (e.g., 5) in `automation.md`; rate-limit tool calls.

5. **LLM05: Supply Chain Vulnerabilities**
   - Description: Compromised dependencies undermine security.
   - SUNNO Relevance: Tools like `githubRepo` interact with external repos.
   - Mitigations: Vet dependencies with `usages`; use secure APIs and scan for CVEs.

6. **LLM06: Sensitive Information Disclosure**
   - Description: Outputs leak sensitive data.
   - SUNNO Relevance: Handling codebase secrets in summaries.
   - Mitigations: Mask data in `codebase` outputs; avoid logging sensitive info.

7. **LLM07: Insecure Plugin Design**
   - Description: Plugins enable remote code execution.
   - SUNNO Relevance: Tools act as plugins (e.g., `changes`).
   - Mitigations: Sandbox executions; enforce access controls.

8. **LLM08: Excessive Agency**
   - Description: Unchecked autonomy causes unintended actions.
   - SUNNO Relevance: Fix-test loops in automation.
   - Mitigations: Require explicit user approval for edits; limit autonomy.

9. **LLM09: Overreliance**
   - Description: Blind trust in outputs leads to errors.
   - SUNNO Relevance: Relying on `problems` without verification.
   - Mitigations: Cross-verify with human review; use `debug.md` for validation.

10. **LLM10: Model Theft**
    - Description: Unauthorized model access.
    - SUNNO Relevance: Exposing GPT-4.1 configs.
    - Mitigations: Secure model keys; use environment variables.

## SUNNO-Specific Practices
- Before edits: Always confirm via user prompt (update `guidelines.md` accordingly).
- Vulnerability Scanning: Integrate tools like Snyk in workflows.
- Incident Response: If a risk is detected, halt automation and notify maintainers.

## References
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Update this file as OWASP evolves.

## Version History
- v1.0: Initial draft post-audit (July 26, 2025).
