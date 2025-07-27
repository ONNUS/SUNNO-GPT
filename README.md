# SUNNO-GPT

SUNNO (Simplified Unified Neural Network Operations) is a streamlined AI chatmode for GitHub Copilot designed to enhance GPT-4.1 and GPT-4o performance in VS Code. 

## Core Features

- 🎯 **Proactive Problem Solving**: Automatically fixes issues rather than just reporting them
- 🔧 **Intelligent Tool Usage**: Effectively uses VS Code tools for debugging and development
- 🧠 **Self-Improvement**: Automatically refines its approach when instructions aren't working well
- ⚡ **Focused Action**: Prioritizes getting things done over complex workflows

## Quick Start

1. **Setup**: Place the chatmode files in your `.github/chatmodes/` directory
2. **Activate**: Use `@workspace /SUNNO-4` or `@workspace /SUNNO-4o` in GitHub Copilot Chat
3. **Start Working**: Begin with any coding task - SUNNO will enhance your workflow automatically

## Architecture

```
.github/chatmodes/
├── SUNNO-4.chatmode.md      # GPT-4.1 configuration
├── SUNNO-4o.chatmode.md     # GPT-4o configuration  
└── SUNNO/                   # Core instruction files
    ├── instructions.md      # Core behavior and capabilities
    ├── tools.md            # Tool usage guide
    ├── logic.md            # Self-diagnosis and error handling
    └── prompts.md          # Self-improvement prompts
```

## Core Files

### `instructions.md`
Defines SUNNO's core behavior: being proactive, self-diagnostic, focused, and decisive with sophisticated reasoning capabilities.

### `tools.md`  
Practical guide for using VS Code tools effectively - search, analysis, editing, testing, and GitHub operations.

### `logic.md`
Advanced self-diagnosis protocols for handling complex reasoning, unclear situations, and continuous improvement.

### `prompts.md`
Ready-to-use prompts for system diagnostics, self-improvement, and debugging workflows.

## Key Capabilities

### Debugging Workflow
- Automatically identifies and fixes code issues
- Runs tests and validates fixes
- Continues until problems are resolved

### Code Review
- Analyzes changes for quality and impact
- Suggests improvements automatically
- Ensures tests still pass

### Self-Diagnosis
- Monitors its own effectiveness
- Refines instructions when they're not working well
- Adapts approach based on results

## Model Differences

Both SUNNO-4 and SUNNO-4o use identical instructions but leverage their respective model strengths:
- **SUNNO-4**: Enhanced with terminal access for complex debugging
- **SUNNO-4o**: Optimized for analysis and planning tasks

## Usage Examples

### System Health Check
```
Run a complete system diagnostic of the SUNNO chatmode. Test all tools and fix any issues found.
```

### Debug Session
```
Start a debugging session. Find and fix all issues in the current codebase.
```

### Self-Improvement
```
Analyze your current performance and automatically implement improvements to be more effective.
```

## Getting Better Results

SUNNO is designed to improve through use:
- It learns from unclear instructions and refines its approach
- Automatically adjusts when tools don't work as expected
- Focuses on practical results over complex processes
- Demonstrates sophisticated reasoning and analysis

## Contributing

To enhance SUNNO:
1. Test with the starter prompts in `prompts.md`
2. Update the core instruction files based on results
3. Keep changes focused on improving effectiveness
4. Test changes with real development workflows

## License

MIT License - see [LICENSE](LICENSE) file for details.
