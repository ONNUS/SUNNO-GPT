# SUNNO-GPT

SUNNO (Structured Unified Neural Network Operations) is a modular AI agent framework designed for GitHub Copilot Chat Modes. It provides intelligent automation for debugging, code review, testing, and collaborative workflows with built-in security, logging, and sidekick collaboration features.

## Features

- 🤖 Multi-Model Support: Compatible with GPT-4.1 and GPT-4o
- 🔧 Advanced Tool Integration: File editing, testing, code analysis, and GitHub operations
- 🛡️ Security-First Design: OWASP LLM compliance with automated security checks
- 🔄 Automated Workflows: Self-healing test loops and dependency analysis
- 👥 Sidekick Collaboration: Multi-agent review and feedback system
- 📊 Comprehensive Logging: Centralized audit trails and decision tracking
- 🧩 Modular Architecture: Extensible instruction system

## Quick Start

1. **Setup GitHub Copilot Chat Mode**:
   - Place the `.chatmode.md` files in your `.github/chatmodes/` directory
   - Configure your preferred model (SUNNO-4 or SUNNO-4o)

2. **Activate SUNNO**:
   ```
   @workspace Use SUNNO-4 chatmode for this session
   ```

3. **Run Diagnostics**:
   ```
   Run a full diagnostic and test all enabled tools
   ```

## Architecture

```
.github/chatmodes/
├── SUNNO-4.chatmode.md      # GPT-4.1 configuration
├── SUNNO-4o.chatmode.md     # GPT-4o configuration
└── SUNNO/                   # Modular instruction system
    ├── instructions.md      # Core instructions
    ├── workflow.md          # Collaborative workflow logic
    ├── tools.md            # Tool documentation
    ├── security.md         # OWASP LLM compliance
    ├── sidekick.md         # Multi-agent collaboration
    ├── automation.md       # Automated debugging loops
    ├── guidelines.md       # Best practices
    ├── logic.md           # Self-correction logic
    ├── _py_/              # Python utilities
    └── prompts/           # Starter prompts
```

## Core Modules

### 🔧 Tools System
- File Operations: Search, edit, analyze dependencies
- Testing: Automated test running and fix loops
- GitHub Integration: Repository operations and PR management
- Diagnostics: Problem detection and resolution

### 🛡️ Security Framework
- OWASP Top 10 LLM compliance
- Input/output sanitization
- Automated security checks
- Privilege escalation prevention

### 👥 Sidekick Collaboration
- Multi-agent review system
- Structured feedback loops
- Decision documentation
- Collaborative auditing

### 📊 Logging & Audit
- Centralized event logging
- Decision tracking
- Compliance monitoring
- Audit trail maintenance

## Usage Examples

### Automated Debugging
```
Debug the failing tests and fix all issues automatically
```

### Code Review
```
Review this pull request and suggest improvements with sidekick collaboration
```

### Security Audit
```
Run a security audit of the codebase following OWASP guidelines
```

### Workflow Testing
```
Test the complete workflow logic and report any issues
```

## Configuration

### Model Selection
- SUNNO-4: GPT-4.1 with terminal access for complex debugging
- SUNNO-4o: GPT-4o optimized for research and planning

### Tool Customization
Edit the `tools` array in the chatmode files to enable/disable specific capabilities.

## Contributing

1. Adding Features: Create new `.md` files in the `SUNNO/` folder
2. Testing: Use starter prompts in `prompts/` for validation
3. Security: Follow guidelines in `security.md`
4. Documentation: Update relevant instruction files

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- 📖 Documentation: See `SUNNO/` folder for detailed instructions
- 🐛 Issues: Use GitHub Issues for bug reports
- 💡 Feature Requests: Submit via GitHub Discussions
